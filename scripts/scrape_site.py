#!/usr/bin/env python3
"""
Discover URLs and scrape a site using self-hosted Firecrawl.
Usage: python3 scrape_site.py <key> <base_url> <output_dir> [--include-paths /a,/b] [--seed-urls url1,url2]
"""
import json, os, re, sys, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

FIRECRAWL = "http://localhost:3002/v1"
MAX_WORKERS = 3  # Keep low: 8 sites × 3 = 24 concurrent max

def api(endpoint, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{FIRECRAWL}/{endpoint}", data=data,
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

def discover_urls_map(base_url):
    """Use Firecrawl /v1/map to discover URLs."""
    result = api("map", {"url": base_url, "limit": 5000})
    if result.get("success"):
        return result.get("links", [])
    print(f"  Map failed: {result.get('error','unknown')[:100]}")
    return []

def discover_urls_scrape_links(seed_urls):
    """Scrape seed pages for links."""
    all_links = set()
    for url in seed_urls:
        result = api("scrape", {"url": url, "formats": ["links"], "timeout": 120000, "waitFor": 3000})
        if result.get("success"):
            links = result.get("data", {}).get("links", [])
            all_links.update(links)
            print(f"  Seed {url}: {len(links)} links")
        else:
            print(f"  Seed {url}: FAILED - {result.get('error','')[:80]}")
    return list(all_links)

def scrape_url(url):
    # No waitFor on first attempt — most blog content is server-rendered.
    # Retry with a 2s wait for SPA-style sites.
    result = api("scrape", {"url": url, "timeout": 60000})
    if result and result.get("success"):
        return result
    time.sleep(1)
    return api("scrape", {"url": url, "timeout": 120000, "waitFor": 2000})

def url_to_filename(url):
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "index"
    name = path.replace("/", "_")
    name = re.sub(r'[^\w\-]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')
    return name[:150]

def main():
    key = sys.argv[1]
    base_url = sys.argv[2]
    output_dir = sys.argv[3]

    include_paths = []
    seed_urls = []
    domain_filter = urllib.parse.urlparse(base_url).netloc

    i = 4
    while i < len(sys.argv):
        if sys.argv[i] == "--include-paths" and i + 1 < len(sys.argv):
            include_paths = [p.strip() for p in sys.argv[i+1].split(",")]
            i += 2
        elif sys.argv[i] == "--seed-urls" and i + 1 < len(sys.argv):
            seed_urls = [u.strip() for u in sys.argv[i+1].split(",")]
            i += 2
        elif sys.argv[i] == "--domain" and i + 1 < len(sys.argv):
            domain_filter = sys.argv[i+1]
            i += 2
        else:
            i += 1

    status_file = f".firecrawl/{key}-status.json"
    url_file = f".firecrawl/{key}-all-urls.txt"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(".firecrawl", exist_ok=True)

    def write_status(data):
        with open(status_file, "w") as f:
            json.dump(data, f, indent=2)

    # Phase 1: Discover URLs
    write_status({"status": "discovering", "total": 0, "completed": 0, "success": 0, "failed": 0})
    print(f"[{key}] Discovering URLs from {base_url}...")

    urls = set()

    # Try /v1/map first
    map_urls = discover_urls_map(base_url)
    print(f"[{key}] Map found {len(map_urls)} URLs")
    urls.update(map_urls)

    # Also scrape seed URLs for links
    if seed_urls:
        link_urls = discover_urls_scrape_links(seed_urls)
        print(f"[{key}] Seed pages found {len(link_urls)} links")
        urls.update(link_urls)

    # Filter to domain and include paths
    filtered = set()
    for u in urls:
        parsed = urllib.parse.urlparse(u)
        if domain_filter not in parsed.netloc:
            continue
        # Skip non-content files
        lower = u.lower()
        if any(lower.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js', '.ico', '.pdf', '.xml', '.rss', '.zip', '.mp4', '.mp3', '.wav']):
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
        print(f"[{key}] No URLs found, done.")
        return

    # Phase 2: Scrape
    # Check which files already exist
    existing = set(os.listdir(output_dir))
    completed = 0
    success = 0
    failed = 0
    skipped = 0
    start_time = time.time()

    def update_status():
        elapsed = time.time() - start_time
        rate = (completed - skipped) / elapsed if elapsed > 0 and (completed - skipped) > 0 else 0
        remaining_to_scrape = total - completed
        remaining = remaining_to_scrape / rate / 60 if rate > 0 else 0
        write_status({
            "total": total,
            "completed": completed,
            "success": success,
            "failed": failed,
            "skipped": skipped,
            "percent": round(completed / total * 100, 1) if total > 0 else 0,
            "rate_per_sec": round(rate, 2),
            "est_remaining_min": round(remaining, 1),
            "output_dir": output_dir
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
        completed_base = completed

    update_status()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
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
                        # Clean title
                        for pattern in [r'\s*[|–-]\s*(Macabacus|CFI|Corporate Finance|Wall Street|Breaking|BIWS|Forvis|Mazars|Pivotal|Full Stack|Modeller|Damodaran).*$']:
                            title = re.sub(pattern, '', title, flags=re.IGNORECASE).strip()
                        if not title:
                            title = url_to_filename(url)

                        fname = url_to_filename(url) + ".md"
                        fpath = os.path.join(output_dir, fname)
                        with open(fpath, "w") as f:
                            f.write(f"# {title}\n\n")
                            f.write(f"**Source:** {url}\n\n---\n\n")
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
                elapsed = time.time() - start_time
                print(f"  [{key}] {completed}/{total} ({round(completed/total*100,1)}%) OK:{success} FAIL:{failed}")

    # Final status
    write_status({
        "status": "done",
        "total": total,
        "completed": total,
        "success": success,
        "failed": failed,
        "skipped": skipped,
        "percent": 100,
        "rate_per_sec": 0,
        "est_remaining_min": 0,
        "output_dir": output_dir
    })
    print(f"\n[{key}] DONE: {success} saved, {failed} failed, {skipped} skipped out of {total}")

if __name__ == "__main__":
    main()
