---
type: concept
title: "Refinancing risk"
aliases: []
tags: [project-finance, risk-management, debt-structuring]
difficulty: intermediate
prerequisites: ["[[Project finance overview]]", "[[Debt sculpting]]"]
related: []
sources: ["[[Full Stack Modeller - Mini-Perm Financing Dilemma]]", "[[Pivotal180 - Bullet, Balloon, & Mini-Perm Repayments]]"]
status: stub
updated: 2026-04-16
---

# Refinancing risk

> **TL;DR.** Refinancing risk is the danger that a borrower cannot replace an existing loan with a new one at maturity, or that the new loan will have significantly worse terms (like higher interest rates).

## When you'd use this

You analyze refinancing risk whenever dealing with debt structures that do not fully amortize over their life, such as bullet, balloon, or mini-perm loans. It is crucial for assessing downside scenarios and determining how much equity return is exposed if future debt markets tighten.

## The 30-second version

In project finance, loans are usually structured to match the life of a project. However, banks sometimes cannot offer long-term loans (e.g., 18-20 years). Instead, they provide a shorter loan (e.g., a 6-year mini-perm) expecting the project to refinance when it matures. If market conditions deteriorate or the project performs poorly, finding new lenders or favorable interest rates becomes difficult, potentially leaving the project unable to repay the original loan.

## The full explanation

### Debt Term vs. Project Life
Many infrastructure and renewable energy projects have operational lives of 20 to 30 years and require long-term debt to match their contracted cash flows. However, lenders are often unwilling to take a 20-year view on a project due to market uncertainty and capital constraints.

### Mini-Perm Structures
To bridge this gap, borrowers often use a mini-perm financing structure. A mini-perm is a short-term loan (e.g., 5-7 years) sized as if it were a long-term loan (e.g., using a 15-20 year amortization profile). Because the debt isn't fully paid off by maturity, a large remaining principal balance must be refinanced with a new loan.

### The Risks for Equity and Lenders
When the initial loan matures, the project must go back to the market to secure new financing. If interest rates have risen sharply, the new debt will cost more, lowering equity returns. More severely, if credit markets are frozen or the project is underperforming, the project might not be able to refinance at all. In that scenario, lenders often have the right to capture 100% of the project's cash flows (a cash sweep) until the debt is paid down to a level that can be refinanced, or they may even foreclose on the asset.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling mini-perm structures, it is essential to build scenarios for the refinancing event. This includes testing what happens to the project's IRR if the refinancing interest rate is 2-3% higher than the current rate, or if the refinancing is delayed entirely and all cash flows are swept to pay down the initial debt.

## Interview-ready answer

Refinancing risk occurs when a borrower uses short-term debt, like a mini-perm facility, for a long-term project and faces the possibility of being unable to secure new financing at maturity. If market conditions worsen or interest rates rise, the new loan may have poor terms or not be available at all, often triggering cash sweeps that wipe out equity distributions.

## Pitfalls and gotchas

- Assuming that current favorable interest rates will still be available in 5 or 10 years when a mini-perm loan matures.
- Failing to model downside scenarios where refinancing fails and lenders take 100% of the project cash flows.
- Viewing mini-perms simply as "kicking the can down the road" without understanding the very real risk of default if credit markets tighten.

## Gaps

- Missing exact formula
- Missing worked example

## Sources

- [[Full Stack Modeller - Mini-Perm Financing Dilemma]]
- [[Pivotal180 - Bullet, Balloon, & Mini-Perm Repayments]]
