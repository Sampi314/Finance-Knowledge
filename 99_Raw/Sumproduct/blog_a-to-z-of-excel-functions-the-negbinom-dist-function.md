# A to Z of Excel Functions: The NEGBINOM.DIST Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinom-dist-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The NEGBINOM.DIST Function

*   October 16, 2022

A to Z of Excel Functions: The NEGBINOM.DIST Function
=====================================================

A to Z of Excel Functions: The NEGBINOM.DIST Function
=====================================================

17 October 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **NEG****BINOM.DIST** function._

**The NEGBINOM.DIST function**

In probability theory and statistics, the negative binomial distribution is a discrete probability distribution that models the number of successes in a sequence of **n** independent success / failure experiments, each of which yields success with probability **p,** before a specified number of failures (denoted **r**) occur. For the record, a success / failure experiment is also called a Bernoulli experiment or Bernoulli trial.

This function returns the negative binomial distribution, the probability that there will be a **number\_f** failures before the **number\_s**\-th success, with **probability\_s** probability of a success. The **NEG****BINOM.DIST** function should be used in problems with a fixed number of successes, when the outcomes of any trial are only success or failure, when trials are independent and when the probability of success is constant throughout the experiment. For example, **NEG****BINOM.DIST** can calculate the probability that two babies born are male before one female baby is born.

The **NEG****BINOM.DIST** function employs the following syntax to operate:

**NEGBINOM.DIST(number\_f,  
number\_s, probability\_s, cumulative)**

The **NEG****BINOM.DIST** function has the following arguments:

*   **number\_f:** this is required and represents the number of failures in trials
*   **number\_s:** this is also required. This is the threshold number of successes
*   **probability\_s:** again, this is required. This is the probability of success in each trial
*   **cumulative:** the final argument is also required. This is a logical value that determines the form of the function. If **cumulative** is TRUE, then **NEG****BINOM.DIST** returns the cumulative distribution function, which is the probability that there are at most **number\_f** failures; if **cumulative** is **FALSE**, it returns the probability density function, which is the probability that there are **number\_f** failures.

It should be further noted that:

*   **number\_f** and **number\_s** are truncated to integers
*   if **number\_f**, **number\_s**, or **probability\_s** is / are non-numeric, **NEGBINOM.DIST** returns the _#VALUE!_ error value
*   if **number\_f** < 0 or **number\_s** < 1, **NEGBINOM.DIST** returns the _#NUM!_ error value
*   if **probability\_s** < 0 or **probability\_s** > 1, **NEGBINOM.DIST** returns the _#NUM!_ error value
*   the equation for the negative binomial distribution is:

![](https://sumproduct.com/wp-content/uploads/2025/05/image2-1662336693.gif)

where:

**x** is **number\_f**, **r** is **number\_s** and **p** is **probability\_s**.

Have I lost you yet? Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/096e21ac25c8e367486649b3fa8d2fb3.jpg)

Essentially, **NEG****BINOM.DIST** replaces **NEG****BINOMDIST.** First introduced in Excel 2010, this provides more compatibility with other statistical software. The former function is still recognised in Excel though for legacy reasons.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found_ _[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinom-dist-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinom-dist-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinom-dist-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinom-dist-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinom-dist-function/#0 "close")

top