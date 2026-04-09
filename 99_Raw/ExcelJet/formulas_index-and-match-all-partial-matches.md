# INDEX and MATCH all partial matches - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/index-and-match-all-partial-matches

---

[Skip to main content](https://exceljet.net/formulas/index-and-match-all-partial-matches#main-content)

[](https://exceljet.net/formulas/index-and-match-all-partial-matches#)

*   [Previous](https://exceljet.net/formulas/index-and-match-all-matches)
    
*   [Next](https://exceljet.net/formulas/index-and-match-approximate-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

INDEX and MATCH all partial matches
===================================

by Dave Bruns · Updated 5 Apr 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel formula: INDEX and MATCH all partial matches](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/INDEX_and_MATCH_all_partial_matches.png "Excel formula: INDEX and MATCH all partial matches")

Summary
-------

    =FILTER(data,ISNUMBER(SEARCH(search,data)))

To extract all matches based on a partial match, you can use a formula based on the [INDEX](https://exceljet.net/functions/index-function)
 and [AGGREGATE](https://exceljet.net/functions/aggregate-function)
 functions, with support from [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
. In the example shown, the formula in G5 is:

    =IF(F5>ct,"",INDEX(data,AGGREGATE(15,6,(ROW(data)-ROW($B$5)+1)/ISNUMBER(SEARCH(search,data)),F5)))
    

where **search** (D5), **CT** (D8) and **data** (B5:B55) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: in the current version of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
 is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for [legacy versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not provide the FILTER function._

Generic formula
---------------

    =IF(F5>ct,"",INDEX(data,AGGREGATE(15,6,(ROW(data)-ROW($B$5)+1)/ISNUMBER(SEARCH(search,data)),F5)))

Explanation 
------------

_Note: in the current version of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
 is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for [legacy versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not provide the FILTER function._

The core of this formula is the INDEX function, with AGGREGATE used to figure out the "nth match" for each row in the extraction area:

    INDEX(data,nth_match_formula)
    

Almost all of the work is in figuring out and reporting which rows in "data" match the search string, and reporting the position of each matching value to INDEX. This is done with the AGGREGATE function configured like this:

    AGGREGATE(15,6,(ROW(data)-ROW($B$5)+1)/ISNUMBER(SEARCH(search,data)),F5)
    

The first argument, 15, tells AGGREGATE to behave like [SMALL](https://exceljet.net/functions/small-function)
, and return nth smallest values. The second argument, 6, is an option to ignore errors. The third argument is an expression that generates an array of matching results (described below). The fourth argument, F5, acts like "k" in SMALL to specify the "nth" value.

AGGREGATE operates on arrays, and the expression below builds an array for the third argument inside AGGREGATE :

    (ROW(data)-ROW($B$5)+1)/ISNUMBER(SEARCH(search,data))
    

Here, the ROW function is used to generate an array of [relative row numbers](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
, and [ISNUMBER and SEARCH](https://exceljet.net/formulas/cell-contains-specific-text)
 are used together to match the search string against values in the data, which generates an array of TRUE and FALSE values.

The clever bit is to divide the row numbers by the search results. In a math operation like this, TRUE behaves like 1, and FALSE behaves like zero. The result is row numbers associated with a positive match are divided by 1 and survive the operation, while row numbers associated with non-matching values are destroyed and become #DIV/0 errors. Because AGGREGATE is set to ignore errors, it ignores the #DIV/0 errors, and returns the "nth" smallest number in the remaining values, using the number in column F for "nth".

### Managing performance

Like all array formulas, this formula is "expensive" in terms of resources with a large data set. To minimize performance impacts, the entire INDEX and MATCH formula is wrapped in IF like this:

    =IF(F5>ct,"",formula)
    

where the named range "ct" (D8) holds this formula:

    =COUNTIF(data,"*"&search&"*")
    

This check stops the INDEX and AGGREGATE portion of the formula from executing once all matching values are extracted.

### Array formula with SMALL

If your version of Excel does not have the AGGREGATE function, you can use an alternative formula based on SMALL and IF:

    =IF(F5>ct,"",INDEX(data,SMALL(IF(ISNUMBER(SEARCH(search,data)),ROW(data)-ROW($B$5)+1),F5)))
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

### FILTER function

The INDEX and MATCH formula explained above is meant for [legacy versions of Excel](https://exceljet.net/glossary/legacy-excel)
 that do not offer the [FILTER function](https://exceljet.net/functions/filter-function)
. In the current version of Excel, a better way to solve this problem is to use FILTER in a formula like this:

    =FILTER(data,ISNUMBER(SEARCH(search,data)))

As you can see, this is a _much simpler formula_. For a detailed explanation, [see this page](https://exceljet.net/formulas/filter-with-partial-match)
.

Related formulas
----------------

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: INDEX and MATCH all matches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20data%20with%20helper%20column4.png "Excel formula: INDEX and MATCH all matches")](https://exceljet.net/formulas/index-and-match-all-matches)

### [INDEX and MATCH all matches](https://exceljet.net/formulas/index-and-match-all-matches)

Note: in more recent versions of Excel, the FILTER function is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for legacy versions of Excel that do not provide the FILTER function. By default, lookup formulas in Excel like VLOOKUP and INDEX + MATCH will find...

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Partial match with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Partial%20match%20with%20VLOOKUP.png "Excel formula: Partial match with VLOOKUP")](https://exceljet.net/formulas/partial-match-with-vlookup)

### [Partial match with VLOOKUP](https://exceljet.net/formulas/partial-match-with-vlookup)

In this example, the goal is to retrieve employee information from a table using only a partial match on the last name. In other words, by typing "Aya" into cell H4, the formula should retrieve information about Michael Ayala. The VLOOKUP function supports wildcards , which makes it possible to...

[![Excel formula: FILTER with partial match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20partial%20match.png "Excel formula: FILTER with partial match")](https://exceljet.net/formulas/filter-with-partial-match)

### [FILTER with partial match](https://exceljet.net/formulas/filter-with-partial-match)

In this example, the goal is to extract a set of records that match a partial text string . To keep things simple, we are only matching one field in the data, the last name ("Last"). The core operation of this formula comes from the FILTER function (new in Excel 365 ) which extracts matching data...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

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
    
*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Partial match with VLOOKUP](https://exceljet.net/formulas/partial-match-with-vlookup)
    
*   [FILTER with partial match](https://exceljet.net/formulas/filter-with-partial-match)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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