---
type: concept
title: "Real estate waterfall"
aliases: ["waterfall returns schedule", "real estate distribution waterfall"]
tags: ["real-estate", "partnership-structures", "distribution-waterfall"]
difficulty: advanced
prerequisites: ["[[Levered vs unlevered IRR]]", "[[Cash-on-cash return for RE]]"]
related: []
sources: ["[[BIWS - Real Estate Waterfall Model Returns and Case Study Answers (Video)]]", "[[A Simple Model - Real Estate Distribution Waterfall Example - A Simple Model]]"]
status: draft
updated: 2026-04-17
---

# Real estate waterfall

> **TL;DR.** A real estate waterfall is a tiered distribution schedule that dictates how project cash flows are split between investors (limited partners) and developers or sponsors (general partners) based on achieved return hurdles.

## When you'd use this

You would use a real estate waterfall to structure the partnership agreement between passive investors who provide the bulk of the equity and the active developer or sponsor executing the project. It aligns incentives by providing the sponsor with a disproportionate share of the upside (the "promote") once certain return milestones, typically measured by IRR or MOIC, are hit.

## The 30-second version

In a real estate partnership, distributions are not always split straight down the middle according to the initial equity contribution (e.g., 90% LP / 10% GP). Instead, the split changes as the project's returns increase. For instance, up to a 10% IRR, cash flows might be distributed 90/10. Between a 10% and 20% IRR, the split shifts to 80/20 in favor of the developer. Above a 20% IRR, it might go to 70/30. This structure rewards the developer for outperforming return expectations.

## The full explanation

A real estate distribution waterfall is fundamentally about allocating cash flow based on performance tiers (hurdles). The general mechanism calculates how much return needs to accrue in a given period based on the IRR hurdle, tracks the beginning and ending balance of equity, and then distributes the actual cash flows (repayment) according to the defined split for that tier.

### Tiers and Hurdles

Common hurdles include:
- **Tier 1 (e.g., up to 10% IRR):** Distributions often occur pro-rata based on the initial equity invested (e.g., 90% to Limited Partners and 10% to the Developer).
- **Tier 2 (e.g., 10% to 20% IRR):** The sponsor begins to receive a "promote," meaning they take a larger share of the cash flow than their initial equity percentage (e.g., an 80/20 split).
- **Tier 3 (e.g., > 20% IRR):** The sponsor's share increases further (e.g., a 70/30 split).

Because these splits favor the developer at higher tiers, the developer's ultimate IRR will typically end up much higher than the project-level IRR or the LP's IRR if the project performs exceptionally well.

### IRR vs. MOIC Hurdles

While IRR is the standard metric for waterfall hurdles, it is highly sensitive to the time horizon. An advanced waterfall might also incorporate Multiple on Invested Capital (MOIC) hurdles to protect the LPs:
- **MOIC for Short-Term Protection:** If a sponsor sells a property very quickly at a modest absolute profit, the IRR might spike over the hurdle rate even if the total dollar return is low. A MOIC requirement ensures the LPs receive a minimum absolute multiple before the sponsor hits their promote.
- **IRR for Long-Term Protection:** Conversely, if a sponsor holds a property for a decade, they might hit a high MOIC without generating a great annualized return. IRR hurdles protect against this scenario.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When building a waterfall in Excel, calculate returns accrual by taking the beginning equity balance multiplied by the IRR hurdle percentage. The "repayment" is the actual cash flow distributed in that tier. Crucially, the cash flow available for the next tier (e.g., Tier 2) is calculated by subtracting the total repayment made in the prior tier (Tier 1) from the total cash flow to equity investors. At the end, check your work by calculating the IRR for each partner group using the `=IRR()` function on their respective cash flow streams and ensuring it aligns with the overall project IRR.

## Interview-ready answer

A real estate waterfall is a method of splitting profits between a sponsor and investors where the profit-sharing ratio changes as the project hits specific return hurdles. Typically, investors get a larger share of early returns up to a baseline IRR, but as the project's IRR clears higher thresholds, the sponsor earns a disproportionate share of the upside, known as the promote, to incentivize strong performance.

## Pitfalls and gotchas

- Setting IRR hurdles too low for risky projects: A 10% hurdle before shifting the split to 80/20 might be acceptable for a stabilized property, but for a risky new development, LP investors usually demand higher initial hurdles (e.g., 20%).
- Failing to account for financing events: In the first year, permanent loan refinancing, construction loan payoffs, and financing fees can drastically alter the effective amount of equity contributed, which must be accurately captured in the beginning balance of the waterfall.

## Sources

- [[BIWS - Real Estate Waterfall Model Returns and Case Study Answers (Video)]]
- [[A Simple Model - Real Estate Distribution Waterfall Example - A Simple Model]]
