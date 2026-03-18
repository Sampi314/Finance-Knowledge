# A to Z of Excel Functions: The IMSUB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsub-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The IMSUB Function

*   January 17, 2021

A to Z of Excel Functions: The IMSUB Function
=============================================

A to Z of Excel Functions: The IMSUB Function
=============================================

18 January 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **IMSUB** function._

**The IMSUB function**

An imaginary number is a complex number that can be written as a real number multiplied by the imaginary unit **i** (sometimes denoted **j**) which is defined by its property **i2** = −1. In general, the square of an imaginary number **bi** is **−b2**. For example, 9**i** is an imaginary number, and its square is −81. Zero is considered to be both real and imaginary.

An **imaginary** number **bi** can be added to a **rea**l number **a** to form a **complex number** of the form **a + bi**, where the real numbers **a** and **b** are called, respectively, the **real** part and the **imaginary** part of the **complex number**.

Sometimes you might wish to subtract one complex number from another. **IMSUB** returns the difference of two complex numbers in the **x + yi** or **x + yj** text format.

The **IMSUB** function employs the following syntax to operate:

**IMSUB(inumber1, inumber2)**

The **IMSUB** function has the following arguments:

*   **inumber1:** the first argument and represents the number from which to subtract **number2**
*   **inumber2:** this is also required. This is the complex number to subtract from **inumber1**.

It should be further noted that:

*   you should use **[COMPLEX](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-complex-function)
    **to convert real and imaginary coefficients into a complex number
*   **IMSUB** recognises either the **i** or **j** notation
*   if any of **inumber1** or **inumber2** is a value that is not in the **x + yi** or **x + yj** text format, **IMSUB** returns the _#NUM!_ error value
*   if any of **inumber1** or **inumber2** is a logical value, **IMSUB** returns the _#VALUE!_ error value
*   if any of **inumber1** or **inumber2** is non-numeric, **IMSUB** returns the _#VALUE!_ error value
*   if any complex number ends in +**i** or –**i** (or **j**), _i.e._ there is no coefficient between the operator and the imaginary unit, there must be no space, otherwise **IMSUB** will return an _#NUM!_ error
*   the difference of two complex numbers is given by:

![](https://sumproduct.com/wp-content/uploads/2025/05/image2-4-1.gif)

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-50-1.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsub-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsub-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsub-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsub-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsub-function/#0 "close")

top