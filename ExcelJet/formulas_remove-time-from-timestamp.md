# Remove time from timestamp - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-time-from-timestamp

---

[Skip to main content](https://exceljet.net/formulas/remove-time-from-timestamp#main-content)

[](https://exceljet.net/formulas/remove-time-from-timestamp#)

*   [Previous](https://exceljet.net/formulas/previous-working-day)
    
*   [Next](https://exceljet.net/formulas/sum-by-fiscal-year)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Remove time from timestamp
==========================

by Dave Bruns · Updated 10 Nov 2024

Related functions 
------------------

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7202/download?token=eJctYWgN)
 (14.18 KB)

![Excel formula: Remove time from timestamp](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove%20time%20from%20timestamp.png "Excel formula: Remove time from timestamp")

Summary
-------

To remove time from a timestamp (or date) that includes both date and time, you can use the [INT function](https://exceljet.net/functions/int-function)
. In the example shown, the formula in cell D5 copied down, is:

    =INT(B5)
    

The result in column D is the date only from the timestamps in column B. The time in the original timestamps is discarded.

Generic formula
---------------

    =INT(date)

Explanation 
------------

In this example, the goal is to use a formula to remove the time value from a timestamp that includes both the date and time. To solve this problem, it's important to understand that Excel handles dates and time using a scheme in which [dates are large serial numbers](https://exceljet.net/glossary/excel-date)
 and [times are fractional values](https://exceljet.net/glossary/excel-time)
. For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. This means the main task in this problem is to remove the decimal portion of the number.

_Note: This example requires valid dates. If you have dates in Excel that don't seem to be dates, try formatting the cells with the [General format](https://exceljet.net/shortcuts/apply-general-format)
. If the date is really a date, you'll see a number. If the date is being treated as text in Excel, nothing will change._

### Number format option

Before permanently removing the time portion of a date, it's important to understand that you have the option of _suppressing the time_ with a [number format](https://exceljet.net/glossary/number-format)
. For example, to display "06-Jun-2000 12:00 PM" as "06-Jun-2000", you can [apply a number format](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)
 like this:

    dd-mmm-yyyy
    

This number format will show the date but hide the time. However, the time will still be there. If the goal is to _permanently_ remove the time portion of a timestamp, see the formulas below.

Note: Excel's date formats are flexible and can be [customized in many ways](https://exceljet.net/articles/custom-number-formats)
.

### INT function

The [INT function](https://exceljet.net/functions/int-function)
 returns the integer part of a decimal number by rounding the number down to the integer. For example:

    =INT(10.8) // returns 10
    

Accordingly, if you have dates in Excel that include time, you can use the [INT function](https://exceljet.net/functions/int-function)
 to remove the time portion of the date. For example, assuming cell A1 contains the date and time, June 1, 2000 12:00 PM (equivalent to the number 36678.5), the formula below returns just the date portion (36678):

    =INT(A1)
    =INT(36678.5)
    =36678
    

Notice that the time portion of the date (the fractional part) is permanently discarded, leaving only the integer value. The screen below shows the original dates with the General number format applied, so you can see what is really happening with all of the dates:

![Same dates with General number format applied](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/dates%20formatted%20with%20general%20number%20format.png?itok=oV2mJeGJ "Same dates with General number format applied")

Note: to see results formatted as a date, be sure to [apply a date number format](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)
. Make sure you use a date format that _does not include a time_. Otherwise, you'll see the time displayed as 12:00 AM even though the time value has been removed. This is normal Excel behavior.

### TRUNC function

You will sometimes see the [TRUNC function](https://exceljet.net/functions/trunc-function)
 used as an alternative to the INT function. Like the INT function, the TRUNC function also removes the decimal portion of a number. Unlike INT, the TRUNC function doesn't round, it _truncates_ a number. In practice, the result is the same with timestamps:

    =TRUNC(A1)
    =TRUNC(36678.5)
    =36678
    

Although the TRUNC function and the INT function [behave differently with negative numbers](https://exceljet.net/functions/trunc-function)
, this difference doesn't affect dates which are by definition positive numbers in Excel. So, in practice, there is no difference between INT and TRUNC in this particular case.

Related formulas
----------------

[![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

### [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD...

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

[![Excel formula: Count unique dates ignore time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20dates%20ignore%20time.png "Excel formula: Count unique dates ignore time")](https://exceljet.net/formulas/count-unique-dates-ignore-time)

### [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)

In this example, the goal is to count the unique dates in a range of timestamps (i.e. dates that contain dates and times). In addition, we also want to create the table of results seen in E7:F9. For convenience, data is the named range B5:B16. Basic count To get a count of individual dates that...

Related functions
-----------------

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract time from a date and time](https://exceljet.net/formulas/extract-time-from-a-date-and-time)
    
*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    
*   [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)
    

### Functions

*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    

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