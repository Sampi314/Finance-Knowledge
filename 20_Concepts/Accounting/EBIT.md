---
type: concept
title: "EBIT"
aliases: ["Operating Income", "Earnings Before Interest and Taxes"]
tags: ["accounting", "profitability", "valuation"]
difficulty: beginner
prerequisites: ["[[The income statement]]", "[[Operating expenses]]"]
related: ["[[EBITDA]]", "[[Net income]]"]
sources: ["[[BIWS - EBIT (Operating Income)- Meaning and Example Calculations, Exciting or No?]]", "[[CFI - EBIT - Earnings Before Interest & Taxes - What You Need To Know]]", "[[Wall Street Prep - EBIT - Formula + Calculator]]"]
status: draft
updated: 2026-04-09
---

# EBIT

> **TL;DR.** EBIT (Earnings Before Interest and Taxes) is a company's profit from its core operations, excluding the effects of its capital structure and tax rate.

## When you'd use this

EBIT is primarily used in relative valuation and financial modeling to compare the operational performance of different companies. Because it excludes interest and taxes, it provides a clean view of profitability that is unaffected by a company's debt levels or the tax jurisdiction in which it operates.

## The 30-second version

EBIT, often referred to as Operating Income, measures the profit a company generates from its core business activities. You calculate it by taking total revenue and subtracting the Cost of Goods Sold (COGS) and operating expenses (like SG&A and R&D).

By stopping before interest and taxes are deducted, EBIT allows analysts to evaluate how well a company's operations are performing on their own. This makes it a crucial metric for peer comparisons, as it strips away the impact of discretionary financing decisions (how much debt the company uses) and regional tax rates.

## The full explanation

EBIT stands for Earnings Before Interest and Taxes. On a standard income statement, it is typically synonymous with "Operating Income" or "Operating Profit," although some companies may have minor non-operating items between Operating Income and EBIT.

### Why exclude interest and taxes?

The main purpose of EBIT is to isolate the performance of the core business operations.
- **Interest expense** is a function of a company's capital structure (how much debt it has chosen to take on). Two identical businesses could have very different net incomes if one is highly levered (has a lot of debt) and the other is entirely equity-funded. EBIT ignores this difference.
- **Taxes** are determined by the jurisdictions in which a company operates and various tax loopholes. They do not reflect the underlying efficiency of the business's operations.

### EBIT vs. EBITDA

EBITDA takes EBIT a step further by also adding back Depreciation and Amortization (D&A).
- **EBIT** includes D&A, meaning it accounts for the wear and tear on a company's capital assets. It is a GAAP (Generally Accepted Accounting Principles) measure when it equals Operating Income.
- **EBITDA** excludes D&A, making it a proxy for operating cash flow, but it is a non-GAAP metric.

EBIT is generally preferred over EBITDA for capital-intensive industries where depreciation is a very real economic cost of doing business.

### Usage in Valuation

EBIT is widely used in valuation multiples, most notably the **EV/EBIT** multiple (Enterprise Value to EBIT). Because EBIT is an unlevered metric (available to both debt and equity investors), it must be paired with Enterprise Value, which represents the total value of the company's operations to all investors.

## Formula

![[EBIT]]

## Worked example

(none)

## Excel and modeling notes

When building a three-statement model, EBIT is typically the subtotal calculated after subtracting total operating expenses from gross profit. Make sure you don't inadvertently include interest income, interest expense, or taxes in this operating subtotal. If you are calculating EBIT from Net Income (bottom-up approach), you simply add back the provision for income taxes and net interest expense.

## Interview-ready answer

"EBIT, or Earnings Before Interest and Taxes, represents a company's operating profit. It's calculated as Revenue minus COGS and Operating Expenses. We use EBIT because it reflects the profitability of a company's core operations independent of its capital structure and tax environment, making it ideal for comparing peers or using in an EV/EBIT valuation multiple."

## Pitfalls and gotchas

- **Non-operating items:** Sometimes companies include non-operating income or expenses above the EBIT line. When normalizing earnings for valuation, you must adjust EBIT to exclude one-time or non-recurring items (like the sale of an asset or a legal settlement).
- **EBIT vs. Operating Income:** While often used interchangeably, strictly speaking, EBIT can include non-operating income (like interest income) if calculating bottom-up from Net Income. Operating Income should only include revenue and expenses directly related to core operations.
- **Capital intensity:** If you use EBITDA instead of EBIT to value a heavily capital-intensive business, you may overstate its profitability by ignoring the massive depreciation expenses that represent true capital costs.

## Sources

- [[BIWS - EBIT (Operating Income)- Meaning and Example Calculations, Exciting or No?]]
- [[CFI - EBIT - Earnings Before Interest & Taxes - What You Need To Know]]
- [[Wall Street Prep - EBIT - Formula + Calculator]]
