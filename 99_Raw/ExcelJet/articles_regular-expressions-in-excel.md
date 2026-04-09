# Regular Expressions in Excel | Exceljet

**Source:** https://exceljet.net/articles/regular-expressions-in-excel

---

[Skip to main content](https://exceljet.net/articles/regular-expressions-in-excel#main-content)

[](https://exceljet.net/articles/regular-expressions-in-excel#)

*   [Previous](https://exceljet.net/articles/floating-point-errors-in-excel)
    
*   [Next](https://exceljet.net/articles/complex-numbers-in-excel)
    

Regular Expressions in Excel
============================

by Dave Bruns · Updated 30 Jun 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/8899/download?token=Sed9Ckvu)
 (29.02 KB)

![Regular Expressions in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Regular_Expressions_in_Excel.png "Regular Expressions in Excel")

Summary
-------

After decades of waiting, Excel finally supports Regular Expressions, aka _regex_! Learn how three powerful new functions - REGEXTEST, REGEXREPLACE, and REGEXEXTRACT - can transform complex text operations into elegant, maintainable formulas. Whether you're cleaning data, validating inputs, or extracting patterns, these new tools will change how you write advanced formulas in Excel.

### Table of Contents

*   [What is regex?](https://exceljet.net/articles/regular-expressions-in-excel#what-is-regex)
    
*   [A brief history of regex in Excel](https://exceljet.net/articles/regular-expressions-in-excel#a-brief-history-of-regex-in-excel)
    
*   [Regex vs. Excel wildcards](https://exceljet.net/articles/regular-expressions-in-excel#regex-vs-excel-wildcards)
    
*   [Why regex is useful in Excel](https://exceljet.net/articles/regular-expressions-in-excel#why-regex-is-useful-in-excel)
    
*   [The REGEXTEST function](https://exceljet.net/articles/regular-expressions-in-excel#the-regextest-function)
    
*   [The REGEXEXTRACT function](https://exceljet.net/articles/regular-expressions-in-excel#the-regexextract-function)
    
*   [The REGEXREPLACE function](https://exceljet.net/articles/regular-expressions-in-excel#the-regexreplace-function)
    
*   [Regex quick reference](https://exceljet.net/articles/regular-expressions-in-excel#regex-quick-reference)
    
*   [Important regex terminology](https://exceljet.net/articles/regular-expressions-in-excel#regex-terminology)
    
*   [Regex anchors](https://exceljet.net/articles/regular-expressions-in-excel#regex-anchors)
    
*   [Regex tips](https://exceljet.net/articles/regular-expressions-in-excel#regex-tips)
    
*   [Summary](https://exceljet.net/articles/regular-expressions-in-excel#summary)
    

### What is regex?

What is regex? Regex, short for Regular Expressions, is a powerful tool for pattern matching in text data. Using a combination of metacharacters, literal characters, character classes, and quantifiers, you can define complex search patterns to extract, validate, or manipulate text data. [See examples below](https://exceljet.net/articles/regular-expressions-in-excel#regex-quick-reference)
. The main benefit of regex in Excel is the ability to work with text very precisely without resorting to complicated formulas that are hard to understand and maintain. In Excel, Regex support comes primarily from the introduction of three brand-new functions:

*   [The REGEXTEST function](https://exceljet.net/functions/regextest-function)
    
*   [The REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
    
*   [The REGEXEXTRACT function](https://exceljet.net/functions/regexextract-function)
    

In addition to the three dedicated functions above, [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 and [XMATCH](https://exceljet.net/functions/xmatch-function)
 have also been upgraded to support regex. Plus, you can use the functions above _inside other formulas_ to instantly upgrade their capabilities. For example, you can use REGEXTEST inside the IF function as the logical test, which "upgrades" IF to support regex. In this article, I'll introduce Excel's new regex functions and provide examples of how these functions are helpful. But first, let's review how we got here.

> Many existing guides to using Regular Expressions in Excel on the web are based on VBA or custom add-ins. However, in Excel 365, you don't need to use VBA or add-ins to use Regular Expressions because regex support is built-in. This guide covers the _native regex support_ added to Excel via the three regex functions listed above.

### A brief history of regex in Excel

Why doesn’t Excel support Regex? This is one of those questions that has bothered Excel power users for many years. It’s been a topic of heated debates and the cause of many clunky, complicated formulas. Although regex is a standard feature in many programming languages, it was notably absent from Excel for most of its history. Here's how Excel's text processing capabilities evolved:

*   Excel has always supported basic wildcards (\* and ?), but these are primitive compared to regex patterns. Users had to rely on combining functions like LEFT, RIGHT, MID, FIND, SEARCH, and SUBSTITUTE for pattern matching, resulting in complex, hard-to-maintain formulas.
*   Power users worked around these limitations using VBA, Power Query, or custom add-ins for regex support, but these tools require different skills and are not available to all users.
*   In Excel 2013, Microsoft added some regex-like capability with the FILTERXML function, which uses XPath queries for pattern matching. Still, this function is not widely used or available in Excel for Mac.
*   In 2022, Microsoft improved text handling with TEXTSPLIT, TEXTBEFORE, and TEXTAFTER functions. These functions make it much easier to split text at specific locations in an Excel formula. However, they do not support regex.
*   In December 2024, Excel introduced three regex functions: REGEXTEST, REGEXREPLACE, and REGEXEXTRACT. These functions modernize Excel's text-processing capabilities and bring it up to speed with other professional tools.

Now that Excel supports regex directly, many complicated formulas of the past can be drastically simplified.

### Regex vs. Excel wildcards

Excel wildcards are like a toolbox with just two tools: \* for "anything" and ? for "one thing." Sure, you can find "apple\*" or "?at," but that's about it. They're the flip phone of pattern matching.

Regex is a different story. While wildcards are asking "Does this have an "a" followed by... stuff?", regex is performing complex queries like "Any word that starts with a capital letter, contains exactly two numbers, and ends with x or y but not z".

Want to match exactly three digits followed by optional whitespace and a hyphen? Try \\d{3}\\s\*- Need to find an email address or validate a strong password? Regex has patterns for that. It can even "look ahead" in your text to match patterns only when they occur before something else.

You get the idea. Regex goes _far beyond_ basic wildcards.

### Why regex is useful in Excel

Before we get into the details, let's look at a specific example of how regex can help simplify a formula. In the workbook below, the goal is to extract the numbers from the product codes in column B. With hundreds of functions available, you might think this is a simple problem in Excel, but it's not! The problem is that the numbers vary in length, and their location in the product code also changes. There's just no easy way to figure out where each number begins and ends. Instead, the formula below in cell D5 takes a "brute force" approach and simply _removes_ all non-numeric characters. It looks like this:

    =TEXTJOIN("",TRUE,IFERROR(MID(B5,SEQUENCE(LEN(B5)),1)+0,""))

![Example of a complicated formula before regex](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/why_regex_is_useful_example1.png "Example of a complicated formula before regex")

It's not exactly obvious what this formula is doing, right? You can find an [explanation here](https://exceljet.net/formulas/strip-non-numeric-characters)
.  It's pretty complicated, and I'm even cheating a bit because I'm assuming at least Excel 2021, which has the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. In Excel 2019, things get uglier because we need to spin up our own number array with the volatile [INDIRECT function](https://exceljet.net/functions/indirect-function)
 and the ROW function:

    =TEXTJOIN("",TRUE,IFERROR(MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1)+0,""))

In Excel versions _before_ 2019, the formula becomes even more complicated!

What about regex? Does it help in this case? _Yes_. Regex helps a lot! In the worksheet below, the new formula in cell D5 is based on the REGEXEXTRACT function. Here it is:

    =REGEXEXTRACT(B5,"\d+")

Yep, that's the whole formula. Basically, we are asking REGEXEXTRACT for a sequence of 1 or more numbers. You can see the results below. I think you'll agree that this new formula is a lot simpler 🙂

![Example of a simple formula after regex](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/why_regex_is_useful_example2.png "Example of a simple formula after regex")

Now that you have a taste of how regex can help simplify difficult formulas, let's look more closely at the three new regex functions.

### The REGEXTEST function

The Excel REGEXTEST function tests for a given regex pattern. The result from REGEXTEST is TRUE or FALSE. For example, `=REGEXTEST(A1,"[0-9]")` will return TRUE if cell A1 contains any numeric digit, and `=REGEXTEST(A1,"[A-Z]")` will return TRUE if A1 contains any uppercase letters. REGEXTEST opens up new possibilities for data validation and text analysis directly within Excel formulas. In the worksheet below, REGEXTEST is configured to test addresses for one of four US states: MN, MT, ND, and SD. The formula in D5, copied down, looks like this:

    =REGEXTEST(B5,"\b(MN|MT|ND|SD)\b")

The pattern "\\b(MN|MT|ND|SD)\\b" matches MN, MT, ND, or SD. The '\\b' is a word boundary character. It will match a space and any punctuation that typically appears around a word. The '|' creates OR logic.

![Example the REGEXTEST function with or logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/regextest_function_example_with_or_logic.png "Example the REGEXTEST function with or logic")

Note: While you probably don't need a TRUE or FALSE result in a case like this, you could use _exactly the same formula_ above _inside_ the [FILTER function](https://exceljet.net/functions/filter-function)
 to list all addresses that contain MN, MT, ND, or SD.

[Learn more about the REGEXTEST function](https://exceljet.net/functions/regextest-function)
.

### The REGEXEXTRACT function

The REGEXEXTRACT function extracts specific information from a string based on a Regex pattern. It’s perfect for pulling out key pieces of data from messy text. For example, in the worksheet below, the goal is to extract telephone numbers in the format `xxx-xxx-xxxx` from the text strings in column B. The formula in cell D5, copied down, looks like this:

    =REGEXEXTRACT(B5,"\d{3}-\d{3}-\d{4}")

![Example the REGEXEXTRACT function with telephone numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/regexextract_function_example_with_telephone_numbers.png "Example the REGEXEXTRACT function with telephone numbers")

This example gives you a sense of regex's power and flexibility. This formula is looking for and extracting phone numbers that follow a pattern like this: "123-456-7890". Let's break down each part:

*   '\\d{3}' looks for exactly 3 digits
*   '-' looks for a hyphen
*   '\\d{3}' looks for 3 more digits
*   '-' looks for another hyphen
*   '\\d{4}' looks for 4 more digits

So, if you have text that contains something like "My phone number is 555-123-4567", this formula will pull out just "555-123-4567".

[Learn more about the REGEXEXTRACT function](https://exceljet.net/functions/regexextract-function)
.

### The REGEXREPLACE function

The REGEXREPLACE function allows you to replace parts of a string that match a regex pattern with something else. It’s very useful for cleaning up or reformatting text. You can think of REGEXREPLACE as a much more powerful version of the simplistic [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. For example, in the workbook below, REGEXREPLACE is configured to remove all non-numeric characters from the telephone numbers in column B. The formula in cell D5, copied down, is:

    =REGEXREPLACE(B5,"[^0-9]","")

![Example the REGEXREPLACE function to clean telephone numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/regexreplace_function_example_clean_phone_numbers.png "Example the REGEXREPLACE function to clean telephone numbers")

The pattern "\[^0-9\]" will match any character that is not a number. Since the replacement pattern is an empty string (""), the result is that REGEXREPLACE effectively "strips" all non-numeric characters from the input, and the final result contains numbers only.

[Learn more about the REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
.

### Regex quick reference

Regex relies on _patterns_ to match specific text. The table below contains some simple regex patterns. These patterns can be combined to create very [capable](https://exceljet.net/formulas/validate-strong-password)
 text-matching formulas.

| Pattern | Description and examples |
| --- | --- |
| abc | Matches the literal text 'abc'. Example: 'abc' matches 'abc', but not 'ABC' or 'ab'. |
| .   | Matches any single character except a newline. Example: 'c.t' matches 'cat', 'cot', 'c@t'. |
| \\d | Matches any digit (0-9). Example: '\\d\\d\\d' matches '123', '999'. |
| \\w | Matches any word character (letter, digit, underscore). Example: '\\w\\w' matches 'ab', '1\_', 'A9'. |
| \\s | Matches any whitespace character (space, tab, newline). Example: 'a\\sb' matches 'a b'. |
| \\b | Matches a word boundary. Example: '\\bcat\\b' matches 'cat' in 'the cat sits' but not 'category'. |
| \[abc\] | Matches any one character listed in brackets. Example: 'gr\[ae\]y' matches 'gray' and 'grey'. |
| \[a-z\] | Matches any one character in the range. Example: '\[a-z\]' matches any lowercase letter. |
| \[^abc\] | Matches any character NOT listed. Example: '\[^0-9\]' matches any non-digit. |
| a\* | Matches 0 or more 'a'. Example: 'ca\*t' matches 'ct', 'cat', 'caaat'. |
| a+  | Matches 1 or more 'a'. Example: 'ca+t' matches 'cat', 'caat', but not 'ct'. |
| a?  | Matches 0 or 1 'a'. Example: 'colou?r' matches 'color' and 'colour'. |
| a{3} | Matches exactly 3 'a'. Example: 'a{3}' matches 'aaa', but not 'aa' or 'aaaa'. |
| a{2,4} | Matches 2 to 4 'a'. Example: 'a{2,4}' matches 'aa', 'aaa', 'aaaa'. |
| ^abc | Matches 'abc' at start of string. Example: '^The' matches 'The cat' but not 'In The'. |
| abc$ | Matches 'abc' at end of string. Example: '.com$' matches 'example.com'. |
| (abc) | Groups pattern and captures match. Example: '(cat\|dog)s' matches 'cats' and 'dogs'. |
| (?:abc) | Non-capturing group. Like () but doesn't store the match. |
| a\|b | Matches 'a' or 'b'. Example: 'cat\|dog' matches 'cat' or 'dog'. |

### Regex terminology

Because Regex is essentially a mini-language, it has its own vocabulary. Here is a list of some important terminology:

*   **Pattern** - The actual sequence of characters that defines the regex. For example `\d+` is a pattern for one or more digits.
*   **Literal** - Characters in a regex pattern that match themselves. For example, in `cat`, the literals are `c`, `a`, and `t`.
*   **Metacharacter** - Characters with special meanings in regex. For example, a period `.` matches any character, `^` matches the start of a string, `$` matches the end of a string.
*   **Character Class** - A set of characters enclosed in square brackets `[]` that matches any one of the characters inside. For example, `[aeiou]` matches any vowel.
*   **Quantifier** - Specifies how many instances of a character, group, or character class must be present in the input for a match. For example, `a*` matches zero or more a's, `a+` matches one or more a's, `a{3}` matches exactly three a's.
*   **Escape Sequence** - A way to handle metacharacters as literals by preceding them with a backslash `\`. For example, `\.` matches a literal period.
*   **Group** - A part of a regex pattern enclosed in parentheses `()` that can be referred to later. For example, `(abc)` matches the exact sequence `abc`.
*   **Capturing Group** - A part of a regex pattern enclosed in parentheses `()` that not only matches text but also 'captures' or remembers what was matched for later use. For example, in the pattern `(\d{4})-(\d{2})` the first group captures 4 digits before the hyphen and the second captures 2 digits after the hyphen.
*   **Non-capturing Group** - A group that matches text but doesn't capture it, written as `(?:...)`. Useful for grouping without creating a reference. Like `()`, but doesn't store the match.
*   **Alternation** - The pipe `|` character is used to match one thing or another. For example, `cat|dog` matches `cat` or `dog`.
*   **Anchor** - Special characters that match positions within a string rather than actual characters. For example, `^` matches the start of a string, `$` matches the end of a string.
*   **Wildcard** - The dot `.` character, which matches _any single character_ except a newline character. For example, `c.t` matches `cat`, `cot`, `cut`, `etc`.
*   **Boundary** - Special sequences that match positions between characters. For example, `\b` matches a word boundary, `\B` matches a non-word boundary.
*   **Greedy vs Lazy** - By default, quantifiers are 'greedy' and match as much text as possible. Adding `?` after a quantifier makes it 'lazy' and matches as little as possible. For example, `.*` vs `.*?`

### Regex anchors

By default, regex will match any _substrings_ that match the pattern. For example, the pattern `cat` will match "cat", "catapult", "scatter", "concatenate", or "the top category" because "cat" appears as a substring in each text string. To match an entire string exactly (i.e., to match the exact text in a cell in Excel), we need to use regex anchors:

*   `^` (caret): Matches the start of the string. For example, `^abc` matches "abc123" but not "123abc".
*   `$` (dollar sign): Matches the end of the string. For example, `abc$` matches "123abc" but not "abc123".

To match the entire contents of a cell exactly, add the `^` and the `$` to a pattern. For example, the pattern `^abc$` will match "abc" but not "123abc456" or "abcd". 

> Without these anchors, a regex pattern will match substrings that appear anywhere in the string, which may or may not meet your needs. For instance, the pattern "abc" will match "abc" in "123abc456" or "abcd", but  the pattern "^abc$" will only match "abc".

### **Regex tips**

Regex patterns can get complicated fast. Here are some general tips for creating and debugging regex patterns:

*   Start small - Test the simplest version of your pattern first and work from there. If `\d+` doesn't work, `\d{3}-\d{3}` probably won't either.
*   Use REGEXTEST to validate your patterns against sample data. REGEXTEST returns TRUE or FALSE, so it is perfect for testing in Excel.
*   Special characters (. \* + ? etc.) need to be escaped with '\\' to match these characters literally.
*   Regular expressions are case-sensitive by default. You can disable this by setting _case\_sensitivity_ to 1 for each of the regex functions in Excel.
*   `^` and `$` match start/end of the entire string, not individual lines
*   If a pattern isn't matching, try making it more permissive. For example, `\s*` instead of just a space to handle variable whitespace.
*   Seek help from AI like [ChatGPT](https://chatgpt.com/)
     or [Claude](https://claude.ai/)
    , and classic regex websites like [regex101](https://regex101.com/)
     and [regexr](https://regexr.com/)
    . These are great resources to help you create the patterns you need.

### **Summary**

The introduction of regex as a native tool in Excel formulas is a game-changer. Many complicated formulas of the past will slowly disappear as people learn how to turn "spaghetti code" into elegant and reliable formulas based on regex. Yet, regex definitely has a learning curve, and the large number of symbols and patterns can be intimidating. Regex is sometimes called a write-only language, only half jokingly :) However, you don't need to _master_ regex in order to _use_ regex. A little goes a long way. Start with small problems and learn as you go.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)