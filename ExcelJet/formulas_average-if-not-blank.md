# Average if not blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-if-not-blank

---

[Skip to main content](https://exceljet.net/formulas/average-if-not-blank#main-content)

[](https://exceljet.net/formulas/average-if-not-blank#)

*   [Previous](https://exceljet.net/formulas/average-hourly-pay-per-day)
    
*   [Next](https://exceljet.net/formulas/average-if-with-filter)
    

[Average](https://exceljet.net/formulas#Average)

Average if not blank
====================

by Dave Bruns · Updated 28 Feb 2023

Related functions 
------------------

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[FILTER](https://exceljet.net/functions/filter-function)

[AVERAGE](https://exceljet.net/functions/average-function)

![Excel formula: Average if not blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_if_not_blank.png "Excel formula: Average if not blank")

Summary
-------

To calculate an average when corresponding cells are _not blank_, you can use the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
. In the example shown, the formula in cell F5 is:

    =AVERAGEIFS(price,group,"<>")

Where **price** (C5:C16) and **group** (D5:D16) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is 354,575, the average of Prices in C5:C16 when corresponding cells in D5:D16 are _not blank_.

Generic formula
---------------

    =AVERAGEIFS(range1,range2,"<>")

Explanation 
------------

In this example, the goal is to average the Prices in C5:C16 when the Group in D5:D16 is not blank (i.e. not empty). The traditional way to solve this problem is to use the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
. However, you can also use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [AVERAGE function](https://exceljet.net/functions/average-function)
, as explained below. Because FILTER can work with ranges _and_ [arrays](https://exceljet.net/glossary/array)
, it is a more flexible solution.

### Background study

*   [How to use the AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### AVERAGEIFS Function

The AVERAGEIFS function calculates the average of cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. To apply criteria, the AVERAGEIFS function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. The generic syntax for AVERAGEIFS looks like this:

    =AVERAGEIFS(avg_range,range1,criteria1)

In this case, we need to test for only one condition, which is that cells in D5:D16 are _not blank_. We start off with the _avg\_range_, which contains the prices in C5:C16:

    =AVERAGEIFS(price,

Next, we add the range that we need to test, the group values in D5:D16:

    =AVERAGEIFS(price,group,

Finally, we add the _criteria_, which is the not equal to [operator](https://exceljet.net/glossary/logical-operators)
 (<>), which must be enclosed in double quotes (""):

    =AVERAGEIFS(price,group,"<>")

The result is 354,575, the average of Prices in C5:C16 when corresponding cells in D5:D16 are _not blank_ (i.e. have group values). The main challenge with AVERAGEIFS is the [quirky syntax](https://exceljet.net/articles/excels-racon-functions)
. For criteria, we simply use the "not equal to" operator, "<>". We don't provide a value, and it's implied that this means "not equal to nothing", i.e. "not blank". To read more about how to use the AVERAGEIFS function with logical operators and wildcards, [see this page](https://exceljet.net/functions/averageifs-function)
.

### Excluding formulas

The formula above will treat empty strings returned by formulas as not empty. If you have empty strings returned by formulas in the criteria range, you can adjust the criteria like this:

    =AVERAGEIFS(price,group,">""")
    

This version of the formula will treat empty strings returned by formulas as blank.

### FILTER function

In the current version of Excel, another approach is to use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [AVERAGE function](https://exceljet.net/functions/average-function)
 in a formula like this:

    =AVERAGE(FILTER(price,group<>""))

In this formula, we are literally removing values we don't want to average. The FILTER function is configured to return only values in C5:C16 when cells in D5:D16 are _not empty_. FILTER returns the 8 values in the data that meet this condition directly to the AVERAGE function:

    =AVERAGE({355000;209900;448000;129900;189000;385000;679900;439900})

The AVERAGE function calculates an average and returns a final result of 354,575. FILTER is a more flexible function that can apply criteria in ways that AVERAGEIFS can't. For more on the FILTER function, [see this page](https://exceljet.net/functions/filter-function)
.

Related formulas
----------------

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

Related functions
-----------------

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)
    

### Functions

*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    

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