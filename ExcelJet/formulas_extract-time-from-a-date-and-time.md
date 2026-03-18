# Extract time from a date and time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-time-from-a-date-and-time

---

[Skip to main content](https://exceljet.net/formulas/extract-time-from-a-date-and-time#main-content)

[](https://exceljet.net/formulas/extract-time-from-a-date-and-time#)

*   [Previous](https://exceljet.net/formulas/extract-date-from-text-string)
    
*   [Next](https://exceljet.net/formulas/filter-on-dates-expiring-soon)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Extract time from a date and time
=================================

by Dave Bruns · Updated 8 Jan 2026

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

[INT](https://exceljet.net/functions/int-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

[TIME](https://exceljet.net/functions/time-function)

[ROUND](https://exceljet.net/functions/round-function)

[HOUR](https://exceljet.net/functions/hour-function)

[MINUTE](https://exceljet.net/functions/minute-function)

[SECOND](https://exceljet.net/functions/second-function)

![Excel formula: Extract time from a date and time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract%20time%20from%20date%20and%20time.png "Excel formula: Extract time from a date and time")

Summary
-------

To extract the time from a date that contains time (also called a "[datetime](https://exceljet.net/glossary/excel-datetime)
"), you can use a formula based on the [MOD function](https://exceljet.net/functions/mod-function)
. In the example shown, the formula in D5 is:

    =MOD(B5,1)
    

The result is the time portion of the value in B5, 6:00 AM, which is the decimal value 0.25. As the formula is copied down, the result is the time portion of each datetime in column B.

Generic formula
---------------

    =MOD(A1,1)

Explanation 
------------

In this example, the goal is to extract the time portion of a date that contains time (also called a "datetime"). Since dates in Excel are serial numbers and times are fractional values of a day, the task is to extract the decimal portion of the serial number. This is easy to do with the MOD function, and other methods mentioned below. Note that if you are comparing extracted times to other time values, there is a subtle [floating point precision issue](https://exceljet.net/formulas/extract-time-from-a-date-and-time#floating-point-precision-issue)
 you should be aware of.

### Table of contents

*   [How Excel handles dates and times](https://exceljet.net/formulas/extract-time-from-a-date-and-time#how-excel-handles-dates-and-times)
    
*   [Using MOD to extract time](https://exceljet.net/formulas/extract-time-from-a-date-and-time#using-mod-to-extract-time)
    
*   [Other methods to extract time](https://exceljet.net/formulas/extract-time-from-a-date-and-time#other-methods-to-extract-time)
    
*   [Floating point precision issue](https://exceljet.net/formulas/extract-time-from-a-date-and-time#floating-point-precision-issue)
    
*   [Workaround: use TIME or ROUND](https://exceljet.net/formulas/extract-time-from-a-date-and-time#workaround-use-time-or-round)
    

### How Excel handles dates and times

Excel handles [dates](https://exceljet.net/glossary/excel-date)
 and [times](https://exceljet.net/glossary/excel-time)
 using a system in which dates are serial numbers and times are fractional values of a day. For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date (June 1, 2000) and .5 is the time (12:00 PM). Since 12:00 PM is exactly halfway through a day, Excel represents it as 0.5. Likewise, 6:00 AM is 0.25 (one quarter of a day) and 6:00 PM is 0.75 (three quarters of a day). In other words, the time value in a "datetime" is the decimal portion of the number.

### Using MOD to extract time

The MOD function returns the remainder from division. The first argument is the number and the second is the divisor. Here are a few examples:

    =MOD(5,2) // returns 1
    =MOD(7,5) // returns 2
    

If you use MOD with a divisor of 1, the result will be the decimal part of the number, if any, because every whole number can be evenly divided by itself. For example:

    =MOD(3.5,1) // returns 0.5
    =MOD(3.125,1) // returns 0.125
    

In short, =MOD(number,1) returns just the fractional part of a number, discarding the integer portion, so it's a convenient way to extract time from a date.

> If you use this formula to strip the time from a date + time, you'll need to apply a [suitable number format](https://exceljet.net/articles/custom-number-formats)
>  to display as time.

### Other methods to extract time

What's nice about MOD is that it's a simple one-function solution. However, there are other ways to extract time from a datetime. The most common alternatives subtract the integer (date) portion from the original value using the [INT function](https://exceljet.net/functions/int-function)
 or the [TRUNC function](https://exceljet.net/functions/trunc-function)
:

    =B5-INT(B5)
    =B5-TRUNC(B5)
    

Both formulas work the same way: they calculate the date portion and subtract it from the datetime, leaving just the time. Another option is to rebuild the time from its components using [TIME](https://exceljet.net/functions/time-function)
, [HOUR](https://exceljet.net/functions/hour-function)
, [MINUTE](https://exceljet.net/functions/minute-function)
, and [SECOND](https://exceljet.net/functions/second-function)
:

    =TIME(HOUR(B5),MINUTE(B5),SECOND(B5))
    

This approach extracts each time component as an integer, then reassembles them into a time value. This is a more verbose formula, but it has the advantage of avoiding the floating-point precision issue described below.

### Floating point precision issue

The MOD formula works well for displaying extracted times, but there's a subtle gotcha you should know about. Because of the way computers handle decimal numbers (known as [floating point arithmetic](https://exceljet.net/articles/floating-point-errors-in-excel)
), the result from MOD may not be exactly equal to the same time created with the [TIME function](https://exceljet.net/functions/time-function)
. This can cause problems when comparing extracted times.

For example, say you have a datetime like October 20, 2024, 4:00 PM in cell A1. If you extract the time with MOD and compare it to 4:00 PM created with TIME, you might expect them to be equal:

    =MOD(A1,1)=TIME(16,0,0) // may return FALSE!
    

The result may be FALSE because MOD returns something like 0.6666666666642413 instead of 0.666666666666667 (the value TIME returns for 4:00 PM). The difference is tiny (invisible when formatted as time) but enough to break equality checks. You can see examples of these very slightly different values for 1:00 PM and 4:00 PM in cells E15 and E16, respectively:

![Example of floating point errors resulting in a tiny difference](https://exceljet.net/sites/default/files/images/formulas/inline/extract_time_from_date_and_time_floating_point_issue.png "Example of floating point errors resulting in a tiny difference")

This issue isn't specific to MOD. Any formula that uses subtraction to isolate the time portion will have the same problem, including formulas based on INT, TRUNC, and [DATE](https://exceljet.net/functions/date-function)
:

    =A1-INT(A1) // same issue
    =A1-TRUNC(A1) // same issue
    =A1-DATE(YEAR(A1),MONTH(A1),DAY(A1)) // same issue
    

### Workaround: use TIME or ROUND

If you need to compare extracted times to other time values, here are two reliable solutions. The first option is to rebuild the time with TIME. The formula extracts the hour, minute, and second with HOUR, MINUTE, and SECOND, then rebuilds the time value using TIME:

    =TIME(HOUR(B5),MINUTE(B5),SECOND(B5))
    

Because TIME builds the time from scratch using integer values, it avoids the precision issue entirely.

Another good option is to round before comparing values with the [ROUND function](https://exceljet.net/functions/round-function)
. Rounding to about 10 decimal places is enough:

    =ROUND(MOD(B5,1),10)=ROUND(TIME(16,0,0),10) // reliable comparison
    

Either approach will give you consistent results when comparing times.

Related formulas
----------------

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

[![Excel formula: Round time to nearest 15 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20time%20to%20nearest%2015%20minutes.png "Excel formula: Round time to nearest 15 minutes")](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

### [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)

MROUND rounds to nearest values based on a supplied multiple. When you supply "0:15" as the multiple, Excel internal converts 0:15 into 0.0104166666666667, which is the decimal value that represents 15 minutes, and rounds using that value. You can also express 15 minutes in a formula with this...

[![Excel formula: Group times into 3 hour buckets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group%20times%20into%203%20hour%20buckets.png "Excel formula: Group times into 3 hour buckets")](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

### [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)

If you need to group times into buckets (i.e. group by 6 hours, group by 3 hours, etc.) you can do so with a rounding function called FLOOR. In the example shown, we have a number of transactions, each with a timestamp. Let's say you want to group these transactions into buckets of 3 hours like...

Related functions
-----------------

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

[![Excel ROUND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20round%20function.png "Excel ROUND function")](https://exceljet.net/functions/round-function)

### [ROUND Function](https://exceljet.net/functions/round-function)

The Excel ROUND function returns a number rounded to a given number of digits. The ROUND function can round to the right or left of the decimal point.

[![Excel HOUR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_hour_function.png "Excel HOUR function")](https://exceljet.net/functions/hour-function)

### [HOUR Function](https://exceljet.net/functions/hour-function)

The Excel HOUR function returns the hour component of a time as a number between 0-23. For example, with a time of 9:30 AM, HOUR will return 9. You can use the HOUR function to extract the hour into a cell, or feed the result into another formula, like the [TIME](https://exceljet.net/functions/time-function)
...

[![Excel MINUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20minute%20function.png "Excel MINUTE function")](https://exceljet.net/functions/minute-function)

### [MINUTE Function](https://exceljet.net/functions/minute-function)

The Excel MINUTE function extracts the minute component of a time as a number between 0-59. For example, with a time of 9:45 AM, minute will return 45. You can use the MINUTE function to extract the minute into a cell, or feed the result into another function like the ...

[![Excel SECOND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_second_function.png "Excel SECOND function")](https://exceljet.net/functions/second-function)

### [SECOND Function](https://exceljet.net/functions/second-function)

The Excel SECOND function extracts the seconds component of a time as a number between 0-59. For example, when given the time 9:10:15 AM, SECOND will return 15. You can use the SECOND function to extract seconds into another cell.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    
*   [Round time to nearest 15 minutes](https://exceljet.net/formulas/round-time-to-nearest-15-minutes)
    
*   [Group times into 3 hour buckets](https://exceljet.net/formulas/group-times-into-3-hour-buckets)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    
*   [TIME Function](https://exceljet.net/functions/time-function)
    
*   [ROUND Function](https://exceljet.net/functions/round-function)
    
*   [HOUR Function](https://exceljet.net/functions/hour-function)
    
*   [MINUTE Function](https://exceljet.net/functions/minute-function)
    
*   [SECOND Function](https://exceljet.net/functions/second-function)
    

### Links

*   [http://excelsemipro.com/2012/11/extract-time-with-the-mod-function-in-excel/](http://excelsemipro.com/2012/11/extract-time-with-the-mod-function-in-excel/)
    

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