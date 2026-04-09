#!/usr/bin/env python3
"""
Scrape URLs using self-hosted Firecrawl /v1/scrape endpoint.
Writes progress to a status file for monitoring.
Usage: python3 scrape_with_firecrawl.py <url_file> <output_dir> <status_file>
"""

import json
import os
import re
import sys
import time
import urllib.request
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

FIRECRAWL_URL = "http://localhost:3002/v1/scrape"
MAX_WORKERS = 5  # parallel scrapes

def scrape_url(url):
    """Scrape a single URL via self-hosted Firecrawl."""
    try:
        payload = json.dumps({"url": url}).encode()
        req = urllib.request.Request(
            FIRECRAWL_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
            if data.get("success"):
                return data.get("data", {})
    except Exception as e:
        return {"error": str(e)}
    return None

def url_to_filename(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "index"
    name = path.replace("/", "_")
    name = re.sub(r'[^\w\-]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')
    return name[:150]

def main():
    url_file = sys.argv[1]
    output_dir = sys.argv[2]
    status_file = sys.argv[3]

    with open(url_file) as f:
        urls = [line.strip() for line in f if line.strip()]

    os.makedirs(output_dir, exist_ok=True)

    total = len(urls)
    completed = 0
    success = 0
    failed = 0
    start_time = time.time()

    def update_status():
        elapsed = time.time() - start_time
        rate = completed / elapsed if elapsed > 0 else 0
        remaining = (total - completed) / rate / 60 if rate > 0 else 0
        status = {
            "total": total,
            "completed": completed,
            "success": success,
            "failed": failed,
            "percent": round(completed / total * 100, 1) if total > 0 else 0,
            "rate_per_sec": round(rate, 2),
            "est_remaining_min": round(remaining, 1),
            "output_dir": output_dir
        }
        with open(status_file, "w") as sf:
            json.dump(status, sf, indent=2)

    update_status()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(scrape_url, url): url for url in urls}

        for future in as_completed(future_to_url):
            url = future_to_url[future]
            completed += 1
            try:
                result = future.result()
                if result and "error" not in result:
                    markdown = result.get("markdown", "")
                    if markdown and len(markdown.strip()) > 50:
                        title = result.get("metadata", {}).get("title", "")
                        clean_title = re.sub(r'\s*[|–-]\s*(Edward Bodmer|SumProduct).*$', '', title, flags=re.IGNORECASE).strip()
                        if not clean_title:
                            clean_title = url_to_filename(url)

                        filename = url_to_filename(url) + ".md"
                        filepath = os.path.join(output_dir, filename)

                        with open(filepath, "w") as f:
                            f.write(f"# {clean_title}\n\n")
                            f.write(f"**Source:** {url}\n\n")
                            f.write("---\n\n")
                            f.write(markdown)

                        success += 1
                    else:
                        failed += 1
                else:
                    failed += 1
            except Exception:
                failed += 1

            if completed % 10 == 0 or completed == total:
                update_status()
                print(f"  [{completed}/{total}] OK:{success} FAIL:{failed} - {url[:80]}")

    update_status()
    print(f"\nDONE: {success} saved, {failed} failed out of {total}")

if __name__ == "__main__":
    main()
