"""Probe NVIDIA chat models with the exact scoring call rss_arxiv.py makes.

Tries every entry of MODEL_CANDIDATES (not just the first that works) on a
few real abstracts and reports speed, scores and a sample summary.

Run from the repo root:  python probe_models.py   (needs NVIDIA_API_KEY in env)
On GitHub: run the workflow with the "probe_models" input ticked.
"""
import os
import time

from openai import OpenAI

import rss_arxiv
from llm_utils import build_interest_profile, score_and_summarize

CANDIDATES = rss_arxiv.MODEL_CANDIDATES
N_ARTICLES = 3

client = OpenAI(base_url="https://integrate.api.nvidia.com/v1",
                api_key=os.environ["NVIDIA_API_KEY"], timeout=60.0)
profile = build_interest_profile(rss_arxiv.load_yaml(rss_arxiv.PREFS_FILE))
articles = rss_arxiv.fetch_articles()[:N_ARTICLES]
print(f"Probing with {len(articles)} articles\n", flush=True)

for model in CANDIDATES:
    times, scores, err = [], [], None
    for a in articles:
        t = time.time()
        try:
            r = score_and_summarize(a, profile, client, model, retries=1)
            scores.append(float(r["score"]))
            summary = r["summary"]
        except Exception as e:
            err = str(e)[:120]
            break
        times.append(time.time() - t)
    if err:
        print(f"FAIL {model}: {err}", flush=True)
    else:
        print(f"OK   {model}: {sum(times)/len(times):.1f}s/article  scores={scores}", flush=True)
        print(f"       last summary: {summary}", flush=True)
