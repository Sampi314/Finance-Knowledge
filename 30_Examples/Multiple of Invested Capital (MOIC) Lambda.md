---
type: example
title: "Multiple of Invested Capital (MOIC) Lambda"
illustrates: ["[[LAMBDA function]]"]
updated: 2024-05-24
---

# Multiple of Invested Capital (MOIC) Lambda

## Setup

We want to calculate the MOIC for an investment using a range of cash flows without having to repeatedly type out the standard `SUMIF` calculations. We'll create a custom LAMBDA function to handle this.

## Assumptions

- Range of cash flows contains at least one negative number (investment) and at least one positive number (return).

## Walk-through

1. The standard formula to calculate MOIC is `=-SUMIF(Range, ">0", Range) / SUMIF(Range, "<=0", Range)`.
2. Convert this to a generic LAMBDA function: `=LAMBDA(Range, -SUMIF(Range, ">0", Range) / SUMIF(Range, "<=0", Range))`.
3. Add error-checking using `IF` and `COUNTIF` to ensure the range has valid inputs: `=LAMBDA(Range, IF(AND(COUNTIF(Range,"<0")>=1, COUNTIF(Range,">0")>=1), -SUMIF(Range,">0",Range) / SUMIF(Range,"<=0",Range), "Range must have at least 1 positive and 1 negative number in it."))`.
4. Open the Name Manager (Ctrl + F3) and create a new name called `MOIC`.
5. Paste the final LAMBDA formula into the "Refers to" box.
6. In the spreadsheet, calculate MOIC by typing `=MOIC(F76:K76)`.

## Result

The custom function cleanly calculates the MOIC, returning an error message if the cash flows are entirely positive or entirely negative.

## What this teaches

- How to convert a standard formula into a reusable custom function.
- How to incorporate error-checking into a LAMBDA function.
- The value of naming LAMBDAs for repeated use in financial models.
