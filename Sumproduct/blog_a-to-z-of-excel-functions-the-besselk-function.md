# A to Z of Excel Functions: The BESSELK Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-besselk-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The BESSELK Function

*   November 10, 2016

A to Z of Excel Functions: The BESSELK Function
===============================================

A to Z of Excel Functions: The BESSELK Function
===============================================

11 November 2016

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **BESSELK** function._

**The BESSELK function**

Bessel functions were first defined by the mathematician Daniel Bernoulli and then generalised by Friedrich Bessel as the canonical solutions y(x) of the differential equation

![](https://sumproduct.com/wp-content/uploads/2025/05/7e37823b16365206f4e350f2169b5a1e.jpg)

(known as Bessel’s differential equation) for an arbitrary complex number **α**, the order of the Bessel function. Although **α** and **−α** produce the same differential equation for real **α**, it is conventional to define different Bessel functions for these two values in such a way that the Bessel functions are mostly smooth functions of **α**.

This is not meant to be a mathematical lecture. I will be out of my depth very quickly. Essentially, Excel has four modified Bessel functions, which may be used by specialists as and when needed. **BESSELK** returns the modified Bessel function, which is equivalent to the Bessel functions evaluated for purely imaginary arguments.

The **BESSELK** function employs the following syntax:

**BESSELK(x, n)**

The **BESSELK** function has the following arguments:

*   **x:** required. This is the value at which to evaluate the function
*   **n:** also required. This represents the order of the Bessel function. If **n** is not an integer, it is truncated accordingly.

It should be further noted that:

*   If **x** is nonnumeric, **BESSELK** returns the _#VALUE!_ error value
*   If **n** is nonnumeric, **BESSELK** returns the _#VALUE!_ error value
*   If **n** < 0, **BESSELK** returns the _#NUM!_ error value
*   The **n**th order modified Bessel function of the variable **x** is:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f13c7e5a012f29627e02cf9a385dc61.jpg)

where **Jn** and **Yn** are the **J** (**BESSELJ**) and **Y** (**BESSELY**) Bessel functions, respectively.

Please see my highly informative example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/b428616aeab1fe01f86fe67629ed218a.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-besselk-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-besselk-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-besselk-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-besselk-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-besselk-function/#0 "close")

top