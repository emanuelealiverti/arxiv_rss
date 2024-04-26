from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
app.config['STATIC_URL'] = '/static'  # URL prefix for static files
app.config['STATIC_FOLDER'] = 'templates/static'  # Path to static folder


@app.route("/")
def articles_list():
    with open('saved_rss.pkl', 'rb') as f:
        articles = pickle.load(f)
        info = []
    return render_template("articles_list.html", articles=articles, info = info)

@app.route("/article/<title>")
def article_details(title):
  articles = clean_duplicates(fetch_articles())
  selected_article = None
  for article in articles:
    if article["article"] == title:
      selected_article = article
      break
  if not selected_article:
      return f"Article '{title}' not found."
  return render_template("article_details.html", article=selected_article)


if __name__ == "__main__":
    app.run(debug=True)

