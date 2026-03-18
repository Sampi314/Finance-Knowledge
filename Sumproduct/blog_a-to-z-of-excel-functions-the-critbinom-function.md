# A to Z of Excel Functions: The CRITBINOM Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-critbinom-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CRITBINOM Function

*   February 18, 2018

A to Z of Excel Functions: The CRITBINOM Function
=================================================

A to Z of Excel Functions: The CRITBINOM Function
=================================================

19 February 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CRITBINOM** function._

**The CRITBINOM function**

In probability theory and statistics, the binomial distribution with parameters **n** and **p** is the discrete probability distribution of the number of successes in a sequence of **n** independent success / failure experiments, each of which yields success with probability **p**. For the record, a success / failure experiment is also called a Bernoulli experiment or Bernoulli trial. The binomial distribution is frequently used to model the number of successes in a sample of size **n** drawn with replacement from a population of size **N**.

![](<Base64-Image-Removed>)

This function returns the smallest value for which the cumulative binomial distribution which is greater than or equal to a criterion value. This might sound like gobbledygook, but it is useful for creating independent simulations analysis in Excel (please see [Simulation Stimulation](https://www.sumproduct.com/thought/simulation-stimulation)
 for more information).

For example, the chart _(below)_ shows the cumulative Binomial Distribution function for 100 tosses of a coin. This curve represents the probability that at most **x** heads will be thrown from the 100 tosses:

![](<Base64-Image-Removed>)

The Excel **CRITBINOM** function calculates the inverse of the curve on the right, _i.e._ the **CRITBINOM** function calculates the minimum value of **x** for which the cumulative Binomial Distribution function is a specified value.

The **CRITBINOM** function employs the following syntax to operate:

**CRITBINOM(trials, probability\_s, alpha)**

The **CRITBINOM** function has the following arguments:

*   **trials:** this is required and represents the number of Bernoulli trials
*   **probability\_s:** this is also required. This is the probability of a success on each trial
*   **alpha:** again, required. This represents the aforementioned criterion value.

It should be further noted that:

*   this function has been replaced with a newer function (**[BINOM.INV](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-binom-dot-inv-function)
    **) that may provide improved accuracy and whose name better reflects its usage. Although this function is still available for backward compatibility, you should consider using the new functions going forward, since this function may not be available in future versions of Excel
*   if any argument is nonnumeric, **CRITBINOM** returns the _#VALUE!_ error value
*   if **trials** is not an integer, it is truncated
*   if **trials** < 0, **CRITBINOM** returns the _#NUM!_ error value
*   if **probability\_s** is < 0 or **probability\_s** > 1, **CRITBINOM** returns the _#NUM!_ error value
*   if **alpha** < 0 or **alpha** \> 1, **CRITBINOM** returns the _#NUM!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-critbinom-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-critbinom-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-critbinom-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-critbinom-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-critbinom-function/#0 "close")

top