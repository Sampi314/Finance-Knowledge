# Excel NUMBERVALUE function | Exceljet

**Source:** https://exceljet.net/functions/numbervalue-function

---

[Skip to main content](https://exceljet.net/functions/numbervalue-function#main-content)

[](https://exceljet.net/functions/numbervalue-function#)

*   [Previous](https://exceljet.net/functions/mid-function)
    
*   [Next](https://exceljet.net/functions/proper-function)
    

Excel 2013

[Text](https://exceljet.net/functions#Text)

NUMBERVALUE Function
====================

by Dave Bruns · Updated 28 Jul 2021

Related functions 
------------------

[VALUE](https://exceljet.net/functions/value-function)

[DATEVALUE](https://exceljet.net/functions/datevalue-function)

[TIMEVALUE](https://exceljet.net/functions/timevalue-function)

![Excel NUMBERVALUE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_%20numbervalue.png "Excel NUMBERVALUE function")

Summary
-------

The Excel NUMBERVALUE function converts a number in text format to numeric value, using specified decimal and group separators. This function can be used to convert locale-specific values into locale-independent values.

Purpose 
--------

Convert text to number with custom separators

Return value 
-------------

Numeric value

Syntax
------

    =NUMBERVALUE(text,[decimal_separator],[group_separator])

*   _text_ - The text to convert to a number.
*   _decimal\_separator_ - \[optional\] The character for decimal values.
*   _group\_separator_ - \[optional\] The character for grouping by thousands.

Using the NUMBERVALUE function 
-------------------------------

The NUMBERVALUE function converts a text value representing a number into a valid numeric using custom decimal and group separators. You can use NUMBERVALUE to translate numbers from a locale-specific text format into a locale-independent number. 

To perform a numeric conversion, the NUMBERVALUE function uses the custom separators you provide. The _decimal\_separator_ is the character used to separate integers from fractional values in the source text. The _group\_separator_ is the character used to group text by thousands in the source text. Both separators should be enclosed in double quotes (""). When _decimal\_separator_ and _group\_separator_, Excel uses separators for the current locale.

### Examples

To convert the [text string](https://exceljet.net/glossary/text-value)
 "10,15" to the number 10.15:

    =NUMBERVALUE("10,15",",") // returns 10.15
    

To convert the text value "5%" to a number with no grouping or decimal separator:

    =NUMBERVALUE("5%") // returns 0.05
    

To convert the string "6.000" to the number 6000, where the grouping separator in the source text is a period (.) use:

    =NUMBERVALUE("6.000",",",".") // returns 6000
    

In the example shown, input text is in column B and function output is in column E. Columns C and D are the decimal and group separators used in each row. The formula in E6, copied down, is:

    =NUMBERVALUE(B6,C6,D6)
    

Notice in addition to decimal and group separators, the NUMBERVALUE automatically ignores the extra space in B9 and automatically evaluates the percentage (%) symbol in B11 by dividing by 100.

### Notes

*   NUMBERVALUE ignores extra space characters.
*   Multiple percent symbols are additive.
*   If decimal separator and/or group\_separators are not provided, NUMBERVALUE uses separators from the current locale.
*   NUMBERVALUE uses only the first character provided for decimal and group separators. Additional characters are discarded.
*   NUMBERVALUE returns zero (0) if no text value is provided.
*   NUMBERVALUE returns the #VALUE error if:
    *   The decimal separator appears more than once in the source text
    *   The group separator occurs after the decimal separator  
         

Related functions
-----------------

[![Excel VALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20value%20function.png "Excel VALUE function")](https://exceljet.net/functions/value-function)

### [VALUE Function](https://exceljet.net/functions/value-function)

The Excel VALUE function converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value. Normally, the VALUE function is not needed in Excel, because Excel automatically converts text to numeric values.

[![Excel DATEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20datevalue.png "Excel DATEVALUE function")](https://exceljet.net/functions/datevalue-function)

### [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)

The Excel DATEVALUE function converts a date represented as a [text string](https://exceljet.net/glossary/text-value)
 into a [valid Excel date](https://exceljet.net/glossary/excel-date)
. For example, the formula =DATEVALUE("3/10/1975") returns a serial number (27463) in the Excel date system that represents March...

[![Excel TIMEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20timevalue%20function.png "Excel TIMEVALUE function")](https://exceljet.net/functions/timevalue-function)

### [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)

The Excel TIMEVALUE function converts a time represented as text into a proper Excel time. For example, the formula =TIMEVALUE("9:00 AM") returns 0.375, the numeric representation of 9:00 AM in Excel's time system. Numeric time values are more useful than text since they can be directly...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [VALUE Function](https://exceljet.net/functions/value-function)
    
*   [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)
    
*   [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)
    

### Links

*   [Microsoft NUMBERVALUE function documentation](https://support.office.com/en-us/article/numbervalue-function-1b05c8cf-2bfa-4437-af70-596c7ea7d879)
    

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