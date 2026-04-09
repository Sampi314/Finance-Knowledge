# A to Z of Excel Functions: The COVAR Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-covar-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The COVAR Function

*   February 8, 2018

A to Z of Excel Functions: The COVAR Function
=============================================

A to Z of Excel Functions: The COVAR Function
=============================================

9 February 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **COVAR** function._

**The COVAR function**

So what’s the **COVAR** story here? Well, this is all about the measure of the linear relationship between random variables. In probability theory and statistics, _covariance_ is a measure of the joint variability of two random variables. If the greater values of one variable mainly correspond with the greater values of the other variable, and the same holds for the lesser values, _i.e._ the variables tend to show similar behaviour, the covariance is positive. In the opposite case, when the greater values of one variable mainly correspond to the lesser values of the other, _i.e._ the variables tend to show opposite behaviour, the covariance is negative.

![](<Base64-Image-Removed>)

The sign of the covariance therefore shows the tendency in the linear relationship between the variables. The magnitude of the covariance is not easy to interpret because it is not normalised and hence depends on the magnitudes of the variables. The normalised version of the covariance, known as the _correlation coefficient_, however, shows by its magnitude the strength of the linear relationship.

This function returns covariance, the average of the products of deviations for each data point pair in two data sets. It is used to determine the relationship between two data sets. For example, you can examine whether greater income accompanies greater levels of education.

The **COVAR** function employs the following syntax to operate:

**COVAR(array1, array2)**

The **COVAR** function has the following arguments:

*   **array1:** this is required and represents the first cell range of integers
*   **array2:** this is also required. This is the second cell range of integers.

It should be further noted that:

*   this function has been replaced with two newer functions (**COVARIANCE.P** and **COVARIANCE.S**) that may provide improved accuracy and whose names better reflect their usage. Although this function is still available for backward compatibility, you should consider using the new functions going forward, since this function may not be available in future versions of Excel
*   the arguments must either be numbers or be names, arrays, or references that contain numbers
*   if an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included
*   if **array1** and **array2** have a different number of data points, **COVAR** returns the _#N/A_ error value
*   if either **array1** or **array2** is empty, **COVAR** returns the _#DIV/0!_ error value
*   the covariance is given by the formula:

![](<Base64-Image-Removed>)

where

![](<Base64-Image-Removed>)

are the sample means **AVERAGE(array1)** and **AVERAGE(array2)**, and **n** is the sample size.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-covar-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-covar-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-covar-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-covar-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-covar-function/#0 "close")

top