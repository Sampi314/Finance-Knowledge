# Excel PERCENTILE.EXC function | Exceljet

**Source:** https://exceljet.net/functions/percentile.exc-function

---

[Skip to main content](https://exceljet.net/functions/percentile.exc-function#main-content)

[](https://exceljet.net/functions/percentile.exc-function#)

*   [Previous](https://exceljet.net/functions/percentile-function)
    
*   [Next](https://exceljet.net/functions/percentile.inc-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

PERCENTILE.EXC Function
=======================

by Dave Bruns · Updated 29 Nov 2021

Related functions 
------------------

[PERCENTILE.INC](https://exceljet.net/functions/percentile.inc-function)

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

[RANK](https://exceljet.net/functions/rank-function)

![Excel PERCENTILE.EXC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_percentile.exc_.png "Excel PERCENTILE.EXC function")

Summary
-------

The Excel PERCENTILE.EXC function calculates the "kth percentile" for a set of data where _k_ is 0 to 1. A percentile is a value below which a given percentage of values in a data set fall. You can use PERCENTILE.EXC to determine the 90th percentile, the 80th percentile, etc.

Purpose 
--------

Get kth percentile

Return value 
-------------

Calculated percentile for k

Syntax
------

    =PERCENTILE.EXC(array,k)

*   _array_ - Data values.
*   _k_ - A value between 0 and 1 that represents the k:th percentile.

Using the PERCENTILE.EXC function 
----------------------------------

The Excel PERCENTILE.EXC function calculates the "kth percentile" for a set of data. The kth percentile is a value below which _k_ percent of values in the data set fall. A percentile calculated with .4 as _k_ means 40% percent of values are less than or equal to the calculated result, a percentile calculated with _k_ = .9 means 90% percent of values are less than or equal to the calculated result.

To use PERCENTILE.EXC, provide a range of values and a number between 0 and 1 for the "_k_" argument, which represents percent. For example:

    =PERCENTILE.EXC(range,.4) // 40th percentile
    =PERCENTILE.EXC(range,.9) // 90th percentile
    

You can also specify _k_ as a percent using the % character:

    =PERCENTILE.EXC(range,80%) // 80th percentile
    

In the example shown, the formula in G5 is:

    =PERCENTILE.EXC(scores,E5)
    

where "scores" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C14.

### PERCENTILE.INC vs. PERCENTILE.EXC

The reason the PERCENTILE.EXC function is exclusive is because the function excludes percentages from 0 to 1/(N+1) as well as N/(N+1) to 1, where N is the size of the input array. On the other hand, PERCENTILE.INC includes the full range from 0 to 1 as valid _k_ values.

![Difference between the two functions, PERCENTILE.EXC and PERCENTILE.INC](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_percentile.exc_diff2.png?itok=z9lpdEtO "Difference between the two functions, PERCENTILE.EXC and PERCENTILE.INC")

Effectively, PERCENTILE.EXC will always choose a value farther away from the mean of the data set, compared to PERCENTILE.INC. Note that both functions map to the full range of data.

### Error Values

PERCENTILE.EXC will return the #NUM error if _k_ is less than 1/(n+1) or greater than n/(n+1). In the example shown, where the array contains 10 values, the minimum value for _k_ is 0.091 and the maximum is 0.909.

_Note: Microsoft classifies PERCENTILE as a "[compatibility function](https://exceljet.net/glossary/compatibility-function)
", now replaced by the PERCENTILE.INC function._

### Notes

*   _k_ can be provided as a decimal (.5) or a percentage (50%)
*   _k_ must be between 0 and 1, or PERCENTILE.EXC will return the #NUM! error.
*   PERCENTILE.EXC will return the #NUM error if _k_ is less than 1/(n+1) or greater than n/(n+1).
*   PERCENTILE.EXC will interpolate when _k_ is not a multiple of 1/(n+1).

Related functions
-----------------

[![Excel PERCENTILE.INC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_percentile.inc_.png "Excel PERCENTILE.INC function")](https://exceljet.net/functions/percentile.inc-function)

### [PERCENTILE.INC Function](https://exceljet.net/functions/percentile.inc-function)

The Excel PERCENTILE.INC function calculates the "kth percentile" for a set of data where _k_ is 0 to 1, inclusive. A percentile is a value below which a given percentage of values in a data set fall. You can use PERCENTILE.INC to determine the 90th percentile, the 80th percentile, etc....

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [PERCENTILE.INC Function](https://exceljet.net/functions/percentile.inc-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    

### Links

*   [Microsoft PERCENTILE.EXC function documentation](https://support.office.com/en-us/article/percentile-exc-function-bbaa7204-e9e1-4010-85bf-c31dc5dce4ba)
    

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