# A to Z of Excel Functions: The SEARCHB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-searchb-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The SEARCHB Function

*   April 7, 2025

A to Z of Excel Functions: The SEARCHB Function
===============================================

A to Z of Excel Functions: The SEARCHB function.
================================================

7 April 2025

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **SEARCHB** function._

**The SEARCHB function**

![](https://sumproduct.com/wp-content/uploads/2025/06/d708f638f2e4e1c7fca0ff29a1e8a405.jpg)

The **SEARCHB** function locates one text string within a second text string and returns the number in respect of the starting position of the first text string from the first character of the second text string. When a double byte character set (DBCS) is set as the default language, **SEARCHB** counts two (2) bytes per character, rather than the usual one (1).

It employs the following syntax to operate:

**SEARCHB(find\_text, within\_text, \[start\_number\])**

The **SEARCHB** function has the following arguments:

*   **find\_text:** this is required and represents thetextyou wish to find
*   **within\_text:** this is also required. This is the text in which you want to search for the value of the **find\_text** argument
*   **start\_number:** this argument is optional and denotes the character number in the **within\_text** argument at which you want to start searching**.**

It should be further noted that:

*   as stated above, the **SEARCHB** function is not case sensitive. If you want to create a case sensitive search, use **FINDB**
*   you may use wildcard characters, such as the question mark (**?**) and asterisk (**\***), in the **find\_text** argument:
    *   a question mark matches any single character
    *   an asterisk matches any sequence of characters
    *   if you want to find an actual question mark or asterisk, type a tilde (**~**) before the character
*   if the value of **find\_text** is not found, the _#VALUE!_ error value is returned
*   if the **start\_number** argument is omitted, it is assumed to be 1
*   if **start\_number** is not greater than zero (0) or is greater than the length of the **within\_text** argument, the _#VALUE!_ error value is returned
*   use **start\_number** to skip a specified number of characters. The **SEARCHB** function always returns the number of characters from the start of the **within\_text** argument, counting the characters you skip if the **start\_number** argument is greater than one (1)
*   this function may not be available in all languages. **SEARCHB** counts two (2) bytes per character only when a DBCS language is set as the default language (the languages that support DBCS include Japanese, Chinese (Simplified), Chinese (Traditional), and Korean
*   otherwise, **SEARCHB** behaves the same as **SEARCH**, counting one (1) byte per character.

For example,

**\=SEARCHB(“****国****“,”****中国香港****“)**

equals 3 because each character is counted by its bytes. The first character has two bytes, so the second character begins at byte 3 if the default language uses DBCS. If not, it behaves like **SEARCH**:

**\=SEARCH(“****国****“,”****中国香港****“)**

The **SEARCH** formula equals 2 since the search item is in the second position within the string. **SEARCH** returns 2 regardless of the default language setting on your computer.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-searchb-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-searchb-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-searchb-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-searchb-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-searchb-function/#0 "close")

top