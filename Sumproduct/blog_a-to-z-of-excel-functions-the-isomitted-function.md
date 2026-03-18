# A to Z of Excel Functions: The ISOMITTED Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isomitted-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ISOMITTED Function

*   August 11, 2021

A to Z of Excel Functions: The ISOMITTED Function
=================================================

A to Z of Excel Functions: The ISOMITTED Function
=================================================

12 August 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ISOMITTED** function._

**The ISOMITTED function**

This new function checks whether the value is missing, and returns either TRUE (value is missing) or FALSE (value is not missing) accordingly. The syntax is simple:

**ISOMITTED(argument)**

where:

*   **argument** is a required parameter, and is the value you want to test, which may be based upon a **LAMBDA**.

The example

**\=LAMBDA(arg1, \[arg2\], IF(ISOMITTED(arg2), arg1, arg2))**

is where this lambda will return the value of **arg1** if **arg2** is omitted (this is why **arg2** is in square brackets as it is an optional argument); otherwise, it will return the value of **arg2**.

Simply put, this lambda will return the value of **arg1** if **arg2** is omitted; otherwise, it will return the value of **arg2**. I’d like to have called this lambda function **Jason** as it sort of checks if his **arg**s are naught, but sadly it’s not Friday 13th…

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
.  
_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isomitted-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isomitted-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isomitted-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isomitted-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isomitted-function/#0 "close")

top