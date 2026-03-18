# List missing values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/list-missing-values

---

[Skip to main content](https://exceljet.net/formulas/list-missing-values#main-content)

[](https://exceljet.net/formulas/list-missing-values#)

*   [Previous](https://exceljet.net/formulas/left-lookup-with-vlookup)
    
*   [Next](https://exceljet.net/formulas/look-up-and-return-to-single-cell)
    

[Lookup](https://exceljet.net/formulas#Lookup)

List missing values
===================

by Dave Bruns · Updated 2 May 2025

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: List missing values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/list_missing_values.png "Excel formula: List missing values")

Summary
-------

To compare two lists and pull missing values into a new list, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
. In the example shown, the formula in cell F5 is:

    =FILTER(list1,NOT(COUNTIF(list2,list1)))
    

where **list1** (B5:B16) and **list2** (D5:D12) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is the names in B5:B16 that do not appear in D5:D12.

Generic formula
---------------

    =FILTER(list1,NOT(COUNTIF(list2,list1)))

Explanation 
------------

In this example, the goal is to generate a list of people who were invited but did not attend an unspecified event. More specifically, we need to compare the names in B5:B16 against the names in D5:D12 and return the missing names. For convenience, **list1** (B5:B16) and **list2** (D5:D12) are [named ranges](https://exceljet.net/glossary/named-range)
. The easiest way to solve this problem in Excel is with the FILTER function and the COUNTIF function, as explained below.

### FILTER function

This formula uses the [FILTER function](https://exceljet.net/functions/filter-function)
 to retrieve data based on a logical test built with the COUNTIF function. In the worksheet shown, the formula in cell F5 is:

    =FILTER(list1,NOT(COUNTIF(list2,list1)))

Working from the inside out, the [COUNTIF function](https://exceljet.net/functions/countif-function)
 is used to create the actual filter:

    COUNTIF(list2,list1)
    

Notice we are using **list2** as the _range_ argument, and **list1** as the _criteria_ argument. In other words, we ask COUNTIF to count all values in **list1** that appear in **list2.** Because we are giving COUNTIF multiple values for the criteria, we get back an [array](https://exceljet.net/glossary/array)
 with multiple results:

    {1;1;0;1;0;1;0;1;1;0;1;1}

Note that the array contains 12 counts, one for each value in **list1**. Also, notice that there are 4 zeros in the array. A zero value indicates a name in **list1** that _was not_ found in **list2**. The 1's in the array indicate a name in **list1** that _was_ found in **list2**. Because we want to list names that _did not attend_, we deliver the result from COUNTIF to the [NOT function](https://exceljet.net/functions/not-function)
:

    NOT({1;1;0;1;0;1;0;1;1;0;1;1})

The NOT function effectively reverses the result from COUNTIF. Any non-zero number becomes FALSE, and any zero value becomes TRUE. The result from NOT is an array like this:

    {FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}

Notice there are now 4 TRUE values in the array. This is what we need to report the missing names. The array is returned directly to the FILTER function as the _include_ argument, and the FILTER function uses the array as a filter. The result is an array of 4 missing names that land in cell F5 and [spill](https://exceljet.net/glossary/spill)
 into the range F5:F8. If any data changes, FILTER will recalculate and return an updated list.

Related formulas
----------------

[![Excel formula: Highlight missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20that%20don%27t%20exist.png "Excel formula: Highlight missing values")](https://exceljet.net/formulas/highlight-missing-values)

### [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)

This formula is evaluated for each of the 10 cells in A1:D10. A1 will change to the address of the cell being evaluated, while C1:C10 is entered as an absolute address, so it won't change at all. The key to this formula is the =0 at the end, which "flips" the logic of the formula. For each value in...

[![Excel formula: Find missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_missing_values.png "Excel formula: Find missing values")](https://exceljet.net/formulas/find-missing-values)

### [Find missing values](https://exceljet.net/formulas/find-missing-values)

The goal is to identify invoice numbers in range D5:D11 that are missing in range B5:B16 (named list ). Two good ways to solve this problem in Excel are the COUNTIF function and the MATCH function . Both approaches are explained below. COUNTIF function COUNTIF counts cells in a range that meet a...

[![Excel formula: Count missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_missing_values.png "Excel formula: Count missing values")](https://exceljet.net/formulas/count-missing-values)

### [Count missing values](https://exceljet.net/formulas/count-missing-values)

In this example, the goal is to count the number of names in the range B5:B16 (Invited) that are missing from the range D5:D12 (Attended). This problem can be solved with the COUNTIF function or the MATCH function, as explained below. Both approaches work well. The advantage of the MATCH approach...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20find%20missing%20values%20with%20COUNTIF-Thumb.png)](https://exceljet.net/videos/how-to-find-missing-values-with-countif)

### [How to find missing values with COUNTIF](https://exceljet.net/videos/how-to-find-missing-values-with-countif)

In this video we'll take a look at how to use the COUNTIF function to solve a common problem: how to find values in one list that appear in another list. Or, how to find values in a list that don't appear in another list. Let's take a look. In this worksheet, on the left, I have a list of 20 names...

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

*   [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)
    
*   [Find missing values](https://exceljet.net/formulas/find-missing-values)
    
*   [Count missing values](https://exceljet.net/formulas/count-missing-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

### Videos

*   [How to find missing values with COUNTIF](https://exceljet.net/videos/how-to-find-missing-values-with-countif)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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