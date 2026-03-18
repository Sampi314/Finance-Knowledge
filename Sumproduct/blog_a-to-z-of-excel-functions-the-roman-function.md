# A to Z of Excel Functions: The ROMAN Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-roman-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ROMAN Function

*   November 24, 2024

A to Z of Excel Functions: The ROMAN Function
=============================================

A to Z of Excel Functions: The ROMAN Function
=============================================

25 November 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ROMAN** function._

**The ROMAN function**

![](<Base64-Image-Removed>)

Hand in hand with the **[ARABIC](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-arabic-function)
** function in Excel, the **ROMAN** function converts an Arabic numeral (number, to you and me) to Roman numerals, as text.

It has the following syntax:

**ROMAN(number\[, form\])**

The **ROMAN** function has the following arguments:

*   **number:** this is required and represents theArabic **number** you wish to convert
*   **form:** this is optional. This is a number specifying the type of Roman numeral you want. The Roman numeral style ranges from Classic to Simplified, becoming more concise as the value of form increases. For example:

![](<Base64-Image-Removed>)

It should be noted that:

*   _#VALUE!_ will be returned if **number** is non-numerical
*   _#VALUE!_ will be returned if **number** is less than zero \[0\]
*   _#VALUE!_ will be returned if **number** is greater than 3,999
*   _#VALUE!_ will be returned if **form** is included, but is not one of 0, 1, 2, 3, 4, TRUE or FALSE
*   if **number** is between zero and strictly less than 4,000, **ROMAN** truncates the **number**
*   if **number** is an empty cell, **ROMAN** returns an empty string (**“”**)
*   if **number** is zero \[0\], **ROMAN** returns an empty string (**“”**).

Please see my examples below (including some more obscure uses rather than the usual bar chart images):

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-roman-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-roman-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-roman-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-roman-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-roman-function/#0 "close")

top