# Extract common values from two lists - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-common-values-from-two-lists

---

[Skip to main content](https://exceljet.net/formulas/extract-common-values-from-two-lists#main-content)

[](https://exceljet.net/formulas/extract-common-values-from-two-lists#)

*   [Previous](https://exceljet.net/formulas/extract-common-values-from-text-strings)
    
*   [Next](https://exceljet.net/formulas/extract-numbers-from-text)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Extract common values from two lists
====================================

by Dave Bruns · Updated 21 Apr 2025

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[SORT](https://exceljet.net/functions/sort-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8219/download?token=7-e53PLc)
 (14.83 KB)

![Excel formula: Extract common values from two lists](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract_common_values_from_two_lists.png "Excel formula: Extract common values from two lists")

Summary
-------

To compare two lists and extract common (i.e. shared) values, you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [XMATCH function](https://exceljet.net/functions/xmatch-function)
. In the example shown, the formula in F5 is:

    =FILTER(B5:B16,ISNUMBER(XMATCH(B5:B16,D5:D14)))
    

The XMATCH function identifies which values are common to both lists. The FILTER function uses this information to filter the values and return only those that appear in both lists. The seven common values spill into the range F5:F11.

Generic formula
---------------

    =FILTER(list1,ISNUMBER(XMATCH(list1,list2)))

Explanation 
------------

In this example, the goal is to compare the values in two different lists, then extract the values that appear in both lists into a third list as shown in the worksheet above. The values for List 1 appear in column B, and the values for List 2 appear in column D. Although we have a list of fruits in this example, the same approach can be applied to names, places, products, and so on. Also, while the lists in the worksheet are short to make the example easy to understand, the same formula will work fine for lists that contain hundreds or thousands of values.

> You can use this same basic approach to [extract common values from text strings](https://exceljet.net/formulas/extract-common-values-from-two-text-strings)
> .

### The approach

The general approach for solving this problem is quite simple and looks like this:

1.  Identify common values in the two lists
2.  Filter one of the lists to extract common values

The tricky part of the formula is identifying common values. Once we have identified common values, we can extract a list of common values from either list. The generic version of the formula looks like this:

    =FILTER(list1,ISNUMBER(XMATCH(list1,list2)))

It does not matter which list we filter, but it is important to provide the _same list_ for the _array_ in FILTER and the _lookup\_value_ in XMATCH. This is because we need the resulting array from XMATCH to match the dimensions of the _array_ provided to FILTER. In the worksheet shown, the formula used to solve this problem looks like this:

    =FILTER(B5:B16,ISNUMBER(XMATCH(B5:B16,D5:D14)))

At a high level, this formula uses the FILTER function to filter the values in B5:B16 so that only values that appear in both lists are retained. The first step in this process is identifying common values.

### Identifying common values

Working from the inside out, the key to this formula is the [XMATCH function](https://exceljet.net/functions/xmatch-function)
, which is configured like this:

    XMATCH(B5:B16,D5:D14)

Inside XMATCH, the _lookup\_value_ is given as the range B5:B16, and the _lookup\_array_ is given as D5:D14. Since the lookup item in XMATCH is most often a single value, you might find this configuration strange. Rest assured, there is a method to this madness. In essence, we are asking the XMATCH function to try and find every value in B5:B16 (List 1) in the range D5:D14 (List 2). The result from XMATCH is an [array](https://exceljet.net/glossary/array)
 that looks like this:

    {#N/A;5;4;1;7;#N/A;#N/A;2;10;3;#N/A;#N/A}

This array is somewhat hard to read, but if you look carefully you will see that it contains 12 items. This makes sense because there are 12 values in the range B5:B16, so each item in the array is a result. The #N/A errors represent values in B5:B16 that _were not found_ in the range D5:D14. The numbers represent the location of values that _were found_. For example, looking at the first four values in the array:

*   The #N/A tells us that "Orange" was not found in D5:D14
*   The 5 tells us that "Grapefruit" was found in row 5 of D5:D14
*   The 4 tells us that "Pear" was found in row 4 of D5:D14
*   The 1 tells us that "Banana" was found in row 1 of D5:D14

And so on. The bottom line is that _numbers represent common values that appear in both lists_, and errors indicate values in List 1 that _were not found_ in List 2.

> XMATCH defaults to an exact match, so _match\_mode_ is not required above.

### Converting results to TRUE and FALSE

Now that we know which values appear in both lists, the next step is filtering one of the lists to show only common values. However, before we can do that, we need to convert the results from XMATCH into something more digestible to FILTER. If we try to use the array as-is, FILTER will throw an error when it encounters any #N/A error in the array. To do the conversion, we use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 which is wrapped around XMATCH:

    =ISNUMBER(XMATCH(B5:B16,D5:D14))

First, XMATCH returns the array of positions, as described above:

    ISNUMBER({#N/A;5;4;1;7;#N/A;#N/A;2;10;3;#N/A;#N/A})

Next, the ISNUMBER function converts these results into simple TRUE and FALSE values. The result is another array like this:

    {FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE}

Again notice we have 12 items in the array, each corresponding to a value in B5:B16. However, the numbers and errors are gone. In this new array, a TRUE indicates a value that was found, and a FALSE indicates a value that was not found. This is exactly what we need for the FILTER function.

### Filtering the values

The final step in the process is to filter the values in B5:B15 by the array we created with XMATCH and ISNUMBER. The result from ISNUMBER is returned directly to FILTER as the _include_ argument with the range B5:B16 given for _array_:

    =FILTER(B5:B16,{FALSE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE})

FILTER uses the array to "filter" the values in B5:B16 and only values associated with TRUE survive the operation. The final result from FILTER is an array that contains the seven values common to both lists:

    {"Grapefruit";"Pear";"Banana";"Mango";"Lemon";"Apple";"Peach"}

This array lands in cell F5 and spills into the range F5:F11.

### Remove duplicates

To remove duplicates, you can nest the formula inside the [UNIQUE function](https://exceljet.net/functions/unique-function)
:

    =UNIQUE(FILTER(list1,ISNUMBER(XMATCH(list1,list2))))
    

### Sort results

To sort results, you can nest the formula inside the [SORT function](https://exceljet.net/functions/sort-function)
:

    =SORT(FILTER(list1,ISNUMBER(XMATCH(list1,list2))))
    

### List missing values

To reverse the logic and list values in List 1 that _do not appear_ in List 2 you can modify the formula like this:

    =FILTER(list1,ISNA(XMATCH(list1,list2)))
    

Notice the only change is to replace ISNUMBER with the [ISNA function](https://exceljet.net/functions/isna-function)
, which returns TRUE for error and FALSE for anything else.

### COUNTIF variation

I want to point out that you can also use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 instead of XMATCH + ISNUMBER to list common values in a formula like this:

    =FILTER(B5:B16,COUNTIF(D5:D14,B5:B16))

As before, the array provided to FILTER is the range B5:B16. However, the logic for filtering is done with COUNTIF like this:

    COUNTIF(D5:D14,B5:B16)

Here, COUNTIF is configured with D5:D14 as the _range_ and B5:B16 as the _criteria_. Because we are giving COUNTIF 12 values for _criteria_, COUNTIF returns 12 results in an array like this:

    {0;1;1;1;1;0;0;1;1;1;0;0}

These values are counts. The 1's correspond to values in B5:B16 that also appear in D5:D14 and the zeros correspond to values in B5:B16 that were _not found_ in D5:D14. This array is delivered directly to the FILTER function as the _include_ argument:

    =FILTER(B5:B16,{0;1;1;1;1;0;0;1;1;1;0;0})
    

The FILTER function then filters the values in B5:B16 and returns only those that correspond to a 1. Values associated with 0 are removed. The final result is an array of seven values that exist in both lists, which [spills](https://exceljet.net/glossary/spill)
 into the range F5:F11.

_On the face of it, this is a pretty slick solution that is simpler than the original formula above. However, it comes with a significant caveat: it only works on ranges. This means you cannot create an array of values in a formula and feed it to the COUNTIF variant of this formula, because COUNTIF will not accept an array in place of an actual range. This limitation is shared by all of the \*IFs functions and is_ [_discussed in some detail here_](https://exceljet.net/articles/excels-racon-functions)
_. It's frustrating to have a simple and elegant formula that fails in some situations and for this reason, I recommend the XMATCH + ISNUMBER formula as a better, more universal solution._

Related formulas
----------------

[![Excel formula: Unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values.png "Excel formula: Unique values")](https://exceljet.net/formulas/unique-values)

### [Unique values](https://exceljet.net/formulas/unique-values)

This example uses the UNIQUE function, which is fully automatic. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. UNIQUE is a dynamic function. If any data in B5:B16 changes, the output from UNIQUE will update immediately...

[![Excel formula: Distinct values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/distinct%20values.png "Excel formula: Distinct values")](https://exceljet.net/formulas/distinct-values)

### [Distinct values](https://exceljet.net/formulas/distinct-values)

This example uses the UNIQUE function . With default settings, UNIQUE will output a list of unique values, i.e. values that appear one or more times in the source data. However, UNIQUE has an optional third argument, called occurs\_once that, when set to TRUE, will cause UNIQUE to return only values...

[![Excel formula: Unique values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20with%20criteria.png "Excel formula: Unique values with criteria")](https://exceljet.net/formulas/unique-values-with-criteria)

### [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove limit data to values associated with group A only: FILTER(B5:B16,C5:C16=E4) Notice we are picking up the value "A" directly from the header in cell E4...

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

[![Excel formula: Unique values ignore blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20ignore%20blanks.png "Excel formula: Unique values ignore blanks")](https://exceljet.net/formulas/unique-values-ignore-blanks)

### [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove any blank values from the data: FILTER(B5:B16,B5:B16<>"") The <> symbol is a logical operator that means "does not equal". For more examples...

[![Excel formula: Find missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_missing_values.png "Excel formula: Find missing values")](https://exceljet.net/formulas/find-missing-values)

### [Find missing values](https://exceljet.net/formulas/find-missing-values)

The goal is to identify invoice numbers in range D5:D11 that are missing in range B5:B16 (named list ). Two good ways to solve this problem in Excel are the COUNTIF function and the MATCH function . Both approaches are explained below. COUNTIF function COUNTIF counts cells in a range that meet a...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Unique values](https://exceljet.net/formulas/unique-values)
    
*   [Distinct values](https://exceljet.net/formulas/distinct-values)
    
*   [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    
*   [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)
    
*   [Find missing values](https://exceljet.net/formulas/find-missing-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

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