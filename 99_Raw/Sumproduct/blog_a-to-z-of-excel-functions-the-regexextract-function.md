# A to Z of Excel Functions: The REGEXEXTRACT function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexextract-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The REGEXEXTRACT function

*   August 25, 2024

A to Z of Excel Functions: The REGEXEXTRACT function
====================================================

A to Z of Excel Functions: The REGEXEXTRACT function
====================================================

26 August 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **REGEXEXTRACT** function._

**The REGEXEXTRACT function**

![](https://sumproduct.com/wp-content/uploads/2025/05/1d43fd5b1e2b3229f6d83f26e8a7d5a9-1.jpg)

The term “regex” is an abbreviation of “regular expressions” and is frequently implemented in various programming languages such as C, C++, Java, Python, VBScript – and now,_Excel_.

Microsoft has stated that the version of Regex coming to Excel uses a “flavor” _(sic)_ called **PCRE2 (PHP>=7.3)** for those that need to know the underlying technical stuff.

Clearly, we need to learn a little about “regular expressions” before continuing. Alternatively referred to “rational expressions” upon occasion, a regular expression is a sequence of characters that specifies what is known as a “match pattern” in text. You have most likely used this functionality in Excel already, with features such as “Find and Relace” or by using the **[FIND](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
** or **SEARCH** functions in Excel. The purpose of this function is to help you match, locate and manage text (strings) in Excel.

The text is obvious but understanding patterns requires you to learn the syntax for regular expressions. Here is a crash course table, which summarises some – but not all – of the main elements, usually referred to as “tokens”.

![](https://sumproduct.com/wp-content/uploads/2025/05/542109927a956fe3327f847e1ab5b61f-1.jpg)

Now we are all experts in regex, let’s consider the **REGEXEXTRACT** function. This function is used extract one or more strings that match a specified pattern from the text being analysed. You may extract the first match, all matches or capturing groups from the first match. Its syntax is as follows:

**REGEXEXTRACT(text,  
pattern, \[return\_mode\], \[ignore\_case\])**

It has the following three arguments:

*   **text:** this is required, and represents the **text** you are searching within
*   **pattern:** this is also required. This is the regular expression to be applied
*   **return\_mode:** the first of two optional arguments, this specifies which matches to return. It has three alternatives:

![](<Base64-Image-Removed>)

Capturing groups are part of a regular expression (“regex”) pattern surrounded by parentheses “(…)”. They allow you to return separate parts of a single match individually

*   **ignore\_case:** the final (optional) argument. This determines whether the match should be case sensitive. It has the following two \[2\] options:

![](<Base64-Image-Removed>)

This function always returns text values. You may convert these results back to numerical values using the **VALUE** function.

Consider the following examples:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._ _A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexextract-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexextract-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexextract-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexextract-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-regexextract-function/#0 "close")

top