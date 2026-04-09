# A to Z of Excel Functions: The BINOM.INV Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-inv-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The BINOM.INV Function

*   February 5, 2017

A to Z of Excel Functions: The BINOM.INV Function
=================================================

A to Z of Excel Functions: The BINOM.INV Function
=================================================

6 February 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **BINOM.INV** function._

**The BINOM.INV function**

In probability theory and statistics, the binomial distribution with parameters **n** and **p** is the discrete probability distribution of the number of successes in a sequence of **n** independent success / failure experiments, each of which yields success with probability **p**. For the record, a success / failure experiment is also called a Bernoulli experiment or Bernoulli trial. The binomial distribution is frequently used to model the number of successes in a sample of size **n** drawn with replacement from a population of size **N**.

![](<Base64-Image-Removed>)

Bored of these functions yet? This function returns the smallest value for which the cumulative binomial distribution which is greater than or equal to a criterion value. This might sound like gobbledygook but it is useful for creating independent simulations analysis in Excel (please see [Simulation Stimulation](https://www.sumproduct.com/thought/simulation-stimulation)
 for more information).

The **BINOM.INV** function employs the following syntax to operate:

**BINOM.INV(trials, probability\_s, alpha)**

The **BINOM.INV** function has the following arguments:

*   **trials:** this is required and represents the number of Bernoulli trials
*   **probability\_s:** this is also required. This is the probability of a success on each trial
*   **alpha:** again, required. This represents the aforementioned criterion value.

It should be further noted that:

*   if any argument is nonnumeric, **BINOM.INV** returns the _#VALUE!_ error value
*   If **trials** is not an integer, it is truncated
*   If **trials** < 0, **BINOM.INV** returns the _#NUM!_ error value
*   If **probability\_s** is < 0 or **probability\_s** > 1, **BINOM.INV** returns the _#NUM!_ error value
*   If **alpha** < 0 or **alpha** \> 1, **BINOM.INV** returns the _#NUM!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-inv-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-inv-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-inv-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-inv-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-binom-inv-function/#0 "close")

top