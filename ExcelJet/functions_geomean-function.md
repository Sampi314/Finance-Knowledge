# Excel GEOMEAN function | Exceljet

**Source:** https://exceljet.net/functions/geomean-function

---

[Skip to main content](https://exceljet.net/functions/geomean-function#main-content)

[](https://exceljet.net/functions/geomean-function#)

*   [Previous](https://exceljet.net/functions/gammaln.precise-function)
    
*   [Next](https://exceljet.net/functions/growth-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

GEOMEAN Function
================

by Dave Bruns · Updated 23 Sep 2021

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[TRIMMEAN](https://exceljet.net/functions/trimmean-function)

[HARMEAN](https://exceljet.net/functions/harmean-function)

[RRI](https://exceljet.net/functions/rri-function)

![Excel GEOMEAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20geomean%20function.png "Excel GEOMEAN function")

Summary
-------

The Excel GEOMEAN function returns the geometric mean for a set of numeric values. Geometric mean can be used to calculate average rate of return with variable rates.

Purpose 
--------

Calculate geometric mean

Return value 
-------------

Calculated mean

Syntax
------

    =GEOMEAN(number1,[number2],...)

*   _number1_ - First value or reference.
*   _number2_ - \[optional\] Second value or reference.

Using the GEOMEAN function 
---------------------------

The Excel GEOMEAN function calculates the [geometric mean](https://en.wikipedia.org/wiki/Geometric_mean)
. Geometric mean is the average of a set of products — technically, the nth root of n numbers. The general formula for the geometric mean of n numbers is the nth root of their product. The equation looks like this:

For example, given two numbers, 4 and 9, the long-hand calculation for the geometric mean is 6:

    =(4*9)^(1/2)
    =(36)^(1/2)
    =6
    

The GEOMEAN function returns the same result:

    =GEOMEAN(4,9) // returns 6
    

By contrast, the arithmetic mean is 6.5:

    =(4+9)/2=6.5
    

The GEOMEAN function takes multiple arguments in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a range. Often, a single range or array is used instead of multiple arguments, as seen in the example worksheet.

### Examples

In the example shown, GEOMEAN is used to calculate a compound annual growth rate. To do this we use the growth factor values in column D in the GEOMEAN function, then subtract 1. The formula in G7 is:

    =GEOMEAN(D6:D10)-1
    

### Notes

*   Arguments can be numbers, names, arrays, or references that contain numbers.
*   Empty cells, and cells that contain text or logical values are ignored.
*   If any provided values are less than or equal to zero, GEOMEAN returns #NUM!

GEOMEAN function examples
-------------------------

[![Excel formula: CAGR formula examples](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cagr%20formula.png "Excel formula: CAGR formula examples")](https://exceljet.net/formulas/cagr-formula-examples)

### [CAGR formula examples](https://exceljet.net/formulas/cagr-formula-examples)

CAGR stands for Compound Annual Growth Rate. CAGR is the average rate of return for an investment over a period of time. It is the rate of return required for an investment to grow from the starting balance to the ending balance, assuming profits are reinvested each year, and interest compounds...

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel TRIMMEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_trimmean.png "Excel TRIMMEAN function")](https://exceljet.net/functions/trimmean-function)

### [TRIMMEAN Function](https://exceljet.net/functions/trimmean-function)

The Excel TRIMMEAN function calculates mean (average) while excluding outliers. The number of data points to exclude is provided as a percentage.

[![Excel HARMEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20harmean%20function.png "Excel HARMEAN function")](https://exceljet.net/functions/harmean-function)

### [HARMEAN Function](https://exceljet.net/functions/harmean-function)

The Excel HARMEAN function returns the harmonic mean for a set of numeric values. The harmonic mean is the reciprocal of the arithmetic mean of reciprocals. Harmonic mean can be used to calculate a mean that reduces the impact of large outliers.

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

### Formulas

*   [CAGR formula examples](https://exceljet.net/formulas/cagr-formula-examples)
    

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [TRIMMEAN Function](https://exceljet.net/functions/trimmean-function)
    
*   [HARMEAN Function](https://exceljet.net/functions/harmean-function)
    
*   [RRI Function](https://exceljet.net/functions/rri-function)
    

### Links

*   [Microsoft GEOMEAN function documentation](https://support.office.com/en-us/article/geomean-function-db1ac48d-25a5-40a0-ab83-0b38980e40d5)
    
*   [Explanation of Geometric mean (wikipedia.org)](https://en.wikipedia.org/wiki/Geometric_mean)
    

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