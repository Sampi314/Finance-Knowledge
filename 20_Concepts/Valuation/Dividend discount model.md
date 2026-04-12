---
type: concept
title: "Dividend discount model"
aliases: ["DDM", "Dividend Discount Model"]
tags: ["valuation", "intrinsic-valuation", "cost-of-equity", "Gordon-Growth-Model"]
difficulty: intermediate
prerequisites: ["[[Gordon growth method]]", "[[Cost of equity]]", "[[Terminal value]]"]
related: ["[[DCF valuation]]", "[[Gordon growth method]]"]
sources: ["[[Wall Street Prep - Dividend Discount Model (DDM) - Formula + Calculator]]", "[[BIWS - Dividend Discount Model Example for Banks - Shawbrook]]", "[[CFI - One-Period Dividend Discount Model - Overview, Formula, Example]]", "[[Macabacus - Advantages of the Dividend Discount Model (DDM)- Formula, Examples Macabacus]]"]
status: draft
updated: 2026-04-12
---

# Dividend discount model

> **TL;DR.** The dividend discount model (DDM) is an intrinsic valuation method that estimates the true value of a company by summing all of its future expected dividend payments, discounted back to their present value.

## When you'd use this

You would use the dividend discount model (DDM) when evaluating large, mature companies with a consistent track record of paying out dividends, such as commercial banks. It is especially useful when an investor is focusing solely on the actual cash returns directly provided to shareholders (dividends).

## The 30-second version

The DDM operates on the premise that today's stock price represents the discounted value of all expected future dividend payments. By forecasting the company's future dividends using a set dividend growth rate, and discounting those payments using the firm's cost of equity (the minimum return required by equity holders), you can calculate an intrinsic value per share. If this intrinsic value is greater than the current stock price, the stock is considered undervalued.

## The full explanation

The dividend discount model (DDM) is an intrinsic valuation approach similar to a Discounted Cash Flow (DCF) model, but instead of using free cash flows, it assumes that the only real "cash flows" received by shareholders are dividends. Therefore, projecting dividend payments and the growth of those payments are the main factors in the DDM approach.

The model comes in several variations based on how the growth rate is structured:
- **Zero Growth DDM**: Assumes the dividend remains constant into perpetuity.
- **Gordon Growth DDM**: Often called the constant growth model, assumes a fixed perpetual dividend growth rate.
- **Multi-Stage DDM (e.g., Two-Stage or Three-Stage)**: Assumes an initial period of higher, unsustainable growth, followed by a transition into a lower, stable long-term growth rate.

For a multi-stage model, such as those typically applied to commercial banks, the valuation is split into the initial explicit forecast period, and a terminal value calculation that represents the present value of all future dividends once the company reaches its mature, stable state.

## Formula

The intrinsic value per share is mathematically expressed as:

$$Intrinsic\ Value\ Per\ Share\ =\ \frac{D_{1}}{(k_e - g)}$$

For a multi-stage DDM, you calculate the explicit present value (PV) of each individual dividend during the high-growth stage, and then add the discounted Terminal Value (using the above Gordon Growth style formula) for the stable-growth stage.

## Worked example

Consider a two-stage dividend discount model with the following assumptions:
- **Dividends Per Share (DPS) – Current Period**: $2.00
- **Cost of Equity (Ke)**: 6.0%
- **Dividend Growth Rate (g) – Stage 1 (Years 1-5)**: 5.0%
- **Dividend Growth Rate (g) – Stage 2 (Perpetuity)**: 3.0%

1. Calculate the explicit PV of each dividend in Stage 1 by growing the $2.00 dividend by 5% each year, and discounting it by dividing by $(1 + 6.0\%)^{Period}$. The sum of these explicitly discounted dividends equals $9.72.
2. For Stage 2, calculate the Year 6 dividend: $\$2.55 \times (1 + 3.0\%) = \$2.63$.
3. Calculate the Terminal Value in Year 5: $\$2.63 \div (6.0\% - 3.0\%) = \$87.64$.
4. Discount the Terminal Value back to the present: $\$87.64 \div (1 + 6.0\%)^5 = \$65.49$.
5. Add the PV of Stage 1 to the PV of Stage 2 to get the intrinsic value per share: $\$9.72 + \$65.49 = \$75.21$.

## Excel and modeling notes

When building a DDM in Excel, break the model into three distinct stages if modeling banks: Development Growth, Maturity Growth (where ROE converges to the cost of equity), and Terminal Growth. Use sensitivity analysis tables to flex the crucial variables, as small changes in the cost of equity or the terminal growth rate will swing the valuation dramatically.

## Interview-ready answer

The dividend discount model is an intrinsic valuation technique that values a company based on the present value of its future dividend payments. It is most commonly applied to mature companies with stable, predictable dividend payout histories, such as commercial banks.

## Pitfalls and gotchas

- The DDM is incredibly sensitive to assumptions; small tweaks to the long-term dividend growth rate or the cost of equity can result in vastly different stock valuations.
- Making accurate long-term dividend projections is difficult, as it fails to account for potential strategic shifts, economic downturns, or changes in dividend policy.
- The model ignores value generated from reinvesting earnings (retained earnings) at high-growth firms and is very difficult to apply to companies that do not currently pay a dividend.

## Sources

- [[Wall Street Prep - Dividend Discount Model (DDM) - Formula + Calculator]]
- [[BIWS - Dividend Discount Model Example for Banks - Shawbrook]]
- [[CFI - One-Period Dividend Discount Model - Overview, Formula, Example]]
- [[Macabacus - Advantages of the Dividend Discount Model (DDM)- Formula, Examples Macabacus]]
