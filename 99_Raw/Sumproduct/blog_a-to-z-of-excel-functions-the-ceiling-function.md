# A to Z of Excel Functions: The CEILING Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CEILING Function

*   March 26, 2017

A to Z of Excel Functions: The CEILING Function
===============================================

A to Z of Excel Functions: The CEILING Function
===============================================

27 March 2017

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CEILING** function._

**The CEILING function**

Have you reached your **CEILING**? This function returns number rounded up, away from zero, to the nearest multiple of significance:

![](<Base64-Image-Removed>)

For example, if you are an American (which, let’s be honest is all Microsoft really cares about) and you want to want to avoid using cents in your prices (that makes no cents) and your product is priced at $4.42, use the formula **\=CEILING(**4.42**,** 0.05**)** to round prices up to the nearest nickel.

The **CEILING** function employs the following syntax to operate:

**CEILING(number, significance)**

The **CEILING** function has the following arguments:

*   **number:** this is required and represents the value you wish to round
*   **significance:** this is also required. This is the multiple used for rounding.

It should be further noted that:

*   if either argument is nonnumeric, **CEILING** returns the _#VALUE!_ error value
*   regardless of the sign of **number**, a value is rounded up when adjusted away from zero. If **number** is an exact multiple of significance, no rounding occurs
*   if **number** is negative, and **significance** is negative, the value is rounded down, away from zero
*   if **number** is negative, and **significance** is positive, the value is rounded up towards zero.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ceiling-function/#0 "close")

top