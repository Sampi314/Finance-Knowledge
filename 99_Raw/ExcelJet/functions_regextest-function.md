# Excel REGEXTEST function | Exceljet

**Source:** https://exceljet.net/functions/regextest-function

---

[Skip to main content](https://exceljet.net/functions/regextest-function#main-content)

[](https://exceljet.net/functions/regextest-function#)

*   [Previous](https://exceljet.net/functions/regexreplace-function)
    
*   [Next](https://exceljet.net/functions/scan-function)
    

Excel 365

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

REGEXTEST Function
==================

by Dave Bruns · Updated 17 Jun 2025

Related functions 
------------------

[REGEXEXTRACT](https://exceljet.net/functions/regexextract-function)

[REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)

[FIND](https://exceljet.net/functions/find-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel REGEXTEST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_regextest_function.png "Excel REGEXTEST function")

Summary
-------

The Excel REGEXTEST function tests for the existence of text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable pattern. The result from REGEXTEST is TRUE or FALSE.

> The REGEXTEST function is only available in Excel 365 for now.

Purpose 
--------

Test a value for a specific pattern of text

Return value 
-------------

TRUE or FALSE

Syntax
------

    =REGEXTEST(text,pattern,[case_sensitivity])

*   _text_ - The text value to test.
*   _pattern_ - The pattern to test for.
*   _case\_sensitivity_ - \[optional\] 0 = Case sensitive, 1= Case-insensitive. Default is 0.

Using the REGEXTEST function 
-----------------------------

The REGEXTEST function provides a way to test for specific text defined by a "regex" pattern. The result from REGEXTEST is TRUE or FALSE. You can think of REGEXTEST as a major upgrade to simpler functions like FIND and SEARCH, which can be used to [test a cell for specific text](https://exceljet.net/formulas/cell-contains-specific-text)
. While these functions can perform primitive tests – FIND is case-sensitive but does not support wildcards, SEARCH supports wildcards but is not case-sensitive – they are no match for REGEXTEST, which can define tests using the full power of regular expressions. With regex, you can easily test for numbers, upper and lower case letters, exact quantities of certain characters, and for specific character sequences that follow a pattern.

> [Regular expressions](https://exceljet.net/articles/regular-expressions-in-excel)
>  ("regex" for short) are a powerful tool for pattern matching and text manipulation. Regex patterns can match simple strings or very specific sequences like phone numbers, email addresses, dates, and other text that has an identifiable pattern. Compared to the simple [wildcards](https://exceljet.net/glossary/wildcard)
>  provided in older versions of Excel, regular expressions are a _huge_ upgrade in functionality. They make it possible to match text in extremely specific ways that were impossible before now. While regex itself can be intimidating to new users, it's a very powerful language. As you become more comfortable with the syntax, you can tackle increasingly complex data challenges.

### Code example

To use REGEXTEST, provide text and a pattern. For example, the formulas below show how REGEXTEXT can be used to test the text in A1 for a number or an uppercase character:

    =REGEXTEST(A1,"[0-9]") // test for a number
    =REGEXTEST(A1,"[A-Z]") // test for an uppercase character

REGEXTEST returns TRUE or FALSE. If we use REGEXTEST to test for "a" in "apple", it returns TRUE:

    =REGEXTEST("apple","a") // returns TRUE

If we use REGEXTEST to test "apple" for a single digit between 0-9, it returns FALSE:

    =REGEXTEST("apple","[0-9]") // returns FALSE

### Worksheet example

The worksheet below uses REGEXTEST to test the same string, "1apple23#z", with twelve different patterns. In each formula, the text string comes from column B, and the pattern comes from column D. The formula in cell F5, copied down, is:

    =REGEXTEST(B5,D5)

![REGEXTEST function - basic examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_regextest_function_basic_examples.png "REGEXTEST function - basic examples")

Let's review the formulas one by one. Note that the formulas below use literal strings instead of cell references for readability. In each case, the text being tested remains the same; only the pattern varies.

    =REGEXTEST("1apple23#z","apple") // returns TRUE

REGEXTEST returns TRUE because the literal string "apple" appears in the text. Note that REGEXTEST automatically performs a "contains" type search.

    =REGEXTEST("1apple23#z","a") // returns TRUE

REGEXTEST returns TRUE because the literal string "a" appears in the text.

    =REGEXTEST("1apple23#z","A") // returns FALSE

REGEXTEST returns FALSE because it is case-sensitive by default, and the text does not contain an uppercase "A."

    =REGEXTEST("1apple23#z","^1") // returns TRUE

REGEXTEST returns TRUE because the text string "1apple23#z" begins with a "1". The caret (^) is a metacharacter that matches the _beginning_ of a text string.

    =REGEXTEST("1apple23#z","^a") // returns FALSE

REGEXTEST returns FALSE because the text does not begin with "a".

    =REGEXTEST("1apple23#z","Z$") // returns FALSE

REGEXTEST returns FALSE because the text does not end with an uppercase "Z". The dollar ($) is a metacharacter that matches the _end_ of a text string.

    =REGEXTEST("1apple23#z","[zZ]$") // returns TRUE

REGEXTEST returns TRUE because the text ends with "z" and the pattern "\[zZ\]$" matches "z" or "Z" at the end of the text.

    =REGEXTEST("1apple23#z","[A-Z]") // returns FALSE

REGEXTEST returns FALSE because the text contains no uppercase character between "A" and "Z".

    =REGEXTEST("1apple23#z","[0-9]") // returns TRUE

REGEXTEST returns TRUE because the text contains the digit "1". The pattern "\[0-9\]" matches any single digit between 0 and 9 anywhere in the text string.

    =REGEXTEST("1apple23#z","[0-9]{2}") // returns TRUE

REGEXTEST returns TRUE because the text contains a two-digit number where each digit is between 0-9. The curly-brace syntax "{n}" specifies how many instances of a character must be present in the input for a match. The pattern "\[0-9\]{2}" means exactly two digits, each between 0-9.

    =REGEXTEST("1apple23#z","[0-9]{3}") // returns FALSE

REGEXTEST returns FALSE because the text does not contain a three-digit number, even though it does contain three digits.

    =REGEXTEST("1apple23#z","[[:punct:]]") // returns TRUE
    

REGEXTEST returns TRUE because the text contains the punctuation "#". The pattern "\[:punct:\]" matches a punctuation character like \[!"#$%&'()\*+,\\-./:;<=>?@\[\\\]^\_\`{|}~\] in the text.

### Alternation in Regex (OR Logic)

One problem you'll often encounter in regex is how to test for this or that within the same pattern. Alternation in regex allows you to check for multiple possibilities by using the pipe (|) symbol, which works like a logical "OR". By grouping alternatives within parentheses, you can match one of several patterns in a test string. For example, in the worksheet below, we want to test addresses for one of four US states: MN, MT, ND, and SD. The formula in D5, copied down, looks like this:

    =REGEXTEST(B5,"\b(MN|MT|ND|SD)\b")

![REGEXTEST function - alternation example (OR logic)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_regextest_function_alternation_example.png "REGEXTEST function - alternation example (OR logic)")

The \\b symbol is a word boundary to ensure that only standalone instances of these abbreviations are matched.

### Regex terminology and reference

Because Regex is essentially a mini programming language, it has its own vocabulary. Here is a list of some important terminology:

*   **Pattern** - The actual sequence of characters that defines the regex.
*   **Literal** - Characters in a regex pattern that match themselves. For example, in `cat`, the literals are `c`, `a`, and `t`.
*   **Metacharacter** - Characters with special meanings in regex. For example, a period `.` matches any character, `^` matches the start of a string, `$` matches the end of a string.
*   **Character Class** - A set of characters enclosed in square brackets `[]` that matches any one of the characters inside. For example, `[aeiou]` matches any vowel.
*   **Quantifier** - Specifies how many instances of a character, group, or character class must be present in the input for a match. For example, `a*` matches zero or more a's, `a+` matches one or more a's, `a{3}` matches exactly three a's.

> For details and more examples of useful regex patterns, see our [Regex Reference Guide](https://exceljet.net/articles/regular-expressions-in-excel#regex-quick-reference)
> .

REGEXTEST function examples
---------------------------

[![Excel formula: Validate strong password](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/validate_strong_password.png "Excel formula: Validate strong password")](https://exceljet.net/formulas/validate-strong-password)

### [Validate strong password](https://exceljet.net/formulas/validate-strong-password)

In this example, the goal is to check for "strong" passwords. What makes a password strong depends on the rules it must follow. In this case, a strong password must meet the following six conditions: At least 8 and not more than 15 characters long Contains at least one uppercase (A-Z) letter...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

Related functions
-----------------

[![Excel REGEXEXTRACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexextract_function.png "Excel REGEXEXTRACT function")](https://exceljet.net/functions/regexextract-function)

### [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)

The Excel REGEXEXTRACT function extracts matching text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXEXTRACT will return the first match, but...

[![Excel REGEXREPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexreplace_function.png "Excel REGEXREPLACE function")](https://exceljet.net/functions/regexreplace-function)

### [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)

The Excel REGEXREPLACE function replaces text matching a specific regex pattern in a given text string. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXREPLACE will...

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Validate strong password](https://exceljet.net/formulas/validate-strong-password)
    

### Functions

*   [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)
    
*   [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

### Articles

*   [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
    

### Links

*   [Microsoft REGEXTEST documentation](https://support.microsoft.com/en-us/office/regextest-function-7d38200b-5e5c-4196-b4e6-9bff73afbd31)
    

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