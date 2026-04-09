# Excel REPLACE function | Exceljet

**Source:** https://exceljet.net/functions/replace-function

---

[Skip to main content](https://exceljet.net/functions/replace-function#main-content)

[](https://exceljet.net/functions/replace-function#)

*   [Previous](https://exceljet.net/functions/proper-function)
    
*   [Next](https://exceljet.net/functions/rept-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

REPLACE Function
================

by Dave Bruns · Updated 23 Jan 2026

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[FIND](https://exceljet.net/functions/find-function)

[REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)

![Excel REPLACE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20replace%20function.png "Excel REPLACE function")

Summary
-------

The Excel REPLACE function replaces characters at a specified position in a given text string with another text string. REPLACE a good solution when the text to replace can't easily be matched, but the location is predictable.

Purpose 
--------

Replace text based on location

Return value 
-------------

The altered text.

Syntax
------

    =REPLACE(old_text,start_num,num_chars,new_text)

*   _old\_text_ - The text to replace.
*   _start\_num_ - The starting location in the text to search.
*   _num\_chars_ - The number of characters to replace.
*   _new\_text_ - The text to replace old\_text with.

Using the REPLACE function 
---------------------------

The REPLACE function replaces text at a specific location inside a text string. The location of the text to replace is given as a number representing the _first character_ to replace, along with a character count to indicate _how many characters_ to replace. Unlike [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
, which replaces text by _matching_ content, REPLACE works by _position_ and _character count_. REPLACE is ideal in cases where the text to replace can't easily be matched, but the location is predictable.

### Key features

*   Works by position, not by matching text content
*   Is _not_ case-sensitive and _does not_ support wildcards
*   Useful when the text to replace has many variations
*   Will accept an empty string ("") to remove text completely
*   Works in all versions of Excel

> You can't use the REPLACE function by itself to "find and replace" text — it works at a more granular level and swaps text based on _position only_. For basic find and replace tasks, see the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
> . For true pattern matching, see the [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
>  (Excel 365).

### Table of contents

*   [Example #1 - Basic usage](https://exceljet.net/functions/replace-function#basic_usage)
    
*   [Example #2 - Replace different text at same location](https://exceljet.net/functions/replace-function#replace_text_same_location)
    
*   [Example #3 - Change first letter](https://exceljet.net/functions/replace-function#change_first_letter)
    
*   [Example #4 - Remove first characters](https://exceljet.net/functions/replace-function#remove_first_characters)
    
*   [Example #5 - Conditionally remove text](https://exceljet.net/functions/replace-function#conditionally_remove_text)
    
*   [Example #6 - Capitalized first letter](https://exceljet.net/functions/replace-function#capitalize_first_letter)
    
*   [Example #7 - Mask credit card numbers](https://exceljet.net/functions/replace-function#mask_credit_card_numbers)
    
*   [Related functions](https://exceljet.net/functions/replace-function#related_functions)
    

### Example #1 - Basic usage

REPLACE function takes four separate [arguments](https://exceljet.net/glossary/function-argument)
 in a generic syntax like this:

    =REPLACE(old_text,start_num,num_chars,new_text)

The first argument, _old\_text_, is the text string to be processed. The second argument, _start\_num_, specifies the numeric position where replacement should begin. The third argument, _num\_chars_, indicates how many characters to replace. The final argument, _new\_text_, provides the replacement text. You can see how these arguments work in the formulas below:

    =REPLACE("C:\docs",1,1,"D") // returns "D:\docs"
    =REPLACE("ABC123",4,3,"456") // returns "ABC456"
    =REPLACE("XYZ",1,1,"") // returns "YZ"
    =REPLACE("www.google.com",1,4,"") // returns "google.com"

1.  Replace "C" at the start of the path with "D".
2.  Replace 3 characters starting at the 4th character ("123" to "456").
3.  Replace the "X" at the start with nothing ("X" to "").
4.  Remove the first 4 characters ("www." to "")

### Example #2 - Replace different text at same location

In the example below, the goal is to replace the year values in the middle of the text strings in column B with the year 2025. This is a scenario where the REPLACE function shines. Instead of matching the various year values (as with a function like SUBSTITUTE), we can simply tell replace to replace 4 characters starting at character 5. The formula in cell D5. copied down, looks like this:

    =REPLACE(B5,5,4,"2025")

![REPLACE example - replace different values at the same location](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/replace_example_-_replace_different_text_at_same_location.png "REPLACE example - replace different values at the same location")

### Example #3 - Change first letter

In the worksheet below, the goal is to change the first letter of each path in column B to the letter "Z". This is another good use case for the REPLACE function because the text we want to change is always fixed at character one, even though it is different in each case. The formula in D5 copied down is:

    =REPLACE(B5,1,1,"Z")

![REPLACE example - change first letter in each path to "Z"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/replace_example_-_change_first_letter.png "REPLACE example - change first letter in each path to "Z"")

> Notice this is a [spill range](https://exceljet.net/glossary/spill-range)
>  example. Because we give the REPLACE function 12 values in the range B5:B16 for _old\_text_, it returns 12 results that spill into the range D5:D16. 

### Example #4 - Remove first characters

The REPLACE function can be used to remove text by providing an empty string ("") for the _new\_text_ argument. In the example below, the goal is to strip the "www." from each domain name in column B. The formula in cell D5, copied down, looks like this:

    =REPLACE(B5,1,4,"")

![REPLACE example - remove "www." from each domain name](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/replace_example_-_remove_first_characters.png "REPLACE example - remove "www." from each domain name")

Notice we use 1 for _start\_num_ and 4 for _num\_chars_, since the text string "www." contains 4 characters and always starts at character 1. You may need to change these inputs depending on your use case.

### Example #5 - Conditionally remove text

In the example below, we have the same problem as above, except the www isn't always present. This means we need to check for the presence of these characters before we remove them. Otherwise, we'll remove characters we don't want to remove. There are a variety of ways to do this in Excel. In the formula below, we're using the LEFT function inside the IF function to perform this check. The formula in cell D5 looks like this:

    =IF(LEFT(B5,4)="www.",REPLACE(B5,1,4,""),B5)

![REPLACE example - remove "www." only when it actually exists!](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/replace_example_-_conditionally_remove_text.png "REPLACE example - remove "www." only when it actually exists!")

> Note: In a current version of Excel, you can also use the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
>  to solve this problem and the previous problem.

### Example #6 - Capitalized first letter

It is possible to combine the REPLACE function with other functions that do more sophisticated text manipulation. For example, in the worksheet below, we use the REPLACE function together with the [UPPER](https://exceljet.net/functions/upper-function)
 and [LEFT](https://exceljet.net/functions/left-function)
 functions to capitalize the text strings in column B. The formula in cell D5 copied down is:

    =REPLACE(B5,1,1,UPPER(LEFT(B5)))

![REPLACE example - capitalize first letter in text string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/replace_example_-_capitalized_first_letter.png "REPLACE example - capitalize first letter in text string")

[This page](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)
 explains this formula in more detail and provides some alternatives.

### Mask credit card numbers

In the worksheet below, the goal is to mask credit card numbers so that only the last four digits are visible. This is accomplished by combining the REPLACE function with the [LEN](https://exceljet.net/functions/len-function)
 and [REPT](https://exceljet.net/functions/rept-function)
 functions in a clever formula like this in cell D5:

    =REPLACE(B5,1,LEN(B5)-4,REPT("*",LEN(B5)-4))

![REPLACE example - mask credit card numbers to how only last 4 digits](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/replace_example_-_mask_credit_card_numbers.png "REPLACE example - mask credit card numbers to how only last 4 digits")

The start number is always 1. To work out the number of characters to replace, we calculate the length of the text string, then subtract 4 to account for the numbers we don't want to replace: `LEN(B5)-4`. To generate the replacement text, we use the REPT function configured to repeat an asterisk (\*) once for each number we are replacing, like this: `REPT("*",LEN(B5)-4)`.

### Related functions

Excel contains several functions that can help you find and replace text:

*   [REPLACE](https://exceljet.net/functions/replace-function)
     – Replace text by position when you know the starting point.
*   [FIND](https://exceljet.net/functions/find-function)
     / [SEARCH](https://exceljet.net/functions/search-function)
     – Find the numeric position of text.
*   [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
     - replace text with simple matching.
*   [REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)
     – Pattern‑based find and replace (Excel 365 only).

### Notes

*   To remove text, use an empty string ("") for _new\_text_.
*   REPLACE returns #VALUE is _start\_num_ or _num\_chars_ is not a positive number.
*   REPLACE works on numbers, but the result is text.

REPLACE function examples
-------------------------

[![Excel formula: Remove first character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20first%20character.png "Excel formula: Remove first character")](https://exceljet.net/formulas/remove-first-character)

### [Remove first character](https://exceljet.net/formulas/remove-first-character)

This formula uses the REPLACE function to replace the first character in a cell with an empty string (""). The arguments for REPLACE are configured as follows: old\_text is the original value from column B start\_num is hardcoded as the number 1 num\_chars comes from column C new\_text is entered as an...

[![Excel formula: Remove text by variable position](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20variable%20position.png "Excel formula: Remove text by variable position")](https://exceljet.net/formulas/remove-text-by-variable-position)

### [Remove text by variable position](https://exceljet.net/formulas/remove-text-by-variable-position)

The REPLACE function will replace text by position. You can use REPLACE to remove text by providing an empty string ("") for the "new\_text" argument. In this case, we want to remove the labels that appear inside text. The labels vary in length, and include words like "Make", "Model", "Fuel economy...

[![Excel formula: Remove text by position](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20position.png "Excel formula: Remove text by position")](https://exceljet.net/formulas/remove-text-by-position)

### [Remove text by position](https://exceljet.net/formulas/remove-text-by-position)

The replace function lets you replace text based on its location and length. In this case, we want to strip off the drive and path and leave only the document name. The length of this part of the string (text) is 24 and the starting position is 1, and the pattern never changes. The REPLACE function...

[![Excel formula: Remove characters from right](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_characters_from_right.png "Excel formula: Remove characters from right")](https://exceljet.net/formulas/remove-characters-from-right)

### [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)

In this example, the goal is to remove the asterisk (\*) at the end of each text city/country name in column B. As usual, there are many ways to solve a problem like this in Excel. In the article below, we'll look at two good options. The first is a traditional formula based on the LEFT function and...

[![Excel formula: Capitalize first letter in a text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/capitalize_first_letter.png "Excel formula: Capitalize first letter in a text string")](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)

### [Capitalize first letter in a text string](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)

One of the most important skills to learn with Excel formulas is the concept of nesting. Put simply, nesting just means putting one function inside another. Nesting is super useful, but it does take some practice. You have to learn to read a formula from the inside out. The formulas below are good...

Related functions
-----------------

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

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

*   [Remove text by position](https://exceljet.net/formulas/remove-text-by-position)
    
*   [Remove characters from right](https://exceljet.net/formulas/remove-characters-from-right)
    
*   [Capitalize first letter in a text string](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)
    
*   [Remove first character](https://exceljet.net/formulas/remove-first-character)
    
*   [Remove text by variable position](https://exceljet.net/formulas/remove-text-by-variable-position)
    

### Functions

*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)
    

### Links

*   [Microsoft REPLACE function documentation](https://support.office.com/en-us/article/replace-replaceb-functions-8d799074-2425-4a8a-84bc-82472868878a)
    

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