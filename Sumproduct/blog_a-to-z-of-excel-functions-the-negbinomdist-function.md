# A to Z of Excel Functions: The NEGBINOMDIST Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinomdist-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The NEGBINOMDIST Function

*   October 23, 2022

A to Z of Excel Functions: The NEGBINOMDIST Function
====================================================

A to Z of Excel Functions: The NEGBINOMDIST Function
====================================================

24 October 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **NEG****BINOMDIST** function._

**The NEGBINOMDIST function**

In probability theory and statistics, the negative binomial distribution is a discrete probability distribution that models the number of successes in a sequence of **n** independent success / failure experiments, each of which yields success with probability **p,** before a specified number of failures (denoted **r**) occur. For the record, a success / failure experiment is also called a Bernoulli experiment or Bernoulli trial.

![](<Base64-Image-Removed>)

You’re probably seeing the similarities between this article and [the last one](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-negbinom-dist-function)
. This function also returns the negative binomial distribution, the probability that there will be a **number\_f** failures before the **number\_s**\-th success, with **probability\_s** probability of a success. The **NEG****BINOMDIST** function should be used in problems with a fixed number of successes, when the outcomes of any trial are only success or failure, when trials are independent and when the probability of success is constant throughout the experiment. For example, **NEG****BINOMDIST** can calculate the probability that exactly two babies born are male before one female baby is born.

The **NEG****BINOMDIST** function employs the following syntax to operate:

**NEGBINOMDIST(number\_f,  
number\_s, probability\_s)**

The **NEG****BINOMDIST** function has the following arguments:

*   **number\_f:** this is required and represents the number of failures in trials
*   **number\_s:** this is also required. This is the threshold number of successes
*   **probability\_s:** again, this is required. This is the probability of success on each trial.

Unlike **[NEGBINOM.DIST](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-negbinom-dist-function)
**, this function does not have the **cumulative** argument.

It should be further noted that:

*   **number\_f** and **number\_s** are truncated to integers
*   if **number\_f**, **number\_s**, or **probability\_s** is / are non-numeric, **NEGBINOMDIST** returns the _#VALUE!_ error value
*   if **number\_f** < 0 or **number\_s** < 1, **NEGBINOMDIST** returns the _#NUM!_ error value
*   if **probability\_s** < 0 or **probability\_s** > 1, **NEGBINOMDIST** returns the _#NUM!_ error value
*   the equation for the negative binomial distribution is:

![](<Base64-Image-Removed>)

where:

**x** is **number\_f**, **r** is **number\_s** and **p** is **probability\_s**.

Please see my example below:

![](<Base64-Image-Removed>)

Essentially, **NEG****BINOMDIST** is a slightly less flexible version of **NEGBINOM.DIST** and represents the version of the function used before its successor was introduced in Excel 2010. It is still recognised in Excel for legacy reasons. Although this function is still available for backward compatibility, you should consider using the new functions from now on, because this function may not be available in future versions of Excel.

_  
We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found_ _[here](https://www.sumproduct.com/cp/collections/entries/a-to-z-of-excel-functions/%7B%7B%20link:8fe87041-c478-4bfa-a08d-b501f4a05486%20%7D%7D)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinomdist-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinomdist-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinomdist-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinomdist-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-negbinomdist-function/#0 "close")

top