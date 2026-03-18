# Excel FORECAST.ETS.SEASONALITY function | Exceljet

**Source:** https://exceljet.net/functions/forecast.ets.seasonality-function

---

[Skip to main content](https://exceljet.net/functions/forecast.ets.seasonality-function#main-content)

[](https://exceljet.net/functions/forecast.ets.seasonality-function#)

*   [Previous](https://exceljet.net/functions/forecast.ets.confint-function)
    
*   [Next](https://exceljet.net/functions/forecast.ets.stat-function)
    

Excel 2016

[Statistical](https://exceljet.net/functions#Statistical)

FORECAST.ETS.SEASONALITY Function
=================================

by Dave Bruns · Updated 14 Mar 2025

Related functions 
------------------

[FORECAST](https://exceljet.net/functions/forecast-function)

[FORECAST.LINEAR](https://exceljet.net/functions/forecast.linear-function)

[FORECAST.ETS](https://exceljet.net/functions/forecast.ets-function)

[FORECAST.ETS.CONFINT](https://exceljet.net/functions/forecast.ets.confint-function)

[FORECAST.ETS.SEASONALITY](https://exceljet.net/functions/forecast.ets.seasonality-function)

[FORECAST.ETS.STAT](https://exceljet.net/functions/forecast.ets.stat-function)

![Excel FORECAST.ETS.SEASONALITY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/forecast.ets_.seasonality%20function.png "Excel FORECAST.ETS.SEASONALITY function")

Summary
-------

The Excel FORECAST.ETS.SEASONALITY function returns the length in time of a seasonal pattern based on existing values and a timeline.

Purpose 
--------

Get length of the seasonal pattern

Return value 
-------------

Season length in timeline units

Syntax
------

    =FORECAST.ETS.SEASONALITY(values,timeline,[data_completion],[aggregation])

*   _values_ - Existing or historical values (y values).
*   _timeline_ - Numeric timeline values (x values).
*   _data\_completion_ - \[optional\] Missing data treatment (0 = treat as zero, 1 = average). Default is 1.
*   _aggregation_ - \[optional\] Aggregation behavior. Default is 1 (AVERAGE). See other options below.

Using the FORECAST.ETS.SEASONALITY function 
--------------------------------------------

The FORECAST.ETS.SEASONALITY function returns the length in time of a seasonal pattern based on existing values and a timeline. FORECAST.ETS.SEASONALITY can be used to calculate the season length for numeric values like sales, inventory, expenses, etc. exhibit a seasonal pattern. If a pattern cannot be detected, FORECAST.ETS.SEASONALITY returns zero.

### Example

In the example shown, the formula in cell H16 is:

    =FORECAST.ETS.SEASONALITY(C5:C16,B5:B16)
    

where C5:C16 contains existing values, and B5:B16 contains a timeline. With these inputs, the FORECAST.ETS.SEASONALITY function returns 4. The result is 4 because the values in C5:C16 represent quarterly sales data, and the length of the season is 1 year, which is 4 quarters. 

The chart to the right shows this data plotted in a [scatter plot](https://exceljet.net/chart-types/scatter-plot)
.

### Argument notes

The _values_ argument contains the dependent array or range of data, also called y values. These are existing historical values from which a season length will be calculated.

The _timeline_ argument is the independent array or range of values, also called x values. The timeline must consist of numeric values with a constant step interval. For example, the timeline could be yearly, quarterly, monthly, daily, etc. The timeline can also be a simple list of numeric periods, as in the example shown.

The _data\_completion_ argument is optional and specifies how FORECAST.ETS.SEASONALITY should handle missing data points. The options are 1 (default) and zero. By default, FORECAST.ETS.SEASONALITY will provide missing data points by averaging neighboring data points. If zero is provided for data\_completion, FORECAST.ETS.SEASONALITY will treat missing data points as zeros.

The _aggregation_ argument is optional, and controls how the function should aggregate data points when the timeline contains duplicate timestamps. The default is 1, which specifies AVERAGE. Other options are given in the table below.

_Note: It is better to perform aggregation before using_ FORECAST.ETS.SEASONALITY _to make results as accurate as possible._

| Value | Behavior |
| --- | --- |
| 1 (or omitted) | AVERAGE |
| 2   | COUNT |
| 3   | COUNTA |
| 4   | MAX |
| 5   | MEDIAN |
| 6   | MIN |
| 7   | SUM |

### Errors

The FORECAST.ETS.SEASONALITY function will return errors, as shown below.

| Error | Cause |
| --- | --- |
| #VALUE! | *   _seasonality_ is not numeric<br>*   _data\_completion_ is not numeric<br>*   _aggregation_  is not numeric |
| #N/A | *   _values_ and _timeline_ are not the same size |
| #NUM | *   Consistent step cannot be determined in _timeline_<br>*   All _timeline_ values are the same<br>*   The value for _data\_completion_ is not 0 or 1<br>*   The value for _aggregation_ is not within 1-7 |

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

*   [Microsoft FORECAST.ETS.SEASONALITY function documentation](https://support.office.com/en-us/article/forecasting-functions-reference-897a2fe9-6595-4680-a0b0-93e0308d5f6e)
    

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