# Final Friday Fix: June 2024 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-june-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: June 2024 Challenge

*   June 27, 2024

Final Friday Fix: June 2024 Challenge
=====================================

Final Friday Fix: June 2024 Challenge
=====================================

28 June 2024

_On the final Friday of each month, we are going to set an Excel / Power BI challenge for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There are no prizes at this stage: you are playing for bragging rights only!_

**_The Challenge_**

Usually, we extract challenges that are accessible to all – but this month (sorry!), we decided to create a test that perhaps not everyone will be able to play with. We procrastinated on this one, but felt that the recent introduction of the regular expression (“regex”) functions had presented a possible issue some of you will want to overcome. Therefore, we felt this challenge was both apt and timely. For those who can’t play, don’t worry, normal service will resume next month!

Regular expressions (“regex”) is a language used for pattern-matching text content and is frequently implemented in various programming languages such as C, C++, Java, Python, VBScript – and now, _Excel_.

Perhaps we need to learn a little about “regular expressions” before continuing. Alternatively referred to “rational expressions” upon occasion, a regular expression is a sequence of characters that specifies what is known as a “match pattern” in text. You have most likely used this functionality in Excel already, with features such as “Find and Relace” or by using the **FIND** or **SEARCH** functions in Excel. The purpose of these three \[3\] new functions (presumably, this is just a start!) is to help you match, locate and manage text (strings) in Excel.

The text is obvious but understanding patterns requires you to learn the syntax for regular expressions. Here is a crash course table, which summarises some – but not all – of the main elements, usually referred to as “tokens”.

![](https://sumproduct.com/wp-content/uploads/2025/05/90a82cb5c91199b3f53e73d9d6cb4dd7-1.jpg)

With this all borne in mind, let’s turn our attention to one of the new functions: **REGEXEXTRACT**.

This function is used to extract one or more strings that match a specified pattern from the text being analysed. You may extract the first match, all matches or capturing groups from the first match. Its syntax is as follows:

**REGEXEXTRACT(text,  
pattern, \[return\_mode\], \[ignore\_case\])**

It has the following three arguments:

*   **text:** this is required, and represents the **text** you are searching within
*   **pattern:** this is also required. This is the regular expression to be applied
*   **return\_mode:** the first of two optional arguments, this specifies which matches to return. It has three alternatives:

![](https://sumproduct.com/wp-content/uploads/2025/05/029f4e8f7cd5a6fe8e5b0c27dc395f80-1.jpg)

Capturing groups are part of a regular expression (“regex”) pattern surrounded by parentheses “(…)”. They allow you to return separate parts of a single match individually

*   **ignore\_case:** the final (optional) argument. This determines whether the match should be case sensitive. It has the following two \[2\] options:

![](https://sumproduct.com/wp-content/uploads/2025/05/aa73b95d2c2ee712025eb2bc156aaa0e-1.jpg)

This function always returns text values. You may convert these results back to numerical values using the **VALUE** function.

The [attached Excel file](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/June/sp-regex-starter-file.xlsx)
 provides an example:

![](https://sumproduct.com/wp-content/uploads/2025/05/9a63a8e74f59cb2f1846ccb7a0b78c61-1.jpg)

Here, the pattern “o+” (matches one \[1\] or more of “o”) is defined in cell **G17** and extracted from the text string situated in cell **G12**. There are four instances:

The w**o**rd is a w**o**rd in a sentence n**o**t a w**o**rd.

That’s interesting. It might as well tell us there are just four \[4\] instances. But what if I wanted to know the position of these instances in the text string instead (_i.e._ the instances of one or more letter “o” texts in a row occurs in positions 6, 16, 35 and 41)?

![](<Base64-Image-Removed>)

Let’s keep this challenge simple. I appreciate not everyone is yet conversant with regex syntax, so let’s consider the pattern to be “word” instead, _viz._

![](<Base64-Image-Removed>)

The challenge is to find the position(s) of the text / pattern in the text string:

![](<Base64-Image-Removed>)

As always, there are some rules:

*   this is a formula challenge; no Power Query / Get & Transform or VBA!
*   no helper cell(s) is / are allowed
*   the formula should use **REGEXEXTRACT**so that regex patterns may be sought and returned.

Once again, apologies to anyone who cannot use this function yet. It is presently being rolled out to the Beta channel. You will need both patience and:

*   Windows: Version 2406 (Build 17715.20000) or later
*   Mac: Version 16.86 (Build 24051422) or later.

_Sounds easy? Then why not have a go? We’ll publish one solution in Monday’s blog. Have a great weekend in the meantime!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-june-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-june-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-june-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-june-2024-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-june-2024-challenge/#0 "close")

top