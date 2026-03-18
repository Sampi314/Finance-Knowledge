# Filter to extract matching values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-to-extract-matching-values

---

[Skip to main content](https://exceljet.net/formulas/filter-to-extract-matching-values#main-content)

[](https://exceljet.net/formulas/filter-to-extract-matching-values#)

*   [Previous](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Next](https://exceljet.net/formulas/filter-to-remove-columns)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter to extract matching values
=================================

by Dave Bruns · Updated 30 Apr 2023

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6430/download?token=dqHfLXT0)
 (17.94 KB)

![Excel formula: Filter to extract matching values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20to%20extract%20matching%20values.png "Excel formula: Filter to extract matching values")

Summary
-------

To filter data to extract matching values in two lists, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [COUNTIF](https://exceljet.net/functions/countif-function)
 or [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in F5 is:

    =FILTER(list1,COUNTIF(list2,list1))
    

where **list1** (B5:B16) and **list2** (D5:D14) are [named ranges](https://exceljet.net/glossary/named-range)
. The result returned by FILTER includes only the values in **list1** that appear in **list2**.

_Note: FILTER is a new [dynamic array function in Excel 365](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
._

Generic formula
---------------

    =FILTER(list1,COUNTIF(list2,list1))

Explanation 
------------

This formula relies on the [FILTER function](https://exceljet.net/functions/filter-function)
 to retrieve data based on a logical test built with the COUNTIF function:

    =FILTER(list1,COUNTIF(list2,list1))
    

working from the inside out, the [COUNTIF function](https://exceljet.net/functions/countif-function)
 is used to create the actual filter:

    COUNTIF(list2,list1)
    

Notice we are using **list2** as the _range_ argument, and **list1** as the _criteria_ argument. In other words, we are asking COUNTIF to count all values in **list1** that appear in **list2.** Because we are giving COUNTIF multiple values for criteria, we get back an [array](https://exceljet.net/glossary/array)
 with multiple results:

    {1;1;0;1;0;1;0;0;1;0;1;1}
    

Note the array contains 12 counts, one for each value in **list1**. A zero value indicates a value in **list1** that _is not_ found in **list2**. Any other positive number indicates a value in **list1** that _is_ found in **list2**. This array is returned directly to the FILTER function as the _include_ argument:

    =FILTER(list1,{1;1;0;1;0;1;0;0;1;0;1;1})
    

The FILTER function uses the array as a filter. Any value in **list1** associated with a zero is removed, while any value associated with a positive number survives.

The result is an array of 7 matching values which [spill](https://exceljet.net/glossary/spill)
 into the range F5:F11. If data changes, FILTER will recalculate and return a new list of matching values based on the new data.

### Non-matching values

To extract non-matching values from **list1** (i.e. values in **list1** that don't appear in **list2**) you can add the [NOT function](https://exceljet.net/functions/not-function)
 to the formula like this:

    =FILTER(list1,NOT(COUNTIF(list2,list1)))
    

The NOT function effectively reverses the result from COUNTIF – any non-zero number becomes FALSE, and any zero value becomes TRUE. The result is a list of the values in **list1** that are not present in **list2**.

![FILTER to extract non-matching values with NOT](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/FILTER%20to%20extract%20non-matching%20values.png?itok=G1JgZJL9 "FILTER to extract non-matching values with NOT")

### With INDEX

It is possible to create a formula to extract matching values without the FILTER function, but the formula is more complex. One option is to use the INDEX function in a formula like this:

![Extract matching values with INDEX](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/Extract%20matching%20values%20with%20INDEX.png?itok=JRqLKq7E "Extract matching values with INDEX")

The formula in G5, copied down is:

    =IFERROR(INDEX(list1,SMALL(IF(COUNTIF(list2,list1),ROW(list1)-ROW(INDEX(list1,1,1))+1),ROWS($F$5:F5))),"")
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

The core of this formula is the [INDEX function](https://exceljet.net/functions/index-function)
, which receives **list1** as the _array_ argument. Most of the remaining formula simply calculates the row number to use for matching values. This expression generates a list of [relative row numbers](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
:

    ROW(list1)-ROW(INDEX(list1,1,1))+1
    

which returns an array of 12 numbers representing the rows in **list1**:

    {1;2;3;4;5;6;7;8;9;10;11;12}
    

These are filtered with the [IF function](https://exceljet.net/functions/if-function)
 and the same logic used above in FILTER, based on the COUNTIF function:

    COUNTIF(list2,list1) // find matching values
    

The resulting [array](https://exceljet.net/glossary/array)
 looks like this:

    {1;2;FALSE;4;FALSE;6;FALSE;FALSE;9;FALSE;11;12} // result from IF
    

This array is delivered directly to the [SMALL function](https://exceljet.net/functions/small-function)
, which is used to fetch the next matching row number as the formula is copied down the column. The k value for SMALL (think nth) is calculated with an [expanding range](https://exceljet.net/glossary/expanding-reference)
:

    ROWS($G$5:G5) // incrementing value for k
    

The [IFERROR function](https://exceljet.net/functions/iferror-function)
 is used to trap errors that occur when the formula is copied down and runs out of matching values. For another example of this idea, see [this formula](https://exceljet.net/formulas/get-nth-match-with-index-match)
.

Related formulas
----------------

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: List missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_missing_values.png "Excel formula: List missing values")](https://exceljet.net/formulas/list-missing-values)

### [List missing values](https://exceljet.net/formulas/list-missing-values)

In this example, the goal is to generate a list of people who were invited but did not attend an unspecified event. More specifically, we need to compare the names in B5:B16 against the names in D5:D12 and return the missing names. For convenience, list1 (B5:B16) and list2 (D5:D12) are named ranges...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [List missing values](https://exceljet.net/formulas/list-missing-values)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

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