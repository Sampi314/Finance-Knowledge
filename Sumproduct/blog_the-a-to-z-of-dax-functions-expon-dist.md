# The A to Z of DAX Functions – EXPON.DIST

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-expon-dist/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EXPON.DIST

*   October 17, 2023

The A to Z of DAX Functions – EXPON.DIST
========================================

Power Pivot Principles: The A to Z of DAX Functions – EXPON.DIST
================================================================

17 October 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EXPON.DIST**._

**_The_** _**EXPON.DIST**_ **_function_**

In probability theory and statistics, the exponential distribution (also known as negative exponential distribution) is the probability distribution that describes the time between events in a Poisson point process. That’s good if you know what that is! This is a process in which events occur continuously and independently at a constant average rate. It is a particular case of the probability distribution known as the gamma distribution. It is also the continuous analogue of the geometric distribution, and it has the key property of being memoryless. In addition to being used for the analysis of Poisson point processes, it is also found in various other contexts.

It should be noted that the exponential distribution is not the same as the class of exponential families of distributions, which is a large class of probability distributions that includes the exponential distribution as one of its members, but also includes the normal distribution, binomial distribution, gamma distribution, Poisson and many others.

![](https://sumproduct.com/wp-content/uploads/2025/06/b459fcd02fb7a9fb713ca5be675af2da.jpg)

The **EXPON.DIST** functionis one of the statistical functions where it returns the exponential distribution. It has the following syntax:

**EXPON.DIST(x, lambda, cumulative)**

It has three \[3\] parameters:

*   **x**: this is required and, it represents the value of the function
*   **lambda**: this is required and, it represents the parameter value
*   **cumulative**: this is also required and, it represents a logical value that indicates which form of the exponential function to provide. If cumulative is TRUE, **EXPON.DIST** returns the cumulative distribution function; if FALSE, it returns the probability density function.

It has the following remarks:

*   if **x** or **lambda** is nonnumeric, **EXPON.DIST** returns an error message
*   if **x** or **lambda** is not an integer, it is rounded
*   if **x** < 0, **EXPON.DIST** returns an error message
*   if **lambda** ≤ **0, EXPON.DIST** returns an error message
*   the equation for the probability density function is:

![](<Base64-Image-Removed>)

*   the equation for the cumulative distribution function is:

![](<Base64-Image-Removed>)

*   This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s consider the following example where we have a **Data** table with a **Variables** column:

![](<Base64-Image-Removed>)

We can write the following DAX code to calculate the probability density function here:

![](<Base64-Image-Removed>)

Similarly, we changed the last argument of **EXPON.DIST** function into TRUE for cumulative distribution function:

![](<Base64-Image-Removed>)

After this we will put the measure on the PivotTable to view the result with **Variables** as a Rows field and the two measures as Values fields:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-expon-dist/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-expon-dist/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-expon-dist/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-expon-dist/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-expon-dist/#0 "close")

top