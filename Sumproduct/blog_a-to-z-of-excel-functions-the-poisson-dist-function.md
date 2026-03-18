# A to Z of Excel Functions: The POISSON.DIST Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-dist-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The POISSON.DIST Function

*   November 12, 2023

A to Z of Excel Functions: The POISSON.DIST Function
====================================================

A to Z of Excel Functions: The POISSON.DIST Function
====================================================

13 November 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **POISSON.DIST** function._

**The POISSON.DIST function**

![](<Base64-Image-Removed>)

Named after the French mathematician Siméon Denis Poisson, the Poisson distribution is the discrete probability distribution of the number of events occurring in a given time period, given the average number of times the event occurs over that time period. It is used when the variable of interest is a discrete count variable.

For example, a supermarket may have 50 customers per hour on average, with peak numbers occurring at lunchtime (say, there are 100 or more) and at other times the number may dwindle to practically zero \[0\]. This distribution can helps calculate the probabilities of busy and quiet times, which can help the manager plan stocking, staffing and scheduling, _etc._

One of the most famous historical, practical uses of the Poisson distribution was estimating the annual number of Prussian cavalry soldiers killed due to horse-kicks! The Poisson distribution also has applications in timetabling, biology (especially mutation detection), finance, disaster readiness, and many other situations where events are time-independent.

The formula for the Poisson probability mass function is

![](<Base64-Image-Removed>)

where:

*   **λ** is the shape parameter which indicates the average number of events in the given time interval
*   is the number of events in the given time.

Here are some examples of plots for different **λ** values:

![](<Base64-Image-Removed>)

The formula for the Poisson cumulative probability function is

![](<Base64-Image-Removed>)

The following is the plot of the Poisson cumulative distribution function with the same values of **λ** as above:

![](<Base64-Image-Removed>)

Excel has a function to return this distribution: **POISSON.DIST**. Its syntax is:

**POISSON.DIST(x, mean, cumulative)**

**POISSON.DIST** has the following arguments:

*   **x:** this is required and represents the number of events
*   **mean:** also required, this is the expected numerical value
*   **cumulative:** this too is required. This is a logical value that determines the form of the probability distribution returned. If cumulative is TRUE, **POISSON.DIST** returns the cumulative Poisson probability that the number of random events occurring will be between zero \[0\] and **x** inclusive; if FALSE, it returns the Poisson probability mass function that the number of events occurring will be exactly **x**.

It should be further noted that:

*   if **x** is not an integer, it is truncated

*   if **x** or **mean** is nonnumeric, **POISSON.DIST** returns the _#VALUE!_ error value

*   if **x** < 0, **POISSON.DIST** returns the _#NUM!_ error value

*   if **mean** < 0, **POISSON.DIST** returns the _#NUM!_ error value.

Please see my examples below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-dist-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-dist-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-dist-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-dist-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-dist-function/#0 "close")

top