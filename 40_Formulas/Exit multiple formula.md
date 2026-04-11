---
type: formula
title: "Exit multiple formula"
used_in: ["[[Exit multiple method]]"]
updated: 2026-04-11
---

# Exit multiple formula

$$ \text{Terminal Value} = \text{EBITDA}_{n} \times \text{Exit Multiple} $$

**Variables**

- $\text{Terminal Value}$ — The estimated value of a business beyond the explicit forecast period.
- $\text{EBITDA}_{n}$ — Earnings Before Interest, Taxes, Depreciation, and Amortization in the final projection year ($n$). Note that EBIT or other financial metrics can also be used depending on the business type.
- $\text{Exit Multiple}$ — The valuation multiple applied, usually determined by looking at current trading multiples of comparable public companies or recent M&A transaction multiples.

**Notes**

While this formula calculates the future terminal value at year $n$, to determine the present value for a DCF, this terminal value must then be discounted back to the present day using the company's Weighted Average Cost of Capital (WACC): $PV = \frac{\text{Terminal Value}}{(1 + WACC)^n}$.
