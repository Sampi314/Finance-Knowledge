---
type: concept
title: "Capex schedule"
aliases: []
tags: [modeling, capex, schedule, excel]
difficulty: intermediate
prerequisites: ["[[Three-statement model]]", "[[Cost build]]"]
related: []
sources: ["[[Financial Modeling NYC - How to Build a Financial Model from Scratch in Excel]]", "[[Financial Modeling NYC - Speed Modeling- Techniques to Build Financial Models faster]]", "[[Pivotal180 - Australian Grid-Scale BESS Project]]", "[[ChallengeJP - Telecom Financial Forecast Model (Excel Tutorial + Template)]]", "[[CFI - Pitchbook - Liquidity Analysis Section of the Template]]"]
status: draft
updated: 2026-04-12
---

# Capex schedule

> **TL;DR.** The CapEx (Capital Expenditures) schedule tracks the additions, disposals, and depreciation of fixed assets, forming a critical part of the three-statement model.

## When you'd use this

You use a CapEx schedule when building a financial model from scratch, updating an operating model, or preparing a transaction pitchbook. It helps accurately forecast future capital investments and their subsequent depreciation, which directly impacts the income statement, balance sheet (Property, Plant & Equipment or PP&E), and cash flow statement.

## The 30-second version

A CapEx schedule details a company's past and future capital expenditures, breaking down investments in fixed assets over time. It typically differentiates between maintenance CapEx (required to keep operations running smoothly) and growth CapEx (investments to expand the business). Additionally, the schedule calculates the associated depreciation expense over the assets' useful lives, seamlessly integrating with the core financial statements.

## The full explanation

Building an effective CapEx schedule is a standard step in the financial modeling process, often grouped under operating or supporting schedules alongside revenue builds, cost structures, and working capital logic.

A well-structured schedule involves:
1. **Separating CapEx Types:** Differentiating between **maintenance CapEx** (replacing depreciated assets to maintain current operations) and **growth CapEx** (investing in new projects, capacity expansion, or M&A to generate additional revenue). Distinguishing between them helps clarify if growth comes from existing assets or new capital investments.
2. **Forecasting Future CapEx:** Based on historical trends, percentage of revenue, or specific management plans (e.g., a battery degradation and augmentation schedule for grid-scale energy projects).
3. **Depreciation Roll-forward:** Calculating the depreciation expense, typically using the straight-line method. The ending PP&E balance rolls forward period over period: `Ending PP&E = Opening PP&E + New CapEx – Disposals - Depreciation`.

In the context of M&A or investments, the CapEx schedule is an essential part of liquidity analysis. It serves as an opportunity cost assessment, helping determine if free cash flow should be used for internal capital investments or allocated toward external transactions and debt repayments.

## Formula

The core logic for depreciation within the CapEx schedule is:
`Depreciation = (Opening PP&E + New CapEx – Disposals) / Useful Life`

## Worked example

(none)

## Excel and modeling notes

- **Templates and Modularity:** For modeling speed, top analysts recommend creating a reusable, robust CapEx module that you build once and reuse across different models, adjusting only assumptions and drivers.
- **Dependency:** Keep all input assumptions (like useful life, maintenance vs. growth split, etc.) separated on a dedicated Assumptions tab to ensure a clean dependency chain.
- **D&A Exclusion from COGS:** Exclude depreciation from the COGS schedule unless specifically modeling it there; standard modeling practice puts depreciation explicitly in the CapEx schedule to feed into D&A cleanly.

## Interview-ready answer

The CapEx schedule is a critical supporting schedule in a three-statement model that tracks the roll-forward of Property, Plant, and Equipment. It breaks down investments into maintenance and growth CapEx and models the depreciation expense over the assets' useful lives, which then feeds into the income statement, lowers the carrying value on the balance sheet, and is added back in the cash flow statement.

## Pitfalls and gotchas

- Failing to distinguish between growth and maintenance CapEx, which obscures the true cost of expanding the business versus just sustaining it.
- Inconsistent time axes or mismatched period structures when linking the CapEx schedule to the main financial statements.
- Not verifying if a target company’s existing CapEx commitments limit the free cash available for transaction funding.

## Sources

- [[Financial Modeling NYC - How to Build a Financial Model from Scratch in Excel]]
- [[Financial Modeling NYC - Speed Modeling- Techniques to Build Financial Models faster]]
- [[Pivotal180 - Australian Grid-Scale BESS Project]]
- [[ChallengeJP - Telecom Financial Forecast Model (Excel Tutorial + Template)]]
- [[CFI - Pitchbook - Liquidity Analysis Section of the Template]]
