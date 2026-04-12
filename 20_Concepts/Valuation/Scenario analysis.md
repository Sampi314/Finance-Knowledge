---
type: concept
title: "Scenario analysis"
aliases: []
tags: ["Valuation", "Risk", "Modeling"]
difficulty: intermediate
prerequisites: ["[[Sensitivity analysis]]", "[[DCF valuation]]"]
related: ["[[Sensitivity analysis]]"]
sources: ["[[IB Interview Questions - Sensitivity and Scenario Analysis in Financial Modeling]]"]
status: draft
updated: 2026-04-12
---

# Scenario analysis

> **TL;DR.** Scenario analysis is a technique that changes multiple input variables simultaneously to model different potential states of the world, typically a base, bull, and bear case.

## When you'd use this

You use scenario analysis when presenting to a board, an investment committee, or management to provide coherent alternative futures. Rather than tweaking isolated variables as in sensitivity analysis, scenarios tell a consistent story (e.g., a "recession scenario" where growth drops, margins shrink, and multiples contract all at once).

## The 30-second version

Every financial model is built on assumptions, and those assumptions are inherently uncertain. Scenario analysis groups these variables into coherent sets (scenarios) to evaluate distinct possible futures. The standard framework uses three scenarios: a Base Case (management's best estimate), a Bull Case (optimistic but plausible), and a Bear Case (pessimistic but realistic). This transforms a single point-estimate valuation into a probability-weighted expected value or a range of outcomes.

## The full explanation

Scenario analysis takes a comprehensive approach by altering multiple interconnected variables to mirror specific business environments.

### Structuring the Scenarios
- **Base Case:** This is the consensus expectation. Revenue grows at historical trends, margins are stable, and market conditions remain normal.
- **Bull Case:** This is an optimistic but plausible state. It assumes revenue accelerates (perhaps due to successful product launches), margins expand via operating leverage, and market conditions are highly favorable.
- **Bear Case:** A pessimistic view where revenue growth slows or declines (recession, customer loss), margins compress, and market conditions deteriorate. It should represent genuine downside risk, not a doomsday event.

### Probability Weighting
In contexts like fairness opinions, you can assign probability weights to each scenario to calculate an expected value:
$$ \text{Expected Value} = (P_{\text{bull}} \times V_{\text{bull}}) + (P_{\text{base}} \times V_{\text{base}}) + (P_{\text{bear}} \times V_{\text{bear}}) $$

### Implementation
The most effective way to implement scenarios in Excel is using a "scenario toggle"—a single cell (e.g., 1=Bull, 2=Base, 3=Bear) that drives all assumption inputs via `CHOOSE`, `INDEX`, or `IF` functions, automatically updating the entire model.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

- Use a **scenario toggle** (a single cell dropdown) linked to all model assumptions via `CHOOSE` or `INDEX` to seamlessly recalculate all financial statements without maintaining separate model versions.
- **Tornado Charts** are an excellent visual tool to complement scenarios, as they rank variables by their impact on the output, showing the upside and downside ranges.
- When presenting to a board, use side-by-side scenario comparison tables rather than dense sensitivity grids, as they highlight the "story" behind the numbers better.

## Interview-ready answer

[[What is the difference between sensitivity and scenario analysis?]]

## Pitfalls and gotchas

- **Internal Inconsistency:** Mixing optimistic revenue growth with pessimistic margin assumptions in the same scenario. A scenario must be a coherent story.
- **Fantasy Scenarios:** Creating a bull case that is mathematically impossible to achieve or a bear case that assumes total catastrophic collapse. Keep scenarios plausible.
- **Double Counting Risk:** Applying conservative assumptions in the base case *and* using a very high discount rate, thereby double-penalizing the valuation.

## Sources

- [[IB Interview Questions - Sensitivity and Scenario Analysis in Financial Modeling]]
