# Basic average example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-average-example

---

[Skip to main content](https://exceljet.net/formulas/basic-average-example#main-content)

[](https://exceljet.net/formulas/basic-average-example#)

*   [Previous](https://exceljet.net/formulas/average-with-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/moving-average-formula)
    

[Average](https://exceljet.net/formulas#Average)

Basic average example
=====================

by Dave Bruns · Updated 13 Jan 2023

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")

Summary
-------

To get the average of a set of numbers, you can use [AVERAGE function](https://exceljet.net/functions/average-function)
. In the example shown, the formula in H5 is:

    =AVERAGE(B5:D5)
    

As the formula is copied down, it calculates a new average for each row using the scores in columns C through F.

Generic formula
---------------

    =AVERAGE(range)

Explanation 
------------

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the [AVERAGE function](https://exceljet.net/functions/average-function)
.

### AVERAGE function

The AVERAGE function calculates the average (arithmetic mean) of numbers provided as [arguments](https://exceljet.net/glossary/function-argument)
. In this example where there are only four quiz values to work with, you could use AVERAGE with separate cell references like this:

    =AVERAGE(C5,D5,E5,F5)

This is a perfectly valid formula, but it will become tedious to enter if there are many values. The more typical way to solve this problem (where all values to average are in a continuous range) is to provide just one range to AVERAGE as seen in cell H5 of the worksheet shown:

    =AVERAGE(C5:F5)

To calculate an average, AVERAGE sums all numeric values and divides by the count of numeric values. The count used by AVERAGE depends on the data. Note that text values and empty cells are ignored, as you can see in rows 9 and 11 of the worksheet shown. However, zero (0) values are included as you can see in row 13.

### Notes

*   AVERAGE includes zero values in the calculation. If you need to ignore zero (0) values in a set of data, you can use the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
    .
*   If the values given to AVERAGE contain errors, AVERAGE will return an error. You can use the [AGGREGATE function to average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)
    .

Related formulas
----------------

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: Average and ignore errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average%20and%20ignore%20errors2.png "Excel formula: Average and ignore errors")](https://exceljet.net/formulas/average-and-ignore-errors)

### [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)

In this example, the goal is to average a list of values that may contain errors. The values to average are in the named range data (B5:B15). Normally, you can use the AVERAGE function to calculate an average. However, if the data contains errors, AVERAGE will return an error. You can see this in...

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20an%20average%20value-thumb.png)](https://exceljet.net/videos/how-to-calculate-an-average-value)

### [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)

In this video we'll look at how to calculate an average value. Let's take a look. In this worksheet we have a list of 16 properties, each with a price and other information. Let's calculate an average price. First, I'll create a named range for the prices. This makes the formulas easier to read and...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageifs-function)

### [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)

In this video we'll look at how to use the AVERAGEIFS function to calculate an average from numbers that meet multiple criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the criteria shown in column K. Note that this data already...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [Average and ignore errors](https://exceljet.net/formulas/average-and-ignore-errors)
    
*   [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)
    

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    

### Videos

*   [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)
    
*   [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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