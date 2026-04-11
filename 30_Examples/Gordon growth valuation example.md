---
type: example
title: "Gordon growth valuation example"
illustrates: ["[[Gordon growth method]]"]
updated: 2026-04-11
---

# Gordon growth valuation example

## Setup

We are calculating the terminal value of a mature manufacturing business at the end of a 5-year explicit DCF forecast period to find its continuing value.

## Assumptions

- Free Cash Flow in final projection year (Year 5, $FCF_n$): $100 million
- Weighted Average Cost of Capital (WACC): 10.0%
- Perpetual growth rate ($g$): 3.0%

## Walk-through

1. Calculate the Free Cash Flow for the first year of the terminal period (Year 6).
   - $FCF_6 = FCF_5 \times (1 + g)$
   - $FCF_6 = \$100 \text{ million} \times 1.03 = \$103 \text{ million}$
2. Calculate the capitalization rate (the spread between WACC and the growth rate).
   - $\text{Capitalization Rate} = WACC - g$
   - $\text{Capitalization Rate} = 0.10 - 0.03 = 0.07$
3. Divide the Year 6 cash flow by the capitalization rate.
   - $\text{Terminal Value} = \frac{\$103 \text{ million}}{0.07} = \$1,471 \text{ million}$

## Result

The terminal value of the business is $1,471 million.

## What this teaches

- The numerator requires the cash flow from the *first year after* the projection period, not the final projection year itself.
- The terminal value is calculated as of the end of the projection period (Year 5). To find its contribution to present Enterprise Value today, this $1,471 million must then be discounted back to Year 0.
