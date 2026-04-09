# Excel COLUMNS function | Exceljet

**Source:** https://exceljet.net/functions/columns-function

---

[Skip to main content](https://exceljet.net/functions/columns-function#main-content)

[](https://exceljet.net/functions/columns-function#)

*   [Previous](https://exceljet.net/functions/column-function)
    
*   [Next](https://exceljet.net/functions/fieldvalue-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

COLUMNS Function
================

by Dave Bruns · Updated 3 Nov 2023

Related functions 
------------------

[ROWS](https://exceljet.net/functions/rows-function)

[ROW](https://exceljet.net/functions/row-function)

[COLUMN](https://exceljet.net/functions/column-function)

![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")

Summary
-------

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

Purpose 
--------

Get the number of columns in an array or reference.

Return value 
-------------

Number of columns

Syntax
------

    =COLUMNS(array)

*   _array_ - A reference to a range of cells.

Using the COLUMNS function 
---------------------------

The COLUMNS function returns the count of columns in a given reference as a number. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns. COLUMNS takes just one argument, called _array_, which should be a [range](https://exceljet.net/glossary/range)
 or [array](https://exceljet.net/glossary/array)
.

### Examples

Use the COLUMNS function to get the column count for a given reference or range. For example, there are 6 columns in the range A1:F1 so the formula below returns 6:

    =COLUMNS(A1:F1) // returns 6
    

The range A1:Z100 contains 26 columns, so the formula below returns 100: 

    =COLUMNS(A1:Z100) // returns 26
    

You can also use the COLUMNS function to get a column count for an [array constant](https://exceljet.net/glossary/array-constant)
:

    =COLUMNS({1,2,3,4,5}) // returns 5
    

Although there is no built-in function to count the number of cells in a range, you can use the COLUMNS function together with the [ROWS function](https://exceljet.net/functions/rows-function)
 like this:

    =COLUMNS(range)*ROWS(range) // total cells
    =COLUMNS(A1:Z100)*ROWS(A1:Z100) // returns 2600
    

[More details here](https://exceljet.net/formulas/count-cells-in-range)
.

### Notes

*   _Array_ can be a range or a reference to a single contiguous group of cells.
*   _Array_ can be an [array constant](https://exceljet.net/glossary/array-constant)
     or an [array](https://exceljet.net/glossary/array)
     created by another formula.
*   To count rows, see the [ROW function](https://exceljet.net/functions/row-function)
    .
*   To get column _numbers_, see the [COLUMN function](https://exceljet.net/functions/column-function)
    .
*   To _lookup_ a column number, see the [MATCH function](https://exceljet.net/functions/match-function)
    .

COLUMNS function examples
-------------------------

[![Excel formula: Average last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_5_columns.png "Excel formula: Average last n columns")](https://exceljet.net/formulas/average-last-n-columns)

### [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)

In this example, the goal is to average the last n columns in a set of data, where n is a variable entered in cell K5 that can be changed at any time. Since more data may be added, a key requirement is to average amounts by position. For convenience, the values to average are in the named range...

[![Excel formula: Combine ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/combine_ranges.png "Excel formula: Combine ranges")](https://exceljet.net/formulas/combine-ranges)

### [Combine ranges](https://exceljet.net/formulas/combine-ranges)

In this example, the goal is to combine ranges. With the introduction of the VSTACK function and the HSTACK function, this is quite a simple task. To combine ranges vertically, stacking one range on top of another, you can use the VSTACK function like this: =VSTACK(range1,range2) To combine ranges...

[![Excel formula: Sum last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_columns.png "Excel formula: Sum last n columns")](https://exceljet.net/formulas/sum-last-n-columns)

### [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)

In this example, the goal is to sum the last n columns in a set of data, where n is a variable that can be changed at any time. In the latest version of Excel, the easiest way to solve this problem is with the TAKE function . In older versions of Excel you can use the OFFSET function , as explained...

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

[![Excel formula: Count cells in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_cells_in_range.png "Excel formula: Count cells in range")](https://exceljet.net/formulas/count-cells-in-range)

### [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)

The goal is to count the number of cells in a given range, regardless of whether the cells are empty or not. Although Excel has several functions designed to count cells based on their contents, there is no built-in function for counting the total number of cells in a range. The classic solution is...

[![Excel formula: Total columns in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20columns%20in%20range.png "Excel formula: Total columns in range")](https://exceljet.net/formulas/total-columns-in-range)

### [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)

The COLUMNS function is fully automatic. When you provide a range to COLUMNS, it will return a count of all columns in the range. In the example, the formula in F6 returns 2, because there are 2 columns in the range B5:C10: =COLUMNS(B5:C10) // count columns COLUMNS counts the number of columns in...

[![Excel formula: Count table columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20table%20columns.png "Excel formula: Count table columns")](https://exceljet.net/formulas/count-table-columns)

### [Count table columns](https://exceljet.net/formulas/count-table-columns)

This formula uses structured referencing , a syntax that allows table parts to be referred to by name. When a table is referred to by the name only, Excel returns a reference to the data region of the table only. In this case, the entire table range is B4:F104 so Table1 returns the range B5:F105 to...

[![Excel formula: Last column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20column%20in%20range.png "Excel formula: Last column number in range")](https://exceljet.net/formulas/last-column-number-in-range)

### [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. If you want only the first column number, you...

[![Excel formula: Max of every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_of_every_nth_column.png "Excel formula: Max of every nth column")](https://exceljet.net/formulas/max-of-every-nth-column)

### [Max of every nth column](https://exceljet.net/formulas/max-of-every-nth-column)

In this example, the goal is to calculate the maximum value of every "nth" column in a row of data, where n is a variable entered in the named range M2 . This problem can be solved in several ways, as explained below. The explanation below also includes a formula that will work in older versions of...

[![Excel formula: XLOOKUP match any column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20match%20any%20column.png "Excel formula: XLOOKUP match any column")](https://exceljet.net/formulas/xlookup-match-any-column)

### [XLOOKUP match any column](https://exceljet.net/formulas/xlookup-match-any-column)

In this example, we have a table that contains 6 columns of codes, and each row of codes belongs to a group in column B. The goal is to lookup any code in C5:H15, and return the name of the group the code belongs to. The challenge is that the code may be in any one of the six columns, and...

[![Excel formula: Get address of named range or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_named_range_or_table.png "Excel formula: Get address of named range or table")](https://exceljet.net/formulas/get-address-of-named-range-or-table)

### [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)

The goal is to return the full address of a range or named range as text. The purpose of this formula is informational, not functional. It provides a way to inspect the current range for a named range, an Excel Table, or even the result of a formula. The core of the solutions explained below is the...

[![Excel formula: Get relative column numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20column%20numbers%20in%20range.png "Excel formula: Get relative column numbers in range")](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

### [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

The first COLUMN function generates an array of 7 numbers like this: {2,3,4,5,6,7,8} The second COLUMN function generates an array with just one item like this: {2} which is then subtracted from the first array to yield: {0,1,2,3,4,5,6} Finally, 1 is added to get: {1,2,3,4,5,6,7} With a named range...

[![Excel formula: Multiple matches into separate columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple_matches_into_separate_columns.png "Excel formula: Multiple matches into separate columns")](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

### [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)

In this example, the goal is to get all names in a given group into the same row, in separate columns, as seen in the worksheet. This is sometimes referred to as a "pivot" operation. The idea is to restructure the data into multiple columns using common values, which in this case are the group...

COLUMNS function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20Excel%20Table%20ranges%20work-Thumb.png)](https://exceljet.net/videos/how-excel-table-ranges-work)

### [How Excel Table ranges work](https://exceljet.net/videos/how-excel-table-ranges-work)

In this video, we'll take a closer look at how table ranges work. One of the most useful features of Excel Tables is that they create a dynamic range. A dynamic range automatically expands to handle new data, so it works well for reports, pivot tables, or charts that need to show the latest...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Introduction%20to%20structured%20references_thumb.png)](https://exceljet.net/videos/introduction-to-structured-references)

### [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)

In this video, I'll give a brief introduction to structured references. A structured reference is a term for using a table name in a formula instead of a normal cell reference. Structured references are optional, and can be used with formulas both inside or outside an Excel table. Let's take a look...

Related functions
-----------------

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)
    
*   [Max of every nth column](https://exceljet.net/formulas/max-of-every-nth-column)
    
*   [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)
    
*   [XLOOKUP match any column](https://exceljet.net/formulas/xlookup-match-any-column)
    
*   [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    
*   [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)
    
*   [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)
    
*   [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
    
*   [Combine ranges](https://exceljet.net/formulas/combine-ranges)
    
*   [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)
    

### Videos

*   [How Excel Table ranges work](https://exceljet.net/videos/how-excel-table-ranges-work)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    
*   [Introduction to structured references](https://exceljet.net/videos/introduction-to-structured-references)
    

### Functions

*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    

### Links

*   [Microsoft COLUMNS function documentation](https://support.office.com/en-us/article/columns-function-4e8e7b4e-e603-43e8-b177-956088fa48ca)
    

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