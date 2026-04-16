---
type: concept
title: "Availability payments"
aliases: []
tags: ["project-finance", "revenue-model", "infrastructure"]
difficulty: beginner
prerequisites: ["[[Project finance overview]]", "[[SPV structure]]"]
related: ["[[Take-or-pay contracts]]", "[[Power purchase agreements]]"]
sources: ["[[Pivotal180 - An introduction to Project Agreements]]"]
status: draft
updated: 2026-04-16
---

# Availability payments

> **TL;DR.** An availability payment is a service fee paid by a government entity to a project company to cover fixed operating costs and debt service, contingent on the infrastructure facility being available for use according to predefined specifications.

## When you'd use this

Availability payments are primarily used in public infrastructure projects (like hospitals, schools, or roads) developed under a public-private partnership (PPP). The government prefers paying for use over time instead of covering large upfront construction costs, while private investors need a stable, predictable revenue stream isolated from demand or usage risk to ensure their financial returns.

## The 30-second version

In a project agreement for public infrastructure, the revenue model often relies on availability payments rather than end-user tolls. The contracting authority (usually a government entity) pays the project company a set fee purely for making the facility available and maintaining it to a specified standard. This fee is designed to cover the project's fixed costs, debt service, and equity returns. Because governments typically have strong credit ratings, the risk of default is low, making it a safe investment profile that can support lower required rates of return.

## The full explanation

When private investors build public infrastructure, they face two types of costs: fixed and variable. The private sector typically avoids the demand risk associated with how frequently the public will actually use the facility. To solve this, the service fee system is disaggregated.

The availability payment component is designed specifically to recover fixed costs—such as labor, basic maintenance, debt service, and the required return on equity—which are incurred regardless of usage. As long as the facility is available to the standard specified in the project agreement, the project company receives this payment. Variable costs linked to actual usage volumes (like utilities or wear-and-tear) are often covered by a separate usage payment that passes through to the contracting authority.

To earn the full availability payment without penalties, the project company must meet smart (specific, measurable, achievable, realistic, and timely) output specifications that define both availability and service quality. Failures to meet these standards result in deductions proportional to the shortfall.

## Formula

(none)

## Worked example

[[Hospital availability penalty calculation]]

## Excel and modeling notes

When modeling availability payments, fixed costs and debt service should be established first. The availability payment amount is then sized as an optimization exercise to deliver the required target return to the equity investors. Modeling should handle penalties or bonuses clearly, tracking any shortfalls against the maximum potential available time (e.g., room-days) and applying the associated revenue deductions.

## Interview-ready answer

Availability payments are stable service fees paid by a government contracting authority to a project company in a public-private partnership, compensating them for building and maintaining an infrastructure asset regardless of how much the public uses it. This structure isolates the project from demand risk, ensuring fixed costs and debt service can be met as long as the facility meets performance specifications.

## Pitfalls and gotchas

- Failing to precisely define "availability" in the project agreement, leading to disputes over whether an asset (e.g., a room without functional air conditioning) qualifies as available.
- Facing severe revenue penalties if poor maintenance causes key parts of the infrastructure to be out of commission, though these penalties are generally capped at the total service fee amount.
- Confusing availability payments with shadow tolls, which are also paid by the government but are based on actual usage volumes rather than pure availability.

## Sources

- [[Pivotal180 - An introduction to Project Agreements]]
