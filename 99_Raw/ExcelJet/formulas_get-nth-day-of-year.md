# Get nth day of year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-nth-day-of-year

---

[Skip to main content](https://exceljet.net/formulas/get-nth-day-of-year#main-content)

[](https://exceljet.net/formulas/get-nth-day-of-year#)

*   [Previous](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
    
*   [Next](https://exceljet.net/formulas/get-percent-of-year-complete)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get nth day of year
===================

by Dave Bruns · Updated 20 May 2021

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[YEAR](https://exceljet.net/functions/year-function)

![Excel formula: Get nth day of year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20nth%20day%20of%20year.png "Excel formula: Get nth day of year")

Summary
-------

To get the nth day of year based on a given date, you can use a formula based on the [DATE](https://exceljet.net/functions/date-function)
 and [YEAR](https://exceljet.net/functions/year-function)
 functions. In the example shown, the formula in C5 is:

    =B5-DATE(YEAR(B5),1,0)
    

With the date "January 9, 2018" in cell B5, the formula returns 9, since January 9 is the 9th day of the year.

Generic formula
---------------

    =date-DATE(YEAR(date),1,0)

Explanation 
------------

This formula takes advantage of the fact that [dates are just sequential numbers](https://exceljet.net/glossary/excel-date)
 in Excel. It determines the last day of the previous year and subtracts that value from the original date with this formula:

    =B5-DATE(YEAR(B5),1,0)
    

The result is nth day of the year, based on the date in cell B5. Notice the _day_ argument in the [DATE function](https://exceljet.net/functions/date-function)
 is supplied as zero. A nice feature of DATE is it can handle _day_ values that are "out of range" and adjust the result appropriately. When we give DATE a year for _year_, a 1 for month, and a zero for _day_, the DATE function returns the last day of the _previous_ year:

    DATE(YEAR(B5),1,0) // last day of previous year
    

So, the formula is solved like this

    =B5-DATE(YEAR(B5),1,0)
    =B5-DATE(2018,1,0)
    =43109-43100
    =9
    

### nth day this year

To adjust the formula to return the nth day of year for the current date, just use the [TODAY function](https://exceljet.net/functions/today-function)
 for the date:

    =TODAY()-DATE(YEAR(TODAY()),1,0)
    

The logic of the formula remains the same, but the date values are supplied by the TODAY function.

Related formulas
----------------

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

[![Excel formula: Convert date to Julian format](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20to%20Julian%20format.png "Excel formula: Convert date to Julian format")](https://exceljet.net/formulas/convert-date-to-julian-format)

### [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)

This formula builds the final result in 2 parts, joined by concatenation with the ampersand (...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

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

*   [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)
    
*   [Convert date to Julian format](https://exceljet.net/formulas/convert-date-to-julian-format)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    

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