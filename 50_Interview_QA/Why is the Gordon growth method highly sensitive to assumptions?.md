---
type: question
title: "Why is the Gordon growth method highly sensitive to assumptions?"
tests: ["[[Gordon growth method]]"]
difficulty: intermediate
updated: 2026-04-11
---

# Why is the Gordon growth method highly sensitive to assumptions?

## The question

Why is the Gordon Growth Method considered so sensitive to its inputs, and how do small changes affect the valuation?

## Short answer (30 seconds)

The Gordon Growth Method is highly sensitive because it values a cash flow stream to infinity. A small absolute change in either the discount rate (WACC) or the perpetual growth rate dramatically changes the spread between the two (the denominator). Because the denominator is usually a very small number (e.g., 5% to 8%), changing it by just 0.5% creates a large relative percentage swing in the final terminal value.

## Long answer (2 minutes)

The Gordon Growth Method calculates terminal value using the formula: $\frac{FCF \times (1+g)}{WACC - g}$.

Because we are projecting cash flows forever, the spread in the denominator ($WACC - g$) acts as a massive lever.

For example, imagine a company with next year's cash flow of $100, WACC of 10%, and a growth rate of 3%.
- The denominator is $10\% - 3\% = 7\%$.
- The terminal value is $\frac{100}{0.07} \approx \$1,429$.

If you decrease the perpetual growth rate by just 0.5% (from 3.0% to 2.5%):
- The denominator becomes $10\% - 2.5\% = 7.5\%$.
- The terminal value becomes $\frac{100}{0.075} \approx \$1,333$.

A mere 0.5% absolute change in the growth rate caused the denominator to increase relatively by over 7%, wiping out nearly $100 million in terminal value. Given that terminal value often makes up 60-80% of a company's total enterprise value in a DCF, this sensitivity means that tiny tweaks to WACC or long-term growth can swing the implied share price by huge margins. This is why investment committees scrutinize these specific assumptions relentlessly.

## Common follow-ups

- **How do you sanity check your Gordon Growth assumptions?** Explain that you cross-check the implied exit multiple. If your Gordon Growth assumption implies the company will trade at 25x EBITDA at the end of the projection period, but comparable mature companies trade at 10x, your perpetual growth rate is likely too high or your WACC is too low.
