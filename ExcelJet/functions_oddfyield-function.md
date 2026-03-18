# Excel ODDFYIELD function | Exceljet

**Source:** https://exceljet.net/functions/oddfyield-function

---

[Skip to main content](https://exceljet.net/functions/oddfyield-function#main-content)

[](https://exceljet.net/functions/oddfyield-function#)

*   [Previous](https://exceljet.net/functions/oddfprice-function)
    
*   [Next](https://exceljet.net/functions/oddlprice-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

ODDFYIELD Function
==================

by Dave Bruns · Updated 30 Aug 2021

Related functions 
------------------

[YIELD](https://exceljet.net/functions/yield-function)

[YIELDDISC](https://exceljet.net/functions/yielddisc-function)

[YIELDMAT](https://exceljet.net/functions/yieldmat-function)

[ODDFYIELD](https://exceljet.net/functions/oddfyield-function)

[ODDLYIELD](https://exceljet.net/functions/oddlyield-function)

![Excel ODDFYIELD function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_oddfyield_function.png "Excel ODDFYIELD function")

Summary
-------

The Excel ODDFYIELD function returns the yield of a security with an odd (irregular) first period.

Purpose 
--------

Get yield security with odd first period

Return value 
-------------

Yield as percentage

Syntax
------

    =ODDFYIELD(sd,md,id,fd,rate,pr,redem,freq,[basis])

*   _sd_ - Settlement date of the security.
*   _md_ - Maturity date of the security.
*   _id_ - Issue date of the security.
*   _fd_ - First coupon date.
*   _rate_ - Annual coupon rate of security.
*   _pr_ - Price of security.
*   _redem_ - Redemption value per $100 face value.
*   _freq_ - Coupon payments per year (annual = 1, semiannual = 2; quarterly = 4).
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the ODDFYIELD function 
-----------------------------

Some bonds have an irregular first or last period, so interest payments don't fit a normal schedule. To calculate the yield of a bond with an irregular first period, you can use the ODDFYIELD function. The ODDFYIELD Function returns the yield (as a percentage) of a security with a short or long first period.

### Example

In the example shown, we want to calculate the yield of a bond with a settlement date of 1-Feb-2019. The bond matures on 15-Feb-2022, and pays a coupon rate of 5%, with the first coupon paid on 15-Feb-2019. Payments are semi-annual, the day count basis is US 30/360, and the redemption value is $100. In the example shown, the formula in F5 is:

    =ODDFYIELD(C10,C12,C9,C11,C7,C5,C6,C13,C14)
    

With these inputs, the ODDFYIELD function returns a yield of 6.10%, with the percentage [number format](https://exceljet.net/articles/custom-number-formats)
 applied.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, the [DATE function](https://exceljet.net/functions/date-function)
 is the best option. To illustrate, the formula below has all values hardcoded, with the DATE function used for each of the four required dates:

    =ODDFYIELD(DATE(2019,2,1),DATE(2022,2,15),DATE(2018,12,1),DATE(2019,2,15),0.05,97,100,2,0)
    

### Basis

The _basis_ argument controls how days are counted. The ODDFYIELD function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on Wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   If dates are invalid (i.e. not actually dates) ODDFYIELD returns #VALUE!
*   ODDFYIELD returns #NUM when:
    *   (_maturity_ > _first\_coupon_ > _settlement_ > _issue_) is NOT true
    *   _Rate_ < 0 or _pr_ <= 0
    *   _Basis_ is out-of-range

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

*   [Microsoft ODDFYIELD function documentation](https://support.office.com/en-us/article/oddfyield-function-66bc8b7b-6501-4c93-9ce3-2fd16220fe37)
    

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