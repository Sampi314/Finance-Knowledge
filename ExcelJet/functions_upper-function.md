# Excel UPPER function | Exceljet

**Source:** https://exceljet.net/functions/upper-function

---

[Skip to main content](https://exceljet.net/functions/upper-function#main-content)

[](https://exceljet.net/functions/upper-function#)

*   [Previous](https://exceljet.net/functions/unicode-function)
    
*   [Next](https://exceljet.net/functions/value-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

UPPER Function
==============

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[LOWER](https://exceljet.net/functions/lower-function)

[UPPER](https://exceljet.net/functions/upper-function)

[PROPER](https://exceljet.net/functions/proper-function)

[EXACT](https://exceljet.net/functions/exact-function)

![Excel UPPER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20upper%20function.png "Excel UPPER function")

Summary
-------

The Excel UPPER function converts a text string to all uppercase letters. Numbers, punctuation, and spaces are not affected.

Purpose 
--------

Convert text to upper case

Return value 
-------------

Uppercase text.

Syntax
------

    =UPPER(text)

*   _text_ - The text to convert to uppercase.

Using the UPPER function 
-------------------------

The UPPER function converts a text string to all uppercase letters. UPPER function takes just one argument, _text_, which can be a text value or cell reference. UPPER changes any lowercase characters in the text value to uppercase. Numbers, punctuation, and spaces are not affected. UPPER will convert numbers to text with [number formatting](https://exceljet.net/glossary/number-format)
 removed.

### Examples

    =UPPER("Apple") // returns "APPLE"
    =UPPER("pear") // returns "PEAR"
    

Numbers or punctuation characters inside a text string are unaffected:

    =UPPER("xyy-020-kwp") // returns "XYY-020-KWP"
    

If a numeric value is given to UPPER, [number formatting](https://exceljet.net/glossary/number-format)
 is removed. For example, if cell A1 contains the date June 26, 2021, date formatting will be lost and UPPER will return a [date serial number](https://exceljet.net/glossary/excel-date)
 as text:

    =UPPER(A1) // returns "44373"
    

If necessary, you can use the [TEXT function](https://exceljet.net/functions/text-function)
 to workaround this limitation. Use TEXT to convert the number to a text value, then pass that value into UPPER:

    =UPPER(TEXT(A1,"mmmm d, yyyy")) // returns "JUNE 26, 2021"
    

### Related functions

Use the [LOWER function](https://exceljet.net/functions/lower-function)
 to convert text to lowercase, use the [UPPER function](https://exceljet.net/functions/upper-function)
 to convert text to uppercase, and use the [PROPER function](https://exceljet.net/functions/proper-function)
 to capitalize the words in a text string.

### Notes

*   All letters in _text_ are converted to uppercase.
*   Numbers and punctuation characters are not affected.
*   Number formatting is removed from standalone numeric values.

UPPER function examples
-----------------------

[![Excel formula: Data validation allow uppercase only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20uppercase%20only.png "Excel formula: Data validation allow uppercase only")](https://exceljet.net/formulas/data-validation-allow-uppercase-only)

### [Data validation allow uppercase only](https://exceljet.net/formulas/data-validation-allow-uppercase-only)

Data validation rules are triggered when a user adds or changes a cell value. The UPPER function changes text values to uppercase, and the EXACT function performs a case-sensitive comparison. The AND function takes multiple arguments (logical conditions) and returns TRUE only when all arguments...

[![Excel formula: Count specific characters in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_characters_in_range.png "Excel formula: Count specific characters in a range")](https://exceljet.net/formulas/count-specific-characters-in-a-range)

### [Count specific characters in a range](https://exceljet.net/formulas/count-specific-characters-in-a-range)

For each cell in the range, SUBSTITUTE removes all the o's from the text, then LEN calculates the length of the text without o's. This number is then subtracted from the length of the text with o's. Because we are using SUMPRODUCT, the result of all this calculation is a list of items (an array),...

[![Excel formula: Count specific words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_1.png "Excel formula: Count specific words in a cell")](https://exceljet.net/formulas/count-specific-words-in-a-cell)

### [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)

B4 is the cell we're counting words in, and C4 contains the substring (word or any substring) you are counting. SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original...

[![Excel formula: Count specific words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_words_in_range.png "Excel formula: Count specific words in a range")](https://exceljet.net/formulas/count-specific-words-in-a-range)

### [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)

In the generic version of the formula, rng represents the range to check, and txt is the word or substring to count. In the example shown, B5:B8 is the range to check, and C2 contains the text (word or substring) to count. For each cell in the range, SUBSTITUTE removes the substring from the...

[![Excel formula: Validate strong password](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/validate_strong_password.png "Excel formula: Validate strong password")](https://exceljet.net/formulas/validate-strong-password)

### [Validate strong password](https://exceljet.net/formulas/validate-strong-password)

In this example, the goal is to check for "strong" passwords. What makes a password strong depends on the rules it must follow. In this case, a strong password must meet the following six conditions: At least 8 and not more than 15 characters long Contains at least one uppercase (A-Z) letter...

[![Excel formula: Capitalize first letter in a text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/capitalize_first_letter.png "Excel formula: Capitalize first letter in a text string")](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)

### [Capitalize first letter in a text string](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)

One of the most important skills to learn with Excel formulas is the concept of nesting. Put simply, nesting just means putting one function inside another. Nesting is super useful, but it does take some practice. You have to learn to read a formula from the inside out. The formulas below are good...

UPPER function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20change%20case%20with%20UPPER%2C%20LOWER%20and%20PROPER-thumb.png)](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

### [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

When you're working with text in Excel, you'll frequently need to change case. In this video we'll look at three functions that allow you to easily change case of text in Excel: UPPER, LOWER, and PROPER. In this worksheet, we have two columns that contain names. Column B contains last names in...

Related functions
-----------------

[![Excel LOWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lower%20function.png "Excel LOWER function")](https://exceljet.net/functions/lower-function)

### [LOWER Function](https://exceljet.net/functions/lower-function)

The Excel LOWER function converts a text string to all lowercase letters. Numbers, punctuation, and spaces are not affected.

[![Excel UPPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20upper%20function.png "Excel UPPER function")](https://exceljet.net/functions/upper-function)

### [UPPER Function](https://exceljet.net/functions/upper-function)

The Excel UPPER function converts a text string to all uppercase letters. Numbers, punctuation, and spaces are not affected.

[![Excel PROPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20proper%20function.png "Excel PROPER function")](https://exceljet.net/functions/proper-function)

### [PROPER Function](https://exceljet.net/functions/proper-function)

The Excel PROPER function capitalizes each word in a given text string. Numbers, punctuation, and spaces are not affected.

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)
    
*   [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)
    
*   [Validate strong password](https://exceljet.net/formulas/validate-strong-password)
    
*   [Capitalize first letter in a text string](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)
    
*   [Data validation allow uppercase only](https://exceljet.net/formulas/data-validation-allow-uppercase-only)
    
*   [Count specific characters in a range](https://exceljet.net/formulas/count-specific-characters-in-a-range)
    

### Videos

*   [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)
    

### Functions

*   [LOWER Function](https://exceljet.net/functions/lower-function)
    
*   [UPPER Function](https://exceljet.net/functions/upper-function)
    
*   [PROPER Function](https://exceljet.net/functions/proper-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

### Links

*   [Microsoft UPPER function documentation](https://support.office.com/en-us/article/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6)
    

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