# Excel SORTBY function | Exceljet

**Source:** https://exceljet.net/functions/sortby-function

---

[Skip to main content](https://exceljet.net/functions/sortby-function#main-content)

[](https://exceljet.net/functions/sortby-function#)

*   [Previous](https://exceljet.net/functions/sort-function)
    
*   [Next](https://exceljet.net/functions/stockhistory-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

SORTBY Function
===============

by Dave Bruns · Updated 2 Mar 2026

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SORT](https://exceljet.net/functions/sort-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9545/download?token=kugU2ZW1)
 (42.33 KB)

![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")

Summary
-------

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

Purpose 
--------

Sorts range or array by column

Return value 
-------------

Sorted array

Syntax
------

    =SORTBY(array,by_array,[sort_order],[array/order],...)

*   _array_ - Range or array to sort.
*   _by\_array_ - Range or array to sort by.
*   _sort\_order_ - \[optional\] Sort order. 1 = ascending (default), -1 = descending.
*   _array/order_ - \[optional\] Additional array and sort order pairs.

Using the SORTBY function 
--------------------------

The SORTBY function sorts the contents of a [range](https://exceljet.net/glossary/range)
 or [array](https://exceljet.net/glossary/array)
 based on the values from another range or array. The result is a dynamic array that will "[spill](https://exceljet.net/glossary/spill)
" onto the worksheet. If values in the source data change, the output from SORTBY updates automatically. Note that the SORTBY function cannot sort data in place like Excel's Sort command on the Ribbon. SORTBY always outputs results to a new location.

The first argument, _array_, is the data to sort. The second argument, _by\_array1_, contains the values used for sorting. These values can come from an existing range or from an array created by a formula — see [Sort by custom list](https://exceljet.net/functions/sortby-function#sort-by-custom-list)
 below for an example. The key feature of SORTBY is that _by\_array1_ values do not need to be part of the source data and do not need to appear in the output. However, _by\_array1_ must have dimensions compatible with _array_. The optional _sort\_order1_ argument controls direction: 1 for ascending (default), -1 for descending. To sort by more than one level, provide additional _by\_array_ and _sort\_order_ pairs.

Excel contains two functions for sorting: SORT and SORTBY. The [SORT function](https://exceljet.net/functions/sort-function)
 is the simpler option when data already contains the values needed for sorting. SORTBY handles two specific situations that SORT can't:

1.  You want to sort by values that shouldn't appear in the output.
2.  The values you need to sort by aren't part of your source data at all.

Use SORTBY when the values to sort by need to be calculated, or should be excluded in the output, or both. This could be to sort in a [custom order](https://exceljet.net/functions/sortby-function#sort-by-custom-list)
, or to sort by [text length](https://exceljet.net/functions/sortby-function#sort-text-by-length)
, [date component](https://exceljet.net/functions/sortby-function#sort-birthdays-by-month-and-day)
, or [extracted substring](https://exceljet.net/functions/sortby-function#sort-by-substring)
. Also, because SORTBY references ranges directly, instead of by column index like SORT, it can handle column additions and deletions more gracefully.

Note that SORT won't automatically adjust the source range if data is added or deleted. To configure SORT with a range that automatically adjusts to fit the data, use an [Excel Table](https://exceljet.net/articles/excel-tables)
 or a dynamic range created with [TRIMRANGE](https://exceljet.net/functions/trimrange-function)
 or the [dot operator](https://exceljet.net/glossary/dot-operator)
.

> Video: [Basic SORTBY function example](https://exceljet.net/videos/basic-sortby-function-example)

### Key features

*   Returns a dynamic array that spills automatically
*   Sorts values don't need to appear in source data or output
*   Auto-detects orientation from _by\_array_ (vertical = sort rows, horizontal = sort columns)
*   Supports multiple sort levels (up to 64 pairs)
*   More resilient to column changes than SORT (references ranges, not index numbers)
*   Works with [Excel Tables](https://exceljet.net/articles/excel-tables)
     and [structured references](https://exceljet.net/glossary/structured-reference)
    

### Table of contents

*   [Basic usage](https://exceljet.net/functions/sortby-function#basic-usage)
    
*   [Sort by score](https://exceljet.net/functions/sortby-function#sort-by-score)
    
*   [Sort horizontally](https://exceljet.net/functions/sortby-function#sort-horizontally)
    
*   [Sort by two columns](https://exceljet.net/functions/sortby-function#sort-by-two-columns)
    
*   [Sort text by length](https://exceljet.net/functions/sortby-function#sort-text-by-length)
    
*   [Sort by custom list](https://exceljet.net/functions/sortby-function#sort-by-custom-list)
    
*   [Sort birthdays by month and day](https://exceljet.net/functions/sortby-function#sort-birthdays-by-month-and-day)
    
*   [Random sort](https://exceljet.net/functions/sortby-function#random-sort)
    
*   [Sort by substring](https://exceljet.net/functions/sortby-function#sort-by-substring)
    
*   [Related functions](https://exceljet.net/functions/sortby-function#related-functions)
    
*   [Notes](https://exceljet.net/functions/sortby-function#notes)
    

### Basic usage

To sort by values in another range:

    =SORTBY(B5:B16,C5:C16) // sort B by C values, ascending
    =SORTBY(B5:B16,C5:C16,-1) // sort B by C values, descending
    

To sort by a calculated value:

    =SORTBY(B5:B16,LEN(B5:B16)) // sort by text length
    =SORTBY(B5:B16,RANDARRAY(12)) // random sort
    

To sort by multiple levels:

    =SORTBY(B5:D14,D5:D14,1,C5:C14,-1) // by D ascending, then C descending
    

### Sort by score

One of the key advantages of SORTBY is the ability to sort data using values that don't appear in the output. In the worksheet below, the goal is to sort the names in column B by the scores in column C, in descending order. The formula in E5 is:

    =SORTBY(B5:B16,C5:C16,-1)
    

![SORTBY function example - sort by score in descending order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sortby_example_sort_by_score.png "SORTBY function example - sort by score in descending order")

The _array_ argument is B5:B16 (names only), while _by\_array1_ is C5:C16 (scores). Because only the names are provided for _array_, the scores are used for sorting but don't appear in the output. The _sort\_order1_ of -1 sorts in descending order, so the highest score appears first. To include both names and scores in the output, provide the full range as _array_:

    =SORTBY(B5:C16,C5:C16,-1) // returns both names and scores
    

### Sort horizontally

Unlike the [SORT function](https://exceljet.net/functions/sort-function)
, SORTBY does not have an argument that controls sorting by rows versus columns. Instead, SORTBY auto-detects the sort orientation from the shape of _by\_array_. When _by\_array1_ is a vertical range (one column), SORTBY sorts by row vertically. When _by\_array1_ is a horizontal range (one row), SORTBY sorts by column horizontally. In the worksheet below, names appear in row 4 and scores in row 5, arranged horizontally. The goal is to sort by score in descending order. The formula in B8 is:

    =SORTBY(B4:K5,B5:K5,-1)
    

![SORTBY function example - sort horizontally by column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sortby_example_sort_horizontally.png "SORTBY function example - sort horizontally by column")

Because _by\_array1_ (B5:K5) is a single row, SORTBY sorts by columns rather than rows. Both rows are rearranged so the highest score appears in the first column. This is different from the [SORT function](https://exceljet.net/functions/sort-function)
, which requires an explicit _by\_col_ argument set to TRUE for horizontal sorting. With SORTBY, the orientation is automatic.

### Sort by two columns

SORTBY supports multiple sort levels by providing additional _by\_array_ and _sort\_order_ pairs. In the worksheet below, the goal is to sort data first by Group in ascending order, then by Score in descending order. The formula in F5 is:

    =SORTBY(B5:D16,C5:C16,1,D5:D16,-1)
    

![SORTBY function example - sort by two columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sortby_example_sort_by_two_columns.png "SORTBY function example - sort by two columns")

The first _by\_array_ is C5:C16 (Group) with _sort\_order_ 1 (ascending), and the second _by\_array_ is D5:D16 (Score) with _sort\_order_ -1 (descending). The result is data grouped alphabetically (A first, then B), with scores sorted from highest to lowest within each group.

For more details, see [Sort by two columns](https://exceljet.net/formulas/sort-by-two-columns)
.

### Sort text by length

SORTBY can sort data by a value calculated with a formula. In the worksheet below, the goal is to sort the country names in column B by character length, with the shortest names first. The formula in D5 is:

    =SORTBY(B5:B16,LEN(B5:B16))
    

![SORTBY function example - sort by text length](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sortby_example_sort_text_by_length.png "SORTBY function example - sort by text length")

The [LEN function](https://exceljet.net/functions/len-function)
 returns an array of character counts — one for each value in B5:B16. SORTBY uses this array to sort the country names from shortest to longest. The sort values (character counts) are calculated on the fly and never appear on the worksheet.

For more details, see [Sort text by length](https://exceljet.net/formulas/sort-text-by-length)
.

### Sort by custom list

SORTBY is especially useful for sorting data in a custom, non-alphabetical order. In the worksheet below, the goal is to sort a table by the Priority column using the custom order in J5:J7 (High, Medium, Low). The formula in F5 is:

    =SORTBY(B5:D14,MATCH(D5:D14,J5:J7,0))
    

![SORTBY function example - sort by a custom list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sortby_example_sort_by_custom_list.png "SORTBY function example - sort by a custom list")

The [MATCH function](https://exceljet.net/functions/match-function)
 looks up each priority value in the custom list and returns its position: High = 1, Medium = 2, Low = 3. SORTBY uses these numeric positions to sort the data, placing High-priority items first. This approach works with any custom order — simply list the values in the desired sequence. With [XMATCH](https://exceljet.net/functions/xmatch-function)
, the formula is a bit shorter, since XMATCH defaults to an exact match:

    =SORTBY(B5:D14,XMATCH(D5:D14,J5:J7))
    

For more details, see [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)
.

### Sort birthdays by month and day

SORTBY can sort dates by month and day while ignoring the year. In the worksheet below, the goal is to sort a list of names and birthdays in calendar order. The formula in E5 is:

    =SORTBY(B5:C16,TEXT(C5:C16,"mmdd"))
    

![SORTBY function example - sort birthdays by month and day](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sortby_example_sort_birthdays.png "SORTBY function example - sort birthdays by month and day")

The [TEXT function](https://exceljet.net/functions/text-function)
 extracts just the month and day from each date using the format "mmdd" (e.g., July 18 becomes "0718"). SORTBY uses these text values to sort the data in calendar order, ignoring the birth year. Without this approach, sorting by date directly would sort by year first, placing the oldest people at the top.

For more details, see [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)
.

### Random sort

SORTBY can randomize the order of a list when combined with the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
. In the worksheet below, the goal is to shuffle the values in column B into a random order. The formula in D5 is:

    =SORTBY(B5:B16,RANDARRAY(ROWS(B5:B16)))
    

![SORTBY function example - random sort](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sortby_example_random_sort.png "SORTBY function example - random sort")

The [ROWS function](https://exceljet.net/functions/rows-function)
 returns 12 (the number of rows in B5:B16), and RANDARRAY generates 12 random decimal numbers. SORTBY uses these random values to sort the data, producing a different order each time the worksheet recalculates.

> RANDARRAY is a [volatile function](https://exceljet.net/glossary/volatile-function)
>  and will recalculate every time the worksheet changes. To keep a random order fixed, copy the results and use Paste Special > Values.

For more details, see [Random sort](https://exceljet.net/formulas/random-sort)
.

> To create random sorting that will not change and can be reproduced, see: [How to do a seeded random sort in Excel](https://exceljet.net/articles/how-to-do-a-seeded-random-sort-in-excel)
> .

### Sort by substring

SORTBY can sort data by a substring extracted with a formula. In the worksheet below, product codes contain a color between hyphens (e.g., "AX-Red-6387"). The goal is to sort the codes by color. The formula in D5 is:

    =SORTBY(B5:B16,TEXTBEFORE(TEXTAFTER(B5:B16,"-"),"-"))
    

![SORTBY function example - sort codes by substring](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sortby_example_sort_by_substring.png "SORTBY function example - sort codes by substring")

Working from the inside out, [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 extracts everything after the first hyphen (e.g., "Red-6387"), then [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 extracts everything before the next hyphen (e.g., "Red"). The result is an array of color names that SORTBY uses to group the codes by color in alphabetical order.

For more details, see [Sort by substring](https://exceljet.net/formulas/sort-by-substring)
.

### Notes

*   SORTBY returns a #VALUE! error if _by\_array_ dimensions are not compatible with _array_.
*   The _by\_array_ arguments must be a single row or a single column.
*   The _sort\_order_ argument only accepts 1 (ascending) or -1 (descending); other values return #VALUE!.
*   SORTBY returns a #SPILL! error if the output range is not empty.
*   SORTBY returns a #REF! error when referencing a closed workbook (dynamic arrays require open workbooks).
*   SORTBY is a "stable sort" — items with the same sort value maintain their original relative order.
*   SORTBY works with [Excel Tables](https://exceljet.net/articles/excel-tables)
     and [structured references](https://exceljet.net/glossary/structured-reference)
    . Results update automatically when table data changes.

SORTBY function examples
------------------------

[![Excel formula: Sort values by columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20values%20by%20columns.png "Excel formula: Sort values by columns")](https://exceljet.net/formulas/sort-values-by-columns)

### [Sort values by columns](https://exceljet.net/formulas/sort-values-by-columns)

The SORT function sorts a range using a given index, called sort\_index . Normally, this index represents a column in the source data. However, the SORT function has an optional argument called " by\_col " which allows sorting values organized in columns. To sort by column, this argument must be set...

[![Excel formula: Sort birthdays by month and day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20birthdays%20by%20month%20and%20day.png "Excel formula: Sort birthdays by month and day")](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

### [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

In this example, the goal is to sort a list of names and birthdays by month and year. The complication is that the birthdays also include a birth year, so if we try to sort the raw data by birthdays, we'll end up with a list of birthdays sorted first by year. We will actually see the oldest people...

[![Excel formula: Last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last-n-rows.png "Excel formula: Last n rows")](https://exceljet.net/formulas/last-n-rows)

### [Last n rows](https://exceljet.net/formulas/last-n-rows)

When you are working with a large table that extends beyond the visible area of a worksheet, you might want to see the most recent data in the table without scrolling to the bottom of the table. Examples of this kind of data include things like: Recent deposits or expenses Recent transactions...

[![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random_sort.png "Excel formula: Random sort")](https://exceljet.net/formulas/random-sort)

### [Random sort](https://exceljet.net/formulas/random-sort)

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the SORTBY function and the RANDARRAY function . SORTBY function The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort...

[![Excel formula: Randomly assign people to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_people_to_groups.png "Excel formula: Randomly assign people to groups")](https://exceljet.net/formulas/randomly-assign-people-to-groups)

### [Randomly assign people to groups](https://exceljet.net/formulas/randomly-assign-people-to-groups)

In this example, the goal is to randomly assign the names in column B to three groups of equal size. The group names are "A", "B", and "C", and these values appear in the named range groups (F5:F7). The solution should automatically count the number of groups to assign and attempt to generate the...

[![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")](https://exceljet.net/formulas/reverse-a-list-or-range)

### [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the SORT function...

[![Excel formula: Sort by substring](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort_by_substring.png "Excel formula: Sort by substring")](https://exceljet.net/formulas/sort-by-substring)

### [Sort by substring](https://exceljet.net/formulas/sort-by-substring)

We have a list of 12 codes in Column B. Each code consists of a prefix (two letters), a color (variable), and a 4-digit number, all separated by hyphens (e.g., AX-Red-6387). The goal is to sort this list based on the color substring so that all codes with the same color are grouped together in the...

[![Excel formula: LAMBDA contains which things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20contains%20which%20strings.png "Excel formula: LAMBDA contains which things")](https://exceljet.net/formulas/lambda-contains-which-things)

### [LAMBDA contains which things](https://exceljet.net/formulas/lambda-contains-which-things)

The goal in this example is to use a formula to report which things exist in a cell. The list of things to check for is in the named range things (E5:E9). The result is returned as a comma separated text string. The first step in creating a custom function with the LAMBDA function is to verify the...

[![Excel formula: Sort by two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20two%20columns.png "Excel formula: Sort by two columns")](https://exceljet.net/formulas/sort-by-two-columns)

### [Sort by two columns](https://exceljet.net/formulas/sort-by-two-columns)

In the example shown, we want to sort data in B5:D14 first by group in descending order. Here is the configuration needed: array = B5:D14 by\_array1 = D5:D14 sort\_order1 = 1 The formula below will sort data by group A-Z: =SORTBY(B5:D14,D5:D14,1) // sort by group only To extend the formula to sort...

[![Excel formula: Random numbers without duplicates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20numbers%20without%20duplicates.png "Excel formula: Random numbers without duplicates")](https://exceljet.net/formulas/random-numbers-without-duplicates)

### [Random numbers without duplicates](https://exceljet.net/formulas/random-numbers-without-duplicates)

In this example, the goal is to generate a list of random numbers without duplicates. This involves jumping through a few hoops because although the RANDARRAY function can easily generate a list of random integers, there is no guarantee that the numbers will be unique. In the explanation below, we'...

[![Excel formula: Sort text by length](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20text%20by%20length.png "Excel formula: Sort text by length")](https://exceljet.net/formulas/sort-text-by-length)

### [Sort text by length](https://exceljet.net/formulas/sort-text-by-length)

The SORTBY function can sort values in a range with an array that doesn't exist on the worksheet. In this example, we want to sort the values in B5:B15 by the number of characters each string contains. Working from inside out, we use the LEN function to get the length of each value: LEN(B5:B15) //...

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

[![Excel formula: Generate random text strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/generate%20random%20strings.png "Excel formula: Generate random text strings")](https://exceljet.net/formulas/generate-random-text-strings)

### [Generate random text strings](https://exceljet.net/formulas/generate-random-text-strings)

The new dynamic array formulas in Excel 365 make it much easier to solve certain tricky problems with formulas. In this example, the goal is to generate a list of random 6-character codes. The randomness is handled by the RANDARRAY function , a new function in Excel 365. RANDARRAY returns 6 random...

[![Excel formula: Random list of names](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random-list-of-names.png "Excel formula: Random list of names")](https://exceljet.net/formulas/random-list-of-names)

### [Random list of names](https://exceljet.net/formulas/random-list-of-names)

In this example, the goal is to create a list of 10 random names from a larger list of 100 names. In other words, we want to select a random subset of names from a larger list. The names to select from are in column B, starting in row 5. The formula should handle any number of names in the input...

[![Excel formula: Sort by custom list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20custom%20list.png "Excel formula: Sort by custom list")](https://exceljet.net/formulas/sort-by-custom-list)

### [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)

In this example, we are sorting a table with 10 rows and 3 columns. In the range J5:J7 (the named range custom ), the colors "red", "blue", and "green" are listed in the desired sort order. The goal is to sort the table using values in the Group column in this same custom order. The SORTBY function...

SORTBY function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Sort%20by%20custom%20list%20with%20SORTBY-Play.png)](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

### [Sort by custom list with SORTBY](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

In this video, we'll look at how to sort with SORTBY function using a custom list. One challenge that comes up frequently when sorting is a need to sort in a custom order. For example, in this worksheet, we have a list of opportunities, and we want to sort the list in the order that stages appear...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/New%20dynamic%20array%20functions%20in%20Excel-Play.png)](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

### [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

In this video, we'll quickly review new Dynamic Array functions in Excel. With the introduction of dynamic array formulas, Excel includes 6 brand new functions that directly leverage dynamic array behavior. Each of these functions is covered in more detail later in the course, so this is just a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20SORTBY%20function%20example-play.png)](https://exceljet.net/videos/basic-sortby-function-example)

### [Basic SORTBY function example](https://exceljet.net/videos/basic-sortby-function-example)

In this video, we’ll look at a basic example of sorting with the SORTBY function . In this worksheet, we have a list of names, scores, and groups. Currently, the data is not sorted. Our goal is to sort this data by group, then by score in descending order. I’ll start off by placing the cursor in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/SORT%20and%20SORTBY%20with%20multiple%20columns-Play_0.png)](https://exceljet.net/videos/sort-and-sortby-with-multiple-columns)

### [SORT and SORTBY with multiple columns](https://exceljet.net/videos/sort-and-sortby-with-multiple-columns)

In this video, we’ll look at how to sort by multiple columns with the SORT and SORTBY functions. In this worksheet, we have a list of names, projects, values, and regions. This data is not sorted. Our goal is to sort the data first by region, then by name, and finally by value, with larger values...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20perform%20a%20random%20sort-Play_0.png)](https://exceljet.net/videos/how-to-perform-a-random-sort)

### [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)

In this video, we’ll look at how to perform a random sort with the SORTBY function , with help from the RANDARRAY function . In this worksheet, we have the first 10 letters in the alphabet in the range B5:B14. How can we sort this data in random order? One way to do this is to add a helper column...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)
    
*   [Sort by substring](https://exceljet.net/formulas/sort-by-substring)
    
*   [Sort text by length](https://exceljet.net/formulas/sort-text-by-length)
    
*   [Sort values by columns](https://exceljet.net/formulas/sort-values-by-columns)
    
*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    
*   [Generate random text strings](https://exceljet.net/formulas/generate-random-text-strings)
    
*   [Sort by two columns](https://exceljet.net/formulas/sort-by-two-columns)
    
*   [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)
    
*   [Last n rows](https://exceljet.net/formulas/last-n-rows)
    
*   [Random list of names](https://exceljet.net/formulas/random-list-of-names)
    

### Videos

*   [Basic SORTBY function example](https://exceljet.net/videos/basic-sortby-function-example)
    
*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
    
*   [SORT and SORTBY with multiple columns](https://exceljet.net/videos/sort-and-sortby-with-multiple-columns)
    
*   [Sort by custom list with SORTBY](https://exceljet.net/videos/sort-by-custom-list-with-sortby)
    
*   [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

### Links

*   [Microsoft SORTBY function documentation](https://support.office.com/en-us/article/sortby-function-cd2d7a62-1b93-435c-b561-d6a35134f28f)
    

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