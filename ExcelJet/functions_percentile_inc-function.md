# Excel PERCENTILE.INC function | Exceljet

**Source:** https://exceljet.net/functions/percentile.inc-function

---

[Skip to main content](https://exceljet.net/functions/percentile.inc-function#main-content)

[](https://exceljet.net/functions/percentile.inc-function#)

*   [Previous](https://exceljet.net/functions/percentile.exc-function)
    
*   [Next](https://exceljet.net/functions/percentrank-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

PERCENTILE.INC Function
=======================

by Dave Bruns · Updated 29 Nov 2021

Related functions 
------------------

[PERCENTILE.EXC](https://exceljet.net/functions/percentile.exc-function)

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

[RANK](https://exceljet.net/functions/rank-function)

![Excel PERCENTILE.INC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_percentile.inc_.png "Excel PERCENTILE.INC function")

Summary
-------

The Excel PERCENTILE.INC function calculates the "kth percentile" for a set of data where _k_ is 0 to 1, inclusive. A percentile is a value below which a given percentage of values in a data set fall. You can use PERCENTILE.INC to determine the 90th percentile, the 80th percentile, etc.

Purpose 
--------

Get kth percentile

Return value 
-------------

Calculated percentile for k

Syntax
------

    =PERCENTILE.INC(array,k)

*   _array_ - Data values.
*   _k_ - Number representing kth percentile.

Using the PERCENTILE.INC function 
----------------------------------

The Excel PERCENTILE.INC function calculates the "kth percentile" for a set of data, where _k_ is between 0 and 1, inclusive. A percentile is a value below which a given percentage of values in a data set fall. A percentile calculated with .4 as _k_ means 40% percent of values are less than or equal to the calculated result, a percentile calculated with _k_ = .9 means 90% percent of values are less than or equal to the calculated result.

To use PERCENTILE.INC, provide a range of values and a number between 0 and 1 for the "_k_" argument, which represents percent. For example:

    =PERCENTILE.INC(range,.4) // 40th percentile
    =PERCENTILE.INC(range,.9) // 90th percentile
    

You can also specify _k_ as a percent using the % character:

    =PERCENTILE.INC(range,80%) // 80th percentile
    

PERCENTILE.INC returns a value greater than or equal to the specified percentile.

In the example shown, the formula in G5 is:

    =PERCENTILE.INC(scores,E5)
    

where "scores" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C14.

### PERCENTILE.INC vs. PERCENTILE.EXC

PERCENTILE.INC includes the full range of 0 to 1 as valid _k_ values, compared to PERCENTILE.EXC which excludes percentages below 1/(N+1) and above N/(N+1).

![Difference between PERCENTILE.INC and PERCENTILE.EXC](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_percentile_inc_diff.png?itok=8T5u4gem "Difference between PERCENTILE.INC and PERCENTILE.EXC")

_Note: Microsoft classifies PERCENTILE as a "[compatibility function](https://exceljet.net/glossary/compatibility-function)
", now replaced by the PERCENTILE.INC function._

### Notes

*   _k_ can be provided as a decimal (.5) or a percentage (50%)
*   _k_ must be between 0 and 1, otherwise PERCENTILE.INC will return the #NUM! error.
*   When percentiles fall between values, PERCENTILE.INC will interpolate and return an intermediate value.

Related functions
-----------------

[![Excel PERCENTILE.EXC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_percentile.exc_.png "Excel PERCENTILE.EXC function")](https://exceljet.net/functions/percentile.exc-function)

### [PERCENTILE.EXC Function](https://exceljet.net/functions/percentile.exc-function)

The Excel PERCENTILE.EXC function calculates the "kth percentile" for a set of data where _k_ is 0 to 1. A percentile is a value below which a given percentage of values in a data set fall. You can use PERCENTILE.EXC to determine the 90th percentile, the 80th percentile, etc.

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

*   [PERCENTILE.EXC Function](https://exceljet.net/functions/percentile.exc-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    

### Links

*   [Microsoft PERCENTILE.INC function documentation](https://support.office.com/en-us/article/percentile-inc-function-680f9539-45eb-410b-9a5e-c1355e5fe2ed)
    

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