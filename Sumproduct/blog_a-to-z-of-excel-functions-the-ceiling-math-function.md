# A to Z of Excel Functions: The CEILING.MATH Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-math-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CEILING.MATH Function

*   April 9, 2017

A to Z of Excel Functions: The CEILING.MATH Function
====================================================

A to Z of Excel Functions: The CEILING.MATH Function
====================================================

10 April 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CEILING.MATH** function._

**The CEILING.MATH function**

This function sounds like something you calculate whilst swinging from the chandeliers. That’s not the case though, exciting as it sounds. This function actually rounds a number up to the nearest integer or to the nearest multiple of significance _(see below)_.

![](https://sumproduct.com/wp-content/uploads/2025/05/a771211b36c50c1b66c17f37eea015f1.jpg)

The **CEILING.MATH** function employs the following syntax to operate:

**CEILING.MATH(number, \[significance\], \[mode\])**

The **CEILING.MATH** function has the following arguments:

*   **number:** this is required. This **number** must be less than 9.99E+307 and greater than -2.229E-308
*   **significance:** this is optional. This represents the multiple to which **number** is to be rounded
*   **mode:** also optional. For negative numbers, this controls whether **number** is rounded toward or away from zero.

It should be further noted that:

*   by default, significance is +1 for positive numbers and -1 for negative numbers
*   by default, positive numbers with decimal portions are rounded up to the nearest integer. For example, 6.3 is rounded up to 7
*   by default, negative numbers with decimal portions are rounded up (toward zero) to the nearest integer. For example, -6.7 is rounded up to -6
*   by specifying the **significance** and **mode** arguments, you can change the direction of the rounding for negative numbers. For example, rounding the **number** -6.3 to a **significance** of 1 with a **mode** of 1 rounds away from 0, to -7. There are many combinations of **significance** and **mode** values that affect rounding of negative numbers in different ways
*   the **mode** argument does not affect positive numbers
*   the **significance** argument rounds the **number** up to the nearest integer that is a multiple of the **significance** specified. The exception is where the **number** to be rounded is an integer. For example, for a **significance** of 3 the **number** is rounded up to the next integer that is a multiple of 3
*   if **number** divided by a **significance** of 2 or greater results in a remainder, the result is rounded up.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/af04a972f939589eec86f1e3460dcffe.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-math-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-math-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-math-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-math-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-math-function/#0 "close")

top