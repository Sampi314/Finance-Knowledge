# Excel XMATCH function | Exceljet

**Source:** https://exceljet.net/functions/xmatch-function

---

[Skip to main content](https://exceljet.net/functions/xmatch-function#main-content)

[](https://exceljet.net/functions/xmatch-function#)

*   [Previous](https://exceljet.net/functions/xlookup-function)
    
*   [Next](https://exceljet.net/functions/bin2dec-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

XMATCH Function
===============

by Dave Bruns · Updated 4 Jun 2025

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[MATCH](https://exceljet.net/functions/match-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[HLOOKUP](https://exceljet.net/functions/hlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")

Summary
-------

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. 

Purpose 
--------

Get the position of an item in a list or table

Return value 
-------------

Numeric position in lookup array

Syntax
------

    =XMATCH(lookup_value,lookup_array,[match_mode],[search_mode])

*   _lookup\_value_ - The lookup value.
*   _lookup\_array_ - The array or range to search.
*   _match\_mode_ - \[optional\] 0 = exact match (default), -1 = exact match or next smallest, 1 = exact match or next larger, 2 = wildcard match, 3 = regex match.
*   _search\_mode_ - \[optional\] 1 = search from first (default), -1 = search from last, 2 = binary search ascending, -2 = binary search descending.

Using the XMATCH function 
--------------------------

XMATCH is a modern replacement for the MATCH function. It is a flexible and versatile function with a number of useful features:

*   The ability to look up values in vertical or horizontal ranges.
*   Exact matching plus "next larger" and "next smaller" approximate matching.
*   Simple "contains" type matching with native Excel wildcards (\* ? ~).
*   Complex pattern matching with "regex", a powerful text-matching language.
*   A reverse search option to find the _last_ matching value in a range.
*   A super-fast binary search option when working with large datasets.

The XMATCH function performs a lookup and returns the numeric position of the lookup value as a result. XMATCH takes four [arguments](https://exceljet.net/glossary/function-argument)
, and the generic syntax looks like this:

    =XMATCH(lookup_value,lookup_array,[match_mode],[search_mode])

_Lookup\_value_ is the value to look for, and _lookup\_array_ is the [range](https://exceljet.net/glossary/range)
 or [array](https://exceljet.net/glossary/array)
 to look in. The _match\_mode_ argument controls what kind of match is performed (exact, next smallest, next largest, or wildcard). _Search\_mode_ controls the search direction (first to last or last to first) and enables the binary search option, which is optimized for speed. [See below](https://exceljet.net/functions/xmatch-function#match_mode)
 for more details.

### Example

To perform an ordinary exact match, only the first two arguments are required. For example, to locate the position of the planet Mars in the worksheet shown, you can use XMATCH like this:

    =XMATCH(G4,B5:B13) // returns 4

The result is 4 since "Mars" appears in the fourth row of the range B5:B13. Typically, the XMATCH function is used together with the INDEX function to retrieve a value _at a specific location_. For example, to find the diameter of Mars, you can combine INDEX and XMATCH like this:

    =INDEX(C5:C13,XMATCH(G4,B5:B13)) // returns 6792
    

In this formula, XMATCH returns the position of Mars (4) to INDEX, and INDEX returns the 4th value in the range C5:C13 (6,792) as the final result.

> _XMATCH defaults to an exact match, so match\_mode is not required above._

### XMATCH vs. MATCH

XMATCH is an upgraded replacement for the MATCH function. Like the MATCH function, XMATCH performs a lookup and returns a numeric position. Also, like MATCH, XMATCH can perform lookups in vertical or horizontal ranges, supports both approximate and exact matches, and allows wildcards (\* ?) for partial matches. The 5 key differences between XMATCH and MATCH are:

1.  XMATCH defaults to an exact match, while MATCH defaults to an approximate match.
2.  XMATCH can find the next larger item _or_ the next smaller item.
3.  XMATCH can perform a reverse search (i.e. search from last to first).
4.  XMATCH does not require values to be sorted when performing an approximate match.
5.  XMATCH can perform a binary search, which is specifically optimized for speed.
6.  XMATCH can use regex for matching, a powerful pattern-matching language.

> In an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
> , using XMATCH instead of the MATCH function "upgrades" the formula to include the benefits listed above.

### Replacing MATCH with XMATCH

In some cases, XMATCH can be a drop-in replacement for the MATCH function. For example, for exact matches, the syntax is identical:

    =MATCH(value,array,0) // exact match
    =XMATCH(value,array,0) // exact match
    

However, for approximate matches, the behavior is _different_ when _match\_type_ is set to 1:

    =MATCH(value,array,1) // exact match or next smallest
    =XMATCH(value,array,1) // exact match or next *largest*
    

In addition, XMATCH allows -1 for match type, which is not available with MATCH:

    =XMATCH(value,array,-1) // exact match or next smallest
    

> There are subtle differences in the behavior of MATCH and XMATCH in specific cases. For example, if cell A1 is empty, and the lookup array contains an empty cell, =XMATCH(A1, array) will return the position of the empty cell, whereas =MATCH(A1, array) will return #N/A. Let me know if you notice other differences and I will include them on this page.

### Match mode

The _match\_mode_ argument controls what kind of match is performed (exact, next smallest, next largest, wildcard, or regex). Note that _match\_mode_ is an optional argument. If you do not provide a value, XMATCH will default to an exact match. The table below shows the values you can use to set _match\_mode_:

| Match mode | Behavior |
| --- | --- |
| 0 (default) | Exact match. |
| \-1 | Exact match or next smaller item. |
| 1   | Exact match or next larger item. |
| 2   | [Wildcard match](https://exceljet.net/glossary/wildcard)<br> (\*, ?, ~) |
| 3   | Regex match |

> In December 2024, XMATCH was upgraded to allow a regex match in Excel 365. The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
>  was also updated to support regex. For more about regex in Excel, see [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
> .

### Search mode

The fourth argument for XMATCH is _search\_mode_. This is an _optional_ argument that controls search behavior as follows:

| Search mode | Behavior |
| --- | --- |
| 1 (default) | Search from the first value to the last |
| \-1 | Search from the last value to the first (reverse) |
| 2   | Binary search values sorted in ascending order (very fast) |
| \-2 | Binary search values sorted in descending order (very fast) |

> Binary searches are very fast, but take care data is sorted as required. If data is not sorted properly, a binary search can return invalid results that look perfectly normal.

### Exact match

In the worksheet below, XMATCH is used to get the position of "Mars" in a list of planets in the range B6:B13. The formula in G6 is:

    =XMATCH(G4,B5:B13) // returns 4
    

![XMATCH exact match example](https://exceljet.net/sites/default/files/images/functions/inline/xmatch_exact_match_example.png "XMATCH exact match example")

XMATCH _defaults_ to an exact match, so there is no need to enable this behavior.

### Match mode behavior

The example below illustrates match mode behavior with a lookup value of 3.1 and lookup values in B5:B11:

![XMATCH match mode examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/xmatch%20match%20mode%20bahavior.png?itok=0KexZV-Z "XMATCH match mode examples")

    E6=XMATCH(E4,B5:B11) // returns #N/A
    E7=XMATCH(E4,B5:B11,-1) // returns 3
    E8=XMATCH(E4,B5:B11,1) // returns 4
    

*   In cell E6, _match\_mode_ defaults to 0 (exact match) so the result is #N/A (not found).
*   In cell E7, _match\_mode_ is given as -1 (next smallest) so the result is 3.
*   In cell E8, match\_mode is given as 1 (next largest) so the result is 4.

### INDEX and XMATCH

XMATCH can be used just like MATCH in a normal INDEX and MATCH formula. To retrieve the diameter of Mars based on the original example above, the formula is:

    =INDEX(C6:C14,XMATCH(G5,B6:B14)) // returns 6792
    

For more information, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

### XMATCH with wildcard

When _match\_mode_ is set to 2, XMATCH can perform a match using [wildcards](https://exceljet.net/glossary/wildcard)
. In the example shown below, the formula in E5 is:

    =XMATCH(E4,B5:B13,2) // returns 6
    

This is equivalent to:

    =XMATCH("pq*",B5:B13,2)
    

![XMATCH with wildcard example](https://exceljet.net/sites/default/files/images/functions/inline/xmatch%20with%20wildcard%20example.png "XMATCH with wildcard example")

XMATCH locates the first code that begins with "pq" and returns 6 since PQR-121 appears in row 6 of the range B5:B13. Notice that XMATCH is _not_ case-sensitive.

### XMATCH with Regex

XMATCH can also match with "regex" (short for Regular Expressions). In the worksheet below, the goal is to look up the correct price of the product number entered in cell F4 using the product codes in column B. This problem is trickier than it looks. Each product code begins with 3 uppercase letters and ends with 2 or 3 uppercase letters. In the middle of the product code is a number between 2 and 4 digits. A wildcard match won't work because a number like 56 can appear inside _other product codes_. However, we can easily solve this problem with a "regex match". To enable a regex match in XMATCH, provide 3 for _match\_mode_. Then supply a valid regex pattern as the _lookup\_value_. In the worksheet below, the formula in cell F5 looks like this:

    =XMATCH("[A-Z]{3}"&F4&"[A-Z]{2,3}",B5:B16,3)

![XMATCH with regex example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/xmatch_regex_match_example.png "XMATCH with regex example")

The regex pattern in this formula is "\[A-Z\]{3}"&F4&"\[A-Z\]{2,3}". The translation is "3 uppercase letters A-Z, followed by the value in F4 (56), followed by 2-3 uppercase letters A-Z". Regex is a powerful and somewhat complex language. For a detailed explanation of the regex used in this example, see [XLOOKUP with regex](https://exceljet.net/formulas/xlookup-with-regex-match)
. XLOOKUP and XMATCH support regex in the same way. Although the functions are different, the regex pattern is exactly the same.

> Regex matching was added to XMATCH in December 2024, so this feature is only available in Excel 365. For an introduction to regex in Excel, see [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
> . 

### Multiple criteria

There is no built-in way to provide multiple criteria with XMATCH but you can use Boolean logic to apply multiple conditions. In the worksheet below, XMATCH is configured to apply 3 separate conditions to match the values for Item, Size, and Color entered in H5:H7.

![XMATCH with multiple criteria](https://exceljet.net/sites/default/files/images/functions/inline/XMATCH_with_multiple_criteria.png "XMATCH with multiple criteria")

For more details, [see this page](https://exceljet.net/formulas/xmatch-with-multiple-criteria)
.

### Case-sensitive match

The MATCH function is not case-sensitive. However, MATCH can be configured to perform a case-sensitive match when combined with the [EXACT function](https://exceljet.net/functions/exact-function)
 in a generic formula like this:

    =XMATCH(TRUE,EXACT(lookup_value,array),0))
    

The EXACT function compares every value in _array_ with the _lookup\_value_ in a case-sensitive manner. This formula is explained in an [INDEX and MATCH example here](https://exceljet.net/formulas/case-sensitive-lookup)
. The example uses the [MATCH function](https://exceljet.net/functions/match-function)
, but XMATCH can be substituted with the same result.

### Binary search

XMATCH has a binary search option that runs _very quickly_. To enable binary search mode, data must be sorted in ascending or descending order. If values are sorted in _ascending order_, use the value 2 for _search\_mode_. If values are sorted in _descending order_, use the value -2. Below is the generic syntax to enable binary search mode for an exact match lookup:

    =XMATCH(value,array,0,2) // binary search A-Z
    =XMATCH(value,array,0,-2) // binary search Z-A
    

For a more detailed example, see [this page](https://exceljet.net/formulas/xlookup-binary-search)
. The primary example is based on the XLOOKUP function but the explanation shows how to use INDEX and XMATCH to solve the same problem.

### Notes

1.  XMATCH can work with both vertical and horizontal arrays.
2.  XMATCH will return #N/A if the lookup value is not found.
3.  XMATCH defaults to an exact match, while MATCH defaults to an approximate match.
4.  XMATCH can find the next larger item _or_ the next smaller item.
5.  XMATCH can perform a reverse search (i.e. search from last to first).
6.  XMATCH does not require values to be sorted when performing an approximate match.
7.  XMATCH can perform a binary search, which is specifically optimized for speed.

XMATCH function examples
------------------------

[![Excel formula: XLOOKUP binary search](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_binary_search.png "Excel formula: XLOOKUP binary search")](https://exceljet.net/formulas/xlookup-binary-search)

### [XLOOKUP binary search](https://exceljet.net/formulas/xlookup-binary-search)

In this example, the goal is to look up amounts for 1000 invoice numbers in a table that contains 1 million invoices. The catch is that not all of the 1000 invoice numbers exist in the source data. In fact, most of the invoice numbers do not appear in column B . This means we need to take care to...

[![Excel formula: Extract common values from text strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_common_values_from_two_text_strings.png "Excel formula: Extract common values from text strings")](https://exceljet.net/formulas/extract-common-values-from-text-strings)

### [Extract common values from text strings](https://exceljet.net/formulas/extract-common-values-from-text-strings)

In this example, the goal is to extract common values from two text strings that contain comma-delimited values. In the worksheet shown the values for "List1" appear in column B and the values for "List2" appear in column C. The results in column D show the intersection of the two lists, that is,...

[![Excel formula: INDEX and MATCH with variable columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_with_variable_columns.png "Excel formula: INDEX and MATCH with variable columns")](https://exceljet.net/formulas/index-and-match-with-variable-columns)

### [INDEX and MATCH with variable columns](https://exceljet.net/formulas/index-and-match-with-variable-columns)

In this example, the goal is to demonstrate how an INDEX and (X)MATCH formula can be set up so that the columns returned are variable. This approach illustrates one benefit of the 2-step process used by INDEX and MATCH: Because INDEX expects a numeric index for row and column numbers, it is easy to...

[![Excel formula: Nearest location with XMATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nearest%20location%20with%20XMATCH.png "Excel formula: Nearest location with XMATCH")](https://exceljet.net/formulas/nearest-location-with-xmatch)

### [Nearest location with XMATCH](https://exceljet.net/formulas/nearest-location-with-xmatch)

At the core, this formula is a basic INDEX and MATCH formula . However, instead of using the older MATCH function , we are using XMATCH function , which provides a more powerful match mode setting: =INDEX(location,XMATCH(0,distance,1)) Working from the inside out, we are using the XMATCH function...

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

[![Excel formula: Get last match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match.png "Excel formula: Get last match")](https://exceljet.net/formulas/get-last-match)

### [Get last match](https://exceljet.net/formulas/get-last-match)

In the example shown, we have a set of order data that includes Date, Product, Name, and Amount. The data is sorted by date in ascending order. The goal is to look up the latest order for a given person by Name. In other words, we want the last match by name. The challenge is that Excel lookup...

[![Excel formula: Cell contains specific words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_words.png "Excel formula: Cell contains specific words")](https://exceljet.net/formulas/cell-contains-specific-words)

### [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)

In this example, the goal is to test the text in a cell and return TRUE if it contains one or more specific words, and FALSE if not. Notice the emphasis here is on words, not substrings. For example, if we are testing for the word "green" and the text contains the word "evergreen" but not the word...

[![Excel formula: Extract common values from two lists](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_common_values_from_two_lists.png "Excel formula: Extract common values from two lists")](https://exceljet.net/formulas/extract-common-values-from-two-lists)

### [Extract common values from two lists](https://exceljet.net/formulas/extract-common-values-from-two-lists)

In this example, the goal is to compare the values in two different lists, then extract the values that appear in both lists into a third list as shown in the worksheet above. The values for List 1 appear in column B, and the values for List 2 appear in column D. Although we have a list of fruits...

[![Excel formula: XMATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XMATCH_with_multiple_criteria.png "Excel formula: XMATCH with multiple criteria")](https://exceljet.net/formulas/xmatch-with-multiple-criteria)

### [XMATCH with multiple criteria](https://exceljet.net/formulas/xmatch-with-multiple-criteria)

The goal is to match a row in a set of data based on a given Item, Size, and Color. At a glance, this seems like a difficult problem because XMATCH only has one value for lookup\_value and lookup\_array . How can we configure XMATCH to consider values from multiple columns? The trick is to generate...

[![Excel formula: GROUPBY with survey results](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/groupby_with_survey_results.png "Excel formula: GROUPBY with survey results")](https://exceljet.net/formulas/groupby-with-survey-results)

### [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)

In May 2025, I ran a survey asking Exceljet newsletter subscribers what version of Excel they use most. This is an important question for Excel learning because the new dynamic array engine has completely changed how many formulas are written. These changes started rolling out after Excel 2019, so...

[![Excel formula: INDEX and MATCH two-column lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_two-column_lookup.png "Excel formula: INDEX and MATCH two-column lookup")](https://exceljet.net/formulas/index-and-match-two-column-lookup)

### [INDEX and MATCH two-column lookup](https://exceljet.net/formulas/index-and-match-two-column-lookup)

In this example, the goal is to look up Width and Length based on inputs for Code (K6) and Size (K7). While finding the correct row based on the Code value is straightforward, the problem of how to best retrieve both columns of data (Width and Length) is more challenging. One good way to solve this...

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

[![Excel formula: XMATCH reverse search](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XMATCH%20reverse%20search.png "Excel formula: XMATCH reverse search")](https://exceljet.net/formulas/xmatch-reverse-search)

### [XMATCH reverse search](https://exceljet.net/formulas/xmatch-reverse-search)

The XMATCH function offers new features not available with the MATCH function. One of these is the ability to perform a "reverse search", by setting the optional search mode argument. The default value for search mode is 1, which specifies a normal "first to last" search. In this mode, XMATCH will...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

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

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

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

*   [Get last match](https://exceljet.net/formulas/get-last-match)
    
*   [XMATCH with multiple criteria](https://exceljet.net/formulas/xmatch-with-multiple-criteria)
    
*   [XLOOKUP binary search](https://exceljet.net/formulas/xlookup-binary-search)
    
*   [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)
    
*   [INDEX and MATCH two-column lookup](https://exceljet.net/formulas/index-and-match-two-column-lookup)
    
*   [Extract common values from two lists](https://exceljet.net/formulas/extract-common-values-from-two-lists)
    
*   [INDEX and MATCH with variable columns](https://exceljet.net/formulas/index-and-match-with-variable-columns)
    
*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    
*   [Extract common values from text strings](https://exceljet.net/formulas/extract-common-values-from-text-strings)
    
*   [XMATCH reverse search](https://exceljet.net/formulas/xmatch-reverse-search)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    
*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

### Links

*   [Microsoft XMATCH function documentation](https://support.office.com/en-us/article/xmatch-function-d966da31-7a6b-4a13-a1c6-5a33ed6a0312)
    

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