# A to Z of Excel Functions: The STDEVPA Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-stdevpa-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The STDEVPA Function

*   January 12, 2026

A to Z of Excel Functions: The STDEVPA Function
===============================================

_Welcome back to our regular A to Z of Excel Functions blog.  Today we look at the **STDEVPA** function._

**The STDEVPA function**

![](<Base64-Image-Removed>)

A probability distribution is a mathematical function or model that describes the likelihood of different outcomes occurring for a given situation, experiment or process.  It provides a statistical framework for understanding and predicting patterns of randomness.  Probability distributions are fundamental in statistics, data analysis, machine learning, and various scientific disciplines, as they allow researchers and analysts to make informed decisions based upon uncertainty.

A probability distribution is associated with a random variable, which is a variable that can take on different values based on the outcome of a random phenomenon.  Random variables may be classified into two \[2\] types:

1.  **Discrete Random Variables:** these assume specific, countable values, such as the outcomes of rolling a six-sided die (1, 2, 3, 4, 5, or 6)  
      
    
2.  **Continuous Random Variables:** these can take on any value within a given range, such as the height of individuals in a population or temperature measurements.

The distributions associated with these two types of variable are thus classified into similar groupings:

1.  **Discrete Probability Distributions**

*   **Binomial Distribution:** this models the number of successes in a fixed number of independent trials, each with the same probability of success.  For example, it can predict the likelihood of flipping a coin and getting heads a certain number of times  
      
    
*   **Poisson Distribution:** this represents the probability of a given number of events occurring in a fixed interval, provided the events happen independently and at a constant rate.  It is often used for modelling rare events, such as the number of emails received in an hour  
      
    
*   **Continuous Probability Distributions  
      
    **
*   **Exponential Distribution:** this represents the time between events in a Poisson process.  It is commonly used in reliability analysis and queuing theory  
      
    
*   **Uniform Distribution:** this assigns equal probability to all values within a specified range, making it suitable for modelling situations with no bias toward particular outcomes  
      
    
*   **Normal Distribution:** also known as the **Gaussian Distribution**, this is a symmetric bell-shaped curve describing many natural phenomena, such as human heights or test scores.  It is defined by its mean and standard deviation.

Therefore, a Normal distribution is a probability distribution that is symmetrical and bell-shaped.  It is easily recognised since most values cluster around the mean (average), with fewer values further away from the mean. 

The mean (or expected value) of a probability distribution indicates the central tendency or average outcome.  The median, median and mode are the same value and represent the centre point, whilst the left and right sides of the curve are mirror images of each other.  The curve gradually approaches the horizontal axis on both sides, but never actually touches it. 

The variance measures the spread or dispersion of the data around the mean and represents the square of the standard deviation.  Together, these parameters provide crucial insights into the behaviour of the distribution.

The standard deviation is a measure of the spread or dispersion of the data.  A smaller standard deviation means the data is clustered closely around the mean, whilst a larger standard deviation means the data is more spread out. 

The formula for the Normal distribution is given by

![](<Base64-Image-Removed>)

Associated with the Normal distribution is the Empirical Rule (68-95-99.7 Rule), which provides guidelines for understanding the spread of data in a Normal distribution: 

*   approximately **68%** of the data falls within one \[1\] standard deviation of the mean
*   approximately **95%** of the data falls within two \[2\] standard deviations of the mean
*   approximately **99.7%** of the data falls within \[3\] three standard deviations of the mean.

  
The **STDEVPA** estimates the standard deviation based upon the entire population (it includes logical values and text).  It is a measure of how widely values are dispersed from the average value (the mean).  The function employs the following syntax to operate:

> **STDEVPA(number1\[, number2, …\])**

The **STDEVPA** function has the following argument(s):

*   **number1:** this is required and represents the first number argument corresponding to the population
*   **number2:** this is optional.  This denotes number arguments 2 to 255 corresponding to the population
*   you may also use a single array or reference to an array instead of arguments separated by commas.

It should be further noted that:

*   this function replaced one or more older functions and may provide improved accuracy and whose names better reflect their usage  
      
    
*   **STDEVPA** assumes that its arguments represent the entire population.  If your data represents a sample of the population, then compute the standard deviation using **STDEVA** _(although this is now an older function)_  
      
    
*   For larger sample sizes, **STDEVPA** and **STDEVA** return approximately equal values
*   the standard deviation is calculated using the “**n**” method, _i.e._ the number of elements in the sample, **n**, is noted and is also used in the calculation  
      
    
*   arguments can be the following: numbers; names, arrays, vectors or references that contain numbers, text representations of numbers or logical values, such as TRUE and FALSE, in a reference

*   text representations of numbers that you type directly into the list of arguments are counted

*   arguments that contain TRUE evaluate as one \[1\]; arguments that contain text or FALSE evaluate as zero \[0\]

*   if an argument is an array, vector or reference, only values in that array, vector or reference are used.  Empty cells in the array or reference are ignored

*   arguments that are error values or that cannot be translated into numbers cause errors

*   if you do not want to include logical values and text representations of numbers in a reference as part of the calculation, use the **STDEVP** function _(albeit an older function)_
*   **STDEVPA** uses the following formula:

![](<Base64-Image-Removed>)

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://sumproduct.com/thought/a-to-z-of-excel-functions/)
._

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-stdevpa-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-stdevpa-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-stdevpa-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-stdevpa-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-stdevpa-function/#0 "close")

top