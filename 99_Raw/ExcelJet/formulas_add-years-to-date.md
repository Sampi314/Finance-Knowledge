# Add years to date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-years-to-date

---

[Skip to main content](https://exceljet.net/formulas/add-years-to-date#main-content)

[](https://exceljet.net/formulas/add-years-to-date#)

*   [Previous](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)
    
*   [Next](https://exceljet.net/formulas/assign-points-based-on-late-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Add years to date
=================

by Dave Bruns · Updated 21 Nov 2024

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[YEAR](https://exceljet.net/functions/year-function)

[MONTH](https://exceljet.net/functions/month-function)

[DAY](https://exceljet.net/functions/day-function)

[EDATE](https://exceljet.net/functions/edate-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8857/download?token=QlV3GKmh)
 (17.49 KB)

![Excel formula: Add years to date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add_years_to_date.png "Excel formula: Add years to date")

Summary
-------

To add a given number of years to a date, you can use a formula based on the [DATE function](https://exceljet.net/functions/date-function)
 together with the [YEAR](https://exceljet.net/functions/year-function)
, [MONTH](https://exceljet.net/functions/month-function)
, and [DAY](https://exceljet.net/functions/day-function)
 functions. In the example shown, the formula in E5 is:

    =DATE(YEAR(B5)+C5,MONTH(B5),DAY(B5))
    

With the date 8-Mar-1960 in cell B5, and the number 10 in C5, the result in E5 is 8-Mar-1970.

> _Note: This formula can return an incorrect result if the start date is the last day in February in a leap year. See below for a simpler and more robust formula that does not have this problem._

Generic formula
---------------

    =DATE(YEAR(A1)+n,MONTH(A1),DAY(A1))

Explanation 
------------

Ever needed to calculate someone's retirement date? Or figure out when a 30-year mortgage will end? Or maybe you're setting a contract expiration date? In each case, you need a way to add years to a date.

Here's something that might surprise you: most Excel users tackle this problem with a formula that's 3x more complex than it needs to be. And worse, the solution can fail in leap years.

In this guide, I'll show you two ways to add years to dates: the traditional method that everyone learns first (and why it's not always ideal) and a lesser-known but simple and more robust formula that correctly handles the last day in February for leap years. You can use this formula to calculate things like:

*   Contract renewal dates
*   Project milestones
*   Financial maturity dates
*   Employee service anniversaries
*   Insurance policy renewals

### Introduction

In this example, the goal is to use a formula to add or subtract a given number of years (_n_) to a date. The dates are in column B, and the years are in column C. There are two main ways to go about this in Excel. The first method uses the YEAR, MONTH, and DAY functions to take apart the date into separate components: _year_, _month_, and _day_. Then, it adds _n_ to the year and reassembles the components to a date. The second method uses the EDATE function to adjust the date by expressing years as months. Both methods are explained below. But first, let's look at why we can't just add 365 days to a date.

### Why not just add 365?

Before diving into the formulas, it's important to understand [how Excel stores and handles dates](https://exceljet.net/glossary/excel-date)
. Every date in Excel is stored as a number, where January 1, 1900, is day 1, January 2, 1900, is day 2, and so on. As I write this on November 21, 2024, the date number is 45617. Given this system, you might wonder if we can't just add 365 days to move forward a year:

    =A1+365

Or, with _n_ as years, move my a multiple of 365:

    =A1+(n*365)

These formulas will correctly add 365 days (or multiples of 365 days) to a date. While this may seem logical, the problem is not all years have 365 days. Leap years have 366 days, so using 365 will be off by one day after every leap year. Worse, the error compounds over time. Dates far into the future could be off by days or even weeks. We need a more robust method.

### Method 1: DATE + YEAR, MONTH, and DAY

The traditional way to solve this problem is to use the [DATE function](https://exceljet.net/functions/date-function)
 together with the [YEAR](https://exceljet.net/functions/year-function)
, [MONTH](https://exceljet.net/functions/month-function)
, and [DAY](https://exceljet.net/functions/day-function)
 functions.

    =DATE(YEAR(date)+n,MONTH(date),DAY(date))

In the worksheet shown, the formula in E5, copied down, looks like this:

    =DATE(YEAR(B5)+C5,MONTH(B5),DAY(B5))
    

Working from the inside out, the YEAR, MONTH, and DAY functions are used to "take apart" the date into separate components like this:

    =YEAR(B5) // returns 1960
    =MONTH(B5) // returns 3
    =DAY(B5) // returns 8
    

These individual values are then returned to the DATE function, which reassembles the date, adding _n_ to the year value along the way. With the number 10 in cell C5, the formula evaluates like this:

    =DATE(YEAR(B5)+C5,MONTH(B5),DAY(B5))
    =DATE(1960+10,3,8)
    =DATE(1970,3,8)

The formula returns the date March 8, 1970, in this example. When you modify either the initial date in B5 or the year offset in C5, the result automatically updates. This example shows off date manipulation in Excel, demonstrating how to:

*   Break down a date using YEAR, MONTH, and DAY functions
*   Reconstruct it using the DATE function

However, the formula is relatively complex, and there is one small problem: If the starting date falls on February 29 (a leap year) and the calculated end year is _not a leap year_, the result shifts to March 1. See the result in cell E12 for an example.

There is a simpler way to add years to a date, and it doesn't have trouble with leap years. It's based on the EDATE function.

### Method 2: EDATE function

A much simpler way to solve this problem is to use the [EDATE function](https://exceljet.net/functions/edate-function)
. EDATE is designed to move a date by a given number of months. For example, to move a date in cell A1 forward by 6 months, you can use EDATE like this:

    =EDATE(A1,6) // move forward 6 months

We can adapt the formula above to add whole years by multiplying by 12 in a generic formula like this:

    =EDATE(A1,n*12)

In this formula, _n_ represents the number of years to add. To use this approach in the workbook shown, we can enter the following formula in cell E5:

    =EDATE(B5,C5*12)

You can see this formula applied in the worksheet below. Notice the results are the same, _except for the result in E12_:

![Adding years to a date with the EDATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/add_years_to_date_with_EDATE.png "Adding years to a date with the EDATE function")

EDATE handles month-end dates intelligently. The date in cell B12 is February 29, 2024. When adding one year, EDATE recognizes that February 29, 2024 is the last day of a leap year month. Since 2025 is not a leap year, EDATE automatically adjusts the result to February 28, 2025 – preserving the "end-of-month" logic.

### Summary

We looked at two methods to add years to a date with a formula: (1) the DATE function combined with YEAR, MONTH, and DAY functions, and (2) the EDATE function. The first method splits the date into parts, adjusts the year, and then reassembles the date. The second method, using the EDATE function, shifts the date by a specified number of months. Both methods work well. Both can handle dates far into the future, as well as negative year adjustments. However, I recommend the EDATE approach because it has some nice advantages:

*   Much simpler formula with less room for error
*   No leap year problem
*   Easier to maintain and modify

Download the example workbook to try the formulas out yourself.

Related formulas
----------------

[![Excel formula: Add months to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_months_to_date.png "Excel formula: Add months to date")](https://exceljet.net/formulas/add-months-to-date)

### [Add months to date](https://exceljet.net/formulas/add-months-to-date)

In this example, the goal is to add a given number of months to a date. If the number of months is positive, the date should move forward. If the number of months is negative, the date should move backward. The standard solution for this problem in Excel is to use the EDATE function although in...

[![Excel formula: Add days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_days_to_date.png "Excel formula: Add days to date")](https://exceljet.net/formulas/add-days-to-date)

### [Add days to date](https://exceljet.net/formulas/add-days-to-date)

In this example, the goal is to add days to a date. This is a frequent task in Excel when you need to calculate a new date by adding a specified number of days to an existing date. Here are some examples of situations where this might be useful: Calculate a due date by adding a given number of days...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add months to date](https://exceljet.net/formulas/add-months-to-date)
    
*   [Add days to date](https://exceljet.net/formulas/add-days-to-date)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [DAY Function](https://exceljet.net/functions/day-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    

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