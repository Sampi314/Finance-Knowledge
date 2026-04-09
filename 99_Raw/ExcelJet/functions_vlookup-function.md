# Excel VLOOKUP function | Exceljet

**Source:** https://exceljet.net/functions/vlookup-function

---

[Skip to main content](https://exceljet.net/functions/vlookup-function#main-content)

[](https://exceljet.net/functions/vlookup-function#)

*   [Previous](https://exceljet.net/functions/transpose-function)
    
*   [Next](https://exceljet.net/functions/char-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

VLOOKUP Function
================

by Dave Bruns · Updated 9 Jul 2025

Related functions 
------------------

[HLOOKUP](https://exceljet.net/functions/hlookup-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[FILTER](https://exceljet.net/functions/filter-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7750/download?token=LDCLVtEW)
 (52.74 KB)

![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")

Summary
-------

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches.

Purpose 
--------

Look up and retrieve a value in a table

Return value 
-------------

A value from the given column number

Syntax
------

    =VLOOKUP(lookup_value,table_array,column_index_num,[range_lookup])

*   _lookup\_value_ - The value to look for in the first column of a table.
*   _table\_array_ - The table from which to retrieve a value.
*   _column\_index\_num_ - The column in the table from which to retrieve a value.
*   _range\_lookup_ - \[optional\] TRUE = approximate match (default). FALSE = exact match.

Using the VLOOKUP function 
---------------------------

The Excel VLOOKUP function scans the first column in a table, finds a match, and returns a result from the same row. If VLOOKUP can't find a match, it returns a #N/A error or an "approximate match", depending on how it is configured. Because VLOOKUP is easy to use and has been in Excel for decades, it is the most popular function in Excel for basic lookups. You will find it in all kinds of worksheets in almost any business or industry. Although VLOOKUP is simple to configure, it has some default behaviors that can be dangerous in certain situations.

### Key features

*   Looks up values in the _first column_ of a vertical table
*   Returns data from _any column to the right of the lookup column_
*   Supports exact match and approximate match modes
*   Approximate match is the default (dangerous if exact match expected)
*   Supports wildcards (\* ?) for partial matching (exact match mode only)
*   Is not case-sensitive
*   Returns first match if duplicates exist
*   Works in all versions of Excel

### Table of contents

*   [VLOOKUP works with vertical data](https://exceljet.net/functions/vlookup-function#vertical_data)
    
*   [VLOOKUP uses column numbers](https://exceljet.net/functions/vlookup-function#column_numbers)
    
*   [VLOOKUP only looks right](https://exceljet.net/functions/vlookup-function#only_looks_right)
    
*   [VLOOKUP has 2 matching modes](https://exceljet.net/functions/vlookup-function#matching_modes)
    
*   [VLOOKUP exact match example](https://exceljet.net/functions/vlookup-function#exact_match)
    
*   [VLOOKUP approximate match example](https://exceljet.net/functions/vlookup-function#approximate_match)
    
*   [VLOOKUP has dangerous defaults](https://exceljet.net/functions/vlookup-function#dangerous_default)
    
*   [VLOOKUP returns the first match](https://exceljet.net/functions/vlookup-function#first_match)
    
*   [VLOOKUP with a wildcard match](https://exceljet.net/functions/vlookup-function#wildcard_match)
    
*   [VLOOKUP with a two-way lookup](https://exceljet.net/functions/vlookup-function#two_way_lookup)
    
*   [VLOOKUP with multiple criteria](https://exceljet.net/functions/vlookup-function#multiple_criteria)
    
*   [Handling VLOOKUP #N/A errors](https://exceljet.net/functions/vlookup-function#na_error)
    
*   [VLOOKUP performance tips](https://exceljet.net/functions/vlookup-function#vlookup_performance_tips)
    
*   [More about VLOOKUP](https://exceljet.net/functions/vlookup-function#more_about_vlookup)
    

> Important: _VLOOKUP performs an approximate match by default_. See [below](https://exceljet.net/functions/vlookup-function#matching_modes)
>  for details.

### VLOOKUP works with vertical data

The "V" in VLOOKUP is for "Vertical". The purpose of VLOOKUP is to look up and retrieve information in a table _organized vertically_:

![VLOOKUP is for vertical data](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20is%20for%20vertical%20data_0.png "VLOOKUP is for vertical data")

For example, with the table above, you can use VLOOKUP to find the amount for a given order like this:

![VLOOKUP is for vertical data - example](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP_is_for_vertical_data_example.png "VLOOKUP is for vertical data - example")

With the order number 1005 as a lookup value in cell I4, the result is 125. VLOOKUP scans the first column of the table, matches order number 1005, and returns 125, the amount. The formula in cell I5 is:

    =VLOOKUP(I4,B5:F9,3,FALSE)

For now, just pay attention to these things:

1.  The lookup value is provided as I4. If this value is changed, VLOOKUP will return a new result.
2.  The lookup table is provided as the range B5:F9, which is the entire table.
3.  The lookup values (order numbers) are in the first column of the table.
4.  The result values (order amounts) are in the third column of the table.
5.  The column index number is given as 3.

### VLOOKUP uses column numbers

The VLOOKUP function uses column numbers to indicate the column from which a value should be retrieved. When you use VLOOKUP, imagine that every column in the table is numbered, starting at 1:

![VLOOKUP is based on column numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/VLOOKUP%20is%20based%20on%20column%20numbers.png?itok=5mtE7ZnS "VLOOKUP is based on column numbers.png")

To retrieve a value from a given column, just provide the number for _column\_index\_num_. For example, to retrieve the first name in cell H4, we use 2 for _column\_index\_num_, as seen above. By changing only the column number, we can retrieve the first name, last name, and email address by asking for columns 2, 3, and 4:

    =VLOOKUP(H3,B4:E13,2,FALSE) // first name
    =VLOOKUP(H3,B4:E13,3,FALSE) // last name
    =VLOOKUP(H3,B4:E13,4,FALSE) // email address
    

Notice that the _only_ difference in the formulas above is the _column number_.

To see a short demo, watch this 3-minute video: [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

### VLOOKUP only looks right

VLOOKUP can only look to the right. In other words, you can only retrieve data _to the right_ of the first column in the table provided to VLOOKUP. For example, to look up information by ID in the table below, we must provide the range D3:F9 as the table, and that means we can only look up Email and Department:

![VLOOKUP can only look to the right](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20only%20looks%20right.png "VLOOKUP can only look to the right")

This is a fundamental limitation of VLOOKUP — the first column of the table must contain lookup values, and VLOOKUP can only access columns to the right. To retrieve information to the left (or right) of a lookup column, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 or an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula.

### VLOOKUP has 2 matching modes

VLOOKUP has two match modes: exact match and approximate match. The last argument, called _range\_lookup_, controls which match mode is used. The word "range" in this case refers to "range of values" – when _range\_lookup_ is TRUE, VLOOKUP will match a _range of values_ rather than an exact value. When _range\_lookup_ is FALSE, VLOOKUP will only allow an exact match:

    =VLOOKUP(value,table,col_index,TRUE) // approximate match
    =VLOOKUP(value,table,col_index,FALSE) // exact match
    

> _Pro tip: You can also supply zero (0) for an exact match, and 1 for an approximate match. Excel will evaluate 0 as FALSE and 1 as TRUE, so 0 and 1 are more compact equivalents._

### VLOOKUP exact match example

In most cases, you'll probably want to use VLOOKUP in exact match mode. This makes sense when you have a unique key to use as a lookup value, for example, the movie title in this data:

![VLOOKUP exact match with movies](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20exact%20match%20example%20movies.png "VLOOKUP exact match with movies")

The formula in H6 to find Year, based on an exact match of the movie title, is:

    =VLOOKUP(H4,B5:E9,2,FALSE) // FALSE = exact match
    

With "Toy Story" in H4, VLOOKUP finds a match in the fourth row in the table and returns 1995 as a result.

Video: [How to use VLOOKUP for an exact match](https://exceljet.net/videos/how-to-use-vlookup)

### VLOOKUP approximate match example

In some cases, you will need an _approximate match_ lookup instead of an _exact match_ lookup. A good example is the problem of assigning a letter grade based on a score. In the worksheet below, we want to use the scores in column C to assign a grade using the table to the right in the range F5:G9, which is [named](https://exceljet.net/glossary/named-range)
 "key". Here, we need to use VLOOKUP in _approximate match_ mode, because in most cases, the exact score in column C will _not be found_ in column F. The VLOOKUP formula in D5 is configured to perform an _approximate match_ by setting the last argument to TRUE:

    =VLOOKUP(C5,$G$5:$H$10,2,TRUE) // TRUE = approximate match
    

![VLOOKUP approximate match to calculate grades](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP_approximate_match_for_grades.png "VLOOKUP approximate match to calculate grades")

As the formula is copied down, VLOOKUP will scan values in column F looking for the score in column C. If an exact match is found, VLOOKUP will return the corresponding grade in that row. If an exact match is _not found_, VLOOKUP will stop at the first larger score, then "step back" and return the grade from the _previous row_.

> Caution: for an approximate match, the table provided to VLOOKUP _must be sorted in ascending order by the first column_. If the table is not sorted, VLOOKUP may return incorrect or unexpected results, as explained in the next section.

Video: [How to use VLOOKUP for approximate match](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### VLOOKUP has dangerous defaults

It is important to understand that VLOOKUP will perform an approximate match by default. This happens because _range\_lookup_ is optional and _defaults to TRUE_. This can cause big problems if you expect an exact match, as seen in the worksheet below. Here, the goal is to look up the amount for a given invoice number in cell F5. The formula in G5 is:

    =VLOOKUP(F5,B5:D10,3) // approximate by default!
    

No value has been provided for range\_lookup, so VLOOKUP performs an approximate match. Notice that invoice number 100235 _does not exist in the data_, but VLOOKUP returns 12,000. This happens because VLOOKUP scans the table until it reaches invoice 100236, then it "steps back" to invoice 100234 and returns the (incorrect) amount in that row:

![VLOOKUP default match mode is dangerous](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/VLOOKUP_default_match_mode_is_dangerous.png "VLOOKUP default match mode is dangerous")

To fix this problem, enable exact matching by providing range\_lookup as FALSE or 0:

    =VLOOKUP(F5,B5:D10,3,FALSE) // exact match
    

This will cause VLOOKUP to return an #N/A error when an invoice number doesn't exist. If you like, you can use the IFNA function to return a more friendly result, as explained below.

> The bottom line: If you don't supply a value for _range\_lookup_, VLOOKUP _will perform an approximate match_. In this mode, VLOOKUP can return results that _look fine_ but are in fact totally incorrect. For this reason, I recommend that you always set a value for _range\_lookup_ as a reminder of what you expect.

### VLOOKUP returns the first match

If there is more than one matching value in a table, VLOOKUP will only find the _first match_. In the screen below, VLOOKUP is configured to get the price for the color "Green". There are three rows with the color Green, and VLOOKUP returns the price in the _first_ row, which is $17.00. The formula in cell F5 is:

    =VLOOKUP(E5,B5:C11,2,FALSE) // returns 17
    

![VLOOKUP returns first match](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20first%20match.png "VLOOKUP returns first match")

To retrieve the _last match_ in a set of data, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 configured to perform a "reverse search". To retrieve _all matches_, use the [FILTER function](https://exceljet.net/functions/filter-function)
.

### VLOOKUP with a wildcard match

The VLOOKUP function supports [wildcards](https://exceljet.net/glossary/wildcard)
, which makes it possible to perform a partial match on a lookup value. To use wildcards with VLOOKUP, you must provide FALSE or zero (0) for _range\_lookup_. In the screen below, the formula in H7 retrieves the first name, "Michael", after typing "Aya" into cell H4. Notice the asterisk (\*) wildcard is [concatenated](https://exceljet.net/glossary/concatenation)
 to the lookup value inside the VLOOKUP formula:

    =VLOOKUP($H$4&"*",$B$5:$E$104,2,FALSE)
    

![VLOOKUP wildcard match](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20wildcard%20match.png "VLOOKUP wildcard match")

For a full explanation of this formula, see [this example](https://exceljet.net/formulas/partial-match-with-vlookup)
.

Video: [How to use VLOOKUP for wildcard matches](https://exceljet.net/videos/how-to-use-vlookup-for-wildcard-matches)

### VLOOKUP with a two-way lookup

Inside the VLOOKUP function, _column\_index\_num_ is normally hard-coded as a static number. However, you can create a _dynamic column index_ by using the [MATCH function](https://exceljet.net/functions/match-function)
 to locate the desired column. This technique allows you to create a dynamic two-way lookup, matching on both rows _and_ columns. In the screen below, VLOOKUP is configured to perform a lookup based on Name and Month like this:

    =VLOOKUP(H4,B5:E13,MATCH(H5,B4:E4,0),0)
    

![VLOOKUP two-way lookup](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20two-way%20lookup.png "VLOOKUP two-way lookup")

MATCH locates "Feb" in the range B4:E4 and returns 3 to VLOOKUP as the column number. For more details, [see this example](https://exceljet.net/formulas/vlookup-two-way-lookup)
.

_Note: In general,_ [_INDEX and MATCH_](https://exceljet.net/articles/index-and-match)
 _is a more flexible way to_ [_perform two-way lookups_](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
_._

### VLOOKUP with multiple criteria

The VLOOKUP function does not handle multiple criteria natively. However, you can use a [helper column](https://exceljet.net/glossary/helper-column)
 to join multiple fields together and use these fields as multiple criteria inside VLOOKUP. In the example below, Column B is a helper column that [concatenates](https://exceljet.net/glossary/concatenation)
 first and last names together with this formula:

    =C5&D5 // helper column
    

VLOOKUP is configured to do the same thing to create a lookup value. The formula in H6 is:

    =VLOOKUP(H4&H5,B5:E13,4,0)
    

![VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20with%20multiple%20criteria.png "VLOOKUP with multiple criteria")

For details, [see this example](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
. For a more advanced, flexible approach, [see this example](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)
.

_Note:_ [_INDEX and MATCH_](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
 _and_ [_XLOOKUP_](https://exceljet.net/functions/xlookup-function)
 _are better for lookups based on multiple criteria._

### Handling VLOOKUP #N/A errors

If you use VLOOKUP, you will inevitably run into the #N/A error. The #N/A error simply means "not found". For example, in the screen below, the lookup value "Toy Story 2" does not exist in the lookup table, and all three VLOOKUP formulas return #N/A:

![VLOOKUP #N/A error example](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20na%20error%20example.png "VLOOKUP #N/A error example")

The #N/A error is useful because it tells you something is wrong. There are several reasons why VLOOKUP might return an #N/A error, including:

*   The lookup value does not exist in the table
*   The lookup value is misspelled or contains extra spaces
*   Match mode is exact, but should be approximate
*   The table range is not entered correctly
*   The formula was copied, and the table [reference is not locked](https://exceljet.net/glossary/absolute-reference)
    

To "trap" the NA error and return a custom value, you can use the [IFNA function](https://exceljet.net/functions/ifna-function)
 like this:

![VLOOKUP #N/A error example - fixed](https://exceljet.net/sites/default/files/images/functions/inline/VLOOKUP%20na%20error%20fixed%20example.png "VLOOKUP #N/A error example - fixed")

The formula in H6 is:

    =IFNA(VLOOKUP(H4,B5:E9,2,FALSE),"Not found")
    

The message can be customized as desired. To return nothing (i.e., to display a blank result) when VLOOKUP returns #N/A you can use an [empty string](https://exceljet.net/glossary/empty-string)
 ("") like this:

    =IFNA(VLOOKUP(H4,B5:E9,2,FALSE),"") // no message
    

You can also use the [IFERROR function](https://exceljet.net/functions/iferror-function)
 to trap VLOOKUP #N/A errors. However, use caution with IFERROR, because it will catch _any error_, not just the #N/A error. Read more: [VLOOKUP without #N/A errors](https://exceljet.net/formulas/vlookup-without-na-error)

Video: [What to do when VLOOKUP returns #N/A](https://exceljet.net/videos/what-to-do-when-vlookup-returns-na)

### VLOOKUP performance tips

VLOOKUP in exact match mode can be slow on large data sets. On the other hand, VLOOKUP in approximate match mode is very fast, but dangerous if you need an exact match because it might return an incorrect value. In a modern version of Excel, the easiest fix is to switch to a function like [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, which has built-in support for a super-fast binary search. You could also use INDEX and XMATCH, since XMATCH also has the fast binary search option. If you are stuck in an older version of Excel without XLOOKUP or XMATCH, another option is to create a fast exact match formula by using [VLOOKUP twice](https://exceljet.net/formulas/vlookup-faster-vlookup)
. This is a cool trick, but I wouldn't use this approach unless it is your only option. I would also avoid using [full column references](https://exceljet.net/glossary/full-column-reference)
 like A:A with VLOOKUP. Since an Excel workbook contains over 1 million rows, using full column references can cause major performance problems in certain cases by making Excel process millions of extra cells.

### More about VLOOKUP

*   [VLOOKUP with multiple criteria (basic)](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
    
*   [VLOOKUP with multiple criteria (advanced)](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)
    
*   [How to use VLOOKUP to merge tables](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)
    
*   [23 tips for using VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    
*   [More VLOOKUP examples and videos](https://exceljet.net/functions/vlookup-function#related-info)
    
*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)
    

### Notes

*   VLOOKUP performs an approximate match by default.
*   VLOOKUP is not case-sensitive.
*   _Range\_lookup_ controls matching. FALSE = exact, TRUE = approximate (default).
*   If _range\_lookup_ is omitted or TRUE:
    *   VLOOKUP will match the nearest value equal to or _less than the lookup\_value**.**_
    *   Column 1 of _table\_array_ must be sorted in ascending order.
*   If _range\_lookup_ is FALSE or zero for an exact match:
    *   VLOOKUP will perform an exact match.
    *   The _table\_array_ does not need to be sorted.

VLOOKUP function examples
-------------------------

[![Excel formula: VLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20muliple%20criteria.png "Excel formula: VLOOKUP with multiple criteria")](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

### [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)

In the example shown, we want to look up employee departments and groups using VLOOKUP by matching the first and last name of an employee. One limitation of VLOOKUP is that it only handles one condition: the lookup\_value, which is matched against the first column in the table. This makes it...

[![Excel formula: Detailed LET function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/let%20function%20example.png "Excel formula: Detailed LET function example")](https://exceljet.net/formulas/detailed-let-function-example)

### [Detailed LET function example](https://exceljet.net/formulas/detailed-let-function-example)

In this example, we have a simple set of data in B5:D16 that includes ID, Name, and Points. The goal is to generate a custom message for any name in the list by entering a valid ID in cell G5. The message uses the name from column C and the points in column D like this: "Hi \[name\], you have \[points...\
\
[![Excel formula: VLOOKUP with multiple criteria advanced](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20multiple%20criteria%20advanced.png "Excel formula: VLOOKUP with multiple criteria advanced")](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)\
\
### [VLOOKUP with multiple criteria advanced](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)\
\
In this example, the goal is to use VLOOKUP to retrieve the price for a given item based on three criteria: name, size, and color, which are entered in H5:H7. For example, for a Blue Medium T-shirt, VLOOKUP should return $16.00. The VLOOKUP function does not handle multiple criteria natively...\
\
[![Excel formula: VLOOKUP with 2 lookup tables](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20two%20lookup%20tables.png "Excel formula: VLOOKUP with 2 lookup tables")](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)\
\
### [VLOOKUP with 2 lookup tables](https://exceljet.net/formulas/vlookup-with-2-lookup-tables)\
\
Working from the inside out, the IF function in this formula, which is entered as the "table\_array" argument in VLOOKUP, runs a logical test on the value in column C "Years", which represents the number of years a salesperson has been with a company. If C5 is less than 2, then table1 is returned as...\
\
[![Excel formula: Map text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20text%20to%20numbers.png "Excel formula: Map text to numbers")](https://exceljet.net/formulas/map-text-to-numbers)\
\
### [Map text to numbers](https://exceljet.net/formulas/map-text-to-numbers)\
\
This formula uses the value in cell F7 for a lookup value, the range B6:C10 for the lookup table, the number 2 to indicate "2nd column", and zero as the last argument to force an exact match. Although in this case we are mapping text values to numeric outputs, the same formula can handle text to...\
\
[![Excel formula: VLOOKUP with two client rates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20two%20client%20rates.png "Excel formula: VLOOKUP with two client rates")](https://exceljet.net/formulas/vlookup-with-two-client-rates)\
\
### [VLOOKUP with two client rates](https://exceljet.net/formulas/vlookup-with-two-client-rates)\
\
This formula is composed of two lookups for the same client. The first lookup finds the onsite rate for the client in column B and multiplies the result by the number of hours in column C: =VLOOKUP(B5,rates,2,0)\*C5 The second lookup finds the offsite rate for same client and multiplies the result...\
\
[![Excel formula: Self-contained VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/self-contained%20VLOOKUP%20formula2.png "Excel formula: Self-contained VLOOKUP")](https://exceljet.net/formulas/self-contained-vlookup)\
\
### [Self-contained VLOOKUP](https://exceljet.net/formulas/self-contained-vlookup)\
\
The goal in this example is to create a self-contained lookup formula to assign a grade to the score in cell E7, based on the table in B6:C10. However, instead of providing B6:B10 as a reference for the table\_array argument, the table is provided as a constant . Normally, the second argument for...\
\
[![Excel formula: Build hyperlink with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/build%20hyperlink%20with%20VLOOKUP.png "Excel formula: Build hyperlink with VLOOKUP")](https://exceljet.net/formulas/build-hyperlink-with-vlookup)\
\
### [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)\
\
The hyperlink function allows you to create a working link with a formula. It takes two arguments: link\_location and, optionally, friendly\_name . Working from the inside out, VLOOKUP looks up and retrieves a link value from column 2 of the named range "link\_table" (B5:C8). The lookup value comes...\
\
[![Excel formula: If else](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_else.png "Excel formula: If else")](https://exceljet.net/formulas/if-else)\
\
### [If else](https://exceljet.net/formulas/if-else)\
\
The goal is to return "Small" when the value in column D is "S" and "Large" when the value in column D is "L". In other words, if the value in column D is "S" return "Small" else return "Large". If else in Excel The concept of "If else" in Excel is handled with the IF function . The IF function...\
\
[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)\
\
### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)\
\
In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...\
\
[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)\
\
### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)\
\
In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...\
\
[![Excel formula: VLOOKUP by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20by%20date.png "Excel formula: VLOOKUP by date")](https://exceljet.net/formulas/vlookup-by-date)\
\
### [VLOOKUP by date](https://exceljet.net/formulas/vlookup-by-date)\
\
This is a standard VLOOKUP formula. It requires a table with lookup values (in this case, dates) to the left of the values being retrieved. The lookup value comes from cell E6, which must be a valid date. The table array is the range B6:C11, and the column index is 2, since the amounts are in the...\
\
[![Excel formula: Get nth match with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_match_with_VLOOKUP.png "Excel formula: Get nth match with VLOOKUP")](https://exceljet.net/formulas/get-nth-match-with-vlookup)\
\
### [Get nth match with VLOOKUP](https://exceljet.net/formulas/get-nth-match-with-vlookup)\
\
The table contains basic order information, with columns for Date, Product, Name, and Amount. The Helper column is used to create a special lookup value, as explained below. The goal is to retrieve the nth matching record in a table for a specific product, which is entered in cell I4. For example,...\
\
[![Excel formula: Multiple chained VLOOKUPs](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/chained%20lookups%20with%20VLOOKUP.png "Excel formula: Multiple chained VLOOKUPs")](https://exceljet.net/formulas/multiple-chained-vlookups)\
\
### [Multiple chained VLOOKUPs](https://exceljet.net/formulas/multiple-chained-vlookups)\
\
The IFERROR function is designed to trap errors and perform an alternate action when an error is detected. The VLOOKUP function will throw an #N/A error when a value isn't found. By nesting multiple VLOOKUPs inside the IFERROR function, the formula allows for sequential lookups. If the first...\
\
[![Excel formula: XLOOKUP wildcard contains substring](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_wildcard_contains_substring.png "Excel formula: XLOOKUP wildcard contains substring")](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)\
\
### [XLOOKUP wildcard contains substring](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)\
\
The goal is to look up the Title, Author, and Year in the list of books as shown using a formula based on a partial match and a wildcard. The text string to search for is entered in cell G4. All data is in an Excel Table named data in the range B5:D16. This problem can be easily solved with the...\
\
VLOOKUP function videos\
-----------------------\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20troubleshoot%20VLOOKUP%20approximate%20match-thumb.png)](https://exceljet.net/videos/how-to-troubleshoot-vlookup-approximate-match)\
\
### [How to troubleshoot VLOOKUP approximate match](https://exceljet.net/videos/how-to-troubleshoot-vlookup-approximate-match)\
\
When you're using VLOOKUP for approximate matches, you're not as likely to run into the problem of values not being found. However, you still need to understand how approximate matches work. Here's the commission example we looked at earlier which uses VLOOKUP to find approximate matches in a named...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20to%20merge%20tables-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)\
\
### [How to use VLOOKUP to merge tables](https://exceljet.net/videos/how-to-use-vlookup-to-merge-tables)\
\
In this video I'll demonstrate how you can use VLOOKUP to join data in separate tables. In this worksheet we have two tables. In the first table, we have order data. You can see that we've got a date, customer id, product, and total. In a second sheet we have customer data. We've got first and last...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)\
\
### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)\
\
VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20to%20do%20when%20VLOOKUP%20returns%20NA-thumb.png)](https://exceljet.net/videos/what-to-do-when-vlookup-returns-na)\
\
### [What to do when VLOOKUP returns NA](https://exceljet.net/videos/what-to-do-when-vlookup-returns-na)\
\
When you start using VLOOKUP , you'll often run into situations where VLOOKUP can't find a match and displays an error. In this video we'll look how to avoid and handle that situation. Here we have a VLOOKUP example we've looked at previously which uses VLOOKUP to retrieve employee information...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)\
\
### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)\
\
In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20group%20a%20pivot%20table%20by%20day%20of%20week-thumb.png)](https://exceljet.net/videos/how-to-group-a-pivot-table-by-day-of-week)\
\
### [How to group a pivot table by day of week](https://exceljet.net/videos/how-to-group-a-pivot-table-by-day-of-week)\
\
Pivot tables are very good at grouping dated information. You can group by year, by month, by quarter, and even by day and hour. But if you want to group by something like day of week, you'll need to do a little prep work in the source data first. Let's take a look. Here we have some raw data for...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20with%20a%20table-Thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-with-a-table)\
\
### [How to use VLOOKUP with a table](https://exceljet.net/videos/how-to-use-vlookup-with-a-table)\
\
In this video, we'll look at how to use VLOOKUP to lookup values in an Excel Table. On this worksheet, I have a table that contains employee data, named Table1. To illustrate how to work with VLOOKUP when the source data is in a table, I'll set up formulas to the right to extract data from the...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20select%20arguments%20with%20the%20formula%20tip%20window-thumb.png)](https://exceljet.net/videos/how-to-select-arguments-with-the-formula-tip-window)\
\
### [How to select arguments with the formula tip window](https://exceljet.net/videos/how-to-select-arguments-with-the-formula-tip-window)\
\
Function screen tips are a great way to navigate and select function arguments. Let's take a look. Whenever you enter or edit a formula that contains a function, the function tip window appears. The location that the function tip window appears in depends on where you're editing the formula. If you...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20VLOOKUP%20is%20better%20than%20nested%20IFs-thumb.png)](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)\
\
### [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)\
\
In this video we look at a few reasons why VLOOKUP is a better option than nested IF statements. In our last video, we used nested IF statements to calculate a commission rate based on a sales number. As a quick recap: The first formula is created with nested IF statements normally. The second...\
\
[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Structured%20references%20inside%20a%20table-Thumb.png)](https://exceljet.net/videos/structured-references-inside-a-table)\
\
### [Structured references inside a table](https://exceljet.net/videos/structured-references-inside-a-table)\
\
In this video, we'll take a look at structured reference syntax inside a table. Inside a table, structured references work a lot like structured references outside a table, except the table name is not used when it's implied. To illustrate, let's look at some examples. The formula to calculate the...\
\
Related functions\
-----------------\
\
[![Excel HLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hlookup%20function.png "Excel HLOOKUP function")](https://exceljet.net/functions/hlookup-function)\
\
### [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)\
\
The Excel HLOOKUP function finds and retrieve a value from data in a horizontal table. The "H" in HLOOKUP stands for "horizontal", and lookup values must appear in the first row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and...\
\
[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)\
\
### [LOOKUP Function](https://exceljet.net/functions/lookup-function)\
\
The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.\
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
[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)\
\
### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)\
\
The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....\
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
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)\
    \
*   [VLOOKUP with multiple criteria advanced](https://exceljet.net/formulas/vlookup-with-multiple-criteria-advanced)\
    \
*   [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)\
    \
*   [VLOOKUP from another sheet](https://exceljet.net/formulas/vlookup-from-another-sheet)\
    \
*   [Group numbers with VLOOKUP](https://exceljet.net/formulas/group-numbers-with-vlookup)\
    \
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)\
    \
*   [VLOOKUP with multiple criteria](https://exceljet.net/formulas/vlookup-with-multiple-criteria)\
    \
*   [Reverse VLOOKUP example](https://exceljet.net/formulas/reverse-vlookup-example)\
    \
*   [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)\
    \
*   [Due date by category](https://exceljet.net/formulas/due-date-by-category)\
    \
\
### Videos\
\
*   [How to group a pivot table by day of week](https://exceljet.net/videos/how-to-group-a-pivot-table-by-day-of-week)\
    \
*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)\
    \
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)\
    \
*   [What to do when VLOOKUP returns NA](https://exceljet.net/videos/what-to-do-when-vlookup-returns-na)\
    \
*   [How to use VLOOKUP for wildcard matches](https://exceljet.net/videos/how-to-use-vlookup-for-wildcard-matches)\
    \
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)\
    \
*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)\
    \
*   [How to troubleshoot VLOOKUP approximate match](https://exceljet.net/videos/how-to-troubleshoot-vlookup-approximate-match)\
    \
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)\
    \
*   [How to group values with VLOOKUP](https://exceljet.net/videos/how-to-group-values-with-vlookup)\
    \
\
### Functions\
\
*   [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)\
    \
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)\
    \
*   [INDEX Function](https://exceljet.net/functions/index-function)\
    \
*   [MATCH Function](https://exceljet.net/functions/match-function)\
    \
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)\
    \
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)\
    \
*   [FILTER Function](https://exceljet.net/functions/filter-function)\
    \
\
### Articles\
\
*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)\
    \
*   [Danger: beware VLOOKUP defaults](https://exceljet.net/articles/danger-beware-vlookup-defaults)\
    \
*   [XLOOKUP vs VLOOKUP](https://exceljet.net/articles/xlookup-vs-vlookup)\
    \
\
### Links\
\
*   [Microsoft VLOOKUP function documentation](https://support.office.com/en-us/article/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1)\
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