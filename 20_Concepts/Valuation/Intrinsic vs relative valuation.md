---
type: concept
title: "Intrinsic vs relative valuation"
aliases: ["Intrinsic valuation", "Relative valuation"]
tags: ["valuation", "dcf", "comparables", "multiples"]
difficulty: intermediate
prerequisites: ["[[Time value of money]]", "[[Present value]]", "[[Future value]]", "[[Discount rate]]"]
related: []
sources: ["[[Damodaran - Intrinsic vs Relative Value]]", "[[Wall Street Prep - DCF Analysis - Intrinsic Value Pros and Cons]]", "[[CFI - Intrinsic Value - Learn How to Calculate Intrinsic Value of a Business]]"]
status: draft
updated: 2026-04-11
---

# Intrinsic vs relative valuation

> **TL;DR.** Intrinsic valuation estimates the absolute worth of an asset based on its future cash flows and risk, while relative valuation estimates worth by comparing the asset to the market prices of similar assets.

## When you'd use this

You use intrinsic valuation when you need an absolute, fundamental estimate of an asset's value that is independent of current market sentiment, often for long-term investing or evaluating fundamental business performance. You use relative valuation when you want a quick, market-based estimate of what a company should be worth today, based on how its peers are currently trading. In practice, both methods are often used together to provide a range of valuation estimates.

## The 30-second version

Intrinsic valuation, typically performed using a Discounted Cash Flow (DCF) model, calculates the present value of a company's expected future free cash flows. It relies heavily on assumptions about future growth, profitability, and the cost of capital. Because it's based on fundamentals, it ignores whether the market is currently overvaluing or undervaluing assets.

Relative valuation, often called "comps" (comparable company analysis) or "multiples," values an asset by looking at the prices of similar assets. It standardizes prices using a metric like earnings or revenue (e.g., the Price-to-Earnings or EV/EBITDA ratio). It assumes the market is pricing similar assets correctly on average.

## The full explanation

### Intrinsic Valuation

In intrinsic valuation, the value of an asset is a function of its expected cash flows, its growth potential, and its risk profile. The core idea is that an asset with high, predictable cash flows is worth more than an asset with low, volatile cash flows.

The most common approach to intrinsic valuation is the **Discounted Cash Flow (DCF)** analysis. The DCF values a company by projecting its future free cash flows and discounting them back to their present value using an appropriate discount rate (the required rate of return or cost of capital).

**Pros of Intrinsic Valuation:**
*   **Fundamentals-Oriented:** It relies on explicit assumptions about the business's specific drivers—revenue growth, margins, reinvestment needs, and risk.
*   **Market-Independent:** It focuses on what the business is fundamentally worth, unaffected by temporary market distortions, irrational exuberance, or panic.
*   **Self-Sufficient:** It doesn't require the existence of comparable peers, making it suitable for unique companies or "pure-plays".

**Cons of Intrinsic Valuation:**
*   **High Sensitivity to Assumptions:** The old adage "garbage in, garbage out" applies heavily. Minor tweaks to the discount rate or long-term growth rate can wildly change the output.
*   **Terminal Value Weight:** A significant portion of the total value (often 75% or more) comes from the "Terminal Value"—the estimated value of the company beyond the explicit forecast period. This relies on simplified assumptions, like a constant perpetuity growth rate.

### Relative Valuation

While intrinsic valuation is academically rigorous, relative valuation is far more prevalent in practice. Relative valuation values an asset based on how the market prices similar, comparable assets. It essentially trusts that the market gets the pricing right, at least on average.

To compare companies of different sizes, relative valuation standardizes prices using a common variable, creating a multiple. For example, dividing a company's Enterprise Value by its EBITDA yields the EV/EBITDA multiple. If the average comparable company trades at 10x EV/EBITDA, you might apply that multiple to the target company's EBITDA to estimate its value.

**Common variations of relative valuation:**
*   **Direct Comparison:** Finding a nearly identical company and using its pricing.
*   **Peer Group Average:** Comparing the target to the average multiple of a sector or peer group.
*   **Adjusted Comparisons:** Adjusting multiples based on differences in fundamentals. For example, using the PEG ratio (Price/Earnings divided by Growth) to control for different growth rates among peers.

**Pros of Relative Valuation:**
*   **Market-Reflective:** It reflects current market conditions and what investors are actually willing to pay today.
*   **Efficiency:** It requires fewer explicit assumptions about the distant future and is generally much faster to perform than a full DCF.

**Cons of Relative Valuation:**
*   **Hard to Find True Comparables:** No two companies are exactly alike in risk, growth, and cash flow profiles.
*   **Market Errors:** If the entire sector is overvalued (like tech stocks in 1999), relative valuation will simply confirm the overvaluation. It doesn't capture whether the baseline market pricing is irrational.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

In financial modeling, both intrinsic and relative valuation methods are typically presented together in a "Football Field" chart. This chart visually displays the range of implied share prices generated by different valuation methods (e.g., a DCF sensitivity range, comparable companies, and precedent transactions), providing a holistic view of the company's value rather than a single point estimate.

## Interview-ready answer

Intrinsic valuation, like a DCF, estimates a company's absolute worth based on its projected future cash flows and the risk of those cash flows, independent of the broader market. Relative valuation, like comparable company analysis, estimates worth by looking at how the market is currently pricing similar peers using standardized multiples like EV/EBITDA. In practice, they are used together: the DCF provides a fundamental check, while relative valuation grounds the estimate in current market realities.

## Pitfalls and gotchas

- **Relying solely on one method:** Depending entirely on a DCF might lead to a valuation far removed from reality if assumptions are flawed, while relying only on comps might blind you to an entire sector being fundamentally overvalued.
- **Forcing comparables:** Using peers that operate in different geographies, have drastically different margin profiles, or face different regulatory risks will distort a relative valuation.
- **Treating the DCF output as a precise number:** A DCF should always be viewed as a range based on a sensitivity analysis of key variables (like WACC and terminal growth rate), not a single definitive calculation.

## Sources

- [[Damodaran - Intrinsic vs Relative Value]]
- [[Wall Street Prep - DCF Analysis - Intrinsic Value Pros and Cons]]
- [[CFI - Intrinsic Value - Learn How to Calculate Intrinsic Value of a Business]]
