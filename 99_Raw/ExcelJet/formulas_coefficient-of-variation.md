# Coefficient of variation - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/coefficient-of-variation

---

[Skip to main content](https://exceljet.net/formulas/coefficient-of-variation#main-content)

[](https://exceljet.net/formulas/coefficient-of-variation#)

*   [Previous](https://exceljet.net/formulas/check-register-balance)
    
*   [Next](https://exceljet.net/formulas/conditional-median-with-criteria)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Coefficient of variation
========================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[STDEV.P](https://exceljet.net/functions/stdev.p-function)

[STDEV.S](https://exceljet.net/functions/stdev.s-function)

[AVERAGE](https://exceljet.net/functions/average-function)

![Excel formula: Coefficient of variation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/coefficient%20of%20variation.png "Excel formula: Coefficient of variation")

Summary
-------

To calculate the coefficient of variation (CV) in Excel you can use the [STDEV.P function](https://exceljet.net/functions/stdev.p-function)
 or [STDEV.S function](https://exceljet.net/functions/stdev.s-function)
 with the [AVERAGE function](https://exceljet.net/functions/average-function)
. In the example shown, the formula in I5 is:

    =H5/AVERAGE(B5:F5)
    

where H5 contains the [calculated standard deviation](https://exceljet.net/formulas/standard-deviation-calculation)
 of B5:F5. The result is formatted with the percentage [number format](https://exceljet.net/articles/custom-number-formats)
.

Generic formula
---------------

    =STDEV.P(B5:F5)/AVERAGE(B5:F5)

Explanation 
------------

The coefficient of variation measures the relative variability of data with respect to the mean. It represents a ratio of the standard deviation to the mean and can be a useful way to compare data series when means are different. It is sometimes called relative standard deviation (RSD).

In this contrived example, the standard deviation is calculated in column H with the STDEV.P function:

    =STDEV.P(B5:F5)
    

Notice that the standard deviation is the same for all data series (1.414214) even though the means vary substantially. To calculate the coefficient of variation (CV), the formula in I5 is:

    =H5/AVERAGE(B5:F5)
    

This formula divides the standard deviation in H5 by the mean of B5:F5, calculated with the AVERAGE function. The result is a decimal value, formatted with the percentage number format. The calculated CV values show variability with respect to the mean more clearly. In the first data series, the CV is nearly 50%. In the last data series, the CV is only .12%.

Related formulas
----------------

[![Excel formula: Standard deviation calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/standard%20deviation%20calculation.png "Excel formula: Standard deviation calculation")](https://exceljet.net/formulas/standard-deviation-calculation)

### [Standard deviation calculation](https://exceljet.net/formulas/standard-deviation-calculation)

Standard deviation in Excel Standard deviation is a measure of how much variance there is in a set of numbers compared to the average (mean) of the numbers. To calculate standard deviation in Excel, you can use one of two primary functions, depending on the data set. If the data represents the...

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

[![Excel formula: Conditional mode with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20mode%20with%20criteria.png "Excel formula: Conditional mode with criteria")](https://exceljet.net/formulas/conditional-mode-with-criteria)

### [Conditional mode with criteria](https://exceljet.net/formulas/conditional-mode-with-criteria)

The MODE function has no built-in way to apply criteria. Given a range, it will return the most frequently occurring number in that range. To apply criteria, we use the IF function inside MODE to filter values in a range. In this example, the IF function filters values by group with an expression...

Related functions
-----------------

[![Excel STDEV.P function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.p.png "Excel STDEV.P function")](https://exceljet.net/functions/stdev.p-function)

### [STDEV.P Function](https://exceljet.net/functions/stdev.p-function)

The Excel STDEV.P function calculates the standard deviation for a sample set of data. STDEV.P calculates standard deviation using the "n" method, ignoring logical values and text.

[![Excel STDEV.S function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.s.png "Excel STDEV.S function")](https://exceljet.net/functions/stdev.s-function)

### [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)

The Excel STDEV.S function calculates the standard deviation for a sample set of data. STDEV.S replaces the older STDEV function, with the same behavior.

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

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
    
*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    
*   [Conditional mode with criteria](https://exceljet.net/formulas/conditional-mode-with-criteria)
    

### Functions

*   [STDEV.P Function](https://exceljet.net/functions/stdev.p-function)
    
*   [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    

### Links

*   [Coefficient of variation (wikipedia)](https://en.wikipedia.org/wiki/Coefficient_of_variation)
    
*   [Standard Deviation (wikipedia)](https://en.wikipedia.org/wiki/Standard_deviation)
    

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