# Calculate expiration date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-expiration-date

---

[Skip to main content](https://exceljet.net/formulas/calculate-expiration-date#main-content)

[](https://exceljet.net/formulas/calculate-expiration-date#)

*   [Previous](https://exceljet.net/formulas/calculate-days-remaining)
    
*   [Next](https://exceljet.net/formulas/calculate-hours-between-two-times)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Calculate expiration date
=========================

by Dave Bruns · Updated 14 Jan 2017

Related functions 
------------------

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[EDATE](https://exceljet.net/functions/edate-function)

![Excel formula: Calculate expiration date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20expiration%20date.png "Excel formula: Calculate expiration date")

Summary
-------

To calculate an expiration in the future, you can use a variety of formulas. In the example shown, the formulas used in column D are:

    =B5+30 // 30 days
    =B5+90 // 90 days
    =EOMONTH(B7,0) // end of month
    =EDATE(B8,1) // next month
    =EOMONTH(B7,0)+1 // 1st of next month
    =EDATE(B10,12) // 1 year
    

Generic formula
---------------

    =A1+30 // 30 days

Explanation 
------------

In Excel, dates are simply serial numbers. In the standard date system for windows, based on the year 1900, where January 1, 1900 is the number 1. This means that January 1, 2050 is the serial number 54,789.

*   If you are calculating a date n days in the future, you can add days directly as in the first two formulas.
*   If you want to count by months, you can use the EDATE function, which returns the same date n months in the future or past.
*   If you need an expiration date at the end month, use the EOMONTH function, which returns the last day of the month, n months in the future or past.
*   An easy way to calculate the 1st day of a month is to use EOMONTH to get the last day of the previous month, then simply add 1 day.

Related formulas
----------------

[![Excel formula: Calculate time before expiration date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_time_before_expiration_date.png "Excel formula: Calculate time before expiration date")](https://exceljet.net/formulas/calculate-time-before-expiration-date)

### [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)

In this example, the goal is to calculate the time remaining before an expiration date. There are many ways to do something like this in Excel, and in this article, we'll look at three different approaches: Calculating the remaining time in days Calculating the remaining time in years, months, and...

[![Excel formula: Get days before a date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_days_before_a_date.png "Excel formula: Get days before a date")](https://exceljet.net/formulas/get-days-before-a-date)

### [Get days before a date](https://exceljet.net/formulas/get-days-before-a-date)

In Excel, dates are simply serial numbers. In the standard date system for windows, based on the year 1900, where January 1, 1900 is the number 1. Dates are valid through 9999, which is serial number 2,958,465. This means that January 1, 2050 is the serial number 54,789. In the example, the date is...

Related functions
-----------------

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

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
    
*   [Get days before a date](https://exceljet.net/formulas/get-days-before-a-date)
    

### Functions

*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    

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