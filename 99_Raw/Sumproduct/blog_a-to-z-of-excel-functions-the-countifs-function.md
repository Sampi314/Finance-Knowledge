# A to Z of Excel Functions: The COUNTIFS Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-countifs-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The COUNTIFS Function

*   January 14, 2018

A to Z of Excel Functions: The COUNTIFS Function
================================================

A to Z of Excel Functions: The COUNTIFS Function
================================================

15 January 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **COUNTIFS** function._

**The COUNTIFS function**

This function applies one or more criteria to cells across multiple ranges and counts the number of times all criteria are met. This is essentially the “multiple” version of **COUNTIF** (please link to **COUNTIF**).

The **COUNTIFS** function employs the following syntax to operate:

**COUNTIFS(criteria\_range1, criteria1, \[criteria\_range2, criteria2\]…)**

The **COUNTIFS** function has the following arguments:

*   **criteria\_range1:** this is required and represents the first range in which to evaluate the associated criteria
*   **criteria1:** this is also required. The criteria must be in the form of a number, expression, cell reference, or text that define which cells will be counted. For example, criteria can be expressed as 32, “>32”, **B4**, “apples”, or “32”
*   **criteria\_range2, criteria2, …:** these arguments are optional but must appear in associated pairs. Up to 127 range / criteria pairs are allowed.

It should be further noted that:

*   **COUNTIFS** ignores upper and lower case in text strings. **Criteria** are not case sensitive, so “red” and “RED” will match the same cells
*   each range’s criteria is applied one cell at a time. If all of the first cells meet their associated criteria, the count increases by 1. If all of the second cells meet their associated criteria, the count increases by 1 again, and so on until all of the cells are evaluated
*   if the criteria argument is a reference to an empty cell, the **COUNTIFS** function treats the empty cell as a zero value
*   wildcard characters are permitted. The characters, question mark (?) and asterisk (\*) can be used in **criterion**. The question mark matches any single character, whereas an asterisk matches any sequence of characters. If you actually want to find a question mark or asterisk use the tilde (~) in front of the required character.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found here._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-countifs-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-countifs-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-countifs-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-countifs-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-countifs-function/#0 "close")

top