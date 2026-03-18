# A to Z of Excel Functions: The NUMBERVALUE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-numbervalue-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The NUMBERVALUE Function

*   March 19, 2023

A to Z of Excel Functions: The NUMBERVALUE Function
===================================================

A to Z of Excel Functions: The NUMBERVALUE Function
===================================================

20 March 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **NUMBERVALUE** function._

**The NUMBERVALUE function**

The **NUMBERVALUE** function converts text into a number, in a locale-independent way. This may also be used to convert local-specific values into locale-independent values.

The **NUMBERVALUE** syntax is as follows:

**NUMBERVALUE(text,  
\[decimal\_separator\], \[group\_separator\])**

The **NUMBERVALUE** function syntax has the following arguments:

*   **text**: this is required. This is the **text** to convert into a number
*   **decimal\_separator**: this argument is optional. This is the character used to separate the integer and fractional part of the result
*   **group\_separator**: this argument is also optional. This represents the character used to separate groupings of numbers, such as thousands from hundreds and millions from thousands.

It should be noted that:

*   if the **decimal\_separator** and **group\_separator** arguments are not specified, separators from the current locale are used
*   if multiple characters are used in the **decimal\_separator** or **group\_separator** arguments, only the first character is used
*   if an empty string (**“”**) is specified as the **text** argument, the result is zero \[0\]
*   empty spaces in the **text** argument are ignored, even in the middle of the argument. For example, ” 3 000 ” is returned as 3,000
*   if a **decimal\_separator** is used more than once in the **text** argument, **NUMBERVALUE** returns the _#VALUE!_ error value
*   if the **group\_separator** occurs before the **decimal\_separator** in the **text** argument , the **group\_separator** is ignored
*   if the **group\_separator** occurs after the **decimal\_separator** in the **text** argument, **NUMBERVALUE** returns the _#VALUE!_ error value
*   if any of the arguments are not valid, **NUMBERVALUE** returns the _#VALUE!_ error value
*   if the **text** argument ends in one or more percent signs (**%**), they are used in the calculation of the result. Multiple percent signs are additive if they are used in the **text** argument just as they are if they are used in a formula. For example, **\=NUMBERVALUE(“9%%”)**returns the same result (0.0009) as the formula **\=9%%**.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/87d4f467d98c1489ec3d8bd2e3bd6f74.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-numbervalue-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-numbervalue-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-numbervalue-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-numbervalue-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-numbervalue-function/#0 "close")

top