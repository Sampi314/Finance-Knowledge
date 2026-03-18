# Calculate days remaining - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-days-remaining

---

[Skip to main content](https://exceljet.net/formulas/calculate-days-remaining#main-content)

[](https://exceljet.net/formulas/calculate-days-remaining#)

*   [Previous](https://exceljet.net/formulas/calculate-days-open)
    
*   [Next](https://exceljet.net/formulas/calculate-expiration-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Calculate days remaining
========================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Calculate days remaining](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20days%20remaining.png "Excel formula: Calculate days remaining")

Summary
-------

To calculate the days remaining from one date to another, you can use a simple formula that subtracts the earlier date from the later date. In the example shown, the formula in D5 is:

    =C5-B5
    

Generic formula
---------------

    =end_date-start_date

Explanation 
------------

[Dates in Excel are just serial numbers](https://exceljet.net/glossary/excel-date)
 that begin on January 1, 1900. If you enter 1/1/1900 in Excel, and format the result with the "General" [number format](https://exceljet.net/glossary/number-format)
, you'll see the number 1. This means that you can easily calculate the days between two dates by subtracting the earlier date from the later date.

In the example shown, the formula is solved like this:

    =C5-B5
    =42735-42370
    =365
    

### Days remaining from today

If you need to calculate days remaining from today, use the [TODAY function](https://exceljet.net/functions/today-function)
 like so:

    =end_date-TODAY()
    

The TODAY function will always return the current date. Note that after the end\_date has passed, you'll start to see negative results, because the value returned by TODAY will be greater than the end date.

You can use this version of the formula to count down days to an important event or milestone, count down days until a membership expires, etc.

### Remaining workdays

To count remaining workdays, see the [NETWORKDAYS function](https://exceljet.net/functions/networkdays-function)
 and the example [here](https://exceljet.net/formulas/get-workdays-between-dates)
.

Related formulas
----------------

[![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")](https://exceljet.net/formulas/get-days-between-dates)

### [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)

Dates in Excel are serial numbers that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this: =C6-B6 =...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Calculate days open](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20days%20open.png "Excel formula: Calculate days open")](https://exceljet.net/formulas/calculate-days-open)

### [Calculate days open](https://exceljet.net/formulas/calculate-days-open)

In this example, the goal is to calculate the number of days a ticket/case/issue has been open. We start counting on the date a ticket was opened and stop counting on the date a ticket was closed. If there is no closed date, the ticket is still open. Because dates in Excel are just serial numbers...

Related functions
-----------------

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

### Formulas

*   [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)
    
*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Calculate days open](https://exceljet.net/formulas/calculate-days-open)
    

### Functions

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