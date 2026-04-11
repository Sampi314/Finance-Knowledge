---
type: concept
title: "Exit multiple method"
aliases: ["Terminal exit value", "Exit multiple"]
tags: ["valuation", "dcf", "terminal-value"]
difficulty: intermediate
prerequisites: ["[[Terminal value]]", "[[DCF valuation]]", "[[WACC]]", "[[EBITDA]]"]
related: ["[[Gordon growth method]]"]
sources: ["[[CFI - Exit Multiple - Overview, Terminal Value, Perpetual Growth Method]]", "[[IB Interview Questions - Terminal Value- Gordon Growth vs Exit Multiple Method]]"]
status: draft
updated: 2026-04-11
---

# Exit multiple method

> **TL;DR.** The exit multiple method calculates the terminal value of a business by assuming it is sold at the end of the projection period for a multiple of a financial metric (like EBITDA) based on current comparable market transactions.

## When you'd use this

You'd use this method in a Discounted Cash Flow (DCF) analysis when valuing a company based on a potential transaction or sale, rather than as a perpetual ongoing enterprise. It is especially useful in M&A advisory, private equity contexts (like Leveraged Buyouts) with defined exit horizons, and in industries with robust data on active comparable company trading.

## The 30-second version

The exit multiple method attempts to find what a business will be worth at the end of an explicit forecast period (e.g., year 5) by applying a market-based valuation multiple to the final year's projected financial metric, typically EBITDA or EBIT. Instead of assuming the business generates cash flow forever (as in the Gordon Growth Method), this method simulates a sale of the company to a hypothetical buyer using multiples similar to recently acquired comparable companies.

## The full explanation

In a DCF analysis, the value of a business consists of the present value of cash flows during the forecast period plus the present value of all cash flows beyond that period, known as the terminal value. Since the forecast period typically only covers 3-5 years, terminal value frequently represents a large majority (e.g., 60% to 80%) of the total assessed enterprise value.

The exit multiple method grounds the terminal value in observable market data rather than theoretical perpetual growth rates. Analysts determine an appropriate "exit multiple" by looking at the current trading multiples of comparable public companies or the multiples paid in precedent M&A transactions. This multiple (e.g., an EV/EBITDA multiple of 8x to 12x) is then multiplied by the company's projected EBITDA or EBIT in the final year of the forecast to generate the terminal value. The terminal value is then discounted back to the present day using the company's Weighted Average Cost of Capital (WACC).

While conceptually simple and easy to communicate to non-finance audiences, the method does have implicit limitations. By applying today's comparable multiples to a future year, the analyst assumes that the prevailing market conditions and the company's growth profile will remain unchanged at exit, which is not always realistic.

## Formula

![[Exit multiple formula]]

## Worked example

(none)

## Excel and modeling notes

- For cyclical businesses, it's safer to apply an industry multiple to the average EBITDA or EBIT over the economic cycle, rather than the raw year N figure, to avoid letting a cyclical peak or trough distort the valuation.
- As a best practice, analysts often calculate the implied perpetual growth rate embedded within their exit multiple to check its validity. The formula is $g_{implied} = WACC - \frac{FCF_{n+1}}{\text{Terminal Value}}$. If the implied growth rate exceeds the overall economic growth rate, the chosen multiple may be too aggressive.

## Interview-ready answer

[[Which terminal value method is better]]

## Pitfalls and gotchas

- Applying an exit multiple to a business that is not structurally similar to the comparables (e.g., different growth rates, margins, or risk profiles) without making appropriate company-specific adjustments.
- Assuming market multiples will stay static; a multiple appropriate in today's interest rate environment might not be applicable 5 years into the future.
- Failing to sanity-check the result against the Gordon Growth Method, which can leave you with a valuation built on unrealistic long-term economic assumptions.

## Sources

- [[CFI - Exit Multiple - Overview, Terminal Value, Perpetual Growth Method]]
- [[IB Interview Questions - Terminal Value- Gordon Growth vs Exit Multiple Method]]
