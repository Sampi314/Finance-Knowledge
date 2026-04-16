---
type: concept
title: "Concession agreements"
aliases: ["concession contract", "concession agreement"]
tags: ["project-finance", "infrastructure", "ppp"]
difficulty: intermediate
prerequisites: ["[[Project finance overview]]", "[[Availability payments]]"]
related: ["Public-private partnerships", "[[Take-or-pay contracts]]"]
sources: ["[[Financial Modeling NYC - Infrastructure Asset Valuation- DCF Modeling for Regulated Utilities and PPP Projects]]", "[[Pivotal180 - An introduction to Project Agreements]]"]
status: stub
updated: 2026-04-16
---

# Concession agreements

> **TL;DR.** A concession agreement is a long-term contract between a government entity and a private operator, granting the operator the right to finance, build, and operate a public infrastructure asset for a finite period.

## When you'd use this

You would encounter concession agreements primarily in Public-Private Partnerships (PPP) such as toll roads, airports, and public facilities. It defines the framework for how a private company can develop and generate revenue from public infrastructure, allocating risks between the public and private sectors before the asset ultimately reverts to the government.

## The 30-second version

A concession agreement dictates how an infrastructure asset will be built, maintained, and operated. Because the underlying asset is public, the contract guarantees that the private developer receives a way to recover its fixed and variable costs (e.g., through availability payments or user tolls). The agreement has a finite term (like 30 or 50 years). At the end of the term, ownership and operation of the asset usually revert to the government at zero value.

## The full explanation

For infrastructure projects, concession agreements (often structured as Build-Operate-Transfer or BOT models) serve as the primary approach to establishing the project's revenue model. The government needs an asset (like a hospital or toll road) but doesn't want the full upfront financial burden, so it grants a private developer a concession.

### Finite Life and Reversion

Unlike corporate assets, concession assets have a finite life determined by the contract term. Cash flows only exist during this period. Once the contract ends, the asset usually reverts to the public authority, meaning there is no traditional terminal value in financial models.

### Risk Allocation and Revenue Streams

Concession agreements typically establish two primary revenue components:
- **Availability payments:** Designed to cover fixed costs (like maintenance, debt service, and equity return), these are paid by the contracting authority as long as the infrastructure meets strict "available" standards (e.g., a hospital's rooms are fully functional).
- **Usage payments or user tolls:** For user-pays assets like toll roads, revenue depends on volume (demand risk). Sometimes governments subsidize this through "shadow tolls," where the government pays a fee per user to keep public costs down.

### Performance Specifications

Revenue under a concession agreement is tied to smart output specifications (Specific, Measurable, Achievable, Realistic, and Timely). If the project company fails to meet these standards (e.g., hospital rooms become unavailable due to poor maintenance), they face explicit financial penalties that reduce their service fee. Conversely, exceeding standards may yield bonuses.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When modeling a concession agreement, do not calculate a perpetual terminal value; cash flows must end exactly when the concession ends. Additionally, ensure strict consistency with inflation: infrastructure revenues are often linked to inflation (like CPI). If cash flows are projected in nominal terms, discount them using a nominal WACC; if real, use a real WACC.

## Interview-ready answer

A concession agreement is a long-term contract in a PPP where a government allows a private entity to build and operate public infrastructure. The contract strictly defines the project's finite life, allocates demand and availability risks, and establishes the revenue mechanism—such as availability payments or tolls—before the asset reverts to the government.

## Pitfalls and gotchas

- Applying a perpetual terminal value in a DCF model, rather than projecting cash flows only to the end of the finite concession life.
- Mixing nominal cash flows with real discount rates, which significantly overstates the asset's present value.
- Failing to rigorously define what "available" means in the output specifications, leading to disputes over penalty reductions to the service fee.

## Gaps

- Missing specific formulas for calculating payments.
- Missing specific worked examples with numbers.

## Sources

- [[Financial Modeling NYC - Infrastructure Asset Valuation- DCF Modeling for Regulated Utilities and PPP Projects]]
- [[Pivotal180 - An introduction to Project Agreements]]
