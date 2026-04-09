# A to Z of Excel Functions: The HARMEAN Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-harmean-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The HARMEAN Function

*   March 15, 2020

A to Z of Excel Functions: The HARMEAN Function
===============================================

A to Z of Excel Functions: The HARMEAN Function
===============================================

16 March 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **HARMEAN** function._

**The HARMEAN function**

A dangerous function for Ean, they say a picture tells a thousand words:

![](https://sumproduct.com/wp-content/uploads/2025/05/f6436168353b82d428d473d2e42f88ba.jpg)

This time, I think this is true, provided the words are in Swahili (apologies to both of our Swahili readers).

In mathematics, there are three averages known as the **three classical Pythagorean means** are the arithmetic mean (AM), the geometric mean (GM), and the harmonic mean (HM). These means were studied with proportions by Pythagoreans and later generations of mathematicians because of their importance in geometry and music. Face it, if you work in Excel, you’re a budding mathematician!

They are defined by:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-254-1.jpg)

Each mean, **M**, has the following properties:

*   Value preservation

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-239-1.jpg)

*   Scalar consistency – also known as first order homogeneity

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-215-1.jpg)

*   Invariance under exchange (_i.e._ you may swap the values without effect)

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-186-1.jpg)

*   Averaging

![](<Base64-Image-Removed>)

The harmonic and arithmetic means are reciprocal duals of each other for positive arguments:

![](<Base64-Image-Removed>)

whereas the geometric mean is its own reciprocal dual:

![](<Base64-Image-Removed>)

There is an ordering to these means (if all of the **xi**are positive)

**min ≤ HM ≤ GM ≤ AM ≤ max**

with equality holding if and only if the **xi** are all equal.

Returning to our graphic,

![](<Base64-Image-Removed>)

this is a geometric construction of various means of **a** and **b**:

*   the arithmetic average A (**[\>AVERAGE](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-average-function)
    **)
*   the geometric mean G (**[GEOMEAN](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-geomean-function)
    **)
*   the harmonic mean H (**HARMEAN**)
*   the quadratic mean Q (also known as the root mean square, which is not a Pythagorean mean, but is “simply” the square root of the arithmetic mean of the squares of a set of numbers). It has no Excel function, but can be calculated using basic operators and functions in Excel.

With understanding, it provides a graphical illustration of the relationship between these four means.

The harmonic mean (also known as the subcontrary mean) is often used to calculate average rates, for example. It is simple to calculate:

![](<Base64-Image-Removed>)

The **HARMEAN** function has the following syntax:

**HARMEAN(number1, \[number2\], …)**

It has the following argument(s):

*   **number1**, **number2**, …: only **number1** is required, subsequent numbers are optional. You may have between one (1) and 255 arguments to calculate the mean
*   you may also use a single array or a reference to an array instead of arguments separated by commas.

It should also be noted that:

*   as stated above, the harmonic mean is always less than the geometric mean, which is always less than the arithmetic mean
*   arguments can either be numbers or names, arrays or references that contain numbers
*   logical values and text representations of numbers that you type directly into the list of arguments are counted
*   if an array or reference argument contains text, logical values or empty cells, those values are ignored; however, cells with the value zero (0) are included
*   arguments that are error values or text that cannot be translated into numbers cause errors
*   if any data point ? 0, **HARMEAN** returns the _#NUM!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-harmean-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-harmean-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-harmean-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-harmean-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-harmean-function/#0 "close")

top