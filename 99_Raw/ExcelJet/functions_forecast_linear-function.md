# Excel FORECAST.LINEAR function | Exceljet

**Source:** https://exceljet.net/functions/forecast.linear-function

---

[Skip to main content](https://exceljet.net/functions/forecast.linear-function#main-content)

[](https://exceljet.net/functions/forecast.linear-function#)

*   [Previous](https://exceljet.net/functions/forecast.ets.stat-function)
    
*   [Next](https://exceljet.net/functions/frequency-function)
    

Excel 2016

[Statistical](https://exceljet.net/functions#Statistical)

FORECAST.LINEAR Function
========================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[FORECAST](https://exceljet.net/functions/forecast-function)

[FORECAST.LINEAR](https://exceljet.net/functions/forecast.linear-function)

[FORECAST.ETS](https://exceljet.net/functions/forecast.ets-function)

[FORECAST.ETS.CONFINT](https://exceljet.net/functions/forecast.ets.confint-function)

[FORECAST.ETS.SEASONALITY](https://exceljet.net/functions/forecast.ets.seasonality-function)

[FORECAST.ETS.STAT](https://exceljet.net/functions/forecast.ets.stat-function)

![Excel FORECAST.LINEAR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/forecast.linear%20function.png "Excel FORECAST.LINEAR function")

Summary
-------

The FORECAST.LINEAR function predicts a value based on existing values along a linear trend. FORECAST.LINEAR calculates future value predictions using linear regression, and can be used to predict numeric values like sales, inventory, test scores, expenses, measurements, etc.

_Note: Starting with Excel 2016, the [FORECAST function](https://exceljet.net/functions/forecast-function)
 was replaced with the FORECAST.LINEAR function. Microsoft recommends replacing FORECAST with FORECAST.LINEAR, since FORECAST will eventually be deprecated._

Purpose 
--------

Predict value along a linear trend

Return value 
-------------

Predicted value

Syntax
------

    =FORECAST.LINEAR(x,known_ys,known_xs)

*   _x_ - The x value data point to use to calculate a prediction.
*   _known\_ys_ - The dependent array or range of data (y values).
*   _known\_xs_ - The independent array or range of data (x values).

Using the FORECAST.LINEAR function 
-----------------------------------

The FORECAST.LINEAR function predicts a value based on existing values along a linear trend. FORECAST.LINEAR calculates future value predictions using linear regression, and can be used to predict numeric values like sales, inventory, test scores, expenses, measurements, etc.

_Note: Starting with Excel 2016, the [FORECAST function](https://exceljet.net/functions/forecast-function)
 was replaced with the FORECAST.LINEAR function. Microsoft recommends replacing FORECAST with FORECAST.LINEAR, since FORECAST will eventually be deprecated._

In statistics, linear regression is an approach for modeling the relationship between a dependent variable (y values) and an independent variable (x values). FORECAST.LINEAR uses this approach to calculate a y value for a given x value based on existing x and y values. In other words, for a given value x, FORECAST.LINEAR returns a predicted value based on the linear regression relationship between x values and y values.

### Example

In the example shown above, the formula in cell D13 is:

    =FORECAST.LINEAR(B13,sales,periods)
    

where **sales** (C5:C12) and **periods** (B5:B12) are [named ranges](https://exceljet.net/glossary/named-range)
. With these inputs, the FORECAST.LINEAR function returns 1505.36 in cell D13. As the formula is copied down the table, FORECAST.LINEAR returns predicted values in D13:D16, using values in column B for x.

The chart to the right shows this data plotted in a [scatter plot](https://exceljet.net/chart-types/scatter-plot)
.

_Note: Although FORECAST calculates future value predictions, it can also be used to interpolate and even predict the past. Mark at Excel Off The Grid has a [detailed explanation here](https://exceloffthegrid.com/interpolate-values-using-the-forecast-function/)
._

### Notes

*   If _x_ is not numeric, FORECAST.LINEAR returns a #VALUE! error.
*   If _known\_ys_ and _known\_xs_ are not the same size, FORECAST.LINEAR will #N/A.
*   If the variance of _known\_x_ values is zero, FORECAST.LINEAR will return #DIV/0!.

Related functions
-----------------

[![Excel FORECAST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/forecast%20function.png "Excel FORECAST function")](https://exceljet.net/functions/forecast-function)

### [FORECAST Function](https://exceljet.net/functions/forecast-function)

The Excel FORECAST function predicts a value based on existing values along a linear trend. FORECAST calculates future value predictions using linear regression, and can be used to predict numeric values like sales, inventory, expenses, measurements, etc.

_Note: Starting with_...

[![Excel FORECAST.LINEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/forecast.linear%20function.png "Excel FORECAST.LINEAR function")](https://exceljet.net/functions/forecast.linear-function)

### [FORECAST.LINEAR Function](https://exceljet.net/functions/forecast.linear-function)

The FORECAST.LINEAR function predicts a value based on existing values along a linear trend. FORECAST.LINEAR calculates future value predictions using linear regression, and can be used to predict numeric values like sales, inventory, test scores, expenses, measurements, etc.

...

[![Excel FORECAST.ETS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/forecast.ets%20function.png "Excel FORECAST.ETS function")](https://exceljet.net/functions/forecast.ets-function)

### [FORECAST.ETS Function](https://exceljet.net/functions/forecast.ets-function)

The Excel FORECAST.ETS function predicts a value based on existing values that follow a seasonal trend. FORECAST.ETS can be used to predict numeric values like sales, inventory, expenses, etc. with a seasonal pattern.

[![Excel FORECAST.ETS.CONFINT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/forecast.ets_.confint%20function.png "Excel FORECAST.ETS.CONFINT function")](https://exceljet.net/functions/forecast.ets.confint-function)

### [FORECAST.ETS.CONFINT Function](https://exceljet.net/functions/forecast.ets.confint-function)

The Excel FORECAST.ETS.CONFINT function returns a confidence interval for a forecast value at a specific point on a timeline. It is designed to be used along with the [FORECAST.ETS function](https://exceljet.net/functions/forecast.ets-function)
 as a way to show forecast accuracy.

[![Excel FORECAST.ETS.SEASONALITY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/forecast.ets_.seasonality%20function.png "Excel FORECAST.ETS.SEASONALITY function")](https://exceljet.net/functions/forecast.ets.seasonality-function)

### [FORECAST.ETS.SEASONALITY Function](https://exceljet.net/functions/forecast.ets.seasonality-function)

The Excel FORECAST.ETS.SEASONALITY function returns the length in time of a seasonal pattern based on existing values and a timeline.

[![Excel FORECAST.ETS.STAT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/forecast.ets_.stat%20function.png "Excel FORECAST.ETS.STAT function")](https://exceljet.net/functions/forecast.ets.stat-function)

### [FORECAST.ETS.STAT Function](https://exceljet.net/functions/forecast.ets.stat-function)

The Excel FORECAST.ETS.STAT function returns a particular statistical value related to time series forecasting with the [FORECAST.ETS function](https://exceljet.net/functions/forecast.ets-function)
. The _statistic\_type_ argument determines which statistic is returned by FORECAST.ETS.STAT...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FORECAST Function](https://exceljet.net/functions/forecast-function)
    
*   [FORECAST.LINEAR Function](https://exceljet.net/functions/forecast.linear-function)
    
*   [FORECAST.ETS Function](https://exceljet.net/functions/forecast.ets-function)
    
*   [FORECAST.ETS.CONFINT Function](https://exceljet.net/functions/forecast.ets.confint-function)
    
*   [FORECAST.ETS.SEASONALITY Function](https://exceljet.net/functions/forecast.ets.seasonality-function)
    
*   [FORECAST.ETS.STAT Function](https://exceljet.net/functions/forecast.ets.stat-function)
    

### Links

*   [Microsoft FORECAST.LINEAR function documentation](https://support.office.com/en-us/article/forecasting-functions-reference-897a2fe9-6595-4680-a0b0-93e0308d5f6e)
    

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