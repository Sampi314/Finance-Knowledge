# A to Z of Excel Functions: The IMABS Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imabs-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The IMABS Function

*   June 14, 2020

A to Z of Excel Functions: The IMABS Function
=============================================

A to Z of Excel Functions: The IMABS Function
=============================================

15 June 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **IMABS** function._

**The IMABS function**

An imaginary number is a complex number that can be written as a real number multiplied by the imaginary unit **i** (sometimes denoted **j**) which is defined by its property **i2** = −1. In general, the square of an imaginary number **bi** is **−b2**. For example, 9**i** is an imaginary number, and its square is −81. Zero is considered to be both real and imaginary.

An **imaginary** number **bi** can be added to a **rea**l number **a** to form a **complex number** of the form **a + bi**, where the real numbers **a** and **b** are called, respectively, the **real** part and the **imaginary** part of the **complex number**.

Just like the Excel function **ABS** measures the “distance” between a number and zero (0) (_e.g._ **ABS(-5)** is five (5) units from zero (0), therefore, **ABS(-5)** \= 5), so **IMABS(“a + bi”)** measures the distance from zero (0) to the point **z = a + bi**. As can be clearly seen in the diagram, this distance is given by Pythagoras’ Theorem

![](<Base64-Image-Removed>)

Technically, **IMABS** returns the absolute value, or modulus, of a complex number **a + bi**, provided the number has been provided in said text format.

The **IMABS** function employs the following syntax to operate:

**IMABS(inumber)**

The **IMABS** function has the following argument:

*   **inumber:** this is required and represents the complex number for which you want the absolute value.

It should be further noted that:

*   you should use **COMPLEX** to convert real and imaginary coefficients into a complex number
*   **IMABS** recognises either the **i** or **j** notation
*   if the complex number ends in +**i** or –**i** (or **j**), _i.e._ there is no coefficient between the operator and the imaginary unit, there must be no space, otherwise **IMABS** will return an _#NUM!_ error.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imabs-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imabs-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imabs-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imabs-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imabs-function/#0 "close")

top