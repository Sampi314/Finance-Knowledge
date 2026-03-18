# Excel TIMEVALUE function | Exceljet

**Source:** https://exceljet.net/functions/timevalue-function

---

[Skip to main content](https://exceljet.net/functions/timevalue-function#main-content)

[](https://exceljet.net/functions/timevalue-function#)

*   [Previous](https://exceljet.net/functions/time-function)
    
*   [Next](https://exceljet.net/functions/today-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

TIMEVALUE Function
==================

by Dave Bruns · Updated 30 Jun 2021

Related functions 
------------------

[DATEVALUE](https://exceljet.net/functions/datevalue-function)

[TIMEVALUE](https://exceljet.net/functions/timevalue-function)

[VALUE](https://exceljet.net/functions/value-function)

[NUMBERVALUE](https://exceljet.net/functions/numbervalue-function)

![Excel TIMEVALUE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20timevalue%20function.png "Excel TIMEVALUE function")

Summary
-------

The Excel TIMEVALUE function converts a time represented as text into a proper Excel time. For example, the formula =TIMEVALUE("9:00 AM") returns 0.375, the numeric representation of 9:00 AM in Excel's time system. Numeric time values are more useful than text since they can be directly manipulated with formulas and pivot tables.

Purpose 
--------

Get a valid time from a text string

Return value 
-------------

A valid Excel time as a decimal number

Syntax
------

    =TIMEVALUE(time_text)

*   _time\_text_ - A date and/or time in a text format recognized by Excel.

Using the TIMEVALUE function 
-----------------------------

Sometimes, times in Excel appear as text values that are not recognized properly as time. The TIMEVALUE function is meant to parse a time that appears as a [text value](https://exceljet.net/glossary/text-value)
 into a valid Excel time. A [native Excel time](https://exceljet.net/glossary/excel-time)
 is more useful than text because it is a numeric value that can be [formatted](https://exceljet.net/glossary/number-format)
 as time and directly manipulated in a formula.

The TIMEVALUE function takes just one argument, called _time\_text_. If _time\_text_ is a cell address, the value in the cell must be text. If _time\_text_ is entered directly into the formula it must be enclosed in double quotes (""). _Time\_text_ should be supplied in a text format that Excel can recognize, for example, "6:45 PM" or "18:45". TIMEVALUE ignores dates if present in a text string. 

The TIMEVALUE function creates a time in serial number format from a date and/or time in an Excel text format. TIMEVALUE will return a decimal number between 0 and 0.99988426, representing 12:00:00 AM to 11:59:59 PM. Because the maximum value returned by TIMEVALUE is less than 1, hours will reset every 24 hours (like a clock).

### Examples

The formulas below show the output from TIMEVALUE:

    =TIMEVALUE("12:00") // returns 0.5
    =TIMEVALUE("12:00 PM") // returns 0.5
    =TIMEVALUE("18:00") // returns 0.75
    

To display the output from TIMEVALUE as a formatted time, apply a time [number format](https://exceljet.net/glossary/number-format)
.

### Alternative formula

Notice that the TIMEVALUE formula in C15 fails with a #VALUE! error, because cell B15 already contains a valid time. This is a limitation of the TIMEVALUE function. If you have a mix of valid and invalid dates, you can use the simple formula below as an alternative:

    =A1+0
    

The math operation of adding zero will cause Excel will try to coerce the value in A1 to a number. If Excel is able parse the text into a proper time it will return a valid time as a decimal number. If the time is already a valid Excel time, adding zero will have no effect, and generate no error.

### Notes

*   TIMEVALUE will return a #VALUE error if _time\_text_ does not contain time formatted as text.

TIMEVALUE function examples
---------------------------

[![Excel formula: Time in hundredths of a second](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time_in_hundredths_of_a_second.png "Excel formula: Time in hundredths of a second")](https://exceljet.net/formulas/time-in-hundredths-of-a-second)

### [Time in hundredths of a second](https://exceljet.net/formulas/time-in-hundredths-of-a-second)

In the worksheet shown, we have race results for an 800m race. The goal is to display time in minutes, seconds, and hundredths of a second (centiseconds). Dealing with times that include fractional seconds can be tricky in Excel. The default time format will only show whole seconds and it is not...

[![Excel formula: Convert date string to date time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20string%20to%20date%20time.png "Excel formula: Convert date string to date time")](https://exceljet.net/formulas/convert-date-string-to-date-time)

### [Convert date string to date time](https://exceljet.net/formulas/convert-date-string-to-date-time)

When date information from other systems is pasted or imported to Excel, it may not be recognized as a proper date or time. Instead, Excel may interpret this information as a text or string value only. In this example, the goal is to extract valid date and time information from a text string and...

Related functions
-----------------

[![Excel DATEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20datevalue.png "Excel DATEVALUE function")](https://exceljet.net/functions/datevalue-function)

### [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)

The Excel DATEVALUE function converts a date represented as a [text string](https://exceljet.net/glossary/text-value)
 into a [valid Excel date](https://exceljet.net/glossary/excel-date)
. For example, the formula =DATEVALUE("3/10/1975") returns a serial number (27463) in the Excel date system that represents March...

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
    
*   [Time in hundredths of a second](https://exceljet.net/formulas/time-in-hundredths-of-a-second)
    

### Functions

*   [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)
    
*   [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)
    
*   [VALUE Function](https://exceljet.net/functions/value-function)
    
*   [NUMBERVALUE Function](https://exceljet.net/functions/numbervalue-function)
    

### Links

*   [Microsoft TIMEVALUE function documentation](https://support.office.com/en-us/article/timevalue-function-0b615c12-33d8-4431-bf3d-f3eb6d186645)
    

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