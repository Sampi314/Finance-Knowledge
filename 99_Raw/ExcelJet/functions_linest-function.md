# Excel LINEST function | Exceljet

**Source:** https://exceljet.net/functions/linest-function

---

[Skip to main content](https://exceljet.net/functions/linest-function#main-content)

[](https://exceljet.net/functions/linest-function#)

*   [Previous](https://exceljet.net/functions/large-function)
    
*   [Next](https://exceljet.net/functions/max-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

LINEST Function
===============

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[SLOPE](https://exceljet.net/functions/slope-function)

[INTERCEPT](https://exceljet.net/functions/intercept-function)

![Excel LINEST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20linest%20function.png "Excel LINEST function")

Summary
-------

The Excel LINEST function returns statistics for a best fit straight line through supplied x and y values. The values returned by LINEST include slope, intercept, standard error values, and more. To find the best fit of a line to the data, LINEST uses the "least squares" method.

Purpose 
--------

Get parameters of linear trend

Return value 
-------------

Array of values

Syntax
------

    =LINEST(known_ys,[known_xs],[const],[stats])

*   _known\_ys_ - An array or range of dependent y values.
*   _known\_xs_ - \[optional\] An array or range of independent x values.
*   _const_ - \[optional\] Boolean - normal or force the constant b to equal 0. Default is TRUE = normal calculation.
*   _stats_ - \[optional\] Boolean - return additional statistics. Default is FALSE = slope and intercept only.

Using the LINEST function 
--------------------------

The LINEST function returns statistics for a best fit straight line through supplied x and y values. The values returned by LINEST include slope, intercept, standard error values, and more, up to [10 different statistics](https://exceljet.net/functions/linest-function#available_statistics)
 in total. To find the best fit of a line to the data, the LINEST function uses the "least squares" method, the standard approach in regression analysis.

The LINEST function returns more than one value at a time in an [array](https://exceljet.net/glossary/array)
. In its most basic form, LINEST returns just intercept and slope. Optionally, LINEST can also return 10 separate statistics for the regression analysis as shown in the worksheet above. In [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports [dynamic arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the array of values will spill into cells in the worksheet automatically. In other versions of Excel, you must enter the LINEST as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 to see all values.

### Available Statistics

The table below shows the statistics that can be returned by the LINEST function. Note the first two, slope and intercept are returned by default. The other statistics are returned by setting the _stats_ argument to TRUE. When all statistics are returned, they are delivered in a 2D [array](https://exceljet.net/glossary/array)
, 5 rows by 2 columns. In the worksheet shown above, the range F4:G8 shows the order in which statistics are returned.

| Statistic | Description |
| --- | --- |
| slope | Slope coefficient |
| intercept | Intercept constant |
| se  | Standard error of slope |
| seb | Standard error of intercept |
| r2  | Coefficient of determination |
| sey | Standard error of y estimate |
| F   | F statistic (F-observed value) |
| df  | Degrees of freedom |
| ssreg | Regression sum of squares |
| ssresid | Residual sum of squares |

### Examples

By default, LINEST returns just two statistics, slope and intercept. For example:

    =LINEST({1.8;5.3;8.2;12;13.5},{1;3;5;7;8}) // default
    

returns a 1 row by 2 column array like this:

    {1.6726,0.1317}
    

Setting the _stats_ argument to TRUE or 1 will cause LINEST to return all 10 statistics:

    =LINEST({1.8;5.3;8.2;12;13.5},{1;3;5;7;8},TRUE,TRUE) // more stats
    

The result is an array with 5 rows and 2 columns:

    {1.6726,0.1317;
    0.0371,0.2017;
    0.9985,0.2124;
    2034.443,3;
    91.7567,0.1353}
    

_Note: values above have been rounded to make them easier to read._

Related functions
-----------------

[![Excel SLOPE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20slope.png "Excel SLOPE function")](https://exceljet.net/functions/slope-function)

### [SLOPE Function](https://exceljet.net/functions/slope-function)

The Excel SLOPE function returns the slope of a regression line based on known y values and known x values. A regression line is a "best fit" line based on known data points.

[![Excel INTERCEPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20intercept.png "Excel INTERCEPT function")](https://exceljet.net/functions/intercept-function)

### [INTERCEPT Function](https://exceljet.net/functions/intercept-function)

The Excel INTERCEPT function returns the point at which a regression line will intersect the y-axis based on known x and y values.

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
    
*   [INTERCEPT Function](https://exceljet.net/functions/intercept-function)
    

### Links

*   [Microsoft LINEST function documentation](https://support.office.com/en-us/article/linest-function-84d7d0d9-6e50-4101-977a-fa7abf772b6d)
    

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