---
type: concept
title: "Power purchase agreements"
aliases: ["PPA", "Corporate PPA", "Virtual PPA", "VPPA"]
tags: ["project-finance", "renewables", "contracts"]
difficulty: intermediate
prerequisites: []
related: []
sources: ["[[Pivotal180 - Understanding the Corporate PPA Landscape]]", "[[Pivotal180 - Corporate PPAs Explained- Structure, Benefits, and Key Risks]]"]
status: draft
updated: 2026-04-16
---

# Power purchase agreements

> **TL;DR.** A long-term contract between a renewable energy seller and a buyer to purchase electricity or its economic value at a set price, providing a guaranteed revenue stream to secure project financing.

## When you'd use this

You would use this concept when structuring, financing, or modeling a renewable energy project. It is essential for determining the long-term cash flows and revenue stability of the project, which lenders require before committing debt. It also applies when analyzing how corporations procure clean energy to meet sustainability targets and hedge against retail electricity price volatility.

## The 30-second version

A Power Purchase Agreement (PPA) is a long-term contract where a buyer agrees to purchase energy from a renewable energy project at a fixed price, typically for 10 to 20 years. Traditionally, the buyer was a utility. Today, "Corporate PPAs" are common, where the buyer is a business aiming for budget certainty and ESG goals. These agreements guarantee a revenue stream, which is crucial for the project developer to secure financing. A key variation is the Virtual PPA (VPPA), which functions as a financial hedge without the physical delivery of electricity.

## The full explanation

A Power Purchase Agreement (PPA) is the cornerstone contract for financing many energy projects. It establishes a fixed price for electricity over a long period (usually 10-30 years). This contractually fixed price provides stable, long-term cash flows, which are heavily analyzed by lenders when deciding to finance the project.

### Traditional vs. Corporate PPAs
Traditionally, PPAs are signed between a Project Company (or Independent Power Producer) and a utility. The utility buys the power and distributes it to its customers. A Corporate PPA, however, involves a corporate offtaker—a business that consumes electricity but is not in the business of energy generation or distribution. Corporates sign these to improve ESG ratings, secure Renewable Energy Certificates (RECs), and hedge against volatile retail power prices.

### Physical vs. Virtual Structures
**Physical PPAs** involve the actual delivery of power. The project and the corporate offtaker are usually on the same grid network, and the generated power replaces what the buyer would have purchased from their local utility.

**Virtual PPAs (VPPAs)** are financial instruments and do not involve physical power delivery. They function as a Contract for Difference (CfD). The project sells power into the open market at floating prices, while the corporate buyer continues to buy power from their local utility. They then financially settle the difference between the open market price and their agreed-upon VPPA "Strike Price."

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling Corporate PPAs, analysts must not confuse the "generation profile" with the "market pricing profile." A common error is assuming the project earns the average 24-hour price, whereas it actually earns the price captured during its specific generation hours (which can be lower in heavily supplied grids).

## Interview-ready answer

A Power Purchase Agreement is a long-term contract to buy electricity at a fixed price, which secures the stable cash flows needed to finance a renewable energy project. Today, Virtual PPAs are popular with corporations; these act as a financial hedge (Contract for Difference) against market prices without requiring the physical delivery of power to the corporate facility.

## Pitfalls and gotchas

- **Basis Risk in VPPAs:** In a VPPA, the settlement is based on the floating market price at the project's grid node. If prices crash at the generator's node but remain high at the corporate's load center, the financial hedge breaks, forcing the corporate to pay the developer a settlement while still paying high local utility rates.
- **Shape Risk and Cannibalization:** Renewable projects generate power intermittently (e.g., solar at noon). If many projects generate simultaneously, excess supply drives down the market value of the power, potentially destroying the project's economics if the PPA settles against a weighted average price.
- **Credit Risk:** The creditworthiness of the corporate offtaker is a major factor in bankability; lenders require financially robust offtakers to guarantee the long-term cash flow.

## Sources

- [[Pivotal180 - Understanding the Corporate PPA Landscape]]
- [[Pivotal180 - Corporate PPAs Explained- Structure, Benefits, and Key Risks]]
