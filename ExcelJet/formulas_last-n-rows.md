# Last n rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-n-rows

---

[Skip to main content](https://exceljet.net/formulas/last-n-rows#main-content)

[](https://exceljet.net/formulas/last-n-rows#)

*   [Previous](https://exceljet.net/formulas/last-column-number-in-range)
    
*   [Next](https://exceljet.net/formulas/last-row-in-mixed-data-with-blanks)
    

[Range](https://exceljet.net/formulas#Range)

Last n rows
===========

by Dave Bruns · Updated 13 Nov 2025

Related functions 
------------------

[TAKE](https://exceljet.net/functions/take-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[ROW](https://exceljet.net/functions/row-function)

[ROWS](https://exceljet.net/functions/rows-function)

[INDEX](https://exceljet.net/functions/index-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9420/download?token=CdpsUVXk)
 (43.9 KB)

![Excel formula: Last n rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/last-n-rows.png "Excel formula: Last n rows")

Summary
-------

To get the last n rows from a range or table, you can use a formula based on the [TAKE function](https://exceljet.net/functions/take-function)
. In the example shown, the formula in cell G5 is:

    =TAKE(Table1,-H2)
    

Where the value in cell H2 is the number of rows to retrieve from the bottom of an [Excel Table](https://exceljet.net/articles/excel-tables)
 named Table1. This formula is dynamic and will update automatically as the number of rows in the table changes, or when the number of rows to retrieve in H2 is changed.

Generic formula
---------------

    =TAKE(range,-n)

Explanation 
------------

When you are working with a large table that extends beyond the visible area of a worksheet, you might want to see the most recent data in the table without scrolling to the bottom of the table. Examples of this kind of data include things like:

*   Recent deposits or expenses
*   Recent transactions
*   Recent stock prices
*   Recent orders
*   Recent invoices

In this example, the goal is to dynamically retrieve the last n rows of a table or range, so that you can quickly check the entries at the bottom, where n is a value that can be easily changed. The main challenge of this problem is that you don't know where the table ends, so the formula needs to work this out. This is a great use case for the TAKE function.

### Table of Contents

*   [Note on Excel Tables](https://exceljet.net/formulas/last-n-rows#note-on-excel-tables)
    
*   [The TAKE function](https://exceljet.net/formulas/last-n-rows#the-take-function)
    
*   [TAKE to get the last n rows](https://exceljet.net/formulas/last-n-rows#take-to-get-the-last-n-rows)
    
*   [Calculating a total amount](https://exceljet.net/formulas/last-n-rows#calculating-a-total-amount)
    
*   [Sorting the last n rows in reverse order](https://exceljet.net/formulas/last-n-rows#sorting-the-last-n-rows-in-reverse-order)
    
*   [Sorting the last n rows in reverse order with a checkbox](https://exceljet.net/formulas/last-n-rows#sorting-the-last-n-rows-in-reverse-order-with-a-checkbox)
    
*   [Legacy Excel Formulas](https://exceljet.net/formulas/last-n-rows#legacy-excel-formulas)
    
*   [Multi-cell array formula to get the last n rows](https://exceljet.net/formulas/last-n-rows#multi-cell-array-formula-to-get-the-last-n-rows)
    
*   [Flagging last n rows in a range](https://exceljet.net/formulas/last-n-rows#flagging-last-n-rows-in-a-range)
    
*   [Flagging last n rows in a table](https://exceljet.net/formulas/last-n-rows#flagging-last-n-rows-in-a-table)
    

### Note on Excel Tables

This example uses [Excel Tables](https://exceljet.net/articles/excel-tables)
 to store the data we are working with, because Excel Tables automatically expand to fit the data as it grows. In other words, they are an easy way to create a dynamic range in Excel. One consequence of using tables is that each table needs a unique name. As a result, the examples below are named Table1, Table2, Table3, and Table4 on each of the four sheets. The data in each table is the same; only the names are different.

> If you don't want to use an Excel Table, you could use the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
>  or the new [dot operator](https://exceljet.net/glossary/dot-operator)
>  to create your own dynamic range.

### The TAKE function

The Excel [TAKE function](https://exceljet.net/functions/take-function)
 returns a subset of a given array. The number of rows and columns to return is provided by separate rows and columns arguments.

    =TAKE(array,rows,columns)
    

Where rows is the number of rows to return and columns is the number of columns to return. When positive numbers are provided for rows and columns, TAKE returns values from the _start of the array_, starting at the upper left cell. For example, to get the first cell in a range, you can use:

    =TAKE(range,1,1) // returns the first cell in the range
    

When negative numbers are provided for rows and columns, TAKE returns values from the _end of the array_, starting at the lower right cell. For example, to get the last cell in a range, you can use:

    =TAKE(range,-1,-1) // returns the last cell in the range.
    

You can use the same approach to retrieve whole rows:

    =TAKE(range,1) // returns the first row in the range
    =TAKE(range,-1) // returns the last row in the range
    

### TAKE to get the last n rows

Moving back to the worksheet shown, we can easily use TAKE to get the last 5 rows in the table shown with a formula like this in cell G5:

    =TAKE(Table1,-5)
    

To make the formula more dynamic, so that it will automatically respond to a number of rows typed in cell H2, we simply need to replace the hard-coded 5 with a reference to cell H2:

    =TAKE(Table1,-H2)
    

You can see how this works in the worksheet below. In the first screen, we have 5 in H2, so the formula returns the last 5 rows in the table. 

![Using TAKE to get the last 5 rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/last-n-rows-get-last-5-rows.png "Using TAKE to get the last 5 rows")

In the next screen, we have entered 10 in H2, so the formula returns the last 10 rows in the table:

![Using TAKE to get the last 10 rows](https://exceljet.net/sites/default/files/images/formulas/inline/last-n-rows-get-last-10-rows.png "Using TAKE to get the last 10 rows")

Notice we need to negate the value in H2 (-H2) in order to pull rows from the end of the table.

### Calculating a total amount

To calculate a total amount from the last n rows, we can use a formula like this in cell J2:

    =SUM(TAKE(Table1,-H2,-1))
    

This formula uses the TAKE function to get the last 5 rows of the last column in the table (Amount), then feeds those values into the [SUM function](https://exceljet.net/functions/sum-function)
, which returns a total:

![Calculating a total amount](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/last-n-rows-calculate-total-amount.png "Calculating a total amount")

Another option is to reference the Amount column directly using a structured reference like this:

    =SUM(TAKE(Table1[Amount],-H2))
    

Both formulas will return a dynamic total for the last n rows in the table, based on the value in cell H2.

### Sorting the last n rows in reverse order

If you want to sort the last n rows in "reverse order" so that the last row is displayed _first_, you can use a formula like this:

    =SORTBY(TAKE(Table2,-H2),SEQUENCE(H2),-1)
    

This formula will return the last n rows in the table sorted in reverse order by position, so that the last row is displayed first. You can see how this works in the worksheet below:

![Sorting the last n rows in reverse order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/last-n-rows-sort-last-n-rows-in-reverse-order.png "Sorting the last n rows in reverse order")

The SEQUENCE function is used to create a sequence of numbers from 1 to n, which is then used to sort the rows in reverse order. For details on how this formula works, see [Reversing a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)
.

### Sorting the last n rows in reverse order with a checkbox

One interesting option we can add to the formula above is the ability to sort the last n rows in reverse order _conditionally,_ using a [checkbox](https://exceljet.net/articles/native-checkboxes-in-excel)
 to control the sort order. In the worksheet below, we have made the reverse sort optional by inserting a checkbox to cell J2 and using a formula like this in cell G5:

    =LET(rows,TAKE(Table3,-H2),IF(J2,SORTBY(rows,SEQUENCE(H2),-1),rows))
    

![Sorting the last n rows in reverse order with a checkbox](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/last-n-rows-sort-last-n-rows-in-reverse-order-with-checkbox.png "Sorting the last n rows in reverse order with a checkbox")

This formula uses the [LET function](https://exceljet.net/functions/let-function)
 to create a variable called `rows`, which becomes the n rows of the table using the original formula above. Next, the [IF function](https://exceljet.net/functions/if-function)
 is used to conditionally sort the rows in reverse order based on the state of the checkbox in cell J2. If the checkbox in cell J2 is checked (TRUE), we sort the rows in reverse order using the [SORTBY function](https://exceljet.net/functions/sortby-function)
:

    =SORTBY(rows,SEQUENCE(H2),-1)
    

If the checkbox in cell J2 is unchecked (FALSE), the IF function returns `rows` as is. The result is a dynamic list of the last n rows in the table, sorted in reverse order when the checkbox is checked, and in the original order when the checkbox is unchecked.

> Note: You could use a simpler formula based on the [SORT function](https://exceljet.net/functions/sort-function)
>  to sort in reverse order by any column in the table that will work for a "reverse" sort. The advantage of using SORTBY + SEQUENCE is that it will work even for tables that do not contain a numeric column to sort by.

Legacy Excel Formulas
---------------------

This section contains some formulas that are useful in older versions of Excel that do not have new functions like TAKE and SEQUENCE, and do not support [dynamic arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. These formulas are not as efficient as the ones using the new functions, but they are still useful in some cases.

### Multi-cell array formula to get the last n rows

One way to get the last n rows in an older version of Excel is to use a multi-cell array formula. Multi-cell array formulas are the precursor to dynamic arrays in Excel, and they work in a similar way. The trick with a multi-cell array formula is to select the entire range that represents the maximum size the formula needs to cover and then enter the same formula using Ctrl+Shift+Enter in the entire range. For example, with the worksheet we've been working with above, first select the range G5:J29 (25 rows) and enter the following formula in cell G5, then press Ctrl+Shift+Enter to enter the formula as an array formula:

    {=IF(ROW()-ROW(G5)+1<=H2,INDEX(Table4,ROWS(Table4)-(H2-1),0):INDEX(Table4,ROWS(Table4),0),"")}
    

> Note: There is no need to copy this formula down and across because it is entered in all cells at the same time. You will see the curly braces around the entire formula in the formula bar when the formula is entered with Ctrl+Shift+Enter. These braces are not part of the formula itself. They are simply an indication that the formula was entered as an array formula. They will disappear when you edit the formula.

![Multi-cell array formula to get the last n rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/last-n-rows-multi-cell-array-formula.png "Multi-cell array formula to get the last n rows")

At a high level, the formula uses the IF function to check if the "current row" is one of the last n rows in the table, using the value for n in cell H2. If it is, the formula retrieves the rows from the table using the INDEX function. If the current row is greater than n, the formula returns an empty string. The row check snippet looks like this:

    =ROW()-ROW(G5)+1<=H2
    

The ROW function is used to get the row number of the current cell, and the row number of the first cell in the table (G5). The difference between the two plus 1 gives us the current row number in the output range. If this value is less than or equal to the number of rows to retrieve, the formula returns the last n rows in the table using the INDEX function:

    =INDEX(Table4,ROWS(Table4)-(H2-1),0):INDEX(Table4,ROWS(Table4),0)
    

Notice the colon (:) between the two INDEX functions. This is a special operator that returns a range of cells. Essentially, we are building a range from the references created by the two INDEX functions. The INDEX on the right is a reference to the last row in the table, and the INDEX on the left is a reference to the first row in the table that we want to include in the output. When we join the two references with the colon, we get a range that contains the last n rows in the table.

> Note: You could also use the [OFFSET function](https://exceljet.net/functions/offset-function)
>  to solve this problem. However, OFFSET is a [volatile function](https://exceljet.net/glossary/volatile-function)
>  and will recalculate every time the worksheet is recalculated, so I avoid using it when possible.

### Flagging last n rows in a range

Sometimes you may want to flag the last n rows in a table or range, so that you can easily identify them. One way to do this is to use a helper column with a formula that returns TRUE if a row is a "last n row", and FALSE if not. For example, in the worksheet shown below, the formula in cell E5, copied down, is:

    =ROW()-ROW(INDEX(data,1,1))+1>ROWS(data)-n
    

Where **data** (B5:E15) and **n** (G5) are [named ranges](https://exceljet.net/glossary/named-range)
. This formula returns TRUE if a row is a "last n row", and FALSE if not.

![Flagging last n rows with a helper column](https://exceljet.net/sites/default/files/images/formulas/inline/last-n-rows-helper-column-flag-formula.png "Flagging last n rows with a helper column")

In brief, we get the current row in the workbook, then subtract the first row number of the range plus 1. The result is an adjusted row number that begins at 1. The [INDEX function](https://exceljet.net/functions/index-function)
 is simply a way to get the first cell in a given range:

    ROW(INDEX(data,1,1) // first cell
    

This is for convenience only. The formula could be rewritten as:

    =ROW()-ROW($E$5)+1
    

Once we have a current row number, we can compare the row number to the total rows in the data less n:

    current_row > ROWS(data)-n
    

This expression returns TRUE if the current row is one of the last n rows we are looking for. Otherwise, it returns FALSE.

### Flagging last n rows in a table

If data is in an Excel table, the formula above can be adapted like this:

    =ROW()-@ROW(Table1)+1>ROWS(Table1)-n
    

![Flagging last n rows with a helper column in an Excel Table](https://exceljet.net/sites/default/files/images/formulas/inline/last-n-rows-helper-column-flag-formula-table.png "Flagging last n rows with a helper column in an Excel Table")

The logic is exactly the same as the previous formula, but we use a slightly different approach to get the first cell in the table:

    @ROW(Table1)
    

The @ operator means [implicit intersection](https://exceljet.net/glossary/implicit-intersection)
. You can think of it as indicating "single":

    =ROW(Table1) // returns {5;6;7;8;9;10;11;12;13;14;15}
    =@ROW(Table1) // returns {5}
    

As before, the table formula returns TRUE in "last n rows" and FALSE in others.

Related formulas
----------------

[![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")](https://exceljet.net/formulas/automatic-row-numbers)

### [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: First row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20row%20in%20range.png "Excel formula: First row number in range")](https://exceljet.net/formulas/first-row-number-in-range)

### [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range that contains multiple rows, the ROW function will return an array that contains all row numbers for the range. In the example shown the array looks like this: {5;6;7;8;9;10}...

[![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")](https://exceljet.net/formulas/last-row-number-in-range)

### [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range: {5;6;7;8;9;10} To get the first row number in a range, we use the MIN...

[![Excel formula: First column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20column%20in%20range.png "Excel formula: First column number in range")](https://exceljet.net/formulas/first-column-number-in-range)

### [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. In the example shown the array looks like this...

[![Excel formula: Basic outline numbering](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20outline%20numbering.png "Excel formula: Basic outline numbering")](https://exceljet.net/formulas/basic-outline-numbering)

### [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)

At the core, this formula builds a level 1 and level 2 number and concatenates the two numbers together with a period (".") as a separator. The result is a value like "1.1". The "level 1" number is generated with COUNTA like this: =COUNTA($B$5:B5) Note the range is an expanding reference , so it...

[![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")](https://exceljet.net/formulas/reverse-a-list-or-range)

### [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the SORT function...

Related functions
-----------------

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

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

*   [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)
    
*   [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)
    
*   [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)
    
*   [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)
    
*   [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)
    

### Functions

*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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