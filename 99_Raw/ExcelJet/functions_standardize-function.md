# Excel STANDARDIZE function | Exceljet

**Source:** https://exceljet.net/functions/standardize-function

---

[Skip to main content](https://exceljet.net/functions/standardize-function#main-content)

[](https://exceljet.net/functions/standardize-function#)

*   [Previous](https://exceljet.net/functions/small-function)
    
*   [Next](https://exceljet.net/functions/stdev-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

STANDARDIZE Function
====================

by Dave Bruns · Updated 1 Dec 2021

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

[RANK](https://exceljet.net/functions/rank-function)

[RANK.AVG](https://exceljet.net/functions/rank.avg-function)

[STDEV.S](https://exceljet.net/functions/stdev.s-function)

[STDEV.P](https://exceljet.net/functions/stdev.p-function)

![Excel STANDARDIZE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_standardize.png "Excel STANDARDIZE function")

Summary
-------

The Excel STANDARDIZE function returns a normalized value (z-score) based on the mean and standard deviation.

Purpose 
--------

Calculate a normalized value (z-score)

Return value 
-------------

Normalized value

Syntax
------

    =STANDARDIZE(x,mean,standard_dev)

*   _x_ - The value to normalize.
*   _mean_ - The arithmetic mean of the distribution.
*   _standard\_dev_ - The standard deviation of the distribution.

Using the STANDARDIZE function 
-------------------------------

The Excel STANDARDIZE function returns a normalized value (z-score) based on the mean and standard deviation. To use the STANDARDIZE function, calculate the mean with the [AVERAGE function](https://exceljet.net/functions/average-function)
, and the standard deviation with the [STDEV.P function](https://exceljet.net/functions/stdev.p-function)
 (see below).

In the example shown, the formula in D5 is:

    =STANDARDIZE(C5,$G$4,$G$5)
    

### About z-scores / standard scores

A z-score, or standard score, is a way of standardizing scores on the same scale by dividing a score's deviation by the standard deviation in a data set. The result is a standard score, or a z-score. It measures the number of standard deviations a given data point is from the mean.

A z-score can be negative or positive. A negative z-score indicates a value less than the mean, and a positive z-score indicates a value greater than the mean. The average of every z-score for a data set is zero.

To calculate a z-score, you need to calculate the mean and standard deviation. The formulas in G4 and G5 are, respectively:

    =AVERAGE(points)
    =STDEV.P(points)
    

Where "points" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C12.

_If you'd like to learn more z-scores, and statistical analysis in Excel, I recommend Joseph Schmuller's book [Statistical Analysis with Excel For Dummies](https://www.amazon.com/Statistical-Analysis-Dummies-Joseph-Schmuller/dp/1119271150)_ 

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

[![Excel RANK.AVG function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank.avg_function.png "Excel RANK.AVG function")](https://exceljet.net/functions/rank.avg-function)

### [RANK.AVG Function](https://exceljet.net/functions/rank.avg-function)

The Excel RANK.AVG function returns the rank of a number against a list of other numeric values. When values contain duplicates, the RANK.AVG function will assign an average rank to each set of duplicates....

[![Excel STDEV.S function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.s.png "Excel STDEV.S function")](https://exceljet.net/functions/stdev.s-function)

### [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)

The Excel STDEV.S function calculates the standard deviation for a sample set of data. STDEV.S replaces the older STDEV function, with the same behavior.

[![Excel STDEV.P function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_stdev.p.png "Excel STDEV.P function")](https://exceljet.net/functions/stdev.p-function)

### [STDEV.P Function](https://exceljet.net/functions/stdev.p-function)

The Excel STDEV.P function calculates the standard deviation for a sample set of data. STDEV.P calculates standard deviation using the "n" method, ignoring logical values and text.

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
    
*   [RANK.AVG Function](https://exceljet.net/functions/rank.avg-function)
    
*   [STDEV.S Function](https://exceljet.net/functions/stdev.s-function)
    
*   [STDEV.P Function](https://exceljet.net/functions/stdev.p-function)
    

### Links

*   [Microsoft STANDARDIZE function documentation](https://support.office.com/en-us/article/standardize-function-81d66554-2d54-40ec-ba83-6437108ee775)
    

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