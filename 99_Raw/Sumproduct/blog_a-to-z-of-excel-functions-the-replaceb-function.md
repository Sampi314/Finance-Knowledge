# A to Z of Excel Functions: The REPLACEB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-replaceb-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The REPLACEB Function

*   October 20, 2024

A to Z of Excel Functions: The REPLACEB Function
================================================

A to Z of Excel Functions: The REPLACEB Function
================================================

21 October 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **REPLACEB** function._

**The REPLACEB function**

![](https://sumproduct.com/wp-content/uploads/2025/05/c10254066ff52c84eff7b37ecccebc0e-1.jpg)

The **REPLACEB** function replaces part of a text string (or should that be “sting”?), based upon the number of bytes you specify, with a different text string. This function is not available in all languages. **[REPLACE](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-replace-function)
** is intended for use with languages that use the single-byte character set (SBCS), whereas **REPLACEB** is anticipated for use with languages that use the double-byte character set (DBCS).

The languages that support DBCS include Japanese, Chinese (Simplified), Chinese (Traditional) and Korean.

**REPLACEB** counts each double-byte character as two \[2\] when you have enabled the editing of a language that supports DBCS and then set it as the default language. Otherwise, **REPLACEB** counts each character as one \[1\].

It has the following syntax:

**REPLACEB(old\_text, start\_num, num\_bytes, new\_text)**

The **REPLACEB** function has the following arguments:

*   **old\_text:** this is required and represents thetextin which you wish to replace some or all of the characters
*   **start\_num:** this is also required. This is the position of the character in **old\_text** that you want to replace with **new\_text**
*   **num\_bytes:** this argument is also mandatory and denotes the number of bytes in **old\_text** that you want **REPLACEB** to change for **new\_text**
*   **new\_text:** again required, this is the text that will replace the characters in the **old\_text.**

Please see my examples below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-replaceb-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-replaceb-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-replaceb-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-replaceb-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-replaceb-function/#0 "close")

top