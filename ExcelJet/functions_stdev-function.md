# Excel STDEV function | Exceljet

**Source:** https://exceljet.net/functions/stdev-function

---

[Skip to main content](https://exceljet.net/functions/stdev-function#main-content)

[](https://exceljet.net/functions/stdev-function#)

*   [Previous](https://exceljet.net/functions/standardize-function)
    
*   [Next](https://exceljet.net/functions/stdev.p-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

STDEV Function
==============

by Dave Bruns · Updated 19 Dec 2017

Related functions 
------------------

[STDEV.S](https://exceljet.net/functions/stdev.s-function)

[STDEVP](https://exceljet.net/functions/stdevp-function)

[STDEV.P](https://exceljet.net/functions/stdev.p-function)

![Excel STDEV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_stdev.png "Excel STDEV function")

Summary
-------

The Excel STDEV function returns the standard deviation for data that represents a sample. To calculate the standard deviation for an entire population, use STDEVP or STDEV.P.

Purpose 
--------

Get the standard deviation in a sample

Return value 
-------------

Estimated standard deviation

Syntax
------

    =STDEV(number1,[number2],...)

*   _number1_ - First number or reference in the sample.
*   _number2_ - \[optional\] Second number or reference.

Using the STDEV function 
-------------------------

The STDEV function calculates the standard deviation for a sample set of data. Standard deviation measures how much variance there is in a set of numbers compared to the average (mean) of the numbers. The STDEV function is meant to estimate standard deviation in a sample. If data represents an entire population, use the STDEVP function.

In the example shown, the formula in F7 is:

    =STDEV(C5:C11)
    

_Note: Microsoft classifies STDEV as a "[compatibility function](https://exceljet.net/glossary/compatibility-function)
", now replaced by the [STDEV.S function](https://exceljet.net/functions/stdev.s-function)
._

### Standard Deviation functions in Excel

The table below summarizes the standard deviation functions provided by Excel.

| Name | Data set | Text and logicals |
| --- | --- | --- |
| [STDEV](https://exceljet.net/functions/stdev-function) | Sample | Ignored |
| [STDEVP](https://exceljet.net/functions/stdevp-function) | Population | Ignored |
| [STDEV.S](https://exceljet.net/functions/stdev.s-function) | Sample | Ignored |
| [STDEV.P](https://exceljet.net/functions/stdev.p-function) | Population | Ignored |
| [STDEVA](https://exceljet.net/functions/stdeva-function) | Sample | Evaluated |
| [STDEVPA](https://exceljet.net/functions/stdevpa-function) | Population | Evaluated |

Notes:

*   STDEV calculates standard deviation using the "n-1" method.
*   STDEV assumes data is a sample only. When data represents an entire population, use STDEVP or STDEV.P.
*   Numbers are supplied as arguments. They can be supplied as actual numbers, ranges, arrays, or references that contain numbers.
*   STDEV ignores text and logical values that occur in references, but evaluates text and logicals hardcoded as function arguments.
*   To evaluate logical values and/or text in the calculation, use the [STDEVA function](https://exceljet.net/functions/stdeva-function)
    .

STDEV function examples
-----------------------

[![Excel formula: Standard deviation calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/standard%20deviation%20calculation.png "Excel formula: Standard deviation calculation")](https://exceljet.net/formulas/standard-deviation-calculation)

### [Standard deviation calculation](https://exceljet.net/formulas/standard-deviation-calculation)

Standard deviation in Excel Standard deviation is a measure of how much variance there is in a set of numbers compared to the average (mean) of the numbers. To calculate standard deviation in Excel, you can use one of two primary functions, depending on the data set. If the data represents the...

Related functions
-----------------

[![Excel STDEV.S function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.s.png "Excel STDEV.S function")](https://exceljet.net/functions/stdev.s-function)

### [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)

The Excel STDEV.S function calculates the standard deviation for a sample set of data. STDEV.S replaces the older STDEV function, with the same behavior.

[![Excel STDEVP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdevp.png "Excel STDEVP function")](https://exceljet.net/functions/stdevp-function)

### [STDEVP Function](https://exceljet.net/functions/stdevp-function)

The STDEVP function calculates the standard deviation for data that represents a population. STDEVP has been replaced with a newer function called STDEV.P, which has the same behavior.

[![Excel STDEV.P function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.p.png "Excel STDEV.P function")](https://exceljet.net/functions/stdev.p-function)

### [STDEV.P Function](https://exceljet.net/functions/stdev.p-function)

The Excel STDEV.P function calculates the standard deviation for a sample set of data. STDEV.P calculates standard deviation using the "n" method, ignoring logical values and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Standard deviation calculation](https://exceljet.net/formulas/standard-deviation-calculation)
    

### Functions

*   [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)
    
*   [STDEVP Function](https://exceljet.net/functions/stdevp-function)
    
*   [STDEV.P Function](https://exceljet.net/functions/stdev.p-function)
    

### Links

*   [Microsoft STDEV function documentation](https://support.office.com/en-us/article/stdev-function-51fecaaa-231e-4bbb-9230-33650a72c9b0)
    

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