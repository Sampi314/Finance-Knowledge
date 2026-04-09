# Get address of named range or table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-address-of-named-range-or-table

---

[Skip to main content](https://exceljet.net/formulas/get-address-of-named-range-or-table#main-content)

[](https://exceljet.net/formulas/get-address-of-named-range-or-table#)

*   [Previous](https://exceljet.net/formulas/first-row-number-in-range)
    
*   [Next](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
    

[Range](https://exceljet.net/formulas#Range)

Get address of named range or table
===================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[ADDRESS](https://exceljet.net/functions/address-function)

[ROW](https://exceljet.net/functions/row-function)

[COLUMN](https://exceljet.net/functions/column-function)

[ROWS](https://exceljet.net/functions/rows-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

[LET](https://exceljet.net/functions/let-function)

[TAKE](https://exceljet.net/functions/take-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[TOCOL](https://exceljet.net/functions/tocol-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7740/download?token=SvjxEanE)
 (21.83 KB)

![Excel formula: Get address of named range or table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_address_of_named_range_or_table.png "Excel formula: Get address of named range or table")

Summary
-------

To get the address of a [named range](https://exceljet.net/glossary/named-range)
 or an [Excel Table](https://exceljet.net/glossary/excel-table)
 as text, you can use the [ADDRESS function](https://exceljet.net/functions/address-function)
. In the example shown, the formula in G5 is:

    =ADDRESS(@ROW(data),@COLUMN(data),4)&":"&ADDRESS(@ROW(data)+ROWS(data)-1,@COLUMN(data)+COLUMNS(data)-1,4)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:E16.

_Note: [Excel 365](https://exceljet.net/glossary/excel-365)
 requires the implicit intersection operator (@) as shown above. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, this is not necessary. See below for a more elegant solution that takes advantage of [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
_.

Generic formula
---------------

    =ADDRESS(ROW(name),COLUMN(name))&":"&ADDRESS(ROW(name)+ROWS(name)-1,COLUMN(name)+COLUMNS(name)-1)

Explanation 
------------

The goal is to return the full address of a range or [named range](https://exceljet.net/glossary/named-range)
 as text. The purpose of this formula is informational, not functional. It provides a way to inspect the current range for a named range, an Excel Table, or even the result of a formula. The core of the solutions explained below is the [ADDRESS function](https://exceljet.net/functions/address-function)
, which returns a cell address based on a given row and column. The formula gets somewhat complicated because we need to use ADDRESS twice, and because there is a lot of busy work in collecting the coordinates we need to provide to ADDRESS. See below for a more elegant formula that takes advantage of the LET function and the TAKE function in Excel 365. This version can also report the range returned by _another function_ (like OFFSET).

_Note: the [CELL function](https://exceljet.net/functions/cell-function)
 is another way to get the address for a cell. However, CELL does not provide a way to choose a relative or absolute format like the ADDRESS function does. In addition, CELL is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems in large or complex worksheets. For those reasons, I have avoided it in this example._

### Background

The links below provide more details about Excel Tables and named ranges:

*   [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)
     (video)
*   [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)
     (video)
*   [How to create a dynamic named range with a table](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)
     (video)

### Demo

The animation below shows how the formula responds when a Table named "data" is resized. In the worksheet, DA stands for Dynamic Array version of Excel and Legacy stands for older versions of Excel. See below for more information about the dynamic array version.

![The formula displays the range as it changes](https://exceljet.net/sites/default/files/images/formulas/inline/get_range_demo.gif "The formula displays the range as it changes")

### The basic idea

The basic idea of this formula is to get the coordinates of the first (upper left) cell in a range and the last (lower right) cell in a range, then use these coordinates to create cell references, then join the references together with [concatenation](https://exceljet.net/glossary/concatenation)
. The formula itself looks complicated and scary:

    =ADDRESS(@ROW(data),@COLUMN(data),4)&":"&ADDRESS(@ROW(data)+ROWS(data)-1,@COLUMN(data)+COLUMNS(data)-1,4)

However, most of what you see is the "busy work" of collecting the coordinates with the ROW, ROWS, COLUMN, and COLUMNS functions. Once that work is done, the formula simplifies to this:

    =ADDRESS(5,2,4)&":"&ADDRESS(16,4,4)

The ADDRESS function then creates a reference to the first and last cell in the range, and the two references are joined together. That's it. The rest of the problem is the details of collecting the coordinates needed by the ADDRESS function.

### ROW and COLUMN functions

The [ROW](https://exceljet.net/functions/row-function)
 and [COLUMN](https://exceljet.net/functions/column-function)
 functions simply return coordinates. For example, if we give ROW and COLUMN cell B5 as a reference, we get back coordinate numbers:

    =ROW(B5) // returns 5
    =COLUMN(B5) // returns 2

Notice that COLUMN returns a number, not a letter: column A, is 1, column B is 2, column C is 3, etc.

### ROWS and COLUMNS functions

The ROWS and COLUMNS functions return counts. For example, if we give ROWS and COLUMNS the range B5:D16, we get back the _number of rows_ and the _number of columns_ in the range:

    =ROWS(B5:D16) // returns 12
    =COLUMNS(B5:D16) // returns 3

### ADDRESS function

The [ADDRESS function](https://exceljet.net/functions/address-function)
 returns the address for a cell based on a given row and column number _as text_. For example:

    =ADDRESS(1,1) // returns "$A$1"
    =ADDRESS(5,2) // returns "$B$5"

Note that ADDRESS returns an address as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 by default. However, by providing 4 for the optional argument _abs\_num_, ADDRESS will return a [relative reference](https://exceljet.net/glossary/relative-reference)
:

    =ADDRESS(1,1,4) // returns "A1"
    =ADDRESS(5,2,4) // returns "B5"

In this problem, we need to build up an address for a range in two parts (1) a reference to the _first_ cell in the range and (2) a reference to the _last_ cell in a range. To get the address for the first cell in the range, we use this formula:

    =ADDRESS(@ROW(data),@COLUMN(data))
    

_Note: **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:E16._

As mentioned above, the [ROW function](https://exceljet.net/functions/row-function)
 and the [COLUMN function](https://exceljet.net/functions/column-function)
 return coordinates: ROW returns a row number, and COLUMN returns a column number. In this case however, we are giving ROW and COLUMN the range **data**, not a single cell. As a result, we get back an [array](https://exceljet.net/glossary/array)
 of numbers:

    =ROW(data) // returns {5;6;7;8;9;10;11;12;13;14;15;16}
    =COLUMN(data) // returns {2,3,4,5}

In other words, ROW returns _all row numbers_ for **data** (B5:D15), and COLUMN returns _all column numbers_ for **data**. This is where the formula gets a bit complicated due to Excel version differences.

Although ROW and COLUMN return multiple results, older versions of Excel will automatically limit the results to the _first_ value only. This works fine for the problem at hand, because we only want the first value. However, in the [dynamic version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, multiple results are not automatically limited, because formulas can [spill](https://exceljet.net/glossary/spill)
 results onto the worksheet. We don't want this behavior in this case, so we use the [implicit intersection](https://exceljet.net/glossary/implicit-intersection)
 operator (@) to limit the output from ROW and COLUMN to one value only:

    =@ROW(data) // returns 5
    =@COLUMN(data) // returns 2

In effect, this mimics the behavior in Legacy Excel where formulas that return more than one result display one result only. Note that the implicit intersection operator (@) is _not required_ in Legacy Excel. In fact, if you try to add the @ in an older version of Excel, Excel will simply remove it. However, it i_s required_ in the current version of Excel.

Returning to the formula, ROW and COLUMN return their results directly to ADDRESS as the _row\_num_ and _column\_num_ arguments. With _abs\_num_ provided as 4 (relative), ADDRESS returns the text "B5".

    =ADDRESS(5,2,4) // returns "B5"
    

To get the _last_ cell in the range, we use the ADDRESS function again like this:

    ADDRESS(@ROW(data)+ROWS(data)-1,@COLUMN(data)+COLUMNS(data)-1,4)
    

Essentially, we follow the same idea as above, using ROW and COLUMN to get the last row and last column of the range. However, we also calculate the total number of rows with the [ROWS function](https://exceljet.net/functions/rows-function)
 and the total number of columns with the [COLUMNS function](https://exceljet.net/functions/columns-function)
:

    =ROWS(data) // returns 12
    =COLUMNS(data) // returns 4

Then we do some simple math to calculate the row and column number of the last cell. We add the row count to the starting row, and add the column count to the starting column, then subtract 1 to get the correct coordinates for the last cell:

    =ADDRESS(@ROW(data)+ROWS(data)-1,@COLUMN(data)+COLUMNS(data)-1,4)
    =ADDRESS(5+12-1,2+4-1,4)
    =ADDRESS(16,5,4)
    ="E16"

With _abs\_num_ set to 4. ADDRESS returns "E16", the address of the last cell in **data** as text. At this point, we have the address for the first cell and the address for the last cell. The only thing left to do is [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 them together separated by a colon:

    ="B5"&":"&"E16"
    ="B5:E16"
    

### More elegant formula

Although the formula above works fine, it is cumbersome and redundant. [New array functions in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 make it possible to solve the problem with a more elegant formula like this:

    =LET(
    first,TAKE(rng,1,1),
    last,TAKE(rng,-1,-1),
    ADDRESS(ROW(first),COLUMN(first),4)&":"&
    ADDRESS(ROW(last),COLUMN(last),4)
    )
    

Where **rng** is the generic placeholder for a named range or Excel Table. In this formula, the [LET function](https://exceljet.net/functions/let-function)
 is used to assign values to two variables: _first_ and _last_. _First_ represents the first cell in the range and _last_ represents the last cell in the range. These values are assigned with the TAKE function like this:

    first,TAKE(rng,1,1), // first cell (B5)
    last,TAKE(rng,-1,-1), // last cell (E16)

The [TAKE function](https://exceljet.net/functions/take-function)
 returns a _subset_ of a given array or range. The size of the array returned is determined by separate _rows_ and _columns_ arguments. When positive numbers are provided for rows or columns, TAKE returns values from the start or top of the array. Negative numbers take values from the end or bottom of the array. What's tricky about this, and not obvious, is that when working with ranges, TAKE returns a _valid reference_. You don't normally see the reference because as with most formulas, Excel returns the _value_ at that reference, _not_ the reference itself. However, the reference is there, as is obvious in the next step.

Finally, the [ADDRESS function](https://exceljet.net/functions/address-function)
 is used to generate an address for both the first cell and the last cell in the range, and the two results are [concatenated](https://exceljet.net/glossary/concatenation)
 with a colon (:) in between:

    ADDRESS(ROW(first),COLUMN(first),4)&":"&ADDRESS(ROW(last),COLUMN(last),4)
    

Substituting the references returned by TAKE, the formula evaluates like this:

    =ADDRESS(ROW(B5),COLUMN(B5),4)&":"&ADDRESS(ROW(E16),COLUMN(E16),4)
    =ADDRESS(5,2,4)&":"&ADDRESS(16,4,4)
    ="B5"&":"&"E16"
    ="B5:E16"

### Named range as text

To get an address for a named range entered as a _text value_ (i.e. "range", "data", etc.), you'll need to use the INDIRECT function to change the text into a valid reference before proceeding. For example, to get the address of a table name entered in A1 as text, you could use this unwieldy formula:

    =ADDRESS(ROW(INDIRECT(A1)),COLUMN(INDIRECT(A1)))&":"&ADDRESS(ROW(INDIRECT(A1))+ROWS(INDIRECT(A1))-1,COLUMN(INDIRECT(A1))+COLUMNS(INDIRECT(A1))-1)
    

In the dynamic array version of Excel, the [LET function](https://exceljet.net/functions/let-function)
 makes this much simpler. With a range or table name as text in cell A1, you can call INDIRECT just once like this:

    =LET(
    rng,INDIRECT(A1),
    first,TAKE(rng,1,1),
    last,TAKE(rng,-1,-1),
    ADDRESS(ROW(first),COLUMN(first),4)&":"&
    ADDRESS(ROW(last),COLUMN(last),4)
    )

You can read more about the LET function [here](https://exceljet.net/functions/let-function)
.

### Named LAMBDA option

Taking things a step further, you can use the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to create a custom function like this:

    =LAMBDA(range,
      LET(
        rng,IF(ISREF(range),range,INDIRECT(range)),
        first,TAKE(rng,1,1),
        last,TAKE(rng,-1,-1),
        ADDRESS(ROW(first),COLUMN(first),4)&":"&
        ADDRESS(ROW(last),COLUMN(last),4)
      )
    )(data)

This version of the formula does the same thing as the formula above with one additional step: it checks for range or table names entered as text values. This is done with the [ISREF function](https://exceljet.net/functions/isref-function)
 in the first step. If the value passed in for _range_ is a valid reference, we use it as-is to assign a value to _rng_. If not, we run it through the [INDIRECT function](https://exceljet.net/functions/indirect-function)
 to try and get a valid reference.

Finally, if we give the LAMBDA formula above the name "GetRange", we can call it on any valid range like this:

    =GetRange(data)

Read more about creating and naming custom LAMBDA formulas [here](https://exceljet.net/functions/lambda-function)
.

### Check reference returned by formula

A nice feature of the LAMBDA version of the formula is we easily can use it to check the result of any formula that returns a range. For example, we can call it with the OFFSET function like this:

    =GetRange(OFFSET(A1,4,1,10,2)) // returns "B5:C14"

The point here is that it is not easy to understand what range is returned by OFFSET, because Excel will return only the _values in the range_. The custom GetRange function makes it possible to print the range returned by a formula explicitly.

### Other ideas

I looked at two other formulas to solve this problem. The first uses ADDRESS and TAKE:

    =LET(
    a,ADDRESS(ROW(data),COLUMN(data),4),
    TAKE(a,1,1)&":"&TAKE(a,-1,-1)
    )

The second uses ADDRESS and the new [TOCOL function](https://exceljet.net/functions/tocol-function)
:

    =LET(
    a,TOCOL(ADDRESS(ROW(data),COLUMN(data),4)),
    INDEX(a,1)&":"&INDEX(a,ROWS(d))
    )

Both formulas use the ADDRESS function to spin up all of the addresses in the range at the same time. The first formula then uses the TAKE function to get the first and last address. The second formula uses the TOCOL function to unwrap the array of references created by ADDRESS, then it uses the INDEX function twice to get the first and the last value. On small ranges, these formulas should work nicely. However, on very large ranges you are likely to see a performance hit because of the time needed to create all of the extra addresses. The proposed formula solution above avoids this problem by only creating the first and last reference. The tradeoff is that the formula is more complex.

Related formulas
----------------

[![Excel formula: Address of first cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20first%20cell%20in%20range.png "Excel formula: Address of first cell in range")](https://exceljet.net/formulas/address-of-first-cell-in-range)

### [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)

The ADDRESS function creates a reference based on a given row and column number. In this case, we want to get the first row and the first column used by the named range data (B5:D14). To get the first row used, we use the ROW function together with the MIN function like this: MIN(ROW(data)) Because...

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

[![Excel formula: Total rows in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20rows%20in%20range.png "Excel formula: Total rows in range")](https://exceljet.net/formulas/total-rows-in-range)

### [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)

The ROWS function is fully automatic. When you provide a range to ROWS, it will return a count of all rows in the range. In the example, the formula in F5 returns 6, because there are 6 rows in the range B5:C10: =ROWS(B5:C10) // count rows ROWS counts the number of rows in any supplied range and...

[![Excel formula: Total columns in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20columns%20in%20range.png "Excel formula: Total columns in range")](https://exceljet.net/formulas/total-columns-in-range)

### [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)

The COLUMNS function is fully automatic. When you provide a range to COLUMNS, it will return a count of all columns in the range. In the example, the formula in F6 returns 2, because there are 2 columns in the range B5:C10: =COLUMNS(B5:C10) // count columns COLUMNS counts the number of columns in...

[![Excel formula: Count cells in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_cells_in_range.png "Excel formula: Count cells in range")](https://exceljet.net/formulas/count-cells-in-range)

### [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)

The goal is to count the number of cells in a given range, regardless of whether the cells are empty or not. Although Excel has several functions designed to count cells based on their contents, there is no built-in function for counting the total number of cells in a range. The classic solution is...

Related functions
-----------------

[![Excel ADDRESS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20address%20function.png "Excel ADDRESS function")](https://exceljet.net/functions/address-function)

### [ADDRESS Function](https://exceljet.net/functions/address-function)

The Excel ADDRESS function returns the address for a cell based on a given row and column number. For example, =ADDRESS(1,1) returns $A$1. ADDRESS can return an address in relative, mixed, or absolute format, and can be used to construct a cell reference inside a formula.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel TOCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20tocol%20function.png "Excel TOCOL function")](https://exceljet.net/functions/tocol-function)

### [TOCOL Function](https://exceljet.net/functions/tocol-function)

The Excel TOCOL function transforms an array into a single column. By default, TOCOL will scan values by row, but TOCOL can also scan values by column.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20named%20range-thumb.png)](https://exceljet.net/videos/how-to-create-a-named-range)

### [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)

Named ranges are one of the most useful features in Excel. They make your formulas much easier to read and understand; they automatically give you absolute references , and they reduce errors. Let's take a look at a few ways to create named ranges. The simplest way to create a named range is to use...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-create-an-excel-table)

### [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

In this video, we'll look at how to create an Excel table. Here we have some data that is a good candidate for a table. Each row represents an entry or record with information that belongs together. Each column has a unique name. The first step in creating a table is to remove any blank rows or...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)
    
*   [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)
    
*   [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)
    
*   [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)
    
*   [Count cells in range](https://exceljet.net/formulas/count-cells-in-range)
    

### Functions

*   [ADDRESS Function](https://exceljet.net/functions/address-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [TOCOL Function](https://exceljet.net/functions/tocol-function)
    

### Videos

*   [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)
    
*   [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)
    

### Articles

*   [Named Ranges in Excel](https://exceljet.net/articles/named-ranges)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
*   [Excel Tables](https://exceljet.net/training/excel-tables)
    

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