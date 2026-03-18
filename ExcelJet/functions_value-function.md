# Excel VALUE function | Exceljet

**Source:** https://exceljet.net/functions/value-function

---

[Skip to main content](https://exceljet.net/functions/value-function#main-content)

[](https://exceljet.net/functions/value-function#)

*   [Previous](https://exceljet.net/functions/upper-function)
    
*   [Next](https://exceljet.net/functions/arraytotext-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

VALUE Function
==============

by Dave Bruns · Updated 2 Jul 2022

Related functions 
------------------

[N](https://exceljet.net/functions/n-function)

[DATEVALUE](https://exceljet.net/functions/datevalue-function)

[TIMEVALUE](https://exceljet.net/functions/timevalue-function)

[NUMBERVALUE](https://exceljet.net/functions/numbervalue-function)

[VALUETOTEXT](https://exceljet.net/functions/valuetotext-function)

![Excel VALUE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20value%20function.png "Excel VALUE function")

Summary
-------

The Excel VALUE function converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value. Normally, the VALUE function is not needed in Excel, because Excel automatically converts text to numeric values.

Purpose 
--------

Convert text to a number

Return value 
-------------

A numeric value.

Syntax
------

    =VALUE(text)

*   _text_ - The text value to convert to a number.

Using the VALUE function 
-------------------------

The VALUE function is meant to convert a text value that represents a number into a numeric value. The text can be a date, a time, or any other number, so long as the format can be recognized by Excel. When the conversion is successful, the result is a numeric value with no number formatting. When the VALUE function is unable to convert a text value to a numeric result, the result is a #VALUE! error.

    =VALUE("July 15, 2021") // returns 44392
    =VALUE("$125.50") // returns 125.5
    =VALUE("32.5%") // returns 0.325
    

In general, there is no need to use the VALUE function because Excel automatically converts text to numbers as needed. However, VALUE is provided for compatibility with other spreadsheet applications.

*   Use the VALUE function to convert text input to a numeric value.
*   The VALUE function converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value.
*   Normally, Excel automatically converts text to numeric values as needed, so the VALUE function is not needed.
*   The VALUE function is provided for compatibility with other spreadsheet programs.
*   The VALUE function returns #VALUE! when a conversion is unsuccessful.

VALUE function examples
-----------------------

[![Excel formula: TEXTSPLIT get numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/TEXTSPLIT_get_numbers.png "Excel formula: TEXTSPLIT get numeric values")](https://exceljet.net/formulas/textsplit-get-numeric-values)

### [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)

In this example, we have comma-separated text in column B. The goal is to split the text in column B into columns D through G while at the same time converting the numbers to true numeric values. The challenge is that TEXTSPLIT always returns text, so we need a way to convert the numbers while...

[![Excel formula: Convert text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert_text_to_numbers.png "Excel formula: Convert text to numbers")](https://exceljet.net/formulas/convert-text-to-numbers)

### [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)

In this example, the goal is to convert the text values seen in column B to the numeric values seen in column D. There are several ways to fix this problem in Excel, but this article focuses on a formula-based approach to convert text values to numbers. It also explains how to convert values in...

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

[![Excel formula: Assign points based on late time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/assign%20penalty%20points%20based%20on%20late%20time2.png "Excel formula: Assign points based on late time")](https://exceljet.net/formulas/assign-points-based-on-late-time)

### [Assign points based on late time](https://exceljet.net/formulas/assign-points-based-on-late-time)

This formula is a classic example of a nested IF formula that tests threshold values in ascending order. To match the schedule shown in G5:G11, the formula first checks the late by time in D5 to see if it's less than 5 minutes. If so, zero points are assigned: IF(D5<VALUE("0:05"),0, If the...

VALUE function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/TEXTSPLIT_with_numbers_Play.png)](https://exceljet.net/videos/textsplit-with-numbers)

### [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)

In this video, we'll take a look at how to handle numbers with the TEXTSPLIT function. One result of using the TEXTSPLIT function is that all output is text, and this can cause problems if you need numeric values. Let me illustrate with an example. In this worksheet, we have some comma-separated...

Related functions
-----------------

[![Excel N function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20n%20function.png "Excel N function")](https://exceljet.net/functions/n-function)

### [N Function](https://exceljet.net/functions/n-function)

The Excel N function returns a number when given a value. The N function can be used to convert TRUE and FALSE to 1 and 0 respectively. When given a text value, the N function returns zero.

[![Excel DATEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20datevalue.png "Excel DATEVALUE function")](https://exceljet.net/functions/datevalue-function)

### [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)

The Excel DATEVALUE function converts a date represented as a [text string](https://exceljet.net/glossary/text-value)
 into a [valid Excel date](https://exceljet.net/glossary/excel-date)
. For example, the formula =DATEVALUE("3/10/1975") returns a serial number (27463) in the Excel date system that represents March...

[![Excel TIMEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20timevalue%20function.png "Excel TIMEVALUE function")](https://exceljet.net/functions/timevalue-function)

### [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)

The Excel TIMEVALUE function converts a time represented as text into a proper Excel time. For example, the formula =TIMEVALUE("9:00 AM") returns 0.375, the numeric representation of 9:00 AM in Excel's time system. Numeric time values are more useful than text since they can be directly...

[![Excel NUMBERVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20numbervalue.png "Excel NUMBERVALUE function")](https://exceljet.net/functions/numbervalue-function)

### [NUMBERVALUE Function](https://exceljet.net/functions/numbervalue-function)

The Excel NUMBERVALUE function converts a number in text format to numeric value, using specified decimal and group separators. This function can be used to convert locale-specific values into locale-independent values.

[![Excel VALUETOTEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20valuetotext%20function.png "Excel VALUETOTEXT function")](https://exceljet.net/functions/valuetotext-function)

### [VALUETOTEXT Function](https://exceljet.net/functions/valuetotext-function)

The Excel VALUETOTEXT function converts a value to text. By default, text values pass through unaffected. However, in strict mode, text values are enclosed in double quotes (""). Numeric values are converted to text in all cases, and [number formatting](https://exceljet.net/glossary/number-format)
...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    
*   [Assign points based on late time](https://exceljet.net/formulas/assign-points-based-on-late-time)
    
*   [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)
    
*   [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)
    

### Videos

*   [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)
    

### Functions

*   [N Function](https://exceljet.net/functions/n-function)
    
*   [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)
    
*   [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)
    
*   [NUMBERVALUE Function](https://exceljet.net/functions/numbervalue-function)
    
*   [VALUETOTEXT Function](https://exceljet.net/functions/valuetotext-function)
    

### Links

*   [Microsoft VALUE function documentation](https://support.office.com/en-us/article/value-function-257d0108-07dc-437d-ae1c-bc2d3953d8c2)
    

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