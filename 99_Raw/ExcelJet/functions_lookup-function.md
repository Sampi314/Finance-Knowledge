# Excel LOOKUP function | Exceljet

**Source:** https://exceljet.net/functions/lookup-function

---

[Skip to main content](https://exceljet.net/functions/lookup-function#main-content)

[](https://exceljet.net/functions/lookup-function#)

*   [Previous](https://exceljet.net/functions/indirect-function)
    
*   [Next](https://exceljet.net/functions/match-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

LOOKUP Function
===============

by Dave Bruns · Updated 14 Mar 2025

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[HLOOKUP](https://exceljet.net/functions/hlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")

Summary
-------

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

Purpose 
--------

Look up a value in a one-column range

Return value 
-------------

A value in the result vector.

Syntax
------

    =LOOKUP(lookup_value,lookup_vector,[result_vector])

*   _lookup\_value_ - The value to search for.
*   _lookup\_vector_ - The array or range to search.
*   _result\_vector_ - \[optional\] The array or range to return.

Using the LOOKUP function 
--------------------------

The LOOKUP function is one of the original lookup functions in Excel. You can use LOOKUP to look up a value in one range or array and return the corresponding value from another range or array. Like the newer XLOOKUP function, LOOKUP can look up values in either rows or columns. However, unlike XLOOKUP, LOOKUP can only perform an approximate match. 

LOOKUP has certain default behaviors that make it useful for solving [tricky problems](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
 in Excel:

1.  LOOKUP always performs an approximate match.
2.  LOOKUP assumes that the _lookup\_vector_ is sorted in ascending order.
3.  LOOKUP can look up values in vertical or horizontal ranges/arrays.
4.  When LOOKUP can't find an exact match, it matches the next smallest value.
5.  It can handle some array operations without control + shift + enter (in older versions of Excel).

Here is an example of a traditionally difficult problem that LOOKUP has been able to solve for many years: [Get value of last non-empty cell.](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
 With the introduction of new power functions like XLOOKUP and XMATCH, LOOKUP is not as important as it was in the past, but if you must use an old version of Excel, LOOKUP can still be quite useful.

The LOOKUP function accepts three arguments: _lookup\_value, lookup\_vector,_ and _result\_vector._ The first argument, _lookup\_value,_ is the value to look for. The second argument, _lookup\_vector_, is the range or array to search. The third argument, result\_vector, is the range or array from which to return a result. _Result\_vector_ is optional. If _result\_vector_ is _not_ provided, LOOKUP returns the _value_ of the match found in _lookup\_vector_. The LOOKUP function has two forms: vector and array. Most of this article describes the _vector_ form, but the last example below explains the _array_ form.

### Example #1 - basic usage

In the example shown above, the formula in cell F5 returns the value of the match found in column B. Note that _result\_vector_ is not provided:

    =LOOKUP(F4,B5:B9) // returns match in level
    

The formula in cell F6 returns the corresponding Tier value from column C. Notice in this case, both _lookup\_vector_ and _result\_vector_ are provided:

    =LOOKUP(F4,B5:B9,C5:C9) // returns corresponding tier
    

In both formulas, LOOKUP _automatically_ performs an approximate match, so _lookup\_vector_ must be sorted in ascending order.

### Example #2 - last non-empty cell

LOOKUP can be used to get the value of the last filled (non-empty) cell in a column. In the screen below, the formula in F6 is:

    =LOOKUP(2,1/(B:B<>""),B:B)
    

![Get value of last non-empty cell with LOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lookup%20example%20last%20non-empty%20cell.png?itok=2zBN4q4w "Get value of last non-empty cell with LOOKUP")

Note the use of a [full column reference](https://exceljet.net/glossary/full-column-reference)
. This is not an intuitive formula, but it works well. The key to understanding this formula is to recognize that the _lookup\_value_ of 2 is deliberately larger than any values that will appear in the _lookup\_vector_. [Detailed explanation here](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
.

### Example #3 - latest price

Like the above example, the lookup function can be used to look up the latest price in data sorted in ascending order by date. In the screen below, the formula in G5 is:

    =LOOKUP(2,1/(item=F5),price)
    

where **item** (B5:B12) and **price** (D5:D12) are [named ranges](https://exceljet.net/glossary/named-range)
. 

![Example of LOOKUP function to find latest price](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/example%20of%20lookup%20function%20to%20find%20latest%20price.png?itok=bJiqfPeH "Example of LOOKUP function to find latest price")

When _lookup\_value_ is greater than all values in _lookup\_array_, the default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors, then deliberately looking for the value 2, which will never be found. [More details here](https://exceljet.net/formulas/lookup-latest-price)
.

### Example #4 - array form

The LOOKUP function has an array form as well. In the array configuration, LOOKUP takes just two arguments: the _lookup\_value_, and a single two-dimensional _array:_

    LOOKUP(lookup_value, array) // array form
    

In the array form, LOOKUP evaluates the array and _automatically_ changes behavior based on the array dimensions. If the array is wider than tall, LOOKUP looks for the lookup value in the _first row_ of the array (like [HLOOKUP](https://exceljet.net/functions/hlookup-function)
). If the array is taller than wide (or square), LOOKUP looks for the lookup value in the _first column_ (like [VLOOKUP](https://exceljet.net/functions/vlookup-function)
). In either case, LOOKUP returns a value at the same position from the _last_ row or column in the array. The example below shows how the array form works. The formula in F5 is configured to use a _vertical_ array, and the formula in F6 is configured to use a _horizontal_ array:

    =LOOKUP(E5,B5:C9) // vertical array
    =LOOKUP(E6,C11:G12) // horizontal array
    

![LOOKUP function array form example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/lookup%20function%20array%20form%20example.png?itok=oBVq8Wby "LOOKUP function array form example")

The vertical and horizontal arrays contain the same values; only the orientation is different.

_Note: Microsoft discourages the use of the array form and suggests_ [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 _and_ [_HLOOKUP_](https://exceljet.net/functions/hlookup-function)
 _as better options._

### Notes

*   LOOKUP assumes that _lookup\_vector_ is sorted in ascending order.
*   When _lookup\_value_ can't be found, LOOKUP will match the _next smallest value_.
*   When _lookup\_value_ is greater than all values in _lookup\_vector_, LOOKUP matches the last value.
*   When _lookup\_value_ is less than the first value in _lookup\_vector_, LOOKUP returns #N/A.
*   _Result\_vector_ must be the same size as _lookup\_vector_.
*   LOOKUP is not case-sensitive

LOOKUP function examples
------------------------

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

[![Excel formula: Group numbers at uneven intervals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Group%20numbers%20at%20uneven%20intervals3.png "Excel formula: Group numbers at uneven intervals")](https://exceljet.net/formulas/group-numbers-at-uneven-intervals)

### [Group numbers at uneven intervals](https://exceljet.net/formulas/group-numbers-at-uneven-intervals)

To do this, LOOKUP is configured as follows: Lookup values are ages in column C The lookup vector is the named range "age" (F5:F8) The result vector is the named range "group" (G5:G8) With this setup, LOOKUP performs an approximate match on the numeric values in column F, and returns the associated...

[![Excel formula: Lookup latest price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20latest%20price.png "Excel formula: Lookup latest price")](https://exceljet.net/formulas/lookup-latest-price)

### [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)

The LOOKUP function assumes data is sorted, and always does an approximate match. If the lookup value is greater than all values in the lookup array, default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors,...

[![Excel formula: Get last match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match.png "Excel formula: Get last match")](https://exceljet.net/formulas/get-last-match)

### [Get last match](https://exceljet.net/formulas/get-last-match)

In the example shown, we have a set of order data that includes Date, Product, Name, and Amount. The data is sorted by date in ascending order. The goal is to look up the latest order for a given person by Name. In other words, we want the last match by name. The challenge is that Excel lookup...

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

[![Excel formula: Get value of last non-empty cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_value_of_last_non-empty_cell.png "Excel formula: Get value of last non-empty cell")](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

### [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

In this example, the goal is to get the last value in column B, even when data may contain empty cells. A secondary goal is to get the corresponding value in column C. This is useful for analyzing datasets where the most recent or last entry is significant. In the current version of Excel, a good...

[![Excel formula: Lookup value between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20value%20between%20two%20numbers.png "Excel formula: Lookup value between two numbers")](https://exceljet.net/formulas/lookup-value-between-two-numbers)

### [Lookup value between two numbers](https://exceljet.net/formulas/lookup-value-between-two-numbers)

The LOOKUP function does an approximate match lookup in one range, and returns the corresponding value in another. Although the table in this example includes both maximum and minimum values, we only need to use the minimum values. This is because when LOOKUP can't find a match, it will match the...

[![Excel formula: Get date associated with last entry](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20date%20associated%20with%20last%20entry.png "Excel formula: Get date associated with last entry")](https://exceljet.net/formulas/get-date-associated-with-last-entry)

### [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)

Working from the inside out, the expression C5:G5<>"" returns an array of true and false values: {FALSE,TRUE,FALSE,FALSE,FALSE} The number 1 is divided by this array, which creates a new array composed of either 1's or #DIV/0! errors: {#DIV/0!,1,#DIV/0!,#DIV/0!,#DIV/0!} This array is used as...

[![Excel formula: Get stock price (latest close)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20latest%20close.png "Excel formula: Get stock price (latest close)")](https://exceljet.net/formulas/get-stock-price-latest-close)

### [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)

In this example, the goal is to retrieve the last available close price for each symbol shown in column B. This can be done with the STOCKHISTORY function . The main purpose of STOCKHISTORY is to retrieve historical stock price information, and we need to make a few adjustments to prevent errors...

[![Excel formula: Lookup last file version](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20last%20file%20version.png "Excel formula: Lookup last file version")](https://exceljet.net/formulas/lookup-last-file-version)

### [Lookup last file version](https://exceljet.net/formulas/lookup-last-file-version)

This formula uses the LOOKUP function to find and retrieve the last matching file name. The lookup value is 2, and the lookup\_vector is created with this: 1/(ISNUMBER(FIND(G6,files))) Inside this snippet, the FIND function looks for the value in G6 inside the named range "files" (B5:B11). The...

[![Excel formula: SUMIFS vs other lookup formulas](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sumifs%20vs%20lookup%20formula.png "Excel formula: SUMIFS vs other lookup formulas")](https://exceljet.net/formulas/sumifs-vs-other-lookup-formulas)

### [SUMIFS vs other lookup formulas](https://exceljet.net/formulas/sumifs-vs-other-lookup-formulas)

If you are new to the SUMIFS function, you can find a basic overview with many examples here . The SUMIFS function is designed to sum numeric values based on one or more criteria. In specific cases however, you may be able to use SUMIFS to "look up" a numeric value that meets required criteria. The...

[![Excel formula: Get last entry by month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20last%20entry%20by%20month%20and%20year.png "Excel formula: Get last entry by month and year")](https://exceljet.net/formulas/get-last-entry-by-month-and-year)

### [Get last entry by month and year](https://exceljet.net/formulas/get-last-entry-by-month-and-year)

Note: the lookup\_value of 2 is deliberately larger than any values in the lookup\_vector, following the concept of bignum . Working from the inside out, the expression: (TEXT($B$5:$B$13,"mmyy")=TEXT(E5,"mmyy")) generates strings like "0117" using the values in column B and E, which are then compared...

[![Excel formula: Highlight approximate match lookup conditional formatting](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20approximate%20match%20lookups.png "Excel formula: Highlight approximate match lookup conditional formatting")](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)

### [Highlight approximate match lookup conditional formatting](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)

This formula uses 4 named ranges, defined as follows: width=K6 height=K7 widths=B6:B11 heights=C5:H5 Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, which is cell B5 in this case. To highlight the matching row, we use this...

[![Excel formula: Get last match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match_cell_contains.png "Excel formula: Get last match cell contains")](https://exceljet.net/formulas/get-last-match-cell-contains)

### [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)

The goal is to search through a cell for one of several specified values and return the last match found when one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in column C...

LOOKUP function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20approximate%20match%20lookups-Thumb.png)](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

### [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

In this video, we'll look at how to highlight approximate match lookups with conditional formatting. Here we have a simple lookup table that shows material costs for various heights and widths. The formula in K8 uses the INDEX and MATCH functions to retrieve the correct cost based on width and...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel HLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hlookup%20function.png "Excel HLOOKUP function")](https://exceljet.net/functions/hlookup-function)

### [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)

The Excel HLOOKUP function finds and retrieve a value from data in a horizontal table. The "H" in HLOOKUP stands for "horizontal", and lookup values must appear in the first row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

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

*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    
*   [Lookup last file version](https://exceljet.net/formulas/lookup-last-file-version)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    
*   [SUMIFS vs other lookup formulas](https://exceljet.net/formulas/sumifs-vs-other-lookup-formulas)
    
*   [Get last entry by month and year](https://exceljet.net/formulas/get-last-entry-by-month-and-year)
    
*   [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    
*   [Highlight approximate match lookup conditional formatting](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)
    
*   [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)
    
*   [Group numbers at uneven intervals](https://exceljet.net/formulas/group-numbers-at-uneven-intervals)
    

### Videos

*   [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Links

*   [Microsoft LOOKUP function documentation](https://support.office.com/en-us/article/lookup-function-446d94af-663b-451d-8251-369d5e3864cb)
    

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