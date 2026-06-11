import feedparser
import LaTexAccents as TeX
import re
import os
import sys
import yaml
from datetime import date, timedelta
from pathlib import Path

from llm_utils import build_interest_profile, score_and_summarize


FEED_URLS = [
    'https://rss.arxiv.org/rss/stat.ME',
    'https://rss.arxiv.org/rss/stat.CO',
    'https://rss.arxiv.org/rss/stat.AP',
]
MODEL = "meta/llama-3.1-8b-instruct"
POSTS_DIR = Path("_posts")
PREFS_FILE = Path("preferences.yml")
RETENTION_DAYS = 7

today = date.today()
converter = TeX.AccentConverter()


def load_yaml(path, default=None):
    try:
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f) or (default if default is not None else {})
    except FileNotFoundError:
        return default if default is not None else {}


def clean_author(name):
    name = re.sub(r'\([^)]*\)', '', name)
    return converter.decode_Tex_Accents(name, utf8_or_ascii=1).strip()


def trim_authors(author_str, max_shown=5):
    """Return (full_str, display_str). If >max_shown authors, show first 4 + last."""
    authors = [a.strip() for a in author_str.split(',') if a.strip()]
    if len(authors) <= max_shown:
        return author_str, author_str
    display = ', '.join(authors[:4]) + ', …, ' + authors[-1]
    return author_str, display


def clean_title(title):
    return converter.decode_Tex_Accents(title, utf8_or_ascii=1)


def extract_abstract(summary_html):
    text = re.sub(r'<[^>]+>', ' ', summary_html)
    text = re.sub(r'\s+', ' ', text).strip()
    match = re.search(r'Abstract[:\s]+(.+)', text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else text


def extract_arxiv_id(link):
    match = re.search(r'arxiv\.org/abs/([^\s?#/]+)', link)
    if match:
        return match.group(1)
    return re.sub(r'[^a-zA-Z0-9.]', '', link)[-20:]


def fetch_articles():
    seen_ids = set()
    articles = []
    for url in FEED_URLS:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                arxiv_id = extract_arxiv_id(entry.link)
                if arxiv_id in seen_ids:
                    continue
                seen_ids.add(arxiv_id)
                full_author, display_author = trim_authors(
                    clean_author(entry.get('author', ''))
                )
                articles.append({
                    'arxiv_id': arxiv_id,
                    'title': clean_title(entry.title),
                    'author': full_author,
                    'author_display': display_author,
                    'abstract': extract_abstract(entry.summary),
                    'link': entry.link,
                    'tags': [t['term'] for t in entry.get('tags', []) if 'stat' in t['term']],
                })
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    return articles


def keyword_boost(article, preferences):
    text = (article['title'] + ' ' + article['abstract']).lower()
    keywords = preferences.get('keywords', [])
    authors = preferences.get('authors', [])
    kw_hits = sum(1 for kw in keywords if kw.lower() in text)
    au_hits = sum(1 for au in authors if au.lower() in article['author'].lower())
    return min(kw_hits * 0.5, 2.0), min(au_hits * 1.0, 2.0)



def badge(score):
    if score >= 7:
        return 'high'
    if score >= 4:
        return 'medium'
    return 'low'


def write_post(article):
    filename = POSTS_DIR / f"{today}-{article['arxiv_id']}.md"
    frontmatter = {
        'layout': 'post',
        'title': article['title'],
        'date': str(today),
        'author': article['author'],
        'author_display': article.get('author_display', article['author']),
        'tags': article['tags'],
        'arxiv_id': article['arxiv_id'],
        'score': round(article['score'], 2),
        'badge': article['badge'],
        'summary': article.get('summary', ''),
    }
    fm = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    body = f"---\n{fm}---\n\n{article['abstract']}\n\n[Read full paper]({article['link']})\n"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(body)


def purge_old_posts():
    cutoff = today - timedelta(days=RETENTION_DAYS)
    for f in POSTS_DIR.glob("*.md"):
        try:
            if date.fromisoformat(f.name[:10]) < cutoff:
                f.unlink()
                print(f"Purged: {f.name}")
        except ValueError:
            pass


def main():
    preferences = load_yaml(PREFS_FILE)

    print("Fetching articles...", flush=True)
    articles = fetch_articles()
    print(f"Fetched {len(articles)} unique articles", flush=True)

    if not articles:
        print("No articles found — keeping existing posts", flush=True)
        return

    interest_profile = build_interest_profile(preferences)
    api_key = os.environ.get('NVIDIA_API_KEY', '')
    llm_available = bool(api_key)
    client = None

    if llm_available:
        try:
            from openai import OpenAI
            client = OpenAI(
                base_url="https://integrate.api.nvidia.com/v1",
                api_key=api_key,
            )
        except Exception as e:
            print(f"LLM client init failed: {e}", flush=True)
            llm_available = False

    def score_article(article):
        kw, au = keyword_boost(article, preferences)
        if llm_available and client:
            try:
                result = score_and_summarize(article, interest_profile, client, MODEL)
                llm_score = float(result['score'])
                article['summary'] = result['summary']
            except Exception as e:
                print(f"LLM failed for {article['arxiv_id']}: {e} — keyword fallback", flush=True)
                llm_score = (kw + au) * 2.5
                article['summary'] = ''
        else:
            llm_score = (kw + au) * 2.5
            article['summary'] = ''
        article['score'] = max(0.0, min(10.0, llm_score + kw + au))
        article['badge'] = badge(article['score'])
        print(f"  [{article['arxiv_id']}] score={article['score']:.1f} badge={article['badge']}", flush=True)
        return article

    print(f"Scoring {len(articles)} articles...", flush=True)
    for article in articles:
        score_article(article)

    articles.sort(key=lambda x: x['score'], reverse=True)

    POSTS_DIR.mkdir(exist_ok=True)
    print(f"Writing {len(articles)} posts...", flush=True)
    for article in articles:
        write_post(article)

    purge_old_posts()
    print("Done.", flush=True)


if __name__ == "__main__":
    main()
