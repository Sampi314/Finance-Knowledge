# Get quarter from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-quarter-from-date

---

[Skip to main content](https://exceljet.net/formulas/get-quarter-from-date#main-content)

[](https://exceljet.net/formulas/get-quarter-from-date#)

*   [Previous](https://exceljet.net/formulas/get-project-start-date)
    
*   [Next](https://exceljet.net/formulas/get-same-date-next-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get quarter from date
=====================

by Dave Bruns · Updated 24 Jan 2025

Related functions 
------------------

[MONTH](https://exceljet.net/functions/month-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

![Excel formula: Get quarter from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20quarter%20from%20date.png "Excel formula: Get quarter from date")

Summary
-------

To calculate the quarter (i.e. 1,2,3,4) for a given date, you can use the [ROUNDUP function](https://exceljet.net/functions/roundup-function)
 together with the [MONTH function](https://exceljet.net/functions/month-function)
. In the example shown, the formula in cell C5 is:

    =ROUNDUP(MONTH(B5)/3,0)
    

The result is 1 since January 31 is in the first quarter.

> This formula returns a standard quarter, where Q1 begins in December. See [this formula](https://exceljet.net/formulas/get-fiscal-quarter-from-date)
>  to get a fiscal quarter.

Generic formula
---------------

    =ROUNDUP(MONTH(date)/3,0)

Explanation 
------------

In this example, the goal is to return a number that represents quarter (i.e. 1,2,3,4) for any given date. In other words, we want to return the quarter that the date resides in.

### ROUNDUP formula solution

In the example shown, the formula in cell C5 is:

    =ROUNDUP(MONTH(B5)/3,0)
    

The ROUNDUP function works like the [ROUND function](https://exceljet.net/functions/round-function)
, except that ROUNDUP will always round numbers 1-9 up to a given number of digits, supplied as the _num\_digits_ [argument](https://exceljet.net/glossary/function-argument)
. In this case, because we want to get back an integer, we use zero for _num\_digits_.

Working from the inside out, the [MONTH function](https://exceljet.net/functions/month-function)
 first extracts the month as a number between 1-12, then divides this number by 3:

    =MONTH(B5)/3
    =1/3
    =0.3333
    

The result is then rounded up to the nearest whole number using the [ROUNDUP function](https://exceljet.net/functions/roundup-function)
:

    =ROUNDUP(0.3333,0) returns 1
    

The result is 1, since 0.3333 rounded up to the next whole number is 1.

### Adding  "Q"

If you want the quarter number to include a "Q" you can [concatenate](https://exceljet.net/glossary/concatenation)
 the numeric result from ROUNDUP to the "Q". The formula in D5 is:

    ="Q"&ROUNDUP(MONTH(B5)/3,0) // returns "Q1"
    

The result is the letter "Q" prepended to the number:

![Calculating quarter of the year from a date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/get%20quarter%20from%20date2.png?itok=yYhZXnnN "Calculating quarter of the year from a date")

Related formulas
----------------

[![Excel formula: Get fiscal quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20quarter%20from%20date.png "Excel formula: Get fiscal quarter from date")](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

### [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

The choose function uses the first argument to "select" remaining elements. For example, in a scheme where 1 = small, 2 = medium, and 3 = large, this formula will "map" the number 2 to "medium". =CHOOSE(2,"small","medium","large") In the case of fiscal quarters, we can use this same idea to map any...

[![Excel formula: Get fiscal year from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20year%20from%20date.png "Excel formula: Get fiscal year from date")](https://exceljet.net/formulas/get-fiscal-year-from-date)

### [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)

In this example, the goal is to return the fiscal year for any given date, where a fiscal year starts in July as seen in the worksheet. By convention a fiscal year is denoted by the year in which it ends. So, if a fiscal year begins in July, then the date August 1, 2018 is in fiscal year 2019. The...

Related functions
-----------------

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)
    
*   [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)
    

### Functions

*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    

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