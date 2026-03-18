# A to Z of Excel Functions: The FIELDFUNCTION function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldfunction-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The FIELDFUNCTION function

*   August 4, 2025

A to Z of Excel Functions: The FIELDFUNCTION function
=====================================================

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the FIELDFUNCTION function._

**The FIELDFUNCTION function**

Ah, the mysterious **FIELDFUNCTION**…

![](<Base64-Image-Removed>)

In 2021, Microsoft introduced the first set of Application Programming Interfaces (APIs) that allowed developers to use data type structures within their add-ins.  But Microsoft didn’t stop there. 

Excel has since allowed you to leverage the same capabilities found in Stocks and Geography data types by creating your own properties (entities) and associated “dot functions”.  This allows you to add custom functions to values with such properties (such as entities). 

As an example of a built-in dot function, consider the dot function “Population” for the Geography data type, _viz._

![](<Base64-Image-Removed>)

When creating your own functions, you are often allowed to construct multiple functions with the same name (!), but with different parameter types – **[INDEX](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-index-function)** and **[LOOKUP](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-lookup-function)** are two such native function examples in Excel, for example.  When you allow multiple functions to have the same name but different parameter types or numbers of parameters this is called **function overloading**.

When a function is called, the compiler or interpreter needs to determine which overloaded version to execute.  This is done by resolving the function call to the most appropriate definition based upon the arguments provided in the call.

**Dynamic resolution** occurs when it involves determining the function to call at runtime, often based upon the type of object being used or the address of the function in memory.  It can prove tricky.  Therefore, in programming, resolving a function means determining which specific function definition to use when a function call is made, especially when there are multiple possible definitions (function overloading) or when the function’s location isn’t immediately clear. 

**FIELDFUNCTION** is a function that is specifically employed for resolving dot functions with a function.  It employs the following syntax to operate:

> **FIELDFUNCTION(value, field\_name\[, function\_argument\_1, …\])**

The **FIELDFUNCTION** function has the following arguments:

*   **value:** this is the **value** required
*   **fieldname:** this is required and is a text string that represents the **fieldname** of the dot function to be resolved
*   **function\_argument:** this is optional and there may be no arguments of various data types, one or multiple.  These are used for the function computation.

If it seems a little confusing, it is because presently it is.  This part of Microsoft’s recently announced work (May 2025) on improving Data Type APIs and little documentation exists as at the time of writing.

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every other business day._

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldfunction-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldfunction-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldfunction-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldfunction-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldfunction-function/#0 "close")

top