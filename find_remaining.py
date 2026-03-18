#!/usr/bin/env python3
"""Find URLs from the site map that weren't in the crawl."""

import json

# Load crawled URLs
with open(".firecrawl/edbodmer-full-crawl.json") as f:
    crawl_data = json.load(f)

crawled_urls = set()
for page in crawl_data.get("data", []):
    url = page.get("metadata", {}).get("sourceURL", "")
    if url:
        crawled_urls.add(url.rstrip("/"))

# Load mapped URLs
with open(".firecrawl/edbodmer-urls.txt") as f:
    mapped_urls = set(line.strip().rstrip("/") for line in f if line.strip())

# Find remaining
remaining = sorted(mapped_urls - crawled_urls)

# Filter out non-content URLs
remaining = [u for u in remaining if "elementor_library" not in u and "sitemap" not in u.lower()]

print(f"Crawled: {len(crawled_urls)}")
print(f"Mapped: {len(mapped_urls)}")
print(f"Remaining (content): {len(remaining)}")

with open(".firecrawl/remaining-urls.txt", "w") as f:
    for url in remaining:
        f.write(url + "\n")

print("\nRemaining URLs saved to .firecrawl/remaining-urls.txt")
for u in remaining[:20]:
    print(f"  {u}")
if len(remaining) > 20:
    print(f"  ... and {len(remaining) - 20} more")
