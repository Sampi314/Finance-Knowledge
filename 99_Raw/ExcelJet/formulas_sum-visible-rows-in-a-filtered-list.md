# Sum visible rows in a filtered list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list

---

[Skip to main content](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list#main-content)

[](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list#)

*   [Previous](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    
*   [Next](https://exceljet.net/formulas/sumifs-with-horizontal-range)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum visible rows in a filtered list
===================================

by Dave Bruns · Updated 3 Jan 2023

Related functions 
------------------

[SUBTOTAL](https://exceljet.net/functions/subtotal-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

![Excel formula: Sum visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_visible_rows_in_a_filtered_list.png "Excel formula: Sum visible rows in a filtered list")

Summary
-------

To sum values in _visible rows_ in a filtered list (i.e. exclude rows that are "filtered out"), you can use the [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
.  In the example shown, the formula in F4 is:

    =SUBTOTAL(9,F7:F19)

The result is $21.17, the sum of the 9 visible values in column F. Note that the range F7:F19 contains 13 values total, 4 of which are hidden by the filter in column C.

Generic formula
---------------

    =SUBTOTAL(9,range)

Explanation 
------------

In this example, the goal is to sum values in rows that are visible and ignore values in rows that are hidden. The range F7:F19 contains 13 values total, 4 of which are hidden by the filter applied to column C. This is a good job for the [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
, which can distinguish between visible and hidden cells when it applies various calculations. Another way to solve this problem is with the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
. Both formulas are explained below.

### SUBTOTAL function

The SUBTOTAL function can perform a variety of calculations like COUNT, SUM, MAX, MIN, etc. on a set of data, returning an _aggregated_ result. What makes SUBTOTAL useful in this case is that it will _automatically_ ignore rows that are hidden in a filtered list or table and can _optionally_ ignore rows that have been [manually hidden](https://exceljet.net/shortcuts/hide-rows)
. The generic syntax for SUBTOTAL looks like this:

    =SUBTOTAL(function_num, reference)

The first [argument](https://exceljet.net/glossary/function-argument)
, _function\_num_, specifies the type of calculation to perform. _Reference_ holds the data that should be used in the operation. In the worksheet shown above, we use SUBTOTAL like this:

    =SUBTOTAL(9,F7:F19) // sum and ignore hidden

For _function\_num_, we provide the number 9, which corresponds to the "SUM" operation. For _reference_, we use the full range for the amounts in column F, which is F7:F19. SUBTOTAL automatically ignores the 4 rows hidden by the filter applied to column C, and returns $21.17, the sum of the 9 visible amounts in column F.

Note that SUBTOTAL _always_ ignores values in rows that are hidden with a filter. To ignore rows that are hidden manually (i.e. right-click > Hide), use 109 for function\_num instead of 9:

    =SUBTOTAL(109,B7:B16) // sum and ignore manually hidden
    

To be clear, SUBTOTAL will _always ignore_ values in rows hidden by a filter in a table, regardless of _function\_num_. Using 109 instead of 9 simply changes the behavior to also ignore manually hidden rows. SUBTOTAL function can perform many other calculations as well. See a complete list [on this page](https://exceljet.net/functions/subtotal-function)
.

### AGGREGATE function

The [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
 is like an ungraded version of SUBTOTAL. Like SUBTOTAL, AGGREGATE can run many aggregate calculations, optionally ignoring hidden rows. However, AGGREGATE provides more calculation options, and more options for ignoring things. The formulas below show how AGGREGATE can be used like the SUBTOTAL function to solve this problem:

    =AGGREGATE(9,5,F7:F19) // sum, ignore hidden
    =AGGREGATE(9,7,F7:F19) // sum, ignore hidden and errors

The second formula shows how to configure AGGREGATE to ignore hidden rows and errors in the data at the same time. AGGREGATE provides a total of 19 different calculations and many options for ignoring things. For details, see our [AGGREGATE function page](https://exceljet.net/functions/aggregate-function)
.

_Note: One subtle difference between AGGREGATE and SUBTOTAL is that default behavior for hidden rows is reversed. While SUBTOTAL will always ignore values in rows hidden by a filter, and needs a different function number to ignore manually hidden rows, AGGREGATE will always ignore manually hidden rows and needs a specific option to ignore rows hidden by a filter._ 

Related formulas
----------------

[![Excel formula: Count visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20visible%20rows%20in%20a%20filtered%20list.png "Excel formula: Count visible rows in a filtered list")](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)

### [Count visible rows in a filtered list](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list)

In this example, the goal is to count rows that are visible and ignore rows that are hidden. This is a job for the SUBTOTAL function . SUBTOTAL can perform a variety of calculations like COUNT, SUM, MAX, MIN, and more. What makes SUBTOTAL interesting and useful is that it automatically ignores...

[![Excel formula: Count visible rows with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20visible%20rows%20with%20criteria.png "Excel formula: Count visible rows with criteria")](https://exceljet.net/formulas/count-visible-rows-with-criteria)

### [Count visible rows with criteria](https://exceljet.net/formulas/count-visible-rows-with-criteria)

In this example, the goal is to count visible rows where Region="West". Row 13 meets this criteria, but has been hidden. The SUBTOTAL function can easily generate sums and counts for visible rows. However, SUBTOTAL is not able to apply criteria like the COUNTIFS function without help. Conversely,...

Related functions
-----------------

[![Excel SUBTOTAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20subtotal%20function.png "Excel SUBTOTAL function")](https://exceljet.net/functions/subtotal-function)

### [SUBTOTAL Function](https://exceljet.net/functions/subtotal-function)

The Excel SUBTOTAL function is designed to run a given calculation on a range of cells while ignoring cells that should not be included. SUBTOTAL can return a SUM, AVERAGE, COUNT, MAX, and others (see complete list below), and SUBTOTAL function can either include or exclude values in hidden...

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
    

### Functions

*   [SUBTOTAL Function](https://exceljet.net/functions/subtotal-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    

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