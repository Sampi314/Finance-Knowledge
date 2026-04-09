# Excel CONCATENATE function | Exceljet

**Source:** https://exceljet.net/functions/concatenate-function

---

[Skip to main content](https://exceljet.net/functions/concatenate-function#main-content)

[](https://exceljet.net/functions/concatenate-function#)

*   [Previous](https://exceljet.net/functions/concat-function)
    
*   [Next](https://exceljet.net/functions/dollar-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

CONCATENATE Function
====================

by Dave Bruns · Updated 10 May 2022

Related functions 
------------------

[CONCAT](https://exceljet.net/functions/concat-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

![Excel CONCATENATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20concatenate%20function.png "Excel CONCATENATE function")

Summary
-------

The Excel CONCATENATE function concatenates (joins) join up to 30 values together and returns the result as text. In Excel 2019 and later, the [CONCAT](https://exceljet.net/functions/concat-function)
 and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 functions are better, more flexible alternatives.

Purpose 
--------

Join text together

Return value 
-------------

Text joined together.

Syntax
------

    =CONCATENATE(text1,text2,[text3],...)

*   _text1_ - The first text value to join together.
*   _text2_ - The second text value to join together.
*   _text3_ - \[optional\] The third text value to join together.

Using the CONCATENATE function 
-------------------------------

The CONCATENATE function [concatenates](https://exceljet.net/glossary/concatenation)
 (joins) join up to 30 values together and returns the result as text. In Excel 2019 and later, the [CONCAT function](https://exceljet.net/functions/concat-function)
 and [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 are better, more flexible alternatives.

The CONCATENATE function accepts multiple [arguments](https://exceljet.net/glossary/function-argument)
 called _text1_, _text2_, _text3_, etc. up to 30 total. Values may be supplied as cell references, and hard-coded text strings. Only the first argument is required, and values are concatenated in the order they appear. For example, to concatenate the value of A1 and B1, separated by a space, you can use CONCATENATE like this:

    =CONCATENATE(A1," ",B1)
    

The result of this formula is the same as using the concatenation [operator](https://exceljet.net/glossary/math-operators)
 (&) manually like this:

    =A1&" "&B1 // manual concatenation
    

The ampersand character (&) is an alternative to CONCATENATE. The result is the same, but the ampersand is more flexible, and creates formulas that are shorter and (arguably) easier to read.

### Number formatting

When concatenating numeric values like dates, times, percentages, etc., [number formatting](https://exceljet.net/glossary/number-format)
 will be lost. For example, with the date 1-Jul-2021 in cell A1, the date reverts to a [serial number](https://exceljet.net/glossary/excel-date)
 during concatenation:

    =CONCATENATE("Date: ",A1) // returns "Date: 44378"
    

To apply formatting during concatenation use the [TEXT function](https://exceljet.net/functions/text-function)
 :

    =CONCATENATE("The date is ",TEXT(A1,"mmmm d")) // "Date: July 1"
    

The CONCATENATE function will not handle [ranges](https://exceljet.net/glossary/range)
:

    =CONCATENATE(A1:D1) // does not work
    

To concatenate values in ranges, see the [CONCAT function](https://exceljet.net/functions/concat-function)
. To concatenate many values with a common delimiter, see the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. TEXTJOIN can do everything CONCAT can do, but can also accept a delimiter and optionally ignore empty values.

### Notes

*   CONCATENATE can join up to 30 text items together.
*   Text items can be text strings, numbers, or cell references that refer to one cell.
*   Numbers are converted to text when joined. If you need to specify a number format for a number being joined, see the [TEXT function](https://exceljet.net/functions/text-function)
    .
*   The ampersand character (&) is an alternative to CONCATENATE. The result is the same, but the ampersand is more flexible, and creates formulas that are shorter and (arguably) easier to read.

CONCATENATE function examples
-----------------------------

[![Excel formula: Create email with display name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20email%20with%20display%20name.png "Excel formula: Create email with display name")](https://exceljet.net/formulas/create-email-with-display-name)

### [Create email with display name](https://exceljet.net/formulas/create-email-with-display-name)

Some applications show email addresses together with a "display name", where the name appears first, followed by the email address enclosed in angle brackets (<>). The goal in this example is to create a format like this based on an existing name and email address. In the worksheet shown,...

[![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")](https://exceljet.net/formulas/join-first-and-last-name)

### [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of concatenation . To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest...

CONCATENATE function videos
---------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20join%20cell%20values%20with%20CONCATENATE-thumb.png)](https://exceljet.net/videos/how-to-join-cell-values-with-concatenate)

### [How to join cell values with CONCATENATE](https://exceljet.net/videos/how-to-join-cell-values-with-concatenate)

In this video we'll look at the CONCATENATE function , which is an alternative to using the ampersand character to join values. This is the same example we looked at previously: a table which contains first, middle, and last names. In column E, I'll add a formula that uses the CONCATENATE function...

Related functions
-----------------

[![Excel CONCAT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20concat%20function.png "Excel CONCAT function")](https://exceljet.net/functions/concat-function)

### [CONCAT Function](https://exceljet.net/functions/concat-function)

The Excel CONCAT function concatenates (joins) values supplied as references or constants. Unlike the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 (which CONCAT replaces), CONCAT will accept a [range](https://exceljet.net/glossary/range)
 of cells to join, in addition to individual...

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
    
*   [Create email with display name](https://exceljet.net/formulas/create-email-with-display-name)
    

### Videos

*   [How to join cell values with CONCATENATE](https://exceljet.net/videos/how-to-join-cell-values-with-concatenate)
    

### Functions

*   [CONCAT Function](https://exceljet.net/functions/concat-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    

### Articles

*   [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
    

### Links

*   [Microsoft CONCATENATE function documentation](https://support.office.com/en-us/article/concatenate-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d)
    

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