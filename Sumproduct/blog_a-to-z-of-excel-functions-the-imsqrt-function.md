# A to Z of Excel Functions: The IMSQRT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsqrt-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The IMSQRT Function

*   January 3, 2021

A to Z of Excel Functions: The IMSQRT Function
==============================================

A to Z of Excel Functions: The IMSQRT Function
==============================================

4 January 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **IMSQRT** function._

**The IMSQRT function**

An imaginary number is a complex number that can be written as a real number multiplied by the imaginary unit **i** (sometimes denoted **j**) which is defined by its property **i2** = −1. In general, the square of an imaginary number **bi** is **−b2**. For example, 9**i** is an imaginary number, and its square is −81. Zero is considered to be both real and imaginary.

An **imaginary** number **bi** can be added to a **rea**l number **a** to form a **complex number** of the form **a + bi**, where the real numbers **a** and **b** are called, respectively, the **real** part and the **imaginary** part of the **complex number**.

The **polar form** of a complex number is another way to represent the number. The form **z = a + bi** is called the **rectangular form** of a complex number.

![](<Base64-Image-Removed>)

The horizontal axis is the real axis and the vertical axis is the imaginary axis. You can find the real and imaginary components in terms of **r** and **θ**, where **r** is the length of the vector and **θ** is the angle made with the real axis.

From the Pythagorean Theorem,

![](<Base64-Image-Removed>)

By using the basic trigonometric ratios,

![](<Base64-Image-Removed>)

Therefore, multiplying each side by **r**:

![](<Base64-Image-Removed>)

Therefore,

![](<Base64-Image-Removed>)

In the case of a complex number, **r** represents the **absolute value**, or **modulus,**

![](<Base64-Image-Removed>)

and the angle **θ** is called the **argument** of the complex number,

![](<Base64-Image-Removed>)

Using **Euler’s Formula**,

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

It is using this approach that the square root of the complex number **x + yi** may be determined:

![](<Base64-Image-Removed>)

where:

![](<Base64-Image-Removed>)

The **IMSQRT** function returns the square root of a complex number in **x + yi** or **x + yj** text format. It employs the following syntax to operate:

**IMSQRT(inumber)**

The **IMSQRT** function has the following argument:

*   **inumber:** this is required and represents the complex number for which you want to calculate the square root.

It should be further noted that:

*   you should use **[COMPLEX](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-complex-function)
    **to convert real and imaginary coefficients into a complex number
*   **IMSQRT** recognises either the **i** or **j** notation
*   if **inumber** is a value that is not in the **x + yi** or **x + yj** text format, **IMSQRT** returns the _#NUM!_ error value
*   if **inumber** is a logical value, **IMSQRT** returns the _#VALUE!_ error value
*   if the complex number ends in +**i** or –**i** (or **j**), _i.e._ there is no coefficient between the operator and the imaginary unit, there must be no space, otherwise **IMSQRT** will return an _#NUM!_ error.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsqrt-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsqrt-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsqrt-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsqrt-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsqrt-function/#0 "close")

top