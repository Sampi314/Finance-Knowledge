# CAGR formula examples - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cagr-formula-examples

---

[Skip to main content](https://exceljet.net/formulas/cagr-formula-examples#main-content)

[](https://exceljet.net/formulas/cagr-formula-examples#)

*   [Previous](https://exceljet.net/formulas/bond-valuation-example)
    
*   [Next](https://exceljet.net/formulas/calculate-compound-interest)
    

[Financial](https://exceljet.net/formulas#Financial)

CAGR formula examples
=====================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[GEOMEAN](https://exceljet.net/functions/geomean-function)

[RRI](https://exceljet.net/functions/rri-function)

![Excel formula: CAGR formula examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cagr%20formula.png "Excel formula: CAGR formula examples")

Summary
-------

There are several ways to calculate CAGR in Excel. In Excel 2013 and later, the simplest way is to use the [RRI function](https://exceljet.net/functions/rri-function)
. In the example shown, the formula in H9 is:

    =RRI(B11,C6,C11)
    

Generic formula
---------------

    =(end/start)^(1/periods)-1

Explanation 
------------

CAGR stands for Compound Annual Growth Rate. CAGR is the average rate of return for an investment over a period of time. It is the rate of return required for an investment to grow from the starting balance to the ending balance, assuming profits are reinvested each year, and interest compounds annually. There are several ways to calculate CAGR in Excel.

### CAGR with the RRI function

In Excel 2013 and later, you can use the [RRI function](https://exceljet.net/functions/rri-function)
 to calculate CAGR with a simple formula. The formula in H9 is:

    =RRI(B11,C6,C11)
    

where C11 is the ending value in year 5, C6 is the starting value (initial investment), and B11 is the total number of periods.

_Note: unlike most other financial functions in Excel, fv (future value, the third argument) does not need to be entered as a negative number in RRI._

### CAGR with a manual formula

The formula for calculating CAGR manually is:

    =(end/start)^(1/periods)-1
    

In the example shown, the formula in H7 is:

    =(C11/C6)^(1/B11)-1
    

where C11 is the ending value in year 5, C6 is the starting value or initial investment, and B11 is the total number of periods.

The first part of the formula is a measure of total return, and the second part of the formula annualizes the return over the life of the investment.

### CAGR with the GEOMEAN function

The [GEOMEAN function](https://exceljet.net/functions/geomean-function)
 calculates geometric mean, and can also be used to calculate CAGR. To calculate CAGR with GEOMEAN, we need to use relative changes (percentage change + 1), sometimes called a growth factor. We have these values already in column E so we can use them directly in GEOMEAN the function. The formula in H8 is:

    =GEOMEAN(E7:E11)-1
    

Related functions
-----------------

[![Excel GEOMEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20geomean%20function.png "Excel GEOMEAN function")](https://exceljet.net/functions/geomean-function)

### [GEOMEAN Function](https://exceljet.net/functions/geomean-function)

The Excel GEOMEAN function returns the geometric mean for a set of numeric values. Geometric mean can be used to calculate average rate of return with variable rates.

[![Excel RRI function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_rri_function.png "Excel RRI function")](https://exceljet.net/functions/rri-function)

### [RRI Function](https://exceljet.net/functions/rri-function)

The Excel RRI function returns an equivalent interest rate for the growth of an investment. You can use RRI to calculate Compound Annual Growth Rate (CAGR) in Excel.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [GEOMEAN Function](https://exceljet.net/functions/geomean-function)
    
*   [RRI Function](https://exceljet.net/functions/rri-function)
    

### Links

*   [YouTube video on GEOMEAN, IRR (Mike Girvin)](https://www.youtube.com/watch?v=0qa6hf3RiJ4)
    

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