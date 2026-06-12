# Stat arXiv

A personalized arXiv RSS reader built with Jekyll and deployed on GitHub Pages.

## How it works

A GitHub Actions workflow runs every weekday at 8:30 Rome time:

1. **Scraping** — fetches RSS feeds from arXiv (stat.ME, stat.CO, stat.AP) via `feedparser`
2. **Ranking** — each paper is scored by an LLM (via the [NVIDIA NIM API](https://integrate.api.nvidia.com), model `meta/llama-3.1-8b-instruct`) against a research interest profile defined in `preferences.yml`; the score is further boosted by keyword and author matches
3. **Publishing** — scored papers are written as Jekyll posts, the site is rebuilt and deployed to GitHub Pages; posts are kept for a rolling 7-day window

The rendered website lives at [https://emanuelealiverti.github.io/arxiv_rss/](https://emanuelealiverti.github.io/arxiv_rss/).

## Customization

Edit `preferences.yml` to update your research context, keywords, and followed authors. Push to `main` and the next scheduled run will pick up the changes.

## Notes

- The `main` branch holds the infrastructure; `gh-pages` holds the deployed site
- If the NVIDIA API is unavailable, scoring falls back to keyword/author matching only

This project started from a personal first draft and was then vibe coded with [Claude Code](https://claude.ai/claude-code).
