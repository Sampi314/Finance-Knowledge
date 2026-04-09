# A to Z of Excel Functions: The MIDB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-midb-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The MIDB Function

*   March 13, 2022

A to Z of Excel Functions: The MIDB Function
============================================

A to Z of Excel Functions: The MIDB Function
============================================

14 March 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **MIDB** function._

**The MIDB function**

![](https://sumproduct.com/wp-content/uploads/2025/05/3d5815f8731343d924c9f0efd1cd335d.jpg)

The **MIDB** function returns a specific number of characters from a text string, starting at the position you specify, based upon the number of bytes you specify.

The **MIDB** function employs the following syntax to operate:

**MIDB(text, start\_number, number\_of\_bytes)**

The **MIDB** function has the following arguments:

*   **text:** this is required and represents the text string that contains the characters you want to extract
*   **start\_number:** this is also required and specifies the position of the first character you want to extract from **text**. This is based upon bytes in **text**, so that the first byte has **start\_number** 1, and so on
*   **number\_of\_characters:** this mandatory argument specifies the number of bytes you want **MID** to return from the **text**.

It should be further noted that:

*   if **number\_of\_bytes** is negative, **MIDB** returns the _#VALUE!_ error value
*   this function may not be available in all languages. **MIDB** counts two (2) bytes per character only when a DBCS language is set as the default language (the languages that support DBCS include Japanese, Chinese (Simplified), Chinese (Traditional), and Korean
*   otherwise, **MIDB** behaves the same as **MID**, counting one (1) byte per character.

For example, **\=MIDB(“****中国香港****“,3,2)** is equal to “**国**“. **MIDB** returns the second character only, because each character is counted as two (2) bytes and the second character begins at the third byte.

However, **\=MID(“****中国香港****“,3,2)** is equal to **“****香港****“** as **MID** returns the next two (2) characters from the third character onwards, because each character is counted as one (1). **MID** returns these two characters no matter what the default language setting is on your computer.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-midb-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-midb-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-midb-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-midb-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-midb-function/#0 "close")

top