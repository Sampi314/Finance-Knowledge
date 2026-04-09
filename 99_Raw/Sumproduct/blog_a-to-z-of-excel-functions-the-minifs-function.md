# A to Z of Excel Functions: The MINIFS Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-minifs-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The MINIFS Function

*   May 22, 2022

A to Z of Excel Functions: The MINIFS Function
==============================================

A to Z of Excel Functions: The MINIFS Function
==============================================

23 May 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **MINIFS** function._

**The MINIFS function**

The **MINIFS** function returns the minimum value among cells specified by a given set of conditions or criteria. It has the following syntax:

**MINIFS(min\_range, criterion\_range1, criterion1, \[criterion\_range2, criterion2\], …)**

where:

*   **min\_range** is the actual range of cells in which the minimum is to be determined
*   **criterion\_range1** is the set of cells to evaluate with the criterion specified
*   **criterion1** is the criterion in the form of a number, expression or text that defines which cells will be evaluated as a minimum
*   **criterion\_range2** (onwards) and **criterion2** (onwards) are the additional ranges and their associated criteria. 126 range / criterion pairs may be specified. All ranges must have the same dimensions otherwise the function returns an _#VALUE!_ error.

It should be noted that:

*   the size and shape of the **min\_range** and **criteria\_rangeN** arguments must be the same, otherwise these functions return the _#VALUE!_ error.

As an example:

![](<Base64-Image-Removed>)

This example **_is_** preferable to its standard Excel counterpart:

**{=MIN(IF(G13:G31=H34,IF(H13:H31=H35,IF(I13:I31=H36,J13:J31))))}**

Array formulae (see [Array of Light](https://www.sumproduct.com/thought/array-of-light)
for more information) are cumbersome and not readily understood, which is why **MINIFS** may be a highly viable alternative.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-minifs-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-minifs-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-minifs-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-minifs-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-minifs-function/#0 "close")

top