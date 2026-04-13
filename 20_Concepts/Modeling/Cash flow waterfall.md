---
type: concept
title: "Cash flow waterfall"
aliases: ["cash cascade", "payment waterfall"]
tags: ["modeling", "project-finance", "debt"]
difficulty: intermediate
prerequisites: []
related: []
sources: ["[[Pivotal180 - Project Finance Cash Flow Waterfall - Priority, Structure & Modeling]]", "[[Finexmod - Building a cash flow waterfall in a project finance model – Finexmod]]", "[[Financial Modelling Handbook - What is a cash flow waterfall in Project Finance?]]"]
status: draft
updated: 2026-04-13
---

# Cash flow waterfall

> **TL;DR.** A structured method in project finance of distributing a project's cash flows among various stakeholders according to a predetermined priority order.

## When you'd use this

The cash flow waterfall is used in non-recourse project finance to protect lenders, prioritize cash allocation, and restrict equity distributions. It is primarily needed during the operations phase when the project begins generating cash, as opposed to the construction phase where the sources and uses of funds statement is more active.

## The 30-second version

A cash flow waterfall sets out the order of priorities for using cash inflows earned by a special purpose vehicle (SPV). When things go according to plan, there is sufficient cash to pay operations, taxes, debt service, reserves, and finally the shareholders. In downside scenarios where cash is limited, the waterfall dictates who gets paid first—ensuring senior debt and essential operations take precedence over subordinated debt and equity.

## The full explanation

In project finance, because the loan is cash-flow based rather than collateral-based, lenders want strict control over how cash is distributed. The waterfall structure is contractually mandated in the loan agreement or a separate "Accounts Agreement." An administrative agent typically manages the cash accounts on behalf of lenders.

While the specific order can vary based on project and regional norms, a standard ranking includes:
1. **Project operating costs and taxes**: Essential to keep the project running. Note that in some countries (like the US, Canada, Netherlands), the SPV is not a taxable entity, so taxes are not included here.
2. **Fees and expenses**: For lawyers, consultants, or the administrative agent.
3. **Senior debt service**: Interest payable and scheduled principal amortization to senior lenders.
4. **Reserve accounts**: Such as replenishing a Debt Service Reserve Account (DSRA) or Maintenance Reserve Account. The exact order of these reserves can be highly negotiated.
5. **Subordinated debt service**: Payments for mezzanine or junior debt.
6. **Cash sweep**: Mandatory prepayment of debt using excess cash flow.
7. **Equity distributions**: Only allowed if the project passes restricted payment tests and covenant checks.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling the cash flow waterfall, it is built from the perspective of the borrower (the SPV), with inflows as positive values and outflows as negative. A dedicated sheet or section usually computes the Cash Available for Debt Service (CADS or CFADS). Building the waterfall can be complex due to circular references (such as calculating taxes, interest during construction, or cash sweeps). It is crucial to set up the model flexibly, avoiding hard-coded rules so different negotiation outcomes or scenarios can be accommodated.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Subordinated reserves: Some maintenance or debt reserves might be funded after senior debt is paid to maximize CADS. This increases debt capacity but raises downside risk.
- Circular references: Accurately calculating cash sweeps and related taxes often introduces circular logic that must be managed with macro-based copy/paste loops.
- SPV Taxes: You must confirm the tax structure of the SPV in the project's jurisdiction before including federal or income taxes at the top of the waterfall.

## Sources

- [[Pivotal180 - Project Finance Cash Flow Waterfall - Priority, Structure & Modeling]]
- [[Finexmod - Building a cash flow waterfall in a project finance model – Finexmod]]
- [[Financial Modelling Handbook - What is a cash flow waterfall in Project Finance?]]
