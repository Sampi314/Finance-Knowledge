# Excel RRI function | Exceljet

**Source:** https://exceljet.net/functions/rri-function

---

[Skip to main content](https://exceljet.net/functions/rri-function#main-content)

[](https://exceljet.net/functions/rri-function#)

*   [Previous](https://exceljet.net/functions/received-function)
    
*   [Next](https://exceljet.net/functions/sln-function)
    

Excel 2013

[Financial](https://exceljet.net/functions#Financial)

RRI Function
============

by Dave Bruns · Updated 8 Nov 2018

Related functions 
------------------

[GEOMEAN](https://exceljet.net/functions/geomean-function)

![Excel RRI function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel_rri_function.png "Excel RRI function")

Summary
-------

The Excel RRI function returns an equivalent interest rate for the growth of an investment. You can use RRI to calculate Compound Annual Growth Rate (CAGR) in Excel.

Purpose 
--------

Get equivalent interest rate for growth

Return value 
-------------

Calculated interest rate

Syntax
------

    =RRI(nper,pv,fv)

*   _nper_ - Number of periods.
*   _pv_ - Present value of investment.
*   _fv_ - Future value of investment.

Using the RRI function 
-----------------------

The RRI function returns an equivalent interest rate for the growth of an investment. For example, to use RRI to calculate equivalent annual compound interest for a 1000 investment worth 1200 after five years you can use a formula like this:

    =RRI(5,1000,1200) // returns 0.037137289
    

In the example shown, the formula in G6 is:

    =RRI(B11,C6,C11)
    

RRI function examples
---------------------

[![Excel formula: Effective annual interest rate](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/effective%20annual%20interest%20rate.png "Excel formula: Effective annual interest rate")](https://exceljet.net/formulas/effective-annual-interest-rate)

### [Effective annual interest rate](https://exceljet.net/formulas/effective-annual-interest-rate)

The Effective Annual Rate (EAR) is the interest rate after factoring in compounding. In other words, the EAR is the rate actually earned due to the effect of compounding more frequently than once a year (annually). The EFFECT function calculates the effective annual interest rate based on the...

[![Excel formula: CAGR formula examples](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cagr%20formula.png "Excel formula: CAGR formula examples")](https://exceljet.net/formulas/cagr-formula-examples)

### [CAGR formula examples](https://exceljet.net/formulas/cagr-formula-examples)

CAGR stands for Compound Annual Growth Rate. CAGR is the average rate of return for an investment over a period of time. It is the rate of return required for an investment to grow from the starting balance to the ending balance, assuming profits are reinvested each year, and interest compounds...

Related functions
-----------------

[![Excel GEOMEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20geomean%20function.png "Excel GEOMEAN function")](https://exceljet.net/functions/geomean-function)

### [GEOMEAN Function](https://exceljet.net/functions/geomean-function)

The Excel GEOMEAN function returns the geometric mean for a set of numeric values. Geometric mean can be used to calculate average rate of return with variable rates.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [CAGR formula examples](https://exceljet.net/formulas/cagr-formula-examples)
    
*   [Effective annual interest rate](https://exceljet.net/formulas/effective-annual-interest-rate)
    

### Functions

*   [GEOMEAN Function](https://exceljet.net/functions/geomean-function)
    

### Links

*   [Microsoft RRI function documentation](https://support.office.com/en-us/article/rri-function-6f5822d8-7ef1-4233-944c-79e8172930f4)
    

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