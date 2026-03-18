# Excel FORECAST.ETS.CONFINT function | Exceljet

**Source:** https://exceljet.net/functions/forecast.ets.confint-function

---

[Skip to main content](https://exceljet.net/functions/forecast.ets.confint-function#main-content)

[](https://exceljet.net/functions/forecast.ets.confint-function#)

*   [Previous](https://exceljet.net/functions/forecast.ets-function)
    
*   [Next](https://exceljet.net/functions/forecast.ets.seasonality-function)
    

Excel 2016

[Statistical](https://exceljet.net/functions#Statistical)

FORECAST.ETS.CONFINT Function
=============================

by Dave Bruns · Updated 3 Nov 2020

Related functions 
------------------

[FORECAST](https://exceljet.net/functions/forecast-function)

[FORECAST.LINEAR](https://exceljet.net/functions/forecast.linear-function)

[FORECAST.ETS](https://exceljet.net/functions/forecast.ets-function)

[FORECAST.ETS.CONFINT](https://exceljet.net/functions/forecast.ets.confint-function)

[FORECAST.ETS.SEASONALITY](https://exceljet.net/functions/forecast.ets.seasonality-function)

[FORECAST.ETS.STAT](https://exceljet.net/functions/forecast.ets.stat-function)

![Excel FORECAST.ETS.CONFINT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/forecast.ets_.confint%20function.png "Excel FORECAST.ETS.CONFINT function")

Summary
-------

The Excel FORECAST.ETS.CONFINT function returns a confidence interval for a forecast value at a specific point on a timeline. It is designed to be used along with the [FORECAST.ETS function](https://exceljet.net/functions/forecast.ets-function)
 as a way to show forecast accuracy.

Purpose 
--------

Get confidence interval for forecast value at given date

Return value 
-------------

Confidence interval value

Syntax
------

    =FORECAST.ETS.CONFINT(target_date,values,timeline,[confidence_level],[seasonality],[data_completion],[aggregation])

*   _target\_date_ - The time or period for the prediction (x value).
*   _values_ - Existing or historical values (y values).
*   _timeline_ - Numeric timeline values (x values).
*   _confidence\_level_ - \[optional\] A number between 0 and 1 (exclusive). Default = 0.95.
*   _seasonality_ - \[optional\] Seasonality calculation (0 = no seasonality, 1 = automatic, n = season length in timeline units).
*   _data\_completion_ - \[optional\] Missing data treatment (0 = treat as zero, 1 = average). Default is 1.
*   _aggregation_ - \[optional\] Aggregation behavior. Default is 1 (AVERAGE). See other options below.

Using the FORECAST.ETS.CONFINT function 
----------------------------------------

The FORECAST.ETS.CONFINT function returns a confidence interval for a forecast value at a specific point on a timeline (i.e. a target date or period). It is designed to be used along with the [FORECAST.ETS function](https://exceljet.net/functions/forecast.ets-function)
 as a way to show forecast accuracy.

### Example

In the example shown above, the formula in cell E13 is:

    =FORECAST.ETS.CONFINT(B13,sales,periods,confidence)
    

where **sales** (C5:C12), **periods** (B5:B12), and **confidence** (J4) are [named ranges](https://exceljet.net/glossary/named-range)
. With these inputs, the FORECAST.ETS.CONFINT returns 198.92 in cell E13. This formula is copied down the table, and the resulting confidence interval values in column "CI" are used to calculate the upper and lower bounds of the forecast, as explained below.

The forecast value in cell D13 is calculated with the [FORECAST.ETS function](https://exceljet.net/functions/forecast.ets-function)
 like this:

    =FORECAST.ETS(B13,sales,periods,4)
    

The upper and lower range formulas in F13 and G13 are:

    =D13+E13 // upper
    =D13-E13 // lower
    

The chart below shows Sales, Forecast, Upper, and Lower values data plotted in a [scatter plot](https://exceljet.net/chart-types/scatter-plot)
:

![FORECAST.ETS.CONFINT chart example](https://exceljet.net/sites/default/files/images/functions/inline/forecast.ets_.confint%20chart.png "FORECAST.ETS.CONFINT chart example")

_Note: Cells D12, F12, and G12 are set equal to C12 to connect the existing values to the forecast values in the chart._

### Argument notes

The _target\_date_ argument represents the point on the timeline that a confidence interval prediction should be calculated.

The _values_ argument contains the dependent array or range of data, also called y values. These are existing historical values from which a prediction will be calculated.

The _timeline_ argument is the independent array or range of values, also called x values. The timeline, must consist of numeric values with a constant step interval. For example, the timeline could be yearly, quarterly, monthly, daily, etc. The timeline can also be a simple list of numeric periods, as in the example shown.

The _seasonality_ argument is optional and represents the length of the seasonal pattern expressed in timeline units. For example, in the example shown, data is quarterly, so seasonality is given as 4, since there are 4 quarters in a year, and the seasonal pattern is 1 year. Allowed values are 0 (no seasonality, use linear algorithm), 1 (calculate seasonal pattern automatically), and n (manual season length, a number between 2 and 8784, inclusive).  The number 8784 = 366 x 24, the number of hours in a leap year.

The _data\_completion_ argument is optional and specifies how FORECAST.ETS.CONFINT should handle missing data points. The options are 1 (default) and zero. By default, FORECAST.ETS.CONFINT will provide missing data points by averaging neighboring data points. If zero is provided, FORECAST.ETS.CONFINT will treat missing data points as zero.

The _aggregation_ argument is optional, and controls what function is used to aggregate data points when the timeline contains duplicate values. The default is 1, which specifies AVERAGE. Other options are given in the table below.

_Note: FORECAST.ETS.CONFINT results will be more accurate if aggregation is performed beforehand._

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

The FORECAST.ETS.CONFINT function will return errors as shown below.

| Error | Cause |
| --- | --- |
| #VALUE! | *   _target\_date_ is not numeric<br>*   _seasonality_ is not numeric<br>*   _data\_completion_ is not numeric<br>*   _aggregation_  is not numeric |
| #N/A | *   _values_ and _timeline_ are not the same size |
| #NUM | *   Consistent step cannot be determined in _timeline_<br>*   All _timeline_ values are the same<br>*   The value for _seasonality_ is not within 0-8784<br>*   The value for _data\_completion_ is not 0 or 1<br>*   The value for _aggregation_ is not within 1-7 |

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

*   [Microsoft FORECAST.ETS.CONFINT function documentation](https://support.office.com/en-us/article/forecasting-functions-reference-897a2fe9-6595-4680-a0b0-93e0308d5f6e)
    

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