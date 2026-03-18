# A to Z of Excel Functions: The LEFTB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-leftb-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The LEFTB Function

*   September 12, 2021

A to Z of Excel Functions: The LEFTB Function
=============================================

A to Z of Excel Functions: The LEFTB Function
=============================================

13 September 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **LEFTB** function._

**The LEFTB function**

The **LEFTB** function returns the first character or characters in a text string, based on the number of bytes specified.

The **LEFTB** function employs the following syntax to operate:

**LEFTB(text, \[number\_of\_bytes\])**

The **LEFTB** function has the following arguments:

*   **text:** this is required and represents the text string that contains the characters you want to extract
*   **number\_of\_bytes:** this argument is optional and specifies the number of characters you want **LEFTB** to extract, based upon bytes.

It should be further noted that:

*   **number\_of\_bytes** must be greater than or equal to zero
*   if **number\_of\_bytes** is omitted, it is assumed to be one (1)
*   this function may not be available in all languages. **LEFTB** counts two (2) bytes per character only when a DBCS language is set as the default language (the languages that support DBCS include Japanese, Chinese (Simplified), Chinese (Traditional), and Korean
*   otherwise, **LEFTB** behaves the same as **[LEFT](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-left-function)
    **, counting one (1) byte per character.

For example, **\=LEFTB(“****中国香港****“,2)** is equal to “**中**“. **LEFTB** returns the first character only, because each character is counted as two (2) bytes.

However, **\=LEFT(“****中国香港****“,2)** is equal to **“****中国****“** as **LEFT** returns the first two (2) characters, because each character is counted as one (1). **LEFT** returns the first two characters no matter what the default language setting is on your computer.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
.  
_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-leftb-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-leftb-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-leftb-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-leftb-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-leftb-function/#0 "close")

top