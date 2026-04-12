---
type: concept
title: "Football field chart"
aliases: ["Football field diagram", "Floating bar chart"]
tags: ["Valuation", "investment-banking", "charting", "financial-modeling"]
difficulty: intermediate
prerequisites: []
related: []
sources: ["[[Macabacus - Building a Football Field Chart in Excel]]", "[[BIWS - Football Field Valuation- Excel Template, Tutorial, and Full Explanation]]", "[[Project Finance - Football Field Diagrams]]"]
status: draft
updated: 2026-04-12
---

# Football field chart

> **TL;DR.** A football field chart visually summarizes multiple valuation methodologies by displaying their respective value ranges side by side, allowing analysts to easily compare the output and identify outliers.

## When you'd use this

A football field chart is primarily used in investment banking, particularly for Mergers & Acquisitions (M&A) analysis, fairness opinions, and pitchbooks. It is used when an analyst has completed several valuation exercises—such as Comparable Company Analysis, Precedent Transactions Analysis, Discounted Cash Flow (DCF) analysis, and perhaps LBO analysis—and needs to summarize the findings for clients or management, presenting a clear graphical overview of the company's estimated value range.

## The 30-second version

A football field chart is a type of stacked or floating bar chart that lines up different valuation ranges vertically, resembling the yard lines on an American football field. It typically displays the low, high, median, and average values for each valuation methodology. By plotting these different methods on the same chart, you can quickly assess whether a company is potentially overvalued or undervalued relative to its current share price, and determine an overarching consensus valuation range.

## The full explanation

A football field diagram acknowledges a fundamental truth in finance: it is naive to believe a single valuation amount is perfectly accurate. Instead, companies are valued using multiple methodologies.

The chart brings these methodologies together. Each bar represents a different technique (e.g., DCF, Trading Comps, Transaction Comps, LBO). The key components of the chart include:
- **Low and High Ends:** The minimum and maximum calculated valuations for a given methodology.
- **Percentile Ranges:** Real-world banking charts often incorporate percentile boundaries (e.g., 25th percentile, median, 75th percentile) rather than just absolute minimums and maximums, providing a more robust view of the standard distribution of peers or precedent deals.
- **Current Share Price Line:** For public companies, a dynamic line indicating the company's current stock price is usually overlaid. If the current share price sits above most of the bars, the company is likely overvalued; if below, it is undervalued.

Creating this chart requires assembling the outputs of each methodology, often using a bridge to convert Enterprise Value back to Equity Value or a per-share price, to ensure all bars are comparable.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

While conceptually simple, building a flexible football field in Excel can be somewhat painful without macros or add-ins.
The basic setup usually involves a **Stacked Bar Chart** (or a High-Low-Close Stock chart).
A common trick to construct the bars properly is to calculate the "increments" or "distances" between data points (e.g., 25th Percentile minus the Minimum). The base of the stack is plotted as an invisible series to push the visible segments (the increments) out to the correct starting point on the axis. Furthermore, adding data labels requires mapping the absolute high/low values to the increments so the labels display the actual valuation amounts.

Advanced templates are built horizontally for greater flexibility and include dynamic lines for current share prices that update automatically. Add-ins like Macabacus can automate the generation of these charts.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- **Failing to use consistent metrics:** Ensure all methodologies are mapped to the same metric (e.g., all implied share prices or all Enterprise Values). Mixing equity value per share with total Enterprise Value will ruin the chart.
- **Ignoring percentiles:** Simply using the absolute min and max of a comp set often results in artificially wide, meaningless ranges due to outliers. Use 25th/75th percentiles to tighten the ranges.
- **Hardcoding values:** A good model should dynamically link the chart data to the valuation outputs and the share price, avoiding manual updates if assumptions change.

## Sources

- [[Macabacus - Building a Football Field Chart in Excel]]
- [[BIWS - Football Field Valuation- Excel Template, Tutorial, and Full Explanation]]
- [[Project Finance - Football Field Diagrams]]
