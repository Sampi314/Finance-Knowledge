---
type: question
title: "What is the difference between sensitivity and scenario analysis?"
tests: ["[[Scenario analysis]]", "[[Sensitivity analysis]]"]
difficulty: beginner
updated: 2026-04-12
---

# What is the difference between sensitivity and scenario analysis?

## The question

What is the difference between sensitivity analysis and scenario analysis?

## Short answer (30 seconds)

Sensitivity analysis isolates the impact of a single variable by changing one input while holding everything else constant, answering "how much does value change if WACC increases by 1%?". Scenario analysis changes multiple variables simultaneously to model coherent alternative futures, such as a "recession case" where revenue, margins, and market multiples all decline together.

## Long answer (2 minutes)

Both techniques acknowledge that financial models are built on uncertain assumptions, but they tackle this uncertainty differently:

- **Sensitivity Analysis** is highly targeted. It isolates individual drivers to see how much the final output swings based on that single assumption. In investment banking, this is typically presented using one- or two-variable data tables in Excel (e.g., WACC vs. Terminal Growth Rate for a DCF). It's great for identifying which specific assumptions pose the biggest risk to the valuation.

- **Scenario Analysis** is holistic. Because real-world variables don't change in a vacuum, scenario analysis groups multiple assumptions into a coherent story. You typically build a Base Case, a Bull Case, and a Bear Case. For instance, in a Bear Case, you wouldn't just lower revenue growth; you would simultaneously compress margins and lower the exit multiple to reflect a deteriorating macroeconomic environment.

In practice, bankers use both: scenarios to frame the overall strategic possibilities, and sensitivity tables to show the mechanical sensitivity of the chosen base case to key inputs.

## Common follow-ups

- **When would you use a scenario analysis over a sensitivity table?** You'd use scenario analysis when presenting to a board or investment committee that needs to understand the big-picture risks and alternative outcomes, rather than just the mechanical impact of isolated variables.
- **Can you probability-weight sensitivity analysis?** Usually no, because sensitivity just maps a mechanical grid of possibilities. Probability weighting is typically applied to scenario analysis to calculate an overall expected value across the Base, Bull, and Bear cases.
