# Regex comes to Excel

**Source:** https://sumproduct.com/news/regex-comes-to-excel/

---

[Home](https://sumproduct.com/)

\> Regex comes to Excel

*   May 22, 2024

Regex comes to Excel
====================

Regex comes to Excel
====================

22 May 2024

**_Regex Comes to Excel_**

Reg Ex was who my wife referred to as a past acquaintance; regex, on the other hand, is a language used for pattern-matching text content. The term “regex” is an abbreviation of “regular expressions” and is frequently implemented in various programming languages such as C, C++, Java, Python, VBScript – and now, _Excel_.

Microsoft has stated that the version of Regex coming to Excel uses a “flavor” _(sic)_ called **PCRE2 (PHP>=7.3)** for those that need to know the underlying technical stuff. Great name for a baby, methinks.

So how is it coming to Excel? Today sees the release of three \[3\] new Excel functions to the Beta versions of Excel:

**REGEXEXTRACT(text, pattern,  
\[return\_mode\], \[ignore\_case\])**

**REGEXREPLACE(text, pattern,  
replacement, \[occurrence\], \[ignore\_case\])**

**REGEXTEST(text, pattern,  
\[ignore\_case\])**.

Clearly, we need to learn a little about “regular expressions” before continuing. Alternatively referred to “rational expressions” upon occasion, a regular expression is a sequence of characters that specifies what is known as a “match pattern” in text. You have most likely used this functionality in Excel already, with features such as “Find and Relace” or by using the **FIND** or **SEARCH** functions in Excel. The purpose of these three \[3\] new functions (presumably, this is just a start!) is to help you match, locate and manage text (strings) in Excel.

The text is obvious but understanding patterns requires you to learn the syntax for regular expressions. Here is a crash course table, which summarises some – but not all – of the main elements, usually referred to as “tokens”.

![](<Base64-Image-Removed>)

Now we are all experts in regex, let’s go through the three new functions.

**_REGEXEXTRACT_**

This function is used extract one or more strings that match a specified pattern from the text being analysed. You may extract the first match, all matches or capturing groups from the first match. Its syntax is as follows:

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

**_REGEXREPLACE_**

The **REGEXREPLACE** function replaces strings within the provided text that matches the pattern with replacement. The syntax of the **REGEXREPLACE** function is:

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

**_REGEXTEST_**

The **REGEXTEST** function allows you to check whether any part of supplied text matches a regular expression (“regex”). It will return TRUE if there is a match and FALSE otherwise. The syntax of the **REGEXTEST** function is:

**REGEXTEST(text,  
pattern, \[case\_sensitivity\])**

where:

*   **text:** this is required, and represents the **text** or the reference to a cell containing the **text** you wish to match against
*   **pattern:** this is also required. This is the regular expression (“regex”) that you wish to match
*   **case\_sensitivity:** the final (optional) argument. This determines whether the match should be case sensitive. It has the following two \[2\] options:

![](<Base64-Image-Removed>)

This function always returns text values. You may convert these results back to numerical values using the **VALUE** function.

Consider the following examples:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**_Word to the Wise_**

In announcing these three new functions, Microsoft has also stated that they will be shortly introducing a way to use regular expressions within **XLOOKUP** and **XMATCH**, via a new, revised option for the **match\_mode** argument. The regex pattern will be supplied as the **lookup\_value** – that’s coming to Beta very soon!!

In the meantime, feel free to play with these new functions (including why not ask Copilot for regex patterns) which are being rolled out to the Beta channel. You will need both patience and:

*   Windows: Version 2406 (Build 17715.20000) or later
*   Mac: Version 16.86 (Build 24051422) or later.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/regex-comes-to-excel/#0)
    
*   [Register](https://sumproduct.com/news/regex-comes-to-excel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/regex-comes-to-excel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/regex-comes-to-excel/#0)

[](https://sumproduct.com/news/regex-comes-to-excel/#0 "close")

top