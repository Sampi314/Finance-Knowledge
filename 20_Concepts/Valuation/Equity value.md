---
type: concept
title: "Equity value"
aliases: ["Market capitalization", "Market cap"]
tags: ["valuation", "corporate-finance", "m-and-a"]
difficulty: beginner
prerequisites: []
related: ["[[Enterprise value]]"]
sources: ["[[Financial Modeling NYC - Equity Value - Financial Modeling New York]]", "[[IB Interview Questions - Enterprise Value vs Equity Value- Complete Guide]]", "[[Wall Street Prep - Equity Value - Formula + Calculator]]", "[[Sapphire 45 - Enterprise Value vs Equity Value- Key Differences Explained]]"]
status: draft
updated: 2026-04-11
---

# Equity value

> **TL;DR.** Equity value is the total value of a company's shares owned by its shareholders, representing the residual value of assets after all liabilities are paid.

## When you'd use this

You would use equity value when determining the market price of a public company's shares or the total value of ownership belonging specifically to equity holders. It is heavily used in valuation multiples like Price-to-Earnings (P/E) or Price-to-Book (P/B), assessing the value of ownership stakes during fundraising, evaluating shareholder wealth, and determining the price an acquirer pays to shareholders in an M&A transaction.

## The 30-second version

Equity value, often known as market capitalization for public companies, represents the total value of a company that is strictly attributable to its common shareholders. It is a measure of what the owners actually own after accounting for debts and other obligations. You can think of it as the residual claim that equity investors have on the business once all other stakeholders (like debt holders or preferred stock holders) are satisfied. For public firms, it's calculated simply by multiplying the share price by the number of outstanding shares. For private companies, it's estimated using valuation models or the enterprise value bridge.

## The full explanation

### What is Equity Value?
Equity value is the value of a company available to its common shareholders. In the public markets, it is synonymous with **market capitalization** (or market cap). It differs from **enterprise value**, which represents the value of the company's core operations to *all* capital providers (including debt and preferred equity holders).

Equity value provides the perspective of the shareholder. When you look at a company's stock price and multiply it by the fully diluted shares outstanding, you are calculating the equity value. It is inherently affected by the capital structure of the business because any debt taken on or paid down shifts the equity value.

### Connecting Equity Value to Enterprise Value (The Bridge)
In investment banking and corporate finance, the relationship between equity value and enterprise value is known as "the bridge."

When an acquirer buys a company, they do not just buy the equity; they assume the company's entire capital structure, including its debts. The enterprise value represents this true acquisition cost. To go from enterprise value back to the value remaining for equity shareholders, you must subtract the non-equity claims and add back non-operating assets.

- **Subtract Debt:** Debt holders have a priority claim on the company's assets. You must deduct all interest-bearing obligations (short-term debt, long-term debt, capital leases).
- **Subtract Preferred Stock:** Preferred shareholders are paid before common shareholders, so their claims reduce the value available to common equity.
- **Subtract Non-Controlling Interest (Minority Interest):** If a company consolidates a subsidiary but doesn't own 100% of it, the portion owned by outside investors must be subtracted, as it doesn't belong to the parent company's common shareholders.
- **Add Cash:** Cash and cash equivalents belong to the company and can theoretically be used to pay off debt or distribute to shareholders, so they increase the equity value.

### Why It Matters
Equity value is crucial for several reasons:
- **Shareholder Wealth:** It directly reflects the wealth of the common shareholders.
- **Valuation Multiples:** It serves as the numerator for equity-based valuation multiples (like P/E and P/B ratios) where the denominator (like Net Income) is also a metric available strictly to equity holders.
- **Fundraising and Ownership:** In private markets, founders and investors use equity value to determine the price of an ownership stake and measure dilution during new funding rounds.

## Formula

![[Equity Value]]

## Worked example

If a company has 10 million outstanding shares and each share is trading at $50, then its equity value is $500 million ($10 \text{ million} \times \$50$).

Alternatively, using the bridge: If a company has an Enterprise Value of $700 million, Debt of $250 million, Preferred Stock of $50 million, and Cash of $100 million:
$\text{Equity Value} = \$700\text{M (EV)} - \$250\text{M (Debt)} - \$50\text{M (Preferred)} + \$100\text{M (Cash)} = \$500\text{ million}$

## Excel and modeling notes

- When calculating equity value for a public company, always use **fully diluted shares outstanding**. This involves calculating basic shares and adding the dilutive effect of options, warrants, and convertible securities, typically using the Treasury Stock Method (TSM).
- When using the EV bridge, use the latest balance sheet to find values for Debt, Preferred Stock, Minority Interest, and Cash, but use the current market price for the shares.

## Interview-ready answer

"Equity value represents the value of a company that belongs strictly to its common shareholders. For a public company, it is calculated as the current share price multiplied by the fully diluted shares outstanding. You can also calculate it by taking Enterprise Value, adding Cash, and subtracting Debt, Preferred Stock, and Non-Controlling Interest."

## Pitfalls and gotchas

- **Mismatching multiples:** A common mistake is pairing equity value with enterprise metrics. Equity value must only be paired with equity metrics (e.g., Net Income), while Enterprise Value should be paired with metrics available to all stakeholders (e.g., EBITDA or EBIT).
- **Using basic instead of diluted shares:** Forgetting to calculate fully diluted shares outstanding using the Treasury Stock Method will result in an understated equity value.
- **Confusing equity value with book value of equity:** Equity value is the *market* value of the equity, which is generally quite different (and usually higher) than the accounting "shareholders' equity" found on a balance sheet.

## Sources

- [[Financial Modeling NYC - Equity Value - Financial Modeling New York]]
- [[IB Interview Questions - Enterprise Value vs Equity Value- Complete Guide]]
- [[Wall Street Prep - Equity Value - Formula + Calculator]]
- [[Sapphire 45 - Enterprise Value vs Equity Value- Key Differences Explained]]
