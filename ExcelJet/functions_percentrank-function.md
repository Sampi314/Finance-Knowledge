# Excel PERCENTRANK function | Exceljet

**Source:** https://exceljet.net/functions/percentrank-function

---

[Skip to main content](https://exceljet.net/functions/percentrank-function#main-content)

[](https://exceljet.net/functions/percentrank-function#)

*   [Previous](https://exceljet.net/functions/percentile.inc-function)
    
*   [Next](https://exceljet.net/functions/percentrank.exc-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

PERCENTRANK Function
====================

by Dave Bruns · Updated 27 Sep 2023

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

[RANK](https://exceljet.net/functions/rank-function)

[PERCENTILE](https://exceljet.net/functions/percentile-function)

[QUARTILE](https://exceljet.net/functions/quartile-function)

![Excel PERCENTRANK function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_percentrank.png "Excel PERCENTRANK function")

Summary
-------

The Excel PERCENTRANK function returns the rank of a value in a data set as a percentage of the data set. You can use PERCENTRANK to find the relative standing of a value within a data set. Percentile rank is commonly used as a way to interpret standing in standardized tests.

Purpose 
--------

Get percentile rank, inclusive

Return value 
-------------

Calculated rank as a decimal value

Syntax
------

    =PERCENTRANK(array,x,[significance])

*   _array_ - Array of data values.
*   _x_ - Value to rank.
*   _significance_ - \[optional\] Number of significant digits in result. Defaults to 3.

Using the PERCENTRANK function 
-------------------------------

The PERCENTRANK function returns the relative standing of a value within a data set as a percentage. For example, a test score greater than 80% of all test scores is said to be at the 80th percentile. In this case, PERCENTRANK will assign a rank of .80 to the score. To use PERCENTRANK, provide an _array_ of values (typically a range) and the value to rank, _x_. In the example shown, the formula in C5 is:

    =PERCENTRANK(data,B5)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B12. As the formula is copied down, it returns the rank of each value in column B as a decimal value. To display the results in column C as a percentage, apply the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
. The table in the range F4:G15 is for reference only. It uses the [PERCENTILE function](https://exceljet.net/functions/percentile-function)
 in column G to calculate a percentile for each value in column F. A percentile is the value below which a given percentage of observations in a group fall.

> The named range **data** is used for convenience only, since named ranges automatically behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
> . If you prefer, you can use an absolute reference like $B$5:$B$12 instead of a named range.

_Note: Microsoft classifies PERCENTRANK as a "[compatibility function](https://exceljet.net/glossary/compatibility-function)
", now replaced by the PERCENTRANK.INC function._

### Inclusive vs. Exclusive

Starting with Excel 2010, the PERCENTRANK function has been replaced by two functions: [PERCENTRANK.INC](https://exceljet.net/functions/percentrank.inc-function)
 and [PERCENTRANK.EXC](https://exceljet.net/functions/percentrank.exc-function)
. The INC version represents "inclusive" behavior, and the EXC version represents "exclusive" behavior. Both formulas use the same arguments.

*   Use the PERCENTRANK.EXC function to determine the percentage rank _exclusive_ of the first and last values in the array.
*   Use the PERCENTRANK.INC or PERCENTRANK to find the percentage rank _inclusive_ of the first and last values in the array. 

### Notes

*   If x does not exist in the array, PERCENTRANK interpolates to find the percentage rank.
*   When significance is omitted PERCENTRANK returns three significant digits (0.xxx)

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

*   [Microsoft PERCENTRANK function documentation](https://support.office.com/en-us/article/percentrank-function-f1b5836c-9619-4847-9fc9-080ec9024442)
    

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