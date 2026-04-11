---
type: concept
title: "Terminal value"
aliases: []
tags: ["valuation"]
difficulty: intermediate
prerequisites: ["[[WACC]]", "[[Free cash flow projection]]", "[[DCF valuation]]"]
related: ["[[Enterprise value]]"]
sources: ["[[IB Interview Questions - Terminal Value- Gordon Growth vs Exit Multiple Method]]"]
status: draft
updated: 2026-04-11
---

# Terminal value

> **TL;DR.** Terminal value represents the estimated value of a business beyond the explicit forecast period in a discounted cash flow analysis, capturing all cash flows from the end of the projection period to infinity.

## When you'd use this

You use terminal value in a discounted cash flow (DCF) analysis because you cannot project cash flows indefinitely. It captures the ongoing value of the business at the end of the forecast period. This single number typically accounts for 60% to 80% of total enterprise value in most DCF models.

## The 30-second version

Terminal value estimates what a business is worth from the end of a DCF projection period into perpetuity. There are two standard methods for calculating it: the Gordon Growth Model and the Exit Multiple Method. The Gordon Growth Model assumes the business operates forever, with cash flows growing at a constant perpetual rate. The Exit Multiple Method assumes the business is sold at the end of the projection period for a multiple of a financial metric, typically EBITDA. Both methods aim to answer what the business is worth at the end of the projection period, but they do so using fundamentally different logic.

## The full explanation

### The Gordon Growth Model
The Gordon Growth Model (or perpetuity growth method) values the company as an ongoing enterprise with no specific exit event. It derives from the mathematical principle that a perpetually growing stream of cash flows has a finite present value, provided the growth rate is less than the discount rate.

The most critical assumption is the perpetual growth rate, which must be sustainable forever. It cannot exceed long-term GDP growth (no company can grow faster than the economy indefinitely) and should generally reflect long-term inflation, typically landing between 2% and 3% for mature U.S. companies.

### The Exit Multiple Method
The Exit Multiple Method is conceptually simpler. It assumes the business is sold at the end of the projection period based on prevailing market conditions. You estimate the future transaction value by applying a valuation multiple (e.g., EV/EBITDA) derived from comparable public companies or precedent transactions to a financial metric in the final projection year.

While this approach relies on observable market data, it implicitly assumes that current market conditions (and multiples) will remain similar at the exit date. In reality, multiples fluctuate with interest rates and market sentiment.

### Cross-Checking
In practice, most investment banking valuations calculate terminal value using both methods and present them side by side. This allows analysts to cross-check results. You can compute the implied perpetual growth rate from an exit multiple, or the implied exit multiple from a Gordon Growth assumption, to ensure your assumptions are internally consistent and realistic.

Finally, remember that the calculated terminal value represents value at the *end* of your projection period. It must be discounted back to the present value using the discount rate (WACC) over the number of projection years before adding it to the present value of the explicit cash flows.

## Formula

![[Gordon Growth Terminal Value]]

![[Exit Multiple Terminal Value]]

## Worked example

(none)

## Excel and modeling notes

When building a DCF model, a common calculation error is using the wrong year's cash flow in the Gordon Growth formula. The formula requires the cash flow for the year *after* the projection period ($FCF_{n+1}$), which is the final year cash flow times $(1 + g)$. Analysts must also ensure that their terminal assumptions are internally consistent; for example, high perpetual growth requires reinvestment, meaning free cash flow margins shouldn't remain unadjusted. Always remember to discount the terminal value back to the present value!

## Interview-ready answer

[[What are the two methods for calculating terminal value?]]

## Pitfalls and gotchas

- **Forgetting to discount:** Adding the undiscounted terminal value directly to the present value of cash flows significantly overstates enterprise value. Terminal value must be discounted back to the present.
- **Growth rate exceeds WACC or GDP:** Using a perpetual growth rate that exceeds WACC produces negative or infinite values, and a rate exceeding long-term GDP growth is economically impossible to sustain forever.
- **Mismatching metrics and multiples:** Make sure to multiply the correct metric by the appropriate multiple (e.g., apply an enterprise value multiple to EBITDA, not to net income).
- **Ignoring implied metrics:** Always calculate implied growth rates or implied multiples to cross-check your work; failing to do so misses an opportunity to validate the assumptions.

## Sources

- [[IB Interview Questions - Terminal Value- Gordon Growth vs Exit Multiple Method]]
