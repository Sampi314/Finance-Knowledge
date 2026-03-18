# A to Z of Excel Functions: The FINDB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-findb-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The FINDB Function

*   June 16, 2019

A to Z of Excel Functions: The FINDB Function
=============================================

A to Z of Excel Functions: The FINDB Function
=============================================

17 June 2019

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **FINDB** function._

The **FINDB** function locates a text “sub-string” inside a longer text string, and returns the starting position of it within the parent string (_i.e._ where the first character is in the longer text string). This function is not available in all languages.

The **FINDB** function employs the following syntax to operate:

**FINDB(find\_text, within\_text, \[start\_number\])**

The **FINDB** function has the following arguments:

*   **find\_text:** this is required and represents the text you wish to find
*   **within\_text:** this is also required. This represents the longer (parent) string that contains the text you seek
*   **start\_number:** this is optional. This specifies the character at which to start the search. The first character in **within\_text** is character number 1. If you omit **start\_number**, then it is assumed to be 1.

It should be noted that:

*   this function is not available in all languages
*   **FINDB** is intended for use with languages that use the double-byte character set (DBCS)
*   **FINDB** always counts each double-byte character as 2 when you have enabled the editing of a language that supports DBCS and then set it as the default language. Otherwise, **FINDB** counts each character as 1
*   The languages that support DBCS include Chinese (Simplified), Chinese (Traditional), Japanese and Korean
*   **FINDB** is case sensitive and doesn’t allow wildcard characters. If you don’t want to do a case sensitive search or use wildcard characters, you can use **SEARCHB** instead
*   if **find\_text** is “” (empty text), **FINDB** matches the first character in the search string (that is, the character numbered **start\_number** or 1)
*   **find\_text** cannot contain any wildcard characters
*   if **find\_text** does not appear in **within\_text**, **FINDB** returns the _#VALUE!_ error value
*   if **start\_number** is not greater than zero (0), **FINDB** returns the _#VALUE!_ error value
*   if **start\_number** is greater than the length of **within\_text**, **FINDB** returns the _#VALUE!_ error value
*   use **start\_number** to skip a specified number of characters. Using **FIND** as an example, suppose you are working with the text string “SumProduct”. To find the number of the first “u” in the descriptive part of the text string, set **start\_number** equal to 4 so that the first part of the text is not searched. **FIND** begins with character 4, finds **find\_text** at the next character, and returns the number 8. **FIND** always returns the number of characters from the start of **within\_text**,
*   counting the characters you skip if **start\_number** is greater than 1.

In the following example, **FINDB** returns 3 because each character is counted by its bytes; the first character has 2 bytes, so the second character begins at byte 3.

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-findb-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-findb-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-findb-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-findb-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-findb-function/#0 "close")

top