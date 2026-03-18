# Excel DATEVALUE function | Exceljet

**Source:** https://exceljet.net/functions/datevalue-function

---

[Skip to main content](https://exceljet.net/functions/datevalue-function#main-content)

[](https://exceljet.net/functions/datevalue-function#)

*   [Previous](https://exceljet.net/functions/datedif-function)
    
*   [Next](https://exceljet.net/functions/day-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

DATEVALUE Function
==================

by Dave Bruns · Updated 13 Jul 2021

Related functions 
------------------

[TIMEVALUE](https://exceljet.net/functions/timevalue-function)

[VALUE](https://exceljet.net/functions/value-function)

[NUMBERVALUE](https://exceljet.net/functions/numbervalue-function)

![Excel DATEVALUE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20datevalue.png "Excel DATEVALUE function")

Summary
-------

The Excel DATEVALUE function converts a date represented as a [text string](https://exceljet.net/glossary/text-value)
 into a [valid Excel date](https://exceljet.net/glossary/excel-date)
. For example, the formula =DATEVALUE("3/10/1975") returns a serial number (27463) in the Excel date system that represents March 10, 1975. Proper Excel dates are more useful than text dates since they can be directly manipulated with formulas and pivot tables .

Purpose 
--------

Convert a date in text format to a valid date

Return value 
-------------

A valid Excel time as a serial number

Syntax
------

    =DATEVALUE(date_text)

*   _date\_text_ - A valid date in text format.

Using the DATEVALUE function 
-----------------------------

Sometimes, dates in Excel appear as text values that are not recognized as proper dates. The DATEVALUE function is meant to convert a date represented as a [text string](https://exceljet.net/glossary/text-value)
 into a [valid Excel date](https://exceljet.net/glossary/excel-date)
. Proper Excel dates are more useful than text dates since they can be formatted as a date, and directly manipulated with other formulas.

The DATEVALUE function takes just one argument, called _date\_text_. If _date\_text_ is a cell address, the value of the cell must be text. If _date\_text_ is entered directly into the formula it must be enclosed in quotes.

### Examples

To illustrate how the DATEVALUE function works, the formula below shows how the text "3/10/1975" is converted to the date serial number 27463 by DATEVALUE:

    =DATEVALUE("3/10/1975")  // returns 27463
    

Note that DATEVALUE returns a serial number, 27463, which represents March 10, 1975 in Excel's date system. A date [number format](https://exceljet.net/glossary/number-format)
 must be applied to display this number as a date.

In the example shown, column B contains dates entered as text values, except for B15, which contains a valid date. The formula in C5, copied down, is:

    =DATEVALUE(B5)
    

Column C shows the number returned by DATEVALUE, and column D shows the same number [formatted as a date](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)
. Notice that Excel makes certain assumptions about missing day and year values. Missing days become the number 1, and the current year is used if there is no year value available.

### Alternative formula

Notice that the DATEVALUE formula in C15 fails with a #VALUE! error, because cell B15 already contains a valid date. This is a limitation of the DATEVALUE function. If you have a mix of valid and invalid dates, you can try the simple formula below as an alternative:

    =A1+0
    

The math operation of adding zero will cause Excel will try to coerce the value in A1 to a number. If Excel can parse the text into a proper date it will return a valid date serial number. If the date is already a valid Excel date (i.e. a serial number), adding zero will have no effect, and generate no error.

### Notes

*   DATEVALUE will return a #VALUE error if _date\_text_ refers does not contain a date formatted as text.

DATEVALUE function examples
---------------------------

[![Excel formula: Zodiac sign lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/zodiac%20sign%20lookup_0.png "Excel formula: Zodiac sign lookup")](https://exceljet.net/formulas/zodiac-sign-lookup)

### [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)

The goal of this example is to look up the correct astrological or zodiac sign for a given birthdate, using the table shown in B5:F15. These are based on the Western zodiac signs described here . Zodiac signs are used in horoscopes, which are a kind of forecast of a person's future, based on the...

[![Excel formula: Convert date string to date time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20string%20to%20date%20time.png "Excel formula: Convert date string to date time")](https://exceljet.net/formulas/convert-date-string-to-date-time)

### [Convert date string to date time](https://exceljet.net/formulas/convert-date-string-to-date-time)

When date information from other systems is pasted or imported to Excel, it may not be recognized as a proper date or time. Instead, Excel may interpret this information as a text or string value only. In this example, the goal is to extract valid date and time information from a text string and...

[![Excel formula: Month number from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/month%20number%20from%20name.png "Excel formula: Month number from name")](https://exceljet.net/formulas/month-number-from-name)

### [Month number from name](https://exceljet.net/formulas/month-number-from-name)

In this example, the goal is to return a number, 1-12, for any month name of the year. For example, given the string "January" we want to return 1, "February" should return 2, and so on. If we had a valid Excel date , we could use a number format for this task, but because we are starting with a...

Related functions
-----------------

[![Excel TIMEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20timevalue%20function.png "Excel TIMEVALUE function")](https://exceljet.net/functions/timevalue-function)

### [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)

The Excel TIMEVALUE function converts a time represented as text into a proper Excel time. For example, the formula =TIMEVALUE("9:00 AM") returns 0.375, the numeric representation of 9:00 AM in Excel's time system. Numeric time values are more useful than text since they can be directly...

[![Excel VALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20value%20function.png "Excel VALUE function")](https://exceljet.net/functions/value-function)

### [VALUE Function](https://exceljet.net/functions/value-function)

The Excel VALUE function converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value. Normally, the VALUE function is not needed in Excel, because Excel automatically converts text to numeric values.

[![Excel NUMBERVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20numbervalue.png "Excel NUMBERVALUE function")](https://exceljet.net/functions/numbervalue-function)

### [NUMBERVALUE Function](https://exceljet.net/functions/numbervalue-function)

The Excel NUMBERVALUE function converts a number in text format to numeric value, using specified decimal and group separators. This function can be used to convert locale-specific values into locale-independent values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert date string to date time](https://exceljet.net/formulas/convert-date-string-to-date-time)
    
*   [Month number from name](https://exceljet.net/formulas/month-number-from-name)
    
*   [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)
    

### Functions

*   [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)
    
*   [VALUE Function](https://exceljet.net/functions/value-function)
    
*   [NUMBERVALUE Function](https://exceljet.net/functions/numbervalue-function)
    

### Links

*   [Microsoft DATEVALUE function documentation](https://support.office.com/en-us/article/datevalue-function-df8b07d4-7761-4a93-bc33-b7471bbff252)
    

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