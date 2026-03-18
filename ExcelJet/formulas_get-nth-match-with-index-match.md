# Get nth match with INDEX / MATCH - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-nth-match-with-index-match

---

[Skip to main content](https://exceljet.net/formulas/get-nth-match-with-index-match#main-content)

[](https://exceljet.net/formulas/get-nth-match-with-index-match#)

*   [Previous](https://exceljet.net/formulas/get-nth-match)
    
*   [Next](https://exceljet.net/formulas/get-nth-match-with-vlookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get nth match with INDEX / MATCH
================================

by Dave Bruns · Updated 30 Oct 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[SMALL](https://exceljet.net/functions/small-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")

Summary
-------

To get the nth matching record in a set of data with an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
, you can use a formula like this in cell H7:

    =INDEX(data[Name],SMALL(IF(data[Product]=$H$4,ROW(data)-MIN(ROW(data))+1),G7))

Where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:E16. When H4 contains "A", the formula will return the 1st, 2nd, and 3rd names that correspond with product "A" in the table. A similar formula can be used to return the Amount in cell I7. See below for details. Note this is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with control + shift + enter in Excel 2019 and earlier.

_Note: The purpose of this example is to explain how to get the nth match in Excel 2019 and older with an INDEX and MATCH formula. In the current version of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
 is a much better way to get multiple matching records._

Generic formula
---------------

    =INDEX(rng,SMALL(IF(rng=A1,ROW(rng)-MIN(ROW(rng))+1),n))

Explanation 
------------

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8 should return 'Juan', since this is the second name associated with product "A". The product in H4 is an input that can be changed at any time. All data exists in an Excel Table named **data**.

### Basic INDEX and MATCH

Before we look at the formula used in the worksheet, we should review why we can't use a "normal" INDEX and MATCH formula to solve this problem. Normally, the INDEX and MATCH functions are used to find the position of a value in a table and return a corresponding value in the same position from a different column. However, this method only works for the first match. For example, in the screen below, these the INDEX and MATCH formulas in H7 and I7 are as follows:

    =INDEX(data[Name],MATCH(H4,data[Product],0)) // returns "John"
    =INDEX(data[Amount],MATCH(H4,data[Product],0)) // returns 100

In these formulas, the MATCH function is configured to match the value in H4 ("A"), in the Product column. In both formulas, MATCH returns 1 because the product is "A". These formulas work perfectly, but the problem is that we have no way to ask MATCH to find the 2nd match, the 3rd match, etc.

![INDEX and MATCH gets first match only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/INDEX_and_MATCH_gets_first_match_only.png "INDEX and MATCH gets first match only")

As mentioned, this is a standard application of INDEX and MATCH. For a complete overview, see: [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### INDEX and SMALL + IF

One workaround to the INDEX and MATCH limitation explained above is to use INDEX with the SMALL and IF instead of MATCH. At the core, this approach uses INDEX to get the name at a specific row number like this:

    =INDEX(data[Name],row_num)

The challenge is how to calculate the row number for each nth match since MATCH will only find the _first_ match. One workaround is to generate a set of row numbers for the entire table, then use the IF function to "filter" the row numbers based on the product specified in cell H4. Then we can give this filtered list to the SMALL function, which is designed to get the "nth smallest" value. That is the approach seen in the worksheet as shown, where the formula in H7 is as follows:

    =INDEX(data[Name],SMALL(IF(data[Product]=$H$4,ROW(data)-MIN(ROW(data))+1),G7))

_Note this is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with control + shift + enter in Excel 2019 and earlier._

All of the hard work in this formula is in determining a row number for INDEX, which is done here:

    SMALL(IF(data[Product]=$H$4,ROW(data)-MIN(ROW(data))+1),G7)

This may look complicated, but the approach is pretty straightforward. We create row numbers for the data, filter the numbers with an appropriate logical test, then retrieve the nth matching row number. Working from the inside out, the code below generates a set of relative row numbers for the entire table:

    ROW(data)-MIN(ROW(data))+1

Since there are 12 rows in the table, the result is an array like this:

    {1;2;3;4;5;6;7;8;9;10;11;12}

For more details on how this works, [see this page](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
. Simplifying the formula, we now have:

    SMALL(IF(data[Product]=$H$4,{1;2;3;4;5;6;7;8;9;10;11;12}),G7)

Next, the [IF function](https://exceljet.net/videos/the-if-function)
 applies a logical test to filter on numbers where the product is "A" in H4:

    IF(data[Product]=$H$4,{1;2;3;4;5;6;7;8;9;10;11;12})

Because there are 12 rows in the table, the result is an array like this:

    {1;FALSE;3;FALSE;5;FALSE;FALSE;FALSE;9;FALSE;11;FALSE}

Notice the only numbers to survive the filtering are the rows associated with product "A". The other row numbers have been replaced by FALSE. Next, the SMALL function is used to return the nth smallest value:

    SMALL({1;FALSE;3;FALSE;5;FALSE;FALSE;FALSE;9;FALSE;11;FALSE},G7)

SMALL automatically ignores the FALSE values. With 1 in cell G7, SMALL returns the smallest value, which is 1. This is returned directly to the INDEX function as _row\_num_. Back in the original formula, we now have:

    =INDEX(data[Name],1) // returns "John"

The INDEX function then returns "John" in cell H7. In cell H8, the value in G8 is 2, and SMALL returns the second smallest row number, which is 3:

    =INDEX(data[Name],3) // returns "Juan"

As the formula is copied down, the value for n increases in column G causing the SMALL function to retrieve the next matching row number. At each new row, the formula returns the next nth match.

### Retrieving Amount

The formula to retrieve the associated Amount is almost exactly the same as the formula above:

    =INDEX(data[Amount],SMALL(IF(data[Product]=$H$4,ROW(data)-MIN(ROW(data))+1),G7))

The only difference is the value for the _array_ provided to INDEX, which is **data\[Amount\]** instead of **data\[Name\]**.

### Handling errors

Once there are no more matches for a given value of n, the SMALL function will return a #NUM error. You can handle this error with the [IFERROR function](https://exceljet.net/functions/iferror-function)
, or by adding logic to count matches and abort processing once the number in column H is greater than the match count. The [example here](https://exceljet.net/formulas/index-and-match-all-matches)
 shows one approach.

### Multiple criteria

To add multiple criteria, you use [boolean logic](https://exceljet.net/glossary/boolean-logic)
, as [explained in this example](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
.

Related formulas
----------------

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: INDEX and MATCH all matches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20data%20with%20helper%20column4.png "Excel formula: INDEX and MATCH all matches")](https://exceljet.net/formulas/index-and-match-all-matches)

### [INDEX and MATCH all matches](https://exceljet.net/formulas/index-and-match-all-matches)

Note: in more recent versions of Excel, the FILTER function is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for legacy versions of Excel that do not provide the FILTER function. By default, lookup formulas in Excel like VLOOKUP and INDEX + MATCH will find...

[![Excel formula: INDEX and MATCH all partial matches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_all_partial_matches.png "Excel formula: INDEX and MATCH all partial matches")](https://exceljet.net/formulas/index-and-match-all-partial-matches)

### [INDEX and MATCH all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)

Note: in the current version of Excel, the FILTER function is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for legacy versions of Excel that do not provide the FILTER function. The core of this formula is the INDEX function, with AGGREGATE used to figure...

[![Excel formula: Get nth match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match.png "Excel formula: Get nth match")](https://exceljet.net/formulas/get-nth-match)

### [Get nth match](https://exceljet.net/formulas/get-nth-match)

The goal is to retrieve the nth matching record in a set of data, after filtering on a specific product. In the worksheet shown, the product in H4 and the value for n in H5 are inputs that can be changed at any time. For instance, if the product in H4 is "A" and the value in H5 is 3, the formula...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [INDEX and MATCH all matches](https://exceljet.net/formulas/index-and-match-all-matches)
    
*   [INDEX and MATCH all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)
    
*   [Get nth match](https://exceljet.net/formulas/get-nth-match)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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