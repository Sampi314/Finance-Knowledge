# Multiple matches into separate rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/multiple-matches-into-separate-rows

---

[Skip to main content](https://exceljet.net/formulas/multiple-matches-into-separate-rows#main-content)

[](https://exceljet.net/formulas/multiple-matches-into-separate-rows#)

*   [Previous](https://exceljet.net/formulas/multiple-matches-into-separate-columns)
    
*   [Next](https://exceljet.net/formulas/nearest-location-with-xmatch)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Multiple matches into separate rows
===================================

by Dave Bruns · Updated 2 May 2025

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[SORT](https://exceljet.net/functions/sort-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[INDEX](https://exceljet.net/functions/index-function)

[SMALL](https://exceljet.net/functions/small-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[ROW](https://exceljet.net/functions/row-function)

[ROWS](https://exceljet.net/functions/rows-function)

![Excel formula: Multiple matches into separate rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/multiple_matches_into_separate_rows.png "Excel formula: Multiple matches into separate rows")

Summary
-------

To extract multiple matches into separate rows based on a common value, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
. In the worksheet shown, the formula in cell E5 is:

    =FILTER(name,group=E4)

Where **name** (B5:B16) and **group** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. The group names in E4:H4 are also created with a formula, as explained below. The explanation below reviews two approaches (1) a modern approach based on the FILTER function and (2) a legacy approach based on INDEX and SMALL for older versions of Excel without the FILTER function.

Generic formula
---------------

    =FILTER(range1,range2=A1)

Explanation 
------------

In this example, the goal is to get all names in a given group into separate rows grouped by column, as seen in the worksheet above. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns where each column holds the names that belong to a group. The article below explains two options: (1) a modern approach based on the FILTER function and (2) a legacy approach based on INDEX and SMALL for older versions of Excel without the FILTER function.

### Modern approach

Several new functions in the current version of Excel make this task easier. First, to build a list of groups in alphabetical order, we use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 with the [SORT function](https://exceljet.net/functions/sort-function)
 in cell E4 like this

    =TRANSPOSE(SORT(UNIQUE(group))) // returns {"A","B","C","D"}

The [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 converts the vertical output from SORT into a horizontal array. This formula [spills](https://exceljet.net/glossary/spill)
 the four unique group names into the range E4:H4. With the groups in place, we now have what we need to retrieve the names in each group. For this step, we use a formula like this in cell E5:

    =FILTER(name,group=E4)

The [FILTER function](https://exceljet.net/functions/filter-function)
 retrieves the names in B5:B16 where the group = "A" (the value in E4). As the formula is copied across, the reference to E5 is [relative](https://exceljet.net/glossary/relative-reference)
 and changes at each new row. The result is that all names in each group are together in the same column.

_Note: It would be nice to use a reference to the_ [_spill range_](https://exceljet.net/glossary/spill-range)
 _in E4:H8 (E4#) inside the FILTER function. However, Excel formulas won't currently return an_ [_array-of-arrays,_](https://exceljet.net/glossary/array-of-arrays)
 _so this doesn't work._

### Legacy solution

In [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that don't offer the FILTER function, you can use a more complex array formula based on the [INDEX function](https://exceljet.net/functions/index-function)
 and the [SMALL function](https://exceljet.net/functions/small-function)
 to get multiple matches into separate columns. Enter the formula below in cell E5, then drag it down and across to fill in the other cells in the range E5:H7:

    =IFERROR(INDEX(name,SMALL(IF(group=E$4,ROW(name)-MIN(ROW(name))+1),ROWS($E$5:E5))),"")

_Note: This is an_ [_array formula_](https://exceljet.net/glossary/array-formula)
 _and must be entered with Control + Shift + Enter in older versions of Excel._

![INDEX and SMALL array formula for legacy Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/multiple_matches_into_separate_rows_legacy.png "INDEX and SMALL array formula for legacy Excel")

The gist of this formula is this: we are using the [SMALL function](https://exceljet.net/functions/small-function)
 to generate a row number corresponding to an "nth match" for each name in a group. Once we have the row number, we pass it into the [INDEX function](https://exceljet.net/functions/index-function)
, which returns the value at that row. To make this work, we need to "pre-filter" the array of values given to SMALL to exclude other groups. We do this with the IF function in this part of the formula:

    IF(group=E$4,ROW(name)-MIN(ROW(name))+1)
    

At a high level, this snippet gets the row numbers for all names that belong to a given group. It does this by testing the group in cell E4 against all values in the named range **group**. When the result is TRUE, the IF function returns the row number (see next step). When the result is FALSE, the IF function returns FALSE. The row numbers are created with the formula below:

    ROW(name)-MIN(ROW(name))+1
    

[See this page for details](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
. The final result is an array like this:

    {1;FALSE;FALSE;FALSE;5;FALSE;FALSE;FALSE;9;FALSE;FALSE;FALSE}

As you can see, the only row numbers that survive the filtering are those that correspond to the group in cell E4. This array goes into SMALL as the _array_ argument. The value for _k_ is created with an [expanding range](https://exceljet.net/glossary/expanding-reference)
 and the [ROWS function](https://exceljet.net/functions/rows-function)
:

    ROWS($E$5:E5) // value for k

As the formula is copied down the table, the range expands, causing _k_ to increment. The result is that the SMALL function returns the row number for each name in a given group. This number is supplied to the INDEX function as _row\_num_, with the named range **name** as the _array_ argument, and INDEX returns the name associated with each row number.

### Handling errors

When ROWS returns a value for k that does not exist, SMALL throws a #NUM error. This happens after all names for a given group have been extracted. To suppress this error, we wrap the formula in the [IFERROR function](https://exceljet.net/functions/iferror-function)
 and return an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

Related formulas
----------------

[![Excel formula: Multiple matches into separate columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_columns.png "Excel formula: Multiple matches into separate columns")](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

### [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

In this example, the goal is to get all names in a given group into the same row, in separate columns, as seen in the worksheet. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns using common values, which in this case are the group...

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

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)
    
*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

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