# Get fiscal quarter from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-fiscal-quarter-from-date

---

[Skip to main content](https://exceljet.net/formulas/get-fiscal-quarter-from-date#main-content)

[](https://exceljet.net/formulas/get-fiscal-quarter-from-date#)

*   [Previous](https://exceljet.net/formulas/get-first-day-of-previous-month)
    
*   [Next](https://exceljet.net/formulas/get-fiscal-year-from-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get fiscal quarter from date
============================

by Dave Bruns · Updated 29 Apr 2023

Related functions 
------------------

[MONTH](https://exceljet.net/functions/month-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

![Excel formula: Get fiscal quarter from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20fiscal%20quarter%20from%20date.png "Excel formula: Get fiscal quarter from date")

Summary
-------

If you want to calculate the fiscal quarter from a date, and the fiscal quarter starts in a month other than January, you can use a formula based on the CHOOSE function.

_Note: if you just need to calculate a "normal" quarter based on a quarter system that starts in January, [you can use this simpler formula](https://exceljet.net/formulas/get-quarter-from-date)
._

In the example shown, the formula in cell D5 is:

    =CHOOSE(MONTH(B5),4,4,4,1,1,1,2,2,2,3,3,3)
    

This formula returns a number, 1-4 that corresponds to a quarter system that begins in April and ends in March.

Generic formula
---------------

    =CHOOSE(MONTH(date),1,1,1,2,2,2,3,3,3,4,4,4)

Explanation 
------------

The choose function uses the first argument to "select" remaining elements. For example, in a scheme where 1 = small, 2 = medium, and 3 = large, this formula will "map" the number 2 to "medium".

    =CHOOSE(2,"small","medium","large")
    

In the case of fiscal quarters, we can use this same idea to map any incoming month (1-12) to one of 4 quarter values. We just need to use the MONTH function to get the month number as the first argument, then provide 12 numbers (one for each month of the year) that are carefully ordered to reflect the fiscal year desired:

    =CHOOSE(MONTH(B5),1,1,1,2,2,2,3,3,3,4,4,4) // Jan start
    =CHOOSE(MONTH(B5),4,4,4,1,1,1,2,2,2,3,3,3) // Apr start
    =CHOOSE(MONTH(B5),3,3,3,4,4,4,1,1,1,2,2,2) // Jul start
    =CHOOSE(MONTH(B5),2,2,2,3,3,3,4,4,4,1,1,1) // Oct start
    

### Adding a Q and year

If you want the quarter number to include a "Q" with a year value, you can concatenate:

    ="Q"&CHOOSE(MONTH(date),1,1,1,2,2,2,3,3,3,4,4,4)&" - "&YEAR(date)
    

Will return values like: "Q1 - 2016", "Q2 - 2016", etc. This works for fiscal years with a January start. If the starting month is different from January, you can use an expression like this to calculate the fiscal year:

    =YEAR(date)+(MONTH(date)>=startmonth)
    

This formula is explained in [more detail here](https://exceljet.net/formulas/get-fiscal-year-from-date)
.

Related formulas
----------------

[![Excel formula: Get quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20quarter%20from%20date.png "Excel formula: Get quarter from date")](https://exceljet.net/formulas/get-quarter-from-date)

### [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)

In this example, the goal is to return a number that represents quarter (i.e. 1,2,3,4) for any given date. In other words, we want to return the quarter that the date resides in. ROUNDUP formula solution In the example shown, the formula in cell C5 is: =ROUNDUP(MONTH(B5)/3,0) The ROUNDUP function...

[![Excel formula: Get fiscal year from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20year%20from%20date.png "Excel formula: Get fiscal year from date")](https://exceljet.net/formulas/get-fiscal-year-from-date)

### [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)

In this example, the goal is to return the fiscal year for any given date, where a fiscal year starts in July as seen in the worksheet. By convention a fiscal year is denoted by the year in which it ends. So, if a fiscal year begins in July, then the date August 1, 2018 is in fiscal year 2019. The...

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

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

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
    
*   [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)
    
*   [Sum by fiscal year](https://exceljet.net/formulas/sum-by-fiscal-year)
    

### Functions

*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    

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