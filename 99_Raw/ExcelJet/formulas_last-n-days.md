# Last n days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-n-days

---

[Skip to main content](https://exceljet.net/formulas/last-n-days#main-content)

[](https://exceljet.net/formulas/last-n-days#)

*   [Previous](https://exceljet.net/formulas/join-date-and-text)
    
*   [Next](https://exceljet.net/formulas/last-n-months)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Last n days
===========

by Dave Bruns · Updated 31 Oct 2023

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Last n days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/last%207%20days.png "Excel formula: Last n days")

Summary
-------

To check if a date is within the last n days of today's date, you can use a formula based on the TODAY and AND functions. In the example shown, we are checking for dates in the last 7 days. The formula in D5, copied down, is:

    =AND(B5>=(TODAY()-7),B5<TODAY())
    

You can use a formula like this for [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
, or to [filter data in a Pivot Table](https://exceljet.net/pivot-tables/pivot-table-last-7-days)
.

Generic formula
---------------

    =AND(A1>=(TODAY()-n),A1<TODAY())

Explanation 
------------

In the image shown, the current date is August 19, 2019.

[Excel dates are serial numbers](https://exceljet.net/glossary/excel-date)
, so you can manipulate them with simple math operations. The [TODAY function](https://exceljet.net/functions/today-function)
 always returns the current date. Inside the [AND function](https://exceljet.net/functions/and-function)
, the first logical test checks to see if the date in B5 is greater than or equal to today's date minus 7 days:

    =B5>=(TODAY()-7)<TODAY())
    

The second logical test checks if the date is less than today:

    B5<TODAY()
    

when both results are TRUE, the AND function will return TRUE. If either result is FALSE, the AND function will return FALSE.

### Without future checks

The second test is meant to exclude any dates greater than (or equal to) today. This test only makes sense if data may include dates in the future, for example forecasts or estimates. If there are no future dates, or if you _want_ future dates included, the formula can be simplified to:

    =B5>=(TODAY()-7)<TODAY())
    

### Return custom value

This formula can be combined with the [IF function](https://exceljet.net/functions/if-function)
 to return any value you want. For example, to return "Last 7" when a date is within last 7 days, and nothing if not, you can use:

    =IF(AND(B5>=(TODAY()-7),B5<TODAY()),"Last 7", "")
    

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

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