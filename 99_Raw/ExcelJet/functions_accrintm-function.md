# Excel ACCRINTM function | Exceljet

**Source:** https://exceljet.net/functions/accrintm-function

---

[Skip to main content](https://exceljet.net/functions/accrintm-function#main-content)

[](https://exceljet.net/functions/accrintm-function#)

*   [Previous](https://exceljet.net/functions/accrint-function)
    
*   [Next](https://exceljet.net/functions/amordegrc-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

ACCRINTM Function
=================

by Dave Bruns · Updated 21 Aug 2021

Related functions 
------------------

[ACCRINT](https://exceljet.net/functions/accrint-function)

![Excel ACCRINTM function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_accrintm_function.png "Excel ACCRINTM function")

Summary
-------

The Excel ACCRINTM function returns the accrued interest for a security that pays interest at maturity (i.e. pays interest one time only).

Purpose 
--------

Get accrued interest at maturity

Return value 
-------------

Accrued interest

Syntax
------

    =ACCRINTM(id,sd,rate,par,[basis])

*   _id_ - Issue date of the security.
*   _sd_ - Settlement date of the security.
*   _rate_ - Annual coupon rate.
*   _par_ - Par value of security.
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the ACCRINTM function 
----------------------------

In finance, bonds prices are quoted "clean". The "clean price" of a bond excludes any interest accrued since the issue date, or most recent coupon payment. The "dirty price" of a bond is the price including accrued interest. The ACCRINTM function can be used to calculate accrued interest for a bond that pays periodic at maturity (i.e. only pays interest one time).

### Date configuration

By default, ACCRINTM will calculate accrued interest from the issue date to the settlement date. If you want to calculate total interest from the issue date to the maturity date, supply maturity date instead of settlement date.

### Example

In the example shown, we want to calculate accrued interest for a bond with a 5% coupon rate. The issue date is 5-Apr-2016, the settlement date is 1-Feb-2019, and maturity date is 15-Apr-2026. We want accrued interest from the _issue_ date to the settlement date. The formula in F5 is:

    =ACCRINTM(C7,C8,C6,C5,C10)
    

With these inputs, the ACCRINTM function returns $141.11, with currency [number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, you can use the [DATE function](https://exceljet.net/functions/date-function)
. To illustrate, the formula below has all values hardcoded. The DATE function is used to supply each of the two required dates:

    =ACCRINTM(DATE(2016,4,5),DATE(2019,2,1),0.05,1000,0)
    

### Basis

The _basis_ argument controls how days are counted. The ACCRINTM function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 basis. This [article on wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   If dates are invalid (i.e. not actually dates) ACCRINTM returns #VALUE!
*   ACCRINTM returns #NUM when:
    *   issue date >= settlement date
    *   _rate_ < 0 or _par_ <= 0
    *   _Basis_ is out-of-range

Related functions
-----------------

[![Excel ACCRINT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_accrint_function.png "Excel ACCRINT function")](https://exceljet.net/functions/accrint-function)

### [ACCRINT Function](https://exceljet.net/functions/accrint-function)

The Excel ACCRINT function returns the accrued interest for a security that pays periodic interest

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [ACCRINT Function](https://exceljet.net/functions/accrint-function)
    

### Links

*   [Microsoft ACCRINTM function documentation](https://support.office.com/en-us/article/accrintm-function-f62f01f9-5754-4cc4-805b-0e70199328a7)
    

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