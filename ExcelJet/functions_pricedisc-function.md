# Excel PRICEDISC function | Exceljet

**Source:** https://exceljet.net/functions/pricedisc-function

---

[Skip to main content](https://exceljet.net/functions/pricedisc-function#main-content)

[](https://exceljet.net/functions/pricedisc-function#)

*   [Previous](https://exceljet.net/functions/price-function)
    
*   [Next](https://exceljet.net/functions/pricemat-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

PRICEDISC Function
==================

by Dave Bruns · Updated 31 Aug 2021

Related functions 
------------------

[PRICE](https://exceljet.net/functions/price-function)

[DISC](https://exceljet.net/functions/disc-function)

[PRICEDISC](https://exceljet.net/functions/pricedisc-function)

[PRICEMAT](https://exceljet.net/functions/pricemat-function)

[ODDFPRICE](https://exceljet.net/functions/oddfprice-function)

[ODDLPRICE](https://exceljet.net/functions/oddlprice-function)

[TBILLPRICE](https://exceljet.net/functions/tbillprice-function)

![Excel PRICEDISC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_%20pricedisc_function.png "Excel PRICEDISC function")

Summary
-------

The Excel PRICEDISC function returns the price per $100 face value of a discounted security.

Purpose 
--------

Get price per $100 discounted security

Return value 
-------------

Bond price

Syntax
------

    =PRICEDISC(sd,md,discount,redemption,[basis])

*   _sd_ - Settlement date of the security.
*   _md_ - Maturity date of the security.
*   _discount_ - Discount rate of the security.
*   _redemption_ - Redemption value per $100 face value.
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the PRICEDISC function 
-----------------------------

The Excel PRICEDISC function returns the price per $100 face value of a discounted security.  In the example shown, the formula in F5 is:

    =PRICEDISC(C6,C7,C8,C9,C10)
    

with these inputs, PRICEDISC returns a price for the bond of $82.50.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, you can use the [DATE function](https://exceljet.net/functions/date-function)
. The same formula above using the DATE function, and with other values hardcoded looks like this:

    =PRICEDISC(DATE(2017,7,1),DATE(2020,1,1),7%,100,0)
    

### Basis

The _basis_ argument controls how days are counted. The PRICEMAT function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis._ This [article on Wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   _Settlement, maturity,_ and _basis_ are truncated to integers.
*   If any date is not valid, PRICEDISC returns #VALUE!
*   _Rate_ must be positive or PRICEDISC returns the #NUM!
*   If _basis_ is out-of-range, PRICEDISC returns #NUM!
*   If _maturity_ date is not later than _settlement_ date, PRICEDISC returns #NUM!

Related functions
-----------------

[![Excel PRICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_price_function.png "Excel PRICE function")](https://exceljet.net/functions/price-function)

### [PRICE Function](https://exceljet.net/functions/price-function)

The Excel PRICE function returns the price per $100 face value of a security that pays periodic interest.

[![Excel DISC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_disc_function.png "Excel DISC function")](https://exceljet.net/functions/disc-function)

### [DISC Function](https://exceljet.net/functions/disc-function)

The Excel DISC function returns the discount rate for a security.

[![Excel PRICEDISC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20pricedisc_function.png "Excel PRICEDISC function")](https://exceljet.net/functions/pricedisc-function)

### [PRICEDISC Function](https://exceljet.net/functions/pricedisc-function)

The Excel PRICEDISC function returns the price per $100 face value of a discounted security.

[![Excel PRICEMAT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20pricemat_function.png "Excel PRICEMAT function")](https://exceljet.net/functions/pricemat-function)

### [PRICEMAT Function](https://exceljet.net/functions/pricemat-function)

The Excel PRICEMAT function returns the price per $100 face value of a security that pays interest at maturity.

[![Excel ODDFPRICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20oddfprice_function2.png "Excel ODDFPRICE function")](https://exceljet.net/functions/oddfprice-function)

### [ODDFPRICE Function](https://exceljet.net/functions/oddfprice-function)

The Excel ODDFPRICE function returns the price per $100 face value of a security with an odd (irregular) first period.

[![Excel ODDLPRICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20oddlprice_function.png "Excel ODDLPRICE function")](https://exceljet.net/functions/oddlprice-function)

### [ODDLPRICE Function](https://exceljet.net/functions/oddlprice-function)

The Excel ODDLPRICE function returns the price per $100 face value of a security with an odd (irregular) last period.

[![Excel TBILLPRICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20tbillprice_function.png "Excel TBILLPRICE function")](https://exceljet.net/functions/tbillprice-function)

### [TBILLPRICE Function](https://exceljet.net/functions/tbillprice-function)

The Excel TBILLPRICE function returns the price per $100 face value for a Treasury bill.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [PRICE Function](https://exceljet.net/functions/price-function)
    
*   [DISC Function](https://exceljet.net/functions/disc-function)
    
*   [PRICEDISC Function](https://exceljet.net/functions/pricedisc-function)
    
*   [PRICEMAT Function](https://exceljet.net/functions/pricemat-function)
    
*   [ODDFPRICE Function](https://exceljet.net/functions/oddfprice-function)
    
*   [ODDLPRICE Function](https://exceljet.net/functions/oddlprice-function)
    
*   [TBILLPRICE Function](https://exceljet.net/functions/tbillprice-function)
    

### Links

*   [Microsoft PRICEDISC function documentation](https://support.office.com/en-us/article/pricedisc-function-d06ad7c1-380e-4be7-9fd9-75e3079acfd3)
    

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