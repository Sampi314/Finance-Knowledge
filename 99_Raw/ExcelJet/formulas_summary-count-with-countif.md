# Summary count with COUNTIF - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/summary-count-with-countif

---

[Skip to main content](https://exceljet.net/formulas/summary-count-with-countif#main-content)

[](https://exceljet.net/formulas/summary-count-with-countif#)

*   [Previous](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Next](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    

[Count](https://exceljet.net/formulas#Count)

Summary count with COUNTIF
==========================

by Dave Bruns · Updated 2 Nov 2023

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")

Summary
-------

To create a summary count from a set of data, you can use [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in cell F5 is:

    =COUNTIF(color,E5)
    

where **color** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16. As the formula is copied down, the COUNTIF function returns a count for each value in column E in the range C5:C16.

Generic formula
---------------

    =COUNTIF(range,A1)

Explanation 
------------

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category, color, size, status, etc. The [COUNTIF function](https://exceljet.net/functions/countif-function)
 is a good way to generate these kinds of totals. Also included below are links to a pivot table option and a dynamic array formula option. Both of these alternatives can automatically extract the values to count and generate the counts at the same time.

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 takes two arguments: a _range_ of cells to count, and the _criteria_ to use for counting. For example, to count cells equal to "red" in a range, we could use COUNTIF like this:

    =COUNTIF(range,"red") // count "red" cells
    

In this example, we want a count for 3 colors, so we have manually created a small table that lists all colors in column E. This allows us to use the color names in column E both for labels, _and_ for the criteria that goes into COUNTIF as the second [argument](https://exceljet.net/glossary/function-argument)
. The formula in cell F5 is:

    =COUNTIF(color,E5) // returns 3
    

where **color** is a [named range](https://exceljet.net/glossary/named-range)
 for cells C5:C16. As the formula is copied down, it returns a count for each of the three colors shown in column E. Notice because we are testing for equality, we don't need to use any [logical operators](https://exceljet.net/glossary/logical-operators)
 in _criteria_. We can simply use the value in cell E5 directly for _criteria_.

By default, named ranges behave like absolute references and do not change when copied. This means the reference to **color** does not change, while the reference to E5 is [relative](https://exceljet.net/glossary/relative-reference)
 and changes at each new row.  Alternately, we could use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 instead of a named range like this:

    =COUNTIF($C$5:$C$16,E5) // absolute address
    

The formula above will return the same results.

### Pivot table solution

If you have a limited number of values to count this is a good solution. However, if you have a large list of values that will change over time, a [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 is a better option since it will automatically expand to include new data.

### Dynamic array formula solution

Now that [dynamic array formulas are part of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, it is possible to build a [dynamic summary count with formulas](https://exceljet.net/formulas/dynamic-summary-count)
, including an all-in-one formula. Like a pivot table, a dynamic formula will automatically expand to include new data. Unlike a pivot table, formulas recalculate automatically and do not need to be refreshed.

Related formulas
----------------

[![Excel formula: Summary count with percentage breakdown](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20%20couunt%20with%20percentage%20breakdown_0.png "Excel formula: Summary count with percentage breakdown")](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

### [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

In this example, the goal is to calculate a count and percentage for each category shown in column B. For convenience, the category values in column B are in the named range category (B5:B122). To generate the count, we use the COUNTIF function . The formula in G5, copied through the range G5:G9 is...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

### [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the named range value . The core of the solution explained below is the COUNTIF function , with help from the IF function to suppress a count for...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Two-way summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20summary%20count.png "Excel formula: Two-way summary count")](https://exceljet.net/formulas/two-way-summary-count)

### [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)

In this example, the goal is to count the people shown in the table by both Department (Dept) and Group as shown in the worksheet. A simple way to do this is with the COUNTIFS function. COUNTIFS function The COUNTIFS function is designed to count things based on more than one condition. Conditions...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIFS%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countifs-function)

### [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

In this video, we'll look at how to use the COUNTIFS function to count cells that meet multiple criteria. Let's take a look. In this first set of tables, we have two named ranges , "number" and "color." In column G, I'll enter a formula that satisfies the conditions in column E. The COUNTIFS...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    

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