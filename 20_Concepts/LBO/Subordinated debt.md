---
type: concept
title: "Subordinated debt"
aliases: ["sub debt", "mezzanine debt", "subordinated financing"]
tags: ["lbo", "debt", "capital-structure", "financing"]
difficulty: intermediate
prerequisites: ["[[Senior debt]]"]
related: ["[[Mezzanine debt]]"]
sources: ["[[Sapphire 45 - Understanding Subordinated Debt- Key Features and Risks]]", "[[IB Interview Questions - Mezzanine Debt and Preferred Equity Explained]]"]
status: draft
updated: 2026-04-15
---

# Subordinated debt

> **TL;DR.** Subordinated debt is unsecured financing that ranks below senior debt but above equity in the capital structure, offering higher yields to compensate for its junior repayment priority in the event of bankruptcy.

## When you'd use this

Subordinated debt is used when a company needs growth capital or wants to maximize leverage beyond what senior lenders will provide, but founders or sponsors want to avoid the dilution of issuing new equity. It is commonly utilized in leveraged buyouts (LBOs), management buyouts, dividend recapitalizations, and funding expansions for high-performing SMEs.

## The 30-second version

Subordinated debt sits in the middle of the capital stack, below secured senior loans and above equity. Because it is typically unsecured and repaid only after senior creditors in a liquidation, lenders demand a higher risk premium. This compensation often comes as a combination of cash interest, Payment-in-Kind (PIK) interest, and sometimes equity kickers like warrants. While expensive compared to senior debt, it is cheaper than equity and provides businesses with flexible, non-dilutive capital.

## The full explanation

Subordinated debt, also often referred to as mezzanine debt in LBO contexts, bridges the gap between debt capacity and equity contribution.

**Capital Stack Placement and Risk**
In the event of bankruptcy or liquidation, senior creditors are paid first. Subordinated debt holders receive whatever remains, exposing them to a higher risk of partial or total loss. Because it lacks collateral backing, lenders rely heavily on the borrower's cash flow stability and creditworthiness.

**Yield Premium and Structure**
To offset the increased risk, subordinated debt commands higher total yields (often 12-20%). The return profile is generally structured with three components:
1. **Cash interest**: Typically higher than senior debt rates (e.g., 8-12%).
2. **PIK (Payment-in-Kind) interest**: Instead of paying cash, the interest accrues and is added to the principal balance, preserving the company's near-term cash flow.
3. **Equity kickers**: Warrants or conversion rights that give the lender a small percentage of equity upside.

**Strategic Value**
For private equity sponsors, substituting equity with subordinated debt reduces the initial equity check, thereby increasing the potential return on invested capital (IRR). Additionally, subordinated debt often has fewer restrictive covenants compared to senior debt, providing the borrower with more operational flexibility.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling subordinated debt, particularly PIK interest, ensure that the PIK amount is added to the ending debt balance rather than treated as a cash outflow on the cash flow statement. At exit, the payoff amount is the accumulated balance (original principal plus all compounded PIK). If the debt includes warrants, model the dilution by allocating the warrant holders' percentage of the total equity value at exit before calculating sponsor returns.

## Interview-ready answer

Subordinated debt is an unsecured layer of financing that sits between senior debt and equity. It carries a higher yield, often structured with PIK interest and equity kickers, to compensate for its lower repayment priority. Sponsors use it in LBOs to maximize leverage and boost equity returns when senior debt capacity is maxed out.

## Pitfalls and gotchas

- **PIK Compounding:** PIK interest compounds over the life of the loan, leading to a significantly larger principal balance at maturity or exit.
- **Liquidity Risk in Distress:** Because it is unsecured and subordinated, these instruments are highly vulnerable to total loss if the company's enterprise value falls below the senior debt amount during a liquidation.
- **Interest Rate Sensitivity:** Fixed-rate subordinated debt becomes less attractive to investors in a rising interest rate environment.

## Sources

- [[Sapphire 45 - Understanding Subordinated Debt- Key Features and Risks]]
- [[IB Interview Questions - Mezzanine Debt and Preferred Equity Explained]]
