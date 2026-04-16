---
type: concept
title: "Construction phase financing"
aliases: []
tags: ["project-finance", "financing", "construction"]
difficulty: intermediate
prerequisites: ["[[Project finance overview]]", "[[SPV structure]]"]
related: []
sources: ["[[Finexmod - the importance of building flexible timeline in project finance models – Finexmod]]", "[[Finexmod - 8 points to Consider Before Building Your Sources and Uses Statement in your Project Finance Models – Finexmod]]", "[[Financial Modelling Handbook - The importance of the Sources and Uses statement in Project Finance]]"]
status: draft
updated: 2026-04-16
---

# Construction phase financing

> **TL;DR.** Construction phase financing is the stage in a project finance model detailing the funding of cash needs during construction, ending with the Commercial Operation Date (COD).

## When you'd use this

You would use construction phase financing concepts when setting up the master timeline in a project finance model. It is essential for determining how capital expenditures (CAPEX), development costs, and other uses of funds are covered by drawdowns of debt and equity over the construction period, leading up to operations.

## The 30-second version

A project finance transaction operates in stages. After the development phase reaches financial close, the construction phase begins. During this period, the project is not yet generating revenue, so all capital expenditures, working capital, and interest during construction must be meticulously funded. The financial model must track the exact schedule of cash outflows (Uses) and how they are paid for by incoming funds (Sources) like debt, equity, and grants. This tracking continues until the project is operational.

## The full explanation

Project finance is typically structured into distinct lifecycle stages: the development phase (ending at financial close), the construction phase, and the operations phase. The construction phase is the period post-financial close when the actual building program occurs, culminating in the Commercial Operation Date (COD).

During the construction phase, a project requires realistic forecasts of cash needs. These needs are summarized in the "Sources and Uses of Funds Statement."

### The Uses
The "Uses" section outlines all capital necessary to build the project. This typically encompasses:
- Capital expenditures (CAPEX)
- Development and construction costs
- Initial working capital requirements
- Interest during construction (IDC) and financing fees
- Pre-funding of necessary reserve accounts (like the Debt Service Reserve Account)

It is recommended to project these uses on a monthly basis to provide flexibility in modeling different drawdown schedules, accommodating contractors' payment milestones, and facilitating post-close actuals tracking.

### The Sources
The "Sources" section details where the money for construction comes from. This funding can include:
- Equity contributions from sponsors
- Senior debt (often drawn in multiple tranches)
- Subordinated or mezzanine debt
- Government grants or subsidies

The fundamental rule during the construction phase is that total Sources must equal total Uses in every model period to ensure there are no cash shortfalls while the project is not generating operating revenue.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling the construction phase, it is crucial to establish a flexible master timeline at the top of each worksheet. The model should include specific flags and counters indicating whether a given month falls within the construction period. Because interest during construction (a Use) depends on the size of the debt drawdown (a Source), circular references are common. It is a best practice to resolve these circularities using a VBA macro or a parallel model approach, rather than leaving the model iterative.

## Interview-ready answer

Construction phase financing refers to how a project company funds its capital needs before the asset begins generating revenue. The key mechanism is the Sources and Uses of Funds Statement, which aligns the schedule of construction costs, fees, and interest with drawdowns of equity and various tranches of debt, ensuring adequate liquidity until the commercial operation date.

## Pitfalls and gotchas

- Failing to resolve circular references in the construction funding loop, which makes the model unstable and slow.
- Modeling the construction phase quarterly or annually instead of monthly, losing the granularity needed for accurate drawdown monitoring.
- Forgetting to include adequate spare contingencies at an early stage, which can leave the project underfunded if costs overrun.

## Sources

- [[Finexmod - the importance of building flexible timeline in project finance models – Finexmod]]
- [[Finexmod - 8 points to Consider Before Building Your Sources and Uses Statement in your Project Finance Models – Finexmod]]
- [[Financial Modelling Handbook - The importance of the Sources and Uses statement in Project Finance]]