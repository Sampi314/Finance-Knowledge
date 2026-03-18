# Excel DURATION function | Exceljet

**Source:** https://exceljet.net/functions/duration-function

---

[Skip to main content](https://exceljet.net/functions/duration-function#main-content)

[](https://exceljet.net/functions/duration-function#)

*   [Previous](https://exceljet.net/functions/dollarfr-function)
    
*   [Next](https://exceljet.net/functions/effect-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

DURATION Function
=================

by Dave Bruns · Updated 26 Aug 2021

Related functions 
------------------

[MDURATION](https://exceljet.net/functions/mduration-function)

![Excel DURATION function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_duration_function.png "Excel DURATION function")

Summary
-------

The Excel DURATION function returns the annual duration of a security with periodic interest payments, calculated with the Macauley duration formula.

Purpose 
--------

Get annual duration with periodic interest

Return value 
-------------

Duration in years

Syntax
------

    =DURATION(settlement,maturity,coupon,yld,freq,[basis])

*   _settlement_ - Settlement date of the security.
*   _maturity_ - Maturity date of the security.
*   _coupon_ - The security's annual coupon rate.
*   _yld_ - The security's annual yield.
*   _freq_ - Number of coupon payments per year (annual = 1, semi-annual = 2, quarterly = 4).
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the DURATION function 
----------------------------

In finance, duration is a measure of the price sensitivity to changes in interest rates for an asset that pays interest on a periodic basis, like a bond. Duration can be used by financial managers as part of a strategy to minimize the impact of interest rates changes on net worth.

Excel's DURATION function returns the [Macauley duration](https://en.wikipedia.org/wiki/Bond_duration#Macaulay_duration)
 for an assumed par value of $100. The Macaulay duration is the weighted average term to maturity of the cash flows from a security. The weight of each cash flow is determined by dividing the present value of the cash flow by the price. Excel also provides the [MDURATION function](https://exceljet.net/functions/mduration-function)
 for calculating modified duration.

### Example

In the example shown, we want to calculate the duration of a bond with an annual coupon rate of 5% and semi-annual payments. The _settlement_ date is 15-Dec-2017, the _maturity_ date is 15-Sep-2027, and the day count _basis i_s US (NASD) 30/360. The formula in F5 is:

    =DURATION(C7,C8,C5,C6,C9,C10)
    

and returns 7.74 years.

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, you can use the [DATE function](https://exceljet.net/functions/date-function)
. To illustrate, the formula below has all values hardcoded, and the DATE function is used to supply each of the two required dates:

    =DURATION(DATE(2017,12,15),DATE(2027,9,15),0.05,0.05,2,0)
    

### Basis

The _basis_ argument controls how days are counted. The DISC function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on Wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
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
*   All dates, _frequency_, and _basis_ are truncated to integers.
*   If dates are invalid (i.e. not actually dates) DURATION returns #VALUE!
*   DURATION returns #NUM when:
    *   _settlement_ >= _maturity_
    *   _coupon_ < 0 or _yield_ < 0
    *   _Basis_ is out-of-range

Related functions
-----------------

[![Excel MDURATION function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mduration_function.png "Excel MDURATION function")](https://exceljet.net/functions/mduration-function)

### [MDURATION Function](https://exceljet.net/functions/mduration-function)

The Excel MDURATION function returns the Macauley modified duration for a security with an assumed par value of $100

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [MDURATION Function](https://exceljet.net/functions/mduration-function)
    

### Links

*   [Microsoft DURATION function documentation](https://support.office.com/en-us/article/duration-function-b254ea57-eadc-4602-a86a-c8e369334038)
    

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