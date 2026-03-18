# Excel INDEX function | Exceljet

**Source:** https://exceljet.net/functions/index-function

---

[Skip to main content](https://exceljet.net/functions/index-function#main-content)

[](https://exceljet.net/functions/index-function#)

*   [Previous](https://exceljet.net/functions/hyperlink-function)
    
*   [Next](https://exceljet.net/functions/indirect-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

INDEX Function
==============

by Dave Bruns · Updated 30 Aug 2024

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[HLOOKUP](https://exceljet.net/functions/hlookup-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel INDEX function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")

Summary
-------

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers.

Purpose 
--------

Get a value in a list or table based on location

Return value 
-------------

The value at a given location.

Syntax
------

    =INDEX(array,row_num,[col_num],[area_num])

*   _array_ - A range of cells, or an array constant.
*   _row\_num_ - The row position in the reference or array.
*   _col\_num_ - \[optional\] The column position in the reference or array.
*   _area\_num_ - \[optional\] The range in reference that should be used.

Using the INDEX function 
-------------------------

The INDEX function returns the value at a given location in a range or array. INDEX is a powerful and versatile function. You can use INDEX to retrieve individual values or entire rows and columns. INDEX is frequently used together with the [MATCH function](https://exceljet.net/functions/match-function)
. In this scenario, the MATCH function locates a value and feeds the numeric position to the INDEX function, and INDEX returns the value at that position. 

In the most common usage, INDEX takes three arguments: _array_, _row\_num_, and _col\_num_. _Array_ is the range or array from which to retrieve values. _Row\_num_ is the row number from which to retrieve a value, and _col\_num_ is the column number at which to retrieve a value. _Col\_num_ is optional and not needed when array is one-dimensional.

In the example shown above, the goal is to get the diameter of the planet Jupiter. Because Jupiter is the fifth planet in the list, and Diameter is the third column, the formula in G7 is:

    =INDEX(B5:E13,5,3) // diameter of Jupiter
    

The formula above is of limited value because the row and column numbers have been hard-coded. Typically, the MATCH function would be used inside INDEX to provide these numbers. For a detailed explanation with many examples, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### Basic usage

INDEX gets a value at a given location in a range of cells based on numeric position. When the range is one-dimensional, you only need to supply a row number. When the range is two-dimensional, you must supply both the row and column numbers. For example, to get the third item from the one-dimensional range A1:A5:

    =INDEX(A1:A5,3) // returns value in A3
    

The formulas below show how INDEX can be used to get a value from a two-dimensional range:

    =INDEX(A1:B5,2,2) // returns value in B2
    =INDEX(A1:B5,3,1) // returns value in A3
    

### INDEX and MATCH

In the examples above, the position is "hardcoded". Typically, the MATCH function is used to find positions for INDEX. For example, in the screen below, the MATCH function is used to locate "Mars" (G6) in row 3 and feed that position to INDEX. The formula in G7 is:

    =INDEX(B5:E13,MATCH(G6,B5:B13,0),3)
    

![Example of INDEX and MATCH formula](https://exceljet.net/sites/default/files/images/functions/inline/excel%20index%20and%20match%20example.png "Example of INDEX and MATCH formula")

MATCH provides the row number (4) to INDEX. The column number is still hardcoded as 3.

### INDEX and MATCH with horizontal table

In the screen below, the table above has been transposed horizontally. The MATCH function returns the column number (4) and the row number is hardcoded as 2. The formula in C10 is:

    =INDEX(C4:K6,2,MATCH(C9,C4:K4,0))
    

![Example of INDEX and MATCH formula with horizontal table](https://exceljet.net/sites/default/files/images/functions/inline/excel%20index%20and%20match%20horizontal%20example.png "Example of INDEX and MATCH formula with horizontal table")

For a detailed explanation with many examples, see: [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)

### Entire row / column

INDEX can be used to return entire columns or rows like this:

    =INDEX(range,0,n) // entire column
    =INDEX(range,n,0) // entire row
    

where n represents the number of the column or row to return. [This example](https://exceljet.net/formulas/look-up-entire-column)
 shows a practical application of this idea.

### Reference as result

It's important to note that the INDEX function returns a _reference_ as a result. For example, in the following formula, INDEX returns A2:

    =INDEX(A1:A5,2) // returns A2
    

In a typical formula, you'll see the _value in cell A2_ as a result, so it's not obvious that INDEX is returning a reference. However, this is a useful feature in formulas [like this one](https://exceljet.net/formulas/dynamic-named-range-with-index)
, which uses INDEX to create a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
. You can use the [CELL function](https://exceljet.net/functions/cell-function)
 to [report the reference](https://exceljet.net/formulas/get-address-of-lookup-result)
 returned by INDEX.

### Two forms

The INDEX function has two forms: **array** and **reference**. Both forms have the same behavior – INDEX returns a reference in an array based on a given row and column location. The difference is that the reference form of INDEX allows _more than one array_, along with an optional argument to select which array should be used. Most formulas use the array form of INDEX, but both forms are discussed below. 

#### Array form

In the array form of INDEX, the first parameter is an _array_, which is supplied as a range of cells or an array constant. The syntax for the array form of INDEX is:

    INDEX(array,row_num,[col_num])
    

*   If both _row\_num_ and _col\_num_ are supplied, INDEX returns the value in the cell at the intersection of _row\_num_ and _col\_num_.
*   If _row\_num_ is set to zero, INDEX returns an array of values for an entire column. To use these array values, you can enter the INDEX function as an array formula in a horizontal range, or feed the array into another function.
*   If _col\_num_ is set to zero, INDEX returns an array of values for an entire row. To use these array values, you can enter the INDEX function as an array formula in a vertical range, or feed the array into another function.

#### Reference form

In the reference form of INDEX, the first parameter is a _reference_ to one or more ranges, and a fourth optional argument, _area\_num_, is provided to select the appropriate range. The syntax for the reference form of INDEX is:

    INDEX(reference,row_num,[col_num],[area_num])
    

Just like the array form of INDEX, the reference form of INDEX returns the reference of the cell at the intersection _row\_num_ and _col\_num_. The difference is that the _reference_ argument contains more than one range, and _area\_num_ selects which range should be used. The _area\_num_ is argument is supplied as a number that acts like a numeric index. The first array inside reference is 1, the second array is 2, and so on.

For example, in the formula below, _area\_num_ is supplied as 2, which refers to the range A7:C10:

    =INDEX((A1:C5,A7:C10),1,3,2)
    

In the above formula, INDEX will return the value at row 1 and column 3 of A7:C10.

*   Multiple ranges in _reference_ are separated by commas and enclosed in parentheses.
*   All ranges must on one sheet or INDEX will return a #VALUE error. Use the [CHOOSE function as a workaround](https://exceljet.net/formulas/index-with-variable-array)
    .

INDEX function examples
-----------------------

[![Excel formula: Name of nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value.png "Excel formula: Name of nth largest value")](https://exceljet.net/formulas/name-of-nth-largest-value)

### [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)

In a nutshell, this formula uses the LARGE function to find the nth largest value in a set of data. Once we have that value, we plug it into a standard INDEX and MATCH formula to retrieve the associated name. In other words, we use the nth largest value like a "key" to retrieve associated...

[![Excel formula: Get address of lookup result](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_lookup_result.png "Excel formula: Get address of lookup result")](https://exceljet.net/formulas/get-address-of-lookup-result)

### [Get address of lookup result](https://exceljet.net/formulas/get-address-of-lookup-result)

There are certain functions in Excel that return a cell reference as a result rather than a value. Two of these functions are XLOOKUP and INDEX . The presence of the cell reference in the result is not obvious, because Excel immediately resolves the reference to the value in that cell. You can...

[![Excel formula: Sort and extract unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20and%20extract%20unique%20values.png "Excel formula: Sort and extract unique values")](https://exceljet.net/formulas/sort-and-extract-unique-values)

### [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)

Note: the core idea of this formula is adapted from an example in Mike Girvin's excellent book Control+Shift+Enter . The example shown uses several formulas, which are described below. At a high level, the MMULT function is used to compute a numeric rank in a helper column (column C), and this rank...

[![Excel formula: Find lowest n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Find%20lowest%20n%20values.png "Excel formula: Find lowest n values")](https://exceljet.net/formulas/find-lowest-n-values)

### [Find lowest n values](https://exceljet.net/formulas/find-lowest-n-values)

The SMALL function retrieves the smallest values from data based on a given rank. For example: =SMALL(range,1) // smallest =SMALL(range,2) // 2nd smallest =SMALL(range,3) // 3rd smallest In the worksheet shown, the rank (which is provided to SMALL as the k argument) comes from numbers in column E...

[![Excel formula: Get first entry by month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_first_entry_by_month_and_year.png "Excel formula: Get first entry by month and year")](https://exceljet.net/formulas/get-first-entry-by-month-and-year)

### [Get first entry by month and year](https://exceljet.net/formulas/get-first-entry-by-month-and-year)

Note: the values in E5:E8 are actual dates, formatted with the custom number format "mmm". Working from the inside out, the expression: MATCH(TRUE,TEXT(date,"mmyy")=TEXT(E5,"mmyy") uses the TEXT function to generate an array of strings in the format "mmyy": {"0117";"0117";"0117";"0217";"0217";"0217...

[![Excel formula: INDEX and MATCH approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match.png "Excel formula: INDEX and MATCH approximate match")](https://exceljet.net/formulas/index-and-match-approximate-match)

### [INDEX and MATCH approximate match](https://exceljet.net/formulas/index-and-match-approximate-match)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table to the right. For convenience only, grade (G5:G9) and score (F5:F9) are named ranges . This is a classic "approximate-match" lookup problem because it is unlikely that a...

[![Excel formula: Sum last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_rows.png "Excel formula: Sum last n rows")](https://exceljet.net/formulas/sum-last-n-rows)

### [Sum last n rows](https://exceljet.net/formulas/sum-last-n-rows)

In the example shown, we have a list of amounts in column C. The goal is to dynamically sum the last n amounts using the number that appears in cell E5 for n . Since the list may grow over time, the key requirement is to sum amounts by position. For convenience only, the values to sum are in the...

[![Excel formula: INDEX with variable array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20with%20variable%20array.png "Excel formula: INDEX with variable array")](https://exceljet.net/formulas/index-with-variable-array)

### [INDEX with variable array](https://exceljet.net/formulas/index-with-variable-array)

At the core, this is a normal INDEX and MATCH function : =INDEX(array,MATCH(value,range,0)) Where the MATCH function is used to find the correct row to return from array, and the INDEX function returns the value at that array. However, in this case we want to make the array variable, so that the...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: Running total in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20total%20in%20table2.png "Excel formula: Running total in Table")](https://exceljet.net/formulas/running-total-in-table)

### [Running total in Table](https://exceljet.net/formulas/running-total-in-table)

At the core, this formula has a simple pattern like this: =SUM(first:current) Where "first" is the first cell in the Total column, and "current" is a reference to a cell in the current row of the Total column. To get the a reference to the first cell, we use INDEX like this: INDEX(\[Total\],1) Here,...

[![Excel formula: Lookup lowest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20lowest%20value.png "Excel formula: Lookup lowest value")](https://exceljet.net/formulas/lookup-lowest-value)

### [Lookup lowest value](https://exceljet.net/formulas/lookup-lowest-value)

Working from the inside out, the MIN function is used to find the lowest bid in the range C5:C9: MIN(C5:C9) // returns 99500 The result, 99500, is fed into the MATCH function as the lookup value: MATCH(99500,C5:C9,0) // returns 4 Match then returns the location of this value in the range, 4, which...

[![Excel formula: Get last match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match.png "Excel formula: Get last match")](https://exceljet.net/formulas/get-last-match)

### [Get last match](https://exceljet.net/formulas/get-last-match)

In the example shown, we have a set of order data that includes Date, Product, Name, and Amount. The data is sorted by date in ascending order. The goal is to look up the latest order for a given person by Name. In other words, we want the last match by name. The challenge is that Excel lookup...

[![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")](https://exceljet.net/formulas/random-value-from-list-or-table)

### [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)

Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead. To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which...

[![Excel formula: INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match_with_multiple_criteria.png "Excel formula: INDEX and MATCH approximate match with multiple criteria")](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)

### [INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)

In this example, the goal is to look up the correct shipping cost for an item based on the shipping service selected and the item's weight. At the core, this is an approximate match lookup based on weight. The challenge is that we also need to filter by service. This means we must apply criteria in...

[![Excel formula: Nearest location with XMATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nearest%20location%20with%20XMATCH.png "Excel formula: Nearest location with XMATCH")](https://exceljet.net/formulas/nearest-location-with-xmatch)

### [Nearest location with XMATCH](https://exceljet.net/formulas/nearest-location-with-xmatch)

At the core, this formula is a basic INDEX and MATCH formula . However, instead of using the older MATCH function , we are using XMATCH function , which provides a more powerful match mode setting: =INDEX(location,XMATCH(0,distance,1)) Working from the inside out, we are using the XMATCH function...

INDEX function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20CHOOSE%20function-Thumb.png)](https://exceljet.net/videos/how-to-use-the-choose-function)

### [How to use the CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)

In this video we'll look at how you can use the CHOOSE function . Let's look at three examples. In this first example we have some items listed with a numeric color code. We want to bring these names into column D. Now, since I already have a table here, I could just use VLOOKUP and reference the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20generate%20random%20text%20values-Play.png)](https://exceljet.net/videos/how-to-generate-random-text-values)

### [How to generate random text values](https://exceljet.net/videos/how-to-generate-random-text-values)

In this video, we'll look at how to create a list of random text values. As we've already seen, the RANDARRAY function can be used to generate random dates and times, which are numeric values. How can we generate random values that aren't numeric? One way is to use this is to use the RANDARRAY...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20approximate%20match%20lookups-Thumb.png)](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

### [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

In this video, we'll look at how to highlight approximate match lookups with conditional formatting. Here we have a simple lookup table that shows material costs for various heights and widths. The formula in K8 uses the INDEX and MATCH functions to retrieve the correct cost based on width and...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)

### [How to create a dynamic named range with INDEX](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)

In this video we'll look at how to create a dynamic named range with the INDEX function . Unlike INDIRECT and OFFSET , INDEX is a non-volatile function. This means that INDEX will not recalculate whenever a change is made to a worksheet. This makes INDEX ideal for professional models and for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20INDEX%20and%20MATCH%20with%20a%20table-Thumb.png)](https://exceljet.net/videos/how-to-use-index-and-match-with-a-table)

### [How to use INDEX and MATCH with a table](https://exceljet.net/videos/how-to-use-index-and-match-with-a-table)

In this video, we'll look at how to use INDEX and MATCH with an Excel Table. Using INDEX and MATCH with an Excel Table is wonderfully straightforward. To illustrate, I'll build INDEX and MATCH formulas that do the same thing as the VLOOKUP formulas already on this worksheet. First, to recap, these...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20do%20a%20two-way%20lookup%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

### [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

In this video we'll look at how to set up a classic two-way lookup using INDEX and MATCH . Here we have a list of salespeople with monthly sales figures. What we want to do is add a formula in Q6 that looks up and retrieves a sales number based on the name and month above. To do this, we'll use the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Introduction%20to%20structured%20references_thumb.png)](https://exceljet.net/videos/introduction-to-structured-references)

### [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)

In this video, I'll give a brief introduction to structured references. A structured reference is a term for using a table name in a formula instead of a normal cell reference. Structured references are optional, and can be used with formulas both inside or outside an Excel table. Let's take a look...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20set%20up%20a%20running%20total%20in%20a%20table-Thumb.png)](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)

### [How to set up a running total in a table](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)

In this video, we'll look at how to set up a running total in an Excel table. Setting up a running total in an Excel table is a little tricky because it's not obvious how to use structured references. This is because structured references provide a notation for current row, but not for first row in...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel HLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hlookup%20function.png "Excel HLOOKUP function")](https://exceljet.net/functions/hlookup-function)

### [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)

The Excel HLOOKUP function finds and retrieve a value from data in a horizontal table. The "H" in HLOOKUP stands for "horizontal", and lookup values must appear in the first row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and...

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Number to words](https://exceljet.net/formulas/number-to-words)
    
*   [Sum last n rows](https://exceljet.net/formulas/sum-last-n-rows)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    
*   [Position of first partial match](https://exceljet.net/formulas/position-of-first-partial-match)
    
*   [Find longest string](https://exceljet.net/formulas/find-longest-string)
    
*   [Lookup lowest Monday tide](https://exceljet.net/formulas/lookup-lowest-monday-tide)
    
*   [Maximum change](https://exceljet.net/formulas/maximum-change)
    
*   [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)
    
*   [Last n rows](https://exceljet.net/formulas/last-n-rows)
    
*   [Average last N values in a table](https://exceljet.net/formulas/average-last-n-values-in-a-table)
    

### Videos

*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    
*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    
*   [How to create a dynamic named range with INDEX](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-index)
    
*   [How to save a formula that's not finished](https://exceljet.net/videos/how-to-save-a-formula-thats-not-finished)
    
*   [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)
    
*   [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)
    
*   [How to use the CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)
    
*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
    
*   [How to set up a running total in a table](https://exceljet.net/videos/how-to-set-up-a-running-total-in-a-table)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    
*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

### Links

*   [Microsoft INDEX function documentation](https://support.office.com/en-us/article/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd)
    

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