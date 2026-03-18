# A to Z of Excel Functions: The MULTINOMIAL Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-multinomial-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The MULTINOMIAL Function

*   September 4, 2022

A to Z of Excel Functions: The MULTINOMIAL Function
===================================================

A to Z of Excel Functions: The MULTINOMIAL Function
===================================================

5 September 2022

The multinomial distribution is a generalisation of the binomial distribution to two or more events.

In probability theory and statistics, the binomial distribution with parameters **n** and **p** is the discrete probability distribution of the number of successes in a sequence of **n** independent success / failure experiments, each of which yields success with probability **p**. For the record, a success / failure experiment is also called a Bernoulli experiment or Bernoulli trial. The binomial distribution is frequently used to model the number of successes in a sample of size **n** drawn with replacement from a population of size **N**.

![](<Base64-Image-Removed>)

This function returns the individual term binomial distribution probability. The **[BINOM.DIST](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-binom-dot-dist-function)
** function should be used in problems with a fixed number of tests or trials, when the outcomes of any trial are only success or failure, when trials are independent and when the probability of success is constant throughout the experiment. For example, **[BINOM.DIST](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-binom-dot-dist-function)
** can calculate the probability that two of the next three babies born are male.

Therefore, for an experiment with the following characteristics:

*   the experiment consists of **n** independent trials
*   each trial has **k** mutually exclusive outcomes **Ei**
*   for each trial the probability of outcome **Ei** is **pi**,

let **x1**, …, **xk** be discrete random variables whose values are the number of times outcome **Ei** occurs in **n** trials. Then, **x1**, …, **xk** has a **_multinomial_** distribution. The (joint) probability distribution function (pdf) is defined as follows:

![](<Base64-Image-Removed>)

where

![](<Base64-Image-Removed>)

The case where k = 2 is equivalent to the binomial distribution.

Key properties of the multinomial distribution are:

*   **E\[xi\]** = **npi**
*   **var(xi)** = **npi(1–pi)**
*   **cov(xi, xj)****\= –npipj** for **i ≠ j**.

The **MULTINOMIAL** function in Excel returns the ratio of the factorial of a sum of values to the product of factorials. It employs the following syntax to operate:

**MULTINOMIAL(number1, \[number2, …\])**

The **MULTINOMIAL** function has the following arguments:

*   **number1, number2, …**: **number1** is required (the rest are optional), and represents one \[1\] to 255 values for which you require the multinomial.

It should be noted that:

*   if any argument is nonnumeric, **MULTINOMIAL** returns the _#VALUE!_ error value
*   if any argument is less than zero, **MULTINOMIAL** returns the _#NUM!_ error value
*   the multinomial is:

![](<Base64-Image-Removed>)

As an example, suppose that a bag contains 12 balls: five \[5\] red, four \[4\] yellow and three \[3\] blue (5 + 4 + 3 = 12). You reach in the bag and pull out a ball at random and then replace before making a subsequent selection. This experiment is repeated a total of 10 times. What is the probability that the outcome will result in exactly six \[6\] reds, two \[2\] yellows and two \[2\] blues (6 + 2 + 2 = 10)?

The possible outcomes for each trial in this experiment are **E1** = a red ball is drawn, **E2** = a yellow ball is drawn and **E3** = a blue ball is drawn. Thus **p1** = 5/12, **p2** = 4/12, **p3** = 3/12, **x1** = 6, **x2** = 2 and **x3** = 2, and so

![](<Base64-Image-Removed>)

This has been reproduced in Excel using the **MULTINOMIAL** function (using three alternative approaches) below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-multinomial-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-multinomial-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-multinomial-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-multinomial-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-multinomial-function/#0 "close")

top