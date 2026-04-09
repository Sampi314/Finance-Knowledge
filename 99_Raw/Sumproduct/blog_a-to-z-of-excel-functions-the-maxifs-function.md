# A to Z of Excel Functions: The MAXIFS Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-maxifs-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The MAXIFS Function

*   January 23, 2022

A to Z of Excel Functions: The MAXIFS Function
==============================================

A to Z of Excel Functions: The MAXIFS Function
==============================================

24 January 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **MAXIFS** function._

**The MAXIFS function**

The **MAXIFS** function returns the maximum value among cells specified by a given set of conditions or criteria. It has the following syntax:

**MAXIFS(max\_range, criterion\_range1, criterion1, \[criterion\_range2, criterion2\], …)**

where:

*   **max\_range** is the actual range of cells in which the maximum is to be determined
*   **criterion\_range1** is the set of cells to evaluate with the criterion specified
*   **criterion1** is the criterion in the form of a number, expression or text that defines which cells will be evaluated as a maximum
*   **criterion\_range2** (onwards) and **criterion2** (onwards) are the additional ranges and their associated criteria. 126 range / criterion pairs may be specified. All ranges must have the same dimensions otherwise the function returns an _#VALUE!_ error.

It should be noted that:

*   the size and shape of the **max\_range** and **criteria\_rangeN** arguments must be the same, otherwise these functions return the _#VALUE!_ error.

As an example:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-104.jpg)

This example **_is_** preferable to its standard Excel counterpart:

**{=MAX(IF(G13:G31=H34,IF(H13:H31=H35,IF(I13:I31=H36,J13:J31))))}**

[Array formulae](https://www.sumproduct.com/thought/array-of-light)
 are cumbersome and not readily understood, which is why **MAXIFS** may be a highly viable alternative.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-maxifs-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-maxifs-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-maxifs-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-maxifs-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-maxifs-function/#0 "close")

top