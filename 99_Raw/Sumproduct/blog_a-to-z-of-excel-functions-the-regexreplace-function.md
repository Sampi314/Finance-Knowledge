# A to Z of Excel Functions: The REGEXREPLACE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexreplace-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The REGEXREPLACE Function

*   September 8, 2024

A to Z of Excel Functions: The REGEXREPLACE Function
====================================================

A to Z of Excel Functions: The REGEXREPLACE Function
====================================================

9 September 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **REGEXREPLACE** function._

**The REGEXREPLACE function**

![](https://sumproduct.com/wp-content/uploads/2025/05/1b27ef75afa7baf5a71cf376c70912ce-1.jpg)

The term “regex” is an abbreviation of “regular expressions” and is frequently implemented in various programming languages such as C, C++, Java, Python, VBScript – and now,_Excel_.

Microsoft has stated that the version of Regex coming to Excel uses a “flavor” _(sic)_ called **PCRE2 (PHP>=7.3)** for those that need to know the underlying technical stuff.

Clearly, we need to learn a little about “regular expressions” before continuing. Alternatively referred to “rational expressions” upon occasion, a regular expression is a sequence of characters that specifies what is known as a “match pattern” in text. You have most likely used this functionality in Excel already, with features such as “Find and Relace” or by using the **[FIND](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
** or **SEARCH** functions in Excel. The purpose of this function is to help you match, locate and manage text (strings) in Excel.

The text is obvious but understanding patterns requires you to learn the syntax for regular expressions. Here is a crash course table, which summarises some – but not all – of the main elements, usually referred to as “tokens”.

![](https://sumproduct.com/wp-content/uploads/2025/05/2a1e73098ccd7ba28e51b3df30f56e40-1.jpg)

Now we are all experts in regex, let’s consider the **REGEXREPLACE** function. This function replaces strings within the provided text that matches the pattern with replacement. The syntax of the **REGEXREPLACE** function is:

**REGEXREPLACE(text,  
pattern, replacement, \[occurrence\], \[case\_sensitivity\])**

where:

*   **text:** this is required, and represents the **text** or the reference to a cell containing the **text** you wish to replace strings within
*   **pattern:** this is also required. This is the regular expression (“regex”) that describes the pattern you wish to replace
*   **replacement:** another required argument, this is the text you wish to replace instances of **pattern**
*   **occurrence:** the first of two optional arguments, this specifies which instance of the pattern you wish to replace. By default, **occurrence** is zero \[0\], which will replace all instances. It should be noted that a negative number replaces that instance, searching from the end instead
*   **case\_sensitivity:** the final (optional) argument. This determines whether the match should be case sensitive. It has the following two \[2\] options:

![](<Base64-Image-Removed>)

This function always returns text values. You may convert these results back to numerical values using the **VALUE** function.

Consider the following examples:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexreplace-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexreplace-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexreplace-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexreplace-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexreplace-function/#0 "close")

top