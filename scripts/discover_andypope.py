#!/usr/bin/env python3
"""Discover all URLs on andypope.info by scraping section pages."""
import json
import urllib.request

FIRECRAWL = "http://localhost:3002/v1/scrape"
SEED_URLS = [
    "https://www.andypope.info/index.htm",
    "https://www.andypope.info/charts.htm",
    "https://www.andypope.info/vba.htm",
    "https://www.andypope.info/fun.htm",
    "https://www.andypope.info/tips.htm",
    "https://www.andypope.info/newsgroups.htm",
    "https://www.andypope.info/links.htm",
    "https://www.andypope.info/books.htm",
    "https://www.andypope.info/about.htm",
]

all_urls = set()

for seed in SEED_URLS:
    print(f"Discovering from {seed}...")
    payload = json.dumps({"url": seed, "formats": ["links"]}).encode()
    req = urllib.request.Request(FIRECRAWL, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            links = data.get("data", {}).get("links", [])
            for l in links:
                if "andypope.info" in l and "#" not in l and not l.endswith(('.xml', '.rss', '.zip', '.xls', '.xlsx', '.png', '.jpg', '.gif')):
                    all_urls.add(l.rstrip("/"))
    except Exception as e:
        print(f"  Error: {e}")

# Also add the seeds themselves
for s in SEED_URLS:
    all_urls.add(s.rstrip("/"))

all_urls = sorted(all_urls)
with open(".firecrawl/andypope-all-urls.txt", "w") as f:
    for u in all_urls:
        f.write(u + "\n")

print(f"\nTotal unique URLs: {len(all_urls)}")
for u in all_urls[:20]:
    print(f"  {u}")
if len(all_urls) > 20:
    print(f"  ... and {len(all_urls)-20} more")
