# A to Z of Excel Functions: The BETA.INV Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-beta-inv-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The BETA.INV Function

*   December 1, 2016

A to Z of Excel Functions: The BETA.INV Function
================================================

A to Z of Excel Functions: The BETA.INV Function
================================================

2 December 2016

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **BETA.INV** function._

**The BETA.INV function**

In probability theory and statistics, the **beta distribution** is a family of continuous probability distributions defined on the interval \[0, 1\] parametrised by two positive shape parameters, denoted by **α** (**alpha**) and **β** (**beta**), that appear as exponents of the random variable and control the shape of the distribution. It has nothing to do with either the beta function (Euler integral) used in other areas of mathematics or the beta cited as the scalar in the Capital Asset Pricing Model.

The beta distribution has been applied to model the behavior of random variables limited to intervals of finite length in a wide variety of disciplines. For example, it has been used as a statistical description of allele frequencies in population genetics, time allocation in project management / control systems, sunshine data, variability of soil properties, proportions of the minerals in rocks in stratigraphy and heterogeneity in the probability of HIV transmission. Who’d have thought statistics and Excel could be so interesting?

In Bayesian inference, the beta distribution is the conjugate prior probability distribution for the Bernoulli, binomial, negative binomial and geometric distributions. For example, the beta distribution can be used in Bayesian analysis to describe initial knowledge concerning probability of success such as the probability that a space vehicle will successfully complete a specified mission. The beta distribution is a suitable model for the random behavior of percentages and proportions.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

The usual formulation of the beta distribution is also known as the beta distribution of the first kind, whereas beta distribution of the second kind is an alternative name for the beta prime distribution.

The **BETA.INV** function returns the inverse of the beta cumulative probability density function (**BETA.DIST**). Be careful: there is a similar function called **BETAINV** which is slightly different (more next time).

If **probability** = **BETA.DIST**(**x**,…**TRUE**), then **BETA.INV**(**probability**,…) = **x**. The beta distribution can be used in project planning to model probable completion times given an expected completion time and variability.

The **BETA.INV** function employs the following syntax to operate:

**BETA.INV(probability,alpha,beta,\[A\],\[B\])**

The **BETA.INV** function has the following arguments:

*   **probability**: required. This represents a **probability** associated with the beta distribution
*   **alpha**: also required. This is a parameter of the distribution
*   **beta**: required. This is also a parameter the distribution
*   **A**: optional. This is a lower bound to the interval of **x**
*   **B**: this is also optional. This is an upper bound to the interval of **x**.

It should be further noted that:

*   If any argument is nonnumeric, **BETA.INV** returns the _#VALUE!_ error value
*   If **alpha** ≤ 0 or **beta** ≤ 0, **BETA.INV** returns the _#NUM!_ error value
*   If **probability** ≤ 0 or **probability** > 1, **BETA.INV** returns the _#NUM!_ error value
*   If you omit values for **A** and **B**, **BETA.INV** uses the standard cumulative beta distribution, so that **A** = 0 and **B** = 1
*   This function first appeared in Excel 2010 and is not backwards compatible. It is essentially a more flexible version of its predecessor, **BETAINV**.

Given a value for probability, **BETA.INV** seeks that value **x** such that **BETA.DIST(x, alpha, beta, TRUE, A, B)** = probability. Thus, precision of **BETA.INV** depends upon the precision of **BETA.DIST**.

Here’s an example:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-beta-inv-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-beta-inv-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-beta-inv-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-beta-inv-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-beta-inv-function/#0 "close")

top