---
type: concept
title: P/E ratio
aliases: ["Price/Earnings", "Price to Earnings ratio"]
tags: [valuation, multiple, equity-value]
difficulty: beginner
prerequisites: ["[[Equity value]]", "[[Net income]]"]
related: ["[[Trading multiples]]", "[[EV-EBITDA]]"]
sources: ["[[IB Interview Questions - Common Valuation Multiples Explained]]", "[[Damodaran - WSJ.com -- Commentary]]", "[[Damodaran - adamodar_New_Home_Page_articles_PErates_htm]]", "[[Financial Modeling NYC - Price-Earnings Ratio (P-E Ratio) - Financial Modeling New York]]"]
status: draft
updated: 2026-04-12
---

# P/E ratio

> **TL;DR.** The P/E (Price-to-Earnings) ratio compares a company's current share price to its earnings per share (EPS), indicating how much investors are willing to pay for each dollar of earnings.

## When you'd use this

You'd use the P/E ratio when comparing the valuation of publicly traded companies, particularly when assessing whether a stock is overvalued or undervalued relative to its peers. It is most useful for companies with positive earnings and similar capital structures. It is heavily utilized in Comparable Company Analysis and is often the primary valuation metric discussed in financial media.

## The 30-second version

The Price-Earnings Ratio is a simple equity valuation multiple that tells you how much the market values a company per dollar of net income it generates. A P/E of 20x means investors are paying twenty times the company's annual net income. High P/E ratios typically reflect high expected growth rates, while low P/E ratios might suggest the stock is undervalued or that growth expectations are poor. Notably, analysts generally prefer the "Forward P/E" (based on estimated future earnings) over trailing P/E, as markets are inherently forward-looking.

## The full explanation

### An Equity Multiple
The P/E ratio is the most widely recognized equity multiple. Unlike enterprise value multiples (like EV/EBITDA), which are capital-structure neutral, equity multiples compare the equity value of the business to a metric that flows directly to shareholders (Net Income).

### Influence of Interest Rates and Inflation
There is an inverse relationship between interest rates and P/E ratios. When long-term interest rates are very low, fixed income provides less return, meaning higher P/E ratios are warranted as investors are willing to pay a premium for equity earnings. Conversely, high rates of inflation and higher bond yields increase the perceived risk, leading to multiple contraction where P/E ratios should theoretically be lower.

### Drivers of P/E
At its core, a P/E multiple is driven by growth expectations, risk (cost of equity), and payout ratios. While simple to calculate, the ratio relies heavily on reported net income, which can be obscured by non-recurring items, varying depreciation policies, or different tax jurisdictions.

## Formula

![[P-E ratio formula]]

## Worked example

If a company’s share price is $50 and its earnings per share (EPS) is $5, its P/E ratio is 10x ($50 / $5 = 10).

## Excel and modeling notes

When performing accretion/dilution analysis in stock-for-stock M&A, the P/E ratio is particularly useful. If an acquirer's P/E multiple is higher than the target's, the deal is typically accretive to the acquirer's Earnings Per Share (EPS), holding all else equal.

## Interview-ready answer

"The P/E ratio is an equity valuation multiple that measures a company's market capitalization relative to its net income, or its share price relative to EPS. While it's the most widely quoted multiple and helpful for comparing similar companies, its main weakness is that it's heavily influenced by capital structure. Since interest expense reduces net income, two operationally identical companies with different debt levels will have different P/E ratios."

## Pitfalls and gotchas

- **Capital Structure Differences:** Two operationally identical companies with different leverage will show different P/E ratios because interest expense directly affects net income. This is why EV/EBITDA is often preferred for comparing companies with differing debt levels.
- **Negative Earnings:** P/E ratios are useless for unprofitable companies.
- **One-Time Items:** Net income can be distorted by one-time or nonrecurring expenses. Analysts often adjust earnings to calculate a "normalized" P/E ratio.

## Sources

- [[IB Interview Questions - Common Valuation Multiples Explained]]
- [[Damodaran - WSJ.com -- Commentary]]
- [[Damodaran - adamodar_New_Home_Page_articles_PErates_htm]]
- [[Financial Modeling NYC - Price-Earnings Ratio (P-E Ratio) - Financial Modeling New York]]
