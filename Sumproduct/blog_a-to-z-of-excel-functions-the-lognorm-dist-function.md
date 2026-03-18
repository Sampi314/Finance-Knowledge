# A to Z of Excel Functions: The LOGNORM.DIST Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-lognorm-dist-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The LOGNORM.DIST Function

*   November 7, 2021

A to Z of Excel Functions: The LOGNORM.DIST Function
====================================================

A to Z of Excel Functions: The LOGNORM.DIST Function
====================================================

8 November 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **LOGNORM.DIST** function._

**The LOGNORM.DIST function**

A Lognormal distribution is a statistical distribution of logarithmic values from an underlying Normal distribution. A Lognormal distribution may be translated to a Normal distribution and vice versa using the associated logarithmic translations.

A Normal distribution is a symmetrical probability distribution of outcomes that forms a bell curve. In a Normal distribution, 68% of the results fall within one standard deviation and 95% fall within two standard deviations, _viz_.

![](<Base64-Image-Removed>)

While most people are familiar with a Normal distribution, they may not be as familiar with the related Lognormal distribution. A Normal distribution may be converted to a Lognormal distribution using logarithms. It should be noted that Lognormal distributions can only arise from a Normally distributed set of random variables.

There can be a few reasons for using Lognormal distributions in conjunction with Normal distributions. Most commonly, Lognormal distributions are the result of taking the natural logarithm where the base is equal to **e**\=2.718… However, the Lognormal distribution may be scaled using a different base, if desired, which affects the shape of the Lognormal distribution.

The Lognormal distribution plots the logarithm of random variables from a Normal distribution curve. In general, the logarithm is known as the exponent to which a base number must be raised in order to produce the random variable (**x**) that is found along a Normally distributed curve. It should be noted that Lognormal distributions are positively skewed with long right tails due to low mean values and high variances in the random variables.

Clear as mud, yes?

In practice, Normal distributions may present a few problems that Lognormal distributions can solve. In particular, Normal distributions allow for negative random variables whilst Lognormal distributions include all positive variables.

Probably _(get it?)_ the most common application where Lognormal distributions are used in finance is in the analysis of stock prices. A Lognormal distribution is more suitable for this purpose because asset prices cannot be negative. An important point to note is that when the continuously compounded returns of a stock follow a Normal distribution, then the stock prices follow a Lognormal distribution. The Lognormal distribution curve may therefore be used to help better identify the compound return that the stock can expect to achieve over a period of time.

The distribution is occasionally referred to as the Galton distribution or Galton’s distribution, after Francis Galton. In summary, a Lognormal process is “simply” the statistical realisation of the multiplicative product of many independent random variables, each of which is positive and it is therefore the maximum entropy probability distribution for a random variate **x** for which the mean and variance of **LN(x)** are specified. And if you follow all of that, get out of here because no one likes a smartarse.

The **LOGNORM.DIST** function returns the Lognormal distribution of **x**, where **LN(x)** is Normally distributed with parameters **mean** and **standard\_deviation**. The **LOGNORM.DIST** function employs the following syntax to operate:

**LOGNORM.DIST(x, mean, standard\_deviation, cumulative)**

The **LOGNORM.DIST** function has the following arguments:

*   **x:** this is required and represents the value at which to evaluate the function
*   **mean:** this is also required and denotes the mean of the natural logarithm of **x**, **LN(x)**
*   **standard\_deviation:** again required, this is the standard deviation of **LN(x)**
*   **cumulative:** yet again, this final argument is required. This is a logical value that determines the form of the function. If **cumulative** is TRUE, **LOGNORM.DIST** returns the cumulative distribution function; if FALSE, it returns the probability density function.

It should be noted that:

*   if any argument is nonnumeric, **LOGNORM.DIST** returns the _#VALUE!_ error value
*   if **x** ? 0 or if **standard\_deviation** ? 0, **LOGNORM.DIST** returns the _#NUM!_ error value
*   the equation for the lognormal cumulative distribution function is:

![](<Base64-Image-Removed>)

Please see my comprehensive example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

A full page of the function articles can be found _[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-lognorm-dist-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-lognorm-dist-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-lognorm-dist-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-lognorm-dist-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-lognorm-dist-function/#0 "close")

top