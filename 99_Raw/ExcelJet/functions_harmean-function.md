# Excel HARMEAN function | Exceljet

**Source:** https://exceljet.net/functions/harmean-function

---

[Skip to main content](https://exceljet.net/functions/harmean-function#main-content)

[](https://exceljet.net/functions/harmean-function#)

*   [Previous](https://exceljet.net/functions/growth-function)
    
*   [Next](https://exceljet.net/functions/intercept-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

HARMEAN Function
================

by Dave Bruns · Updated 8 Oct 2021

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[TRIMMEAN](https://exceljet.net/functions/trimmean-function)

[GEOMEAN](https://exceljet.net/functions/geomean-function)

![Excel HARMEAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20harmean%20function.png "Excel HARMEAN function")

Summary
-------

The Excel HARMEAN function returns the harmonic mean for a set of numeric values. The harmonic mean is the reciprocal of the arithmetic mean of reciprocals. Harmonic mean can be used to calculate a mean that reduces the impact of large outliers.

Purpose 
--------

Calculate harmonic mean

Return value 
-------------

Calculated mean

Syntax
------

    =HARMEAN(number1,[number2],...)

*   _number1_ - First value or reference.
*   _number2_ - \[optional\] Second value or reference.

Using the HARMEAN function 
---------------------------

The Excel HARMEAN function returns the harmonic mean for a set of numeric values. The harmonic mean is a kind of numeric average, calculated by dividing the number values in a list by the sum of the reciprocal of each value. In other words, the harmonic mean is the reciprocal of the average of the reciprocals.

Because the harmonic mean tends toward the smallest values in a set of data, it limits the impact of large outliers, but exaggerates the impact of small outliers. The harmonic mean is always less than the geometric mean ([GEOMEAN](https://exceljet.net/functions/geomean-function)
), which is always less than the arithmetic mean ([AVERAGE](https://exceljet.net/functions/average-function)
).

The HARMEAN function takes multiple arguments in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a range. Often, a single range or array is used instead of multiple arguments, as seen in the example worksheet.

### Examples

The average of 1, 2, and 6 is 3. The harmonic mean of 1, 2, and 6 is 1.8:

    =AVERAGE(1,2,6) // returns 3
    =HARMEAN(1,2,6) // returns 1.8
    

In the example shown, the formulas in E5 and E6 are, respectively:

    =AVERAGE(B5:B14)
    =HARMEAN(B5:B14)
    

Note that harmonic mean reduces the impact of the larger outliers in the data set.

### Notes

*   [Arguments](https://exceljet.net/glossary/function-argument)
     can be numbers, names, arrays, or references that contain numbers.
*   Empty cells, and cells that contain text or logical values are ignored.

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel TRIMMEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_trimmean.png "Excel TRIMMEAN function")](https://exceljet.net/functions/trimmean-function)

### [TRIMMEAN Function](https://exceljet.net/functions/trimmean-function)

The Excel TRIMMEAN function calculates mean (average) while excluding outliers. The number of data points to exclude is provided as a percentage.

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

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [TRIMMEAN Function](https://exceljet.net/functions/trimmean-function)
    
*   [GEOMEAN Function](https://exceljet.net/functions/geomean-function)
    

### Links

*   [Microsoft HARMEAN function documentation](https://support.office.com/en-us/article/harmean-function-5efd9184-fab5-42f9-b1d3-57883a1d3bc6)
    

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