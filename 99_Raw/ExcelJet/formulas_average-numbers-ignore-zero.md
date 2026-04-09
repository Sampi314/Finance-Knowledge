# Average numbers ignore zero - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-numbers-ignore-zero

---

[Skip to main content](https://exceljet.net/formulas/average-numbers-ignore-zero#main-content)

[](https://exceljet.net/formulas/average-numbers-ignore-zero#)

*   [Previous](https://exceljet.net/formulas/average-last-n-rows)
    
*   [Next](https://exceljet.net/formulas/average-salary-by-department)
    

[Average](https://exceljet.net/formulas#Average)

Average numbers ignore zero
===========================

by Dave Bruns · Updated 16 Jan 2023

Related functions 
------------------

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")

Summary
-------

To get the average of a set of numbers, excluding zero values, use the [AVERAGEIF function](https://exceljet.net/functions/averageif-function)
. In the example shown, the formula in I5, copied down, is:

    =AVERAGEIF(C5:F5,"<>0")
    

On each new row, AVERAGEIF returns the average of non-zero quiz scores only.

Generic formula
---------------

    =AVERAGEIF(range,"<>0")

Explanation 
------------

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the [AVERAGEIF function](https://exceljet.net/functions/averageif-function)
 or the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
. It can also be solved with a combination of [FILTER](https://exceljet.net/functions/filter-function)
 and [AVERAGE](https://exceljet.net/functions/average-function)
. See below for details.

### AVERAGE function

The standard way to calculate an average in Excel with a formula is to use the [AVERAGE function](https://exceljet.net/functions/average-function)
. You can see the results from AVERAGE in column H of the worksheet shown. The formula in H5, copied down, is:

    =AVERAGE(C5:F5)

However, while AVERAGE _will ignore text values and empty cells_, it _will not ignore zero values_ like those in cell E6, D11, and F15. An easy solution in this case is to switch to the AVERAGEIF or AVERAGEIFS function instead.

### AVERAGEIF function

The [AVERAGEIF function](https://exceljet.net/functions/averageif-function)
 calculates the average of the numbers in a range that meet a single condition. To apply criteria, AVERAGEIF supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. In this case, we can use AVERAGEIFS to solve this problem by excluding zero values with the criteria "<>0". The formula in cell I5, copied down, is:

    =AVERAGEIF(C5:F5,"<>0")

Note that the average returned by AVERAGEIF is higher than the average calculated by AVERAGE in rows 6, 11, and 16. This is the effect of excluding Quiz scores equal to zero.

### AVERAGEIFS function

The AVERAGEIFS function works like AVERAGEIF, except it is designed to apply _multiple_ criteria. We can use AVERAGEIFS to solve this problem by excluding zero values with the criteria "<>0" like this:

    =AVERAGEIFS(C5:F5,C5:F5,"<>0")

One difference between AVERAGEIFS and AVERAGEIF is that the average range is always the first argument with AVERAGEIFS, and is required. With AVERAGEIF the average range is the last argument and is optional. For more details on the syntax of AVERAGEIFS with many more examples, [see this page](https://exceljet.net/functions/averageifs-function)
.

### AVERAGE with FILTER

Another way to solve this problem in the current version of Excel is to use the [AVERAGE function](https://exceljet.net/functions/average-function)
 together with the [FILTER function](https://exceljet.net/functions/filter-function)
 in a formula like this:

    =AVERAGE(FILTER(C5:F5,C5:F5<>0))

This is a newer and more flexible way to handle this problem. The FILTER function is configured to select only quiz scores that are not equal to zero like this:

    =FILTER(C5:F5,C5:F5<>0)

The result from FILTER is an [array](https://exceljet.net/glossary/array)
 that contains only non-zero quiz scores. This array is returned directly to the AVERAGE function, which calculates the average. Zero values never make it into the AVERAGE function to start with. For more on FILTER, [see this page](https://exceljet.net/functions/filter-function)
.

Related formulas
----------------

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

Related functions
-----------------

[![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")](https://exceljet.net/functions/averageif-function)

### [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20an%20average%20value-thumb.png)](https://exceljet.net/videos/how-to-calculate-an-average-value)

### [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)

In this video we'll look at how to calculate an average value. Let's take a look. In this worksheet we have a list of 16 properties, each with a price and other information. Let's calculate an average price. First, I'll create a named range for the prices. This makes the formulas easier to read and...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageifs-function)

### [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)

In this video we'll look at how to use the AVERAGEIFS function to calculate an average from numbers that meet multiple criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the criteria shown in column K. Note that this data already...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageif-function)

### [How to use the AVERAGEIF function](https://exceljet.net/videos/how-to-use-the-averageif-function)

In this video, we'll look at how to use the AVERAGEIF function to calculate an average from numbers that meet a single criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the conditions listed in column K. The AVERAGEIF function...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

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
    
*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    

### Functions

*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [How to calculate an average value](https://exceljet.net/videos/how-to-calculate-an-average-value)
    
*   [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)
    
*   [How to use the AVERAGEIF function](https://exceljet.net/videos/how-to-use-the-averageif-function)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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