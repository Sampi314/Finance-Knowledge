# Excel AMORLINC function | Exceljet

**Source:** https://exceljet.net/functions/amorlinc-function

---

[Skip to main content](https://exceljet.net/functions/amorlinc-function#main-content)

[](https://exceljet.net/functions/amorlinc-function#)

*   [Previous](https://exceljet.net/functions/amordegrc-function)
    
*   [Next](https://exceljet.net/functions/coupdaybs-function)
    

Excel 2003

[Financial](https://exceljet.net/functions#Financial)

AMORLINC Function
=================

by Dave Bruns · Updated 21 Aug 2021

Related functions 
------------------

[AMORDEGRC](https://exceljet.net/functions/amordegrc-function)

![Excel AMORLINC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_amorlinc_function.png "Excel AMORLINC function")

Summary
-------

The Excel AMORLINC function returns the depreciation for each accounting period

Purpose 
--------

Depreciation for accounting period

Return value 
-------------

Depreciation in given period

Syntax
------

    =AMORLINC(cost,purchase,first,salvage,period,rate,[basis])

*   _cost_ - Asset cost.
*   _purchase_ - Asset purchase date.
*   _first_ - End date of first period.
*   _salvage_ - Asset salvage value.
*   _period_ - The period for which to calculate depreciation.
*   _rate_ - Rate of depreciation.
*   _basis_ - \[optional\] Day count basis (see below, default =0).

Using the AMORLINC function 
----------------------------

The Excel AMORLINC function returns the depreciation for a given accounting period. This function is provided for the French accounting system. Depreciation is prorated based on the date an asset is purchased in the first period.

### Example

In the example shown, an asset was purchased on June 30, 2019 at an initial cost of $10,000. The end of the first period is December 31, 2019 and the depreciation rate is 20% per year. The salvage value is $1000, and the basis is European 30/360. The formula in F7, copied down the table is:

    =AMORLINC($C$5,$C$6,$C$7,$C$8,E7,$C$9,$C$10)
    

Notice with the exception of the period numbers in column E, the other arguments use [absolute references](https://exceljet.net/glossary/absolute-reference)
 to prevent changes when copying.

For period zero, the depreciation is prorated based on a purchase date midway through the year, so the AMORLINC function returns $1,000. The full table of results looks like this: 

| Period | Depreciation | Value |
| --- | --- | --- |
|     |     | $10,000 |
| 0   | $1,000 | $9,000 |
| 1   | $2,000 | $7,000 |
| 2   | $2,000 | $5,000 |
| 3   | $2,000 | $3,000 |
| 4   | $2,000 | $1,000 |
| 5   | $0  | $1,000 |

### Entering dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
. Generally, the best way to enter valid dates is to use cell references, as shown in the example. To enter valid dates directly inside a function, you can use the [DATE function](https://exceljet.net/functions/date-function)
. To illustrate, the formula below has all values hardcoded, and the DATE function is used to supply each of the two required dates:

    =AMORLINC(10000,date(2019,6,30),date(2019,12,31),1000,3,0.2,4)
    

Note the above formula returns depreciation in period 3.

### Basis

The _basis_ argument controls how days are counted. The DISC function allows 5 options (0-4) and defaults to zero, which specifies US 30/360 _basis_. This [article on wikipedia](https://en.wikipedia.org/wiki/Day_count_convention)
 provides a detailed explanation of available conventions.

| Basis | Day count |
| --- | --- |
| 0 or omitted | US (NASD) 30/360 |
| 1   | Actual/actual |
| 2   | Actual/360 |
| 3   | Actual/365 |
| 4   | European 30/360 |

### Notes

*   AMORLINC will return #VALUE if any dates are invalid.
*   AMORLINC returns #NUM if:
    *   _cost_ <= _salvage_
    *   _rate_ <= 0
    *   _basis_ is not 0-4

Related functions
-----------------

[![Excel AMORDEGRC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_amordegrc_function.png "Excel AMORDEGRC function")](https://exceljet.net/functions/amordegrc-function)

### [AMORDEGRC Function](https://exceljet.net/functions/amordegrc-function)

The Excel AMORDEGRC function returns the depreciation for a given accounting using a depreciation coefficient determined by asset life.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [AMORDEGRC Function](https://exceljet.net/functions/amordegrc-function)
    

### Links

*   [Microsoft AMORLINC function documentation](https://support.office.com/en-us/article/amorlinc-function-7d417b45-f7f5-4dba-a0a5-3451a81079a8)
    

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