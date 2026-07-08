import re
import json
import time


def build_interest_profile(preferences):
    keywords = preferences.get('keywords', [])
    authors = preferences.get('authors', [])
    context = preferences.get('context', '')
    parts = []
    if context:
        parts.append(context)
    if keywords:
        parts.append(f"Key topics: {', '.join(keywords)}")
    if authors:
        parts.append(f"Followed authors: {', '.join(authors)}")
    return '\n'.join(parts) if parts else "Statistics and machine learning research"


def score_and_summarize(article, interest_profile, client, model, retries=3):
    prompt = f"""You are helping a statistician rank arxiv papers by relevance.

Researcher's interests:
{interest_profile}

Paper:
Title: {article['title']}
Abstract: {article['abstract']}
Tags: {', '.join(article['tags'])}

Return ONLY a valid JSON object with exactly these two fields:
- "score": relevance from 1.0 to 10.0 (float). Be discriminating: reserve 8-10 for papers directly advancing the researcher's core topics, 5-7 for related work, 1-4 for tangential or irrelevant.
- "summary": ONE short sentence (max ~20 words) stating the paper's main contribution or method, in plain factual terms. Do NOT mention the researcher, their interests, relevance, or why the paper matters — just say what the paper does.

JSON:"""

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=120,
            )
            text = response.choices[0].message.content.strip()
            match = re.search(r'\{.*?\}', text, re.DOTALL)
            if match:
                return json.loads(match.group())
            raise ValueError(f"No JSON found in response: {text[:200]}")
        except Exception as e:
            is_rate_limit = '429' in str(e)
            if is_rate_limit and attempt < retries - 1:
                wait = 2 ** attempt * 5  # 5s, 10s, 20s
                time.sleep(wait)
                continue
            raise
