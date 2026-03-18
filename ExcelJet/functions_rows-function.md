# Excel ROWS function | Exceljet

**Source:** https://exceljet.net/functions/rows-function

---

[Skip to main content](https://exceljet.net/functions/rows-function#main-content)

[](https://exceljet.net/functions/rows-function#)

*   [Previous](https://exceljet.net/functions/row-function)
    
*   [Next](https://exceljet.net/functions/transpose-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

ROWS Function
=============

by Dave Bruns · Updated 3 Nov 2023

Related functions 
------------------

[ROW](https://exceljet.net/functions/row-function)

[COLUMN](https://exceljet.net/functions/column-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

![Excel ROWS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")

Summary
-------

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

Purpose 
--------

Get the number of rows in an array or reference.

Return value 
-------------

Number of rows

Syntax
------

    =ROWS(array)

*   _array_ - A reference to a cell or range of cells.

Using the ROWS function 
------------------------

The ROWS function returns the count of rows in a given reference as a number. For example, =ROWS(A1:A5) returns 5, since the range A1:A5 contains 5 rows. ROWS takes just one argument, called _array_, which can be a [range](https://exceljet.net/glossary/range)
 or [array](https://exceljet.net/glossary/array)
.

### Examples

Use the ROWS function to get the row count for a given reference or range. For example, there are 10 rows in the range A1:F10 so the formula below returns 10:

    =ROWS(A1:F10) // returns 10
    

The range A1:Z100 contains 100 rows, so the formula below returns 100: 

    =ROWS(A1:Z100) // returns 100
    

You can also use the ROWS function to get a row count for an [array constant](https://exceljet.net/glossary/array-constant)
:

    =ROWS({1;2;3;4;5}) // returns 5
    

Although there is no built-in function to count the number of cells in a range, you can use the ROWS function together with the [COLUMNS function](https://exceljet.net/functions/columns-function)
 like this:

    =COLUMNS(range)*ROWS(range) // total cells
    =COLUMNS(A1:Z100)*ROWS(A1:Z100) // returns 2600
    

[This article](https://exceljet.net/formulas/count-cells-in-range)
 explains this formula in more detail.

### Notes

*   _Array_ can be a range or a reference to a single contiguous group of cells.
*   _Array_ can be an [array constant](https://exceljet.net/glossary/array-constant)
     or an [array](https://exceljet.net/glossary/array)
     created by another formula.
*   To count _columns_, see the [COLUMNS function](https://exceljet.net/functions/columns-function)
    .
*   To get row _numbers_, see the [ROW function](https://exceljet.net/functions/row-function)
    .
*   To _lookup_ a row number, see the [MATCH function](https://exceljet.net/functions/match-function)
    .

ROWS function examples
----------------------

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

[![Excel formula: Random list of names](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random-list-of-names.png "Excel formula: Random list of names")](https://exceljet.net/formulas/random-list-of-names)

### [Random list of names](https://exceljet.net/formulas/random-list-of-names)

In this example, the goal is to create a list of 10 random names from a larger list of 100 names. In other words, we want to select a random subset of names from a larger list. The names to select from are in column B, starting in row 5. The formula should handle any number of names in the input...

[![Excel formula: Combine ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/combine_ranges.png "Excel formula: Combine ranges")](https://exceljet.net/formulas/combine-ranges)

### [Combine ranges](https://exceljet.net/formulas/combine-ranges)

In this example, the goal is to combine ranges. With the introduction of the VSTACK function and the HSTACK function, this is quite a simple task. To combine ranges vertically, stacking one range on top of another, you can use the VSTACK function like this: =VSTACK(range1,range2) To combine ranges...

[![Excel formula: Count table rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20table%20rows.png "Excel formula: Count table rows")](https://exceljet.net/formulas/count-table-rows)

### [Count table rows](https://exceljet.net/formulas/count-table-rows)

This formula uses structured referencing , a syntax that allows table parts to be called out by name. When a table is called with the name only, Excel returns a reference to the data region of the table only. In this case, the entire table range is B4:F104 so Table1 returns the range B5:F105 to the...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: First column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20column%20in%20range.png "Excel formula: First column number in range")](https://exceljet.net/formulas/first-column-number-in-range)

### [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. In the example shown the array looks like this...

[![Excel formula: Last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last-n-rows.png "Excel formula: Last n rows")](https://exceljet.net/formulas/last-n-rows)

### [Last n rows](https://exceljet.net/formulas/last-n-rows)

When you are working with a large table that extends beyond the visible area of a worksheet, you might want to see the most recent data in the table without scrolling to the bottom of the table. Examples of this kind of data include things like: Recent deposits or expenses Recent transactions...

[![Excel formula: Count cells in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_cells_in_range.png "Excel formula: Count cells in range")](https://exceljet.net/formulas/count-cells-in-range)

### [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)

The goal is to count the number of cells in a given range, regardless of whether the cells are empty or not. Although Excel has several functions designed to count cells based on their contents, there is no built-in function for counting the total number of cells in a range. The classic solution is...

[![Excel formula: Total rows in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20rows%20in%20range.png "Excel formula: Total rows in range")](https://exceljet.net/formulas/total-rows-in-range)

### [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)

The ROWS function is fully automatic. When you provide a range to ROWS, it will return a count of all rows in the range. In the example, the formula in F5 returns 6, because there are 6 rows in the range B5:C10: =ROWS(B5:C10) // count rows ROWS counts the number of rows in any supplied range and...

[![Excel formula: Dynamic date list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20date%20list.png "Excel formula: Dynamic date list")](https://exceljet.net/formulas/dynamic-date-list)

### [Dynamic date list](https://exceljet.net/formulas/dynamic-date-list)

Dates in Excel are just serial numbers , formatted to display as dates. This means you can perform math operations on dates to calculate days in the future or past. In the example shown, the date in the named range "start" is provided by the TODAY function: =TODAY() //returns current date The...

[![Excel formula: Get address of named range or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_named_range_or_table.png "Excel formula: Get address of named range or table")](https://exceljet.net/formulas/get-address-of-named-range-or-table)

### [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)

The goal is to return the full address of a range or named range as text. The purpose of this formula is informational, not functional. It provides a way to inspect the current range for a named range, an Excel Table, or even the result of a formula. The core of the solutions explained below is the...

[![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")](https://exceljet.net/formulas/reverse-a-list-or-range)

### [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the SORT function...

[![Excel formula: Display sorted values with helper column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/display%20sorted%20values%20with%20helper%20column.png "Excel formula: Display sorted values with helper column")](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

### [Display sorted values with helper column](https://exceljet.net/formulas/display-sorted-values-with-helper-column)

This formula relies on a helper column that already contains a sequential list of numbers to represent an established sort order. The numbers in the helper column are independent of the operation of this formula. As long as the sequence is continuous, it can represent an ascending or descending...

[![Excel formula: Random value from list or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20value%20from%20list%20or%20table.png "Excel formula: Random value from list or table")](https://exceljet.net/formulas/random-value-from-list-or-table)

### [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)

Note: this formula uses the named range "data" (B5:E104) for readability and convenience. If you don't want to use a named range, substitute $B$5:$E$104 instead. To pull a random value out of a list or table, we'll need a random row number. For that, we'll use the RANDBETWEEN function, which...

[![Excel formula: Average last N values in a table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Average%20last%20N%20values%20in%20a%20table.png "Excel formula: Average last N values in a table")](https://exceljet.net/formulas/average-last-n-values-in-a-table)

### [Average last N values in a table](https://exceljet.net/formulas/average-last-n-values-in-a-table)

This formula is a good example of how structured references can make working with data in Excel much easier. At the core, this is what we're doing: =AVERAGE(first:last) where "first" is a reference to the first cell to include in the average and "last" is a reference to the last cell to include...

ROWS function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Introduction%20to%20structured%20references_thumb.png)](https://exceljet.net/videos/introduction-to-structured-references)

### [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)

In this video, I'll give a brief introduction to structured references. A structured reference is a term for using a table name in a formula instead of a normal cell reference. Structured references are optional, and can be used with formulas both inside or outside an Excel table. Let's take a look...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20count%20items%20in%20a%20filtered%20list%20with%20the%20SUBTOTAL%20function_thumb.png)](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)

### [How to count items in a filtered list](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)

When you're working with filtered lists, you might want to know how many items are in the list and how many items are currently visible. In this video, we'll show you how to add a message at the top of a filtered list that displays this information. Here we have a list of properties. If we enable "...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20a%20dynamic%20named%20range-thumb.png)](https://exceljet.net/videos/what-is-a-dynamic-named-range)

### [What is a dynamic named range](https://exceljet.net/videos/what-is-a-dynamic-named-range)

In this video we'll introduce the idea of a dynamic range and show you why you might want to use one. Let's take a look. In this first worksheet, we have a list of ten properties set up in a normal way. If we check the formulas that summarize this data to the right, you can see that each formula...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20a%20Table-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)

### [How to create a dynamic named range with a Table](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)

In this video we'll look at how to create a dynamic named range with a Table. This is the simplest way to create a dynamic named range in Excel. This table contains data for ten properties. I can easily create a named range for this data. For example, I can create a range called "data." Then, using...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20named%20range-thumb.png)](https://exceljet.net/videos/how-to-create-a-named-range)

### [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)

Named ranges are one of the most useful features in Excel. They make your formulas much easier to read and understand; they automatically give you absolute references , and they reduce errors. Let's take a look at a few ways to create named ranges. The simplest way to create a named range is to use...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20perform%20a%20random%20sort-Play_0.png)](https://exceljet.net/videos/how-to-perform-a-random-sort)

### [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)

In this video, we’ll look at how to perform a random sort with the SORTBY function , with help from the RANDARRAY function . In this worksheet, we have the first 10 letters in the alphabet in the range B5:B14. How can we sort this data in random order? One way to do this is to add a helper column...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20remove%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-remove-an-excel-table)

### [How to remove an Excel Table](https://exceljet.net/videos/how-to-remove-an-excel-table)

In this video, we'll look at how to remove a table from an Excel worksheet. In this workbook, we have a number of Excel Tables . Let's look at some ways you can remove these tables. You won't find a "delete table" command in Excel. To completely remove an Excel table, and all associated data, you'...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20Excel%20Table%20ranges%20work-Thumb.png)](https://exceljet.net/videos/how-excel-table-ranges-work)

### [How Excel Table ranges work](https://exceljet.net/videos/how-excel-table-ranges-work)

In this video, we'll take a closer look at how table ranges work. One of the most useful features of Excel Tables is that they create a dynamic range. A dynamic range automatically expands to handle new data, so it works well for reports, pivot tables, or charts that need to show the latest...

Related functions
-----------------

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)
    
*   [Dynamic date list](https://exceljet.net/formulas/dynamic-date-list)
    
*   [Random value from list or table](https://exceljet.net/formulas/random-value-from-list-or-table)
    
*   [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)
    
*   [Average last N values in a table](https://exceljet.net/formulas/average-last-n-values-in-a-table)
    
*   [Multiple matches into separate rows](https://exceljet.net/formulas/multiple-matches-into-separate-rows)
    
*   [Random list of names](https://exceljet.net/formulas/random-list-of-names)
    
*   [Combine ranges](https://exceljet.net/formulas/combine-ranges)
    
*   [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)
    
*   [Random sort](https://exceljet.net/formulas/random-sort)
    

### Videos

*   [How to create a dynamic named range with a Table](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)
    
*   [What is a dynamic named range](https://exceljet.net/videos/what-is-a-dynamic-named-range)
    
*   [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)
    
*   [How to count items in a filtered list](https://exceljet.net/videos/how-to-count-items-in-a-filtered-list)
    
*   [How Excel Table ranges work](https://exceljet.net/videos/how-excel-table-ranges-work)
    
*   [How to remove an Excel Table](https://exceljet.net/videos/how-to-remove-an-excel-table)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    
*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
    
*   [How to perform a random sort](https://exceljet.net/videos/how-to-perform-a-random-sort)
    

### Functions

*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    

### Links

*   [Microsoft ROWS function documentation](https://support.office.com/en-us/article/rows-function-b592593e-3fc2-47f2-bec1-bda493811597)
    

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