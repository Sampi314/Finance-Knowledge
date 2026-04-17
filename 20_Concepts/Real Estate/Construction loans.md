---
type: concept
title: "Construction loans"
aliases: ["Construction Loan"]
tags: ["real-estate", "development", "debt"]
difficulty: intermediate
prerequisites: ["[[Real estate development pro forma]]", "[[Hard costs and soft costs]]"]
related: []
sources: ["[[Mergers and Inquisitions - REFM- Real Estate Financial Modeling Ultimate Guide w- Templates]]", "[[Pivotal180 - Glossary of Terms for Project Finance Training]]"]
status: stub
updated: 2026-04-17
---

# Construction loans

> **TL;DR.** A construction loan is a loan with periodic disbursements used to fund the construction of a project, which is typically converted into a permanent loan or paid back at the end of the construction period.

## When you'd use this

Construction loans are used primarily when an equity investor or developer wants to fund the construction of a real estate property from the ground up, minimizing their upfront cash requirements. They are critical in real estate development modeling because they require interest to be capitalized while the property is being built. Lenders only fund these loans after the developer contributes a sufficient amount of equity.

## The 30-second version

A construction loan provides capital during a project's building phase. Unlike standard loans where you get all the money upfront, construction loans are drawn down over time as building costs are incurred. The interest rates are typically higher than permanent loans. Because the project isn't generating income yet, interest and loan fees are "capitalized"—added to the loan balance rather than paid in cash. Once construction finishes and the property stabilizes, the construction loan is usually paid off or refinanced into a permanent loan.

## The full explanation

Construction loans are essential in real estate development modeling because the asset is being built from the ground up. Before lenders allow a developer to draw from the construction loan, they require the equity investors to contribute sufficient equity to cover initial land and construction costs. Once this equity limit is reached, funding switches to the construction loan.

Because the property generates no income during construction, interest on the loan is capitalized. This means interest isn't paid out of pocket but is added to the total debt balance, along with capitalized loan fees. To avoid circular references in modeling, interest calculations are based on the beginning balance of each month.

After the property stabilizes, the construction loan is often refinanced with a permanent loan, which uses the stabilized value and a loan-to-value (LTV) ratio to size the new debt tranche.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling construction loans, interest and fees are typically capitalized. To calculate the interest each month, base the calculation on the beginning debt balance to avoid creating circular references in Excel. Drawdowns occur incrementally as construction progresses, usually switching to the debt facility only after maximum equity has been deployed.

## Interview-ready answer

A construction loan is drawn down incrementally to fund development costs after equity has been injected. During construction, the loan accrues capitalized interest since the property is not yet stabilized or generating income. Upon completion and stabilization, the loan is typically replaced by a permanent loan at a lower interest rate.

## Pitfalls and gotchas

- **Circular references:** Calculating interest on the ending debt balance during construction will create a circular reference; use the beginning balance instead.
- **Capitalized interest and fees:** Forgetting to add accrued interest and loan fees to the final debt balance will understate the total financing cost.
- **Refinancing risk:** The property must reach sufficient stabilized value (and NOI) to qualify for a permanent loan that can fully repay the construction loan.

## Gaps

- Missing exact formula
- Missing worked example

## Sources

- [[Mergers and Inquisitions - REFM- Real Estate Financial Modeling Ultimate Guide w- Templates]]
- [[Pivotal180 - Glossary of Terms for Project Finance Training]]
