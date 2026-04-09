# A to Z of Excel Functions: The ISTHAIDIGIT Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isthaidigit-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ISTHAIDIGIT Function

*   January 5, 2025

A to Z of Excel Functions: The ISTHAIDIGIT Function
===================================================

A to Z of Excel Functions: The ISTHAIDIGIT Function
===================================================

6 January 2025

_Welcome back to our regular A to Z of Excel Functions blog. Today, we look at the **ISTHAIDIGIT** function._

**The ISTHAIDIGIT function**

![](https://sumproduct.com/wp-content/uploads/2025/05/6f434f3a19d3079c8c8e4b3dfbbe7cfa-1.jpg)

The **ISTHAIDIGIT** function in Excel is a one of several functions that is support the Thai language in Microsoft Excel. We are not quite sure why there is such favouritism, but it exists nonetheless.

This function is designed to determine whether a given character or string of characters consists entirely of Thai digits. It is thought the syntax of the function is of the form

**ISTHAIDIGIT(text)**

where:

*   **text** is a required argument and represents the **text** or cell reference that you want to check for Thai digits. This **text** may be a single character or a string of characters.

It appears to be no longer operational but is still recognised in Excel, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/a701597b282dccf30e00948c09ad8069-1.jpg)

This function is presented for completeness only and is denoted as “internally reserved”. It does not appear to work in any generally available current versions of Excel.

Theoretically, the **ISTHAIDIGIT** function should work as follows:

**\=ISTHAIDIGIT(“****๕๖๗****“)**

This should return TRUE because the string “**๕๖๗**” consists entirely of Thai digits.

**\=ISTHAIDIGIT(“****๕****6****๗****“)**

This should return FALSE because the string “**๕****6****๗**” contains a non-Thai digit (**6**).

**\=ISTHAIDIGIT(A1)**

Assuming cell **A1** contains the text “**๓๔๕**“, this should return TRUE.

Presently, this function tends to return _#VALUE!_ but it may return to Excel in a functioning capacity in the future (we have no idea!).

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isthaidigit-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isthaidigit-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isthaidigit-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isthaidigit-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isthaidigit-function/#0 "close")

top