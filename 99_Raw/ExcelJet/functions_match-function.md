# Excel MATCH function | Exceljet

**Source:** https://exceljet.net/functions/match-function

---

[Skip to main content](https://exceljet.net/functions/match-function#main-content)

[](https://exceljet.net/functions/match-function#)

*   [Previous](https://exceljet.net/functions/lookup-function)
    
*   [Next](https://exceljet.net/functions/offset-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

MATCH Function
==============

by Dave Bruns · Updated 9 Feb 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[HLOOKUP](https://exceljet.net/functions/hlookup-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel MATCH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_match.png "Excel MATCH function")

Summary
-------

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the [INDEX function](https://exceljet.net/functions/index-function)
 to retrieve a value at a matched position.

Purpose 
--------

Get the position of an item in an array

Return value 
-------------

A number representing a position in lookup\_array.

Syntax
------

    =MATCH(lookup_value,lookup_array,[match_type])

*   _lookup\_value_ - The value to match in lookup\_array.
*   _lookup\_array_ - A range of cells or an array reference.
*   _match\_type_ - \[optional\] 1 = exact or next smallest (default), 0 = exact match, -1 = exact or next largest.

Using the MATCH function 
-------------------------

The MATCH function is used to determine the _position_ of a value in a range or [array](https://exceljet.net/glossary/array)
. For example, in the screenshot above, the formula in cell E6 is configured to get the position of the value in cell D6. The MATCH function returns 5 because the lookup value ("peach") is in the 5th position in the range B6:B14:

    =MATCH(D6,B6:B14,0) // returns 5
    

The MATCH function can perform exact and approximate matches and supports [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. There are 3 separate match modes (set by the _match\_type_ argument), as described below. 

_Note: the MATCH function will always return the first match. If you need to return the last match (reverse search) see the [XMATCH function](https://exceljet.net/functions/xmatch-function)
. If you want to return all matches, see the [FILTER function](https://exceljet.net/functions/filter-function)
._

MATCH only supports one-dimensional [arrays](https://exceljet.net/glossary/array)
 or [ranges](https://exceljet.net/glossary/range)
, either vertical or horizontal. However, you can use MATCH to locate values in a two-dimensional range or table by [giving MATCH the single column](https://exceljet.net/formulas/index-and-match-exact-match)
 (or row) that contains the lookup value. You can even [use MATCH twice in a single formula](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
 to find a matching row and column at the same time.

Frequently, the MATCH function is combined with the [INDEX function](https://exceljet.net/functions/index-function)
 to retrieve a value at a certain (matched) position. In other words, MATCH figures out the _position_, and INDEX returns the _value at that position_. For a detailed overview with simple examples, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### Match type information

Match type is optional. If not provided, _match\_type_ defaults to 1 (exact or next smallest). When _match\_type_ is 1 or -1, it is sometimes referred to as an "approximate match". However, keep in mind that MATCH will _always_ perform an exact match when possible, as noted in the table below:

| Match type | Behavior | Details |
| --- | --- | --- |
| 1   | Approximate | MATCH finds the largest value _less than or equal to_ the lookup value. The lookup array must be sorted in _ascending_ order. |
| 0   | Exact | MATCH finds the first value _equal_ to the lookup value. The lookup array does not need to be sorted. |
| \-1 | Approximate | MATCH finds the smallest value _greater than or equal to_ the lookup value. The lookup array must be sorted in _descending_ order. |
| (omitted) | Approximate | When _match\_type_ is omitted, it defaults to 1 with behavior as explained above. |

_Caution: Be sure to set match\_type to zero (0) if you need an exact match. The default setting of 1 can cause MATCH to return results that look normal but are in fact incorrect. Explicitly providing a value for match\_type, is a good reminder of what behavior is expected._

### Exact match

When _match\_type_ is zero (0), MATCH performs an exact match only. In the example below, the formula in E3 is:

    =MATCH(E2,B3:B11,0) // returns 4
    

![Basic exact match with MATCH function](https://exceljet.net/sites/default/files/images/functions/inline/exact%20match%20planets.png "Basic exact match with MATCH function")

In the formula above, the lookup value comes from cell E2. If the lookup value is hardcoded into the formula, it must be enclosed in double quotes (""), since it is a text value:

    =MATCH("Mars",B3:B11,0)
    

_Note: MATCH is not case-sensitive, so "Mars" and "mars" will both return 4._

### Approximate match

When _match\_type_ is set to 1, MATCH will perform an approximate match on values sorted A-Z, finding the largest value _less than or equal to_ the lookup value. In the example shown below, the formula in E3 is:

    =MATCH(E2,B3:B11,1) // returns 5
    

![Basic approximate match with MATCH function](https://exceljet.net/sites/default/files/images/functions/inline/basic%20approximate%20match.png "Basic approximate match with MATCH function")

### Wildcard match

When _match\_type_ is set to zero (0), MATCH can use [wildcards](https://exceljet.net/glossary/wildcard)
. In the example shown below, the formula in E3 is:

    =MATCH(E2,B3:B11,0) // returns 6
    

This is equivalent to:

    =MATCH("pq*",B3:B11,0)
    

![Basic wildcard match with MATCH function](https://exceljet.net/sites/default/files/images/functions/inline/match%20with%20wildcard.png "Basic wildcard match with MATCH function")

### INDEX and MATCH

The MATCH function is commonly used together with the [INDEX function](https://exceljet.net/functions/index-function)
. The resulting formula is called "INDEX and MATCH".  For example, in the screen below, INDEX and MATCH are used to return the cost of a code entered in cell F4. The formula in F5 is:

    =INDEX(C5:C12,MATCH(F4,B5:B12,0)) // returns 150
    

![Basic INDEX and MATCH example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/basic%20index%20and%20match%20example.png?itok=Ddh-jMVU "Basic INDEX and MATCH example")

In this example, MATCH is set up to perform an exact match. The MATCH function locates the code ABX-075 and returns its position (7) directly to the INDEX function as the row number. The INDEX function then returns the 7th value from the range C5:C12 as a final result. The formula is solved like this:

    =INDEX(C5:C12,MATCH(F4,B5:B12,0))
    =INDEX(C5:C12,7)
    =150
    

See below for more examples of the MATCH function. For an overview of how to use INDEX and MATCH with many examples, see:  [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### Case-sensitive match

The MATCH function is not case-sensitive. However, MATCH can be configured to perform a case-sensitive match when combined with the [EXACT function](https://exceljet.net/functions/exact-function)
 in a generic formula like this:

    =MATCH(TRUE,EXACT(lookup_value,array),0)
    

The EXACT function compares every value in _array_ with the _lookup\_value_ in a case-sensitive manner. This formula is explained with an [INDEX and MATCH example here](https://exceljet.net/formulas/case-sensitive-lookup)
.

### Notes

*   MATCH is not case-sensitive.
*   MATCH returns the #N/A error if no match is found.
*   MATCH only works with text up to 255 characters in length.
*   In case of duplicates, MATCH returns the first match.
*   If match\_type is -1 or 1, the **lookup\_array** must be sorted as noted above.
*   If **match\_type** is 0, the **lookup\_value** can contain the [wildcards](https://exceljet.net/glossary/wildcard)
    .
*   The MATCH function is frequently used [together with the INDEX function](https://exceljet.net/articles/index-and-match)
    .

MATCH function examples
-----------------------

[![Excel formula: Rank values by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/display%20ranked%20names%20by%20month.png "Excel formula: Rank values by month")](https://exceljet.net/formulas/rank-values-by-month)

### [Rank values by month](https://exceljet.net/formulas/rank-values-by-month)

This example is set up in two parts for clarity: (1) a formula to determine the top 3 amounts for each month and (2) a formula to retrieve the client name for each of the top 3 monthly amounts. Note there is no actual rank in the source data. Instead, we are using the LARGE function to work...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: COUNTIFS with variable table column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20variable%20table%20column.png "Excel formula: COUNTIFS with variable table column")](https://exceljet.net/formulas/countifs-with-variable-table-column)

### [COUNTIFS with variable table column](https://exceljet.net/formulas/countifs-with-variable-table-column)

First, for context, it's important to note that you can use COUNTIFS with a regular structured reference like this: =COUNTIFS(Table1\[Swim\],"x") This is a much simpler formula, but you can't copy it down column H, because the column reference won't change. The example on this page therefore is meant...

[![Excel formula: Look up entire row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20row.png "Excel formula: Look up entire row")](https://exceljet.net/formulas/look-up-entire-row)

### [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)

In this example, the goal is to look up and retrieve an entire row of values in a set of data. For example, when a value like "Neptune" is entered into cell H5, all values in the range C11:F11 should be returned. For convenience and readability, project (B5:B16) and data (C5:F16) are named ranges...

[![Excel formula: Count not equal to multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20not%20equal%20to%20multiple%20criteria.png "Excel formula: Count not equal to multiple criteria")](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

### [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

In this example, the goal is to count rows in a set of data using multiple criteria and "not equals to" logic. Specifically, we want to count males that are not in group A or B. All data is in an Excel Table named data in the range B5:D15. This problem can be solved with the COUNTIFS function or...

[![Excel formula: Count unique text values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20text%20values%20with%20criteria.png "Excel formula: Count unique text values with criteria")](https://exceljet.net/formulas/count-unique-text-values-with-criteria)

### [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)

This is a complex formula that uses FREQUENCY to count numeric values that are derived with the MATCH function. Working from the inside out, the MATCH function is used to get the position of each value that appears in the data: MATCH(B5:B11,B5:B11,0) The result from MATCH is an array like this: {1;...

[![Excel formula: Step-based lookup example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/step-based_lookup_example.png "Excel formula: Step-based lookup example")](https://exceljet.net/formulas/step-based-lookup-example)

### [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)

This worksheet demonstrates a clever way to look up prices that change based on a selected tier. Imagine a pricing system where the cost of a product depends on both the product color and a tier (e.g., "Bronze," "Silver," or "Gold"). The challenge is to pull the correct price based on both inputs...

[![Excel formula: FILTER with multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20multiple%20or%20criteria.png "Excel formula: FILTER with multiple OR criteria")](https://exceljet.net/formulas/filter-with-multiple-or-criteria)

### [FILTER with multiple OR criteria](https://exceljet.net/formulas/filter-with-multiple-or-criteria)

In this example, criteria are entered in the range F5:H6. The logic of the formula is: item is (tshirt OR hoodie) AND color is (red OR blue) AND city is (denver OR seattle) The filtering logic of this formula (the include argument) is applied with the ISNUMBER and MATCH functions, together with...

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: Multi-criteria lookup and transpose](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multi%20criteria%20lookup%20and%20transpose.png "Excel formula: Multi-criteria lookup and transpose")](https://exceljet.net/formulas/multi-criteria-lookup-and-transpose)

### [Multi-criteria lookup and transpose](https://exceljet.net/formulas/multi-criteria-lookup-and-transpose)

The core of this formula is INDEX, which is retrieving a value from the named range "amount" (B5:B13): =INDEX(amount,row\_num) where row\_num is worked out with the MATCH function and some boolean logic : MATCH(1,($F5=location)\*(G$4=date),0) In this snippet, the location in F5 is compared with all...

[![Excel formula: First match between two ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20match%20between%20two%20ranges.png "Excel formula: First match between two ranges")](https://exceljet.net/formulas/first-match-between-two-ranges)

### [First match between two ranges](https://exceljet.net/formulas/first-match-between-two-ranges)

In this example the named range "range1" refers to cells B5:B8, and the named range "range2" refers to D5:D7. We are using named ranges for convenience and readability only; the formula works fine with regular cell references as well. The core of this formula is INDEX and MATCH. The INDEX function...

[![Excel formula: INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match_with_multiple_criteria.png "Excel formula: INDEX and MATCH approximate match with multiple criteria")](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)

### [INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)

In this example, the goal is to look up the correct shipping cost for an item based on the shipping service selected and the item's weight. At the core, this is an approximate match lookup based on weight. The challenge is that we also need to filter by service. This means we must apply criteria in...

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

[![Excel formula: Sum if x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_x_or_y.png "Excel formula: Sum if x or y")](https://exceljet.net/formulas/sum-if-x-or-y)

### [Sum if x or y](https://exceljet.net/formulas/sum-if-x-or-y)

In this example, the goal is to sum Total when the corresponding Color is either "Red" or "Blue". For convenience, all data is in an Excel Table named data . This is a tricky problem, because the solution is not obvious. The go-to function for conditional sums is the SUMIFS function . However, when...

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

MATCH function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20approximate%20match%20lookups-Thumb.png)](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

### [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

In this video, we'll look at how to highlight approximate match lookups with conditional formatting. Here we have a simple lookup table that shows material costs for various heights and widths. The formula in K8 uses the INDEX and MATCH functions to retrieve the correct cost based on width and...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Sort%20by%20custom%20list%20with%20SORTBY-Play.png)](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

### [Sort by custom list with SORTBY](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

In this video, we'll look at how to sort with SORTBY function using a custom list. One challenge that comes up frequently when sorting is a need to sort in a custom order. For example, in this worksheet, we have a list of opportunities, and we want to sort the list in the order that stages appear...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Two-way%20lookup%20with%20INDEX%20and%20MATCH%20approximate-Thumb.png)](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)

### [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)

In this video we'll look at how to build a two-way lookup with INDEX and MATCH using an approximate match. Here we have a simple cost calculator which looks up cost based on a material's width and height. The match needs to be approximate. For example, if the width is 250, and the height is 325,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20INDEX%20and%20MATCH%20with%20a%20table-Thumb.png)](https://exceljet.net/videos/how-to-use-index-and-match-with-a-table)

### [How to use INDEX and MATCH with a table](https://exceljet.net/videos/how-to-use-index-and-match-with-a-table)

In this video, we'll look at how to use INDEX and MATCH with an Excel Table. Using INDEX and MATCH with an Excel Table is wonderfully straightforward. To illustrate, I'll build INDEX and MATCH formulas that do the same thing as the VLOOKUP formulas already on this worksheet. First, to recap, these...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20MATCH%20to%20find%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-match-to-find-approximate-matches)

### [How to use MATCH to find approximate matches](https://exceljet.net/videos/how-to-use-match-to-find-approximate-matches)

In this video we'll look at how to use the MATCH function to find approximate matches. This is useful for things like determining a commission tier based on a sales number, figuring out a tax rate based on income, or calculating postage based on weight. Let's take a look. In this example, we have a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Introduction%20to%20structured%20references_thumb.png)](https://exceljet.net/videos/introduction-to-structured-references)

### [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)

In this video, I'll give a brief introduction to structured references. A structured reference is a term for using a table name in a formula instead of a normal cell reference. Structured references are optional, and can be used with formulas both inside or outside an Excel table. Let's take a look...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20with%20a%20table-Thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-with-a-table)

### [How to use VLOOKUP with a table](https://exceljet.net/videos/how-to-use-vlookup-with-a-table)

In this video, we'll look at how to use VLOOKUP to lookup values in an Excel Table. On this worksheet, I have a table that contains employee data, named Table1. To illustrate how to work with VLOOKUP when the source data is in a table, I'll set up formulas to the right to extract data from the...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

[![Excel HLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hlookup%20function.png "Excel HLOOKUP function")](https://exceljet.net/functions/hlookup-function)

### [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)

The Excel HLOOKUP function finds and retrieve a value from data in a horizontal table. The "H" in HLOOKUP stands for "horizontal", and lookup values must appear in the first row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and...

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

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

*   [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)
    
*   [COUNTIFS with variable table column](https://exceljet.net/formulas/countifs-with-variable-table-column)
    
*   [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)
    
*   [Next largest match with the MATCH function](https://exceljet.net/formulas/next-largest-match-with-the-match-function)
    
*   [XLOOKUP date of max value](https://exceljet.net/formulas/xlookup-date-of-max-value)
    
*   [Data validation specific characters only](https://exceljet.net/formulas/data-validation-specific-characters-only)
    
*   [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)
    
*   [INDEX and MATCH descending order](https://exceljet.net/formulas/index-and-match-descending-order)
    
*   [XLOOKUP two-way exact match](https://exceljet.net/formulas/xlookup-two-way-exact-match)
    
*   [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    
*   [How to use MATCH to find approximate matches](https://exceljet.net/videos/how-to-use-match-to-find-approximate-matches)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    
*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    
*   [How to save a formula that's not finished](https://exceljet.net/videos/how-to-save-a-formula-thats-not-finished)
    
*   [Two-way lookup with INDEX and MATCH approximate](https://exceljet.net/videos/two-way-lookup-with-index-and-match-approximate)
    
*   [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)
    
*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
    
*   [How to use VLOOKUP with a table](https://exceljet.net/videos/how-to-use-vlookup-with-a-table)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

### Links

*   [Microsoft MATCH function documentation](https://support.office.com/en-us/article/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a)
    

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