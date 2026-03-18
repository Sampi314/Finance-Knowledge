# Get days before a date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-days-before-a-date

---

[Skip to main content](https://exceljet.net/formulas/get-days-before-a-date#main-content)

[](https://exceljet.net/formulas/get-days-before-a-date#)

*   [Previous](https://exceljet.net/formulas/get-day-name-from-date)
    
*   [Next](https://exceljet.net/formulas/get-days-between-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get days before a date
======================

by Dave Bruns · Updated 14 Aug 2018

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Get days before a date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_days_before_a_date.png "Excel formula: Get days before a date")

Summary
-------

To calculate the number of days before a certain date, you can use subtraction and the TODAY function. In the example, D5 contains this formula:

    =B4-TODAY()
    

Generic formula
---------------

    =date-TODAY()

Explanation 
------------

In Excel, dates are simply serial numbers. In the standard date system for windows, based on the year 1900, where January 1, 1900 is the number 1. Dates are valid through 9999, which is serial number 2,958,465. This means that January 1, 2050 is the serial number 54,789.

In the example, the date is March 9, 2016, which is the serial number 42,438. So:

    = B4-TODAY()
    = January 1 2050 - April 27, 2014
    = 54,789 - 42,438
    = 12,351
    

This means there are 13,033 days before January 1, 2050, when counting from March 9, 2016.

### Without TODAY

Note: you don't need to use the TODAY function. In the second example, the formula in D6 is:

    =B6-C6
    

### Concatenating with text

In the third example, the same basic formula is used along with concatenation operator (&) to embed the calculated days in a simple text message:

    ="Just "& B6-C6 &" days left!"
    

Since there are 15 days between December 10, 2014 and December 25, 2014, the result is this message: _Just 15 days left!_

### Workdays only

To calculate workdays between dates, you can use the NETWORKDAYS function [as explained here.](https://exceljet.net/formulas/get-workdays-between-dates)

Related formulas
----------------

[![Excel formula: Calculate time before expiration date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_time_before_expiration_date.png "Excel formula: Calculate time before expiration date")](https://exceljet.net/formulas/calculate-time-before-expiration-date)

### [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)

In this example, the goal is to calculate the time remaining before an expiration date. There are many ways to do something like this in Excel, and in this article, we'll look at three different approaches: Calculating the remaining time in days Calculating the remaining time in years, months, and...

[![Excel formula: Calculate expiration date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20expiration%20date.png "Excel formula: Calculate expiration date")](https://exceljet.net/formulas/calculate-expiration-date)

### [Calculate expiration date](https://exceljet.net/formulas/calculate-expiration-date)

In Excel, dates are simply serial numbers. In the standard date system for windows, based on the year 1900, where January 1, 1900 is the number 1. This means that January 1, 2050 is the serial number 54,789. If you are calculating a date n days in the future, you can add days directly as in the...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

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

*   [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)
    
*   [Calculate expiration date](https://exceljet.net/formulas/calculate-expiration-date)
    
*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    

### Functions

*   [TODAY Function](https://exceljet.net/functions/today-function)
    

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