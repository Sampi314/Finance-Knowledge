# A to Z of Excel Functions: The IMSUM Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsum-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The IMSUM Function

*   January 24, 2021

A to Z of Excel Functions: The IMSUM Function
=============================================

A to Z of Excel Functions: The IMSUM Function
=============================================

25 January 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **IMSUM** function._

**The IMSUM function**

An imaginary number is a complex number that can be written as a real number multiplied by the imaginary unit **i** (sometimes denoted **j**) which is defined by its property **i2** = −1. In general, the square of an imaginary number **bi** is **−b2**. For example, 9**i** is an imaginary number, and its square is −81. Zero is considered to be both real and imaginary.

An **imaginary** number **bi** can be added to a **rea**l number **a** to form a **complex number** of the form **a + bi**, where the real numbers **a** and **b** are called, respectively, the **real** part and the **imaginary** part of the **complex number**.

Sometimes you might wish to add one complex number to one or more other complex numbers. **IMSUM** returns the sum of two or more complex numbers in the **x + yi** or **x + yj** text format.

The **IMSUM** function employs the following syntax to operate:

**IMSUM(inumber1, \[inumber2\], …)**

The **IMSUM** function has the following arguments:

*   **inumber1, \[inumber2\], …****:****inumber1** is required; other arguments are optional. Between 1 and 255 complex numbers may be added together.

It should be further noted that:

*   you should use **[COMPLEX](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-complex-function)
    **to convert real and imaginary coefficients into a complex number
*   **IMSUM** recognises either the **i** or **j** notation
*   if any of **inumber1, \[inumber2\], …** is a value that is not in the **x + yi** or **x + yj** text format, **IMSUM** returns the _#NUM!_ error value
*   if any of **inumber1, \[inumber2\], …** is a logical value, **IMSUM** returns the _#VALUE!_ error value
*   if any of **inumber1, \[inumber2\], …** is non-numeric, **IMSUM** returns the _#VALUE!_ error value
*   if any complex number ends in +**i** or –**i** (or **j**), _i.e._ there is no coefficient between the operator and the imaginary unit, there must be no space, otherwise **IMSUM** will return an _#NUM!_ error
*   the addition of two complex numbers is given by:

![](<Base64-Image-Removed>)

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsum-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsum-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsum-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsum-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-imsum-function/#0 "close")

top