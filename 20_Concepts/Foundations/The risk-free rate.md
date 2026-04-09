---
type: concept
title: "The risk-free rate"
aliases: ["Rf", "Risk-free yield", "Risk-free return"]
tags: ["foundations", "discount-rates", "valuation"]
difficulty: beginner
prerequisites: ["[[Time value of money]]", "[[Discount rate]]", "[[Risk and return basics]]"]
related: ["[[WACC]]", "[[CAPM]]", "[[Cost of equity]]", "[[Equity risk premium]]"]
sources: ["[[IB Interview Questions - How to Calculate WACC Step-by-Step]]", "[[Damodaran - adamodar_New_Home_Page_littlebook_discountrates_htm]]", "[[Damodaran - ValuationN1]]"]
status: draft
updated: 2026-04-09
---

# The risk-free rate

> **TL;DR.** The expected return on an investment with guaranteed, certain returns where no default risk exists.

## When you'd use this

You use the risk-free rate as the foundational building block for determining discount rates in valuation. It serves as the base rate in the Capital Asset Pricing Model (CAPM) to calculate the cost of equity, and it is used as the base reference point when estimating the cost of debt by adding a credit spread. Ultimately, it flows into the Weighted Average Cost of Capital (WACC) to discount future cash flows.

## The 30-second version

The risk-free rate represents the return an investor can expect from a theoretically riskless investment. It captures the time value of money—the compensation required for locking up capital for a period of time, without taking on any additional risk. Because no investment is entirely risk-free in reality, financial analysts use government bonds (like US Treasuries) as a proxy, assuming governments with control over their currency won't default. The time horizon of the bond used should match the duration of the cash flows being analyzed, with the 10-year Treasury yield being the most common benchmark in corporate valuation.

## The full explanation

### Theoretical requirements
For an investment to be considered truly "risk-free", the actual return must be exactly equal to the expected return. This requires two conditions to be met:
1. **No default risk:** The entity issuing the security must have zero probability of defaulting on its obligations. This is why government securities (from stable governments) are typically used, as they possess taxation power and control over currency printing.
2. **No reinvestment risk:** The time horizon of the security must match the time horizon of the investment being analyzed. A 6-month Treasury bill is not risk-free for a 5-year project because you don't know what rate you'll be able to reinvest at after 6 months. Even a 5-year coupon-paying bond isn't perfectly risk-free for a 5-year horizon because the intermediate coupon payments must be reinvested at unknown future rates.

### Practical proxies used in valuation
In practice, analysts use the long-term government bond yield as the proxy for the risk-free rate.
- For most standard corporate valuations and DCF models (especially in the US), the **10-year U.S. Treasury yield** is the standard benchmark.
- For longer-duration projects (like infrastructure or project finance), 20-year or 30-year Treasury yields might be used.
- For companies operating outside the US, local long-term government bond yields are used (e.g., UK long-term government bonds for a company evaluated in British Pounds), provided the local government is considered default-free.

### Adjustments for non-default-free governments
If a company operates in a country where the government is *not* considered default-free (e.g., emerging markets with lower credit ratings), the local government bond yield will include a "default spread." In these cases, the true risk-free rate can be estimated by taking the local government bond yield and subtracting the country's default spread.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

- Never hardcode the risk-free rate directly into formulas; always have it as an explicit input cell in your assumptions block.
- Keep the risk-free rate assumption internally consistent. If you use the 10-year Treasury rate for calculating the Cost of Equity via CAPM, you should use the same 10-year rate as the base for estimating the Cost of Debt.
- Ensure the currency of the risk-free rate matches the currency of your cash flow projections. If your DCF is projecting cash flows in Euros, use a Euro-denominated risk-free rate (like the German Bund), not the US Treasury rate.

## Interview-ready answer

"The risk-free rate represents the baseline return investors require just for the time value of money, assuming zero default risk. In practice, we typically use the yield on the 10-year U.S. Treasury bond for standard valuations, as the U.S. government is considered to have no default risk, and the 10-year horizon broadly aligns with the duration of cash flows in a standard DCF. This rate serves as the foundation for calculating both the cost of equity via CAPM and the cost of debt."

## Pitfalls and gotchas

- **Mismatching time horizons:** Using a short-term rate (like a 3-month T-bill) for a long-term DCF valuation. The risk-free rate duration should roughly match the cash flow duration.
- **Double counting risk:** If you are valuing a company in an emerging market, adding a default premium to the country's risk premium while *also* using the elevated local government bond rate (which already contains a default spread) double-counts the country risk.
- **Currency mismatch:** Using a U.S. risk-free rate while projecting cash flows in a foreign currency with a significantly different inflation profile.

## Sources

- [[IB Interview Questions - How to Calculate WACC Step-by-Step]]
- [[Damodaran - adamodar_New_Home_Page_littlebook_discountrates_htm]]
- [[Damodaran - ValuationN1]]
