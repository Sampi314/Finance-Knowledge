# Get information about max value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-information-about-max-value

---

[Skip to main content](https://exceljet.net/formulas/get-information-about-max-value#main-content)

[](https://exceljet.net/formulas/get-information-about-max-value#)

*   [Previous](https://exceljet.net/formulas/get-first-text-value-in-a-row)
    
*   [Next](https://exceljet.net/formulas/get-last-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get information about max value
===============================

by Dave Bruns · Updated 29 Apr 2025

Related functions 
------------------

[TAKE](https://exceljet.net/functions/take-function)

[SORT](https://exceljet.net/functions/sort-function)

[MAX](https://exceljet.net/functions/max-function)

[MATCH](https://exceljet.net/functions/match-function)

[INDEX](https://exceljet.net/functions/index-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7929/download?token=jmWDK0na)
 (17.86 KB)

![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")

Summary
-------

To get information related to the maximum value in a range, you can use a formula based on the [TAKE function](https://exceljet.net/functions/take-function)
 and the [SORT function](https://exceljet.net/functions/sort-function)
. In the example shown, the formula in G5 is:

    =TAKE(SORT(data,2,-1),1)
    

where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:E16. The result is all information related to the property at 4960 Roseland, which has the maximum price in the data shown.

_Note: In older versions of Excel without TAKE and SORT, you can use an_ [_INDEX and MATCH formula_](https://exceljet.net/articles/index-and-match)
_. See below for details._

Generic formula
---------------

    =TAKE(SORT(range,2,-1),1)

Explanation 
------------

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on which version of Excel you use. In Excel 2019 and earlier, the classic solution is to use the MAX function to find the maximum value, then use this value in an INDEX and MATCH formula as the lookup value. In the current version of Excel, there is a better way. Instead of performing a lookup operation, you can use the SORT function to sort by price in descending order, and then use the TAKE function to retrieve the first row.

This new approach is simple and elegant, and it greatly simplifies many complicated formulas. The article explains the new approach based on SORT and TAKE, as well as the traditional approach based on INDEX and MATCH. Don’t forget to download the worksheet and try it out yourself.

### The goal

The goal is to retrieve information related to the maximum price in the worksheet shown. Specifically, we want to return all four columns of data (Location, Price, Beds, and Baths) for the property with the highest price. If the data changes, the formula should automatically recalculate and display updated information. For convenience, all property information is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data**.

### TAKE function

The TAKE function in Excel allows you to return a subset of a given array. The size of the array returned is determined by separate _rows_ and _columns_ arguments. The generic syntax looks like this:

    =TAKE(range,rows,columns)

For example, to retrieve the first row in a range, you can use TAKE like this:

    =TAKE(range,1) // get first row

When positive numbers are provided for rows or columns, TAKE will get values from the _start_ of the array. When negative numbers are provided, TAKE will get values from the end of the array.

For more details, see [How to use the TAKE function](https://exceljet.net/functions/take-function)

### SORT function

The SORT function in Excel allows you to sort a range or array in either ascending or descending order. For this problem, the generic syntax for SORT looks like this:

    =SORT(array,sort_index,sort_order)

_Sort\_index_ is a number representing the column to sort by. _Sort\_order_ controls sort direction and can be provided as 1 (ascending) or -1 (descending). For example, to sort a range by the second column of data, you can use SORT like this:

    =SORT(range,2,1) // sort by column 2 ascending
    =SORT(range,2,-1) // sort by column 2 descending

For more details, see [How to use the SORT function](https://exceljet.net/functions/sort-function)

### TAKE with SORT

An efficient way to solve this problem is to combine the TAKE and SORT functions. In the example shown, we want to get all information related to the most expensive property. This can be done with a formula that combines SORT and TAKE like this:

    =TAKE(SORT(data,2,-1),1)

Working from the inside out, the SORT function first sorts the data by price in _descending_ order:

    SORT(data,2,-1) // sort descending by price

By itself, SORT returns _all data in a single array,_ with the most expensive property listed first:

![SORT function on its own](https://exceljet.net/sites/default/files/images/formulas/inline/get_information_about_max_value_sort_function.png "SORT function on its own")

The sorted array is then handed off to the TAKE function, which is configured to return just row 1:

    =TAKE(SORT(data,2,-1),1)

The result from TAKE is an [array](https://exceljet.net/glossary/array)
 with 4 values like this:

    {"4960 Roseland",849900,4,3}

This array lands in cell G5, and the 4 values [spill](https://exceljet.net/glossary/spill)
 into the range G5:J5.

### FILTER with LARGE

Because this is Excel, there is _always_ another way to solve the same problem :) Here is another good formula:

    =FILTER(data,data[Price]=LARGE(data[Price],1))

In this formula, we use the LARGE function to get the maximum price, then use the FILTER function to extract rows where the price equals the maximum price. For more details, see [How to use the FILTER function](https://exceljet.net/functions/filter-function)
 and [How to use the LARGE function](https://exceljet.net/functions/large-function)
.

### INDEX and MATCH

If you are using an older version of Excel without TAKE, SORT, or FILTER, you can solve this problem with an alternative method based on an INDEX and MATCH formula like this:

    =INDEX(data,MATCH(MAX(data[Price]),data[Price],0),1)

Working from the inside out, the [MAX function](https://exceljet.net/functions/max-function)
 first extracts the maximum value from the Price column:

    MAX(data[Price]) // returns 849900

This value is then provided to the [MATCH function](https://exceljet.net/functions/match-function)
 as the _lookup\_value_, with _lookup\_array_ given as the Price column, and _match\_type_ is set to zero (0) for an exact match:

    MATCH(849900,data[Price],0) // returns 6

Using this information, the MATCH function returns the row number of the maximum price (6) directly to INDEX as _row\_num_:

    =INDEX(data,6,1) // returns "4960 Roseland"

The [INDEX function](https://exceljet.net/functions/index-function)
 then returns the value at row 6 and column 1 of the table, which is "4960 Roseland". In case of duplicates (i.e., two or more max values that are the same), the formula will return info for the _first match_, the default behavior of the MATCH function. The other three columns can be retrieved in the same way by adjusting the column number as needed:

    =INDEX(data,MATCH(MAX(data[Price]),data[Price],0),2) // price
    =INDEX(data,MATCH(MAX(data[Price]),data[Price],0),3) // beds
    =INDEX(data,MATCH(MAX(data[Price]),data[Price],0),4) // baths

For a complete overview of INDEX with MATCH, see [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

Related formulas
----------------

[![Excel formula: Position of max value in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/position%20of%20max%20value%20in%20list.png "Excel formula: Position of max value in list")](https://exceljet.net/formulas/position-of-max-value-in-list)

### [Position of max value in list](https://exceljet.net/formulas/position-of-max-value-in-list)

In this formula, the goal is to return the numeric position of the most expensive property in the list. The formula in cell I5 is: =MATCH(MAX(C3:C11),C3:C11,0) The MAX function extracts the maximum value from the range C3:C11. In this case, that value is 849900. This number is then supplied to the...

[![Excel formula: Lookup latest price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20latest%20price.png "Excel formula: Lookup latest price")](https://exceljet.net/formulas/lookup-latest-price)

### [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)

The LOOKUP function assumes data is sorted, and always does an approximate match. If the lookup value is greater than all values in the lookup array, default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors,...

[![Excel formula: Max by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_by_month.png "Excel formula: Max by month")](https://exceljet.net/formulas/max-by-month)

### [Max by month](https://exceljet.net/formulas/max-by-month)

In this example, the goal is to get the maximum value in the data for each month listed in column E. The easiest way to do this is with the MAXIFS function, which is designed to return a maximum value based on one or more criteria. In older versions of Excel without the MAXIFS function, you can use...

Related functions
-----------------

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20SORT%20function%20example-Play.png)](https://exceljet.net/videos/basic-sort-function-example)

### [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)

In this video, we’ll look at a basic example of sorting with the SORT function . Sorting with formulas is one of those traditionally hard problems in Excel that new dynamic array formulas have made much easier. In this worksheet, we have a list of names, scores, and groups. Currently the data is...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Position of max value in list](https://exceljet.net/formulas/position-of-max-value-in-list)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    
*   [Max by month](https://exceljet.net/formulas/max-by-month)
    

### Functions

*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Videos

*   [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)
    

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