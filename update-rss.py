import feedparser
import LaTexAccents as TeX
from collections import defaultdict
import re
import pickle

converter = TeX.AccentConverter()

feed_urls = [
    'https://rss.arxiv.org/rss/stat',
]

def clean_author_name(name):
  nn = re.sub(r'\([^)]*\)', '', name)
  nn = converter.decode_Tex_Accents(nn, utf8_or_ascii=1)
  #nn = re.sub("[^\w ,']*",'', nn)
  return nn 

def feed_info():
    feeds = [feedparser.parse(url) for url in feed_urls]
    return(feeds[0]['feed']['published'])


def fetch_articles():
  all_articles = []
  for url in feed_urls:
    try:
        #response = requests.get(url)
      #feed = feedparser.parse(response.content)
      feed = feedparser.parse(url)
      for entry in feed.entries:
        # Extract relevant data (may vary depending on RSS format)
        title = entry.title
        link = entry.link
        author = clean_author_name(entry.author) if hasattr(entry, "author") else "Unknown"
        abstract = entry.summary if hasattr(entry, "summary") else ""
        tags = [f['term'] for f in entry.tags if 'stat' in f['term']]
        # pulisci abstract
        abstract = abstract[(abstract.index("\n")+10):]
        tmp = {"author": author, 
               "article": title, 
               "abstract": abstract,
               "link": link,
               "tags": tags}
        all_articles.append(tmp)
    except Exception as e:
      print(f"Error fetching RSS feed: {url} - {e}")
  return all_articles

def clean_duplicates(articles):
  # Use defaultdict to efficiently store articles with title as key
  unique_articles = defaultdict(list)
  for article in articles:
    unique_articles[article["article"]].append(article)
  # Keep only the first article (assuming duplicates have same content)
  return [articles[0] for articles in unique_articles.values()]

articles = clean_duplicates(fetch_articles())


with open('saved_rss.pkl', 'wb') as f:
    pickle.dump(articles, f)


