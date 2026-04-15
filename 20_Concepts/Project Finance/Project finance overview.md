---
type: concept
title: "Project finance overview"
aliases: ["Project finance theory"]
tags: ["project-finance", "overview", "debt-structuring", "risk-analysis"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[Project Finance - Project Finance Theory and Marriage Contracts]]"]
status: draft
updated: 2026-04-15
---

# Project finance overview

> **TL;DR.** Project finance is a method of funding infrastructure and energy projects relying heavily on the project's cash flows for repayment, evaluated through rigorous risk analysis and debt structuring.

## When you'd use this

You would use project finance concepts when structuring, funding, or modeling large-scale infrastructure, energy, or real estate projects. It is essential when analyzing risks, sizing debt, setting up debt service reserve accounts, or dealing with non-recourse or limited-recourse financing where the project's future cash flows dictate its viability.

## The 30-second version

Project finance differs from corporate finance by focusing strictly on the specific project's cash flows rather than a sponsor's balance sheet. It involves detailed risk analysis—assessing volume risk, availability risk, and contract structures. Debt structuring is critical and comprises five main parts: debt sizing, funding, repayment schedules (like sculpting), interest rates, and credit protections (like DSCR covenants and sweeps). Re-financing also plays a major role as a value-adding option once construction risks diminish.

## The full explanation

Project finance theory integrates risk analysis with rigorous debt structuring.

### Risk Analysis
Risk analysis in project finance involves evaluating how risks change over a project's life. Projects often face different types of risks such as volume risk (e.g., toll roads where traffic fluctuates) or availability risk (e.g., thermal plants where availability is contracted). Understanding these through case studies helps identify dangers like poorly structured power contracts or situations where high contract prices become unsustainable.

### Debt Structuring
Debt structuring is a core component and is typically broken down into five areas:
1. **Debt Size:** Determining how much debt a project can handle, often sized using debt-to-capital constraints or Debt Service Coverage Ratio (DSCR) targets. The debt at Commercial Operations Date (COD) equals the present value of the debt service.
2. **Debt Funding:** Managing how debt is drawn during construction, including equity-first or pro-rata funding, and handling equity bridge loans (EBL).
3. **Debt Repayment:** Structuring how the debt is paid back, which often involves "sculpting" repayment schedules to match cash flows, or using balloon payments.
4. **Interest Rates and Fees:** Factoring in the cost of debt and credit spreads.
5. **Credit Protections:** Implementing mechanisms like Debt Service Reserve Accounts (DSRA), cash lock-up DSCR covenants, and cash sweeps to provide liquidity and protect lenders.

### Re-financing
Re-financing is treated as an option whose value stems from uncertainty. As a project transitions from construction to operations and risk profiles drop, re-financing can significantly improve equity returns. Credit spreads earned and compounded over long periods imply a probability of default that must be managed.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

Project finance models are notoriously prone to circular references due to factors like interest during construction, debt sizing based on DSCR, or DSRA sizing. A recommended best practice to resolve these is using a "Parallel Model" with User-Defined Functions (UDFs). This parallel model acts independently to calculate CFADS, total funding, and DSRA flows. Connecting these outputs to your main model eliminates circular references and increases model flexibility (e.g., testing fixed debt vs. DSCR-sized debt, or sculpting changes) without relying on slow copy-and-paste macros.

## Interview-ready answer

Project finance focuses on funding specific projects where repayment relies entirely on the project's generated cash flows rather than the sponsor's balance sheet. It requires rigorous risk analysis, handling specific risks like volume or availability, and complex debt structuring involving sizing, funding, repayment sculpting, and credit protections like DSRAs.

## Pitfalls and gotchas

- Relying on copy-and-paste macros to resolve circular references can make models slow and inflexible; a parallel model is preferable.
- Assuming risks remain constant; risk changes significantly from the construction phase to the operations phase.
- Misunderstanding that debt size at COD is essentially the present value of the future debt service.

## Sources

- [[Project Finance - Project Finance Theory and Marriage Contracts]]
