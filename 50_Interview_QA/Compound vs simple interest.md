---
type: question
title: "Compound vs simple interest"
tests: ["[[Compound interest]]"]
difficulty: beginner
updated: 2026-04-09
---

# Compound vs simple interest

## The question

What is the difference between simple interest and compound interest, and which is more relevant in financial modeling?

## Short answer (30 seconds)

Simple interest is calculated solely on the original principal amount, whereas compound interest is calculated on both the original principal and the accumulated interest from prior periods. In financial modeling, compound interest is far more relevant because virtually all real-world financial instruments, investments, and debt obligations accrue interest on a compounding basis.

## Long answer (2 minutes)

The fundamental difference lies in what base the interest rate is applied to.

1.  **Simple Interest:** The interest calculation is strictly `Principal × Rate × Time`. If you deposit $100 at 5% simple interest, you earn exactly $5 every year, regardless of how long the money sits there. The accrued interest is never added to the principal to generate more interest.
2.  **Compound Interest:** The interest calculation applies the rate to the current balance, which includes the original principal plus all previously accumulated interest. If you deposit $100 at 5% compounding annually, you earn $5 in year one. In year two, your balance is $105, so you earn 5% on $105, which is $5.25.

Because compound interest generates "interest on interest", it leads to exponential growth over time, creating a snowball effect.

In financial modeling, you will almost exclusively use compound interest. Whether you are modeling a leveraged buyout, projecting a DCF, calculating the future value of a company's cash flows, or projecting debt schedules, the assumption is always that returns compound. Simple interest is rarely seen outside of very short-term, specific consumer loans or introductory textbook examples.

## Common follow-ups

- **How does the frequency of compounding affect returns?**
  - **How to handle:** Explain that more frequent compounding (e.g., monthly vs. annually) leads to higher overall returns because the interest is added to the principal more often, allowing "interest on interest" to start accumulating sooner.
