---
type: concept
title: "IFS function"
aliases: []
tags: ["excel", "functions", "logic"]
difficulty: beginner
prerequisites: ["[[IF and nested IF]]"]
related: ["[[SUMIFS and COUNTIFS]]"]
sources: ["[[Trump Excel - Test Multiple Conditions Using Excel IFS Function]]", "[[Sumproduct - A to Z of Excel Functions- The IFS Function]]"]
status: draft
updated: 2026-04-18
---

# IFS function

> **TL;DR.** The IFS function allows you to test multiple conditions at once and returns the result for the first condition that evaluates to TRUE, eliminating the need for complex nested IF formulas.

## When you'd use this

You would use the IFS function when you have multiple conditions that need to be evaluated in a specific sequence. It is particularly useful for grading or categorization, such as assigning letter grades based on test scores or determining tiered sales commissions.

## The 30-second version

The IFS function evaluates a series of logical tests and returns the value corresponding to the first test that evaluates to TRUE. It can handle up to 127 condition/value pairs, significantly streamlining formulas that would otherwise require multiple nested IF statements. If no condition is met, the formula returns an #N/A error.

## The full explanation

Introduced in Excel 2016 (and available in Office 365), the IFS function evaluates multiple conditions in sequence. The syntax requires pairs of arguments: a `logical_test` followed by the `value_if_true`. Excel stops evaluating as soon as it finds the first true condition.

Because there is no inherent "ELSE" argument in the IFS function, it is standard practice to use `TRUE` or `1=1` as the final `logical_test` to catch any scenarios that did not meet the preceding conditions, providing a fallback `value_if_true`. Without an explicit catch-all, if all conditions are FALSE, the function returns an `#N/A` error. Additionally, if a `logical_test` evaluates to something other than TRUE or FALSE (or equivalent numbers), the function returns a `#VALUE!` error.

While IFS simplifies nested IFs, extremely long logic chains can still be difficult to debug. In some cases, utilizing a lookup function (like VLOOKUP with approximate match) or employing boolean flags (multiplying true/false conditions by 1) can provide more transparent and manageable solutions.

## Formula

`=IFS(logical_test1, value_if_true1, [logical_test2, value_if_true2], ...)`

## Worked example

To calculate a commission based on sales values stored in cell B2 and tiers listed in columns E and F:
`=IFS(B2<$E$3, $F$2, B2<$E$4, $F$3, B2<$E$5, $F$4, B2<$E$6, $F$5, B2>$E$6, $F$6)*B2`
If B2 contains a sales value of $5000, and $E$3 is $1000 with $F$2 being 2%, and $E$4 is $10000 with $F$3 being 5%, it will evaluate `B2<$E$3` as FALSE, evaluate `B2<$E$4` as TRUE, and multiply $5000 by 5%.

## Excel and modeling notes

- Always include a final condition of `TRUE` (with its corresponding default value) to act as an "ELSE" statement and prevent `#N/A` errors.
- Ensure that you order your conditions correctly, going from most specific/restrictive to least, because IFS stops at the first TRUE condition.
- Using boolean flags (e.g., `=(condition=TRUE)*1`) can sometimes be a clearer alternative to complex nested logic for other users trying to read the model.

## Interview-ready answer

The IFS function lets you evaluate multiple conditions in sequence without using confusing nested IF statements. It tests pairs of conditions and return values, outputting the value for the first true condition, and it's best practice to add a final condition of TRUE to act as a catch-all ELSE.

## Pitfalls and gotchas

- Not including a final catch-all condition (like TRUE), resulting in an `#N/A` error if no earlier conditions are met.
- Incorrectly ordering conditions, which may cause a broader condition to be met before a more specific one is evaluated.
- Using IFS for simple table lookups when an approximate match VLOOKUP or XLOOKUP would be more efficient and easier to update.

## Sources

- [[Trump Excel - Test Multiple Conditions Using Excel IFS Function]]
- [[Sumproduct - A to Z of Excel Functions- The IFS Function]]
