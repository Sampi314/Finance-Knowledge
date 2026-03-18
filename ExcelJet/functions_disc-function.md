# Excel DISC function | Exceljet

**Source:** https://exceljet.net/functions/disc-function

---

[Skip to main content](https://exceljet.net/functions/disc-function#main-content)

[](https://exceljet.net/functions/disc-function#)

*   [Previous](https://exceljet.net/functions/ddb-function)
    
*   [Next](https://exceljet.net/functions/dollarde-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

DISC Function
=============

by Dave Bruns · Updated 27 Aug 2021

Related functions 
------------------

[PRICEDISC](https://exceljet.net/functions/pricedisc-function)

![Excel DISC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_disc_function.png "Excel DISC function")

Summary
-------

The Excel DISC function returns the discount rate for a security.

Purpose 
--------

Get discount rate for a security

Return value 
-------------

Discount rate as percentage

Syntax
------

    =DISC(settlement,maturity,pr,redemption,[basis])

*   _settlement_ - Settlement date of the security.
*   _maturity_ - Maturity date of the security.
*   _pr_ - Security price per $100 face value.
*   _redemption_ - Security redemption value per $100 face value.
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the DISC function 
------------------------

The Excel DISC function returns the discount rate for a security. A discounted security does not pay periodic interest, but has a specified redemption value at maturity. The return on a discounted security is the difference between the price and redemption value.

Discount rate is based on the concept of the time value of money. The discount rate is the interest used to convert between future value and present value. A future value can be "discounted" by a given interest rate to determine the present value.

### Example

In the example shown, we want to find the discount rate for a bond with a price of $89.50 and a _redemption_ value of $100. The _settlement_ date is 6-Jul-2017 and the _maturity_ date is 15-Jan-2020. The day count _basis_ is US (NASD) 30/360. The formula in F5 is:

    =DISC(C7,C8,C5,C9,C10)
    

With these inputs, the DISC function returns 4.16%, with percentage [number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, you can use the [DATE function](https://exceljet.net/functions/date-function)
. To illustrate, the formula below has all values hardcoded, and the DATE function is used to supply each of the two required dates:

    =DISC(DATE(2017,7,6),DATE(2020,1,15),89.5,100,0)
    

### Basis

The _basis_ argument controls how days are counted. The DISC function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
 provides a detailed explanation of available conventions.

| Basis | Day count |
| --- | --- |
| 0 or omitted | US (NASD) 30/360 |
| 1   | Actual/actual |
| 2   | Actual/360 |
| 3   | Actual/365 |
| 4   | European 30/360 |

### Notes

*   In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
    . 
*   All dates, and _basis_, are truncated to integers.
*   If dates are invalid (i.e. not actually dates) DISC returns #VALUE!
*   DISC returns #NUM when:
    *   _settlement_ >= _maturity_
    *   _pr_ <= 0 or _redemption_ <= 0
    *   _Basis_ is out-of-range

Related functions
-----------------

[![Excel PRICEDISC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20pricedisc_function.png "Excel PRICEDISC function")](https://exceljet.net/functions/pricedisc-function)

### [PRICEDISC Function](https://exceljet.net/functions/pricedisc-function)

The Excel PRICEDISC function returns the price per $100 face value of a discounted security.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [PRICEDISC Function](https://exceljet.net/functions/pricedisc-function)
    

### Links

*   [Microsoft DISC function documentation](https://support.office.com/en-us/article/disc-function-71fce9f3-3f05-4acf-a5a3-eac6ef4daa53)
    

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