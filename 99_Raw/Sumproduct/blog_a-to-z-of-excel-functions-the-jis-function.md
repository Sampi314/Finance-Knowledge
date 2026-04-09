# A to Z of Excel Functions: The JIS Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-jis-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The JIS Function

*   August 22, 2021

A to Z of Excel Functions: The JIS Function
===========================================

A to Z of Excel Functions: The JIS Function
===========================================

23 August 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **JIS** function._

**The JIS function**

There’s a great trivia question out there that asks, which is the only letter of the alphabet for which there is no Excel function? Wiser hands than mine say this is “J”. I say, “it depends”. If they have Excel 2013 or later, “they” would be right as the **JIS** function was “retired” in this edition.

The **JIS** function (such an unfortunate name…) was renamed in Excel 2013 as **DCBS** (pretty obvious if you think about it – _not_). This function returns the text string converted from single byte (SCBS) to double byte (DCBS) characters.

A double-byte character set (DBCS) is a character encoding in which either all characters (including control characters) are encoded in two bytes, or merely every graphic character not representable by an accompanying single-byte character set (SBCS) is encoded in two bytes (Han characters would generally comprise most of these two-byte characters). A DBCS supports national languages that contain many unique characters or symbols (the maximum number of characters that can be represented with one byte is 256 characters, while two bytes can represent up to 65,536 characters, _i.e._ 2562).

Examples of such languages include Japanese and Chinese. Korean Hangul does not contain as many characters, but KS X 1001 supports both Hangul and Hanja, and uses two bytes per character.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-191.jpg)

This function converts half-width (single-byte) letters within a character string to full-width (double-byte) characters. The name of the function (and the characters that it converts) depends upon your language settings.

For Japanese, this function changes half-width (single-byte) English letters or katakana within a character string to full-width (double-byte) characters.

The **JIS** function employed the following syntax to operate:

**JIS(text)**

The **JIS** function had the following argument:

*   **text:** this is required and represents the text you wish to convert from single byte to double byte characters.

It should be noted that:

*   this function was removed in Excel 2013
*   **DCBS** was introduced in Excel 2013 and has replaced this function
*   this function does not appear in the Function Wizard
*   If **text** does not contain any half-width characters, then **text** is not altered
*   this function is used in connection to phonetics and using different types of fonts and languages
*   you may use the **ASC** function to convert from double byte characters to single byte characters.

My example is extremely enlightening:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-jis-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-jis-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-jis-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-jis-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-jis-function/#0 "close")

top