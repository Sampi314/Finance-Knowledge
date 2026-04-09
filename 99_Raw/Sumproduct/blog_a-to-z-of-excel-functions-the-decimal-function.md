# A to Z of Excel Functions: The DECIMAL Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-decimal-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DECIMAL Function

*   July 8, 2018

A to Z of Excel Functions: The DECIMAL Function
===============================================

A to Z of Excel Functions: The DECIMAL Function
===============================================

9 July 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DECIMAL** function._

**The DECIMAL function**

This function converts a text representation of a number in a given base into a decimal number (base 10).

The **DECIMAL** function employs the following syntax to operate:

**DECIMAL(text, radix)**

The **DECIMAL** function has the following arguments:

*   **text**: this is required
*   **radix:** this is also required and must be an integer.

It should be further noted that:

*   the string length of **text** must be less than or equal to 255 characters
*   the **text** argument can be any combination of alpha-numeric characters that are valid for the **radix**, and is not case sensitive
*   Excel supports a **text** argument greater than or equal to 0 and less than 2^53. A **text** argument that resolves to a number greater than 2^53 may result in a loss of precision
*   **radix** must be greater than or equal to 2 (binary, or base 2) and less than or equal to 36 (base 36)
*   a **radix** greater than 10 use the numeric values 0-9 and the letters A-Z as needed. For example, base 16 (hexadecimal) uses 0-9 and A-F, and base 36 uses 0-9 and A-Z
*   if either argument is outside its constraints, **DECIMAL** may return the _#NUM!_ or _#VALUE!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-decimal-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-decimal-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-decimal-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-decimal-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-decimal-function/#0 "close")

top