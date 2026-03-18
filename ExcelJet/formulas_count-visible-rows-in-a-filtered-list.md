# Count visible rows in a filtered list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list

---

[Skip to main content](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list#main-content)

[](https://exceljet.net/formulas/count-visible-rows-in-a-filtered-list#)

*   [Previous](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
    
*   [Next](https://exceljet.net/formulas/count-visible-rows-with-criteria)
    

[Count](https://exceljet.net/formulas#Count)

Count visible rows in a filtered list
=====================================

by Dave Bruns · Updated 15 Jul 2022

Related functions 
------------------

[SUBTOTAL](https://exceljet.net/functions/subtotal-function)

![Excel formula: Count visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20visible%20rows%20in%20a%20filtered%20list.png "Excel formula: Count visible rows in a filtered list")

Summary
-------

To count the number of visible rows in a filtered list, you can use the [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
. In the example shown, the formula in cell C4 is:

    =SUBTOTAL(3,B7:B16)
    

The result is 7, since there are 7 rows visible out of 10 rows total.

Generic formula
---------------

    =SUBTOTAL(3,range)

Explanation 
------------

In this example, the goal is to count rows that are visible and ignore rows that are hidden. This is a job for the [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
. SUBTOTAL can perform a variety of calculations like COUNT, SUM, MAX, MIN, and more. What makes SUBTOTAL interesting and useful is that it _automatically ignores items that are not visible in a filtered list or table_. This makes it ideal for running calculations on the rows that _are visible_ in filtered data.

### Count with SUBTOTAL

Following the example in the worksheet above, to count the number of non-blank rows visible when a filter is active, use a formula like this:

    =SUBTOTAL(3,B7:B16)
    

The first argument, _function\_num_, specifies count as the operation to be performed. SUBTOTAL ignores the 3 rows hidden by the filter and returns 7 as a result, since there are 7 rows visible.

Note that SUBTOTAL _always_ ignores values in cells that are hidden with a filter. Values in rows that have been "filtered out" are never included, regardless of _function\_num_. If you are hiding rows manually (i.e. right-click > Hide), and not using [filter controls](https://exceljet.net/shortcuts/toggle-autofilter)
 , use this version of the formula instead:

    =SUBTOTAL(103,B7:B16)
    

With the _function\_num_ set to 103, SUBTOTAL still performs a count, but this time it will ignore rows that are manually hidden, as well as those hidden with a filter. To be clear, values in rows that have been hidden with a filter are _never_ included, regardless of _function\_num_.

_The SUBTOTAL function can perform many other calculations. To see a list of all the calculations SUBTOTAL can perform, [see this page](https://exceljet.net/functions/subtotal-function)
._

Related formulas
----------------

[![Excel formula: Sum visible rows in a filtered list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_visible_rows_in_a_filtered_list.png "Excel formula: Sum visible rows in a filtered list")](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)

### [Sum visible rows in a filtered list](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)

In this example, the goal is to sum values in rows that are visible and ignore values in rows that are hidden. The range F7:F19 contains 13 values total, 4 of which are hidden by the filter applied to column C. This is a good job for the SUBTOTAL function , which can distinguish between visible and...

[![Excel formula: Count visible rows with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20visible%20rows%20with%20criteria.png "Excel formula: Count visible rows with criteria")](https://exceljet.net/formulas/count-visible-rows-with-criteria)

### [Count visible rows with criteria](https://exceljet.net/formulas/count-visible-rows-with-criteria)

In this example, the goal is to count visible rows where Region="West". Row 13 meets this criteria, but has been hidden. The SUBTOTAL function can easily generate sums and counts for visible rows. However, SUBTOTAL is not able to apply criteria like the COUNTIFS function without help. Conversely,...

Related functions
-----------------

[![Excel SUBTOTAL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20subtotal%20function.png "Excel SUBTOTAL function")](https://exceljet.net/functions/subtotal-function)

### [SUBTOTAL Function](https://exceljet.net/functions/subtotal-function)

The Excel SUBTOTAL function is designed to run a given calculation on a range of cells while ignoring cells that should not be included. SUBTOTAL can return a SUM, AVERAGE, COUNT, MAX, and others (see complete list below), and SUBTOTAL function can either include or exclude values in hidden...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20count%20items%20in%20a%20filtered%20list%20with%20the%20SUBTOTAL%20function_thumb.png)](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)

### [How to count items in a filtered list](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)

When you're working with filtered lists, you might want to know how many items are in the list and how many items are currently visible. In this video, we'll show you how to add a message at the top of a filtered list that displays this information. Here we have a list of properties. If we enable "...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum visible rows in a filtered list](https://exceljet.net/formulas/sum-visible-rows-in-a-filtered-list)
    
*   [Count visible rows with criteria](https://exceljet.net/formulas/count-visible-rows-with-criteria)
    

### Functions

*   [SUBTOTAL Function](https://exceljet.net/functions/subtotal-function)
    

### Videos

*   [How to count items in a filtered list](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)
    

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