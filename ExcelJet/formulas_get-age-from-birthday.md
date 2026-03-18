# Get age from birthday - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-age-from-birthday

---

[Skip to main content](https://exceljet.net/formulas/get-age-from-birthday#main-content)

[](https://exceljet.net/formulas/get-age-from-birthday#)

*   [Previous](https://exceljet.net/formulas/generate-quarter-dates)
    
*   [Next](https://exceljet.net/formulas/get-date-from-day-number)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get age from birthday
=====================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[DATEDIF](https://exceljet.net/functions/datedif-function)

[TODAY](https://exceljet.net/functions/today-function)

[DATE](https://exceljet.net/functions/date-function)

[YEARFRAC](https://exceljet.net/functions/yearfrac-function)

[INT](https://exceljet.net/functions/int-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6377/download?token=uaWrf8TH)
 (15.78 KB)

![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")

Summary
-------

To calculate age from a birthdate, you can use the [DATEDIF function](https://exceljet.net/functions/datedif-function)
 together with the [TODAY function](https://exceljet.net/functions/today-function)
. In the example shown, the formula in cell E5, copied down, is:

    =DATEDIF(D5,TODAY(),"y")
    

Because TODAY always returns the current date, the formula will continue to calculate the correct age in the future.

Generic formula
---------------

    =DATEDIF(birthdate,TODAY(),"y")

Explanation 
------------

The [DATEDIF function](https://exceljet.net/functions/datedif-function)
 (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the interval between two dates in years, months, and days.

In the example shown, the goal is to calculate age in years. The formula in E5 is:

    =DATEDIF(D5,TODAY(),"y")
    

The first two arguments for DATEDIF are start\_date and end\_date. The start date comes from cell D5 (May 15, 2001) in the example. The end date is generated with the TODAY function. TODAY always returns the current date in Excel. As of this writing, the current date is November 24, 2020. The last argument in DATEDIF specifies the time unit. The DATEDIF function [supports several options here](https://exceljet.net/functions/datedif-function)
, but for this example the goal is age in whole years, so we use "y" to specify complete years.

At this point, we can rewrite the formula as below:

    =DATEDIF("15-May-2001","24-Nov-2020", "y")
    

Because [Excel dates are actually serial numbers](https://exceljet.net/glossary/excel-date)
, the raw values are:

    =DATEDIF(37026,44159,"y")
    

With these inputs, DATEDIF returns 19 as a final result.

### Age on specific date

To calculate age on a specific date, replace the TODAY function with the target date. An easy and safe way to hardcode a specific date into a formula is to use the [DATE function](https://exceljet.net/functions/date-function)
. For example, to calculate age as of January 1, 2021, you can use a formula like this:

    =DATEDIF(D5,DATE(2022,1,1),"y") // returns 20
    

This formula will return Michael Chang's age on January 1, 2022, which is 20.

### Adult or Minor

To check a birthdate and return "Minor" or "Adult", you can wrap the formula in the [IF function](https://exceljet.net/functions/if-function)
 like so:

    =IF(DATEDIF(D5,TODAY(),"y")<18,"Minor","Adult")
    

The above formula is an example of [nesting](https://exceljet.net/glossary/nesting)
. Replace 18 with whatever age is appropriate.

### Age in years, months, and days

To calculate age in years, months, and days, use three instances of DATEDIF like this:

    =DATEDIF(A1,TODAY(),"y")&"y "&DATEDIF(A1,TODAY(),"ym")&"m "&DATEDIF(A1,TODAY(),"md")&"d"
    

The first instance of DATEDIF returns years, the second instance returns months, and the third instance returns days. This is an example of [concatenation](https://exceljet.net/glossary/concatenation)
, and the result is a [text string](https://exceljet.net/glossary/text-value)
 like this:

    19y 6m 9d
    

Note start and end dates remain the same in all three DATEDIFs; only the unit is changed.

###  YEARFRAC with INT

Another option for calculating age from birthdate uses the [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
 together with the INT function in a formula like this:

    =INT(YEARFRAC(D5,TODAY()))
    

YEARFRAC calculates a decimal number representing the fraction of a year between two dates. To work out the fraction of a year as a decimal value, Excel uses days between two dates. As above, the birthdate is provided as the start\_date from cell D5, and today's date is supplied as the end\_date, courtesy of the TODAY function.

With a current date of November 24, 2020, the result from YEARFRAC for Michael Chang is:

    19.5290896646133
    

Next, the [INT function](https://exceljet.net/functions/int-function)
 takes over and rounds down that number to the integer value, which is the number 19.

    =INT(19.5290896646133) // returns 19
    

This formula appears perfectly logical and it works fine in most cases. However, YEARFRAC can return a number that isn't correct on anniversary dates (birthdays). I'm not sure exactly why this happens, but it is related to how YEARFRAC uses days to determine fractional years, which is controlled by the [basis argument](https://exceljet.net/functions/yearfrac-function)
.  For example:

    =YEARFRAC(DATE(1960,6,30),DATE(1962,6,30),1) // 1.998, should be 2
    =YEARFRAC(DATE(1960,3,3),DATE(1964,3,3),1) // 3.998, should be 4
    

The bottom line is that the date DATEDIF formula is a safer and easier option when the goal is to report age in whole years.

Related formulas
----------------

[![Excel formula: Calculate retirement date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20retirement%20date.png "Excel formula: Calculate retirement date")](https://exceljet.net/formulas/calculate-retirement-date)

### [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)

In this example, the goal is to calculate a retirement date at age 60, based on a given birthdate. The simplest way to do this is with the EDATE function. The EDATE function will return a date n months in the future or past when given a date and the number of months to traverse. In this case, we...

[![Excel formula: Calculate years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate_years_between_dates.png "Excel formula: Calculate years between dates")](https://exceljet.net/formulas/calculate-years-between-dates)

### [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)

In this example, the goal is to calculate the number of years between a start date in column B and an end date in column C. An easy way to solve this problem is to use the YEARFRAC function, which returns the number of years between any two dates as a decimal number. YEARFRAC function The YEARFRAC...

[![Excel formula: Get days, months, and years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20months%20and%20years%20between%20dates.png "Excel formula: Get days, months, and years between dates")](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

### [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

In this example, the goal is to output the time between a start date and an end date as a text string that lists years, months, and days separately. For example, given a start date of 1-Jan-2018 and an end date of 1-Jul-2018, the result should be a string like this: "1 years, 6 months, 0 days"...

[![Excel formula: Next anniversary date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20anniversary%20date.png "Excel formula: Next anniversary date")](https://exceljet.net/formulas/next-anniversary-date)

### [Next anniversary date](https://exceljet.net/formulas/next-anniversary-date)

Working from the inside out, we use the DATEDIF function to calculate how many complete years are between the original anniversary date and the "as of" date, where the as of date is any date after the anniversary date: DATEDIF(B5,C5,"y") Note: in this case, we are arbitrarily fixing the "as of"...

Related functions
-----------------

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel YEARFRAC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_yearfrac_function.png "Excel YEARFRAC function")](https://exceljet.net/functions/yearfrac-function)

### [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)

The Excel YEARFRAC function returns a decimal value that represents fractional years between two dates. You can use YEARFRAC to do things like calculate age with a birthdate....

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)
    
*   [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)
    
*   [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    
*   [Next anniversary date](https://exceljet.net/formulas/next-anniversary-date)
    

### Functions

*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    

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