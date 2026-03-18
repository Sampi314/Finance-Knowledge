# A to Z of Excel Functions: The CONFIDENCE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CONFIDENCE Function

*   September 24, 2017

A to Z of Excel Functions: The CONFIDENCE Function
==================================================

A to Z of Excel Functions: The CONFIDENCE Function
==================================================

25 September 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CONFIDENCE** function._

**The CONFIDENCE function**

Do you need more **CONFIDENCE** in your Excel files? This function returns the confidence interval for a population mean, using the theory associated with the normal distribution.

To explain: the confidence interval is a range of values around a sample mean, **x**, which sits at the centre of this range, _i.e._ the range is **x** ± **CONFIDENCE**. For example, if **x** is the sample mean of delivery times for products ordered through the mail, **x ± CONFIDENCE** is a range of population means.

For any population mean, **μ0**, in this range, the probability of obtaining a sample mean further from **μ0** than **x** is greater than the significance level required, **alpha**; for any population mean, **μ0**, not in this range, the probability of obtaining a sample mean further from **μ0**than **x** is less than this level, **alpha**. In other words, assume that we use **x**, a standard deviation **standard\_dev**, and **size** to construct a two-tailed test at significance level alpha of the hypothesis that the population mean is **μ0**. Then we will not reject that hypothesis if **μ0**is in the confidence interval and will reject that hypothesis if **μ0** is not in the confidence interval. The confidence interval does not allow us to infer that there is probability **1 – alpha** that our next package will take a delivery time that is in the confidence interval.

The **CONFIDENCE** function employs the following syntax to operate:

**CONFIDENCE**(**alpha**, **standard\_dev**, **size**)

*   **alpha:** this is required. This represents the significance level used to compute the confidence level. The confidence level equals **100\*(1 – alpha)%**, or in other words, an **alpha** of 0.05 indicates a 95 percent confidence level
*   **standard\_dev:** this is also required. This is the population standard deviation for the data range and is assumed to be known
*   **size:** also required. This is the sample size.

It should be further noted that:

*   if any argument is non-numeric, **CONFIDENCE** returns the _#VALUE!_ error value
*   if **alpha** is ≤ 0 or ≥ 1, **CONFIDENCE** returns the _#NUM!_ error value
*   if **standard\_dev** ≤ 0, **CONFIDENCE** returns the _#NUM!_ error value
*   if **size** is not an integer, it is truncated
*   if **size** < 1, **CONFIDENCE** returns the _#NUM!_ error value
*   if we assume **alpha** equals 0.05, we need to calculate the area under the standard normal curve that equals **1 – alpha**, or 95%. This value is ± 1.96. The confidence interval is therefore:

![](https://sumproduct.com/wp-content/uploads/2025/05/4aa4954ccada961991fff85336e5a000-1.jpg)

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/dd4b4b32b1e9db045fbc48ad493a77b6.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-confidence-function/#0 "close")

top