# Excel TRIMMEAN function | Exceljet

**Source:** https://exceljet.net/functions/trimmean-function

---

[Skip to main content](https://exceljet.net/functions/trimmean-function#main-content)

[](https://exceljet.net/functions/trimmean-function#)

*   [Previous](https://exceljet.net/functions/stdevpa-function)
    
*   [Next](https://exceljet.net/functions/var-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

TRIMMEAN Function
=================

by Dave Bruns · Updated 24 Dec 2017

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[MODE](https://exceljet.net/functions/mode-function)

![Excel TRIMMEAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_trimmean.png "Excel TRIMMEAN function")

Summary
-------

The Excel TRIMMEAN function calculates mean (average) while excluding outliers. The number of data points to exclude is provided as a percentage.

Purpose 
--------

Calculate mean excluding outliers

Return value 
-------------

Calculated mean

Syntax
------

    =TRIMMEAN(array,percent)

*   _array_ - Values to trim and average.
*   _percent_ - The number of data points to exclude from the calculation.

Using the TRIMMEAN function 
----------------------------

The Excel TRIMMEAN function calculates mean (average) while excluding outliers. The number of data points to exclude is provided as a percentage.

TRIMMEAN works by first excluding values from the top and bottom of a data set, then calculating mean. The number of data points is provided as a percentage. The percentage can be input either in decimal format or percent format:

    =TRIMMEAN(A1:A100,0.1) // exclude 10%
    =TRIMMEAN(A1:A100,10%) // exclude 10%
    =TRIMMEAN(A1:A100,0.2) // exclude 20%
    =TRIMMEAN(A1:A100,20%) // exclude 20%
    

It's important to note that TRIMMEAN rounds excluded data points down to the nearest multiple of 2. For example, with 50 data points, 10% equals 5 values. In this case, TRIMMEAN will round 5 down to 4, then exclude two values from the top, of the data set, and two values from the bottom of the data set.

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")](https://exceljet.net/functions/averageif-function)

### [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

[![Excel MODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")](https://exceljet.net/functions/mode-function)

### [MODE Function](https://exceljet.net/functions/mode-function)

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

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
    
*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [MODE Function](https://exceljet.net/functions/mode-function)
    

### Links

*   [Microsoft TRIMMEAN function documentation](https://support.office.com/en-us/article/trimmean-function-d90c9878-a119-4746-88fa-63d988f511d3)
    

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