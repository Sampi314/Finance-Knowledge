---
type: example
title: "Future value of a $100,000 deposit"
illustrates: ["[[Future value]]"]
updated: 2026-04-09
---

# Future value of a $100,000 deposit

## Setup

We want to calculate how much an initial cash deposit of $100,000 will be worth after 10 years to understand the impact of varying compounding frequencies.

## Assumptions

- Initial deposit (Present Value): $100,000
- Annual interest rate ($r$): 5.0%
- Investment horizon ($t$): 10 years
- Scenarios: Annual, Semi-Annual, Quarterly, Monthly, and Daily compounding frequencies.

## Walk-through

1.  **Annual Compounding ($n = 1$):**
    $FV = \$100,000 \times (1 + \frac{0.05}{1})^{(1 \times 10)} = \$162,889$
2.  **Semi-Annual Compounding ($n = 2$):**
    $FV = \$100,000 \times (1 + \frac{0.05}{2})^{(2 \times 10)} = \$163,862$
3.  **Quarterly Compounding ($n = 4$):**
    $FV = \$100,000 \times (1 + \frac{0.05}{4})^{(4 \times 10)} = \$164,362$
4.  **Monthly Compounding ($n = 12$):**
    $FV = \$100,000 \times (1 + \frac{0.05}{12})^{(12 \times 10)} = \$164,701$
5.  **Daily Compounding ($n = 365$):**
    $FV = \$100,000 \times (1 + \frac{0.05}{365})^{(365 \times 10)} = \$164,866$

## Result

With monthly compounding, the future value of the deposit is $164,701, representing a total interest earned of $64,701 over the 10 years.

## What this teaches

- Compounding interest means earning interest on your accrued interest.
- As the frequency of compounding increases (from annual to daily), the future value of the investment also increases.
- The difference between annual and daily compounding over 10 years on a $100,000 deposit is almost $2,000, demonstrating that the compounding schedule can significantly impact long-term returns.
