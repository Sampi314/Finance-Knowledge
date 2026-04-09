# Excel YEARFRAC function | Exceljet

**Source:** https://exceljet.net/functions/yearfrac-function

---

[Skip to main content](https://exceljet.net/functions/yearfrac-function#main-content)

[](https://exceljet.net/functions/yearfrac-function#)

*   [Previous](https://exceljet.net/functions/year-function)
    
*   [Next](https://exceljet.net/functions/address-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

YEARFRAC Function
=================

by Dave Bruns · Updated 2 Apr 2024

Related functions 
------------------

[DAYS360](https://exceljet.net/functions/days360-function)

[DATEDIF](https://exceljet.net/functions/datedif-function)

![Excel YEARFRAC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_yearfrac_function.png "Excel YEARFRAC function")

Summary
-------

The Excel YEARFRAC function returns a decimal value that represents fractional years between two dates. You can use YEARFRAC to do things like calculate age with a birthdate.

Purpose 
--------

Get the fraction of a year between two dates

Return value 
-------------

A decimal number

Syntax
------

    =YEARFRAC(start_date,end_date,[basis])

*   _start\_date_ - The start date.
*   _end\_date_ - The end date.
*   _basis_ - \[optional\] The type of day count basis to use (see below).

Using the YEARFRAC function 
----------------------------

YEARFRAC returns a decimal number representing years between two dates. For example:

    =YEARFRAC("1-Jan-2019","1-Jan-2020") // returns 1
    =YEARFRAC("1-Jan-2019","1-Jul-2020") // returns 1.5
    =YEARFRAC("1-Jan-2019","1-Jan-2021") // returns 2

Although the generic syntax for YEARFRAC shows the start date followed by the end date, you can provide the dates in any order with the same result. For example:

    =YEARFRAC("1-Jan-2000","1-Jan-2019") // returns 19
    =YEARFRAC("1-Jan-2019","1-Jan-2000") // returns 19

### Basis options

YEARFRAC uses whole days between two dates to calculate the fraction of a year as a decimal number. The YEARFRAC function accepts an optional argument called "basis" that controls how days are counted when computing fractional years. The default behavior is to count days between two dates based on a 360-day year, where all 12 months are considered to have 30 days. The table below summarizes the available options:

| Basis | Calculation | Notes |
| --- | --- | --- |
| 0 (default) | 30/360 | US convention |
| 1   | actual/actual |     |
| 2   | actual/360 |     |
| 3   | actual/365 |     |
| 4   | 30/360 | European convention |

Note that basis 0 (the default) and basis 4 both operate based on a 360-day year, but they handle the last day of the month differently. With the US convention, when the start date is the last day of the month, it is set to the 30th day of the same month. When the end date is the last day of the month, and the start date < 30, the end date is set to the 1st of the next month, otherwise the end date is set to the 30th of the same month. With the European convention, start dates and end dates equal to the 31st of a month are set to the 30th of the same month.

### Examples

With a start date in cell A1, and an end date in cell B1, the YEARFRAC will return years between the two dates as a decimal number:

    =YEARFRAC(A1,B1) // years between two dates 
    

To get a whole number only (not rounded), you can use the [INT function](https://exceljet.net/functions/int-function)
 like this:

    =INT(YEARFRAC(A1,B1)) // whole number only, discard decimal
    

To get current age based on a birthdate, you can use a formula like this:

    =INT(YEARFRAC(birthdate,TODAY())) // age from birthdate
    

_Note: this formula can sometimes return incorrect results. [See this example](https://exceljet.net/formulas/get-age-from-birthday)
 for more details._

To get the percentage of the current year complete, you can use YEARFRAC like this:

    =YEARFRAC(DATE(YEAR(TODAY()),1,1),TODAY()) // % year complete
    

[Full explanation here](https://exceljet.net/formulas/get-percent-of-year-complete)
.

YEARFRAC function examples
--------------------------

[![Excel formula: Get months between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_months_between_dates.png "Excel formula: Get months between dates")](https://exceljet.net/formulas/get-months-between-dates)

### [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)

In this example, the goal is to calculate the number of months between two valid Excel dates . This is a curiously tricky problem in Excel because the number of days in a month varies, and the rules about how a whole month might be calculated are not obvious. In addition, there is not a modern...

[![Excel formula: Calculate years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate_years_between_dates.png "Excel formula: Calculate years between dates")](https://exceljet.net/formulas/calculate-years-between-dates)

### [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)

In this example, the goal is to calculate the number of years between a start date in column B and an end date in column C. An easy way to solve this problem is to use the YEARFRAC function, which returns the number of years between any two dates as a decimal number. YEARFRAC function The YEARFRAC...

[![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")](https://exceljet.net/formulas/get-age-from-birthday)

### [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)

The DATEDIF function (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the...

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

[![Excel formula: Calculate retirement date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20retirement%20date.png "Excel formula: Calculate retirement date")](https://exceljet.net/formulas/calculate-retirement-date)

### [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)

In this example, the goal is to calculate a retirement date at age 60, based on a given birthdate. The simplest way to do this is with the EDATE function. The EDATE function will return a date n months in the future or past when given a date and the number of months to traverse. In this case, we...

YEARFRAC function videos
------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20step%20through%20complex%20formulas%20using%20evaluate-thumb.png)](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)

### [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)

Excel has a handy feature called Evaluate Formula, which solves a formula one step at a time. Each time you click the Evaluate button, Excel will solve the underlined part of the formula and show you the result. Here's the same worksheet we looked at in a previous video when we talked about...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20check%20and%20debug%20a%20formula%20with%20F9.png)](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

### [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

One thing you'll frequently do in Excel is check or debug formulas. In this video, we'll look at how to use the F9 key to quickly break a formula down into pieces that you can understand. Here we have a simple list of names. In addition to names, we have a column for birthdate, a column for age,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20years%20and%20months%20between%20dates-thumb.png)](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)

### [How to calculate years and months between dates](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)

In this video we'll look at how to calculate the number of years or months between dates using a function called DATEDIF and a function called YEARFRAC . The DATEDIF function is a "compatibility" function that comes from Lotus 1-2-3. For reasons that are unknown, it's only documented in Excel 2000...

Related functions
-----------------

[![Excel DAYS360 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20days360%20function.png "Excel DAYS360 function")](https://exceljet.net/functions/days360-function)

### [DAYS360 Function](https://exceljet.net/functions/days360-function)

The Excel DAYS360 function returns the number of days between two dates based on a 360-day year, where all months are assumed to have 30 days. For example, the formula =DAYS360("1-Jan-2021","31-Dec-2021") returns 360 days.

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

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
    
*   [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)
    
*   [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)
    
*   [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)
    
*   [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)
    

### Videos

*   [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
    
*   [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)
    
*   [How to calculate years and months between dates](https://exceljet.net/videos/how-to-calculate-years-and-months-between-dates)
    

### Functions

*   [DAYS360 Function](https://exceljet.net/functions/days360-function)
    
*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    

### Links

*   [Microsoft YEARFRAC function documentation](https://support.office.com/en-us/article/yearfrac-function-3844141e-c76d-4143-82b6-208454ddc6a8)
    

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