#!/usr/bin/env python3
"""
Bulk scrape 100 financial modelling websites using self-hosted Firecrawl.
Runs sites in batches to avoid overwhelming the Firecrawl instance.
"""
import json
import os
import re
import time
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

FIRECRAWL = "http://localhost:3002/v1"
WORKERS_PER_SITE = 3
MAX_CONCURRENT_SITES = 4  # Run 4 sites at a time (4 x 3 = 12 concurrent)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def api(endpoint, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{FIRECRAWL}/{endpoint}", data=data,
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

def discover_urls(base_url, domain_filter=None):
    """Discover URLs via /v1/map."""
    result = api("map", {"url": base_url, "limit": 5000})
    urls = []
    if result.get("success"):
        urls = result.get("links", [])
    return urls

def scrape_url(url):
    result = api("scrape", {"url": url, "timeout": 120000, "waitFor": 3000})
    if result and result.get("success"):
        return result
    time.sleep(2)
    return api("scrape", {"url": url, "timeout": 120000, "waitFor": 5000})

def url_to_filename(url):
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "index"
    name = path.replace("/", "_")
    name = re.sub(r'[^\w\-]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')
    return name[:150]

def scrape_site(site):
    key = site["key"]
    base_url = site["url"]
    folder = site["folder"]
    include_paths = [p.strip() for p in site.get("include", "").split(",") if p.strip()]

    output_dir = os.path.join(BASE_DIR, folder)
    status_file = os.path.join(BASE_DIR, ".firecrawl", f"{key}-status.json")
    url_file = os.path.join(BASE_DIR, ".firecrawl", f"{key}-all-urls.txt")

    os.makedirs(output_dir, exist_ok=True)

    domain = urllib.parse.urlparse(base_url).netloc

    def write_status(data):
        data["key"] = key
        data["name"] = site["name"]
        with open(status_file, "w") as f:
            json.dump(data, f, indent=2)

    write_status({"status": "discovering", "total": 0, "completed": 0, "success": 0, "failed": 0})
    print(f"[{key}] Discovering URLs from {base_url}...")

    raw_urls = discover_urls(base_url, domain)
    print(f"[{key}] Map found {len(raw_urls)} URLs")

    # Filter
    filtered = set()
    for u in raw_urls:
        parsed = urllib.parse.urlparse(u)
        if domain not in parsed.netloc:
            continue
        lower = u.lower()
        skip_exts = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js', '.ico',
                     '.pdf', '.xml', '.rss', '.zip', '.mp4', '.mp3', '.wav', '.woff',
                     '.woff2', '.ttf', '.eot', '.map']
        if any(lower.endswith(ext) for ext in skip_exts):
            continue
        if '#' in u:
            u = u.split('#')[0]
        if include_paths:
            if any(parsed.path.startswith(p) for p in include_paths):
                filtered.add(u.rstrip("/"))
        else:
            filtered.add(u.rstrip("/"))

    urls = sorted(filtered)

    # Save URL list
    with open(url_file, "w") as f:
        for u in urls:
            f.write(u + "\n")

    total = len(urls)
    print(f"[{key}] {total} URLs to scrape")

    if total == 0:
        write_status({"status": "done", "total": 0, "completed": 0, "success": 0, "failed": 0, "percent": 100})
        return

    # Check existing
    existing = set(os.listdir(output_dir)) if os.path.exists(output_dir) else set()
    completed = 0
    success = 0
    failed = 0
    skipped = 0
    start_time = time.time()

    def update_status():
        elapsed = time.time() - start_time
        rate = (completed - skipped) / elapsed if elapsed > 0 and (completed - skipped) > 0 else 0
        remaining = (total - completed) / rate / 60 if rate > 0 else 0
        write_status({
            "total": total, "completed": completed, "success": success,
            "failed": failed, "skipped": skipped,
            "percent": round(completed / total * 100, 1) if total > 0 else 0,
            "rate_per_sec": round(rate, 2),
            "est_remaining_min": round(remaining, 1),
            "output_dir": folder
        })

    urls_to_scrape = []
    for url in urls:
        fname = url_to_filename(url) + ".md"
        if fname in existing:
            completed += 1
            skipped += 1
            success += 1
        else:
            urls_to_scrape.append(url)

    if skipped > 0:
        print(f"[{key}] Skipping {skipped} already scraped")

    update_status()

    with ThreadPoolExecutor(max_workers=WORKERS_PER_SITE) as executor:
        future_to_url = {executor.submit(scrape_url, url): url for url in urls_to_scrape}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            completed += 1
            try:
                result = future.result()
                if result and result.get("success"):
                    data = result.get("data", {})
                    markdown = data.get("markdown", "")
                    if markdown and len(markdown.strip()) > 50:
                        title = data.get("metadata", {}).get("title", "")
                        if not title:
                            title = url_to_filename(url)
                        fname = url_to_filename(url) + ".md"
                        fpath = os.path.join(output_dir, fname)
                        with open(fpath, "w") as f:
                            f.write(f"# {title}\n\n**Source:** {url}\n\n---\n\n")
                            f.write(markdown)
                        success += 1
                    else:
                        failed += 1
                else:
                    failed += 1
            except Exception:
                failed += 1

            if completed % 5 == 0 or completed == total:
                update_status()
                print(f"  [{key}] {completed}/{total} ({round(completed/total*100,1)}%) OK:{success} FAIL:{failed}")

    write_status({
        "status": "done", "total": total, "completed": total,
        "success": success, "failed": failed, "skipped": skipped,
        "percent": 100, "rate_per_sec": 0, "est_remaining_min": 0,
        "output_dir": folder
    })
    print(f"\n[{key}] DONE: {success} saved, {failed} failed, {skipped} skipped / {total}")


def main():
    with open(os.path.join(BASE_DIR, "sites_100.json")) as f:
        sites = json.load(f)

    # Skip sites already done
    skip_keys = set()
    for site in sites:
        sf = os.path.join(BASE_DIR, ".firecrawl", f"{site['key']}-status.json")
        if os.path.exists(sf):
            try:
                with open(sf) as f:
                    st = json.load(f)
                if st.get("status") == "done" and st.get("success", 0) > 0:
                    skip_keys.add(site["key"])
                    print(f"[{site['key']}] Already done ({st['success']} saved), skipping")
            except:
                pass

    remaining = [s for s in sites if s["key"] not in skip_keys]
    print(f"\n{len(remaining)} sites to scrape ({len(skip_keys)} already done)")

    # Process in batches

    # Use threading batches instead of processes for simplicity
    batch_size = MAX_CONCURRENT_SITES
    for i in range(0, len(remaining), batch_size):
        batch = remaining[i:i+batch_size]
        batch_names = [s["name"] for s in batch]
        print(f"\n=== BATCH {i//batch_size + 1}: {', '.join(batch_names)} ===\n")

        threads = []
        import threading
        for site in batch:
            t = threading.Thread(target=scrape_site, args=(site,), name=site["key"])
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    print("\n=== ALL 100 SITES COMPLETE ===")


if __name__ == "__main__":
    main()
