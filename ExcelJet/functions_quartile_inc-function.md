# Excel QUARTILE.INC function | Exceljet

**Source:** https://exceljet.net/functions/quartile.inc-function

---

[Skip to main content](https://exceljet.net/functions/quartile.inc-function#main-content)

[](https://exceljet.net/functions/quartile.inc-function#)

*   [Previous](https://exceljet.net/functions/quartile.exc-function)
    
*   [Next](https://exceljet.net/functions/rank-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

QUARTILE.INC Function
=====================

by Dave Bruns · Updated 29 Nov 2021

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

[MEDIAN](https://exceljet.net/functions/median-function)

[RANK](https://exceljet.net/functions/rank-function)

[PERCENTILE](https://exceljet.net/functions/percentile-function)

![Excel QUARTILE.INC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_quartile.inc_.png "Excel QUARTILE.INC function")

Summary
-------

The Excel QUARTILE.INC function returns the quartile (each of four equal groups) for a given set of data. QUARTILE.INC can return minimum value, first quartile, second quartile, third quartile, and max value. Starting with Excel 2010, the QUARTILE.INC function replaces the QUARTILE function with the same behavior.

Purpose 
--------

Get the quartile in a data set

Return value 
-------------

Value for requested quartile

Syntax
------

    =QUARTILE.INC(array,quart)

*   _array_ - A reference containing data to analyze.
*   _quart_ - The quartile value to return.

Using the QUARTILE.INC function 
--------------------------------

Use the QUARTILE.INC function to get the quartile for a given set of data. QUARTILE.INC takes two arguments, the _array_ containing numeric data to analyze, and _quart,_ indicating which quartile value to return. The QUARTILE function accepts 5 values for the _quart_ argument, as shown in the table below.

| Quart | Return value |
| --- | --- |
| 0   | Min value |
| 1   | First quartile – 25th percentile |
| 2   | Median value – 50th percentile |
| 3   | Third quartile – 75th percentile |
| 4   | Max value |

### QUARTILE.INC vs QUARTILE.EXC

Percentiles can be defined as "greater than or equal to" (inclusive) or "greater than" (exclusive). The [QUARTILE.INC](https://exceljet.net/functions/quartile.inc-function)
 function is inclusive and has "greater than or equal to" behavior. [QUARTILE.EXC](https://exceljet.net/functions/quartile.exc-function)
 is exclusive, and has "greater than" behavior.  The screen below shows how QUARTILE.INC and QUARTILE.EXC return different results for the same data. Note QUARTILE.EXC cannot be used to get the minimum or maximum value like QUARTILE.INC. 

![QUARTILE.inc vs QUARTILE.exc](https://exceljet.net/sites/default/files/images/functions/inline/quartile.inc%20vs%20quartile.exc_.png "QUARTILE.inc vs QUARTILE.exc")

_Note: Starting with Excel 2010, the QUARTILE.INC function replaces the [QUARTILE function](https://exceljet.net/functions/quartile-function)
 with the same behavior._

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MEDIAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20median%20function.png "Excel MEDIAN function")](https://exceljet.net/functions/median-function)

### [MEDIAN Function](https://exceljet.net/functions/median-function)

The Excel MEDIAN function returns the median (middle number) in the supplied set of data. For example, =MEDIAN(1,2,3,4,5) returns 3.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel PERCENTILE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_percentile.png "Excel PERCENTILE function")](https://exceljet.net/functions/percentile-function)

### [PERCENTILE Function](https://exceljet.net/functions/percentile-function)

The Excel PERCENTILE function calculates the "kth percentile" for a set of data. A percentile is a value below which a given percentage of values in a data set fall. You can use PERCENTILE to determine the 90th percentile, the 80th percentile, etc.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MEDIAN Function](https://exceljet.net/functions/median-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [PERCENTILE Function](https://exceljet.net/functions/percentile-function)
    

### Links

*   [Microsoft QUARTILE.INC function documentation](https://support.office.com/en-us/article/quartile-inc-function-1bbacc80-5075-42f1-aed6-47d735c4819d)
    

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