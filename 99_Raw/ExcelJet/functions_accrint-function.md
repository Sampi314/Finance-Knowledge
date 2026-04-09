# Excel ACCRINT function | Exceljet

**Source:** https://exceljet.net/functions/accrint-function

---

[Skip to main content](https://exceljet.net/functions/accrint-function#main-content)

[](https://exceljet.net/functions/accrint-function#)

*   [Previous](https://exceljet.net/functions/oct2hex-function)
    
*   [Next](https://exceljet.net/functions/accrintm-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

ACCRINT Function
================

by Dave Bruns · Updated 21 Aug 2021

Related functions 
------------------

[ACCRINTM](https://exceljet.net/functions/accrintm-function)

![Excel ACCRINT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_accrint_function.png "Excel ACCRINT function")

Summary
-------

The Excel ACCRINT function returns the accrued interest for a security that pays periodic interest

Purpose 
--------

Get accrued interest periodic

Return value 
-------------

Accrued interest

Syntax
------

    =ACCRINT(id,fd,sd,rate,par,freq,[basis],[calc])

*   _id_ - Issue date of the security.
*   _fd_ - First interest date of security.
*   _sd_ - Settlement date of security.
*   _rate_ - Interest rate of security.
*   _par_ - Par value of security.
*   _freq_ - Coupon payments per year (annual = 1, semiannual = 2; quarterly = 4).
*   _basis_ - \[optional\] Day count basis (see below, default =0).
*   _calc_ - \[optional\] Calculation method (see below, default = TRUE).

Using the ACCRINT function 
---------------------------

In finance, bonds prices are quoted "clean". The "clean price" of a bond excludes any interest accrued since the issue date or most recent coupon payment. The "dirty price" of a bond is the price including accrued interest. The ACCRINT function can be used to calculate accrued interest for a security that pays periodic interest, but pay attention to date configuration.

### Date configuration

By default, ACCRINT will calculate accrued interest from the _issue_ date. If the settlement date is in the first period, this works. However, if the settlement date is not in the first period, you probably don't want total accrued interest from the issue date but rather accrued interest from the last interest date (previous coupon date). As a workaround, based on the [article here](http://www.tvmcalcs.com/calculators/apps/calculate-accrued-interest-on-a-bond-in-excel-3-ways)
:

*   set _issue_ date to the previous coupon date
*   set _first\_interest_ date to the previous coupon date

Note: According to Microsoft documentation, _calc\_method_ controls how total accrued interest is calculated when the date of _settlement_ > _first\_interest_. The default is TRUE, which returns the total accrued interest from issue date to settlement date. Setting calculation method to FALSE is supposed to return accrued interest from _first\_interest_ to settlement date. However, I was unable to produce this behavior. In the example below, _issue_ date and _first\_interest_ date are set to the previous coupon date (as described above).

### Example

In the example shown, we want to calculate accrued interest for a bond with a 5% coupon rate. The issue date is 5-Apr-2018, the settlement date is 1-Feb-2019, and the last coupon date is 15-Oct-2018. We want accrued interest from October 15, 2018 to February 1, 2019. The formula in F5 is:

    =ACCRINT(C9,C9,C8,C6,C5,C12,C13,TRUE)
    

With these inputs, the ACCRINT function returns $14.72, with currency [number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, you can use the [DATE function](https://exceljet.net/functions/date-function)
. To illustrate, the formula below has all values hardcoded. The DATE function is used to supply each of the three required dates:

    =ACCRINT(DATE(2018,10,15),DATE(2018,10,15),DATE(2019,2,1),0.05,1000,2,0,TRUE)
    

### Basis

The _basis_ argument controls how days are counted. The ACCRINT function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 basis. This [article on wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   All dates, plus _frequency_ and _basis_, are truncated to integers.
*   If dates are invalid (i.e. not actually dates) ACCRINT returns #VALUE!
*   ACCRINT returns #NUM when:
    *   issue date >= settlement date
    *   _rate_ < 0 or _par_ <= 0
    *   _frequency_ is not 1, 2, or 4
    *   _Basis_ is out-of-range

Related functions
-----------------

[![Excel ACCRINTM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_accrintm_function.png "Excel ACCRINTM function")](https://exceljet.net/functions/accrintm-function)

### [ACCRINTM Function](https://exceljet.net/functions/accrintm-function)

The Excel ACCRINTM function returns the accrued interest for a security that pays interest at maturity (i.e. pays interest one time only).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [ACCRINTM Function](https://exceljet.net/functions/accrintm-function)
    

### Links

*   [Microsoft ACCRINT function documentation](https://support.office.com/en-us/article/accrint-function-fe45d089-6722-4fb3-9379-e1f911d8dc74)
    

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