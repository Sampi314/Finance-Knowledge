# A to Z of Excel Functions: The SKEW.P Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-skew-p-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The SKEW.P Function

*   August 18, 2025

A to Z of Excel Functions: The SKEW.P Function
==============================================

_Welcome back to our regular A to Z of Excel Functions blog.  Today we look at the **SKEW.P** function._

**The SKEW.P function**

![](<Base64-Image-Removed>)

Imagine you plotted the entire population of outcomes of an event occurring (_i.e._ the likelier the outcome, the greater the frequency / probability).  This could be plotted as a distribution of outcomes.  The **SKEW.P** function returns the skewness of this distribution.  Skewness characterises the degree of asymmetry of a distribution around its mean.  Positive skewness indicates a distribution with an asymmetric tail extending toward more positive values.  Negative skewness indicates a distribution with an asymmetric tail extending toward more negative values.

There are various measures employed to determine the level of skewness.  **Pearson Mode skewness** uses the formula

> **(Mean – Mode) / σ**

where **σ** represents the standard deviation of the distribution.  An alternative version often used is

> **3(Mean – Median) / σ**

which is also referred to as **Pearson’s second coefficient of skewness**.  Which one would you lean to?  _(Sigh – Ed.)_

These calculations assume you know the mean, mode or median, and the standard deviation of your data.  Sometimes you might not have that information.  Instead, you might have information about your quartiles.  In this instance, you can use **Bowley Skewness** as an alternative to find out more about the asymmetry of your distribution. It’s very useful if you have extreme data values (outliers) or if you have an open-ended distribution.  It is calculated as

> **(Q3 + Q1 – 2Q2) / (Q3 – Q1)**

> _or_ **(Q3 + Q1 – 2 x Median) / (Q3 – Q1)**

**Kelly’s Measure of Skewness** is one of several ways to measure skewness in a data distribution.  The last approach is based upon the central 50% of the observations in a data set.  It leaves 25% of the observations in each tail of the distribution.  Kelly suggested that leaving out 50% of data to calculate skewness was too extreme.  He created a measure to find skewness with more data.  Kelly’s measure is based on **P90** (the 90th percentile) and **P10** (the 10th percentile).  Only 20% of observations (10% in each tail) are excluded from the measure.

> **Skewness = P90 + P10 – 2 x P50 = D9 + D1 – 2 x D5**

The technique you use depends upon what you know about your data.  There are more sophisticated approaches, such as the one Microsoft employs.

Excel has the function **SKEW.P** to calculate it.  Its syntax is:

> **SKEW.P(number1, number2, …)**

**SKEW.P** has the following arguments:

*   **number1, number2, …:** the first argument (number1) is required, whereas subsequent numbers are optional.  You may have between one \[1\] and 255 arguments for which you want to calculate the population skewness.  You can also use a single array or a reference to an array instead of arguments separated by commas.

It should be further noted that:

*   arguments may either be numbers or names, arrays or references that contain numbers
*   logical values and text representations of numbers that you type directly into the list of arguments are counted
*   if an array or reference argument contains text, logical values or empty cells, those values are ignored; however, cells with the value zero \[0\] are included
*   arguments that are error values or text that cannot be translated into numbers cause errors
*   if there are fewer than three data points or the sample standard deviation is zero, **SKEW.P** returns the _#DIV/0!_ error value

the equation for skewness is defined as the adjusted Fisher-Pearson standardised moment coefficient:  

![](<Base64-Image-Removed>)

*   Here, ![](<Base64-Image-Removed>) represents the number of data points in the sample, ![](<Base64-Image-Removed>) represents the **i**th data point**,** ![](<Base64-Image-Removed>) represents the mean and ![](<Base64-Image-Removed>) denotes the standard deviation of the sample.  It is difficult to find this formula; It generally doesn’t even appear in elementary statistics textbooks.  However, the results of the calculation are important and tell you:
    *   the direction of the skew (positive or negative)
    *   how the sample compares with a normal (symmetric) distribution.  The further the skew result is from zero, the greater the skew.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every other business day._

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-skew-p-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-skew-p-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-skew-p-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-skew-p-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-skew-p-function/#0 "close")

top