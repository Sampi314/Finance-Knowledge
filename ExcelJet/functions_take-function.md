# Excel TAKE function | Exceljet

**Source:** https://exceljet.net/functions/take-function

---

[Skip to main content](https://exceljet.net/functions/take-function#main-content)

[](https://exceljet.net/functions/take-function#)

*   [Previous](https://exceljet.net/functions/stockhistory-function)
    
*   [Next](https://exceljet.net/functions/textafter-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

TAKE Function
=============

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[DROP](https://exceljet.net/functions/drop-function)

[CHOOSEROWS](https://exceljet.net/functions/chooserows-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

[EXPAND](https://exceljet.net/functions/expand-function)

![Excel TAKE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")

Summary
-------

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

Purpose 
--------

Get a subset of an array

Return value 
-------------

A subset of a given array

Syntax
------

    =TAKE(array,[rows],[col])

*   _array_ - The source array or range.
*   _rows_ - \[optional\] Number of rows to return as an integer.
*   _col_ - \[optional\] Number of columns to return as an integer.

Using the TAKE function 
------------------------

The TAKE function returns a subset of a given array. The size of the array returned is determined by separate _rows_ and _columns_ arguments. When positive numbers are provided for rows or columns, TAKE will retrieve values from the start or top of the array. Negative numbers take values from the end or bottom of the array.

The TAKE function takes three arguments: _array_, _rows_, and _columns_. _Array_ is required, along with at least one value for _rows_ or _columns_. _Array_ can be a [range](https://exceljet.net/glossary/range)
 or an [array](https://exceljet.net/glossary/array)
 from another formula. _Rows_ and _columns_ can be negative or positive integers. Positive numbers take values from the _start_ of the array; negative numbers take values from the _end_ of the array. Both _rows_ and _columns_ default to _total_ rows and columns. If no value is supplied, TAKE will return _all_ rows/columns in the result.

### Basic usage

To use TAKE, provide an [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
, and a value for rows and/or columns:

    =TAKE(array,3) // get first 3 rows
    =TAKE(array,,3) // get first 3 columns
    =TAKE(array,3,2) // get first 3 rows and 2 columns
    

Notice in the second example above, no value is provided for _rows_.

### Take from start

To get rows or columns from the _start_ of a range or array, provide _positive_ numbers for rows and columns. In the worksheet below, the formula in F3 is:

    =TAKE(B3:D11,3)
    

The TAKE function returns the first 3 rows from B3:D11. The formula in F8 is:

    =TAKE(B3:D11,4,2)
    

The TAKE function returns the first 2 columns of the first 4 rows.

![TAKE function - basic example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TAKE%20function%20-%20basic%20usage.png?itok=X6sWhs-j "TAKE function - basic example")

Notice that if a number for _rows_ or _columns_ is not provided, TAKE returns _all_ rows or columns. For example, in the first formula above, a value for _columns_ is not provided so TAKE returns all 3 columns as a result. Also notice that positive numbers for _rows_ or _columns_ take values from the _start_ of the _array_.

### Take from end

When negative numbers are provided for _rows_ or _columns,_ the TAKE function returns values from the _end_ of the _array_. In the worksheet below, the first formula in cell F3 returns the last 3 rows of the range B3:D11:

    =TAKE(B3:D11,-3)
    

The formula in F8 returns the last 2 columns of the last 4 rows:

    =TAKE(B3:D11,-4,-2)
    

![TAKE function - extract from end of array](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TAKE%20function%20-%20extract%20from%20end%20of%20array.png?itok=QmstexmJ "TAKE function - extract from end of array")

Notice in the first example no value is provided for _columns_ so TAKE returns _all_ columns.

### Last column or row

To return the last complete column or row with TAKE, you can use formulas like this:

    =TAKE(array,-1) // last row
    =TAKE(array,,-1) // last column
    

Note in the second example the _rows_ argument is simply not provided. Extending these examples, we can get the last 3 rows or columns like this:

    =TAKE(array,-3) // last 3 rows
    =TAKE(array,,-3) // last 3 columns
    

### TAKE vs. DROP

The DROP and TAKE functions both return a subset of an array, but they work in opposite ways. While the [DROP function](https://exceljet.net/functions/drop-function)
 _removes_ specific rows or columns from an array, the [TAKE function](https://exceljet.net/functions/take-function)
 _extracts_ specific rows or columns from an array:

    =DROP(array,1) // remove first row
    =TAKE(array,1) // get first row
    

Which function to use depends on the situation.

### Notes

*   _Rows_ and _columns_ are both optional, but at least one must be provided.
*   If _rows_ or _columns_ are zero, TAKE returns a #VALUE error.
*   If _rows_ > total rows, all rows are returned.
*   If _columns_ > total columns, all columns are returned.

TAKE function examples
----------------------

[![Excel formula: Get address of named range or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_named_range_or_table.png "Excel formula: Get address of named range or table")](https://exceljet.net/formulas/get-address-of-named-range-or-table)

### [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)

The goal is to return the full address of a range or named range as text. The purpose of this formula is informational, not functional. It provides a way to inspect the current range for a named range, an Excel Table, or even the result of a formula. The core of the solutions explained below is the...

[![Excel formula: Sum first n matching values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20first%20n%20matching%20values_0.png "Excel formula: Sum first n matching values")](https://exceljet.net/formulas/sum-first-n-matching-values)

### [Sum first n matching values](https://exceljet.net/formulas/sum-first-n-matching-values)

In this example, the goal is to sum the first n matching values in a set of data. Specifically, we want to sum the first 3 values for both Red and Blue, based on the order they appear in the table. There are 12 values total; 6 entries each for Red and Blue. All data is in Excel Table named data in...

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

[![Excel formula: Get last match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match.png "Excel formula: Get last match")](https://exceljet.net/formulas/get-last-match)

### [Get last match](https://exceljet.net/formulas/get-last-match)

In the example shown, we have a set of order data that includes Date, Product, Name, and Amount. The data is sorted by date in ascending order. The goal is to look up the latest order for a given person by Name. In other words, we want the last match by name. The challenge is that Excel lookup...

[![Excel formula: Get information about max value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_information_corresponding_to_max_value.png "Excel formula: Get information about max value")](https://exceljet.net/formulas/get-information-about-max-value)

### [Get information about max value](https://exceljet.net/formulas/get-information-about-max-value)

An interesting problem in Excel is how to look up information related to the maximum value in a set of data. For example, if you have a dataset of property listings and prices, you might want to find details about the property with the highest price. The best way to solve this problem depends on...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: Sum last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_rows.png "Excel formula: Sum last n rows")](https://exceljet.net/formulas/sum-last-n-rows)

### [Sum last n rows](https://exceljet.net/formulas/sum-last-n-rows)

In the example shown, we have a list of amounts in column C. The goal is to dynamically sum the last n amounts using the number that appears in cell E5 for n . Since the list may grow over time, the key requirement is to sum amounts by position. For convenience only, the values to sum are in the...

[![Excel formula: Last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last-n-rows.png "Excel formula: Last n rows")](https://exceljet.net/formulas/last-n-rows)

### [Last n rows](https://exceljet.net/formulas/last-n-rows)

When you are working with a large table that extends beyond the visible area of a worksheet, you might want to see the most recent data in the table without scrolling to the bottom of the table. Examples of this kind of data include things like: Recent deposits or expenses Recent transactions...

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

[![Excel formula: Lookup first negative value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20first%20negative%20value.png "Excel formula: Lookup first negative value")](https://exceljet.net/formulas/lookup-first-negative-value)

### [Lookup first negative value](https://exceljet.net/formulas/lookup-first-negative-value)

In this example, the goal is to lookup the first negative value in a set of data. In addition, we also want to get the corresponding date. All data is in an Excel Table called data, in the range B5:C16. This information represents the low temperature in Fahrenheit (F) for the dates as shown. There...

[![Excel formula: Sum first n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_first_n_rows.png "Excel formula: Sum first n rows")](https://exceljet.net/formulas/sum-first-n-rows)

### [Sum first n rows](https://exceljet.net/formulas/sum-first-n-rows)

In the example shown, we have a list of amounts by month. The goal is to dynamically sum values through a given number of months using a variable n in cell E5. Since month names are just text, and months are listed in order, the key requirement is to sum amounts by position , starting with cell C5...

[![Excel formula: 10 most common text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/10%20most%20common%20text%20values.png "Excel formula: 10 most common text values")](https://exceljet.net/formulas/10-most-common-text-values)

### [10 most common text values](https://exceljet.net/formulas/10-most-common-text-values)

In this example, the goal is to list the 10 most frequently occurring text values in a range, in descending order by count, as seen in the range in E5:F14. This is an advanced formula that requires a number of nested functions. However, it is an excellent example of the power of dynamic array...

[![Excel formula: Random list of names](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random-list-of-names.png "Excel formula: Random list of names")](https://exceljet.net/formulas/random-list-of-names)

### [Random list of names](https://exceljet.net/formulas/random-list-of-names)

In this example, the goal is to create a list of 10 random names from a larger list of 100 names. In other words, we want to select a random subset of names from a larger list. The names to select from are in column B, starting in row 5. The formula should handle any number of names in the input...

[![Excel formula: Average last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_5_columns.png "Excel formula: Average last n columns")](https://exceljet.net/formulas/average-last-n-columns)

### [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)

In this example, the goal is to average the last n columns in a set of data, where n is a variable entered in cell K5 that can be changed at any time. Since more data may be added, a key requirement is to average amounts by position. For convenience, the values to average are in the named range...

[![Excel formula: Sum last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_columns.png "Excel formula: Sum last n columns")](https://exceljet.net/formulas/sum-last-n-columns)

### [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)

In this example, the goal is to sum the last n columns in a set of data, where n is a variable that can be changed at any time. In the latest version of Excel, the easiest way to solve this problem is with the TAKE function . In older versions of Excel you can use the OFFSET function , as explained...

Related functions
-----------------

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

[![Excel CHOOSEROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20chooserows%20function.png "Excel CHOOSEROWS function")](https://exceljet.net/functions/chooserows-function)

### [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)

The Excel CHOOSEROWS function returns specific rows from an array or range. The rows to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a row in the given array.

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

[![Excel EXPAND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20expand%20function.png "Excel EXPAND function")](https://exceljet.net/functions/expand-function)

### [EXPAND Function](https://exceljet.net/functions/expand-function)

The EXPAND function expands an array by adding rows and columns, which are supplied as separate arguments. The numbers given for rows and columns represent the dimensions of the final array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [Sum last n rows](https://exceljet.net/formulas/sum-last-n-rows)
    
*   [Sum first n rows](https://exceljet.net/formulas/sum-first-n-rows)
    
*   [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    
*   [10 most common text values](https://exceljet.net/formulas/10-most-common-text-values)
    
*   [Random list of names](https://exceljet.net/formulas/random-list-of-names)
    
*   [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)
    
*   [Filter and exclude columns](https://exceljet.net/formulas/filter-and-exclude-columns)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    
*   [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)
    

### Functions

*   [DROP Function](https://exceljet.net/functions/drop-function)
    
*   [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    
*   [EXPAND Function](https://exceljet.net/functions/expand-function)
    

### Links

*   [Microsoft TAKE function documentation](https://support.microsoft.com/en-us/office/take-function-25382ff1-5da1-4f78-ab43-f33bd2e4e003)
    

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