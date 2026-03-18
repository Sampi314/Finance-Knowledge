# Excel SUBTOTAL function | Exceljet

**Source:** https://exceljet.net/functions/subtotal-function

---

[Skip to main content](https://exceljet.net/functions/subtotal-function#main-content)

[](https://exceljet.net/functions/subtotal-function#)

*   [Previous](https://exceljet.net/functions/sqrtpi-function)
    
*   [Next](https://exceljet.net/functions/sum-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SUBTOTAL Function
=================

by Dave Bruns · Updated 3 Jan 2023

Related functions 
------------------

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

![Excel SUBTOTAL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel%20subtotal%20function.png "Excel SUBTOTAL function")

Summary
-------

The Excel SUBTOTAL function is designed to run a given calculation on a range of cells while ignoring cells that should not be included. SUBTOTAL can return a SUM, AVERAGE, COUNT, MAX, and others (see complete list below), and SUBTOTAL function can either include or exclude values in hidden rows.

Purpose 
--------

Get a subtotal in a list or database

Return value 
-------------

A number representing a specific kind of subtotal

Syntax
------

    =SUBTOTAL(function_num,ref1,[ref2],...)

*   _function\_num_ - A number that specifies which function to use in calculating subtotals within a list. See table below for full list.
*   _ref1_ - A named range or reference to subtotal.
*   _ref2_ - \[optional\] A named range or reference to subtotal.

Using the SUBTOTAL function 
----------------------------

The SUBTOTAL function is designed to run a given calculation on a range of cells while ignoring cells that should not be included. SUBTOTAL has three features that make it especially useful:

1.  It automatically ignores cells that have been filtered out of view.
2.  It automatically ignores existing subtotal formulas to avoid double counting.
3.  It can perform many calculations, including SUM, AVERAGE, COUNT, MAX, MIN, and [others](https://exceljet.net/functions/subtotal-function#subtotal_calculations)
    .

Because SUBTOTAL ignores cells that have been "filtered out", it is especially useful in [Excel Tables](https://exceljet.net/glossary/excel-table)
 or [filtered data](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
. In addition, SUBTOTAL can be optionally set to exclude values in rows that have been _manually_ hidden (i.e. [rows hidden with a shortcut](https://exceljet.net/shortcuts/hide-rows)
 or by Right click > Hide). Regardless of the calculation performed, SUBTOTAL returns single [aggregate result](https://exceljet.net/glossary/aggregate-operation)
 from a set of data. Finally, while SUBTOTAL is good at ignoring things, it _does not_ ignore errors. If you need capability, see the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
.

_Note: the SUBTOTAL function automatically ignores other SUBTOTAL formulas that exist in references to prevent double-counting._

### Examples

Below are  examples of SUBTOTAL configured to SUM, COUNT, and AVERAGE the values in a range. Notice the only difference is the value used for the _function\_num_ argument:

    =SUBTOTAL(109,range) // SUM
    =SUBTOTAL(103,range) // COUNT
    =SUBTOTAL(101,range) // AVERAGE
    

In the worksheet shown above, the formulas in C4 and F4 are:

    =SUBTOTAL(3,B7:B19) // count visible
    =SUBTOTAL(9,F7:F19) // sum visible
    

### Available calculations

The calculation performed by SUBTOTAL is determined by the _function\_num_ argument, which is given as a number. There are 11 calculations total, each with two options, as seen below. Notice these values are "paired" (e.g. 1-101, 2-102, 3-103, and so on). This is related to how SUBTOTAL deals with _manually_ hidden rows. When _function\_num_ is between 1-11, SUBTOTAL _includes_ rows that have been _manually_ hidden. When _function\_num_ is between 101-111, SUBTOTAL _excludes_ rows that have been manually hidden. 

|     |     |     |
| --- | --- | --- |
| **Function** | **Include hidden** | **Ignore hidden** |
| [AVERAGE](https://exceljet.net/functions/average-function) | 1   | 101 |
| [COUNT](https://exceljet.net/functions/count-function) | 2   | 102 |
| [COUNTA](https://exceljet.net/functions/counta-function) | 3   | 103 |
| [MAX](https://exceljet.net/functions/max-function) | 4   | 104 |
| [MIN](https://exceljet.net/functions/min-function) | 5   | 105 |
| [PRODUCT](https://exceljet.net/functions/product-function) | 6   | 106 |
| [STDEV](https://exceljet.net/functions/stdev-function) | 7   | 107 |
| [STDEVP](https://exceljet.net/functions/stdev-function) | 8   | 108 |
| [SUM](https://exceljet.net/functions/sum-function) | 9   | 109 |
| [VAR](https://exceljet.net/functions/var-function) | 10  | 110 |
| [VARP](https://exceljet.net/functions/varp-function) | 11  | 111 |

Note: SUBTOTAL _always_ ignores values in cells that are hidden with a filter. Values in rows that have been "filtered out" are never included, regardless of _function\_num_.

### SUBTOTAL in Excel Tables

The SUBTOTAL function is used when you [display a Total row in an Excel Table](https://exceljet.net/videos/how-to-add-a-totals-row-to-a-table)
. Excel inserts the SUBTOTAL function automatically, and you can use a drop-down menu to switch behavior and show max, min, average, etc.  Excel uses SUBTOTAL for calculations in the Total row of an [Excel Table](https://exceljet.net/articles/excel-tables)
 because SUBTOTAL _automatically_ excludes rows hidden by the filter controls at the top of the table. That is, as you filter rows in a table with a Total row, calculations automatically respect the filter.

### SUBTOTAL with outlines

Excel has a Subtotal feature that automatically inserts SUBTOTAL formulas in sorted data. You can find this feature at Data > Outline > Subtotal. SUBTOTAL formulas inserted this way use the standard function numbers 1-11. This allows the subtotal results to remain visible even as rows are hidden and displayed when the outline is collapsed and expanded.

_Note: although the Outline feature is an "easy" way to insert subtotals in a set of data, a [Pivot Table](https://exceljet.net/articles/excel-pivot-tables)
 is a better and more flexible way to analyze data. In addition, a Pivot Table will separate the data from the presentation of the data, which is a best practice._

### Notes

*   When _function\_num_ is between 1-11, SUBTOTAL _includes_ manually hidden rows.
*   When _function\_num_ is between 101-111, SUBTOTAL _excludes_ manually hidden rows.
*   In filtered lists, SUBTOTAL always ignores values in hidden rows, regardless of _function\_num_.
*   SUBTOTAL ignores other SUBTOTAL formulas that exist in references to prevent double-counting.
*   SUBTOTAL works with vertical data. In horizontal ranges, values in hidden columns are _always_ included.

SUBTOTAL function examples
--------------------------

[![Excel formula: Sum visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_visible_rows_in_a_filtered_list.png "Excel formula: Sum visible rows in a filtered list")](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)

### [Sum visible rows in a filtered list](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)

In this example, the goal is to sum values in rows that are visible and ignore values in rows that are hidden. The range F7:F19 contains 13 values total, 4 of which are hidden by the filter applied to column C. This is a good job for the SUBTOTAL function , which can distinguish between visible and...

[![Excel formula: Count visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20visible%20rows%20in%20a%20filtered%20list.png "Excel formula: Count visible rows in a filtered list")](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)

### [Count visible rows in a filtered list](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)

In this example, the goal is to count rows that are visible and ignore rows that are hidden. This is a job for the SUBTOTAL function . SUBTOTAL can perform a variety of calculations like COUNT, SUM, MAX, MIN, and more. What makes SUBTOTAL interesting and useful is that it automatically ignores...

[![Excel formula: Count visible rows with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20visible%20rows%20with%20criteria.png "Excel formula: Count visible rows with criteria")](https://exceljet.net/formulas/count-visible-rows-with-criteria)

### [Count visible rows with criteria](https://exceljet.net/formulas/count-visible-rows-with-criteria)

In this example, the goal is to count visible rows where Region="West". Row 13 meets this criteria, but has been hidden. The SUBTOTAL function can easily generate sums and counts for visible rows. However, SUBTOTAL is not able to apply criteria like the COUNTIFS function without help. Conversely,...

SUBTOTAL function videos
------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20count%20items%20in%20a%20filtered%20list%20with%20the%20SUBTOTAL%20function_thumb.png)](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)

### [How to count items in a filtered list](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)

When you're working with filtered lists, you might want to know how many items are in the list and how many items are currently visible. In this video, we'll show you how to add a message at the top of a filtered list that displays this information. Here we have a list of properties. If we enable "...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20add%20a%20totals%20row%20to%20a%20Table-Thumb.png)](https://exceljet.net/videos/how-to-add-a-totals-row-to-a-table)

### [How to add a totals row to a Table](https://exceljet.net/videos/how-to-add-a-totals-row-to-a-table)

In this video, we'll look at how to add and configure a Total Row to an Excel Table. All Excel Tables come with a built-in Total Row feature. The total row allows you to easily show summary calculations below a table. You can use this total row to calculate counts, sums, min and max, averages, and...

Related functions
-----------------

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count visible rows in a filtered list](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)
    
*   [Count visible rows with criteria](https://exceljet.net/formulas/count-visible-rows-with-criteria)
    
*   [Sum visible rows in a filtered list](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
    

### Videos

*   [How to count items in a filtered list](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    
*   [How to add a totals row to a Table](https://exceljet.net/videos/how-to-add-a-totals-row-to-a-table)
    

### Functions

*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    

### Links

*   [Microsoft SUBTOTAL function documentation](https://support.office.com/en-us/article/subtotal-function-7b027003-f060-4ade-9040-e478765b9939)
    

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