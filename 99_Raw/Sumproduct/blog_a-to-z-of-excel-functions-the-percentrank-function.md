# A to Z of Excel Functions: The PERCENTRANK Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentrank-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The PERCENTRANK Function

*   August 13, 2023

A to Z of Excel Functions: The PERCENTRANK Function
===================================================

A to Z of Excel Functions: The PERCENTRANK Function
===================================================

14 August 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **PERCENTRANK** function._

**The PERCENTRANK function**

The Excel **PERCENTRANK** function calculates the relative position, between zero \[0\] and one \[1\], including the extreme values, of a specified value within a supplied array. It calculates the percentage rank of a value in an ordered dataset, _i.e._ it is the percentage of values in the dataset that are less than or equal to itself.

The syntax of the **PERCENTRANK** function is as follows:

**\=PERCENTRANK(array,  
x, \[significance\])**

It contains three arguments:

*   **array:** this is required and represents the **array** of values within which you want to find the relative position of a specific value (_i.e._ the **array** or range of numerical values that defines relative standing)
*   **x:** also required, this is the value that you want to calculate the relative position of (**x** must be within the range of the values in the supplied **array**, but it does not need to be exactly equal to one of the values: if **x** is not found in the **array**, the **array** values are interpolated to calculate the percentage rank)
*   **significance:** this is an optional argument that specifies the number of significant digits that the returned percentage value is rounded to (by default, this is rounded to three \[3\] decimal places).

This function is particularly useful when you want to determine the percentile rank of a value, excluding the highest and lowest values in the dataset.

It should be noted that:

*   if **array** is empty, **PERCENTRANK** returns the _#NUM!_ error value
*   if **significance** < 1, **PERCENTRANK** returns the _#NUM!_ error value
*   if **x** does not match one of the values in array, **PERCENTRANK** interpolates to return the correct percentage rank
*   This function has been replaced with one or more new functions that may provide improved accuracy and whose names better reflect their usage. Although this function is still available for backward compatibility, you should consider using the new functions from now on, because this function may not be available in future versions of Excel
*   It works similarly to **PERCENTRANK.INC**.

Please see my examples below:

![](https://sumproduct.com/wp-content/uploads/2025/05/1121bfac987f588dd8a23100bb341db5.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentrank-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentrank-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentrank-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentrank-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentrank-function/#0 "close")

top