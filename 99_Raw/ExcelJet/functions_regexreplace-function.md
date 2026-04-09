# Excel REGEXREPLACE function | Exceljet

**Source:** https://exceljet.net/functions/regexreplace-function

---

[Skip to main content](https://exceljet.net/functions/regexreplace-function#main-content)

[](https://exceljet.net/functions/regexreplace-function#)

*   [Previous](https://exceljet.net/functions/regexextract-function)
    
*   [Next](https://exceljet.net/functions/regextest-function)
    

Excel 365

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

REGEXREPLACE Function
=====================

by Dave Bruns · Updated 17 Jun 2025

Related functions 
------------------

[REGEXTEST](https://exceljet.net/functions/regextest-function)

[REGEXEXTRACT](https://exceljet.net/functions/regexextract-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

![Excel REGEXREPLACE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_regexreplace_function.png "Excel REGEXREPLACE function")

Summary
-------

The Excel REGEXREPLACE function replaces text matching a specific regex pattern in a given text string. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXREPLACE will replace all matching text, but it can be configured to replace a specific instance.

> The REGEXREPLACE function is only available in Excel 365 for now.

Purpose 
--------

Replace text with a regex pattern

Return value 
-------------

Text after all replacements

Syntax
------

    =REGEXREPLACE(text,pattern,replacement,[occurrence],[case_sensitivity])

*   _text_ - The text value to process.
*   _pattern_ - The pattern to replace.
*   _replacement_ - The text to replace with.
*   _occurrence_ - \[optional\] The instance to replace. Default = 0 = all instances.
*   _case\_sensitivity_ - \[optional\] 0 = Case sensitive, 1= Case-insensitive. Default is 0.

Using the REGEXREPLACE function 
--------------------------------

The REGEXREPLACE function replaces text matching a specific regex pattern in a given text string. You can think of REGEXREPLACE as a much more powerful version of the simplistic [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. While both functions can be used to search and replace simple text strings, REGEXREPLACE can use regex, a powerful language built for matching and manipulating text values. This function is a major upgrade to Excel's rather primitive text functions.

> [Regular expressions](https://exceljet.net/articles/regular-expressions-in-excel)
>  ("regex" for short) are a powerful tool for pattern matching and text manipulation. Regex patterns can match simple strings or very specific sequences like phone numbers, email addresses, dates, and other text that has an identifiable pattern. Compared to the simple [wildcards](https://exceljet.net/glossary/wildcard)
>  provided in older versions of Excel, regular expressions are a _huge_ upgrade in functionality. They make it possible to match text in extremely specific ways that were impossible before now. While regex itself can be daunting to newcomers, it's a very powerful language. As you become more comfortable with the syntax, you can tackle increasingly complex data extraction challenges.

### Table of Contents

*   [Example - Basic usage](https://exceljet.net/functions/regexreplace-function#example---basic-usage)
    
*   [Example - Strip non-numeric characters](https://exceljet.net/functions/regexreplace-function#example---strip-non-numeric-characters)
    
*   [Example - capitalize first letter in text string](https://exceljet.net/functions/regexreplace-function#example---capitalize-first-letter-in-text-string)
    
*   [Example - capitalize specific words](https://exceljet.net/functions/regexreplace-function#example--%20capitalize-specific-words)
    
*   [Example - Format telephone numbers with grouping](https://exceljet.net/functions/regexreplace-function#example--%20-format-telephone-numbers-with-grouping)
    
*   [Example - combining multiple REGEXREPLACE functions](https://exceljet.net/functions/regexreplace-function#example--%20combining-multiple-regexreplace-functions)
    
*   [Regex terminology and reference](https://exceljet.net/functions/regexreplace-function#regex-terminology-and-reference)
    

### Example - Basic usage

To use REGEXREPLACE, provide a text string, a regex pattern, and the replacement text. For example, to replace "t" with "b" in the text string "tuttle", you can use a formula like this:

    =REGEXREPLACE("tuttle","t","b") // returns "bubble"

The formula replaces all three instances of "t" with "b". Note that REGEXREPLACE is case-sensitive by default. If we capitalize the first "t", only the second and third occurrences of "t" are changed:

    =REGEXREPLACE("Tuttle","t","b") // returns "Tubble"

To disable case sensitivity, provide a 1 for the case-sensitive argument:

    =REGEXREPLACE("Tuttle","t","b",,1) // returns "bubble"

With case sensitivity disabled, all three "t"s are replaced with "b". Another way to replace both "T" and "t" with "b" is to include both in a regex character set like this:

    =REGEXREPLACE("Tuttle","[Tt]","b") // returns "bubble"

### Example - Strip non-numeric characters

The REGEXREPLACE function provides an easy way to remove non-numeric characters from a text string. You can see an example below, where REGEXREPLACE is configured to remove all space and punctuation from the (fake) telephone numbers in column B. The formula in cell D5, copied down, is:

    =REGEXREPLACE(B5,"[^0-9]","")

![REGEXREPLACE example - strip non-numeric characters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexreplace_example_-_strip_non-numeric_characters.png "REGEXREPLACE example - strip non-numeric characters")

The arguments in REGEXREPLACE are configured like this:

*   text - from cell B5
*   pattern - "\[^0-9\]"
*   replacement - "" (an empty string)

The pattern "\[^0-9\]" breaks down like this:

*   Square brackets \[ \]: - In regex, square brackets define a character set. They mean "match any single character that is inside these brackets."
*   Caret ^: When used inside \[\], it means "not"
*   0-9: - A range that includes all digits from 0 to 9. It's a shorthand way of writing \[0123456789\].

The result is that the pattern will match any character that is _not a digit_. With this pattern, REGEXREPLACE will replace any character that is not a digit with an empty string. The final result contains digits only.

> Note that if the pattern is not found in the text, REGEXEXTRACT will return the original value.

### Example - capitalize first letter in text string

REGEXREPLACE can perform certain transformations, for example making text upper or lower case. You can see an example of how this works in the worksheet below, where REGEXREPLACE is used to capitalize the first letter in a text string. The formula in cell D5 is:

    =REGEXREPLACE(B5,"^(.)","\U$1")

![REGEXREPLACE example - capitalize first letter](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexreplace_example_-_capitalize_first_letter.png "REGEXREPLACE example - capitalize first letter")

The arguments in REGEXREPLACE are configured as follows:

*   text - B5
*   pattern - "^(.)".
*   replacement - "\\U$1"

In the pattern, "^" means the start of the string, and "." means any single character. The parentheses () define a capturing group. The full pattern "^(.)" captures any single character at the beginning of the text in a group. In the replacement, "\\U" means convert to uppercase, and "$1" refers to the first (and only) captured group. So, the formula finds the first character of the text in B5 and replaces it with its uppercase version, effectively capitalizing the first letter of the text.

### Example - capitalize specific words

We can extend the idea in the example above to use REGEXREPLACE to capitalize specific words in a text string. In the worksheet below, REGEXREPLACE is configured to capitalize "cat", "bird", and "dog", including the pluralized versions of these words. The formula in cell D5 looks like this:

    =REGEXREPLACE(B5,"\b((cat|dog|bird)s?)\b","\U$1",,1)

![REGEXREPLACE example - capitalize specific words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexreplace_example_-_capitalize_specific_words.png "REGEXREPLACE example - capitalize specific words")

The arguments are provided as follows:

*   _text_ - from cell B5
*   _pattern_ - "\\b((cat|dog|bird)s?)\\b"
*   _replacement_ - "\\U$1"
*   _occurrence_ - omitted
*   _case\_sensitivity_ - 1 (to disable case sensitivity)

This formula will capitalize both singular and plural forms of "cat", "dog", and "bird", regardless of their original capitalization.

*   In the pattern "\\b((cat|dog|bird)s?)\\b", "\\b" is a word boundary to ensure we match whole words only. The partial pattern "(cat|dog|bird)" matches "cat" or "dog" or "bird". The parentheses define a capturing group. The full pattern "((cat|dog|bird)s?)" matches "cat", "dog", or "bird", optionally followed by "s". Note we have a second pair of parentheses that defines a capturing group for the entire match, including the optional "s".
*   The replacement pattern is "\\U$1". The "\\U" is an uppercase operator. The "$1" is the first capturing group. The capturing groups are numbered from left to right based on the order of their opening parentheses, so the "outer" group is the first and includes the optional "s".
*   Note that we have omitted _occurrence_ since it is not needed (extra blank comma), and _case\_sensitivity_ is set to 1 to disable the default case sensitivity of REGEXREPLACE. We do this so that REGEXREPLACE will ignore the case when looking for words.

### Example - Format telephone numbers with grouping

In the worksheet below, we are using REGEXREPLACE to format telephone numbers that were previously "cleaned" by removing all non-numeric characters (see the example above for details). The formula in cell F5 looks like this:

    =REGEXREPLACE(D5,"(\d{3})(\d{3})(\d{4})","($1)-$2-$3")

![REGEXREPLACE example -  format telephone numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexreplace_example_-__format_telephone_numbers.png "REGEXREPLACE example -  format telephone numbers")

The arguments to REGEXREPLACE are configured like this:

*   _text_ - from cell D5
*   _pattern_ - "(\\d{3})(\\d{3})(\\d{4})"
*   _replacement_ - "($1)-$2-$3"

Note that we are working with previously "cleaned" phone numbers in column D. These are 10-digit numbers with all punctuation and white space removed (see above for details).

*   The regex _pattern_ is "(\\d{3})(\\d{3})(\\d{4})". The first part (\\d{3}) captures the first three digits, the second part (\\d{3}) captures the next three digits, and the third part (\\d{4}) captures the last four digits. Note that the three pairs of parentheses define three capturing groups.
*   The replacement pattern is "($1)-$2-$3", which uses all three groups. ($1) puts parentheses around the first group, -$2- adds hyphens before and after the second group, and $3 adds the last group.
*   The result is that a number like "0234568765" becomes "(023)-456-8765".

This formula will work for 10-digit phone numbers. If you need to handle different lengths or formats, you will need to adjust the regular expression accordingly.

### Example - combining multiple REGEXREPLACE functions

In the examples above, we used two separate REGEXREPLACE formulas, one to strip out non-numeric characters and one to format the remaining digits. Excel makes it easy to combine these two formulas together by nesting the first REGEXREPLACE inside the second. You can see how this works in the worksheet below, where the formula in D5 is:

    =REGEXREPLACE(REGEXREPLACE(B5,"[^0-9]",""),"(\d{3})(\d{3})(\d{4})","($1)-$2-$3")

![Combining multiple REGEXREPLACE functions together](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexreplace_example_-_combining_multiple_regexreplace.png "Combining multiple REGEXREPLACE functions together")

The inner REGEXREPLACE removes punctuation and whitespace and returns a cleaned phone number to the outer REGEXREPLACE, which formats the final result. Solving problems this way is a good approach because each formula can be developed and tested separately, and neither formula is especially complex. While it would be possible to do everything in a single REGEXREPLACE formula, the regex would be significantly more complex.

### Regex terminology and reference

Because Regex is essentially a mini programming language, it has its own vocabulary. Here is a list of some important terminology:

*   **Pattern** - The actual sequence of characters that defines the regex.
*   **Literal** - Characters in a regex pattern that match themselves. For example, in `cat`, the literals are `c`, `a`, and `t`.
*   **Metacharacter** - Characters with special meanings in regex. For example, a period `.` matches any character, `^` matches the start of a string, `$` matches the end of a string.
*   **Character Class** - A set of characters enclosed in square brackets `[]` that matches any one of the characters inside. For example, `[aeiou]` matches any vowel.
*   **Quantifier** - Specifies how many instances of a character, group, or character class must be present in the input for a match. For example, `a*` matches zero or more a's, `a+` matches one or more a's, `a{3}` matches exactly three a's.

> For details and more examples of useful regex patterns, see our [Regex Reference Guide](https://exceljet.net/articles/regular-expressions-in-excel#regex-quick-reference)
> .

REGEXREPLACE function examples
------------------------------

[![Excel formula: Find and replace multiple values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find-and-replace-multiple-values.png "Excel formula: Find and replace multiple values")](https://exceljet.net/formulas/find-and-replace-multiple-values)

### [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)

There is no built-in function to perform a series of find and replace operations in Excel, but you can create a formula that does the same thing. The goal in this example is to replace multiple ("find") values with corresponding ("replace") values in a single "replace all" operation. The text...

[![Excel formula: Convert text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert_text_to_numbers.png "Excel formula: Convert text to numbers")](https://exceljet.net/formulas/convert-text-to-numbers)

### [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)

In this example, the goal is to convert the text values seen in column B to the numeric values seen in column D. There are several ways to fix this problem in Excel, but this article focuses on a formula-based approach to convert text values to numbers. It also explains how to convert values in...

[![Excel formula: Remove characters from right](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_characters_from_right.png "Excel formula: Remove characters from right")](https://exceljet.net/formulas/remove-characters-from-right)

### [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)

In this example, the goal is to remove the asterisk (\*) at the end of each text city/country name in column B. As usual, there are many ways to solve a problem like this in Excel. In the article below, we'll look at two good options. The first is a traditional formula based on the LEFT function and...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

Related functions
-----------------

[![Excel REGEXTEST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regextest_function.png "Excel REGEXTEST function")](https://exceljet.net/functions/regextest-function)

### [REGEXTEST Function](https://exceljet.net/functions/regextest-function)

The Excel REGEXTEST function tests for the existence of text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable pattern. The result from REGEXTEST is TRUE or FALSE....

[![Excel REGEXEXTRACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexextract_function.png "Excel REGEXEXTRACT function")](https://exceljet.net/functions/regexextract-function)

### [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)

The Excel REGEXEXTRACT function extracts matching text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXEXTRACT will return the first match, but...

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)
    
*   [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)
    

### Functions

*   [REGEXTEST Function](https://exceljet.net/functions/regextest-function)
    
*   [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

### Articles

*   [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
    

### Links

*   [Microsoft REGEXREPLACE documentation](https://support.microsoft.com/en-us/office/regexreplace-function-9c030bb2-5e47-4efc-bad5-4582d7100897)
    

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