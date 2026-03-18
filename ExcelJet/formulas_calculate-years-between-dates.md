# Calculate years between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-years-between-dates

---

[Skip to main content](https://exceljet.net/formulas/calculate-years-between-dates#main-content)

[](https://exceljet.net/formulas/calculate-years-between-dates#)

*   [Previous](https://exceljet.net/formulas/calculate-time-before-expiration-date)
    
*   [Next](https://exceljet.net/formulas/convert-date-string-to-date-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Calculate years between dates
=============================

by Dave Bruns · Updated 2 Apr 2024

Related functions 
------------------

[YEARFRAC](https://exceljet.net/functions/yearfrac-function)

[INT](https://exceljet.net/functions/int-function)

![Excel formula: Calculate years between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Calculate_years_between_dates.png "Excel formula: Calculate years between dates")

Summary
-------

To calculate the number of years between two dates, you can use the [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
, which will return a decimal number representing the fraction of a year between two dates. In the example shown, the formula in D5 is:

    =YEARFRAC(B6,C6)
    

As the formula is copied down, it returns the number of years between each start and end date as a decimal number. In the example shown, column D results use a [number format](https://exceljet.net/articles/custom-number-formats)
 with 2 decimal places.

Generic formula
---------------

    =YEARFRAC(start_date,end_date)

Explanation 
------------

In this example, the goal is to calculate the number of years between a start date in column B and an end date in column C. An easy way to solve this problem is to use the YEARFRAC function, which returns the number of years between any two dates as a decimal number.

### YEARFRAC function

The [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
 returns a decimal number representing the fraction of a year between two valid [Excel dates](https://exceljet.net/glossary/excel-date)
. the generic syntax for YEARFRAC looks like this:

    =YEARFRAC(start_date,end_date)

For example, here are a few results from YEARFRAC with some hardcoded dates:

    =YEARFRAC("1-Jan-2019","1-Jan-2020") // returns 1
    =YEARFRAC("1-Jan-2019","1-Jul-2020") // returns 1.5
    =YEARFRAC("1-Jan-2019","1-Jan-2021") // returns 2

In the worksheet shown, the formula used to calculate years between dates in cell D5 looks like this:

    =YEARFRAC(B5,C5) // returns 1

As the formula is copied down, it returns the number of years between each start and end date as a decimal number.

|     |     |     |
| --- | --- | --- |
| Start date | End date | Result |
| 1-Jan-2015 | 1-Jan-2016 | 1.00 |
| 1-Jan-2015 | 1-Jan-2020 | 5.00 |
| 1-Apr-2024 | 1-Apr-2054 | 30.00 |
| 15-Mar-1970 | 15-Sep-1976 | 6.50 |

### Rounding results

Once you have the decimal number from YEARFRAC, you can round the number as you like. For example, you could round to the nearest whole number with the [ROUND function](https://exceljet.net/functions/round-function)
:

    =ROUND(YEARFRAC(A1,B1),0)
    

### Whole years only

You might also want to keep only the integer portion of the result with no decimal value so that you are only counting whole years. In that case, you can wrap YEARFRAC in the [INT function](https://exceljet.net/functions/int-function)
 like this:

    =INT(YEARFRAC(A1,B1))
    

The INT function removes the decimal portion of the number altogether. If you need to calculate years on an ongoing basis, for example, to calculate current age based on a birthday, [see the example here](https://exceljet.net/formulas/get-age-from-birthday)
.

_Note: The YEARFRAC function has an optional 3rd argument that controls how days are counted when computing fractional years. The default behavior is to count days between two dates based on a 360-day year, where all 12 months are considered to have 30 days. The [YEARFRAC page](https://exceljet.net/functions/yearfrac-function)
 provides more information._

Related formulas
----------------

[![Excel formula: Get age from birthday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20age%20from%20birthdate.png "Excel formula: Get age from birthday")](https://exceljet.net/formulas/get-age-from-birthday)

### [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)

The DATEDIF function (Date + Dif) is a bit of an anomaly in Excel. A compatibility function that comes originally from Lotus 1-2-3, Excel will not help supply arguments when the function is entered. However, DATEDIF works in all modern versions of Excel and is a useful function for calculating the...

Related functions
-----------------

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

*   [Get age from birthday](https://exceljet.net/formulas/get-age-from-birthday)
    

### Functions

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