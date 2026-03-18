# Excel INTRATE function | Exceljet

**Source:** https://exceljet.net/functions/intrate-function

---

[Skip to main content](https://exceljet.net/functions/intrate-function#main-content)

[](https://exceljet.net/functions/intrate-function#)

*   [Previous](https://exceljet.net/functions/fvschedule-function)
    
*   [Next](https://exceljet.net/functions/ipmt-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

INTRATE Function
================

by Dave Bruns · Updated 27 Aug 2021

Related functions 
------------------

[DISC](https://exceljet.net/functions/disc-function)

![Excel INTRATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_intrate_function.png "Excel INTRATE function")

Summary
-------

The Excel INTRATE function returns the interest rate for a fully invested security.

Purpose 
--------

Get interest rate for fully invested security

Return value 
-------------

Interest rate as percentage

Syntax
------

    =INTRATE(settlement,maturity,investment,redemption,[basis])

*   _settlement_ - Settlement date of the security.
*   _maturity_ - Maturity date of the security.
*   _investment_ - The amount originally invested.
*   _redemption_ - The amount received at maturity.
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the INTRATE function 
---------------------------

The INTRATE function calculates the annual effective interest rate for a "fully invested" security. A fully invested security does not pay periodic interest before maturity. The interest income is the difference between the redemption value of the security and the original investment.

### Example

In the example shown, we want to find the effective annual interest rate for a bond with a price of $895.00 and a redemption value of $1000. The settlement date is 6-Jul-2017 and the maturity date is 15-Jan-2020. There are no periodic interest payments, and the day count basis is US (NASD) 30/360. The formula in F5 is:

    =INTRATE(C7,C8,C5,C9,C10)
    

With these inputs, the INTRATE function returns 4.65%, with percentage [number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, you can use the [DATE function](https://exceljet.net/functions/date-function)
. To illustrate, the formula below has all values hardcoded, and the DATE function is used to supply each of the two required dates:

    =INTRATE(DATE(2017,7,6),DATE(2020,1,15),895,1000,0)
    

### Basis

The _basis_ argument controls how days are counted. The INTRATE function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   If dates are invalid (i.e. not actually dates) INTRATE returns #VALUE!
*   INTRATE returns #NUM when:
    *   _settlement_ >= _maturity_
    *   _investment_ <= 0 or _redemption_ <= 0
    *   _Basis_ is out-of-range

Related functions
-----------------

[![Excel DISC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_disc_function.png "Excel DISC function")](https://exceljet.net/functions/disc-function)

### [DISC Function](https://exceljet.net/functions/disc-function)

The Excel DISC function returns the discount rate for a security.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [DISC Function](https://exceljet.net/functions/disc-function)
    

### Links

*   [Microsoft INTRATE function documentation](https://support.office.com/en-us/article/intrate-function-5cb34dde-a221-4cb6-b3eb-0b9e55e1316f)
    

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