# A to Z of Excel Functions: The CONFIDENCE.T Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-t-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CONFIDENCE.T Function

*   October 8, 2017

A to Z of Excel Functions: The CONFIDENCE.T Function
====================================================

A to Z of Excel Functions: The CONFIDENCE.T Function
====================================================

9 October 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CONFIDENCE.T** function._

**The CONFIDENCE.T function**

Have you got your **CONFIDENCE** down to a **T**? This function first appeared in Excel 2010 but unlike **CONFIDENCE.NORM** there was no equivalent in earlier versions of Excel. That is because this function returns the confidence interval for a population mean, using a **Student’s t** distribution.

The **CONFIDENCE.T** function employs the following syntax to operate:

**CONFIDENCE.T**(**alpha**, **standard\_dev**, **size)**

*   **alpha:** this is required. This represents the significance level used to compute the confidence level. The confidence level equals **100\*(1 – alpha)%**, or in other words, an **alpha** of 0.05 indicates a 95 percent confidence level
*   **standard\_dev:** this is also required. This is the population standard deviation for the data range and is assumed to be known
*   **size:** also required. This is the sample size.

It should be further noted that:

*   if any argument is non-numeric, **CONFIDENCE.T** returns the _#VALUE!_ error value
*   if **alpha** is ≤ 0 or ≥ 1, **CONFIDENCE.T** returns the _#NUM!_ error value
*   if **standard\_dev** ≤ 0, **CONFIDENCE.T** returns the _#NUM!_ error value
*   if **size** is not an integer, it is truncated
*   if **size** < 1, **CONFIDENCE.T** returns the _#DIV/0!_ error value

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/cb0a8f2808fb61e01af3424c6d75194e.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-t-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-t-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-t-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-t-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-t-function/#0 "close")

top