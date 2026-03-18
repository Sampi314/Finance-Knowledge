# Excel ODDLPRICE function | Exceljet

**Source:** https://exceljet.net/functions/oddlprice-function

---

[Skip to main content](https://exceljet.net/functions/oddlprice-function#main-content)

[](https://exceljet.net/functions/oddlprice-function#)

*   [Previous](https://exceljet.net/functions/oddfyield-function)
    
*   [Next](https://exceljet.net/functions/oddlyield-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

ODDLPRICE Function
==================

by Dave Bruns · Updated 30 Aug 2021

Related functions 
------------------

[PRICE](https://exceljet.net/functions/price-function)

[PRICEDISC](https://exceljet.net/functions/pricedisc-function)

[PRICEMAT](https://exceljet.net/functions/pricemat-function)

[ODDFPRICE](https://exceljet.net/functions/oddfprice-function)

[ODDLPRICE](https://exceljet.net/functions/oddlprice-function)

[TBILLPRICE](https://exceljet.net/functions/tbillprice-function)

![Excel ODDLPRICE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_%20oddlprice_function.png "Excel ODDLPRICE function")

Summary
-------

The Excel ODDLPRICE function returns the price per $100 face value of a security with an odd (irregular) last period.

Purpose 
--------

Get price per $100 face value with odd last period

Return value 
-------------

Bond price

Syntax
------

    =ODDLPRICE(sd,md,id,rate,yld,redem,freq,[basis])

*   _sd_ - Settlement date of the security.
*   _md_ - Maturity date of the security.
*   _id_ - Last interest date of security.
*   _rate_ - Interest rate of security.
*   _yld_ - Annual required rate of return.
*   _redem_ - Redemption value per $100 face value.
*   _freq_ - Coupon payments per year (annual = 1, semiannual = 2; quarterly = 4).
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the ODDLPRICE function 
-----------------------------

Some bonds have an irregular first or last period, so interest payments don't fit a normal schedule. To calculate the price of a bond with an irregular last period, you can use the ODDLPRICE function. The ODDLPRICE Function returns the price per $100 face value of a security having a short or long last period.

### Example

Assume we need to calculate the price per $100 face value of a bond with a last interest date of 15-Oct-2017 and a settlement date of 5-Feb-2018. The bond matures on 15-Jun-2018, and pays a coupon rate of 5% with a required return of 6%. Payments are semi-annual, the day count basis is US 30/360, and the redemption value is $100. In the example shown, the formula in F5 is:

    =ODDLPRICE(C8,C10,C9,C6,C7,C5,C11,C12)
    

With these inputs, the ODDLPRICE function returns 99.61, with currency [number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, the [DATE function](https://exceljet.net/functions/date-function)
 is the best option. To illustrate, the formula below has all values hardcoded. The DATE function is used to supply each of the three required dates:

    =ODDLPRICE(DATE(2018,2,5),DATE(2018,6,15),DATE(2017,10,15),0.05,0.06,100,2,0)
    

### Basis

The _basis_ argument controls how days are counted. The ODDLPRICE function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on Wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   If dates are invalid (i.e. not actually dates) ODDLPRICE returns #VALUE!
*   ODDLPRICE returns #NUM when:
    *   (_maturity_ > _settlement_ > _last\_interest_) is NOT true
    *   _Basis_ is out-of-range

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

### Functions

*   [PRICE Function](https://exceljet.net/functions/price-function)
    
*   [PRICEDISC Function](https://exceljet.net/functions/pricedisc-function)
    
*   [PRICEMAT Function](https://exceljet.net/functions/pricemat-function)
    
*   [ODDFPRICE Function](https://exceljet.net/functions/oddfprice-function)
    
*   [ODDLPRICE Function](https://exceljet.net/functions/oddlprice-function)
    
*   [TBILLPRICE Function](https://exceljet.net/functions/tbillprice-function)
    

### Links

*   [Microsoft ODDLPRICE function documentation](https://support.office.com/en-us/article/oddlprice-function-fb657749-d200-4902-afaf-ed5445027fc4)
    

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