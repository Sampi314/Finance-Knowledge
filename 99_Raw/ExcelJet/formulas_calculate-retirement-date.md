# Calculate retirement date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-retirement-date

---

[Skip to main content](https://exceljet.net/formulas/calculate-retirement-date#main-content)

[](https://exceljet.net/formulas/calculate-retirement-date#)

*   [Previous](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Next](https://exceljet.net/formulas/calculate-time-before-expiration-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Calculate retirement date
=========================

by Dave Bruns · Updated 25 Oct 2023

Related functions 
------------------

[EDATE](https://exceljet.net/functions/edate-function)

[YEARFRAC](https://exceljet.net/functions/yearfrac-function)

[SIGN](https://exceljet.net/functions/sign-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6841/download?token=4raOHeew)
 (14.67 KB)

![Excel formula: Calculate retirement date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20retirement%20date.png "Excel formula: Calculate retirement date")

Summary
-------

To calculate a retirement date based on a birthdate, you can use the [EDATE function](https://exceljet.net/functions/edate-function)
. In the example shown, the formula in D6 is:

    =EDATE(C6,12*60)
    

The result is a date 60 years (720 months) from the date of birth in column C.

_Note: At the time of this writing, the current date is September 2, 2021. This is the date used to calculate the remaining years in column F._

Generic formula
---------------

    =EDATE(A1,12*years)

Explanation 
------------

In this example, the goal is to calculate a retirement date at age 60, based on a given birthdate. The simplest way to do this is with the EDATE function. The [EDATE function](https://exceljet.net/functions/edate-function)
 will return a date **n** months in the future or past when given a date and the number of months to traverse. In this case, we want a date 60 years from the birthdate in column C, so the formula in D5 is:

    =EDATE(C5,12*60) // 60 years from birthdate
    

The _date_ comes from column C. For _months_, we need the equivalent of 60 years in months. Since most people don't know how many months are in 60 years, a nice way to do this is to embed the calculation in the formula like this:

    12*60 // 720 months = 60 years
    

Inside the EDATE function, Excel will perform the math and return 720 directly to EDATE as the _months_ [argument](https://exceljet.net/glossary/function-argument)
. Embedding calculations this way can help make the assumptions and purpose of a formula easier to understand. To use a retirement age of 65, just adjust the calculation:

    12*65 // 780 months = 65 years
    

In cell D5, returns the date March 10, 2023. As the formula is copied down column D, a different date is returned for each person in the list based on their birthdate.

_Note: EDATE returns a date as a [serial number](https://exceljet.net/glossary/excel-date)
, so apply a date [number format](https://exceljet.net/glossary/number-format)
 to display as a date._

### End of month

To calculate a retirement date that lands at the end of the month, you can use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 instead of the EDATE function like this:

    =EOMONTH(C5,12*60) // +60 years at end of month
    

EOMONTH works like EDATE, but always returns the end of the month. If there is a rule that people with birthdays that fall on the first of the month retire on the last day of the previous month, the formula can be adjusted like this:

    =EOMONTH(C5,(12*60)-(DAY(C5)=1))
    

Here, the logical expression DAY(C5)=1 is subtracted from 12\*60 = 720. The [DAY function](https://exceljet.net/functions/day-function)
 returns the day of the birthdate. If the day is 1, the expression returns TRUE. Otherwise, the expression returns FALSE. The math operation of subtraction coerces TRUE to 1 and FALSE to zero. The result is that EOMONTH moves forward 719 months if a birthday falls on the first of the month, and 720 months if not. This moves first-of-month birthdays to the last day of the previous month.

### Year only

To return the retirement year only, we can [nest](https://exceljet.net/glossary/nesting)
 EDATE inside the [YEAR function](https://exceljet.net/functions/year-function)
 like this:

    =YEAR(EDATE(C5,12*60)) // return year only
    

Since we already have the date in column D, the formula in column E is:

    =YEAR(D5) // year from date in D5
    

The YEAR function returns the year of the date returned by EDATE.

### Years remaining

In column F, we calculate the years remaining with the YEARFRAC function like this:

    =YEARFRAC(TODAY(),D5)
    

This formula returns the difference between today's date and the calculated retirement date in column D. As the retirement date approaches, the years remaining will automatically decrease. To guard against a retirement date that has already passed, the formula in column F uses the [SIGN function](https://exceljet.net/functions/sign-function)
 to change the years remaining to a negative number like this:

    =YEARFRAC(TODAY(),D5)*SIGN(D5-TODAY()) // make negative if past
    

The SIGN function simply returns the sign of a number as 1, -1, or 0. To use it, we subtract today's date from the retirement date. If the result is positive, the retirement date is in the future and SIGN returns 1, which does not affect the result from YEARFRAC. If the result is negative, the retirement date is in the past and SIGN returns -1, flipping the YEARFRAC calculation to a negative number. You can see the result in row 8, where the retirement date has already passed.

### Other uses

This same approach can be used to calculate dates for a wide variety of use cases:

*   Warranty expiration dates
*   Membership expiration dates
*   Promotional period end date
*   Shelf life expiration
*   Inspection dates
*   Certification expiration

Related formulas
----------------

[![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")](https://exceljet.net/formulas/get-age-from-birthday)

### [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)

The DATEDIF function (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the...

[![Excel formula: Calculate years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate_years_between_dates.png "Excel formula: Calculate years between dates")](https://exceljet.net/formulas/calculate-years-between-dates)

### [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)

In this example, the goal is to calculate the number of years between a start date in column B and an end date in column C. An easy way to solve this problem is to use the YEARFRAC function, which returns the number of years between any two dates as a decimal number. YEARFRAC function The YEARFRAC...

[![Excel formula: Get same date next year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20same%20date%20next%20year.png "Excel formula: Get same date next year")](https://exceljet.net/formulas/get-same-date-next-year)

### [Get same date next year](https://exceljet.net/formulas/get-same-date-next-year)

EDATE can get the "same date" in the future or past, based on the number of months supplied. When 12 is given for months, EDATE gets the same date next year. Same date in previous year To get the same date in a previous month, use -12: =EDATE(date,-12) // prior year

[![Excel formula: Next business day 6 months in future](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20business%20day%206%20months%20in%20future.png "Excel formula: Next business day 6 months in future")](https://exceljet.net/formulas/next-business-day-6-months-in-future)

### [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)

Working from the inside out, EDATE first calculates a date 6 months in the future. In the example shown, that date is December 24, 2015. Next, the formula subtracts 1 day to get December 23, 2015, and the result goes into the WORKDAY function as the start date, with days = 1, and the range B9:B11...

[![Excel formula: Next anniversary date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20anniversary%20date.png "Excel formula: Next anniversary date")](https://exceljet.net/formulas/next-anniversary-date)

### [Next anniversary date](https://exceljet.net/formulas/next-anniversary-date)

Working from the inside out, we use the DATEDIF function to calculate how many complete years are between the original anniversary date and the "as of" date, where the as of date is any date after the anniversary date: DATEDIF(B5,C5,"y") Note: in this case, we are arbitrarily fixing the "as of"...

Related functions
-----------------

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel YEARFRAC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_yearfrac_function.png "Excel YEARFRAC function")](https://exceljet.net/functions/yearfrac-function)

### [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)

The Excel YEARFRAC function returns a decimal value that represents fractional years between two dates. You can use YEARFRAC to do things like calculate age with a birthdate....

[![Excel SIGN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sign%20function.png "Excel SIGN function")](https://exceljet.net/functions/sign-function)

### [SIGN Function](https://exceljet.net/functions/sign-function)

The Excel SIGN function returns the sign of a number as +1, -1 or 0. If _number_ is positive, SIGN returns 1. If _number_ is negative, sign returns -1. If _number_ is zero, SIGN returns 0.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20expiration%20dates.png)](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)

### [How to calculate and highlight expiration dates](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)

In this video we'll look at how to calculate and highlight expiration dates. Let's say your company has started a membership program of some kind and your boss just sent you a set of data. She's given you a list of 1,000 people that have renewed a membership in the last year or so, and she's...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)
    
*   [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)
    
*   [Get same date next year](https://exceljet.net/formulas/get-same-date-next-year)
    
*   [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    
*   [Next anniversary date](https://exceljet.net/formulas/next-anniversary-date)
    

### Functions

*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)
    
*   [SIGN Function](https://exceljet.net/functions/sign-function)
    

### Videos

*   [How to calculate and highlight expiration dates](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)
    

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