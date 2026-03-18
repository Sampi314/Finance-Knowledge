# A to Z of Excel Functions: The CHITEST Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chitest-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CHITEST Function

*   July 9, 2017

A to Z of Excel Functions: The CHITEST Function
===============================================

A to Z of Excel Functions: The CHITEST Function
===============================================

10 July 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CHITEST** function._

**The CHITEST function**

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

This function returns the test for independence. **CHITEST** returns the value from the chi-squared (**χ2**) distribution for the statistic and the appropriate degrees of freedom. You can use **χ2** tests to determine whether hypothesised results are verified by an experiment.

![](<Base64-Image-Removed>)

The **CHITEST** function employs the following syntax to operate:

**CHITEST(actual\_range, expected\_range)**

The **CHITEST** function has the following arguments:

*   **actual\_range:** this is required and represents the range of data that contains observations to test against expected values
*   **expected\_range:** this is also required. This denotes the range of data that contains the ratio of the product of row totals and column totals to the grand total.

It should be further noted that:

*   if **actual\_range** and **expected\_range** have a different number of data points, **CHITEST** returns the _#N/A_ error value
*   the **χ2** test first calculates a **χ2** statistic using the formula:

![](<Base64-Image-Removed>)

where:

o **Aij** \= actual frequency in the **i**\-th row, **j**\-th column

o **Eij** \= expected frequency in the **i**\-th row, **j**\-th column

o **r** = number or rows

o **c** = number of columns

*   a low value of **χ2** is an indicator of independence. As can be seen from the formula above, **χ2** is always positive or 0, and is 0 only if **Aij** = **Eij** for every **i** and **j**
*   **CHITEST** returns the probability that a value of the **χ2** statistic at least as high as the value calculated by the above formula could have happened by chance under the assumption of independence. In computing this probability, **CHITEST** uses the **χ2** distribution with an appropriate number of degrees of freedom, **df**.
*   If **r** \> 1 and **c** > 1, then **df = (r – 1)(c – 1)**. If **r** = 1 and **c** > 1, then **df = c – 1** or if **r** > 1 and **c** = 1, then **df = r – 1**. **r** \= **c** \= 1 is not allowed and _#N/A_ is returned
*   the use of **CHITEST** is most appropriate when **Eij**‘s are not too small. Some statisticians suggest that each **Eij** should be greater than or equal to 5
*   It should be noted that this function has been replaced with one or more new functions from Excel 2010 onwards (**CHISQ.TEST**) that may provide improved accuracy and whose names better reflect their usage. Although this function is still available for backward compatibility, you should consider using the new functions from now on, because this function may not be available in future versions of Excel. This may require you to amend existing models too.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chitest-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chitest-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chitest-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chitest-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-chitest-function/#0 "close")

top