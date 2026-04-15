---
type: concept
title: Mezzanine debt
aliases: ["Mezzanine financing", "Mezz debt"]
tags: ["lbo", "debt", "capital-structure", "financing"]
difficulty: intermediate
prerequisites: ["[[Senior debt]]", "[[LBO overview]]"]
related: []
sources: ["[[Financial Modeling NYC - Unitranche vs Senior-Mezz- Financing Structures Compared]]"]
status: draft
updated: 2026-04-15
---

# Mezzanine debt

> **TL;DR.** Mezzanine debt is a layer of financing that sits between senior debt and equity in the capital stack, carrying higher risk and higher pricing but offering looser covenants and often including Payment-in-Kind (PIK) or equity upside features.

## When you'd use this

Mezzanine debt is typically used in leveraged buyouts (LBOs) and acquisitions when the buyer needs more leverage than senior lenders are willing to provide. It is particularly useful for companies with stable, predictable cash flows where sponsors want to maximize their equity returns or when traditional senior loans don't fully cover the required purchase price.

## The 30-second version

In a traditional leveraged structure, risk and pricing are separated into distinct tranches. Mezzanine debt represents a subordinated layer below senior debt but above equity. Because it is riskier than senior debt (as it gets paid out later in a downside scenario), it commands higher interest rates. It also generally features looser covenant restrictions compared to senior debt and frequently includes structural enhancements like Payment-In-Kind (PIK) interest or equity warrants to compensate for the added risk.

## The full explanation

Mezzanine debt is a crucial component of traditional acquisition financing stacks, particularly in classic leveraged buyouts.

### Risk and Reward Profile
In a traditional Senior/Mezzanine stack, risk is explicitly separated:
- **Higher Risk:** Subordinated to senior debt, meaning mezzanine lenders are paid after senior lenders in the event of default or bankruptcy.
- **Higher Pricing:** To compensate for the increased risk, mezzanine debt carries higher interest rates than senior facilities.

### Structural Characteristics
Mezzanine debt offers specific structural trade-offs compared to senior debt or unitranche facilities:
- **Looser Covenants:** Mezzanine facilities often have fewer or more flexible financial covenants, providing the borrower with more operational breathing room than strict senior loan covenants.
- **PIK Components:** They often include a Payment-In-Kind (PIK) feature, where interest accretes and is added to the principal balance rather than being paid out in cash periodically. This helps companies manage their near-term cash flow volatility.
- **Equity Kickers:** Mezzanine lenders sometimes require warrants or equity conversion features to boost their overall return.

### Modeling Implications
In financial models, mezzanine debt requires modeling layered interest, potential step-ups, and PIK accretion. The behavior of a Senior/Mezzanine stack under stress is materially different from a unitranche facility, as downside cases can break faster under stacked structures due to intercreditor agreements and payment waterfalls.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling a traditional Senior/Mezzanine stack, the financing structure must be explicitly mapped out. This means modeling the layered interest structure, PIK (Payment-in-Kind) accretion, and intercreditor payment waterfalls. A model that treats a Senior/Mezzanine stack identically to a single-tranche (unitranche) facility is structurally wrong and will not properly reflect downside risks or refinancing assumptions.

## Interview-ready answer

Mezzanine debt is a subordinated layer of financing used in LBOs that sits between senior debt and equity. It carries higher risk and thus a higher interest rate than senior debt, but offers looser covenants and often includes Payment-in-Kind (PIK) interest or equity warrants. It's used to maximize leverage and equity returns, though it requires modeling complex intercreditor payment waterfalls and PIK accretion.

## Pitfalls and gotchas

- Assuming all debt behaves the same in a downside scenario; mezzanine debt is subordinated to senior debt and is riskier in restructuring or bankruptcy.
- Failing to explicitly model the PIK (Payment-in-Kind) accretion, which alters the cash flow profile and outstanding debt balance over time.
- Overlooking the structural complexity and higher execution friction caused by intercreditor negotiations between senior and mezzanine lenders.

## Sources

- [[Financial Modeling NYC - Unitranche vs Senior-Mezz- Financing Structures Compared]]
