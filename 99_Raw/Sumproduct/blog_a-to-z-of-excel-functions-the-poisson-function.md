# A to Z of Excel Functions: The POISSON Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The POISSON Function

*   November 5, 2023

A to Z of Excel Functions: The POISSON Function
===============================================

A to Z of Excel Functions: The POISSON Function
===============================================

6 November 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **POISSON** function._

**The POISSON function**

![](https://sumproduct.com/wp-content/uploads/2025/05/ee481df908db53f53cc3b1b4d9ebb411.jpg)

Named after the French mathematician Siméon Denis Poisson, the Poisson distribution is the discrete probability distribution of the number of events occurring in a given time period, given the average number of times the event occurs over that time period. It is used when the variable of interest is a discrete count variable.

For example, a supermarket may have 50 customers per hour on average, with peak numbers occurring at lunchtime (say, there are 100 or more) and at other times the number may dwindle to practically zero \[0\]. This distribution can helps calculate the probabilities of busy and quiet times, which can help the manager plan stocking, staffing and scheduling, _etc._

One of the most famous historical, practical uses of the Poisson distribution was estimating the annual number of Prussian cavalry soldiers killed due to horse-kicks! The Poisson distribution also has applications in timetabling, biology (especially mutation detection), finance, disaster readiness, and many other situations where events are time-independent.

The formula for the Poisson probability mass function is

![](https://sumproduct.com/wp-content/uploads/2025/05/0875253bc1829aad74771b361d5f1f8e.jpg)

where:

*   **λ** is the shape parameter which indicates the average number of events in the given time interval
*   is the number of events in the given time.

Here are some examples of plots for different **λ** values:

![](https://sumproduct.com/wp-content/uploads/2025/05/7832dabc594b0260b5652ad5ddfd0b3c.jpg)

The formula for the Poisson cumulative probability function is

![](https://sumproduct.com/wp-content/uploads/2025/05/90622dcb99c422184bbbecda4bc257e5.jpg)

The following is the plot of the Poisson cumulative distribution function with the same values of **λ** as above:

![](https://sumproduct.com/wp-content/uploads/2025/05/063bf74ea19c4bb6c61efe3e41792041.jpg)

Excel has a function to return this distribution: **POISSON**. Its syntax is:

**POISSON(x, mean, cumulative)**

**POISSON** has the following arguments:

*   **x:** this is required and represents the number of events
*   **mean:** also required, this is the expected numerical value
*   **cumulative:** this too is required. This is a logical value that determines the form of the probability distribution returned. If cumulative is TRUE, **POISSON** returns the cumulative Poisson probability that the number of random events occurring will be between zero \[0\] and **x** inclusive; if FALSE, it returns the Poisson probability mass function that the number of events occurring will be exactly **x**.

It should be further noted that:

*   if **x** is not an integer, it is truncated
*   if **x** or **mean** is nonnumeric, **POISSON** returns the _#VALUE!_ error value
*   if **x** < 0, **POISSON** returns the _#NUM!_ error value
*   if **mean** < 0, **POISSON** returns the _#NUM!_ error value
*   this function has been replaced with one or more new functions that may provide improved accuracy and whose names better reflect their usage. Although this function is still available for backward compatibility, you should consider using the new functions from now on, because this function may not be available in future versions of Excel.

Please see my examples below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-poisson-function/#0 "close")

top