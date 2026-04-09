# Excel PERCENTRANK.EXC function | Exceljet

**Source:** https://exceljet.net/functions/percentrank.exc-function

---

[Skip to main content](https://exceljet.net/functions/percentrank.exc-function#main-content)

[](https://exceljet.net/functions/percentrank.exc-function#)

*   [Previous](https://exceljet.net/functions/percentrank-function)
    
*   [Next](https://exceljet.net/functions/percentrank.inc-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

PERCENTRANK.EXC Function
========================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

[RANK](https://exceljet.net/functions/rank-function)

[PERCENTILE](https://exceljet.net/functions/percentile-function)

[QUARTILE](https://exceljet.net/functions/quartile-function)

![Excel PERCENTRANK.EXC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_percentrank.exc_.png "Excel PERCENTRANK.EXC function")

Summary
-------

The Excel PERCENTRANK.EXC function returns the relative rank of a value in a data set as a percentage representing how many values are less than or equal to the value. Percentile rank is commonly used as a way to interpret standing in standardized tests.

Purpose 
--------

Get percentile rank, exclusive

Return value 
-------------

Calculated rank as a decimal value

Syntax
------

    =PERCENTRANK.EXC(array,x,[significance])

*   _array_ - Array of data values.
*   _x_ - Value to rank.
*   _significance_ - \[optional\] Number of significant digits in result. Defaults to 3.

Using the PERCENTRANK.EXC function 
-----------------------------------

The Excel PERCENTRANK.INC returns the relative standing of a value within a data set as a percentage. For example, a test score greater than or equal to 80% of all test scores is said to be at the 80th percentile. In the example shown, the formula in C5 is:

    =PERCENTRANK.EXC(data,B5)
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C12.

### Interpolation

When _x_ does not exist within the array, the function interpolates a value between data points. For example, when the _x_ value of 4.00 is passed as an argument to the function, the percentage is interpolated to 44.4%, which lies between the percent ranks of 3.3 and 4.56, which are 37.5% and 50.0%, respectively.

![Interpolation example for PERCENTRANK.EXC](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_percentrank_exc_interpolation.png?itok=C1quoPYj "Interpolation example for PERCENTRANK.EXC")

In the graph below, solid orange dots represent _x_ values that are contained within the input array, while the outlined orange dots are values that are interpolated.

![Interpolation example for PERCENTRANK.EXC](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_percentrank_exc_interpolation%20orange.png?itok=c8aXrGR1 "Interpolation example for PERCENTRANK.EXC")

### Inclusive vs. Exclusive

Starting with Excel 2010, the PERCENTRANK function has been replaced by two distinct functions: [PERCENTRANK.INC](https://exceljet.net/functions/percentrank.inc-function)
 and [PERCENTRANK.EXC](https://exceljet.net/functions/percentrank.exc-function)
. Both functions use the same arguments, but they differ in how they handle the boundaries of the dataset:

*   PERCENTRANK.INC (Inclusive): Calculates the percentage rank of a value within the full range of the dataset, including the first and last values. The output is within the range \[0,1\], inclusive of the endpoints.
*   PERCENTRANK.EXC (Exclusive): Calculates the percentage rank in a slightly different way by conceptually adding two virtual values—one smaller than the smallest actual value and one larger than the largest actual value. As a result, the percentage rank of the smallest value will be slightly above 0, and the rank of the largest value will be slightly below 1. The output falls within the range (0,1), exclusive of the endpoints.

The screen below shows differences with a small data set:

![PERCENTRANK.INC vs PERCENTRANK.EXC data](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/percentrank.inc%20vs%20percentrank.exc%20kurt_0.png?itok=vzyzs4J- "PERCENTRANK.INC vs PERCENTRANK.EXC data")

![PERCENTRANK.INC vs PERCENTRANK.EXC graph](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/percentrank.inc%20vs%20percentrank.exc%20graph_0.png?itok=LkL84Z9E "PERCENTRANK.INC vs PERCENTRANK.EXC graph")

As the size of the input array increases, the difference between the two functions decreases. The difference between the returned percentages will never be larger than 1/(N+1), where N is the size of the input array.

### Notes

*   If _x_ does not exist in the array, PERCENTRANK.EXC interpolates to find the percentage rank.
*   When significance is omitted, PERCENTRANK.EXC returns three significant digits (0.xxx)

Related functions
-----------------

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel PERCENTILE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_percentile.png "Excel PERCENTILE function")](https://exceljet.net/functions/percentile-function)

### [PERCENTILE Function](https://exceljet.net/functions/percentile-function)

The Excel PERCENTILE function calculates the "kth percentile" for a set of data. A percentile is a value below which a given percentage of values in a data set fall. You can use PERCENTILE to determine the 90th percentile, the 80th percentile, etc.

[![Excel QUARTILE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_quartile.png "Excel QUARTILE function")](https://exceljet.net/functions/quartile-function)

### [QUARTILE Function](https://exceljet.net/functions/quartile-function)

The Excel QUARTILE function returns the quartile (each of four equal groups) for a given set of data. QUARTILE can return minimum value, first quartile, second quartile, third quartile, and max value.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [PERCENTILE Function](https://exceljet.net/functions/percentile-function)
    
*   [QUARTILE Function](https://exceljet.net/functions/quartile-function)
    

### Links

*   [Microsoft PERCENTRANK.EXC function documentation](https://support.office.com/en-us/article/percentrank-exc-function-d8afee96-b7e2-4a2f-8c01-8fcdedaa6314)
    

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