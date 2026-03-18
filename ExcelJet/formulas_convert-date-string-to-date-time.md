# Convert date string to date time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-date-string-to-date-time

---

[Skip to main content](https://exceljet.net/formulas/convert-date-string-to-date-time#main-content)

[](https://exceljet.net/formulas/convert-date-string-to-date-time#)

*   [Previous](https://exceljet.net/formulas/calculate-years-between-dates)
    
*   [Next](https://exceljet.net/formulas/convert-date-to-julian-format)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Convert date string to date time
================================

by Dave Bruns · Updated 24 Feb 2022

Related functions 
------------------

[DATEVALUE](https://exceljet.net/functions/datevalue-function)

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

[TIMEVALUE](https://exceljet.net/functions/timevalue-function)

![Excel formula: Convert date string to date time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20date%20string%20to%20date%20time.png "Excel formula: Convert date string to date time")

Summary
-------

To convert a date string to a datetime (date with time) you can parse the text into separate components then build a proper datetime. In the example shown, we are using several functions to perform this task, including [DATEVALUE](https://exceljet.net/functions/datevalue-function)
, [TIMEVALUE](https://exceljet.net/functions/timevalue-function)
, [LEFT](https://exceljet.net/functions/left-function)
 and [MID](https://exceljet.net/functions/mid-function)
. In the worksheet shown, to extract the date, the formula in C5 is:

    =DATEVALUE(LEFT(B5,10))
    

To extract the time, the formula in D5 is:

    =TIMEVALUE(MID(B5,12,8))
    

To assemble a [datetime](https://exceljet.net/glossary/excel-datetime)
, the formula in E5 is:

    =C5+D5
    

Generic formula
---------------

    =LEFT(date,10)+MID(date,12,8)

Explanation 
------------

When date information from other systems is pasted or imported to Excel, it may not be recognized as a proper date or time. Instead, Excel may interpret this information as a text or string value only. In this example, the goal is to extract valid date and time information from a [text string](https://exceljet.net/glossary/text-value)
 and convert that information into a [datetime](https://exceljet.net/glossary/excel-datetime)
. It is important to understand that [Excel dates](https://exceljet.net/glossary/excel-date)
 and [Excel times](https://exceljet.net/glossary/excel-time)
 are numbers so at a high level, the main task is to convert a text value to the appropriate numeric value.

### Date

To get the date, we extract the first 10 characters of the value with the [LEFT function](https://exceljet.net/functions/left-function)
:

    LEFT(B5,10) // returns "2015-03-01"
    

The result is text, so to get Excel to interpret as a date, we wrap LEFT in [DATEVALUE](https://exceljet.net/functions/datevalue-function)
, which converts the text into a proper [Excel date](https://exceljet.net/glossary/excel-date)
.

### Time

To get the time, we extract 8 characters from the middle of the text with the [MID function](https://exceljet.net/functions/mid-function)
:

    MID(B5,12,8) // returns "12:28:45"
    

Again, the result is text. To get Excel to interpret this value as time, we wrap MID in [TIMEVALUE](https://exceljet.net/functions/timevalue-function)
, which converts the text into a proper [Excel time](https://exceljet.net/glossary/excel-time)
.

### Datetime

To get a final [datetime](https://exceljet.net/functions/datevalue-function)
, we just add the date value to the time value. The formula in E5 is:

    =C5+D5
    

Once you have a valid datetime, use [custom number formatting](https://exceljet.net/articles/custom-number-formats)
 to display the value as desired.

### All in one formula

Although this example extracts the date and time separately for clarity, you can combine formulas if you like. The following formula extracts the date and time, and adds them together in one step:

    =LEFT(date,10)+MID(date,12,8)
    

Note that DATEVALUE and TIMEVALUE aren't necessary in this case because the math operation (+) causes Excel to automatically coerce the text values to numbers.

Related formulas
----------------

[![Excel formula: Convert date to text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20text.png "Excel formula: Convert date to text")](https://exceljet.net/formulas/convert-date-to-text)

### [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)

Dates and times in Excel are stored as serial numbers and converted to human-readable values on the fly using number formats. When you enter a date in Excel, you can apply a number format to display that date as you like. Similarly, the TEXT function allows you to convert a date or time into text...

[![Excel formula: Convert text to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20to%20date.png "Excel formula: Convert text to date")](https://exceljet.net/formulas/convert-text-to-date)

### [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)

The DATE function creates a valid date using three arguments: year, month, and day: =DATE(year,month,day) In cell C6, we use the LEFT, MID, and RIGHT functions to extract each of these components from a text string, and feed the results into the DATE function: =DATE(LEFT(B6,4),MID(B6,5,2),RIGHT(B6,...

[![Excel formula: Convert time to time zone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20time%20to%20time%20zone.png "Excel formula: Convert time to time zone")](https://exceljet.net/formulas/convert-time-to-time-zone)

### [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)

Times in Excel are fractional values of the number 1 . So, 12 PM is 12/24 = .5, 6:00 AM is 6/24 = .25, and so on. So, to convert a time by a given number, you need to divide the number of hours by 24 to get required decimal value: E5/24 // convert adjustment to Excel time We add the result to the...

Related functions
-----------------

[![Excel DATEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20datevalue.png "Excel DATEVALUE function")](https://exceljet.net/functions/datevalue-function)

### [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)

The Excel DATEVALUE function converts a date represented as a [text string](https://exceljet.net/glossary/text-value)
 into a [valid Excel date](https://exceljet.net/glossary/excel-date)
. For example, the formula =DATEVALUE("3/10/1975") returns a serial number (27463) in the Excel date system that represents March...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

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

### Formulas

*   [Convert date to text](https://exceljet.net/formulas/convert-date-to-text)
    
*   [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
    
*   [Convert time to time zone](https://exceljet.net/formulas/convert-time-to-time-zone)
    

### Functions

*   [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [TIMEVALUE Function](https://exceljet.net/functions/timevalue-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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