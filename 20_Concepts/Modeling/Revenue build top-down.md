---
type: concept
title: "Revenue build top-down"
aliases: ["Top-down forecasting", "Top-down revenue build", "Top-down analysis", "Top-down budgeting"]
tags: ["modeling", "forecasting", "revenue", "assumptions"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[CFI - Top-Down Forecasting - Overview, Example, Steps]]", "[[Wall Street Prep - Bottom Up Forecasting - Formula + Calculator]]", "[[Macabacus - Building a Startup Financial Model]]", "[[CFI - Top-Down Budgeting - Definition, Example, Vs. Bottom Up]]", "[[CFI - Top-Down Analysis - Definition, Breakdown, Risks]]"]
status: draft
updated: 2026-04-12
---

# Revenue build top-down

> **TL;DR.** A forecasting method that estimates a company's revenue by starting with the total addressable market (TAM) size and applying a projected market share percentage.

## When you'd use this

You would use a top-down revenue build when forecasting revenues for early-stage startups that lack historical financial data or operating metrics. It is also used when a company enters a new market, launches a novel product, or operates in a rapidly growing, nascent industry where macro-level industry data is more reliable or easier to obtain than micro-level unit economics.

## The 30-second version

A top-down revenue build projects future revenue by looking at the big picture rather than internal company metrics. You start by determining the Total Addressable Market (TAM), which represents the total revenue opportunity if a company achieved 100% market share. Then, you estimate the percentage of that market the company realistically expects to capture over time. Multiplying the TAM by the estimated market share yields the company's projected revenue. It is a quick way to gauge the potential upside of a business, though it often requires a sanity check against bottom-up models.

## The full explanation

Top-down forecasting starts with macroeconomic indicators or broad industry data and "trickles down" to a specific company's revenue. Unlike bottom-up forecasting, which builds up revenue from unit prices and customer volume, the top-down approach focuses on market size and penetration.

### 1. Determining Total Addressable Market (TAM)
The first step is sizing the overall market. Analysts typically rely on industry reports, third-party research (like Gartner or Statista), or macroeconomic data (like GDP or sector-specific spending) to find the TAM. For a company with multiple distinct business segments, you must find the TAM for each segment individually.

### 2. Estimating Market Share
Once the total market size is established, you forecast the percentage of the market the company will capture. For example, if a startup is entering a $10 billion industry, you might assume they will capture 1% of the market by Year 3 and 5% by Year 5. This is often the most subjective part of the analysis, as it relies heavily on assumptions about competitive advantages, marketing effectiveness, and industry dynamics.

### 3. Calculating Revenue
The estimated market share is multiplied by the TAM to project revenue. As the company scales, market share growth might follow an S-curve or other non-linear paths, especially in businesses that benefit from network effects.

### Top-Down vs. Bottom-Up
While top-down models estimate share of a large market, bottom-up models start with specific operating drivers (e.g., website traffic, conversion rates, average order value). Top-down methods are better for long-term forecasting and understanding the total market opportunity, whereas bottom-up approaches provide more operational granularity for short-term budgeting and resource allocation. Often, analysts use both methods to triangulate a more realistic forecast.

## Formula

The core calculation for a top-down revenue forecast is:

$$ \text{Revenue} = \text{Total Addressable Market (TAM)} \times \text{Estimated Market Share (\%)} $$

## Worked example

Imagine a startup launching a new e-commerce platform for pet supplies.
1. **Total Addressable Market:** Industry reports indicate the total e-commerce pet supply market is currently $20 billion and is expected to grow by 5% annually. By Year 3, the TAM is projected to be $23.15 billion.
2. **Market Share:** The startup estimates that through aggressive marketing, it can capture 0.5% of the market by Year 3.
3. **Revenue:**
   Year 3 Revenue = $23.15 billion × 0.5% = $115.75 million.

## Excel and modeling notes

- **Sanity check the market share:** Even a "conservative" 1% or 2% market share of a massive market can imply unreasonably high absolute revenue figures for a new business. Always compare the implied revenue against operational realities (e.g., "Do we have the capacity to serve that many customers?").
- **Dynamic TAM:** Ensure the TAM in your model grows or shrinks over time based on industry trends. Don't assume the market size is static.
- **Segmented modeling:** If a company operates in multiple geographies or product lines, build separate top-down forecasts for each segment and sum them up, rather than using one blended market share assumption.

## Interview-ready answer

A top-down revenue build is a forecasting approach that estimates revenue by determining the Total Addressable Market (TAM) and multiplying it by an assumed market share percentage. It is typically used for startups, new product launches, or entering new markets where historical data is unavailable. While useful for sizing the total opportunity, it is often paired with a bottom-up forecast to ensure the operational assumptions required to capture that market share are realistic.

## Pitfalls and gotchas

- **Overestimating market share:** It is easy to assume a business will capture "just 1%" of a billion-dollar market, but without a clear operational strategy to acquire those customers, that assumption is a guess, not a forecast.
- **Ignoring operational constraints:** A top-down model might project $50 million in revenue, but if the company's manufacturing capacity or sales team size can only support $10 million, the forecast is flawed.
- **Using an overly broad TAM:** Defining the market too broadly (e.g., using the entire "software industry" TAM for a niche HR tool) will artificially inflate the revenue projections.

## Sources

- [[CFI - Top-Down Forecasting - Overview, Example, Steps]]
- [[Wall Street Prep - Bottom Up Forecasting - Formula + Calculator]]
- [[Macabacus - Building a Startup Financial Model]]
- [[CFI - Top-Down Budgeting - Definition, Example, Vs. Bottom Up]]
- [[CFI - Top-Down Analysis - Definition, Breakdown, Risks]]
