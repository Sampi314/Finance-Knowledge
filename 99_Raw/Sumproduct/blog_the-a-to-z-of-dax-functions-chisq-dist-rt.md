# The A to Z of DAX Functions – CHISQ.DIST.RT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-chisq-dist-rt/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CHISQ.DIST.RT

*   January 4, 2022

The A to Z of DAX Functions – CHISQ.DIST.RT
===========================================

Power Pivot Principles: The A to Z of DAX Functions – CHISQ.DIST.RT
===================================================================

4 January 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CHISQ.DIST.RT** function._

**_The CHISQ.DIST.RT function_**

In probability theory and statistics, the chi-squared distribution (also chi-square or **χ2**\-distribution) with **k** degrees of freedom is the distribution of a sum of the squares of **k** independent standard normal random variables. It is one of the most widely used probability distributions in inferential statistics, _e.g._ in hypothesis testing or in construction of confidence intervals.

The chi-squared distribution is used in the common chi-squared tests for goodness of fit of an observed distribution to a proposed theoretical one, the independence of two criteria of classification of qualitative data, and in confidence interval estimation for a population standard deviation of a normal distribution from a sample standard deviation.

If **Z1**, …, **Zk** are independent, standard normal random variables, then the sum of their squares

![](<Base64-Image-Removed>)

is distributed according to the chi-squared distribution with **k** degrees of freedom. This is usually denoted as

![](<Base64-Image-Removed>)

Thus, the chi-squared distribution has one parameter: **k** — a positive integer that specifies the number of degrees of freedom.

As aforementioned, the chi-squared distribution is used primarily in hypothesis testing. Unlike more widely known distributions such as the normal distribution and the exponential distribution, the chi-squared distribution is rarely used to model natural phenomena. It arises in the following hypothesis tests, among others.

The primary reason that the chi-squared distribution is used extensively in hypothesis testing is its relationship to the normal distribution. Many hypothesis tests use a test statistic, such as the **t** statistic in a **t-test**. For these hypothesis tests, as the sample size, **n**, increases, the sampling distribution of the test statistic approaches the normal distribution (**Central Limit Theorem**). Since the test statistic (such as **t**) is asymptotically normally distributed, provided the sample size is sufficiently large, the distribution used for hypothesis testing may be approximated by a normal distribution. Testing hypotheses using a normal distribution is well understood and relatively easy. The simplest chi-squared distribution is the square of a standard normal distribution. Therefore, wherever a normal distribution could be used for a hypothesis test, a chi-squared distribution could be used.

A chi-squared distribution constructed by squaring a single standard normal distribution is said to have 1 degree of freedom, _etc._

The **CHISQ.DIST.RT** function returns the right-tailed probability of the chi-squared distribution. The **χ2** distribution is associated with a **χ2** test. It is used to test the **χ2** test to compare observed and expected values. For example, a genetic experiment might hypothesise that the next generation of plants will exhibit a certain set of colours. By comparing the observed results with the expected ones, you can decide whether your original hypothesis is valid.

The **CHISQ.DIST.RT** function employs the following syntax to operate:

**CHISQ.DIST.RT(x, deg\_freedom)**

The **CHISQ.DIST.RT** function has the following arguments:

*   **x:** this is required and represents the value at which you want to evaluate the distribution
*   **deg\_freedom:** this is also required. This denotes the number of degrees of freedom.

It should be further noted that:

*   if either argument is nonnumeric, **CHISQ.DIST.RT** function returns an error
*   if x is negative, **CHISQ.DIST.RT** returns an error
*   if **deg\_freedom** is not an integer, it is rounded
*   if **deg\_freedom** < 1 or **deg\_freedom** > 10^10, **CHISQ.DIST.RT** returns an error
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

**_Example_**

One-tailed probability of the chi-squared distribution for 18.307, using 10 degrees of freedom. The result is 0.050001.

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-chisq-dist-rt/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-chisq-dist-rt/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-chisq-dist-rt/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-chisq-dist-rt/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-chisq-dist-rt/#0 "close")

top