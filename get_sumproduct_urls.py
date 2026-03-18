#!/usr/bin/env python3
"""Fetch all URLs from sumproduct.com sitemaps."""
import xml.etree.ElementTree as ET
import urllib.request

SITEMAP_URLS = [
    "https://sumproduct.com/wp-sitemap-posts-post-1.xml",
    "https://sumproduct.com/wp-sitemap-posts-post-2.xml",
    "https://sumproduct.com/wp-sitemap-posts-page-1.xml",
    "https://sumproduct.com/wp-sitemap-posts-product-1.xml",
]

ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
all_urls = []

for sitemap_url in SITEMAP_URLS:
    try:
        req = urllib.request.Request(sitemap_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            tree = ET.parse(resp)
            root = tree.getroot()
            for loc in root.findall('.//ns:loc', ns):
                url = loc.text.strip()
                if url and 'add-to-cart' not in url:
                    all_urls.append(url)
        print(f"  {sitemap_url}: {len(root.findall('.//ns:loc', ns))} URLs")
    except Exception as e:
        print(f"  SKIP {sitemap_url}: {e}")

# Dedupe
all_urls = sorted(set(all_urls))
with open('.firecrawl/sumproduct-all-urls.txt', 'w') as f:
    for u in all_urls:
        f.write(u + '\n')

print(f"\nTotal unique URLs: {len(all_urls)}")
