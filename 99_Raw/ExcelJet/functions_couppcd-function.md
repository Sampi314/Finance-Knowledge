# Excel COUPPCD function | Exceljet

**Source:** https://exceljet.net/functions/couppcd-function

---

[Skip to main content](https://exceljet.net/functions/couppcd-function#main-content)

[](https://exceljet.net/functions/couppcd-function#)

*   [Previous](https://exceljet.net/functions/coupnum-function)
    
*   [Next](https://exceljet.net/functions/cumipmt-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

COUPPCD Function
================

by Dave Bruns · Updated 22 Aug 2021

Related functions 
------------------

[COUPNUM](https://exceljet.net/functions/coupnum-function)

[COUPDAYS](https://exceljet.net/functions/coupdays-function)

[COUPDAYBS](https://exceljet.net/functions/coupdaybs-function)

[COUPDAYSNC](https://exceljet.net/functions/coupdaysnc-function)

[COUPNCD](https://exceljet.net/functions/coupncd-function)

[COUPPCD](https://exceljet.net/functions/couppcd-function)

![Excel COUPPCD function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_couppcd_function.png "Excel COUPPCD function")

Summary
-------

The Excel COUPPCD function returns the previous coupon date before the settlement date for a coupon bond.

Purpose 
--------

Get previous coupon date before settlement date

Return value 
-------------

Previous coupon date

Syntax
------

    =COUPPCD(settlement,maturity,frequency,[basis])

*   _settlement_ - Settlement date of the security.
*   _maturity_ - Maturity date of the security.
*   _frequency_ - Number of coupon payments per year (annual = 1, semi-annual = 2, quarterly = 4).
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the COUPPCD function 
---------------------------

Historically, bonds were printed with an elaborate design on paper that included detachable coupons. The coupons were presented to the bond issuer by the bondholder to collect periodic interest payments. 

The Excel COUPPCD function returns the previous coupon date before the settlement date. The settlement date is the date the investor takes possession of a security. The maturity date is the date when the investment ends and the principle plus accrued interest is returned to the investor.  The _frequency_ is the number of interest payments per year. _Basis_ specifies the method used to count days (see below). In the example shown, the formula in F6 is:

    =COUPPCD(C6,C7,C10,C11)
    

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly, you can use the [DATE function](https://exceljet.net/functions/date-function)
. Below is the formula in F6 reworked with hardcoded values and the DATE function:

    =COUPPCD(DATE(2019,9,1),DATE(2029,1,1),2,0)
    

With these inputs, COUPPCD returns the same result, 1-Jul-2019.

### Basis

The _basis_ argument controls how days are counted. The COUPPCD function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   All arguments are truncated to integers, so for example, [time](https://exceljet.net/glossary/excel-time)
     is ignored.
*   If settlement or maturity dates are not valid, COUPPCD returns #VALUE!
*   If _basis_ is out-of-range , COUPPCD returns #NUM!
*   If maturity date is not later than settlement date, COUPPCD returns #NUM!

Related functions
-----------------

[![Excel COUPNUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_coupnum_function.png "Excel COUPNUM function")](https://exceljet.net/functions/coupnum-function)

### [COUPNUM Function](https://exceljet.net/functions/coupnum-function)

The Excel COUPNUM function returns the number of coupons, or interest payments, payable between the settlement date and maturity date.

[![Excel COUPDAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_coupdays_function2.png "Excel COUPDAYS function")](https://exceljet.net/functions/coupdays-function)

### [COUPDAYS Function](https://exceljet.net/functions/coupdays-function)

The Excel COUPDAYS function returns the number of days in a coupon period that includes the settlement date.

[![Excel COUPDAYBS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_coupdaybs_function.png "Excel COUPDAYBS function")](https://exceljet.net/functions/coupdaybs-function)

### [COUPDAYBS Function](https://exceljet.net/functions/coupdaybs-function)

The Excel COUPDAYBS function returns the number of days from the beginning of the coupon period to the settlement date.

[![Excel COUPDAYSNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_coupdaysnc_function.png "Excel COUPDAYSNC function")](https://exceljet.net/functions/coupdaysnc-function)

### [COUPDAYSNC Function](https://exceljet.net/functions/coupdaysnc-function)

The Excel COUPDAYSNC function returns the number of days from the settlement date to the next coupon date.

[![Excel COUPNCD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_coupncd_function.png "Excel COUPNCD function")](https://exceljet.net/functions/coupncd-function)

### [COUPNCD Function](https://exceljet.net/functions/coupncd-function)

The Excel COUPNCD function returns the next coupon date after the settlement date.

[![Excel COUPPCD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_couppcd_function.png "Excel COUPPCD function")](https://exceljet.net/functions/couppcd-function)

### [COUPPCD Function](https://exceljet.net/functions/couppcd-function)

The Excel COUPPCD function returns the previous coupon date before the settlement date for a coupon bond.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COUPNUM Function](https://exceljet.net/functions/coupnum-function)
    
*   [COUPDAYS Function](https://exceljet.net/functions/coupdays-function)
    
*   [COUPDAYBS Function](https://exceljet.net/functions/coupdaybs-function)
    
*   [COUPDAYSNC Function](https://exceljet.net/functions/coupdaysnc-function)
    
*   [COUPNCD Function](https://exceljet.net/functions/coupncd-function)
    
*   [COUPPCD Function](https://exceljet.net/functions/couppcd-function)
    

### Links

*   [Microsoft COUPPCD function documentation](https://support.office.com/en-us/article/couppcd-function-2eb50473-6ee9-4052-a206-77a9a385d5b3)
    

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