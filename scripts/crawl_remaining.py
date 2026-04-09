#!/usr/bin/env python3
"""Use crawl4ai to scrape remaining edbodmer.com pages."""

import asyncio
import os
import re
from urllib.parse import urlparse

OUTPUT_DIR = "Project Finance"

def url_to_filename(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "index"
    name = path.replace("/", "_")
    for prefix in ["edbodmer-wikispaces-com-", "http-edbodmer-wikispaces-com-"]:
        name = name.replace(prefix, "")
    name = re.sub(r'[^\w\-]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')
    return name[:120]

def categorize(url):
    path = urlparse(url).path.lower()
    if "/product/" in path or "/product-category/" in path or "/product-tag/" in path:
        return "Courses"
    elif any(x in path for x in ["corporate-finance", "corporate-model", "valuation", "multiples", "dcf", "wacc", "capm", "beta-analysis", "cost-of-capital", "stock-price", "irr"]):
        return "Corporate Finance"
    elif any(x in path for x in ["debt-sizing", "debt-repayment", "debt-funding", "interest-rate", "sculpt", "credit-protection", "credit-spread", "eca-financing"]):
        return "Debt Structuring"
    elif any(x in path for x in ["solar", "wind", "thermal", "hydro", "renewable", "energy-project", "biomass", "biogas"]):
        return "Energy - Renewables and Thermal"
    elif any(x in path for x in ["toll-road", "infrastructure", "airport", "sea-port", "traffic"]):
        return "Infrastructure"
    elif any(x in path for x in ["real-estate", "hotel", "commercial-real", "residential", "mixed-development"]):
        return "Real Estate"
    elif any(x in path for x in ["mining", "oil", "lng", "agriculture", "upstream", "downstream", "resource-project"]):
        return "Resources - Mining Oil Agriculture"
    elif any(x in path for x in ["ppp", "value-for-money"]):
        return "PPP"
    elif any(x in path for x in ["interview", "exam", "torture", "arrogance"]):
        return "Modelling Interviews and Exams"
    elif any(x in path for x in ["exercise", "a-z-project", "construction", "working-capital", "cash-flow-waterfall", "timeline", "audit-test", "sheet-structure"]):
        return "Building a Finance Model"
    elif any(x in path for x in ["database", "graph", "fred", "commodity"]):
        return "Databases and Graphs"
    elif any(x in path for x in ["excel", "macro", "short-cut", "backpack", "udf", "user-defined", "screenshot", "cntl"]):
        return "Excel Utilities"
    elif any(x in path for x in ["monte-carlo", "risk-analysis", "statistical", "sensitivity"]):
        return "Risk and Statistical Analysis"
    elif any(x in path for x in ["tax-equity", "modelling-tax"]):
        return "Tax Equity"
    elif any(x in path for x in ["battery", "storage", "microgrid", "lcoe", "lcos"]):
        return "Battery and Storage"
    elif any(x in path for x in ["electricity", "merchant", "ipp", "rate-base", "carrying-charge", "heat-rate"]):
        return "Electricity Markets"
    elif any(x in path for x in ["hydrogen"]):
        return "Hydrogen"
    elif any(x in path for x in ["circular", "template"]):
        return "Circular References"
    elif "project-finance" in path:
        return "Project Finance General"
    else:
        return "Other"


async def main():
    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

    # Load remaining URLs
    with open(".firecrawl/remaining-urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]

    # Filter out non-content URLs
    skip_patterns = ["basket", "checkout", "check", "apply-for-scholarship", "my-account", "shop"]
    urls = [u for u in urls if not any(urlparse(u).path.strip("/") in skip_patterns for _ in [1])]

    print(f"Crawling {len(urls)} remaining pages with crawl4ai...")

    browser_config = BrowserConfig(headless=True)
    crawler_config = CrawlerRunConfig()

    success = 0
    failed = 0

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Process in batches of 10
        batch_size = 10
        for i in range(0, len(urls), batch_size):
            batch = urls[i:i+batch_size]
            print(f"\nBatch {i//batch_size + 1}/{(len(urls) + batch_size - 1)//batch_size} ({i+1}-{min(i+batch_size, len(urls))} of {len(urls)})")

            results = await crawler.arun_many(batch, config=crawler_config)

            for result in results:
                if result.success and result.markdown and len(result.markdown.raw_markdown.strip()) > 100:
                    url = result.url
                    title = result.metadata.get("title", "") if result.metadata else ""
                    clean_title = re.sub(r'\s*[–-]\s*Edward Bodmer.*$', '', title).strip()
                    if not clean_title:
                        clean_title = url_to_filename(url)

                    category = categorize(url)
                    folder = os.path.join(OUTPUT_DIR, category)
                    os.makedirs(folder, exist_ok=True)

                    filename = url_to_filename(url) + ".md"
                    filepath = os.path.join(folder, filename)

                    with open(filepath, "w") as f:
                        f.write(f"# {clean_title}\n\n")
                        f.write(f"**Source:** {url}\n\n")
                        f.write("---\n\n")
                        f.write(result.markdown.raw_markdown)

                    success += 1
                    print(f"  OK: {clean_title[:60]}")
                else:
                    failed += 1
                    print(f"  SKIP: {result.url} (no content or failed)")

    print(f"\n\nDone! Success: {success}, Skipped/Failed: {failed}")


if __name__ == "__main__":
    asyncio.run(main())
