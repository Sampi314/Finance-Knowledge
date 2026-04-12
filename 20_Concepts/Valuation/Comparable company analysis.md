---
type: concept
title: "Comparable company analysis"
aliases: ["Comps", "Comparable companies", "Trading multiples"]
tags: ["valuation", "m-and-a", "multiples"]
difficulty: intermediate
prerequisites: ["[[Enterprise value]]", "[[Equity value]]", "[[Intrinsic vs relative valuation]]"]
related: []
sources: ["[[IB Interview Questions - How to Build a Comparable Company Analysis (Comps)]]"]
status: draft
updated: 2026-04-12
---

# Comparable company analysis

> **TL;DR.** A relative valuation methodology that estimates a company's value by comparing it to similar publicly traded companies using valuation multiples like EV/EBITDA.

## When you'd use this

You would use comparable company analysis (comps) in virtually every pitch book, investment memo, and fairness opinion to establish valuation benchmarks based on how similar companies are valued by the market. It works best when you have multiple truly comparable public companies in the same industry with similar business models, growth profiles, and margins. It is particularly valuable for establishing valuation ranges for M&A transactions or IPO pricing, checking DCF or other valuation approaches, and understanding market sentiment.

## The 30-second version

Comparable company analysis is a relative valuation method based on the efficient market hypothesis, suggesting that similar companies should trade at similar valuations. If five similar software companies trade at 8-10x revenue, a sixth comparable company should fall in that range. Building comps involves identifying 5-10 public peers, gathering their financial data, calculating multiples (like EV/Revenue and EV/EBITDA), analyzing the distribution (usually focusing on the median), and applying the appropriate multiples to your target company to derive an implied valuation range.

## The full explanation

Comparable company analysis involves a 6-step process to arrive at a valuation for a target company based on public peers.

### 1. Select Comparable Companies
This is the most critical and subjective step. Select 5-10 truly comparable companies based on industry and business model (e.g., B2B enterprise software vs consumer mobile apps), size and scale (typically 0.5x to 2x the target's revenue), growth profile, profitability/margins, and geography. Quality beats quantity; it is better to have 5 highly comparable companies than 15 loose matches.

### 2. Gather Financial Data
Collect market data such as stock price, fully diluted shares outstanding, and net debt to calculate equity and enterprise value. You also need financial metrics (LTM and NTM estimates for revenue, EBITDA, EBIT, and net income), and growth/margin metrics. Sources include company filings (10-Ks, 10-Qs), market data websites, analyst estimates (for forward-looking metrics), and investor presentations.

### 3. Calculate Valuation Multiples
Calculate relevant multiples for each comparable. Enterprise value multiples (EV/Revenue, EV/EBITDA, EV/EBIT) are capital structure neutral and preferred in M&A. Equity multiples (P/E) reflect leverage differences. Calculate both last twelve months (LTM) and next twelve months (NTM) multiples, as NTM estimates are often more relevant.

### 4. Analyze the Multiple Distribution
Calculate key statistics for each multiple across your peers: mean, median, 25th percentile, and 75th percentile. The median and interquartile range (IQR) are preferred because they exclude extreme outliers. Analyze why certain companies trade at higher or lower multiples; for instance, higher growth rates and better margins typically drive premium valuations.

### 5. Apply Multiples to Your Target
Apply the selected multiple range (often based on the median and IQR) to your target company's financial metrics to find its implied enterprise value or equity value. Adjust this application based on whether the target's growth and margins are superior or inferior to the peer group. Convert implied enterprise value to equity value by subtracting net debt.

### 6. Present Your Analysis
Display the results in a clear table with consistent formatting. Include summary statistics and footnotes documenting data sources and market data dates. Highlight why comparables were selected, key observations about the range, and where the target falls within it.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

Ensure your spreadsheet lists comparables in rows and data points in columns for easy multiple calculation. Include explicit calculations for fully diluted shares outstanding (using the treasury stock method) and net debt. Build in summary statistic rows (mean, median, min, max, 25th/75th percentiles) at the bottom.

## Interview-ready answer

[[Walk me through a comparable company analysis]]

## Pitfalls and gotchas

- Padding the comparable set with companies that aren't truly similar just to hit a higher number of peers.
- Using stale market data without disclosing the date it was pulled.
- Mechanically applying median multiples without considering if the target has superior or inferior growth/margins compared to peers.
- Confusing enterprise value multiples (which use operating metrics like EBITDA or Revenue) with equity multiples (which use net income).
- Poor documentation of data sources and assumptions.

## Sources

- [[IB Interview Questions - How to Build a Comparable Company Analysis (Comps)]]
