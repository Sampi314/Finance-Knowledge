# Last n months - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-n-months

---

[Skip to main content](https://exceljet.net/formulas/last-n-months#main-content)

[](https://exceljet.net/formulas/last-n-months#)

*   [Previous](https://exceljet.net/formulas/last-n-days)
    
*   [Next](https://exceljet.net/formulas/last-n-weeks)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Last n months
=============

by Dave Bruns · Updated 30 Oct 2021

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[TODAY](https://exceljet.net/functions/today-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: Last n months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/last%20n%20months.png "Excel formula: Last n months")

Summary
-------

To check if a date is within the last n months of today's date, you can use a formula based on the AND, TODAY, and EOMONTH functions. In the example shown, we are checking for dates in the last 6 months. The formula in D5, copied down, is:

    =AND(B5>EOMONTH(TODAY(),-7),B5<=EOMONTH(TODAY(),-1))
    

The result is TRUE for any date in the last complete six month period, starting with the previous month. The TODAY function will continue to return the current date, so you can use a formula like this to create reports based on a rolling 6 months, rolling 12 months, etc.

Generic formula
---------------

    =AND(A1>EOMONTH(TODAY(),-(n+1)),A1<=EOMONTH(TODAY(),-1))

Explanation 
------------

In this example, the goal is to create a formula that will return TRUE if a date is in the last complete 6 month period, starting in the previous month. This means the date must fall between a calculated start date and end date, which requires two logical tests. The formula uses the AND function to require that both logical tests are TRUE. In the example shown, the current date is October 30, 2021. The formula in D5, copied down, is:

    =AND(B5>EOMONTH(TODAY(),-7),B5<=EOMONTH(TODAY(),-1))
    

[Excel dates are serial numbers](https://exceljet.net/glossary/excel-date)
, so you can manipulate them with simple math operations. The [TODAY function](https://exceljet.net/functions/today-function)
 returns the current date on an on-going basis. Inside the [AND function](https://exceljet.net/functions/and-function)
, the first logical test checks to see if the date in B5 is greater than the last day of the month 7 months previous to the current date:

    =B5>EOMONTH(TODAY(),-7) // test 1
    

We use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 to move back in time to the last day of the month 7 months previous the current date, which is calculated with the [TODAY function](https://exceljet.net/functions/today-function)
.

The second logical test checks if the date is less than or equal to the last day of the previous month:

    B5<=EOMONTH(TODAY(),-1) // test 2
    

when both results are TRUE, the AND function will return TRUE. If either result is FALSE, the AND function will return FALSE.

### Last 12 months

To test for the last 12 months, you can adjust the formula like this:

    =AND(B5>EOMONTH(TODAY(),-13),B5<=EOMONTH(TODAY(),-1))
    

### Return custom value

This formula can be combined with the [IF function](https://exceljet.net/functions/if-function)
 to return any value you want. For example, to return "Last 6" when a date is within 6 months, you can use:

    =IF(AND(B5>EOMONTH(TODAY(),-7),B5<=EOMONTH(TODAY(),-1)),"Last 6", "")
    

Related formulas
----------------

[![Excel formula: Last n days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%207%20days.png "Excel formula: Last n days")](https://exceljet.net/formulas/last-n-days)

### [Last n days](https://exceljet.net/formulas/last-n-days)

In the image shown, the current date is August 19, 2019. Excel dates are serial numbers , so you can manipulate them with simple math operations. The TODAY function always returns the current date. Inside the AND function , the first logical test checks to see if the date in B5 is greater than or...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Last n days](https://exceljet.net/formulas/last-n-days)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

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