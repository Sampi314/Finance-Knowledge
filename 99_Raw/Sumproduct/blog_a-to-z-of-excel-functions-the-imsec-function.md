# A to Z of Excel Functions: The IMSEC Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsec-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The IMSEC Function

*   November 22, 2020

A to Z of Excel Functions: The IMSEC Function
=============================================

A to Z of Excel Functions: The IMSEC Function
=============================================

23 November 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **IMSEC** function._

**The IMSEC function**

An imaginary number is a complex number that can be written as a real number multiplied by the imaginary unit **i** (sometimes denoted **j**) which is defined by its property **i2** = -1. In general, the square of an imaginary number **bi** is –**b2**. For example, 9**i** is an imaginary number, and its square is ?81. Zero is considered to be both real and imaginary.

An **imaginary** number **bi** can be added to a **rea**l number **a** to form a **complex number** of the form **a + bi**, where the real numbers **a** and **b** are called, respectively, the **real** part and the **imaginary** part of the **complex number**.

The **polar form** of a complex number is another way to represent the number. The form **z = a + bi** is called the **rectangular form** of a complex number.

![](https://sumproduct.com/wp-content/uploads/2025/05/2f3d9f9b13b569cea15f1d5ed99f71a2.jpg)

The horizontal axis is the real axis and the vertical axis is the imaginary axis. You can find the real and imaginary components in terms of **r** and **θ**, where **r** is the length of the vector and **θ**is the angle made with the real axis.

From the Pythagorean Theorem,

![](https://sumproduct.com/wp-content/uploads/2025/05/5f07840847396f1a4166b7de5c2dd029-1.jpg)

By using the basic trigonometric ratios,

![](https://sumproduct.com/wp-content/uploads/2025/05/37938e4090258439f1b681de3524a582-2.jpg)

Therefore, multiplying each side by **r**:

![](https://sumproduct.com/wp-content/uploads/2025/05/29294e1d316d7e916c8a2f1727a688ff-2.jpg)

Therefore,

![](https://sumproduct.com/wp-content/uploads/2025/05/0e3654c8cc77d6d9adb33a668919a1b6-1.jpg)

In the case of a complex number, **r** represents the **absolute value**, or **modulus** (where **r = |z| =**

![](<Base64-Image-Removed>)

and the angle **θ**is called the **argument** of the complex number

![](<Base64-Image-Removed>)

The secant is simply the reciprocal of the cosine function. The **IMSEC** function returns the secant of a complex number in **x + yi** or **x + yj** text format.

![](<Base64-Image-Removed>)

The **IMSEC** function employs the following syntax to operate:

**IMSEC(inumber)**

The **IMSEC** function has the following argument:

*   **inumber:** this is required and represents the complex number for which you want to calculate the secant.

It should be further noted that:

*   you should use **[\>COMPLEX](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-complex-function)
    **to convert real and imaginary coefficients into a complex number
*   **IMSEC** recognises either the **i** or **j** notation
*   if **inumber** is a value that is not in the **x + yi** or **x + yj** text format, **IMSEC** returns the _#NUM!_ error value
*   if **inumber** is a logical value, **IMSEC** returns the _#VALUE!_ error value
*   if the complex number ends in +**i** or –**i** (or **j**), _i.e._ there is no coefficient between the operator and the imaginary unit, there must be no space, otherwise **IMSEC** will return an _#NUM!_ error.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsec-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsec-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsec-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsec-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsec-function/#0 "close")

top