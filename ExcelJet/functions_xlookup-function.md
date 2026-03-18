# Excel XLOOKUP function | Exceljet

**Source:** https://exceljet.net/functions/xlookup-function

---

[Skip to main content](https://exceljet.net/functions/xlookup-function#main-content)

[](https://exceljet.net/functions/xlookup-function#)

*   [Previous](https://exceljet.net/functions/wraprows-function)
    
*   [Next](https://exceljet.net/functions/xmatch-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

XLOOKUP Function
================

by Dave Bruns · Updated 6 May 2025

Related functions 
------------------

[XMATCH](https://exceljet.net/functions/xmatch-function)

[FILTER](https://exceljet.net/functions/filter-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[HLOOKUP](https://exceljet.net/functions/hlookup-function)

![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")

Summary
-------

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges. XLOOKUP is a modern and flexible replacement for older functions like VLOOKUP, HLOOKUP, and LOOKUP. 

Purpose 
--------

Look up values in range or array

Return value 
-------------

Matching value in return array

Syntax
------

    =XLOOKUP(lookup,lookup_array,return_array,[if_not_found],[match_mode],[search_mode])

*   _lookup_ - The lookup value.
*   _lookup\_array_ - The array or range to search.
*   _return\_array_ - The array or range to return.
*   _if\_not\_found_ - \[optional\] Value to return if no match found.
*   _match\_mode_ - \[optional\] 0 = exact match (default), -1 = exact match or next smallest, 1 = exact match or next larger, 2 = wildcard match, 3 = regex match.
*   _search\_mode_ - \[optional\] 1 = search from first (default), -1 = search from last, 2 = binary search ascending, -2 = binary search descending.

Using the XLOOKUP function 
---------------------------

XLOOKUP is Excel's modern all‑in‑one lookup function. It lets you search a row or column for a value and retrieve the corresponding value from another range, without the frustrating limitations that plagued older functions like VLOOKUP, HLOOKUP, and LOOKUP. It can even return more than one corresponding value at the same time. With a straightforward syntax, XLOOKUP can be configured to support wildcards, regex, approximate‑match, reverse, and high‑speed binary searches. Key features include:

*   The ability to look up values in vertical or horizontal ranges.
*   Support for a default value when a lookup operation fails.
*   Exact matching plus "next larger" and "next smaller" approximate matching.
*   Simple "contains" type matching with native Excel wildcards (\* ? ~).
*   Complex pattern matching with "regex", a powerful text-matching language.
*   A reverse search option to find the last matching value in a range.
*   A super-fast binary search option when working with large datasets.

For a quick demonstration of XLOOKUP in action, watch this 3-minute video:

Video: [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
 (3 minutes)

### Table of Contents

*   [Exact match](https://exceljet.net/functions/xlookup-function#exact-match)
    
*   [Approximate match](https://exceljet.net/functions/xlookup-function#approximate-match)
    
*   [Multiple values](https://exceljet.net/functions/xlookup-function#multiple-values)
    
*   [Two-way lookup](https://exceljet.net/functions/xlookup-function#two-way-lookup)
    
*   [Custom not found message](https://exceljet.net/functions/xlookup-function#not-found-message)
    
*   [Wildcard match](https://exceljet.net/functions/xlookup-function#wildcard-match)
    
*   [Regex match](https://exceljet.net/functions/xlookup-function#regex-match)
    
*   [Multiple criteria](https://exceljet.net/functions/xlookup-function#multiple-criteria)
    
*   [Complex multiple criteria](https://exceljet.net/functions/xlookup-function#complex-multiple-criteria)
    
*   [Binary search](https://exceljet.net/functions/xlookup-function#binary-search)
    
*   [Match mode options](https://exceljet.net/functions/xlookup-function#match-mode)
    
*   [Search mode options](https://exceljet.net/functions/xlookup-function#search-mode)
    
*   [Advantages of XLOOKUP](https://exceljet.net/functions/xlookup-function#advantages)
    

### Example #1 - Basic exact match

By default, XLOOKUP will perform an exact match. In the example below, XLOOKUP is configured to retrieve the Sales amount from column E based on an exact match of the movie titles in column B. The formula in H5 is:

    =XLOOKUP(H4,B5:B9,E5:E9)
    

![XLOOKUP - basic exact match example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/xlookup%20basic%20exact%20match%20example.png?itok=-2UhrsNm "XLOOKUP - basic exact match example")

[More detailed explanation here](https://exceljet.net/formulas/xlookup-basic-exact-match)
.

### Example #2 - Basic approximate match

To enable an approximate match, provide a value for the _match\_mode_ argument. In the example below, XLOOKUP is used to calculate a discount based on quantity, which requires an approximate match. The formula in F5 sets _match\_mode_ to -1 to enable approximate match with "exact match or next smallest" behavior:

    =XLOOKUP(E5,B5:B9,C5:C9,,-1)
    

![XLOOKUP - basic approximate match example](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20approximate%20match%20example_0.png "XLOOKUP - basic approximate match example")

[More detailed explanation here](https://exceljet.net/formulas/xlookup-basic-approximate-match)
.

### Example #3 - Multiple values

XLOOKUP can return more than one value at the same time (i.e., an array of values) with one formula. The example below shows how XLOOKUP can be used to return three values with a single formula. The formula in C5 is:

    =XLOOKUP(B5,B8:B15,C8:E15)
    

![XLOOKUP - multiple value example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/xlookup%20basic%20multiple%20values.png?itok=IulWTDLp "XLOOKUP - multiple value example")

Notice the return array (C8:E15) includes 3 columns: First, Last, and Department. All three values are returned and [spill](https://exceljet.net/glossary/spill)
 into the range C5:E5.

> In the example above, we use XLOOKUP to return multiple values from the same matching record. If your goal is to return _more than one_ matching record — for example, all people in the Sales Department — XLOOKUP is not a good choice because it will return only one match. In that case, you should switch to the [FILTER function](https://exceljet.net/functions/filter-function)
> , which is designed to return all matching records from a dataset based on a given set of logical conditions.

### Example #4 - Two-way lookup

XLOOKUP can perform a two-way lookup by [nesting](https://exceljet.net/glossary/nesting)
 one XLOOKUP inside another. In the example below, the "inner" XLOOKUP retrieves an entire row (all values for Glass), which is handed off to the "outer" XLOOKUP as the return array. The outer XLOOKUP finds the appropriate group (B) and returns the corresponding value (17.25) as the final result.

    =XLOOKUP(I6,C4:F4,XLOOKUP(I5,B5:B9,C5:F9))
    

![XLOOKUP - two-way lookup example](https://exceljet.net/sites/default/files/images/functions/inline/xlookup%20two-way%20lookup%20example.png "XLOOKUP - two-way lookup example")

[More details here](https://exceljet.net/formulas/xlookup-two-way-exact-match)
.

### Example #5 - Not found message

When XLOOKUP can't find a match, it returns the #N/A error, like other match functions in Excel. Unlike the other match functions, XLOOKUP supports an optional argument called _not\_found_ that can be used to override the #N/A error when it would otherwise appear. Typical values for _not\_found_ include "Not found", "No match", "No result", etc. For example, to display "Not found" when no matching movie is found, you can use a formula like this:

    =XLOOKUP(H4,B5:B9,E5:E9,"Not found")
    

![XLOOKUP - not found example](https://exceljet.net/sites/default/files/images/functions/inline/xlookup%20not%20found%20example.png "XLOOKUP - not found example")

You can customize this message as you like. You can even supply an empty string ("") to display nothing when a match is not found.

> Note: Be careful if you supply an empty string ("") for not\_found because it hides the #N/A error that XLOOKUP will display by default. If you want to see the #N/A error when a match isn't found, omit the not\_found argument entirely.

### Example #6 - Wildcard match

XLOOKUP supports wildcards to enable partial match lookups. Set the _match\_mode_ argument to 2 to enable wildcards in XLOOKUP. In the example below, XLOOKUP is configured to perform a "contains substring" match on the Titles of the books listed in column B. The search string is entered in cell G4, and the formula in cell G6 is:

    =TRANSPOSE(XLOOKUP("*"&G4&"*",data[Title],data,,2))

![XLOOKUP - contains substring example](https://exceljet.net/sites/default/files/images/functions/inline/xlookup_contains_substring_example.png "XLOOKUP - contains substring example")

[Read a complete explanation here](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)
. For a slightly simpler formula, [see this page](https://exceljet.net/formulas/xlookup-wildcard-match-example)
.

### Example #7 - Regex match

In Excel 365, XLOOKUP can match with Regular Expressions (also called "regex"). In the worksheet below, the goal is to look up the correct price of the product number entered in cell F4 using the product codes in column B. This problem is trickier than it looks. Each product code begins with 3 uppercase letters and ends with 2 or 3 uppercase letters. In the middle of the product code is a number between 2 and 4 digits. A wildcard match won't work because a number like 56 can appear inside _other product codes_. However, we can easily solve this problem with a "regex match". To enable a regex match in XLOOKUP, provide 3 for _match\_mode_. Then supply a valid regex pattern as the lookup\_value. In the worksheet below, the formula in cell F5 looks like this:

    =XLOOKUP("[A-Z]{3}"&F4&"[A-Z]{2,3}",B5:B16,C5:C16,,3)

![XLOOKUP - regex match example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/xlookup_with_regex_match_example.png "XLOOKUP - regex match example")

The regex pattern in this formula is "\[A-Z\]{3}"&F4&"\[A-Z\]{2,3}". The translation is "3 uppercase letters A-Z, followed by the value in F4 (56), followed by 2-3 uppercase letters A-Z". Regex is a powerful and somewhat complex language. For a detailed explanation of this particular example (including the workbook), [see this page](https://exceljet.net/formulas/xlookup-with-regex-match)
.

> Regex is a complicated and deep topic. For an introduction to regex in Excel, see [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
> . Regex support in XLOOKUP is only available in Excel 365. 

### Example #8 - multiple criteria

One common challenge with XLOOKUP is how to apply multiple criteria. For example, how do you look up the price for a Medium Blue Hoodie when the item, size, and color are all in different columns? A good approach is to assemble a _new lookup array_ composed of 1s and 0s using Boolean logic and then change the lookup value to 1. This sounds complicated, but it is quite straightforward. You can see this approach in the worksheet below, where the formula in H8 looks like this:

    =XLOOKUP(1,(B5:B15=H5)*(C5:C15=H6)*(D5:D15=H7),E5:E15)

![XLOOKUP example - simple multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/xlookup_simple_multiple_criteria.png "XLOOKUP example - simple multiple criteria")

Each of the three expressions generates an array of TRUE and FALSE values. The math operation (multiplication) automatically converts the TRUE and FALSE values to 1s and 0s:

    {0;0;0;0;1;1;1;0;0;0;0}*{0;1;0;0;0;1;0;1;1;0;0}*{0;1;0;1;0;1;0;0;0;0;0}
    

After multiplication is complete, we have a single array like this:

    {0;0;0;0;0;1;0;0;0;0;0}
    

XLOOKUP uses this array as the _lookup\_array_. Notice the sixth value in the array is 1. This corresponds to the sixth row in the data, which contains a Medium Blue Hoodie. XLOOKUP finds the 1 and returns the corresponding value in the _return\_array_ (E5:E15), which is $29.00. For more details and to download the worksheet, [see this page](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
.

### Example #9 - complex multiple criteria

With the ability to handle arrays natively, XLOOKUP can be used to apply complex criteria using the method explained above. In the worksheet below, XLOOKUP is configured to match the first record where (1) the account begins with "x", _and_ (2) the region is "east", _and_ (3) the month is _not_ April. The formula in G5 looks like this:

    =XLOOKUP(1,(LEFT(B5:B16)="x")*(C5:C16="east")*NOT(MONTH(D5:D16)=4),B5:E16)
    

![XLOOKUP - complex criteria example](https://exceljet.net/sites/default/files/images/functions/inline/xlookup%20complex%20multiple%20criteria.png "XLOOKUP - complex criteria example")

See [this page](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
 for a more detailed explanation of how this formula works.

### Example #10 - Fast binary search

XLOOKUP has a binary search mode option that performs lookups very quickly. To use binary search mode, data must be sorted in ascending or descending order. If values are sorted in _ascending order_, use the value 2 for _search\_mode_. If values are sorted in _descending order_, use the value -2. Below is the generic syntax to enable binary search mode for an exact match lookup:

    =XLOOKUP(A1,lookup_array,return_array,,0,2) // binary search A-Z
    =XLOOKUP(A1,lookup_array,return_array,,0,-2) // binary search Z-A
    

For a more detailed example, see [XLOOKUP binary search](https://exceljet.net/formulas/xlookup-binary-search)
.

### Match mode options

By default, XLOOKUP will perform an _exact match_. Match behavior is controlled by an optional argument called _match\_mode_**,** which has the following options:

| Match mode | Behavior |
| --- | --- |
| 0 (default) | Exact match. Will return #N/A if no match. |
| \-1 | Exact match or the next smaller item. |
| 1   | Exact match or the next larger item. |
| 2   | [Wildcard match](https://exceljet.net/glossary/wildcard)<br> (\*, ?, ~) |
| 3   | Regex match |

> In December 2024, XLOOKUP was upgraded to allow a regex match in Excel 365. You can find a [detailed example here](https://exceljet.net/formulas/xlookup-with-regex-match)
> . The [XMATCH function](https://exceljet.net/functions/xmatch-function)
>  was also updated to support regex. For more about regex in Excel, see [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
> .

### Search mode options

By default, XLOOKUP will start matching from the first data value. Search behavior is controlled by an optional argument called _search\_mode_, which provides the following options:

| Search mode | Behavior |
| --- | --- |
| 1 (default) | Search from the first value |
| \-1 | Search from the last value (reverse) |
| 2   | Binary search values sorted in ascending order |
| \-2 | Binary search values sorted in descending order |

Binary searches are very fast, but _data must be sorted as required_. If data is not sorted properly, a binary search can return invalid results that look perfectly normal. [Detailed example here](https://exceljet.net/formulas/xlookup-binary-search)
.

### XLOOKUP benefits

XLOOKUP offers several important advantages compared to VLOOKUP:

*   XLOOKUP can look up data to the right [or to the left](https://exceljet.net/formulas/xlookup-lookup-left)
     of lookup values
*   XLOOKUP defaults to an exact match
*   XLOOKUP can work with vertical and horizontal data
*   XLOOKUP can perform a reverse search (last to first)
*   XLOOKUP can return entire [rows or columns](https://exceljet.net/formulas/xlookup-lookup-row-or-column)
    , not just one value

For a more detailed comparison, see [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
.

### Notes

1.  XLOOKUP can work with both vertical and horizontal arrays.
2.  XLOOKUP will return #N/A if the lookup value is not found.
3.  Like the [INDEX function](https://exceljet.net/functions/index-function)
    , XLOOKUP returns a [_reference_ as a result](https://exceljet.net/formulas/get-address-of-lookup-result)
    .
4.  The size of the _lookup\_array_ must be compatible with the _return\_array_, or XLOOKUP will return #VALUE!
5.  If XLOOKUP points to an [Excel Table](https://exceljet.net/glossary/excel-table)
     in an _external workbook_, the other workbook must be open or XLOOKUP will return a #REF! error.

XLOOKUP function examples
-------------------------

[![Excel formula: Get last match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match.png "Excel formula: Get last match")](https://exceljet.net/formulas/get-last-match)

### [Get last match](https://exceljet.net/formulas/get-last-match)

In the example shown, we have a set of order data that includes Date, Product, Name, and Amount. The data is sorted by date in ascending order. The goal is to look up the latest order for a given person by Name. In other words, we want the last match by name. The challenge is that Excel lookup...

[![Excel formula: Detailed LET function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/let%20function%20example.png "Excel formula: Detailed LET function example")](https://exceljet.net/formulas/detailed-let-function-example)

### [Detailed LET function example](https://exceljet.net/formulas/detailed-let-function-example)

In this example, we have a simple set of data in B5:D16 that includes ID, Name, and Points. The goal is to generate a custom message for any name in the list by entering a valid ID in cell G5. The message uses the name from column C and the points in column D like this: "Hi \[name\], you have \[points...\
\
[![Excel formula: Lookup first negative value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20first%20negative%20value.png "Excel formula: Lookup first negative value")](https://exceljet.net/formulas/lookup-first-negative-value)\
\
### [Lookup first negative value](https://exceljet.net/formulas/lookup-first-negative-value)\
\
In this example, the goal is to lookup the first negative value in a set of data. In addition, we also want to get the corresponding date. All data is in an Excel Table called data, in the range B5:C16. This information represents the low temperature in Fahrenheit (F) for the dates as shown. There...\
\
[![Excel formula: Find longest string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_longest_string.png "Excel formula: Find longest string")](https://exceljet.net/formulas/find-longest-string)\
\
### [Find longest string](https://exceljet.net/formulas/find-longest-string)\
\
The goal is to find the longest text string in the range B5:B16. At the core, this is a lookup problem that requires creating a value (the string length) that does not exist in the data as part of the formula. The easiest way to solve this problem is with the XLOOKUP function or the FILTER function...\
\
[![Excel formula: Find closest match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_closest_match_0.png "Excel formula: Find closest match")](https://exceljet.net/formulas/find-closest-match)\
\
### [Find closest match](https://exceljet.net/formulas/find-closest-match)\
\
In this example, the goal is to find the closest match to a target value entered in cell E5. Although it may not look like it, this is essentially a look-up problem. The easiest way to solve this problem is with the XLOOKUP function . However in older versions of Excel without the XLOOKUP function...\
\
[![Excel formula: Get first numeric value in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_numeric_value_in_a_range.png "Excel formula: Get first numeric value in a range")](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)\
\
### [Get first numeric value in a range](https://exceljet.net/formulas/get-first-numeric-value-in-a-range)\
\
The general goal is to return the first numeric value in a row or column. More specifically, in the worksheet shown, we have dates in column B and a numeric value in the range C5:C16. Notice that all of the cells in this range have numeric values. Some are blank and some contain text values. We...\
\
[![Excel formula: XLOOKUP latest by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20latest%20by%20date.png "Excel formula: XLOOKUP latest by date")](https://exceljet.net/formulas/xlookup-latest-by-date)\
\
### [XLOOKUP latest by date](https://exceljet.net/formulas/xlookup-latest-by-date)\
\
XLOOKUP offers several features that make it exceptionally good for more complicated lookups. In this example, we want the latest price for an item by date . If data were sorted by date in ascending order, this would be very straightforward . However, in this case, data is unsorted . By default,...\
\
[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)\
\
### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)\
\
In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...\
\
[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)\
\
### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)\
\
XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...\
\
[![Excel formula: XLOOKUP wildcard contains substring](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_wildcard_contains_substring.png "Excel formula: XLOOKUP wildcard contains substring")](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)\
\
### [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)\
\
The goal is to look up the Title, Author, and Year in the list of books as shown using a formula based on a partial match and a wildcard. The text string to search for is entered in cell G4. All data is in an Excel Table named data in the range B5:D16. This problem can be easily solved with the...\
\
[![Excel formula: Get address of lookup result](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_lookup_result.png "Excel formula: Get address of lookup result")](https://exceljet.net/formulas/get-address-of-lookup-result)\
\
### [Get address of lookup result](https://exceljet.net/formulas/get-address-of-lookup-result)\
\
There are certain functions in Excel that return a cell reference as a result rather than a value. Two of these functions are XLOOKUP and INDEX . The presence of the cell reference in the result is not obvious, because Excel immediately resolves the reference to the value in that cell. You can...\
\
[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)\
\
### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)\
\
The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...\
\
[![Excel formula: XLOOKUP lookup left](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20lookup%20left.png "Excel formula: XLOOKUP lookup left")](https://exceljet.net/formulas/xlookup-lookup-left)\
\
### [XLOOKUP lookup left](https://exceljet.net/formulas/xlookup-lookup-left)\
\
Whereas VLOOKUP is limited to lookups to the right of the lookup column, XLOOKUP can lookup values to the left natively. This means XLOOKUP can be used instead of INDEX and MATCH to find values to the left in a table or range. In the example shown, we are looking for the weight associated with...\
\
[![Excel formula: Find longest string with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Find_longest_string_with_criteria.png "Excel formula: Find longest string with criteria")](https://exceljet.net/formulas/find-longest-string-with-criteria)\
\
### [Find longest string with criteria](https://exceljet.net/formulas/find-longest-string-with-criteria)\
\
In this example, the goal is to find the longest text string in the range C5:C16 that belongs to the group entered in cell F5. The group is a variable that may be changed at any time. At the core, this is a lookup problem, and the challenge is that the value we need to look up (the string length)...\
\
[![Excel formula: XLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_without_NA_error.png "Excel formula: XLOOKUP without #N/A error")](https://exceljet.net/formulas/xlookup-without-na-error)\
\
### [XLOOKUP without #N/A error](https://exceljet.net/formulas/xlookup-without-na-error)\
\
In this example, we have a simple worksheet that uses the XLOOKUP function to lookup the name of a U.S. state when a valid two-letter code is provided as a lookup value. The goal is to remove the #N/A error that XLOOKUP returns when it can't find a result. Although you could use the IFNA or IFERROR...\
\
XLOOKUP function videos\
-----------------------\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/XLOOKUP%20with%20boolean%20logic-Play.png)](https://exceljet.net/videos/xlookup-with-boolean-logic)\
\
### [XLOOKUP with boolean logic](https://exceljet.net/videos/xlookup-with-boolean-logic)\
\
In this video we'll look at how to use the XLOOKUP function with Boolean logic. Boolean logic is an elegant way to apply multiple criteria. In this worksheet we have sample order data in a table called "data". Let's use the XLOOKUP function to find the first order in March where the color is red...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20approximate%20match-Play.png)](https://exceljet.net/videos/basic-xlookup-approximate-match)\
\
### [Basic XLOOKUP approximate match](https://exceljet.net/videos/basic-xlookup-approximate-match)\
\
In this video, we’ll set up the XLOOKUP function to perform an approximate match. In this worksheet, the table in B5:C9 contains quantity-based discounts. As the quantity increases, the discount also increases. Let's set up the XLOOKUP function to calculate the correct discount for each quantity...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)\
\
### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)\
\
In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/XLOOKUP%20with%20multiple%20lookup%20values-Play.png)](https://exceljet.net/videos/xlookup-with-multiple-lookup-values)\
\
### [XLOOKUP with multiple lookup values](https://exceljet.net/videos/xlookup-with-multiple-lookup-values)\
\
In this video, we'll set up the XLOOKUP function to return multiple values in a dynamic array. In this worksheet, we have an example we looked at previously. On the left, we have quantity-based discounts, and on the right, we have some random quantities. Let's set up XLOOKUP to return all results...\
\
Related functions\
-----------------\
\
[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)\
\
### [XMATCH Function](https://exceljet.net/functions/xmatch-function)\
\
The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...\
\
[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)\
\
### [FILTER Function](https://exceljet.net/functions/filter-function)\
\
The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...\
\
[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)\
\
### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)\
\
The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...\
\
[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)\
\
### [INDEX Function](https://exceljet.net/functions/index-function)\
\
The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....\
\
[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)\
\
### [MATCH Function](https://exceljet.net/functions/match-function)\
\
MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)\
 (\* ?) for partial matches. Often, MATCH is combined with the...\
\
[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)\
\
### [LOOKUP Function](https://exceljet.net/functions/lookup-function)\
\
The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.\
\
[![Excel HLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hlookup%20function.png "Excel HLOOKUP function")](https://exceljet.net/functions/hlookup-function)\
\
### [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)\
\
The Excel HLOOKUP function finds and retrieve a value from data in a horizontal table. The "H" in HLOOKUP stands for "horizontal", and lookup values must appear in the first row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and...\
\
Was this page helpful? Yes No Report a problem\
\
Cancel Submit\
\
![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)\
\
Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)\
\
### Dave Bruns\
\
Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.\
\
Related Information\
-------------------\
\
### Formulas\
\
*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)\
    \
*   [XLOOKUP binary search](https://exceljet.net/formulas/xlookup-binary-search)\
    \
*   [Dynamic range between two matches](https://exceljet.net/formulas/dynamic-range-between-two-matches)\
    \
*   [Lookup first negative value](https://exceljet.net/formulas/lookup-first-negative-value)\
    \
*   [XMATCH with multiple criteria](https://exceljet.net/formulas/xmatch-with-multiple-criteria)\
    \
*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)\
    \
*   [XLOOKUP horizontal lookup](https://exceljet.net/formulas/xlookup-horizontal-lookup)\
    \
*   [Due date by category](https://exceljet.net/formulas/due-date-by-category)\
    \
*   [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)\
    \
*   [Get last match](https://exceljet.net/formulas/get-last-match)\
    \
\
### Videos\
\
*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)\
    \
*   [Basic XLOOKUP approximate match](https://exceljet.net/videos/basic-xlookup-approximate-match)\
    \
*   [XLOOKUP with multiple lookup values](https://exceljet.net/videos/xlookup-with-multiple-lookup-values)\
    \
*   [XLOOKUP with boolean logic](https://exceljet.net/videos/xlookup-with-boolean-logic)\
    \
\
### Functions\
\
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)\
    \
*   [FILTER Function](https://exceljet.net/functions/filter-function)\
    \
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)\
    \
*   [INDEX Function](https://exceljet.net/functions/index-function)\
    \
*   [MATCH Function](https://exceljet.net/functions/match-function)\
    \
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)\
    \
*   [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)\
    \
\
### Articles\
\
*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)\
    \
*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)\
    \
*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)\
    \
\
### Links\
\
*   [Microsoft XLOOKUP function documentation](https://support.office.com/en-us/article/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929)\
    \
\
Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!\
\
Thierry\
\
[More Testimonials](https://exceljet.net/feedback)\
\
Get [Training](https://exceljet.net/training)\
\
----------------------------------------------\
\
### Quick, clean, and to the point training\
\
Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.\
\
[View Paid Training & Bundles](https://exceljet.net/training)\
\
[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)\
\
[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)\
\
[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)\
\
[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)\
\
[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)\
\
[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)