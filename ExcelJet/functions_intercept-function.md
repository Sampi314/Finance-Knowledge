# Excel INTERCEPT function | Exceljet

**Source:** https://exceljet.net/functions/intercept-function

---

[Skip to main content](https://exceljet.net/functions/intercept-function#main-content)

[](https://exceljet.net/functions/intercept-function#)

*   [Previous](https://exceljet.net/functions/harmean-function)
    
*   [Next](https://exceljet.net/functions/large-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

INTERCEPT Function
==================

by Dave Bruns · Updated 21 Nov 2021

Related functions 
------------------

[SLOPE](https://exceljet.net/functions/slope-function)

[LINEST](https://exceljet.net/functions/linest-function)

![Excel INTERCEPT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20intercept.png "Excel INTERCEPT function")

Summary
-------

The Excel INTERCEPT function returns the point at which a regression line will intersect the y-axis based on known x and y values.

Purpose 
--------

Get intercept of linear regression line

Return value 
-------------

y-axis intercept value

Syntax
------

    =INTERCEPT(known_ys,known_xs)

*   _known\_ys_ - An array or range of numeric data points (dependent values).
*   _known\_xs_ - An array or range of numeric data points (independent values).

Using the INTERCEPT function 
-----------------------------

The INTERCEPT function returns the point at which a line will intersect the y-axis based on known x and y values. The intercept point is based on a regression line plotted with known x and y values. A regression line is a line that best fits that known data points. Use the INTERCEPT function to calculate the value of a dependent variable when the independent variable is zero (0).

The INTERCEPT function takes two [arguments](https://exceljet.net/glossary/function-argument)
, _known\_ys_ and _known\_xs_, which should be a [range](https://exceljet.net/glossary/range)
 or [array](https://exceljet.net/glossary/array)
 of numeric values. The _known\_ys_ represent dependent values and _known\_xs_ represent independent values. Both arguments must contain the same number values, or INTERCEPT will return #N/A.

### Example

Values can be entered directly in INTERCEPT as [array constants](https://exceljet.net/glossary/array-constant)
:

    =INTERCEPT({2;0},{-1;1}) // returns 1
    

Typically, values are supplied as ranges. In the example shown, the formula in E5 is:

    =INTERCEPT(C5:C9,B5:B9) // returns 2
    

This formula returns 2, based on known\_ys in C5:C9, and known\_xs in B5:B9.

### Equation

The equation for the intercept of the regression line (a) is:

where b is the slope. The formula used by Excel to calculate slope is the same one used by the [SLOPE function](https://exceljet.net/functions/slope-function)
:

In the example shown, the intercept formula can be manually created like this:

    =AVERAGE(C5:C9)-SLOPE(C5:C9,B5:B9)*AVERAGE(B5:B9)
    

This formula returns the same result as that returned by the INTERCEPT function.

### Notes

*   If there is only one set of points, INTERCEPT will return #DIV/0!
*   If the count of _known\_ys_ is different from _known\_xs_, INTERCEPT returns #N/A

Related functions
-----------------

[![Excel SLOPE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20slope.png "Excel SLOPE function")](https://exceljet.net/functions/slope-function)

### [SLOPE Function](https://exceljet.net/functions/slope-function)

The Excel SLOPE function returns the slope of a regression line based on known y values and known x values. A regression line is a "best fit" line based on known data points.

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

*   [SLOPE Function](https://exceljet.net/functions/slope-function)
    
*   [LINEST Function](https://exceljet.net/functions/linest-function)
    

### Links

*   [Microsoft INTERCEPT function documentation](https://support.office.com/en-us/article/intercept-function-2a9b74e2-9d47-4772-b663-3bca70bf63ef)
    

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