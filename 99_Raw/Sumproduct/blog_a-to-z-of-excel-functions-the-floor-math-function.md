# A to Z of Excel Functions: The FLOOR.MATH Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-floor-math-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The FLOOR.MATH Function

*   August 4, 2019

A to Z of Excel Functions: The FLOOR.MATH Function
==================================================

A to Z of Excel Functions: The FLOOR.MATH Function
==================================================

5 August 2019

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **FLOOR.MATH** function._

Not to be confused with a floor mat… This function actually rounds a number down to the nearest integer or to the nearest multiple of significance _(see below)_.

![](<Base64-Image-Removed>)

The **FLOOR.MATH** function employs the following syntax to operate:

**FLOOR.MATH(number, \[significance\], \[mode\])**

The **FLOOR.MATH** function has the following arguments:

*   **number:** this is required. This **number** is what is to be rounded (down for positive numbers)
*   **significance:** this is optional. This represents the multiple to which **number** is to be rounded
*   **mode:** also optional. For negative numbers, this controls whether **number** is rounded toward or away from zero.

It should be further noted that:

*   by default, positive numbers with decimal portions are rounded down to the nearest integer, _e.g._ 6.3 is rounded down to 6, using the default **significanc**e (1)
*   by default, negative numbers with decimal portions are rounded away from 0 to the nearest integer, _e.g._ -6.7 is rounded to -7
*   by using 0 or a negative **number** as the **mode** argument, you can change the direction of the rounding for negative numbers. For example, rounding the **number** -6.3 with a **significance** of 1 and a **mode** of -1 rounds toward zero (0), to -6
*   the **significance** argument rounds the **number** down to the nearest integer that is a multiple of the **significance** specified. The exception is where the **number** to be rounded is an integer. For example, for a **significance** of 3, the **number** is rounded down to the last integer that is a multiple of 3
*   if **number** divided by a **significance** of 2 or greater results in a remainder, the result is rounded down.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-floor-math-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-floor-math-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-floor-math-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-floor-math-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-floor-math-function/#0 "close")

top