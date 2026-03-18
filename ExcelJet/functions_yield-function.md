# Excel YIELD function | Exceljet

**Source:** https://exceljet.net/functions/yield-function

---

[Skip to main content](https://exceljet.net/functions/yield-function#main-content)

[](https://exceljet.net/functions/yield-function#)

*   [Previous](https://exceljet.net/functions/xnpv-function)
    
*   [Next](https://exceljet.net/functions/yielddisc-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

YIELD Function
==============

by Dave Bruns · Updated 2 Sep 2021

Related functions 
------------------

[YIELD](https://exceljet.net/functions/yield-function)

[YIELDDISC](https://exceljet.net/functions/yielddisc-function)

[YIELDMAT](https://exceljet.net/functions/yieldmat-function)

[ODDFYIELD](https://exceljet.net/functions/oddfyield-function)

[ODDLYIELD](https://exceljet.net/functions/oddlyield-function)

![Excel YIELD function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_%20yield_function2.png "Excel YIELD function")

Summary
-------

The Excel YIELD function returns the yield on a security that pays periodic interest.

Purpose 
--------

Get yield for security that pays periodic interest

Return value 
-------------

Yield as percentage

Syntax
------

    =YIELD(sd,md,rate,pr,redemption,frequency,[basis])

*   _sd_ - Settlement date of the security.
*   _md_ - Maturity date of the security.
*   _rate_ - Annual coupon rate.
*   _pr_ - Security's price per $100 face value.
*   _redemption_ - Redemption value per $100 face value.
*   _frequency_ - Coupon payments per year (annual = 1, semiannual = 2; quarterly = 4).
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the YIELD function 
-------------------------

The YIELD function returns the yield on a security that pays periodic interest. In the example shown, the formula in F6 is:

    =YIELD(C9,C10,C7,F5,C6,C12,C13)
    

with these inputs, the YIELD function returns 0.08 which, or 8.00% when formatted with the [percentage number format](https://exceljet.net/articles/custom-number-formats)
.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. If you want to enter valid dates directly inside a function, the [DATE function](https://exceljet.net/functions/date-function)
 is the best approach.

### Basis

The basis argument controls how days are counted. The PRICE function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 basis. This [article on Wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   _Settlement_, _maturity, frequency,_ and _basis_ are truncated to integers
*   If _settlement_ or _maturity_ dates are not valid, YIELD returns #VALUE!
*   YIELD returns #NUM! if any of the following are true:
    *   _rate_ < 0
    *   _frequency_ is not 1,2, or 4
    *   _pr_ or _redemption_ are <= 0
    *   _settlement_ >= _maturity_
    *   _Basis_ is not 0-4

Related functions
-----------------

[![Excel YIELD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20yield_function2.png "Excel YIELD function")](https://exceljet.net/functions/yield-function)

### [YIELD Function](https://exceljet.net/functions/yield-function)

The Excel YIELD function returns the yield on a security that pays periodic interest.

[![Excel YIELDDISC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20yielddisc_function.png "Excel YIELDDISC function")](https://exceljet.net/functions/yielddisc-function)

### [YIELDDISC Function](https://exceljet.net/functions/yielddisc-function)

The Excel YIELDDISC function returns the annual yield for a discounted security, such as a Treasury bill, that is issued at a discount but that matures at face value.

[![Excel YIELDMAT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20yieldmat_function.png "Excel YIELDMAT function")](https://exceljet.net/functions/yieldmat-function)

### [YIELDMAT Function](https://exceljet.net/functions/yieldmat-function)

The Excel YIELDMAT function returns the annual yield of a security that pays interest at maturity.

[![Excel ODDFYIELD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oddfyield_function.png "Excel ODDFYIELD function")](https://exceljet.net/functions/oddfyield-function)

### [ODDFYIELD Function](https://exceljet.net/functions/oddfyield-function)

The Excel ODDFYIELD function returns the yield of a security with an odd (irregular) first period.

[![Excel ODDLYIELD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_oddlyield_function.png "Excel ODDLYIELD function")](https://exceljet.net/functions/oddlyield-function)

### [ODDLYIELD Function](https://exceljet.net/functions/oddlyield-function)

The Excel ODDLYIELD function returns the yield of a security with an odd (irregular) last period.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [YIELD Function](https://exceljet.net/functions/yield-function)
    
*   [YIELDDISC Function](https://exceljet.net/functions/yielddisc-function)
    
*   [YIELDMAT Function](https://exceljet.net/functions/yieldmat-function)
    
*   [ODDFYIELD Function](https://exceljet.net/functions/oddfyield-function)
    
*   [ODDLYIELD Function](https://exceljet.net/functions/oddlyield-function)
    

### Links

*   [Microsoft YIELD function documentation](https://support.office.com/en-us/article/yield-function-f5f5ca43-c4bd-434f-8bd2-ed3c9727a4fe)
    

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