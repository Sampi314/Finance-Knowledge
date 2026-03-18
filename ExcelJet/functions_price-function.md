# Excel PRICE function | Exceljet

**Source:** https://exceljet.net/functions/price-function

---

[Skip to main content](https://exceljet.net/functions/price-function#main-content)

[](https://exceljet.net/functions/price-function#)

*   [Previous](https://exceljet.net/functions/ppmt-function)
    
*   [Next](https://exceljet.net/functions/pricedisc-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

PRICE Function
==============

by Dave Bruns · Updated 31 Aug 2021

Related functions 
------------------

[PRICE](https://exceljet.net/functions/price-function)

[PRICEDISC](https://exceljet.net/functions/pricedisc-function)

[PRICEMAT](https://exceljet.net/functions/pricemat-function)

[ODDFPRICE](https://exceljet.net/functions/oddfprice-function)

[ODDLPRICE](https://exceljet.net/functions/oddlprice-function)

[TBILLPRICE](https://exceljet.net/functions/tbillprice-function)

![Excel PRICE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_price_function.png "Excel PRICE function")

Summary
-------

The Excel PRICE function returns the price per $100 face value of a security that pays periodic interest.

Purpose 
--------

Get price per $100 face value - periodic interest

Return value 
-------------

Bond price

Syntax
------

    =PRICE(sd,md,rate,yld,redemption,frequency,[basis])

*   _sd_ - Settlement date of the security.
*   _md_ - Maturity date of the security.
*   _rate_ - Annual coupon rate.
*   _yld_ - Annual required rate of return.
*   _redemption_ - Redemption value per $100 face value.
*   _frequency_ - Coupon payments per year (annual = 1, semiannual = 2; quarterly = 4.
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the PRICE function 
-------------------------

The Excel PRICE function returns the price per $100 face value of a security that pays periodic interest. For example, the PRICE function can be used to determine the "clean price" of a bond (also known as the quoted price), which is the price of the bond excluding accrued interest.

In the example shown, the formula in F5 is:

    =PRICE(C9,C10,C7,C8,C6,C12,C13)
    

with these inputs, the PRICE function returns 97.56, which indicates the value of the bond is 97.56% of the face value. To get the actual dollar value, the formula in F6 is:

    =F5/100*C5
    

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. If you want to enter valid dates directly inside a function, the [DATE function](https://exceljet.net/functions/date-function)
 is the best approach.

### Basis

The _basis_ argument controls how days are counted. The PRICE function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on Wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   _settlement_, _maturity_, _frequency_, and _basis_ are truncated to integers
*   If _settlement_ or _maturity_ dates are not valid, PRICE returns #VALUE!
*   If _basis_ is out-of-range, PRICE returns #NUM!
*   If _maturity_ date is not later than _settlement_ date, PRICE returns #NUM!

PRICE function examples
-----------------------

[![Excel formula: Bond valuation example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Bond%20valuation%20example.png "Excel formula: Bond valuation example")](https://exceljet.net/formulas/bond-valuation-example)

### [Bond valuation example](https://exceljet.net/formulas/bond-valuation-example)

In the example shown, we have a 3-year bond with a face value of $1,000. The coupon rate is 7% so the bond will pay 7% of the $1,000 face value in interest every year, or $70. However, because interest is paid semiannually in two equal payments, there will be 6 coupon payments of $35 each. The $1,...

Related functions
-----------------

[![Excel PRICE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_price_function.png "Excel PRICE function")](https://exceljet.net/functions/price-function)

### [PRICE Function](https://exceljet.net/functions/price-function)

The Excel PRICE function returns the price per $100 face value of a security that pays periodic interest.

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

### Formulas

*   [Bond valuation example](https://exceljet.net/formulas/bond-valuation-example)
    

### Functions

*   [PRICE Function](https://exceljet.net/functions/price-function)
    
*   [PRICEDISC Function](https://exceljet.net/functions/pricedisc-function)
    
*   [PRICEMAT Function](https://exceljet.net/functions/pricemat-function)
    
*   [ODDFPRICE Function](https://exceljet.net/functions/oddfprice-function)
    
*   [ODDLPRICE Function](https://exceljet.net/functions/oddlprice-function)
    
*   [TBILLPRICE Function](https://exceljet.net/functions/tbillprice-function)
    

### Links

*   [Microsoft PRICE function documentation](https://support.office.com/en-us/article/price-function-3ea9deac-8dfa-436f-a7c8-17ea02c21b0a)
    

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