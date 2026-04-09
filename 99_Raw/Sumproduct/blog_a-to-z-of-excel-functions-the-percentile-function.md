# A to Z of Excel Functions: The PERCENTILE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentile-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The PERCENTILE Function

*   July 16, 2023

A to Z of Excel Functions: The PERCENTILE Function
==================================================

A to Z of Excel Functions: The PERCENTILE Function
==================================================

17 July 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **PERCENTILE** function._

**The PERCENTILE function**

![](https://sumproduct.com/wp-content/uploads/2025/05/8bf8a0b5c2716dc0c9f659e1209c3a59.jpg)

The **n**th percentile of a dataset is the value that cuts off the first **n**% of the data values when all of the values are sorted from least to greatest. For example, the 90th percentile of a dataset is the value that segregates the bottom 90% of the data values from the top 10% of data values.

There are three distinct functions you can use to calculate percentiles in Excel:

1.  **PERCENTILE.EXC:** this function returns the **k**th percentile of a dataset, excluding the values zero \[0\] and one \[1\]
2.  **PERCENTILE.INC:** this function returns the **k**th percentile of a dataset, including the values zero \[0\] and one \[1\]
3.  **PERCENTILE:** this function returns the **k**th percentile of a dataset as well. It will return the same value as the **PERCENTILE.INC** function.

In almost all cases, it is probably best to use the **PERCENTILE.INC** function because this function includes the values zero \[0\] and one \[1\] when calculating the percentiles and is the function that effectively “replaces” **PERCENTILE**.

No matter which of the three functions you use to calculate percentiles, the difference between the values calculated by **PERCENTILE.EXC** and **PERCENTILE.INC** will be similar in most cases. In some instances, it’s even possible that the two functions will return precisely the same values depending upon the numbers analysed.

The **PERCENTILE** function is a statistical function that calculates the value at a given percentile in a dataset. It considers the range between zero \[0\] and one\[1\] including the extreme values. This function is particularly useful when analysing data distributions and understanding the relative position of a specific value within a dataset. For example, you can decide to examine candidates who score above the 90th percentile.

The **PERCENTILE** function has the following syntax:

**\=PERCENTILE(array,  
k)**

It contains two arguments:

*   **array** which is required and represents the array of values or range of data that defines relative standing
*   **k** which is also required is a value 0 ≤ **k** ≤ 1 (0..1 inclusive), which represents the percentile (or **k**th percentage).

It should be noted that:

*   this function has been replaced with one or more new functions that may provide improved accuracy and whose names better reflect their usage. Although this function is still available for backward compatibility, you should consider using the new functions from now on, because this function may not be available in future versions of Excel
*   if **array** is empty, **PERCENTILE** returns the _#NUM!_ error value
*   if **k** is nonnumeric, **PERCENTILE** returns the _#VALUE!_ error value
*   if **k** is < 0 or if **k** > 1, **PERCENTILE** returns the _#NUM!_ error value
*   if **k** is not a multiple of **1/(n + 1)** (where **n** is the number of values in the **array**), **PERCENTILE** interpolates to determine the value at the **k**th percentile
*   **PERCENTILE** will interpolate when the value for the specified percentile lies between two \[2\] values in the array. If it cannot interpolate for the percentile, **k** specified, Excel will return _#NUM!_error
*   the **array** argument ignores text, logic, date and time values.

Please see my examples below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found here._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentile-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentile-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentile-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentile-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-percentile-function/#0 "close")

top