# Get same date next year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-same-date-next-year

---

[Skip to main content](https://exceljet.net/formulas/get-same-date-next-year#main-content)

[](https://exceljet.net/formulas/get-same-date-next-year#)

*   [Previous](https://exceljet.net/formulas/get-same-date-next-month)
    
*   [Next](https://exceljet.net/formulas/get-week-number-from-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get same date next year
=======================

by Dave Bruns · Updated 19 Nov 2015

Related functions 
------------------

[EDATE](https://exceljet.net/functions/edate-function)

![Excel formula: Get same date next year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20same%20date%20next%20year.png "Excel formula: Get same date next year")

Summary
-------

To get the same date next year from a given date, you can use the EDATE function.

In the example shown, the formula in cell B5 is:

    =EDATE(B5,12)
    

Generic formula
---------------

    =EDATE(date,12)

Explanation 
------------

EDATE can get the "same date" in the future or past, based on the number of months supplied. When 12 is given for months, EDATE gets the same date next year.

### Same date in previous year

To get the same date in a previous month, use -12:

    =EDATE(date,-12) // prior year
    

Related formulas
----------------

[![Excel formula: Get same date next month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20same%20date%20next%20month.png "Excel formula: Get same date next month")](https://exceljet.net/formulas/get-same-date-next-month)

### [Get same date next month](https://exceljet.net/formulas/get-same-date-next-month)

The EDATE function returns a date on the same day of the month, n months in the past or future. You can use EDATE to calculate expiration dates, maturity dates, and other due dates. When 1 is given for months , EDATE returns the same date in the next month. Notice that EDATE automatically handles...

Related functions
-----------------

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

*   [Get same date next month](https://exceljet.net/formulas/get-same-date-next-month)
    

### Functions

*   [EDATE Function](https://exceljet.net/functions/edate-function)
    

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