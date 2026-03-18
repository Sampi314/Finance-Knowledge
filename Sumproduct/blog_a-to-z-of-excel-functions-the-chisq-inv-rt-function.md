# A to Z of Excel Functions: The CHISQ.INV.RT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-rt-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CHISQ.INV.RT Function

*   June 18, 2017

A to Z of Excel Functions: The CHISQ.INV.RT Function
====================================================

A to Z of Excel Functions: The CHISQ.INV.RT Function
====================================================

19 June 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CHISA.INV.RT** function._

**The CHISQ.INV.RT function**

In probability theory and statistics, the chi-squared distribution (also chi-square or **χ2**\-distribution) with **k** degrees of freedom is the distribution of a sum of the squares of **k** independent standard normal random variables. It is one of the most widely used probability distributions in inferential statistics, _e.g._ in hypothesis testing or in construction of confidence intervals.

The chi-squared distribution is used in the common chi-squared tests for goodness of fit of an observed distribution to a proposed theoretical one, the independence of two criteria of classification of qualitative data, and in confidence interval estimation for a population standard deviation of a normal distribution from a sample standard deviation.

If **Z1**, …, **Zk** are independent, standard normal random variables, then the sum of their squares

![](<Base64-Image-Removed>)

is distributed according to the chi-squared distribution with **k** degrees of freedom. This is usually denoted as

![](<Base64-Image-Removed>)

Thus, the chi-squared distribution has one parameter: **k** — a positive integer that specifies the number of degrees of freedom.

As aforementioned, the chi-squared distribution is used primarily in hypothesis testing. Unlike more widely known distributions such as the normal distribution and the exponential distribution, the chi-squared distribution is rarely used to model natural phenomena. It arises in the following hypothesis tests, among others.

The primary reason that the chi-squared distribution is used extensively in hypothesis testing is its relationship to the normal distribution. Many hypothesis tests use a test statistic, such as the **t** statistic in a **t-test**. For these hypothesis tests, as the sample size, **n**, increases, the sampling distribution of the test statistic approaches the normal distribution (**Central Limit Theorem**). Since the test statistic (such as **t**) is asymptotically normally distributed, provided the sample size is sufficiently large, the distribution used for hypothesis testing may be approximated by a normal distribution. Testing hypotheses using a normal distribution is well understood and relatively easy. The simplest chi-squared distribution is the square of a standard normal distribution. So wherever a normal distribution could be used for a hypothesis test, a chi-squared distribution could be used.

A chi-squared distribution constructed by squaring a single standard normal distribution is said to have 1 degree of freedom, _etc._

This function returns the inverse of the right-tailed probability of the chi-squared distribution. If probability = **CHISQ.DIST.RT(x**,…**)**, then **CHISQ.INV.RT(probability**,…**)** = **x**. Use this function to compare observed results with expected ones in order to decide whether your original hypothesis is valid.

![](<Base64-Image-Removed>)

The **CHISQ.INV.RT** function employs the following syntax to operate:

**CHISQ.INV.RT(probability, deg\_freedom)**

The **CHISQ.INV.RT** function has the following arguments:

*   **probability:** this is required and represents a probability associated with the chi-squared distribution
*   **deg\_freedom:** this is also required. This denotes the number of degrees of freedom.

It should be further noted that:

*   if either argument is nonnumeric, **CHISQ.INV.RT** returns the _#VALUE!_ error value
*   if **probability** < 0 or **probability** > 1, **CHISQ.INV.RT** returns the _#NUM!_ error value
*   if **deg\_freedom** is not an integer, it is truncated
*   if **deg\_freedom** < 1, **CHISQ.INV.RT** returns the _#NUM!_ error value
*   **CHISQ.INV.RT** appears to be the Excel 2010 replacement for the **CHIINV** function.

Given a value for probability, **CHISQ.INV.RT** seeks that value **x** such that **CHISQ.DIST.RT(x, deg\_freedom)** = **probability**. Thus, precision of **CHISQ.INV.RT** depends on precision of **CHISQ.DIST.RT.****CHISQ.INV.RT** uses an iterative search technique. If the search has not converged after 64 iterations, the function returns the _#N/A_ error value. There aren’t many functions that stop at 64 iterations: we would be interested to know why this is the case here.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-rt-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-rt-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-rt-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-rt-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-rt-function/#0 "close")

top