# A to Z of Excel Functions: The BINOM.DIST Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-dist-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The BINOM.DIST Function

*   January 8, 2017

A to Z of Excel Functions: The BINOM.DIST Function
==================================================

A to Z of Excel Functions: The BINOM.DIST Function
==================================================

9 January 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **BINOM.DIST** function._

**The BINOM.DIST function**

In probability theory and statistics, the binomial distribution with parameters **n** and **p** is the discrete probability distribution of the number of successes in a sequence of **n** independent success / failure experiments, each of which yields success with probability **p**. For the record, a success / failure experiment is also called a Bernoulli experiment or Bernoulli trial. The binomial distribution is frequently used to model the number of successes in a sample of size **n** drawn with replacement from a population of size **N**.

This function returns the individual term binomial distribution probability. The **BINOM.DIST** function should be used in problems with a fixed number of tests or trials, when the outcomes of any trial are only success or failure, when trials are independent and when the probability of success is constant throughout the experiment. For example, **BINOM.DIST** can calculate the probability that two of the next three babies born are male.

The **BINOM.DIST** function employs the following syntax to operate:

**BINOM.DIST(number\_s, trials, probability\_s, cumulative)**

The **BINOM.DIST** function has the following arguments:

*   **number\_s:** this is required and represents the number of successes in trials
*   **trials:** this is also required. This is the number of independent trials
*   **probability\_s:** again, required. This is the probability of success on each trial
*   **cumulative:** also required. This is a logical value that determines the form of the function. If **cumulative** is **TRUE**, then **BINOM.DIST** returns the cumulative distribution function, which is the probability that there are at most **number\_s** successes; if **cumulative** is **FALSE**, it returns the probability mass function, which is the probability that there are **number\_s** successes.

It should be further noted that:

*   **number\_s** and **trials** are truncated to integers
*   if **number\_s**, **trials**, or **probability\_s** is / are non-numeric, **BINOM.DIST** returns the _#VALUE!_ error value
*   if **number\_s** < 0 or **number\_s** > **trials**, **BINOM.DIST** returns the _#NUM!_ error value
*   if **probability\_s** < 0 or **probability\_s** > 1, **BINOM.DIST** returns the _#NUM!_ error value.

The binomial probability mass function is:

![](https://sumproduct.com/wp-content/uploads/2025/05/046be421bd75ee7eee1403046fc8732a.jpg)

where:

![](https://sumproduct.com/wp-content/uploads/2025/05/0fdf5ec5e7ea027e3d5adb6914eb8e59.jpg)

which is **COMBIN(n, x)**.

The cumulative binomial distribution is:

![](https://sumproduct.com/wp-content/uploads/2025/05/33b6a421e1a94cfcfc133dbdbe463a9f.jpg)

Essentially, **BINOM.DIST** replaces **BINOMDIST.** First introduced in Excel 2010, this provides more compatibility with other statistical software. The former function is still recognised in Excel though for legacy reasons.

All clear as mud? Please see my example below:

![](<Base64-Image-Removed>)

Essentially, **BINOM.DIST** replaces **BINOMDIST.** First introduced in Excel 2010, this provides more compatibility with other statistical software. The former function is still recognised in Excel though for legacy reasons.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-dist-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-dist-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-dist-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-dist-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-dist-function/#0 "close")

top