# The A to Z of DAX Functions – BETA.DIST

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-beta-dist/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – BETA.DIST

*   October 26, 2021

The A to Z of DAX Functions – BETA.DIST
=======================================

Power Pivot Principles: The A to Z of DAX Functions – BETA.DIST
===============================================================

26 October 2021

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. Things are getting **BETA** this time…_

In probability theory and statistics, the **beta distribution** is a family of continuous probability distributions defined on the interval \[0, 1\] parameterised by two positive shape parameters, denoted by **α**(**alpha**) and **β** (**beta**), that appear as exponents of the random variable and control the shape of the distribution. It has nothing to do with either the beta function (Euler integral) used in other areas of mathematics or the beta cited as the scalar in the Capital Asset Pricing Model.

The beta distribution has been applied to model the behavior of random variables limited to intervals of finite length in a wide variety of disciplines. For example, it has been used as a statistical description of allele frequencies in population genetics, time allocation in project management / control systems, sunshine data, variability of soil properties, proportions of the minerals in rocks in stratigraphy and heterogeneity in the probability of HIV transmission. Who’d have thought statistics and Excel could be so interesting?

In Bayesian inference, the beta distribution is the conjugate prior probability distribution for the Bernoulli, binomial, negative binomial and geometric distributions. For example, the beta distribution can be used in Bayesian analysis to describe initial knowledge concerning probability of success such as the probability that a space vehicle will successfully complete a specified mission. The beta distribution is a suitable model for the random behavior of percentages and proportions.

The usual formulation of the beta distribution is also known as the beta distribution of the first kind, whereas beta distribution of the second kind is an alternative name for the beta prime distribution.

The **BETA.DIST** function returns the beta distribution, which is commonly used to study variation in the percentage of something across samples, such as the fraction of the day people spend watching television or writing articles like this.

The **BETA.DIST** function employs the following syntax to operate:

**BETA.DIST(x, alpha, beta, cumulative, \[A\], \[B\])**

The **BETA.DIST** function has the following arguments:

*   **x**: required. This represents the value between **A** and **B** at which to evaluate the function
*   **alpha:** also required. This is a parameter of the distribution
*   **beta:** required. This is also a parameter of the distribution
*   **cumulative:** required. This is a logical value that determines the form of the function. If **cumulative** is TRUE, **BETA.DIST** returns the cumulative distribution function; if it is FALSE, it returns the probability density function
*   **A:** this is optional. This is a lower bound to the interval of **x**
*   **B:** this is also optional. This is an upper bound to the interval of **x**.

It should be further noted that:

*   if any argument is nonnumeric, **BETA.DIST** returns the _#VALUE!_ error value
*   if **alpha** ≤ 0 or **beta** ≤ 0, **BETA.DIST** returns the _#NUM!_ error value
*   if **x** < **A**, **x** > **B**, or **A** = **B**, **BETA.DIST** returns the _#NUM!_ error value
*   if you omit values for **A** and **B**, **BETA.DIST** uses the standard cumulative beta distribution, so that **A** = 0 and **B** = 1
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

As an example:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-beta-dist/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-beta-dist/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-beta-dist/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-beta-dist/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-beta-dist/#0 "close")

top