# Next anniversary date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/next-anniversary-date

---

[Skip to main content](https://exceljet.net/formulas/next-anniversary-date#main-content)

[](https://exceljet.net/formulas/next-anniversary-date#)

*   [Previous](https://exceljet.net/formulas/month-number-from-name)
    
*   [Next](https://exceljet.net/formulas/next-biweekly-payday-from-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Next anniversary date
=====================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[EDATE](https://exceljet.net/functions/edate-function)

[DATEDIF](https://exceljet.net/functions/datedif-function)

![Excel formula: Next anniversary date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/next%20anniversary%20date.png "Excel formula: Next anniversary date")

Summary
-------

To calculate the next anniversary date, you can use a formula based on the EDATE and DATEDIF functions. In the example shown, the formula in D5 is:

     =EDATE(B5,(DATEDIF(B5,C5,"y")+1)*12)
    

This formula will work to calculate next upcoming birthday as well.

Generic formula
---------------

    =EDATE(date,(DATEDIF(date,as_of,"y")+1)*12)

Explanation 
------------

Working from the inside out, we use the DATEDIF function to calculate how many complete years are between the original anniversary date and the "as of" date, where the as of date is any date _after_ the anniversary date:

    DATEDIF(B5,C5,"y")
    

_Note: in this case, we are arbitrarily fixing the "as of" date as June 1, 2017 in all examples._

Because we are interested in the \*next\* anniversary date, we add 1 to the DATEDIF result, then multiply by 12 to convert to years to months.

Next, the month value goes into the EDATE function, with the original date from column B. The EDATE function rolls the original date forward by the number of months given in the previous step which creates the next upcoming anniversary date.

### As of today

To calculate the next anniversary as of today, use the TODAY() function for the "as of" date:

    =EDATE(date,(DATEDIF(date,TODAY(),"y")+1)*12)
    

Related formulas
----------------

[![Excel formula: Get days before a date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_days_before_a_date.png "Excel formula: Get days before a date")](https://exceljet.net/formulas/get-days-before-a-date)

### [Get days before a date](https://exceljet.net/formulas/get-days-before-a-date)

In Excel, dates are simply serial numbers. In the standard date system for windows, based on the year 1900, where January 1, 1900 is the number 1. Dates are valid through 9999, which is serial number 2,958,465. This means that January 1, 2050 is the serial number 54,789. In the example, the date is...

[![Excel formula: Calculate time before expiration date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_time_before_expiration_date.png "Excel formula: Calculate time before expiration date")](https://exceljet.net/formulas/calculate-time-before-expiration-date)

### [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)

In this example, the goal is to calculate the time remaining before an expiration date. There are many ways to do something like this in Excel, and in this article, we'll look at three different approaches: Calculating the remaining time in days Calculating the remaining time in years, months, and...

[![Excel formula: Calculate retirement date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20retirement%20date.png "Excel formula: Calculate retirement date")](https://exceljet.net/formulas/calculate-retirement-date)

### [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)

In this example, the goal is to calculate a retirement date at age 60, based on a given birthdate. The simplest way to do this is with the EDATE function. The EDATE function will return a date n months in the future or past when given a date and the number of months to traverse. In this case, we...

Related functions
-----------------

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel DATEDIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_datedif_function_0.png "Excel DATEDIF function")](https://exceljet.net/functions/datedif-function)

### [DATEDIF Function](https://exceljet.net/functions/datedif-function)

The Excel DATEDIF function returns the difference between two date values in years, months, or days. DATEDIF supports six unit codes that let you calculate complete years, complete months, total days, and partial intervals. DATEDIF is a "compatibility" function inherited from Lotus 1-2-3....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get days before a date](https://exceljet.net/formulas/get-days-before-a-date)
    
*   [Calculate time before expiration date](https://exceljet.net/formulas/calculate-time-before-expiration-date)
    
*   [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)
    

### Functions

*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [DATEDIF Function](https://exceljet.net/functions/datedif-function)
    

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