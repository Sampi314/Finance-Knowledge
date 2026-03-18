# Excel SLOPE function | Exceljet

**Source:** https://exceljet.net/functions/slope-function

---

[Skip to main content](https://exceljet.net/functions/slope-function#main-content)

[](https://exceljet.net/functions/slope-function#)

*   [Previous](https://exceljet.net/functions/skew.p-function)
    
*   [Next](https://exceljet.net/functions/small-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

SLOPE Function
==============

by Dave Bruns · Updated 1 Dec 2021

Related functions 
------------------

[INTERCEPT](https://exceljet.net/functions/intercept-function)

[LINEST](https://exceljet.net/functions/linest-function)

![Excel SLOPE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20slope.png "Excel SLOPE function")

Summary
-------

The Excel SLOPE function returns the slope of a regression line based on known y values and known x values. A regression line is a "best fit" line based on known data points.

Purpose 
--------

Get slope of linear regression line

Return value 
-------------

Calculated slope as a number

Syntax
------

    =SLOPE(known_ys,known_xs)

*   _known\_ys_ - An array or range of numeric data points (dependent values).
*   _known\_xs_ - An array or range of numeric data points (independent values).

Using the SLOPE function 
-------------------------

The SLOPE function returns the slope of a regression line based on known y values and known x values. A regression line is a "best fit" line based on known data points.

The slope of a line is a measure of steepness. Mathematically, slope is calculated as "rise over run", or change in y over the change in x. For example, if a line has a slope of 2/1 (2), then if y increases by 2 units, x increases by 1 unit.

### Example

In the example shown, the formula in E5 is:

    =SLOPE(B5:B9,C5:C9) // returns -2
    

This formula returns -2, based on _known\_ys_ in C5:C9, and _known\_xs_ in B5:B9.

### Equation

In statistics, a best fit line does not normally lie exactly on the known x and y points. The equation used by the SLOPE function in Excel is based on the mean of known x's and y's:

For the example shown, this formula can be manually recreated like this:

    =SUM((B5:B9-AVERAGE(B5:B9))*(C5:C9-AVERAGE(C5:C9)))/SUM((B5:B9-AVERAGE(B5:B9))^2)
    

The calculated result from the SLOPE function and the manual formula are the same.

### Notes

*   If there is only one set of points, SLOPE will return #DIV/0!
*   If the count of _known\_ys_ is different from _known\_xs_, SLOPE returns #N/A

Related functions
-----------------

[![Excel INTERCEPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20intercept.png "Excel INTERCEPT function")](https://exceljet.net/functions/intercept-function)

### [INTERCEPT Function](https://exceljet.net/functions/intercept-function)

The Excel INTERCEPT function returns the point at which a regression line will intersect the y-axis based on known x and y values.

[![Excel LINEST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20linest%20function.png "Excel LINEST function")](https://exceljet.net/functions/linest-function)

### [LINEST Function](https://exceljet.net/functions/linest-function)

The Excel LINEST function returns statistics for a best fit straight line through supplied x and y values. The values returned by LINEST include slope, intercept, standard error values, and more. To find the best fit of a line to the data, LINEST uses the "least squares" method....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [INTERCEPT Function](https://exceljet.net/functions/intercept-function)
    
*   [LINEST Function](https://exceljet.net/functions/linest-function)
    

### Links

*   [Microsoft SLOPE function documentation](https://support.office.com/en-us/article/slope-function-11fb8f97-3117-4813-98aa-61d7e01276b9)
    

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