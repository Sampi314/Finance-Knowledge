# Excel PROPER function | Exceljet

**Source:** https://exceljet.net/functions/proper-function

---

[Skip to main content](https://exceljet.net/functions/proper-function#main-content)

[](https://exceljet.net/functions/proper-function#)

*   [Previous](https://exceljet.net/functions/numbervalue-function)
    
*   [Next](https://exceljet.net/functions/replace-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

PROPER Function
===============

by Dave Bruns · Updated 22 Dec 2023

Related functions 
------------------

[UPPER](https://exceljet.net/functions/upper-function)

[LOWER](https://exceljet.net/functions/lower-function)

[PROPER](https://exceljet.net/functions/proper-function)

[EXACT](https://exceljet.net/functions/exact-function)

![Excel PROPER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20proper%20function.png "Excel PROPER function")

Summary
-------

The Excel PROPER function capitalizes each word in a given text string. Numbers, punctuation, and spaces are not affected.

Purpose 
--------

Capitalize the first letter in each word

Return value 
-------------

Text in proper case.

Syntax
------

    =PROPER(text)

*   _text_ - The text that should be converted to proper case.

Using the PROPER function 
--------------------------

The PROPER function capitalizes each word in a given text string. PROPER function takes just one argument, _text_, which can be a text value or cell reference. PROPER first lowercases any uppercase letters, then capitalizes each word in the provided text string. Numbers, punctuation, and spaces are not affected. PROPER will convert numbers to text with [number formatting](https://exceljet.net/glossary/number-format)
 removed.

### Examples

    =PROPER("apple") // returns "Apple"
    =PROPER("APPLE") // returns "Apple"
    

Numbers or punctuation characters inside a text string are unaffected:

    =PROPER("XYY-020-kwp") // returns "Xyy-020-Kwp"
    

If a numeric value is given to PROPER, [number formatting](https://exceljet.net/glossary/number-format)
 is removed. For example, if cell A1 contains the date June 26, 2021, date formatting will be lost and PROPER will return a [date serial number](https://exceljet.net/glossary/excel-date)
 as text:

    =PROPER(A1) // returns "44373"
    

### Related functions

Use the [LOWER function](https://exceljet.net/functions/lower-function)
 to convert text to lowercase, use the [UPPER function](https://exceljet.net/functions/upper-function)
 to convert text to uppercase, and use the [PROPER function](https://exceljet.net/functions/proper-function)
 to capitalize the words in a text string.

### Capitalizing the first word only

One limitation of the PROPER function is that it will capitalize _all words in a text string_. If you only want to capitalize the first word (i.e. capitalize the first word in a sentence) while leaving other characters unchanged, you can use a custom formula like this:

    =REPLACE(A1,1,1,UPPER(LEFT(A1)))

[See this page for a full explanation](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)
.

### Notes

*   Use PROPER to capitalize each word in a given string.
*   All words in a text string are capitalized.
*   Numbers and punctuation characters are not affected.
*   Number formatting is removed from standalone numeric values.

PROPER function examples
------------------------

[![Excel formula: Put names into proper case](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/put_names_into_proper_case.png "Excel formula: Put names into proper case")](https://exceljet.net/formulas/put-names-into-proper-case)

### [Put names into proper case](https://exceljet.net/formulas/put-names-into-proper-case)

The goal in this example is to reformat names that appear in mixed upper and lower case letters into "proper case", defined as each word in the name beginning with a capital letter. This can easily be done in Excel with the PROPER function. PROPER function The PROPER function automatically...

PROPER function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20change%20case%20with%20UPPER%2C%20LOWER%20and%20PROPER-thumb.png)](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

### [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

When you're working with text in Excel, you'll frequently need to change case. In this video we'll look at three functions that allow you to easily change case of text in Excel: UPPER, LOWER, and PROPER. In this worksheet, we have two columns that contain names. Column B contains last names in...

Related functions
-----------------

[![Excel UPPER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20upper%20function.png "Excel UPPER function")](https://exceljet.net/functions/upper-function)

### [UPPER Function](https://exceljet.net/functions/upper-function)

The Excel UPPER function converts a text string to all uppercase letters. Numbers, punctuation, and spaces are not affected.

[![Excel LOWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lower%20function.png "Excel LOWER function")](https://exceljet.net/functions/lower-function)

### [LOWER Function](https://exceljet.net/functions/lower-function)

The Excel LOWER function converts a text string to all lowercase letters. Numbers, punctuation, and spaces are not affected.

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

*   [Put names into proper case](https://exceljet.net/formulas/put-names-into-proper-case)
    

### Videos

*   [How to change case with UPPER LOWER and PROPER](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)
    

### Functions

*   [UPPER Function](https://exceljet.net/functions/upper-function)
    
*   [LOWER Function](https://exceljet.net/functions/lower-function)
    
*   [PROPER Function](https://exceljet.net/functions/proper-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

### Links

*   [Microsoft PROPER function documentation](https://support.office.com/en-us/article/proper-function-52a5a283-e8b2-49be-8506-b2887b889f94)
    

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