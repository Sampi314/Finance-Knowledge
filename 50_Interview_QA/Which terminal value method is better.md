---
type: question
title: "Which terminal value method is better"
tests: ["[[Exit multiple method]]", "[[Gordon growth method]]"]
difficulty: intermediate
updated: 2026-04-11
---

# Which terminal value method is better

## The question

"Which terminal value method is better: the Gordon Growth Method or the Exit Multiple Method?"

## Short answer (30 seconds)

Neither method is inherently "better." They serve different purposes and look at valuation from different angles. Academics often prefer the Gordon Growth Method because it values a company purely on its fundamental ability to generate cash flow in perpetuity. However, practitioners and bankers heavily favor the Exit Multiple Method because it is grounded in observable market realities and answers what a real buyer would pay for the business at the end of the projection period.

## Long answer (2 minutes)

The best approach is not choosing one, but using both and cross-checking the results. They work best in different contexts:

1. **Gordon Growth Method:** This is best for mature, stable businesses where cash flows are expected to grow predictably at a low rate forever (typically tracking GDP or inflation). It values the company as an ongoing, standalone enterprise.
2. **Exit Multiple Method:** This is ideal for transaction-oriented contexts, such as M&A advisory or private equity/LBO models with defined exit horizons. It calculates what the company could be sold for based on current comparable company or precedent transaction multiples.

In practice, after calculating the terminal value using an Exit Multiple, you should calculate the *implied perpetual growth rate* to ensure it makes economic sense. If an exit multiple implies a perpetual growth rate of 8%, that is mathematically impossible in the long run since it exceeds the growth of the overall economy. Conversely, if you use Gordon Growth, you should calculate the *implied exit multiple* to make sure the resulting valuation is somewhat in line with what comparable companies are actually trading for in the market.

## Common follow-ups

- **How do you calculate the implied perpetual growth rate from an exit multiple?** By rearranging the Gordon Growth formula: $g_{implied} = WACC - \frac{FCF_{n+1}}{\text{Terminal Value}}$. This allows you to sanity-check if your chosen exit multiple implies a realistic long-term growth rate.
- **What is a common mistake when using the Exit Multiple Method?** Applying today's multiples (which might be inflated or depressed by current market cycles) to a future year's EBITDA without considering if the market conditions or the company's growth profile will change by the exit year.
