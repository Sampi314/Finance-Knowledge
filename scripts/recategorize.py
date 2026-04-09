#!/usr/bin/env python3
"""Recategorize files in Project Finance/Other into better subfolders."""

import os
import shutil

BASE = "Project Finance"
OTHER = os.path.join(BASE, "Other")

# Map filename patterns to categories
RULES = [
    # Corporate Finance & Valuation
    (["dcf", "wacc", "capm", "cost-of-capital", "irr", "roic", "roi-", "valuation",
      "multiples", "price-to-book", "price-to-earnings", "value-driver", "terminal-cash",
      "enterprise-value", "equity-value", "football-field", "lbo", "payback-period",
      "mckinsey", "discount-rate", "stock-price", "stock-return", "beta-analysis",
      "financial-model-for-amazon", "financial-statement", "key-files-for-corporate",
      "normalised-cash-flow", "partial-year-discounting", "implied-default",
      "country-risk-premium", "political-risk", "reconciliation-of-irr",
      "economic-depreciation", "alternative-to-irr", "alternatives-to-capm",
      "mean-reversion", "overview-of-irr", "b-s-mckinsey", "resolution-of-tax-shield",
      "roic-mechanical", "computing-the-implied-retirement", "using-the-price",
      "using-the-value-driver", "advanced-dcf", "advanced-multples",
      "application-of-wacc", "credit-analysis-bond", "credit-analysis",
      "market-price-c-model"], "Corporate Finance"),

    # Debt & Structuring
    (["debt-service-reserve", "dsra", "cash-sweep", "llcr", "plcr", "dscr",
      "covenant", "sculpt", "repayment", "re-financing", "mini-perm",
      "multiple-issues", "deficit-reduction", "financing-with-multiple",
      "financing-the-consolidated", "idc-on-subordinated", "equity-bridge",
      "structuring-multiple", "repayments-with-debt", "resolving-negative",
      "modelling-defaults", "soveriegn-debt", "introduction-to-structuring",
      "reserve-based-loan", "development-fee-timing-for-debt"], "Debt Structuring"),

    # Circular References & Templates
    (["circular-reference", "circular-template", "circular-solution",
      "introduction-to-circular", "adding-template"], "Circular References"),

    # Battery & Storage
    (["battery", "storage", "microgrid", "mini-grid", "lcoe", "lcos",
      "introduction-to-battery", "modelling-battery", "retail-rate-analysis"], "Battery and Storage"),

    # Electricity & Energy Markets
    (["carrying-charge", "heat-rate", "conversion", "electricity",
      "merchant", "ipp", "rate-base", "generation-compan", "load-duration",
      "short-term-marginal", "levelised-cost", "smr-versus", "cost-of-service",
      "energy-courses", "ancillary-services"], "Electricity Markets"),

    # Excel & VBA Utilities
    (["vba", "macro", "short-cut", "excel", "spinner", "dropdown", "list-box",
      "data-table", "table-of-contents", "goal-seek", "copy-to-the-right",
      "delete-blank", "find-month", "european-numbers", "external-link",
      "interpolate-lookup", "match-with-partial", "maxif", "na-trick",
      "sheet-name-remove", "removing-links", "re-setting-your-model",
      "scenario-analysis", "scenario-reporter", "scenarios-3", "scenario",
      "finding-no-dependent", "finding-data-with-range", "resolving-millions",
      "better-data-tables", "fundamental-of-one-way", "dynamic-goal-seek",
      "finding-links-to", "spinners-drop-down"], "Excel Utilities"),

    # Risk & Sensitivity Analysis
    (["tornado", "spider", "sensitivity", "monte-carlo", "risk-analysis",
      "scatter-plot", "bubble-diagram", "forecasting", "exponential-smoothing",
      "creating-a-spider"], "Risk and Statistical Analysis"),

    # Tax Equity & Developer Fees
    (["tax-equity", "developer-fee", "development-fee", "paygo", "inside-capital",
      "outside-capital", "minimum-gain", "704-account", "inverted-lease",
      "performance-incentive", "sale-leasback", "capital-account",
      "production-sharing"], "Tax Equity"),

    # Building a Finance Model
    (["timeline", "time-line", "audit-test", "transparent-formula",
      "model-audit", "sheet-structure", "setting-up-model", "introduction-and-time",
      "cash-flow-waterfall", "operating-tax-and-depreciation",
      "construction-analysis", "working-capital", "vat-in-project",
      "tabulating-annual", "monthly-model", "detailed-model",
      "currency-adjustment", "learning-from-bad", "high-crimes",
      "reviewing-other-models", "heavy-financial-models"], "Building a Finance Model"),

    # Project Finance General
    (["project-finance", "spv", "cost-of-transferring-risk", "epc",
      "counter-party", "structuring-contract", "economics-of-contract",
      "economics-of-incentives", "liquidated-damage", "a-z-case",
      "a-z-course", "parallel-model"], "Project Finance General"),

    # Courses & Website Admin
    (["course-schedule", "overview-of-courses", "online-courses", "webinar",
      "financial-modelling-courses", "register-for", "sign-up", "reserve-a-place",
      "send-me-an-e-mail", "contact-form", "contat-us", "instructions-for",
      "subjects-to-cover", "teaching-philosophy", "overview", "home-2",
      "search_gcse", "slides", "index", "new-book", "writings", "draft-of-book",
      "expert-testimony", "testimony-on", "cost-of-capital-testimony",
      "technical-details", "energy-courses", "files-and-videos"], "Courses and Resources"),

    # Databases & Data
    (["clean-data-extracted", "collecting-ticker", "database-for-historical",
      "read-pdf", "exchange-rate"], "Databases and Graphs"),

    # Real Estate
    (["lease-analysis", "real-estate"], "Real Estate"),

    # M&A
    (["lbo", "merger", "acquisition", "ma-theory", "consolidation",
      "portfolio-of-investment", "air-freight-and-corporation"], "MA and Other Modelling"),

    # Climate / Hydrogen / Resources
    (["hydrogen", "climate-change", "modelling-for-adaption"], "Hydrogen and Climate"),
    (["oil", "lng", "upstream", "downstream", "mining", "agriculture"], "Resources - Mining Oil Agriculture"),

    # Options / Futures
    (["options-and-futures"], "Options and Futures"),

    # Banking / Financial Institutions
    (["return-on-risk-adjusted", "rorac", "budgeting-analysis"], "Financial Institutions"),

    # Depreciation
    (["depreciation"], "Building a Finance Model"),
]


def categorize_file(filename):
    name_lower = filename.lower()
    for patterns, category in RULES:
        for p in patterns:
            if p in name_lower:
                return category
    return None  # stays in Other


def main():
    files = os.listdir(OTHER)
    moved = 0
    stayed = 0

    for f in sorted(files):
        if not f.endswith(".md"):
            continue
        cat = categorize_file(f)
        if cat:
            dest_dir = os.path.join(BASE, cat)
            os.makedirs(dest_dir, exist_ok=True)
            src = os.path.join(OTHER, f)
            dst = os.path.join(dest_dir, f)
            if not os.path.exists(dst):
                shutil.move(src, dst)
                moved += 1
            else:
                stayed += 1
        else:
            stayed += 1

    print(f"Moved: {moved}, Remained in Other: {stayed}")

    # Print final counts
    remaining = [f for f in os.listdir(OTHER) if f.endswith(".md")]
    print(f"\nRemaining in Other: {len(remaining)}")
    for f in sorted(remaining):
        print(f"  {f}")


if __name__ == "__main__":
    main()
