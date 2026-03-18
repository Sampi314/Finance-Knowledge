# Get last match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-match

---

[Skip to main content](https://exceljet.net/formulas/get-last-match#main-content)

[](https://exceljet.net/formulas/get-last-match#)

*   [Previous](https://exceljet.net/formulas/get-information-about-max-value)
    
*   [Next](https://exceljet.net/formulas/get-last-match-cell-contains)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get last match
==============

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[FILTER](https://exceljet.net/functions/filter-function)

[TAKE](https://exceljet.net/functions/take-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[INDEX](https://exceljet.net/functions/index-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7935/download?token=b9lEAE-4)
 (16.41 KB)

![Excel formula: Get last match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_last_match.png "Excel formula: Get last match")

Summary
-------

To get the last match in a set of data you can use the XLOOKUP function. In the example shown, the formula in G7 is:

    =XLOOKUP(H4,data[Name],data,,,-1)
    

Where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:B16. The result, in this case, is the last entry for 'Juan', which is row 8 in the table.

Generic formula
---------------

    =XLOOKUP(A1,range,range,,,-1)

Explanation 
------------

In the example shown, we have a set of order data that includes Date, Product, Name, and Amount. The data is sorted by date in ascending order. The goal is to look up the latest order for a given person by Name. In other words, we want the last match by name. The challenge is that Excel lookup formulas will return the first match by default. There are several ways to approach this problem. In the current version of Excel, a good option is the XLOOKUP function. Another more flexible approach is to use the FILTER function with the TAKE function. In an older version of Excel, the easiest approach is to use a formula based on the LOOKUP function. All three approaches are explained below.

### XLOOKUP function

One way to solve this problem is with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, which is a modern upgrade to the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
. XLOOKUP is a very flexible function that takes six separate arguments:

    =XLOOKUP(lookup,lookup_array,return_array,[if_not_found],[match_mode],[search_mode])

Where each input has the following meaning:

*   _lookup\_value_ - the value to look for
*   _lookup\_array_ - the range or array to search within
*   _return\_array_ - the range or array to return values from
*   _if\_not\_found_ - value to return if no match is found
*   _match\_mode_ - settings for exact, approximate, and wildcard matching
*   search\_mode - settings for first, last, and binary searches

To solve this problem with XLOOKUP, you only need four of the parameters listed above:

    =XLOOKUP(lookup,lookup_array,return_array,,,search_mode)

The key input is _search\_mode_, which is needed to enable a reverse search. In the worksheet shown, the formula in cell G7 is:

    =XLOOKUP(H4,data[Name],data,,,-1)

The inputs to XLOOKUP are:

*   _lookup\_value:_ H4 (search value)
*   _lookup\_array_: data\[Name\]
*   _return\_array_: data (the entire table)
*   _search\_mode_: -1 for search last-to-first

The last input, _search\_mode_, is provided as -1 to create the last match behavior. In this configuration, XLOOKUP looks for the name "Juan" in the Name column of the table, _starting from the bottom_. When it finds a match, it returns the entire matching row from the **data** table. Notice we leave _if\_not\_found_ and _match\_mode_ empty, but we still need to supply the commas. Feel free to supply any value you like for if\_not\_found. _Match\_mode_ is not necessary, because XLOOKUP operates in exact-match mode by default, which is what we want in this case. It is not necessary to return the entire row. To return just the amount, simply adjust _return\_array_, as needed. For example, to return just Amount, use **data\[Amount\]** like this:

    =XLOOKUP(H4,data[Name],data[Amount],,,-1) // amount only

For more details on XLOOKUP, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. Excel Tables use structured references like **data\[Name\]**. See [Excel Tables](https://exceljet.net/articles/excel-tables)
 for a complete overview.

### Last n matches

Another way to solve this problem is to use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [TAKE function](https://exceljet.net/functions/take-function)
 like this:

    =TAKE(FILTER(data,data[Name]=H4),-1)

Essentially, we are filtering the entire set of data by name, then grabbing the last record from the filtered data with TAKE. This is a more flexible approach because it can be used to get the "last n matches". The generic version of the formula looks like this:

    =TAKE(FILTER(range,logical_test),-n)

For example, to get the last two matches in the worksheet shown, you can use:

    =TAKE(FILTER(data,data[Name]=H4),-2)

Here, the FILTER function is configured to return all matching records by name using the value in H4, and the TAKE function is configured to return the last two records returned by FILTER, _starting from the bottom_, by providing -2 for the _rows_ argument.

_Note: For more details on FILTER and TAKE, see [How to use the FILTER function](https://exceljet.net/functions/filter-function)
 and [How to use the TAKE function](https://exceljet.net/functions/take-function)
._

### nth to last match

If you want the nth to last match (i.e. the second to the last match, the third to the last match, etc.) you can replace TAKE with the [CHOOSEROWS function](https://exceljet.net/functions/chooserows-function)
 like this:

    =CHOOSEROWS(FILTER(data,data[Name]=H4),-n)

Where n represents the number of the match you want. For example, to get the second to last match, you can use:

    =CHOOSEROWS(FILTER(data,data[Name]=H4),-2)

FILTER returns all matching rows as before. CHOOSEROWS then returns the second to last row from the FILTER result. Keep in mind that there may not be a second-to-last match and, in that case, CHOOSEROWS will return a #VALUE! error.

### XMATCH function

The example shown returns the _data_ from the location of the last match. If you only want the _location_ of the last match, you can use the XMATCH function like this:

    =XMATCH(H4,data[Name],,-1) // returns 8

As with XLOOKUP, the search\_mode argument is set to -1 to enable last-to-first matching. The result is 8 since the last match is in the eighth row of the table. To retrieve the matching row, nest the XMATCH formula above inside the INDEX function like this:

    =INDEX(data,XMATCH(H4,data[Name],,-1),0)

Note that _row\_num_ must be provided as zero to return an [entire row with INDEX](https://exceljet.net/formulas/look-up-entire-row)
. For more details, see:

*   [How to use the XMATCH function](https://exceljet.net/functions/xmatch-function)
    
*   [How to use the INDEX function](https://exceljet.net/functions/index-function)
    
*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

### Older versions of Excel

In older versions of Excel that do not provide XLOOKUP or XMATCH, you can use a formula based on the [LOOKUP function](https://exceljet.net/functions/lookup-function)
. LOOKUP is an older function in Excel that can work well in "last match" scenarios, because it can handle array operations in older versions of Excel natively, with no need to enter as an array formula with control + shift + enter. In this problem, we can use LOOKUP in a formula like this:

    =LOOKUP(2,1/(data[Name]=H4),data[Amount])

This formula finds the last Amount for Juan in the data, which is 160. Let's look at how this works step by step. Working from the inside out, we first apply the criteria with a simple logical expression:

    data[Name]=H4
    

With "Juan" in cell H4, this expression results in an [array](https://exceljet.net/glossary/array)
 of 12 TRUE and FALSE values, where TRUE corresponds to names equal to "Juan" in the Name column:

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE}

Notice, we have TRUE values at rows 3 and 8. Next, we divide the number 1 by this array. During division, the math operation coerces TRUE to 1 and FALSE to zero, so you should visualize the operation like this:

    1/{0;0;1;0;0;0;0;1;0;0;0;0}
    

When the actual division takes place, one divided by one is one, and one divided by zero creates a #DIV/0 error and the resulting array looks like this:

    {#DIV/0!;#DIV/0!;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!}

This array is the _lookup\_vector_ inside LOOKUP, so at this point, we have:

    =LOOKUP(2,{#DIV/0!;#DIV/0!;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!},data[Amount])

Notice that the lookup value is 2. This may seem strange, but it is intentional. We use 2 as a lookup value to force LOOKUP to scan to the _end of the data_. LOOKUP will automatically ignore errors, so the only thing left to match are the 1s. It will scan through the 1s looking for a 2 that can never be found. When it reaches the end of the array, it will "step back" to the last valid value (the last 1), and return the Amount from the row at that position.

### Row numbers and nth last match

_The workarounds needed in older versions of Excel can be very complex. This section is quite technical and not necessary unless you want to use INDEX and MATCH to get the last match in an older version of Excel. Personally, I would try the LOOKUP alternative above first and only use the approach described below if there is a reason LOOKUP does not work as required. Nonetheless, it is useful to see how these things can be done in older versions of Excel and it provides a nice contrast to the simplicity of the XLOOKUP and FILTER + TAKE options explained above._

_Note: The formulas in this section are array formulas and must be entered with control + shift + enter in Excel 2019 and older._ 

Getting the row number (and ultimately, the value) for the nth last match is more difficult in older versions of Excel because we have no direct way to perform a reverse search. One option to get "nth last row numbers" is to use an [array formula](https://exceljet.net/glossary/array-formula)
 like this:

    =LARGE(IF(criteria,ROW(rng)-MIN(ROW(rng))+1),k)
    

where **k** represents "nth", as seen below:

    =LARGE(IF(data[Name]=H4,ROW(data)-MIN(ROW(data))+1),1) // last match
    =LARGE(IF(data[Name]=H4,ROW(data)-MIN(ROW(data))+1),2) // 2nd last
    =LARGE(IF(data[Name]=H4,ROW(data)-MIN(ROW(data))+1),3) // 3rd last
    

Working from the inside out, this part of the formula will generate a [relative set of row numbers](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
:

    ROW(data)-MIN(ROW(data))+1
    

The result of the above expression is an array of numbers like this:

    {1;2;3;4;5;6;7;8;9;10;11;12}
    

Notice we get 12 numbers, corresponding to the 12 rows in the table. Next, we only want _row numbers for matching values_, so we use the IF function to filter the values like so:

    IF(data[Name]=H4,ROW(data)-MIN(ROW(data))+1)
    

This results in an array like this:

    {FALSE;FALSE;3;FALSE;FALSE;FALSE;FALSE;8;FALSE;FALSE;FALSE;FALSE}
    

Note this array still contains 12 values, but only the row numbers where the name equals H4 ("Juan") survive. All other values become FALSE since they failed the logical test in the IF function. Finally, the array is delivered to the LARGE function, which extracts the nth largest value, which corresponds to the nth last match:

    LARGE({FALSE;FALSE;3;FALSE;FALSE;FALSE;FALSE;8;FALSE;FALSE;FALSE;FALSE},1) // returns 8
    LARGE({FALSE;FALSE;3;FALSE;FALSE;FALSE;FALSE;8;FALSE;FALSE;FALSE;FALSE},2) // returns 3
    

Once we know the last matching row number, we can use INDEX to retrieve a value at that position. The final formula looks like this:

    =INDEX(data[Amount],LARGE(IF(data[Name]=H4,ROW(data)-MIN(ROW(data))+1),n))

With "Juan" in cell H4, we get the following:

    ​=INDEX(data[Amount],LARGE(IF(data[Name]=H4,ROW(data)-MIN(ROW(data))+1),1)) // 160
    ​=INDEX(data[Amount],LARGE(IF(data[Name]=H4,ROW(data)-MIN(ROW(data))+1),2)) // 120

For more details on INDEX with MATCH, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

Related formulas
----------------

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Articles

*   [How to lookup first and last match](https://exceljet.net/articles/how-to-lookup-first-and-last-match)
    

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