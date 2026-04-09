# A to Z of Excel Functions: The ECMA.CEILING Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ecma-ceiling-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ECMA.CEILING Function

*   February 18, 2024

A to Z of Excel Functions: The ECMA.CEILING Function
====================================================

A to Z of Excel Functions: The ECMA.CEILING Function
====================================================

19 February 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ECMA.****CEILING** function._

**The ECMA.CEILING function**

![](<Base64-Image-Removed>)

**ECMA.CEILING** is not a skin disorder for rooves. This function appears to be provided in Excel as compatible with OnlyOffice, a free software office suite and ecosystem of collaborative applications. It is intended to be compliant with Ecma International (formerly the European Computer Manufacturers Association): **ECMA.CEILING** is the term for the standard version of **[CEILING](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-ceiling-function)
**. It returns a number rounded up, away from zero, to the nearest multiple of significance:

![](<Base64-Image-Removed>)

For example, if you are an American and you want to want to avoid using cents in your prices (that makes no cents) and your product is priced at $4.42, use the formula **\=ECMA.CEILING(**4.42**,** 0.05**)** to round prices up to the nearest nickel.

The **ECMA.****CEILING** function employs the following syntax to operate:

**ECMA.CEILING(number, significance)**

The **ECMA.****CEILING** function has the following arguments:

*   **number:** this is required and represents the value you wish to round
*   **significance:** this is also required. This is the multiple used for rounding.

It should be further noted that:

*   if either argument is nonnumeric, **ECMA.CEILING** returns the _#VALUE!_ error value
*   regardless of the sign of **number**, a value is rounded up when adjusted away from zero. If **number** is an exact multiple of significance, no rounding occurs
*   if **number** is negative, and **significance** is negative, the value is rounded down, away from zero
*   if **number** is negative, and **significance** is positive, the value is rounded up towards zero.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ecma-ceiling-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ecma-ceiling-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ecma-ceiling-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ecma-ceiling-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ecma-ceiling-function/#0 "close")

top