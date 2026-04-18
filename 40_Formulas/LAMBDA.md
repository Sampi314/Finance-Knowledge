---
type: formula
title: "LAMBDA"
used_in: ["[[LAMBDA function]]"]
updated: 2024-05-24
---

# LAMBDA

$$=\text{LAMBDA}([\text{parameter1}, \text{parameter2}, \dots,], \text{calculation})$$

**Variables**

- $parameter$ — An optional input value for the function, such as a cell reference, number, or text string. You can use up to 253 parameters.
- $calculation$ — The formula to execute using the parameters. It must be the final argument and must return a value.

**Notes**

To test the formula in a cell before adding it to the Name Manager, append the testing parameters in a separate set of parentheses, like `=LAMBDA(x, y, x+y)(A1, B1)`.
