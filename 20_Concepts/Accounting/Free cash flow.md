---
type: concept
title: "Free cash flow"
aliases: ["FCF", "Unlevered Free Cash Flow", "UFCF", "Levered Free Cash Flow"]
tags: ["accounting", "cash-flow", "valuation", "modeling"]
difficulty: intermediate
prerequisites: ["[[Cash from operations]]", "[[EBITDA]]", "[[EBIT]]", "[[Capital expenditures]]"]
related: ["[[DCF valuation]]", "[[Enterprise value]]", "[[Equity value]]"]
sources: ["[[BIWS - How to Calculate Free Cash Flow + Excel Examples]]", "[[BIWS - Unlevered Free Cash Flow: Formulas, Calculations, and Full Tutorial]]", "[[BIWS - EBITDA to FCF: Full Tutorial, Examples, and Excel Files]]", "[[BIWS - Free Cash Flow Conversion Analysis]]", "[[IB Interview Questions - How to Link the Three Financial Statements (Explained)]]"]
status: draft
updated: 2026-04-10
---

# Free cash flow

> **TL;DR.** Free cash flow is the cash a company generates after accounting for cash outflows to support operations and maintain its capital assets.

## When you'd use this

You use Free Cash Flow (FCF) as the fundamental metric in valuation models, such as the Discounted Cash Flow (DCF) analysis, and when assessing a company's capacity to pay down debt in LBO models. It represents the true cash a business produces that is available to distribute to its investors (both debt and equity holders) without impacting the core operations.

## The 30-second version

While metrics like Net Income or EBITDA provide insight into a company's profitability, they can be misleading because they ignore crucial cash outflows like capital expenditures and changes in working capital. Free Cash Flow rectifies this by measuring the actual cash left over after a business pays for its operating expenses and capital investments. Depending on the context—such as valuing the entire firm versus just the equity—analysts calculate different variations of FCF, most notably Unlevered Free Cash Flow (available to all investors) and Levered Free Cash Flow (available only to equity investors).

## The full explanation

Free Cash Flow is a more accurate proxy for a company's cash-generating ability than accounting profits. It indicates the true discretionary cash flow that can be used to pay dividends, buy back stock, pay down debt, or acquire other companies.

### Unlevered Free Cash Flow (Free Cash Flow to Firm)
Unlevered Free Cash Flow (UFCF) is the cash flow available to *all* investors in the company—both debt and equity holders. It evaluates the company's core operations, ignoring the impact of its capital structure (i.e., it excludes interest expense). UFCF is the standard metric projected in a typical DCF to calculate a company's Enterprise Value. The calculation starts with operating income (EBIT), deducts taxes to get Net Operating Profit After Taxes (NOPAT), adds back non-cash expenses like Depreciation & Amortization, adjusts for changes in Net Working Capital, and subtracts Capital Expenditures.

### Levered Free Cash Flow (Free Cash Flow to Equity)
Levered Free Cash Flow represents the cash available solely to the equity investors after all debt obligations (interest and mandatory principal repayments) have been met. It is used to determine Equity Value directly.

### FCF Conversion
FCF Conversion is the ratio of Free Cash Flow to EBITDA or Net Income. It measures how efficiently a company turns its accounting profits into actual cash. A high FCF conversion rate indicates strong cash generation, which is highly attractive to lenders and private equity firms looking for LBO candidates because it means the company can consistently service debt.

## Formula

![[Free cash flow formula]]

## Worked example

(none)

## Excel and modeling notes

When building a model, pay close attention to the components of the Change in Working Capital. Only operating current assets and liabilities should be included; cash and debt items are strictly excluded. Also, ensure that CapEx figures encompass all necessary investments to sustain and grow operations, including the purchase of intangible assets if they are a regular part of the business model.

## Interview-ready answer

[[Walk me through calculating Free Cash Flow from EBITDA]]

## Pitfalls and gotchas

- Not clarifying whether you are discussing Unlevered or Levered Free Cash Flow; they serve different purposes and use different discount rates (WACC vs. Cost of Equity).
- Failing to deduct Capital Expenditures when trying to measure a company's true discretionary cash.
- Adding back non-cash items like Stock-Based Compensation incorrectly; while non-cash, it has real dilutive effects on equity investors and is often treated differently depending on the analysis.
- Confusing FCF with Cash Flow from Operations, which does not deduct CapEx.

## Sources

- [[BIWS - How to Calculate Free Cash Flow + Excel Examples]]
- [[BIWS - Unlevered Free Cash Flow: Formulas, Calculations, and Full Tutorial]]
- [[BIWS - EBITDA to FCF: Full Tutorial, Examples, and Excel Files]]
- [[BIWS - Free Cash Flow Conversion Analysis]]
- [[IB Interview Questions - How to Link the Three Financial Statements (Explained)]]
