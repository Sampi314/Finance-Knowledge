# A to Z of Excel Functions: The COMPLEX Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-complex-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The COMPLEX Function

*   September 14, 2017

A to Z of Excel Functions: The COMPLEX Function
===============================================

A to Z of Excel Functions: The COMPLEX Function
===============================================

15 September 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **COMPLEX** function._

**The COMPLEX function**

Imagine this complex function. This function converts real and imaginary coefficients into a complex number of the form **x + yi** or **x + yj**, where **i** or **j** denotes the square root of -1.

The COMPLEX function employs the following syntax to operate:

**COMPLEX(real\_num, i\_num, \[suffix\])**

The **COMPLEX** function has the following arguments:

*   **real\_num:** this is required and represents the real coefficient of the complex number
*   **i\_num:** this is also required. This denotes the imaginary coefficient of the complex number
*   **suffix:** this argument is optional. The suffix for the imaginary component of the complex number. If omitted, **suffix** is assumed to be “**i**“.

**NOTE:** All complex number functions accept “**i**” and “**j**” for **suffix**, but neither “I” nor “J”. Using uppercase results in the #VALUE! error value, given the possible confusion with cell references _etc_. All functions that accept two or more complex numbers require that all suffices match.

It should be further noted that:

*   if **real\_num** is non-numeric, **COMPLEX** returns the _#VALUE!_ error value
*   if **i\_num** is non-numeric, **COMPLEX** returns the _#VALUE!_ error value
*   if **suffix** is neither “**i**” nor “**j**“, **COMPLEX** returns the _#VALUE!_ error value
*   arithmetic operations involving imaginary numbers require specific functions such as **IMSUB** (subtract), **IMSUM** (add), **IMPRODUCT** (multiply) and **IMDIV** (divide). If these are not used, the calculations will return the _#VALUE!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found here._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-complex-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-complex-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-complex-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-complex-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-complex-function/#0 "close")

top