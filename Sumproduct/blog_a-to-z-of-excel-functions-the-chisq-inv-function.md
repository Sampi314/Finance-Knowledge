# A to Z of Excel Functions: The CHISQ.INV Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CHISQ.INV Function

*   June 11, 2017

A to Z of Excel Functions: The CHISQ.INV Function
=================================================

A to Z of Excel Functions: The CHISQ.INV Function
=================================================

12 June 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CHISQ.INV** function._

**The CHISQ.INV function**

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

This function returns the inverse of the left-tailed probability of the chi-squared distribution. The chi-squared distribution is commonly used to study variation in the percentage of something across samples, such as the fraction of the day people spend trying to understand what this function does.

![](<Base64-Image-Removed>)

The **CHISQ.INV** function employs the following syntax to operate:

**CHISQ.INV(probability, deg\_freedom)**

The **CHISQ.INV** function has the following arguments:

*   **probability:** this is required and represents a probability associated with the chi-squared distribution
*   **deg\_freedom:** this is also required. This denotes the number of degrees of freedom.

It should be further noted that:

*   if either argument is nonnumeric, **CHISQ.INV** returns the _#VALUE!_ error value
*   if **probability** < 0 or **probability** > 1, **CHISQ.INV** returns the _#NUM!_ error value
*   if **deg\_freedom** is not an integer, it is truncated
*   if **deg\_freedom** < 1 or **deg\_freedom** > 10^10, **CHISQ.INV** returns the _#NUM!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found here._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chisq-inv-function/#0 "close")

top