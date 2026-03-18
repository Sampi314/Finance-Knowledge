# Average hourly pay per day - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-hourly-pay-per-day

---

[Skip to main content](https://exceljet.net/formulas/average-hourly-pay-per-day#main-content)

[](https://exceljet.net/formulas/average-hourly-pay-per-day#)

*   [Previous](https://exceljet.net/formulas/average-call-time-per-month)
    
*   [Next](https://exceljet.net/formulas/average-if-not-blank)
    

[Average](https://exceljet.net/formulas#Average)

Average hourly pay per day
==========================

by Dave Bruns · Updated 27 Feb 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel formula: Average hourly pay per day](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_hourly_pay_per_day.png "Excel formula: Average hourly pay per day")

Summary
-------

To calculate an average pay per day based on logged hours and hourly rates, you can use a formula based on the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in I5 is:

    =SUMIFS(data[Total],data[Date],H5)/SUMIFS(data[Hours],data[Date],H5)

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:F16. Note this is a _weighted average_ that takes into account the number of hours logged at each rate on each day.

Generic formula
---------------

    =SUMIFS(totals,dates,A1)/SUMIFS(hours,dates,A1)

Explanation 
------------

In this example, the goal is to calculate the average hourly rate per day based on the data shown. All data is in Excel Table named **data** in the range B5:F16. Note that we want to calculate a _weighted average_ in this case. A weighted average hourly rate is the average rate at which the workers are paid, taking into account the number of hours worked at each rate. This weighted average is calculated by multiplying each rate by its corresponding weight (hours worked) for a given date, then dividing by the sum of the hours logged on that date. The solution shown requires four general steps:

1.  Create an [Excel Table](https://exceljet.net/glossary/excel-table)
     called **data**
2.  Create a summary table for results, like H4:I7 in the example
3.  Enter the formula and copy it down the summary table

### Create the Excel Table

One of the key features of an [Excel Table](https://exceljet.net/articles/excel-tables)
 is its ability to dynamically resize when rows are added or removed. In this case, all we need to do is create a new table named **data** with the data shown in B5:D16.  You can use the [keyboard shortcut Control + T](https://exceljet.net/shortcuts/insert-table)
.

Video: [How to create an Excel table](https://exceljet.net/videos/how-to-create-an-excel-table)

The table will now automatically expand or contract as needed when new data is added or removed.

### Total amounts per date

Because we have the total for each entry in column F, we already have rates \* hours. This means we can just use the SUMIFS function (the SUMIF function would work fine too) to get a total for each date with a formula like this:

    SUMIFS(data[Total],data[Date],H5)

The _sum\_range_ is the Total column, the _criteria\_range_ is the Date column, and the criteria itself is the date in cell H5. By itself, this formula will return the total Amount for each date.

### Total hours per date

The next step is to calculate the total hours per date. To do this, we can again use the SUMIFS function in a very similar formula:

    SUMIFS(data[Hours],data[Date],H5)

In this formula, the _sum\_range_ is the Hours column, and the _criteria\_range_ and criteria are the same as the formula above. This formula will return the total Hours logged for each date.

### Divide amounts by hours

The last step is to divide the total amount per date by the total hours per date like this:

    =SUMIFS(data[Total],data[Date],H5)/SUMIFS(data[Hours],data[Date],H5)

In cell I5, the formula is solved like this:

    =SUMIFS(data[Total],data[Date],H5)/SUMIFS(data[Hours],data[Date],H5)
    =518/29
    =17.86

### SUMPRODUCT alternative

As mentioned above, because we have hours \* rate already in column F as Amount, we can use this value directly in the SUMIFS formula as shown. However, in cases where the data does not contain hours \* rate, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to run this calculation inside the formula like this:

    =SUMPRODUCT((data[Date]=H5)*data[Hours]*data[Rate])/SUMIFS(data[Hours],data[Date],H5)

This formula returns the same result, but does not need the Amount in column F to be part of the data. Why not do the same thing with SUMIFS? It's a bit technical, but the reason we can't take the same approach with SUMIFS is that SUMIFS is in a [group of eight Excel functions](https://exceljet.net/articles/excels-racon-functions)
 that _require_ a range. This means we can't supply a calculation for the sum range in this case.

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

[![Excel formula: Basic average example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic_average_example.png "Excel formula: Basic average example")](https://exceljet.net/formulas/basic-average-example)

### [Basic average example](https://exceljet.net/formulas/basic-average-example)

In this example, the goal is to calculate a quiz score average for each person listed in column D using the four scores in columns C, D, E, and F. The standard way to solve this problem in Excel is to use the AVERAGE function . AVERAGE function The AVERAGE function calculates the average (...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

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
    
*   [Basic average example](https://exceljet.net/formulas/basic-average-example)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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