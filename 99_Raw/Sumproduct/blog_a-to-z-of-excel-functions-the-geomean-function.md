# A to Z of Excel Functions: The GEOMEAN Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-geomean-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The GEOMEAN Function

*   February 12, 2020

A to Z of Excel Functions: The GEOMEAN Function
===============================================

A to Z of Excel Functions: The GEOMEAN Function
===============================================

13 February 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **GEOMEAN** function._

**The GEOMEAN function**

In mathematics, the geometric mean is a mean or average, which indicates the central tendency or typical value of a set of numbers by using the product of their values (as opposed to the arithmetic mean which uses their sum). The geometric mean is defined as the **n**th root of the product of **n** numbers, _i.e._ for a set of numbers **x1**, **x2**, …, **xn**, the geometric mean is defined as

![](<Base64-Image-Removed>)

In two dimensions, it is the equivalent of finding the equivalent square with the same area as the rectangle given by the two dimensions cited:

![](<Base64-Image-Removed>)

In three dimensions, it is the equivalent of finding the equivalent cube with the same volume as the given hexahedron with the three dimensions cited:

![](<Base64-Image-Removed>)

The idea continues in **n** dimensions.

The Excel function **GEOMEAN** returns the geometric mean of an array or range of positive data. For example, you can use **GEOMEAN** to calculate average growth rate given compound interest with variable rates. It has the following syntax:

**GEOMEAN(number1, \[number2\], …)**

The **GEOMEAN** function has the following arguments:

*   **number1**, **number2**, … where **number1** is required, and subsequent numbers are optional. There can be between one (1) and 255 numbers. You can also use a single array or a reference to an array instead of arguments separated by commas.

It should be further noted that:

*   arguments can either be numbers or names, arrays, or references that contain numbers
*   logical values and text representations of numbers that you type directly into the list of arguments are counted
*   of an array or reference argument contains text, logical values or empty cells, those values are ignored; however, cells with the value zero are included
*   arguments that are error values or text that cannot be translated into numbers cause errors
*   if any data point ≤ 0, **GEOMEAN** returns the _#NUM!_ error value
*   the equation for the geometric mean is:

![](<Base64-Image-Removed>)

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-geomean-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-geomean-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-geomean-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-geomean-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-geomean-function/#0 "close")

top