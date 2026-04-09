#!/usr/bin/env python3
"""Download all Excel and zip files from andypope.info."""
import os
import json
import urllib.request
import urllib.parse

INPUT = ".firecrawl/andypope-excel-links.txt"
OUTPUT_DIR = "Andy Pope/files"
STATUS_FILE = ".firecrawl/andypope-download-status.json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT) as f:
    urls = [line.strip() for line in f if line.strip()]

total = len(urls)
success = 0
failed = 0
skipped = 0

print(f"Downloading {total} files...")

for i, url in enumerate(urls, 1):
    filename = urllib.parse.unquote(url.split("/")[-1])
    # Organize into subfolders by section
    parts = urllib.parse.urlparse(url).path.strip("/").split("/")
    if len(parts) > 1:
        subfolder = parts[-2]  # e.g. charts, vba, fun, ngs, tips
        dest_dir = os.path.join(OUTPUT_DIR, subfolder)
    else:
        dest_dir = OUTPUT_DIR
    os.makedirs(dest_dir, exist_ok=True)
    filepath = os.path.join(dest_dir, filename)

    if os.path.exists(filepath):
        skipped += 1
        continue

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            with open(filepath, "wb") as f:
                f.write(resp.read())
        success += 1
        size = os.path.getsize(filepath)
        print(f"  [{i}/{total}] OK {filename} ({size//1024}KB)")
    except Exception as e:
        failed += 1
        print(f"  [{i}/{total}] FAIL {filename}: {e}")

    # Update status
    if i % 10 == 0 or i == total:
        with open(STATUS_FILE, "w") as sf:
            json.dump({"total": total, "completed": i, "success": success, "failed": failed, "skipped": skipped}, sf, indent=2)

print(f"\nDone: {success} downloaded, {failed} failed, {skipped} skipped")
