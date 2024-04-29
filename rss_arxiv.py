import feedparser
import LaTexAccents as TeX
from collections import defaultdict
import re
import os
from datetime import date


# Debug: file locale (non ci sono rss sabato e domenica)
debug = False

# Aggiungi anche statML e statTH
all_stat_feeds = False

today = date.today()
converter = TeX.AccentConverter()

feed_urls = [
        'https://rss.arxiv.org/rss/stat.ME',
        'https://rss.arxiv.org/rss/stat.CO',
        'https://rss.arxiv.org/rss/stat.AP'
        ]

if(all_stat_feeds):
    feed_urls = ['https://rss.arxiv.org/rss/stat']

if(debug): 
    feed_urls = [r'./test.xml']

def clean_author_name(name):
    nn = re.sub(r'\([^)]*\)', '', name)
    nn = converter.decode_Tex_Accents(nn, utf8_or_ascii=1)
    # nn = re.sub("[^\w ,']*",'', nn)  # Uncomment for stricter cleanup
    return nn

def clean_title(tit):
    nn = rf'{converter.decode_Tex_Accents(tit, utf8_or_ascii=1)}'.replace('\\','\\\\')
    return nn # raw string per gli slash


def fetch_articles(feed_urls):
    all_articles = []
    for url in feed_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                # Extract relevant data
                title = clean_title(entry.title)
                link = entry.link
                author = clean_author_name(entry.author) 
                abstract = entry.summary 
                tags = [f['term'] for f in entry.tags if 'stat' in f['term']]
                abstract = abstract[(abstract.index("\n")+10):]  # Adjust based on abstract location

                tmp = {"author": author,
                       "title": title,
                       "abstract": abstract,
                       "link": link,
                       "tags": tags}
                all_articles.append(tmp)
        except Exception as e:
            print(f"Error fetching RSS feed: {url} - {e}")
    return all_articles


def write_article_to_markdown(article, filename):
    # Create Markdown content lines
    lines = [
        "---",
        "layout: post",
        rf'title: "{article["title"]}"',
        f"date: {today}",  # Use publication date from feed
        f"author: {article['author']}",
        f"tags: {', '.join(article['tags'])}",  # Combine tags with comma and space
        "---",
        "",  # Empty line after header
        article['abstract'],
        "",
        f"[Read more]({article['link']})",
    ]

    # Remove leading whitespace from each line
    markdown_content = "\n".join(line.lstrip() for line in lines)

    # Write to a Markdown file with title as filename 
    with open(filename, 'w') as f:
        f.write(markdown_content)


#articles = fetch_articles(feed_urls)


def main():
    os.listdir()
    print("Deleting old posts")
    os.system('rm -rf _posts/*')
    print("Fetching new articles")
    articles = fetch_articles(feed_urls)
    # remove duplicates
    articles = [i for n, i in enumerate(articles) if i not in articles[n + 1:]]
    print(f"Writing { len(articles) } new articles")
    os.makedirs("_posts", exist_ok=True) # check is there
    for article in articles:
        # Sanitize file names
        title_ok = ''.join(filter(str.isalnum,article['title']))
        filename = f"_posts/{today}-{title_ok.replace(' ', '-')}.md"
        write_article_to_markdown(article, filename)


if __name__ == "__main__":
    main()

