# Get fiscal year from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-fiscal-year-from-date

---

[Skip to main content](https://exceljet.net/formulas/get-fiscal-year-from-date#main-content)

[](https://exceljet.net/formulas/get-fiscal-year-from-date#)

*   [Previous](https://exceljet.net/formulas/get-fiscal-quarter-from-date)
    
*   [Next](https://exceljet.net/formulas/get-last-day-of-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get fiscal year from date
=========================

by Dave Bruns · Updated 21 Apr 2021

Related functions 
------------------

[MONTH](https://exceljet.net/functions/month-function)

[YEAR](https://exceljet.net/functions/year-function)

![Excel formula: Get fiscal year from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20fiscal%20year%20from%20date.png "Excel formula: Get fiscal year from date")

Summary
-------

To get a fiscal year from a date, you can use a formula based on the [YEAR](https://exceljet.net/functions/year-function)
 and [MONTH](https://exceljet.net/functions/month-function)
 functions. In the example shown, the formula in D5 is:

    =YEAR(B5)+(MONTH(B5)>=C5)
    

The result in column D is the fiscal year for each date, based on a fiscal year start in July.

Generic formula
---------------

    =YEAR(date)+(MONTH(date)>=startmonth)

Explanation 
------------

In this example, the goal is to return the fiscal year for any given date, where a fiscal year starts in July as seen in the worksheet. By convention a fiscal year is denoted by the year in which it ends. So, if a fiscal year begins in July, then the date August 1, 2018 is in fiscal year 2019. The formula in D5, copied down, is:

    =YEAR(B5)+(MONTH(B5)>=C5)
    

On the left, the [YEAR function](https://exceljet.net/functions/year-function)
 first returns the year from the date in B5:

    =YEAR(B5) // returns 2017
    

To adjust this value to return the fiscal year for a July start, the following [boolean expression](https://exceljet.net/glossary/boolean-logic)
 is added to the year value:

    +(MONTH(B5)>=C5) // returns zero
    

Here, the [MONTH function](https://exceljet.net/functions/month-function)
 returns the month from the date in B5 (1), and this result is compared to the start month in C5 (7). Since 1 is less than 7, the expression returns FALSE, which is [evaluated by Excel as zero](https://exceljet.net/videos/introduction-to-booleans)
 (0). The zero has no effect, so the final result is 2017. In cases where the month number for a date is greater than 7, this expression will return TRUE, which will be evaluated as 1 by Excel. This increments the year by one.

_Note: with [boolean logic](https://exceljet.net/glossary/boolean-logic)
, TRUE values are evaluated as 1 and FALSE values are evaluated as zero. Therefore, if the month from the date is greater than or equal to the start month, the expression returns TRUE, or 1. If not, the expression returns FALSE, or zero._

Related formulas
----------------

[![Excel formula: Get quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20quarter%20from%20date.png "Excel formula: Get quarter from date")](https://exceljet.net/formulas/get-quarter-from-date)

### [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)

In this example, the goal is to return a number that represents quarter (i.e. 1,2,3,4) for any given date. In other words, we want to return the quarter that the date resides in. ROUNDUP formula solution In the example shown, the formula in cell C5 is: =ROUNDUP(MONTH(B5)/3,0) The ROUNDUP function...

[![Excel formula: Get fiscal quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20quarter%20from%20date.png "Excel formula: Get fiscal quarter from date")](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

### [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

The choose function uses the first argument to "select" remaining elements. For example, in a scheme where 1 = small, 2 = medium, and 3 = large, this formula will "map" the number 2 to "medium". =CHOOSE(2,"small","medium","large") In the case of fiscal quarters, we can use this same idea to map any...

[![Excel formula: Sum by fiscal year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20fiscal%20year.png "Excel formula: Sum by fiscal year")](https://exceljet.net/formulas/sum-by-fiscal-year)

### [Sum by fiscal year](https://exceljet.net/formulas/sum-by-fiscal-year)

The goal of this example is to sum amounts by fiscal year, when the fiscal year begins in July. The first approach is a self-contained formula based on the SUMPRODUCT function. The second method uses SUMIF with column D as a helper column. Either approach will work correctly, and the best option...

Related functions
-----------------

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)
    
*   [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)
    
*   [Sum by fiscal year](https://exceljet.net/formulas/sum-by-fiscal-year)
    

### Functions

*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    

### Links

*   [Fiscal year explanation (wikipedia)](https://en.wikipedia.org/wiki/Fiscal_year)
    

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