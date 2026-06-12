#!/usr/bin/env python3
"""
Backfill _posts/ for the current week (Mon–today) using the arXiv API.
Run from the repo root with the NVIDIA_API_KEY env var set if you want LLM scoring.
"""

import os
import re
import sys
import yaml
import time
import requests
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path

from rss_arxiv import (
    clean_author, trim_authors, clean_title,
    keyword_boost, badge, load_yaml,
    POSTS_DIR, PREFS_FILE, MODEL,
)
from llm_utils import build_interest_profile, score_and_summarize

ARXIV_API = "https://export.arxiv.org/api/query"
CATEGORIES = ["stat.ME", "stat.CO", "stat.AP"]
NS = {
    'atom': 'http://www.w3.org/2005/Atom',
    'arxiv': 'http://arxiv.org/schemas/atom',
}


def fetch_arxiv_api(start_date, end_date, max_results=500):
    # Go back 14 days before start to catch Monday papers (submitted previous week)
    query_start = (start_date - timedelta(days=14)).strftime("%Y%m%d") + "000000"
    query_end = end_date.strftime("%Y%m%d") + "235959"
    cat_query = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    search_query = f"({cat_query}) AND submittedDate:[{query_start} TO {query_end}]"
    params = {
        "search_query": search_query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    }
    resp = requests.get(ARXIV_API, params=params, timeout=30)
    resp.raise_for_status()
    return resp.text


def parse_entries(xml_text, target_dates):
    root = ET.fromstring(xml_text)
    seen_ids = set()
    papers_by_date = {d: [] for d in target_dates}

    for entry in root.findall('atom:entry', NS):
        id_elem = entry.find('atom:id', NS)
        if id_elem is None:
            continue

        arxiv_id = re.sub(r'v\d+$', '', id_elem.text.strip().split('/abs/')[-1])
        if arxiv_id in seen_ids:
            continue
        seen_ids.add(arxiv_id)

        published_elem = entry.find('atom:published', NS)
        if published_elem is None:
            continue
        announced_date = date.fromisoformat(published_elem.text.strip()[:10])
        if announced_date not in target_dates:
            continue

        title_elem = entry.find('atom:title', NS)
        title = re.sub(r'\s+', ' ', title_elem.text.strip()) if title_elem is not None else ''

        authors = []
        for author in entry.findall('atom:author', NS):
            name_elem = author.find('atom:name', NS)
            if name_elem is not None:
                authors.append(name_elem.text.strip())

        summary_elem = entry.find('atom:summary', NS)
        abstract = re.sub(r'\s+', ' ', summary_elem.text.strip()) if summary_elem is not None else ''

        tags = [
            cat.get('term', '')
            for cat in entry.findall('atom:category', NS)
            if 'stat' in cat.get('term', '')
        ]

        full_author, display_author = trim_authors(clean_author(', '.join(authors)))

        papers_by_date[announced_date].append({
            'arxiv_id': arxiv_id,
            'title': clean_title(title),
            'author': full_author,
            'author_display': display_author,
            'abstract': abstract,
            'link': f"https://arxiv.org/abs/{arxiv_id}",
            'tags': tags,
        })

    return papers_by_date


def post_exists(arxiv_id):
    return bool(list(POSTS_DIR.glob(f"*-{arxiv_id}.md")))


def write_post_for_date(article, post_date, force=False):
    POSTS_DIR.mkdir(exist_ok=True)
    filename = POSTS_DIR / f"{post_date}-{article['arxiv_id']}.md"
    if not force and post_exists(article['arxiv_id']):
        print(f"  skip  {article['arxiv_id']} (already posted under another date)", flush=True)
        return
    frontmatter = {
        'layout': 'post',
        'title': article['title'],
        'date': str(post_date),
        'author': article['author'],
        'author_display': article.get('author_display', article['author']),
        'tags': article['tags'],
        'arxiv_id': article['arxiv_id'],
        'score': round(article['score'], 2),
        'badge': article['badge'],
        'summary': article.get('summary', ''),
    }
    fm = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"---\n{fm}---\n\n{article['abstract']}\n")
    print(f"  wrote {filename.name}", flush=True)


def main():
    force = '--force' in sys.argv
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    target_dates = set()
    d = monday
    while d <= today:
        if d.weekday() < 5:
            target_dates.add(d)
        d += timedelta(days=1)

    print(f"Backfilling {sorted(target_dates)}", flush=True)

    preferences = load_yaml(PREFS_FILE)
    interest_profile = build_interest_profile(preferences)

    api_key = os.environ.get('NVIDIA_API_KEY', '')
    llm_available = bool(api_key)
    client = None
    if llm_available:
        try:
            from openai import OpenAI
            client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=api_key)
            print("LLM scoring enabled.", flush=True)
        except Exception as e:
            print(f"LLM init failed: {e} — keyword fallback", flush=True)
            llm_available = False
    else:
        print("No NVIDIA_API_KEY — keyword fallback scoring.", flush=True)

    print("Querying arXiv API ...", flush=True)
    xml_text = fetch_arxiv_api(monday, today)
    papers_by_date = parse_entries(xml_text, target_dates)

    total = sum(len(v) for v in papers_by_date.values())
    print(f"Found {total} papers across {len(target_dates)} days.", flush=True)

    for post_date in sorted(target_dates):
        papers = papers_by_date[post_date]
        print(f"\n--- {post_date} ({len(papers)} papers) ---", flush=True)
        for article in papers:
            kw, au = keyword_boost(article, preferences)
            if llm_available and client:
                try:
                    result = score_and_summarize(article, interest_profile, client, MODEL)
                    article['score'] = max(0.0, min(10.0, float(result['score']) + kw + au))
                    article['summary'] = result['summary']
                except Exception as e:
                    print(f"  LLM failed {article['arxiv_id']}: {e}", flush=True)
                    article['score'] = max(0.0, min(10.0, (kw + au) * 2.5))
                    article['summary'] = ''
            else:
                article['score'] = max(0.0, min(10.0, (kw + au) * 2.5))
                article['summary'] = ''
            article['badge'] = badge(article['score'])
            print(f"  [{article['arxiv_id']}] score={article['score']:.1f} badge={article['badge']}", flush=True)
            write_post_for_date(article, post_date, force=force)

    print("\nDone.", flush=True)


if __name__ == "__main__":
    main()
