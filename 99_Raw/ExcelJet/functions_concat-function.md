# Excel CONCAT function | Exceljet

**Source:** https://exceljet.net/functions/concat-function

---

[Skip to main content](https://exceljet.net/functions/concat-function#main-content)

[](https://exceljet.net/functions/concat-function#)

*   [Previous](https://exceljet.net/functions/code-function)
    
*   [Next](https://exceljet.net/functions/concatenate-function)
    

Excel 2019

[Text](https://exceljet.net/functions#Text)

CONCAT Function
===============

by Dave Bruns · Updated 10 May 2022

Related functions 
------------------

[CONCATENATE](https://exceljet.net/functions/concatenate-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

![Excel CONCAT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20concat%20function.png "Excel CONCAT function")

Summary
-------

The Excel CONCAT function concatenates (joins) values supplied as references or constants. Unlike the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 (which CONCAT replaces), CONCAT will accept a [range](https://exceljet.net/glossary/range)
 of cells to join, in addition to individual cell references.

Purpose 
--------

Join text values without delimiter

Return value 
-------------

Result of concatenated text

Syntax
------

    =CONCAT(text1,[text2],...)

*   _text1_ - First text value, cell reference, or range.
*   _text2_ - \[optional\] Second text value, cell reference, or range.

Using the CONCAT function 
--------------------------

The CONCAT function [concatenates](https://exceljet.net/glossary/concatenation)
 (joins) values supplied as references or constants. Unlike the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 (which CONCAT replaces), CONCAT will accept a [range](https://exceljet.net/glossary/range)
 of cells to join, in addition to individual cell references. The CONCAT function automatically ignores empty cells.

The CONCAT function accepts multiple [arguments](https://exceljet.net/glossary/function-argument)
 called text1, text2, text3, etc. up to 255 total. Arguments may be supplied as cell references, ranges, and hard-coded text strings. Only the first argument is required, and values are concatenated in the order they appear. For example, to concatenate the value of A1 and B1, separated by a space, you can configure CONCAT like this:

    =CONCAT(A1," ",B1)
    

This is equivalent to using the concatenation [operator](https://exceljet.net/glossary/math-operators)
 (&) manually like this:

    =A1&" "&B1 // manual concatenation
    

When concatenating numbers, [number formatting](https://exceljet.net/glossary/number-format)
 is lost. For example, with the date 1-Jul-2021 in cell A1, the date reverts to a [serial number](https://exceljet.net/glossary/excel-date)
:

    =CONCAT("The date is ",A1) // returns "The date is 44378"
    

Use the [TEXT function](https://exceljet.net/functions/text-function)
 to apply formatting during concatenation:

    =CONCAT("The date is ",TEXT(A1,"mmmm d")) // "The date is July 1"
    

The main benefit of CONCAT over the older CONCATENATION function is the ability to concatenate ranges. To concatenate the values in A1, B1, and C1, you can use a range like this:

    =CONCAT(A1:C1)
    

However, the CONCAT does not provide a way to specify a delimiter to use when concatenating many values together.  To join many values with a common delimiter, see the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. TEXTJOIN can do everything CONCAT can do, but can also apply a delimiter and optionally ignore empty values.

### Notes

*   CONCAT can accept ranges in addition to individual cells.
*   To concatenate manually, use the [concatenation operator](https://exceljet.net/glossary/concatenation)
     (&).
*   The [CONCAT function](https://exceljet.net/functions/concat-function)
     provides no options for delimiters or empty values.
*   Numbers provided to CONCAT will be converted to text values during concatenation.
*   If the result is greater than 32767 characters, CONCAT returns #VALUE!

CONCAT function examples
------------------------

[![Excel formula: Create email with display name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20email%20with%20display%20name.png "Excel formula: Create email with display name")](https://exceljet.net/formulas/create-email-with-display-name)

### [Create email with display name](https://exceljet.net/formulas/create-email-with-display-name)

Some applications show email addresses together with a "display name", where the name appears first, followed by the email address enclosed in angle brackets (<>). The goal in this example is to create a format like this based on an existing name and email address. In the worksheet shown,...

[![Excel formula: Create email address from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create_email_address_from_name.png "Excel formula: Create email address from name")](https://exceljet.net/formulas/create-email-address-from-name)

### [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)

One of the key skills you need to be good with Excel formulas is concatenation . Put simply, concatenation is just a fancy name for joining text together. In Excel formulas, the primary operator for concatenation is the ampersand (&). A good example of a simple concatenation task is the...

[![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")](https://exceljet.net/formulas/join-first-and-last-name)

### [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of concatenation . To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest...

[![Excel formula: Count paired items in listed combinations](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20paired%20items%20in%20listed%20combinations.png "Excel formula: Count paired items in listed combinations")](https://exceljet.net/formulas/count-paired-items-in-listed-combinations)

### [Count paired items in listed combinations](https://exceljet.net/formulas/count-paired-items-in-listed-combinations)

We want to count how often items in columns B, C, and D appear together. For example, how often A appears with C, B appears with F, G appears with D, and so on. This would seem like a perfect use of COUNTIFS, but if we try to add criteria looking for 2 items across 3 columns, it isn't going to work...

Related functions
-----------------

[![Excel CONCATENATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20concatenate%20function.png "Excel CONCATENATE function")](https://exceljet.net/functions/concatenate-function)

### [CONCATENATE Function](https://exceljet.net/functions/concatenate-function)

The Excel CONCATENATE function concatenates (joins) join up to 30 values together and returns the result as text. In Excel 2019 and later, the [CONCAT](https://exceljet.net/functions/concat-function)
 and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 functions are better, more flexible alternatives...

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    
*   [Count paired items in listed combinations](https://exceljet.net/formulas/count-paired-items-in-listed-combinations)
    
*   [Create email with display name](https://exceljet.net/formulas/create-email-with-display-name)
    
*   [Create email address from name](https://exceljet.net/formulas/create-email-address-from-name)
    

### Functions

*   [CONCATENATE Function](https://exceljet.net/functions/concatenate-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    

### Articles

*   [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
    

### Links

*   [Microsoft CONCAT function documentation](https://support.office.com/en-us/article/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2)
    

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