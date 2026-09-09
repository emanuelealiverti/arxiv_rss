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


def extract_result(text):
    """Pull the score/summary object out of a model reply.

    Reasoning models emit their scratchpad before the answer, which can hold
    several JSON-looking fragments, so take the last one that actually parses
    and carries a score rather than the first thing that looks like an object.
    """
    for candidate in reversed(re.findall(r'\{[^{}]*\}', text, re.DOTALL)):
        try:
            obj = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and 'score' in obj:
            obj.setdefault('summary', '')
            return obj
    return None


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
                max_tokens=800,
            )
            message = response.choices[0].message
            # Reasoning models leave `content` empty and put everything,
            # answer included, in `reasoning_content`.
            text = (message.content or getattr(message, 'reasoning_content', '') or '').strip()
            result = extract_result(text)
            if result is not None:
                return result
            raise ValueError(f"No JSON found in response: {text[:200]}")
        except Exception as e:
            is_rate_limit = '429' in str(e)
            if is_rate_limit and attempt < retries - 1:
                wait = 2 ** attempt * 5  # 5s, 10s, 20s
                time.sleep(wait)
                continue
            raise
