# Extract common values from text strings - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-common-values-from-text-strings

---

[Skip to main content](https://exceljet.net/formulas/extract-common-values-from-text-strings#main-content)

[](https://exceljet.net/formulas/extract-common-values-from-text-strings#)

*   [Previous](https://exceljet.net/formulas/dynamic-two-way-sum)
    
*   [Next](https://exceljet.net/formulas/extract-common-values-from-two-lists)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Extract common values from text strings
=======================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[LET](https://exceljet.net/functions/let-function)

[SORT](https://exceljet.net/functions/sort-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8236/download?token=5zaeiXXu)
 (14.9 KB)

![Excel formula: Extract common values from text strings](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract_common_values_from_two_text_strings.png "Excel formula: Extract common values from text strings")

Summary
-------

To compare two delimited text strings and extract common values, you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [XMATCH function](https://exceljet.net/functions/xmatch-function)
 with help from the LET function to keep things efficient. In the example shown, the formula in D5 is:

    =LET(
    list1,TEXTSPLIT(B5,,", "),
    list2,TEXTSPLIT(C5,,", "),
    common,FILTER(list1,ISNUMBER(XMATCH(list1,list2))),
    TEXTJOIN(", ",1,common)
    )

As the formula is copied down it returns the values common to both lists. A separate formula in column E returns the count of the common values.

_Note: this example builds directly on a [more basic example here](https://exceljet.net/formulas/extract-common-values-from-two-lists)
._

Generic formula
---------------

    =LET(
    list1,TEXTSPLIT(A1,,", "),
    list2,TEXTSPLIT(A2,,", "),
    common,FILTER(list1,ISNUMBER(XMATCH(list1,list2))),
    TEXTJOIN(", ",1,common)
    )

Explanation 
------------

In this example, the goal is to extract common values from two text strings that contain comma-delimited values. In the worksheet shown the values for "List1" appear in column B and the values for "List2" appear in column C. The results in column D show the intersection of the two lists, that is, the values shared by List1 and List2. Notice that the order of the values in each list is random. In column E, we want to display a count of the common values.

_Note: this formula builds directly on another [more basic example here](https://exceljet.net/formulas/extract-common-values-from-two-lists)
, where the values in the lists appear in ranges on the worksheet instead of text strings. I recommend you take a look at that example first since it explains the underlying process in a bit more detail._

### The approach

The general approach for solving this problem breaks down into four steps:

1.  Split the text string for each list into an array of values
2.  Identify common values in the two arrays
3.  Filter one of the arrays to extract common values
4.  Create a comma-separated text string that contains the common values

In addition, I'm using LET in this case to keep the formula efficient and make it easier to read. In the worksheet shown, the formula used to solve this problem looks like this:

    =LET(
    list1,TEXTSPLIT(B5,,", "),
    list2,TEXTSPLIT(C5,,", "),
    common,FILTER(list1,ISNUMBER(XMATCH(list1,list2))),
    TEXTJOIN(", ",1,common)
    )

At a high level, this formula uses the FILTER function to filter the values in _list1_ to include only values that also appear in _list2_. The first step in this process is to name some variables.

### Splitting the text strings

This formula uses the LET function to define three variables: list1, list2, and common. First, the variable _list1_ is declared. The value for list1 comes from the TEXTSPLIT function, which is configured to split the text in cell B5 using a comma and a space as a delimiter:

    list1,TEXTSPLIT(B5,,", ") // split text in B5 to array

Next, the variable _list2_ is created in exactly the same way, this time with text from C5:

    list2,TEXTSPLIT(C5,,", ") // split text in C5 to array

At this point, _list1_ is an [array](https://exceljet.net/glossary/array)
 that looks like this:

    {"Orange";"Grapefruit";"Pear";"Banana";"Mango";"Lime";"Kiwi";"Lemon";"Apple";"Peach";"Apricot";"Cherry"}

And list2 is an array that looks like this:

    {"Banana","Lemon","Peach","Pear","Grapefruit","Honeydew","Mango","Nectarine","Fig","Apple"}

_Note: Arrays in Excel are very closely related to ranges. You can think of an array as a range of values without an address._

The next step in the formula is to identify common values.

### Identifying common values

Working from the inside out, the key to this formula is the [XMATCH function](https://exceljet.net/functions/xmatch-function)
, which is configured like this:

    XMATCH(list1,list2)

Inside XMATCH, the _lookup\_value_ is given as list1, and the _lookup\_array_ is given as _list2_. Since _list1_ is an array that contains 12 values, XMATCH returns 12 results in an array like this:

    {#N/A,5,4,1,7,#N/A,#N/A,2,10,3,#N/A,#N/A}

The #N/A errors represent values in list1 that _were not found_ in list2. The numbers represent the location of values that _were found_. For example, looking at the first four values in the array:

*   The #N/A tells us that "Orange" was not found in list2
*   The 5 tells us that "Grapefruit" was found as the fifth value in list2
*   The 4 tells us that "Pear" was found as the fourth value in list2
*   The 1 tells us that "Banana" was found as the first value in list2

And so on. In other words, the numbers represent _values that appear in both lists_, and errors indicate values in list1 that _were not found_ in list2.

> XMATCH defaults to an exact match, so _match\_mode_ is not required above.

### Converting results to TRUE and FALSE

Now that we know which values in list1 appear in list2, the next step is to filter list1 to select only common values. However, before we can use FILTER, we need to convert the array returned by XMATCH into TRUE and FALSE values. This is why the XMATCH function is nested inside the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    =ISNUMBER(XMATCH(list1,list2))

First, XMATCH returns the array of positions, as described above:

    ISNUMBER({#N/A,5,4,1,7,#N/A,#N/A,2,10,3,#N/A,#N/A})

Next, the ISNUMBER function converts these results into simple TRUE and FALSE values. The result is another array like this:

    {FALSE,TRUE,TRUE,TRUE,TRUE,FALSE,FALSE,TRUE,TRUE,TRUE,FALSE,FALSE}

Notice we still have 12 items in the array, one for each value in list1. However, the numbers and errors have been replaced by TRUE and FALSE values. A TRUE indicates a value that was found, and a FALSE indicates a value that was not found. This is exactly what we need for the FILTER function.

### Filtering the values

The final step in the process is to filter the values in list1 by the array we created with XMATCH and ISNUMBER above. The result from ISNUMBER is delivered to FILTER as the _include_ argument with list1 given for _array_:

    =FILTER(list1,{FALSE,TRUE,TRUE,TRUE,TRUE,FALSE,FALSE,TRUE,TRUE,TRUE,FALSE,FALSE})

FILTER then selects all values in list1 that correspond to TRUE and returns an array that contains the seven values common to both lists:

    {"Grapefruit","Pear","Banana","Mango","Lemon","Apple","Peach"}

This array contains just the values shared by list1 and list2. Inside the LET function, we declare a variable named common, and use the array to assign a value:

    common,FILTER(list1,ISNUMBER(XMATCH(list1,list2))),

### Creating a comma-separated text string

The final step in the process is to join the common values in the comma-separated text string that appears in column D. For this, we use the TEXTJOIN function:

    TEXTJOIN(", ",1,common)

With a comma and space (", ") given as a delimiter, TEXTJOIN joins the values in the array returned by FILTER and returns the comma-separated text string in D5 as a final result. When the formula is copied down to D6, the same operation is performed on different text strings that contain colors.

### Sort results

To sort results, you can nest the FILTER function inside the [SORT function](https://exceljet.net/functions/sort-function)
 like this:

    =LET(
    list1,TEXTSPLIT(B5,,", "),
    list2,TEXTSPLIT(C5,,", "),
    common,SORT(FILTER(list1,ISNUMBER(XMATCH(list1,list2)))),
    TEXTJOIN(", ",1,common)
    )

### Count results

Once you have a list of common values, you can count the values returned in cell D5 with [COUNTA](https://exceljet.net/functions/counta-function)
 and TEXTSPLIT. The formula in cell E5 is:

    =COUNTA(TEXTSPLIT(D5,", "))

If you only want a count of common values (not a list), you can calculate the count with an all-in-one formula like this:

    =LET(
    list1,TEXTSPLIT(B5,,", "),
    list2,TEXTSPLIT(C5,,", "),
    common,FILTER(list1,ISNUMBER(XMATCH(list1,list2))),
    COUNTA(common)
    )

This is pretty much the same formula as the original, except for the last line. Instead of joining the values in _common_ with TEXTSPLIT, we count them with COUNTA.

### List missing values

To reverse the logic and list values in List 1 that _do not appear_ in List 2 you can modify the formula like this:

    =LET(
    list1,TEXTSPLIT(B5,,", "),
    list2,TEXTSPLIT(C5,,", "),
    common,FILTER(list1,ISNA(XMATCH(list1,list2))),
    TEXTJOIN(", ",1,common)
    )

Notice the only change is to replace ISNUMBER with the [ISNA function](https://exceljet.net/functions/isna-function)
, which returns TRUE for error and FALSE for anything else.

Related formulas
----------------

[![Excel formula: Extract common values from two lists](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_common_values_from_two_lists.png "Excel formula: Extract common values from two lists")](https://exceljet.net/formulas/extract-common-values-from-two-lists)

### [Extract common values from two lists](https://exceljet.net/formulas/extract-common-values-from-two-lists)

In this example, the goal is to compare the values in two different lists, then extract the values that appear in both lists into a third list as shown in the worksheet above. The values for List 1 appear in column B, and the values for List 2 appear in column D. Although we have a list of fruits...

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

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

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

*   [Extract common values from two lists](https://exceljet.net/formulas/extract-common-values-from-two-lists)
    
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
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    

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