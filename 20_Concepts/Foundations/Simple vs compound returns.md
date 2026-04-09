---
type: concept
title: "Simple vs compound returns"
aliases: ["Simple vs compound interest"]
tags: ["foundations", "returns", "interest"]
difficulty: beginner
prerequisites: ["[[Compound interest]]"]
related: []
sources: ["[[CFI - Interest Rate Calculator]]", "[[CFI - Compound Interest]]", "[[CFI - Continuously Compounded Return]]"]
status: draft
updated: 2026-04-09
---

# Simple vs compound returns

> **TL;DR.** Simple returns are calculated only on the initial principal, whereas compound returns are calculated on both the principal and the accumulated interest from previous periods.

## When you'd use this

Understanding the difference between simple and compound returns is essential when evaluating investment performance or the cost of a loan. It helps you choose between different savings accounts or investment opportunities and ensures you use the correct financial formulas for modeling returns over multiple periods.

## The 30-second version

Simple interest is calculated only on the principal amount, which means the interest earned remains constant for each period. Compound interest, on the other hand, is "interest on interest." It is calculated on both the original principal and the accumulated interest from prior periods. Because the base on which interest is calculated grows over time, compound returns can lead to significantly larger totals over long time horizons compared to simple returns.

## The full explanation

When calculating the return on an investment or the interest on a loan, there are two primary methods: simple returns and compound returns.

### Simple Returns
Simple interest is calculated strictly as a percentage of the original principal amount. The amount of interest earned or paid is fixed in each period because the base amount does not change. For example, if you invest $10,000 at a simple interest rate of 5% per year, you will earn $500 in the first year, $500 in the second year, and so on. The total interest is simply the principal multiplied by the interest rate and the number of periods.

### Compound Returns
Compound interest means that the return on an investment is calculated not only on the initial principal but also on the interest previously accumulated. This leads to exponential growth of the account value. In each successive period, the interest payment increases because it is based on a continuously growing principal. Over a long time horizon, compound interest allows investors to earn potentially very high returns, a phenomenon often referred to as the "power of compounding."

Continuous compounding is an extreme case where interest is calculated over an infinite number of periods, using an exponential constant ($e$), rather than over specific intervals like monthly or annually.

## Formula

The simple return total can be defined as:
`Total = Principal × (1 + (Interest Rate × Number of Years))`

The annual compounding return formula is:
`Total = Principal × (1 + Interest Rate)^(Number of Years)`

For continuously compounded returns:
`Total = Principal × e^(Interest Rate × Number of Years)`

## Worked example

Assume an initial investment of $10,000 at an interest rate of 5% for 2 years.

**Simple Interest:**
Total = $10,000 × (1 + (0.05 × 2)) = $10,000 × 1.10 = $11,000.
The total interest earned is $1,000.

**Compound Interest (Annual):**
Total = $10,000 × (1 + 0.05)^2 = $10,000 × 1.1025 = $11,025.
The total interest earned is $1,025.

The compound return provides a slightly higher total even after just two years because the second year's interest is calculated on $10,500 rather than $10,000. Over longer horizons, this difference becomes dramatic.

## Excel and modeling notes

(none)

## Interview-ready answer

Simple returns only calculate interest on the original principal, leading to linear growth. Compound returns calculate interest on the principal plus any previously accumulated interest, resulting in exponential growth that generates significantly larger totals over long time horizons.

## Pitfalls and gotchas

- Applying simple interest formulas when the investment actually compounds can result in significantly underestimating the future value.
- The frequency of compounding (monthly, quarterly, annually) affects the effective return; high-frequency compounding yields higher total returns than annual compounding at the same nominal rate.

## Sources

- [[CFI - Interest Rate Calculator]]
- [[CFI - Compound Interest]]
- [[CFI - Continuously Compounded Return]]
