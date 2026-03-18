# Get value of last non-empty cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-value-of-last-non-empty-cell

---

[Skip to main content](https://exceljet.net/formulas/get-value-of-last-non-empty-cell#main-content)

[](https://exceljet.net/formulas/get-value-of-last-non-empty-cell#)

*   [Previous](https://exceljet.net/formulas/get-nth-match-with-vlookup)
    
*   [Next](https://exceljet.net/formulas/index-and-match-advanced-example)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get value of last non-empty cell
================================

by Dave Bruns · Updated 17 Jun 2023

Related functions 
------------------

[LOOKUP](https://exceljet.net/functions/lookup-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6701/download?token=S3e66att)
 (14.8 KB)

![Excel formula: Get value of last non-empty cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_value_of_last_non-empty_cell.png "Excel formula: Get value of last non-empty cell")

Summary
-------

To get the value of the last non-empty cell in a range, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. In the example shown, the formula in E5 is:

    =XLOOKUP(TRUE,B5:B16<>"",B5:B16,,,-1)
    

The result is 15-Jun-23, as seen in cell B15. To get the corresponding amount in column C, just adjust the _return\_array_, as explained below.

Generic formula
---------------

    =XLOOKUP(TRUE,range<>"",range,,,-1)

Explanation 
------------

In this example, the goal is to get the last value in column B, even when data may contain empty cells. A secondary goal is to get the corresponding value in column C. This is useful for analyzing datasets where the most recent or last entry is significant. In the current version of Excel, a good way to solve this problem is with the XLOOKUP function. In older versions of Excel, you can use the LOOKUP function. Both methods are explained below.

###  XLOOKUP function

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 is a modern upgrade to the VLOOKUP function. XLOOKUP is very flexible and can handle many different lookup scenarios. The key feature, in this case, is the ability to perform a "last to first" search. The generic syntax for XLOOKUP looks like this:

    =XLOOKUP(lookup_value,lookup_array,return_array,if_not_found,match_mode,search_mode)

Where each argument has the following meaning:

*   _lookup\_value_ - the value to look for
*   _lookup\_array_ - the range or array to search within
*   _return\_array_ - the range or array to return values from
*   _if\_not\_found_ - value to return if no match is found
*   _match\_mode_ - settings for exact, approximate, and wildcard matching
*   _search\_mode_ - settings for first to last, last to first, and binary searches

For more details, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
.

In this example, we want to find the last non-empty cell in a range, so we use XLOOKUP like this:

    =XLOOKUP(TRUE,B5:B16<>"",B5:B16,,,-1)

At a high level, we configure XLOOKUP to look for TRUE in a lookup array created with a logical expression, and we enable a "last to first" search by providing -1 for _search\_mode_:

*   _lookup\_value_ - TRUE
*   _lookup\_array_ - B5:B16<>""
*   _return\_array_ - B5:B16
*   _if\_not\_found_ - omitted, defaults to #N/A
*   _match\_mode_ - omitted, defaults to exact match
*   _search\_mode -_ given as -1 for search last to first

The main trick is the logical expression used for _lookup\_array_:

    B5:B16<>""

The <> [operator](https://exceljet.net/glossary/logical-operators)
 means "not", so <>"" means "not empty". Because B5:B16 contains 12 values, the expression returns an [array](https://exceljet.net/glossary/array)
 that contains 12 TRUE and FALSE results. 

    {TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}

In this array, the TRUE values in the array indicate _non-blank_ cells and the FALSE values indicate _blank_ cells. This array is delivered directly to the XLOOKUP function as the _lookup\_array_:

    =XLOOKUP(TRUE,{TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE},B5:B16,,,-1)

Because search\_mode is -1, XLOOKUP starts its search from the _end of the array_ and matches the first TRUE encountered (the second to last value in the array). With the _return\_array_ provided as B5:B16, XLOOKUP returns 15-Jun-23 as a final result.

### Corresponding value

The XLOOKUP formula in cell F7 to get the corresponding price from column C is almost identical:

    =XLOOKUP(TRUE,B5:B16<>"",C5:C16,,,-1)

Note the only difference is the return\_array, which is provided as C5:C16.

### Dealing with errors

If the last non-empty cell contains an error, the error will be ignored. If you want to return an error that appears last in a range you can adjust the formula to use the [ISBLANK](https://exceljet.net/functions/isblank-function)
 and [NOT](https://exceljet.net/functions/not-function)
 functions like this:

    =XLOOKUP(TRUE,NOT(ISBLANK(B5:B16)),B5:B16,,,-1)
    

This version of the formula will show an error if the last non-empty cell contains an error.

### Last numeric value

To get the last numeric value, you can use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 like this:

    =XLOOKUP(TRUE,ISNUMBER(B5:B16),B5:B16,,,-1)
    

### Last non-blank, non-zero value

To check that the last value is not blank _and_ not zero, you use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 like this:

    =XLOOKUP(1,(B5:B16<>"")*(B5:B16<>0),B5:B16,,,-1)
    

Notice the lookup value is now 1 instead of TRUE. For more details, see [Boolean Algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
 and [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
.

Older versions of Excel
-----------------------

In older versions of Excel, there is no XLOOKUP function, so we need another approach. One solution is to use the [LOOKUP function](https://exceljet.net/functions/lookup-function)
, which can handle [array operations](https://exceljet.net/glossary/array-operation)
 natively. The generic formula looks like this:

    =LOOKUP(2,1/(range<>""),range)

Adjusting references for this problem, we have the following formula:

    =LOOKUP(2,1/(B5:B16<>""),B5:B16)

_Note: This is an [array formula](https://exceljet.net/glossary/array-formula)
. But because LOOKUP can handle the [array operation](https://exceljet.net/glossary/array-operation)
 natively, the formula does not need to be entered with Control + Shift + Enter, even in older versions of Excel._

Working from the inside out, we use a logical expression to test for empty cells in B5:B16:

    B5:B16<>""
    

The [logical operator](https://exceljet.net/glossary/logical-operators)
 <> means _not equal to_, and "" means [empty string](https://exceljet.net/glossary/empty-string)
, so this expression means _B5:B16 is not empty_. The result is an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values, where TRUE represents cells that _are not empty_ and FALSE represents cells that _are empty_. Because B5:C16 contains 12 values, the expression returns an [array](https://exceljet.net/glossary/array)
 with 12 results:

    {TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}

Next, we divide the number 1 by the array. The math operation automatically coerces TRUE to 1 and FALSE to 0, so we have:

    1/({1;1;1;1;0;1;1;0;1;0;1;0})
    

Since dividing by zero generates an error, the result is an array composed of 1s and #DIV/0 errors:

    {1;1;1;1;#DIV/0!;1;1;#DIV/0!;1;#DIV/0!;1;#DIV/0!}
    

Here, the 1s represent non-empty cells, and errors represent empty cells. This array becomes the _lookup\_array_ [argument](https://exceljet.net/glossary/function-argument)
 in LOOKUP. The _lookup\_value_ is given as the number 2. This may seem baffling, but there is a good reason. We are using 2 as a lookup value to force LOOKUP to scan to the _end of the data_. LOOKUP automatically ignores errors, so LOOKUP will scan through the 1s looking for a 2 that will never be found. When it reaches the end of the array, it will "step back" to the last 1, which corresponds to the last non-empty cell. Since the _result\_vector_ is B5:B16,  the final result is: 15-Jun-23.

_Note: the key to understanding this formula is to recognize that the lookup\_value of 2 is deliberately larger than any values that will appear in the lookup\_vector. When lookup\_value can't be found, LOOKUP will match the next smallest value that is not an error: the last 1 in the array. This works because LOOKUP assumes that values in lookup\_vector are sorted in ascending order and will always perform an approximate match. When LOOKUP can't find a match, it will match the next smallest value._

### Get corresponding value

You can easily adapt the lookup formula to return a corresponding value. For example, to get the price associated with the last value in column B, the formula in F7 is:

    =LOOKUP(2,1/(B5:B16<>""),C5:C16) // get price
    

The only difference is that the _result\_vector_ argument has been supplied as C5:C16.

### Dealing with errors

If the last non-empty cell contains an error, the error will be ignored. If you want to return an error that appears last in a range you can adjust the formula to use the [ISBLANK](https://exceljet.net/functions/isblank-function)
 and [NOT](https://exceljet.net/functions/not-function)
 functions like this:

    =LOOKUP(2,1/(NOT(ISBLANK(B5:B16))),B5:B16)
    

This version of the formula will show an error if the last non-empty cell contains an error.

### Last numeric value

To get the last _numeric value_, you can use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 like this:

    =LOOKUP(2,1/(ISNUMBER(B5:B16)),B5:B16)
    

### Last non-blank, non-zero value

To check that the last value is not blank _and_ not zero, you can use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 like this:

    =LOOKUP(2,1/((B5:B16<>"")*(B5:B16<>0)),B5:B16)
    

For a more detailed explanation, see [Boolean Algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
.

Related formulas
----------------

[![Excel formula: Get date associated with last entry](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20date%20associated%20with%20last%20entry.png "Excel formula: Get date associated with last entry")](https://exceljet.net/formulas/get-date-associated-with-last-entry)

### [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)

Working from the inside out, the expression C5:G5<>"" returns an array of true and false values: {FALSE,TRUE,FALSE,FALSE,FALSE} The number 1 is divided by this array, which creates a new array composed of either 1's or #DIV/0! errors: {#DIV/0!,1,#DIV/0!,#DIV/0!,#DIV/0!} This array is used as...

[![Excel formula: Get last entry by month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20last%20entry%20by%20month%20and%20year.png "Excel formula: Get last entry by month and year")](https://exceljet.net/formulas/get-last-entry-by-month-and-year)

### [Get last entry by month and year](https://exceljet.net/formulas/get-last-entry-by-month-and-year)

Note: the lookup\_value of 2 is deliberately larger than any values in the lookup\_vector, following the concept of bignum . Working from the inside out, the expression: (TEXT($B$5:$B$13,"mmyy")=TEXT(E5,"mmyy")) generates strings like "0117" using the values in column B and E, which are then compared...

[![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

### [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function. XLOOKUP function The XLOOKUP function is a modern upgrade to the VLOOKUP function. XLOOKUP is very...

[![Excel formula: Lookup latest price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20latest%20price.png "Excel formula: Lookup latest price")](https://exceljet.net/formulas/lookup-latest-price)

### [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)

The LOOKUP function assumes data is sorted, and always does an approximate match. If the lookup value is greater than all values in the lookup array, default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors,...

[![Excel formula: Last row in numeric data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20numeric%20data.png "Excel formula: Last row in numeric data")](https://exceljet.net/formulas/last-row-in-numeric-data)

### [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)

When building advanced formulas that use dynamic ranges, it's often necessary to figure out the last location of data in a list. Depending on the data, this could be the last row with data, the last column with data, or the intersection of both. Note: we want the last \*relative position\* inside a...

[![Excel formula: Last row in text data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20text%20data.png "Excel formula: Last row in text data")](https://exceljet.net/formulas/last-row-in-text-data)

### [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)

This formula uses the MATCH function in approximate match mode to locate the last text value in a range. Approximate match enabled by setting by the 3rd argument in MATCH to 1, or omitting this argument, which defaults to 1. The lookup value is a so-called "big text" (sometimes abbreviated "bigtext...

Related functions
-----------------

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get date associated with last entry](https://exceljet.net/formulas/get-date-associated-with-last-entry)
    
*   [Get last entry by month and year](https://exceljet.net/formulas/get-last-entry-by-month-and-year)
    
*   [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    
*   [Last row in numeric data](https://exceljet.net/formulas/last-row-in-numeric-data)
    
*   [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)
    

### Functions

*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

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