# Excel ODDFPRICE function | Exceljet

**Source:** https://exceljet.net/functions/oddfprice-function

---

[Skip to main content](https://exceljet.net/functions/oddfprice-function#main-content)

[](https://exceljet.net/functions/oddfprice-function#)

*   [Previous](https://exceljet.net/functions/npv-function)
    
*   [Next](https://exceljet.net/functions/oddfyield-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

ODDFPRICE Function
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

![Excel ODDFPRICE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_%20oddfprice_function2.png "Excel ODDFPRICE function")

Summary
-------

The Excel ODDFPRICE function returns the price per $100 face value of a security with an odd (irregular) first period.

Purpose 
--------

Get price per $100 odd first period

Return value 
-------------

Bond price

Syntax
------

    =ODDFPRICE(sd,md,id,fd,rate,yld,redem,freq,[basis])

*   _sd_ - Settlement date of the security.
*   _md_ - Maturity date of the security.
*   _id_ - Issue date of the security.
*   _fd_ - First coupon date.
*   _rate_ - Annual coupon rate of security.
*   _yld_ - Annual required rate of return.
*   _redem_ - Redemption value per $100 face value.
*   _freq_ - Coupon payments per year (annual = 1, semiannual = 2; quarterly = 4).
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the ODDFPRICE function 
-----------------------------

Some bonds have an irregular first or last period, so interest payments don't fit a normal schedule. To calculate the price of a bond with an irregular first period, you can use the ODDFPRICE function. The ODDFPRICE Function returns the price per $100 face value of a security having an irregular (short or long) first period.

### Example

Assume we need to calculate the price per $100 face value of a bond with a first coupon date of 15-Feb-2019. The bond was issued on 1-Dec-2018, matures on 15-Feb-2022, and pays a coupon rate of 5% with a required return of 6%. Payments are semi-annual, the day count basis is US 30/360, and the redemption value is $100. In the example shown, the formula in F5 is:

    =ODDFPRICE(C9,C11,C8,C10,C6,C7,C5,C12,C13)
    

With these inputs, the ODDFPRICE function returns 97.26, with currency [number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, you can use the [DATE function](https://exceljet.net/functions/date-function)
. To illustrate, the formula below has all values hardcoded. The DATE function is used to supply each of the four required dates:

    =ODDFPRICE(DATE(2019,2,1),DATE(2022,2,15),DATE(2018,12,1),DATE(2019,2,15),0.05,0.06,100,2,0)
    

### Basis

The _basis_ argument controls how days are counted. The ODDFPRICE function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on Wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   All dates, plus _frequency_ and _basis_, are truncated to integers.
*   If dates are invalid (i.e. not actually dates) ODDFPRICE returns #VALUE!
*   ODDFPRICE returns #NUM when:
    *   (_maturity_ > _first\_coupon_ > _settlement_ > _issue_) is not true
    *   _Maturity_ does not follow _frequency_ interval w.r.t last coupon date
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

*   [Microsoft ODDFPRICE function documentation](https://support.office.com/en-us/article/oddfprice-function-d7d664a8-34df-4233-8d2b-922bcf6a69e1)
    

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