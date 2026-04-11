---
type: concept
title: "Gordon growth method"
aliases: ["Perpetuity growth method", "Gordon Growth Model"]
tags: ["valuation", "dcf", "terminal-value"]
difficulty: intermediate
prerequisites: ["[[Terminal value]]", "[[WACC]]", "[[Free cash flow projection]]"]
related: []
sources: ["[[IB Interview Questions - Terminal Value- Gordon Growth vs Exit Multiple Method]]", "[[BIWS - DCF - Terminal Value - Gordon Growth Method Intuition]]"]
status: draft
updated: 2026-04-11
---

# Gordon growth method

> **TL;DR.** The Gordon growth method calculates terminal value by assuming a business continues to operate forever with cash flows growing at a constant perpetual rate.

## When you'd use this

You would use the Gordon growth method when calculating terminal value in a DCF for stable, mature businesses with predictable, sustainable growth. It is also favored in academic contexts, for long-term hold assumptions, or when there are limited comparable companies available for an exit multiple approach. It provides a purely intrinsic valuation that is not directly influenced by current market conditions.

## The 30-second version

In a DCF analysis, the explicit forecast period only lasts for a few years, but the business generates value into perpetuity. The Gordon growth method (or perpetuity growth method) values the company as an ongoing enterprise by capitalizing the final year's cash flow. It assumes this cash flow will grow at a single, constant rate forever. By dividing next year's free cash flow by the discount rate minus the growth rate, you can determine the present value of an infinite stream of growing cash flows.

## The full explanation

### Theoretical Foundation

The Gordon growth method derives from the mathematical principle that a perpetually growing stream of cash flows has a finite present value, as long as the growth rate is strictly less than the discount rate (WACC). If the growth rate equaled or exceeded the discount rate, the present value would theoretically be infinite, which is economically impossible.

The formula takes the free cash flow in the first year of the terminal period (the year immediately following the projection period) and converts it into a capitalized value by dividing it by the spread between the discount rate and the perpetual growth rate. This spread is sometimes referred to as the capitalization rate.

### Selecting the Perpetual Growth Rate

Choosing the appropriate perpetual growth rate is the most critical and heavily scrutinized assumption in the Gordon Growth Model because it must be sustainable *forever*.

1. **Economic Limits:** The growth rate cannot exceed long-term macroeconomic (GDP) growth. No company can grow faster than the overall economy indefinitely without eventually becoming the entire economy. For U.S. companies, this typically implies a cap of 2% to 3%.
2. **Inflation Floor:** The rate should generally reflect long-term inflation at a minimum. A business maintaining its real purchasing power should grow its nominal cash flows at the rate of inflation, suggesting a floor of around 2%.
3. **Industry Maturity:** Mature industries with limited growth prospects should use rates at the lower end of the spectrum.
4. **Margin Consistency:** High perpetual growth combined with stable margins implies significant reinvestment needs. Ensure your terminal assumptions are internally consistent.

## Formula

![[Gordon Growth Terminal Value]]

## Worked example

[[Gordon growth valuation example]]

## Excel and modeling notes

(none)

## Interview-ready answer

[[Why is the Gordon growth method highly sensitive to assumptions?]]

## Pitfalls and gotchas

- **Growth Rate > WACC:** Using a perpetual growth rate that is equal to or higher than the discount rate will result in a mathematically invalid (infinite or negative) terminal value.
- **Unrealistic Growth Rates:** Assuming a perpetual growth rate higher than long-term GDP growth (e.g., >3% for developed markets) implies the company will outgrow the economy forever.
- **Circular Reasoning Risk:** Relying exclusively on this method without cross-checking against the exit multiple method might lead to a valuation that is completely detached from prevailing market realities.

## Sources

- [[IB Interview Questions - Terminal Value- Gordon Growth vs Exit Multiple Method]]
- [[BIWS - DCF - Terminal Value - Gordon Growth Method Intuition]]
