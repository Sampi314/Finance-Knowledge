# Multiple matches into separate columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/multiple-matches-into-separate-columns

---

[Skip to main content](https://exceljet.net/formulas/multiple-matches-into-separate-columns#main-content)

[](https://exceljet.net/formulas/multiple-matches-into-separate-columns#)

*   [Previous](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list)
    
*   [Next](https://exceljet.net/formulas/multiple-matches-into-separate-rows)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Multiple matches into separate columns
======================================

by Dave Bruns · Updated 2 May 2025

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[SORT](https://exceljet.net/functions/sort-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[INDEX](https://exceljet.net/functions/index-function)

[SMALL](https://exceljet.net/functions/small-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[COLUMN](https://exceljet.net/functions/column-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

![Excel formula: Multiple matches into separate columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/multiple_matches_into_separate_columns.png "Excel formula: Multiple matches into separate columns")

Summary
-------

To extract multiple matches into separate columns based on a common value, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
. In the worksheet shown, the formula in cell F5 is:

    =TRANSPOSE(FILTER(name,group=E5))

Where **name** (B5:B16) and **group** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. The group names in E5:E8 and the name headings in F4:H4 are also created with formulas, as explained below. The explanation below covers two approaches (1) a modern approach based on the FILTER function and (2) a legacy approach based on INDEX and SMALL for older versions of Excel without the FILTER function.

Generic formula
---------------

    =TRANSPOSE(FILTER(range1,range2=A1))

Explanation 
------------

In this example, the goal is to get all names in a given group into the same row, in separate columns, as seen in the worksheet. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns using common values, which in this case are the group names. The explanation below includes two options: (1) a modern approach based on the FILTER function and (2) a legacy approach based on INDEX and SMALL for older versions of Excel without the FILTER function.

### Modern approach

Several new functions in the current version of Excel make this task easier. First, to build a list of groups in alphabetical order, we use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 with the [SORT function](https://exceljet.net/functions/sort-function)
 in cell E5 like this

    =SORT(UNIQUE(group)) // returns {"A";"B";"C";"D"}

This formula [spills](https://exceljet.net/glossary/spill)
 the four unique group names into the range E5:E8. To generate the headings that appear in the range F4:H4, we use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 with MAX and COUNTIF like this:

    ="Name "&SEQUENCE(1,MAX(COUNTIF(group,group)))

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 returns an array of counts for each group, and the [MAX function](https://exceljet.net/functions/max-function)
 returns the maximum count, which is 3. We use COUNTIF and MAX like this so that the header will automatically expand as needed when a group contains more names. The result is delivered to the SEQUENCE function as the _columns_ argument, and SEQUENCE returns the array {1,2,3}:

    SEQUENCE(1,3) // returns {1,2,3}

The result from SEQUENCE is then [concatenated](https://exceljet.net/articles/how-to-concatenate-in-excel)
 to the text string "Name ". The result is an array like this:

    {"Name 1","Name 2","Name 3"}

We now have what we need to retrieve the names in each group. For this step, we use a formula like this in cell F5:

    =TRANSPOSE(FILTER(name,group=E5))

Working from the inside out, the [FILTER function](https://exceljet.net/functions/filter-function)
 retrieves the names in B5:B16 where the group = "A" (the value in E5), and [TRANSPOSE](https://exceljet.net/functions/transpose-function)
 converts the vertical array from FILTER into a [horizontal array](https://exceljet.net/glossary/array)
 that spills into the range F5:H5. As the formula is copied down column F, the reference to E5 is [relative](https://exceljet.net/glossary/relative-reference)
 and changes at each new row. As a final result, we have all names in each group together in the same row.

_Note: It would be nice to use a reference to the_ [_spill range_](https://exceljet.net/glossary/spill-range)
 _in E5:E8 (E5#) inside the FILTER function. However, Excel formulas won't currently return an_ [_array-of-arrays_](https://exceljet.net/glossary/array-of-arrays)
 _so this won't work._

### Legacy solution

In [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that don't offer the FILTER function, you can use a more complex array formula based on the [INDEX function](https://exceljet.net/functions/index-function)
 and the [SMALL function](https://exceljet.net/functions/small-function)
 to get multiple matches into separate columns. Enter the formula below in cell F5, then drag it down and across to fill in the other cells in the range F5:H8:

    {=IFERROR(INDEX(name,SMALL(IF(group=$E5,ROW(name)-MIN(ROW(name))+1),COLUMNS($E$5:E5))),"")}

_Note: This is an_ [_array formula_](https://exceljet.net/glossary/array-formula)
 _and must be entered with Control + Shift + Enter in older versions of Excel._

![INDEX and SMALL array formula for legacy Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/multiple_matches_into_separate_columns_legacy.png "INDEX and SMALL array formula for legacy Excel")

The gist of this formula is this: we are using the [SMALL function](https://exceljet.net/functions/small-function)
 to generate a row number corresponding to an "nth match" for each name in a group. Once we have the row number, we simply pass it into the [INDEX function](https://exceljet.net/functions/index-function)
, which returns the value at that row. The trick is that SMALL is working with an array that is already filtered by group. The filtering is done with the IF function in this part of the formula:

    IF(group=$E5,ROW(name)-MIN(ROW(name))+1)
    

At a high level, this code gets the row numbers of all names that belong to a given group. It does this by testing the group in cell E5 against all values in the named range **group**. When the result is TRUE, the IF function returns the row number. The relative row numbers for all values in the data are created with the formula below:

    ROW(name)-MIN(ROW(name))+1
    

[See this page for details](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
. The final result is an array that contains numbers where there is a match, and FALSE where not:

    {1;FALSE;FALSE;FALSE;5;FALSE;FALSE;FALSE;9;FALSE;FALSE;FALSE}

As you can see, the only row numbers that survive the trip are those that correspond to the group in cell E5. This array goes into SMALL as the _array_ argument. The value for _k_ is created with an [expanding range](https://exceljet.net/glossary/expanding-reference)
 and the [COLUMNS function](https://exceljet.net/functions/columns-function)
:

    COLUMNS($E$5:E5) // value for k

As the formula is copied across the table, the range expands, causing _k_ to increment. The result is that the SMALL function returns the row number for each name in a given group. This number is supplied to the INDEX function as _row\_num_, with the named range **name** as the array. Finally, INDEX returns the name associated with each row number.

### Handling errors

When COLUMNS returns a value for k that does not exist, SMALL throws a #NUM error. This happens after all names for a given group have been extracted. To suppress this error, we wrap the formula in the [IFERROR function](https://exceljet.net/functions/iferror-function)
 and return an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

Related formulas
----------------

[![Excel formula: Multiple matches into separate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_rows.png "Excel formula: Multiple matches into separate rows")](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

### [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)

In this example, the goal is to get all names in a given group into separate rows grouped by column, as seen in the worksheet above. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns where each column holds the names that belong to a...

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: Multiple matches in comma separated list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple%20matches%20in%20comma%20separated%20result2.png "Excel formula: Multiple matches in comma separated list")](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list)

### [Multiple matches in comma separated list](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list)

The core of this formula is the IF function, which "filters" the names in the table by color like this: IF(group=E5,name,"")) The logical test checks each cell in the named range "group" for the color value in E5 (red in this case). The result is an array like this: {FALSE;FALSE;TRUE;TRUE;FALSE;...

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

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)
    
*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [Multiple matches in comma separated list](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    

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