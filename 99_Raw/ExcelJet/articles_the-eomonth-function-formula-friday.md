# The EOMONTH function - Formula Friday | Exceljet

**Source:** https://exceljet.net/articles/the-eomonth-function-formula-friday

---

[Skip to main content](https://exceljet.net/articles/the-eomonth-function-formula-friday#main-content)

[](https://exceljet.net/articles/the-eomonth-function-formula-friday#)

*   [Previous](https://exceljet.net/articles/build-friendly-messages-with-concatenation)
    
*   [Next](https://exceljet.net/articles/concat-textjoin)
    

The EOMONTH function - Formula Friday
=====================================

by Dave Bruns · Updated 20 Oct 2022

![Use the EOMONTH function to get the last day of a month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/eomonth%20get%20last%20day.png)

Summary
-------

The EOMONTH function is one of those little gems in Excel that can save you a lot of trouble. It's a simple function that does just one thing: given a date, it returns the last day of a month. You can use EOMONTH to build all kinds of useful Excel formulas.

The [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 is one of those little gems in Excel that can save you a lot of trouble. It's a simple function that does just one thing: _given a date, it returns the last day of a month._

This may seem a little silly — how hard can it be to figure out the last day of a month? — but it's actually a bit tricky, since each month has a different numbers of days, and February changes in leap years.

### Enter the EOMONTH function

EOMONTH takes two arguments: a start date, and months. _Months_ represents the number of months to move in the future or past. So, for example, with May 12, 2017 in cell B5:

![EOMONTH function basic usage example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/The%20EOMONTH%20function%20basic%20example.png?itok=GK45zb0B "EOMONTH function basic usage example")

    =EOMONTH(B5,0) returns May 31, 2017
    =EOMONTH(B5,4) returns Sep 30, 2017
    =EOMONTH(B5,-3) returns Feb 28, 2017
    

You can easily use EOMONTH to move through years as well:

![EOMONTH function example moving by years](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/The%20EOMONTH%20funtion%20example%20move%20by%20years.png?itok=oixwdA7X "EOMONTH function example moving by years")

    =EOMONTH(B5,12) returns May 31, 2018
    =EOMONTH(B5,36) returns May 31, 2020
    =EOMONTH(B5,-24) returns May 31, 2015
    

You can also use EOMONTH to easily get the first day of the next month:

    =EOMONTH(B5,0)+1 returns Jun 1, 2017
    

### Notes on using EOMONTH

1.  Make sure you give EOMONTH a proper date to start. You can use the [DATE function](https://exceljet.net/functions/date-function)
     if you need to assemble a date from scratch.
2.  Make sure you apply date formatting to the result of EOMONTH, otherwise you may see just a big number.
3.  If you want to move to the \*same\* date in past or future months, use the [EDATE function](https://exceljet.net/functions/edate-function)
    .

### Example formulas built on EOMONTH

Building on EOMONTH's simple utility, you can build all kinds of useful formulas. Here are a few examples to give you some inspiration:

*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    
*   [Days in month](https://exceljet.net/formulas/days-in-month)
    
*   [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)
    
*   [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)
    
*   [Get first day of previous month](https://exceljet.net/formulas/get-first-day-of-previous-month)
    

### More formulas

Want to learn more formulas? Need help with formulas?

We have [more than 500 formulas examples](https://exceljet.net/formulas)
, and [high-quality video training](https://exceljet.net/training)
 if you like learning with a structured program.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

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