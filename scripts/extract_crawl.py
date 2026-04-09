#!/usr/bin/env python3
"""Extract crawled content from firecrawl JSON into organized markdown files."""

import json
import os
import re
from urllib.parse import urlparse

INPUT = ".firecrawl/edbodmer-full-crawl.json"
OUTPUT_DIR = "Project Finance"

def url_to_filename(url, title):
    """Convert URL/title to a clean filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    if not path:
        return "index"

    # Clean up the path to use as filename
    name = path.replace("/", "_")
    # Remove common prefixes
    for prefix in ["edbodmer-wikispaces-com-", "http-edbodmer-wikispaces-com-"]:
        name = name.replace(prefix, "")

    # Clean special chars
    name = re.sub(r'[^\w\-]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')

    return name[:120]  # Limit length

def categorize(url, title):
    """Assign a subfolder based on URL path."""
    path = urlparse(url).path.lower()
    (title or "").lower()

    if "/product/" in path or "/product-category/" in path or "/product-tag/" in path:
        return "Courses"
    elif "corporate-finance" in path or "corporate-model" in path or "valuation" in path or "multiples" in path:
        return "Corporate Finance"
    elif any(x in path for x in ["debt-sizing", "debt-repayment", "debt-funding", "interest-rate",
                                   "sculpt", "credit-protection", "credit-spread", "eca-financing",
                                   "project-finance-structuring", "ballon-payment", "sinking-fund"]):
        return "Debt Structuring"
    elif any(x in path for x in ["solar", "wind", "thermal", "hydro", "renewable", "energy-project"]):
        return "Energy - Renewables and Thermal"
    elif any(x in path for x in ["toll-road", "infrastructure", "airport", "sea-port", "traffic"]):
        return "Infrastructure"
    elif any(x in path for x in ["real-estate", "hotel", "commercial-real", "residential", "mixed-development", "lease-roll"]):
        return "Real Estate"
    elif any(x in path for x in ["mining", "oil", "lng", "agriculture", "upstream", "downstream", "resource-project"]):
        return "Resources - Mining Oil Agriculture"
    elif any(x in path for x in ["ppp", "value-for-money", "university-ppp", "parking"]):
        return "PPP"
    elif any(x in path for x in ["interview", "exam", "torture", "arrogance"]):
        return "Modelling Interviews and Exams"
    elif any(x in path for x in ["exercise", "a-z-project", "construction", "working-capital",
                                   "cash-flow-waterfall", "timeline", "audit-test", "sheet-structure",
                                   "transparent-formula", "model-audit", "nol", "vat", "bad-model",
                                   "crimes", "religion"]):
        return "Building a Finance Model"
    elif any(x in path for x in ["database", "graph", "fred", "commodity"]):
        return "Databases and Graphs"
    elif any(x in path for x in ["excel", "macro", "short-cut", "backpack", "udf", "user-defined"]):
        return "Excel Utilities"
    elif any(x in path for x in ["monte-carlo", "risk-analysis", "statistical"]):
        return "Risk and Statistical Analysis"
    elif any(x in path for x in ["ma-", "merger", "acquisition"]):
        return "MA and Other Modelling"
    elif any(x in path for x in ["tax-equity", "modelling-tax"]):
        return "Tax Equity"
    elif any(x in path for x in ["electricity", "merchant", "ipp", "rate-base"]):
        return "Electricity Markets"
    elif any(x in path for x in ["housing", "u-s-housing"]):
        return "Housing Crisis"
    elif any(x in path for x in ["hydrogen"]):
        return "Hydrogen"
    elif any(x in path for x in ["article", "case-stud", "valuation-error"]):
        return "Articles and Cases"
    elif "project-finance" in path:
        return "Project Finance General"
    else:
        return "Other"

def main():
    with open(INPUT, "r") as f:
        data = json.load(f)

    pages = data.get("data", [])
    stats = {"total": 0, "with_content": 0, "skipped": 0}
    categories = {}

    for page in pages:
        stats["total"] += 1
        metadata = page.get("metadata", {})
        title = metadata.get("title", "")
        url = metadata.get("sourceURL", "")
        markdown = page.get("markdown", "")

        # Skip pages with no meaningful content
        if not markdown or len(markdown.strip()) < 100:
            stats["skipped"] += 1
            continue

        # Skip XML sitemaps and elementor templates
        if "sitemap" in url.lower() or "elementor_library" in url:
            stats["skipped"] += 1
            continue

        # Clean title (remove site suffix)
        clean_title = re.sub(r'\s*[–-]\s*Edward Bodmer.*$', '', title).strip()
        if not clean_title:
            clean_title = url_to_filename(url, title)

        category = categorize(url, title)
        folder = os.path.join(OUTPUT_DIR, category)
        os.makedirs(folder, exist_ok=True)

        filename = url_to_filename(url, clean_title) + ".md"
        filepath = os.path.join(folder, filename)

        # Write markdown with metadata header
        with open(filepath, "w") as f:
            f.write(f"# {clean_title}\n\n")
            f.write(f"**Source:** {url}\n\n")
            f.write("---\n\n")
            f.write(markdown)

        stats["with_content"] += 1
        categories[category] = categories.get(category, 0) + 1

    print("\nExtraction complete:")
    print(f"  Total pages: {stats['total']}")
    print(f"  With content: {stats['with_content']}")
    print(f"  Skipped: {stats['skipped']}")
    print("\nCategories:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count} pages")

if __name__ == "__main__":
    main()
