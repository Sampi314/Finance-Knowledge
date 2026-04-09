# Excel REGEXEXTRACT function | Exceljet

**Source:** https://exceljet.net/functions/regexextract-function

---

[Skip to main content](https://exceljet.net/functions/regexextract-function#main-content)

[](https://exceljet.net/functions/regexextract-function#)

*   [Previous](https://exceljet.net/functions/reduce-function)
    
*   [Next](https://exceljet.net/functions/regexreplace-function)
    

Excel 365

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

REGEXEXTRACT Function
=====================

by Dave Bruns · Updated 28 Aug 2025

Related functions 
------------------

[REGEXTEST](https://exceljet.net/functions/regextest-function)

[REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)

![Excel REGEXEXTRACT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_regexextract_function.png "Excel REGEXEXTRACT function")

Summary
-------

The Excel REGEXEXTRACT function extracts matching text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXEXTRACT will return the first match, but it can be configured to return all matches.

> The REGEXEXTRACT function is only available in Excel 365 for now.

Purpose 
--------

Extract text with regex pattern

Return value 
-------------

Text matching pattern

Syntax
------

    =REGEXEXTRACT(text,pattern,[return_mode],[case_sensitivity])

*   _text_ - The text value to extract from.
*   _pattern_ - The pattern to extract.
*   _return\_mode_ - \[optional\] 0 = first match, 1 = all matches, 2 = capture groups.
*   _case\_sensitivity_ - \[optional\] 0 = Case sensitive, 1= Case-insensitive. Default is 0.

Using the REGEXEXTRACT function 
--------------------------------

The REGEXEXTRACT function extracts text matching a specific regex pattern from a given text string. For the advanced Excel user, this function is a _major_ upgrade. Instead of working out complex formulas based on functions like LEFT, RIGHT, FIND, MID, etc., REGEXEXTRACT can target data very precisely with a single regex pattern. With REGEXEXTRACT, you can easily extract numbers, dates, times, email addresses, and other text with a recognizable structure. REGEXEXTRACT not only saves time but also reduces errors created by complicated workarounds.

> [Regular expressions](https://exceljet.net/articles/regular-expressions-in-excel)
>  ("regex" for short) are a powerful tool for pattern matching and text manipulation. Regex patterns can match simple strings or very specific sequences like phone numbers, email addresses, dates, and other text that has an identifiable pattern. Compared to the simple [wildcards](https://exceljet.net/glossary/wildcard)
>  provided in older versions of Excel, regular expressions are a _huge_ upgrade in functionality. They make it possible to match text in extremely specific ways that were impossible before now. While regex itself can be daunting to newcomers, it's a very powerful language. As you become more comfortable with the syntax, you can tackle increasingly complex data extraction challenges.

### Table of Contents

*   [Example - Extracting numbers](https://exceljet.net/functions/regexextract-function#example-extracting-numbers)
    
*   [Example - Extracting phone numbers](https://exceljet.net/functions/regexextract-function#example-extracting-phone-num)
    
*   [Example - Extracting email addresses](https://exceljet.net/functions/regexextract-function#example-extracting-email-add)
    
*   [Example - Extracting dates](https://exceljet.net/functions/regexextract-function#example-extracting-dates)
    
*   [Example - Extract all hashtags](https://exceljet.net/functions/regexextract-function#example-extract-all-hashtags)
    
*   [Example - Capturing groups](https://exceljet.net/functions/regexextract-function#example-capturing-groups)
    
*   [Regex terminology and reference](https://exceljet.net/functions/regexextract-function#regex-terminology-and-reference)
    

### Example - Extracting numbers

The REGEXEXTRACT function provides a way to extract text values using regular expressions. To use REGEXEXTRACT, provide the text string to extract from and a regex pattern. For example, to extract a number from a text string, you can use REGEXEXTRACT with a pattern like "\[0-9\]+":

    =REGEXEXTRACT("10 apples","[0-9]+") // returns "10"

You can see how this works in the worksheet below, where the formula in cell D5, copied down, is:

    =REGEXEXTRACT(B5,"[0-9]+")

![Regexextract example - extract numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexextract_example_-_extract_number.png "Regexextract example - extract numbers")

The pattern "\[0-9\]+" means "match one or more characters, where each character is a digit from 0 to 9":

*   Square brackets \[ \]: - In regex, square brackets define a character set. They mean "match any single character that is inside these brackets."
*   0-9: - This is a range that includes all digits from 0 to 9. It's a shorthand way of writing \[0123456789\].
*   The plus sign +: The "+" is a quantifier that means "one or more of the preceding element." In this case, it applies to the range \[0-9\].

In practice, this pattern will:

*   Match any sequence of one or more digits.
*   Match the entire number, not just a single digit.
*   Not match decimal points, negative signs, or any non-digit characters.

Note that you can also match one or more digits with the more compact pattern "\\d+". The "\\d" is a character class representing digits, so "\\d+" also means "one or more digits".

> Note that if a number is not found in the text, REGEXEXTRACT will return a #N/A error.

### Example - Extracting phone numbers

Expanding on the example above, the worksheet below shows how to match and extract phone numbers in the format xxx-xxx-xxxx (i.e., a number like 888-123-1234) from text strings. The formula in cell D5, copied down, looks like this:

    =REGEXEXTRACT(B5,"\d{3}-\d{3}-\d{4}")

![Regexextract example - extract phone numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexextract_example_-_extract_phone_numbers.png "Regexextract example - extract phone numbers")

Here's how the pattern "\\d{3}-\\d{3}-\\d{4}" works:

*   The "\\d" matches any digit (0-9). "{3}" is a quantifier meaning "exactly 3 times". So "\\d{3}" matches exactly 3 digits.
*   The hyphen ("-") is a "literal" and matches a literal hyphen character.
*   As before, the pattern "\\d{3}" matches exactly 3 digits.
*   The ("-") matches a literal hyphen character.
*   The pattern "\\d{4}" matches exactly 4 digits.

### Example - Extracting email addresses

Another classic use of regex is matching and extracting email addresses. In the worksheet below, the formula in cell D5, copied down, is:

    =REGEXEXTRACT(B5, "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

This example shows how matching simple things like an email address can quickly become more complicated as the pattern expands to handle variations in format. You can see how it works in the worksheet below. Briefly, here's how it works:

*   The pattern "\[a-zA-Z0-9.\_%+-\]+@\[a-zA-Z0-9.-\]+\\.\[a-zA-Z\]{2,}" is designed to match the most common email address formats.
*   It begins with "\[a-zA-Z0-9.%+-\]+", which matches one or more characters that can be letters (both lowercase and uppercase), numbers, or certain special characters typically allowed in email usernames.
*   This is followed by a literal "@" symbol. After the "@", "\[a-zA-Z0-9.-\]+" matches one or more characters for the domain name, allowing letters, numbers, dots, and hyphens.
*   The "." matches a literal dot, which is followed by "\[a-zA-Z\]{2,}", matching two or more letters for the top-level domain (like .com, .org, etc.).

![Regexextract example - extract email addresses](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexextract_example_-_extract_email_addresses.png "Regexextract example - extract email addresses")

_Note: although this pattern covers most standard email formats while excluding many invalid ones, it doesn't capture all possible valid email addresses._

### Example - Extracting dates

Another classic problem in Excel is how to extract a date from a text string. Traditionally, you might use a formula based on the SEARCH function and the MID function like this:

    =MID(A1,SEARCH("??/??/??",A1),8)+0

However, SEARCH only supports Excel's very primitive wildcards, so the formula above is error-prone. With REGEXEXTRACT, we can use a more robust formula like this:

    =REGEXEXTRACT(A1,"\b\d{1,2}/\d{1,2}/\d{2,4}\b")+0

You can see how this works in the worksheet below:

![Regexextract example - extract dates from text strings](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexextract_example_-_extract_dates_from_text.png "Regexextract example - extract dates from text strings")

For a full explanation and sample worksheet, [see this page](https://exceljet.net/formulas/extract-date-from-text-string)
.

### Example - Extract all hashtags

The _return\_mode_ argument in REGEXEXTRACT defaults to zero (0), which will return only the _first match_. To return all matches, set this value to 1. You can see how this works in the worksheet below, where the formula in cell D5 is:

    =REGEXEXTRACT(B5,"#\w+",1)

With the _pattern_ "#\\w+", and _return\_type_ set to 1, REGEX will return all hashtags for each text string in column B.

![REGEXEXTRACT example - extract all hashtags](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexextract_example_-_extract_all_hashtags.png "REGEXEXTRACT example - extract all hashtags")

Multiple matches are returned in an array that spills to the right. If needed, you can use the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 to combine multiple values into a single text string.

### Example - Capturing groups

Capturing groups are a key concept in regular expressions (regex) that provide the ability to isolate and extract specific portions of a matched pattern. These groups are created by enclosing part of a regex pattern in parentheses (), which tells the regex engine to "capture" or remember the text matched by that particular section. REGEXEXTRACT provides basic support for capturing groups by setting the third argument, return\_mode, to 2. You can see how this works below, where the formula in cell D5 is:

    =REGEXEXTRACT(B5,"(\d{4})-(\w+)-(\w+)",2)

Note that we are using three sets of parentheses (), which create three capturing groups inside the pattern. The value for return\_mode is set to 2, which causes REGEXEXTRACT to return all three groups in an array that spills onto the worksheet:

![REGEXEXTRACT example - using capturing groups](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/regexextract_example_-_capturing_groups.png "REGEXEXTRACT example - using capturing groups")

### Regex terminology and reference

Because Regex is essentially a mini programming language, it has its own vocabulary. Here is a list of some important terminology:

*   **Pattern** - The actual sequence of characters that defines the regex.
*   **Literal** - Characters in a regex pattern that match themselves. For example, in `cat`, the literals are `c`, `a`, and `t`.
*   **Metacharacter** - Characters with special meanings in regex. For example, a period `.` matches any character, `^` matches the start of a string, `$` matches the end of a string.
*   **Character Class** - A set of characters enclosed in square brackets `[]` that matches any one of the characters inside. For example, `[aeiou]` matches any vowel.
*   **Quantifier** - Specifies how many instances of a character, group, or character class must be present in the input for a match. For example, `a*` matches zero or more a's, `a+` matches one or more a's, `a{3}` matches exactly three a's.

> For details and more examples of useful regex patterns, see our [Regex Reference Guide](https://exceljet.net/articles/regular-expressions-in-excel#regex-quick-reference)
> .

REGEXEXTRACT function examples
------------------------------

[![Excel formula: Extract date from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_date_from_text_string.png "Excel formula: Extract date from text string")](https://exceljet.net/formulas/extract-date-from-text-string)

### [Extract date from text string](https://exceljet.net/formulas/extract-date-from-text-string)

In this example, the goal is to extract a date in a format like mm/dd/yy from a text string with a formula. The position of the date is not known, so the date must be located as a first step. This article explains two ways to solve this challenge: A "classic" formula based on the SEARCH function...

[![Excel formula: Split text string to character array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_to_character_array_0.png "Excel formula: Split text string to character array")](https://exceljet.net/formulas/split-text-string-to-character-array)

### [Split text string to character array](https://exceljet.net/formulas/split-text-string-to-character-array)

In this example, the goal is to use a formula to split a text string into an array of characters. For example, if the text string is "Apple", the resulting array should be {"A","p","p","l","e"}. For a long time, this was quite a difficult problem that required a complicated array formula approach...

[![Excel formula: Get Unicode Sequence from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_unicode_sequence_of_text_main_0.png "Excel formula: Get Unicode Sequence from text")](https://exceljet.net/formulas/get-unicode-sequence-from-text)

### [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)

In this example, the goal is to convert each character in a text string into its corresponding Unicode code point and display the results as a space-separated sequence. This problem can be solved using several Excel functions working together to extract, convert, and format the Unicode values. The...

Related functions
-----------------

[![Excel REGEXTEST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regextest_function.png "Excel REGEXTEST function")](https://exceljet.net/functions/regextest-function)

### [REGEXTEST Function](https://exceljet.net/functions/regextest-function)

The Excel REGEXTEST function tests for the existence of text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable pattern. The result from REGEXTEST is TRUE or FALSE....

[![Excel REGEXREPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexreplace_function.png "Excel REGEXREPLACE function")](https://exceljet.net/functions/regexreplace-function)

### [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)

The Excel REGEXREPLACE function replaces text matching a specific regex pattern in a given text string. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXREPLACE will...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split text string to character array](https://exceljet.net/formulas/split-text-string-to-character-array)
    
*   [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)
    
*   [Extract date from text string](https://exceljet.net/formulas/extract-date-from-text-string)
    

### Functions

*   [REGEXTEST Function](https://exceljet.net/functions/regextest-function)
    
*   [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)
    

### Articles

*   [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
    

### Links

*   [Microsoft REGEXEXTRACT documentation](https://support.microsoft.com/en-us/office/regexextract-function-4b96c140-9205-4b6e-9fbe-6aa9e783ff57)
    

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