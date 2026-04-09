# Excel COLUMN function | Exceljet

**Source:** https://exceljet.net/functions/column-function

---

[Skip to main content](https://exceljet.net/functions/column-function#main-content)

[](https://exceljet.net/functions/column-function#)

*   [Previous](https://exceljet.net/functions/choose-function)
    
*   [Next](https://exceljet.net/functions/columns-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

COLUMN Function
===============

by Dave Bruns · Updated 6 Jun 2021

Related functions 
------------------

[ROW](https://exceljet.net/functions/row-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

[ROWS](https://exceljet.net/functions/rows-function)

![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")

Summary
-------

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

Purpose 
--------

Get the column number of a reference.

Return value 
-------------

A number representing the column.

Syntax
------

    =COLUMN([reference])

*   _reference_ - \[optional\] A reference to a cell or range of cells.

Using the COLUMN function 
--------------------------

The COLUMN function returns the column number of a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. COLUMN takes just one argument, called _reference_, which can be empty, a cell reference, or a range. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

### Examples

With a single cell reference, COLUMN returns the associated column number:

    =COLUMN(A1) // returns 1
    =COLUMN(C1) // returns 3
    

When a reference is not provided, COLUMN returns the column number of the cell the formula resides in. For example, if the following formula is entered in cell D6, the result is 4:

    =COLUMN() // returns 4 in D6
    

When COLUMN is given a range, it returns the column numbers for that range:

    =COLUMN(E4:G6) // returns {5,6,7}
    

In [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the result is an [array](https://exceljet.net/glossary/array)
 {5,6,7} that [spills](https://exceljet.net/glossary/spill)
 horizontally into three cells, starting with the cell the formula resides in. In earlier Excel versions, the first item of the array (5) will display in one cell only.

To get Excel 365 to return a single value, you can use the [implicit intersection](https://exceljet.net/glossary/implicit-intersection)
 operator (@):

    =@COLUMN(E4:G6) // returns 5
    

 This @ symbol disables array behavior and tells Excel you want a single value.

### Notes

*   _Reference_ can be a single cell address or a range of cells.
*   _Reference_ is optional and will default to the cell in which the COLUMN function exists.
*   _Reference_ cannot include multiple references or addresses.
*   To get _row_ numbers, see the [ROW function](https://exceljet.net/functions/row-function)
    .
*   To _count_ columns, see the [COLUMNS function](https://exceljet.net/functions/columns-function)
    .
*   To _lookup_ a column number, see the [MATCH function](https://exceljet.net/functions/match-function)
    .

COLUMN function examples
------------------------

[![Excel formula: Fixed value every N columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/fixed%20value%20every%20N%20months.png "Excel formula: Fixed value every N columns")](https://exceljet.net/formulas/fixed-value-every-n-columns)

### [Fixed value every N columns](https://exceljet.net/formulas/fixed-value-every-n-columns)

The core of this formula is the MOD function. MOD takes a number and divisor, and returns the remainder after division, which makes it useful for formulas that need to do something every nth time. In this case, the number is created with the COLUMN function, which return the column number of cell...

[![Excel formula: Sum every 3 cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%203%20cells.png "Excel formula: Sum every 3 cells")](https://exceljet.net/formulas/sum-every-3-cells)

### [Sum every 3 cells](https://exceljet.net/formulas/sum-every-3-cells)

At the core, the OFFSET function delivers a range of 3 cells to SUM, which returns a summed result. The arguments for OFFSET are provided as follows: For reference we use the first cell in the data range, B5, entered as a mixed reference (column locked, row relative). For rows , we use 0, since we...

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

[![Excel formula: Index and match on multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/index%20and%20match%20on%20multiple%20columns.png "Excel formula: Index and match on multiple columns")](https://exceljet.net/formulas/index-and-match-on-multiple-columns)

### [Index and match on multiple columns](https://exceljet.net/formulas/index-and-match-on-multiple-columns)

Working from the inside out, the logical criteria used in this formula is this expression: --(names=G4) where names is the named range C4:E7. This generates a TRUE / FALSE result for every value in the data, and the double negative coerces the TRUE and FALSE values to 1 and 0 to yield an array like...

[![Excel formula: Last column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20column%20in%20range.png "Excel formula: Last column number in range")](https://exceljet.net/formulas/last-column-number-in-range)

### [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. If you want only the first column number, you...

[![Excel formula: Increment a calculation with ROW or COLUMN](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/increment%20a%20calculation.png "Excel formula: Increment a calculation with ROW or COLUMN")](https://exceljet.net/formulas/increment-a-calculation-with-row-or-column)

### [Increment a calculation with ROW or COLUMN](https://exceljet.net/formulas/increment-a-calculation-with-row-or-column)

The ROW function, when entered into a cell with no arguments returns the row number of that cell. In this case, the first instance of the formula is in cell D6 so, ROW() returns 6 inside the formula in D6. We want to start with 1, however, so we need to subtract 5, which yields 1. As the formula is...

[![Excel formula: Max of every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_of_every_nth_column.png "Excel formula: Max of every nth column")](https://exceljet.net/formulas/max-of-every-nth-column)

### [Max of every nth column](https://exceljet.net/formulas/max-of-every-nth-column)

In this example, the goal is to calculate the maximum value of every "nth" column in a row of data, where n is a variable entered in the named range M2 . This problem can be solved in several ways, as explained below. The explanation below also includes a formula that will work in older versions of...

[![Excel formula: Get location of value in 2D array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_location_of_value_in_2D_array.png "Excel formula: Get location of value in 2D array")](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

### [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

In this example, the goal is to return a list of the locations for a specific value in a 2D array of values (i.e., a table). The target value is entered in cell N5, and the table being tested is in the range C4:L16. The coordinates are supplied from row 4 and column B, as seen in the worksheet. In...

[![Excel formula: Address of first cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20first%20cell%20in%20range.png "Excel formula: Address of first cell in range")](https://exceljet.net/formulas/address-of-first-cell-in-range)

### [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)

The ADDRESS function creates a reference based on a given row and column number. In this case, we want to get the first row and the first column used by the named range data (B5:D14). To get the first row used, we use the ROW function together with the MIN function like this: MIN(ROW(data)) Because...

[![Excel formula: Count rows with at least n matching values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20at%20least%20n%20matching%20values3.png "Excel formula: Count rows with at least n matching values")](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)

### [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)

Working from the inside out, the logical criteria used in this formula is: (data)<70 where data is the named range C5:I14. This generates a TRUE / FALSE result for every value in data , and the double negative coerces the TRUE FALSE values to 1 and 0 to yield an array like this: {0,0,0,1,0,1,0;0...

[![Excel formula: Count with repeating values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20with%20repeating%20values.png "Excel formula: Count with repeating values")](https://exceljet.net/formulas/count-with-repeating-values)

### [Count with repeating values](https://exceljet.net/formulas/count-with-repeating-values)

The core of this formula is the ROUNDUP function. The ROUNDUP function works like the ROUND function except that when rounding, the ROUNDUP function will always round the numbers 1-9 up. In this formula, we use that fact to repeat values. To supply a number to ROUNDUP, we are using this expression...

[![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")](https://exceljet.net/formulas/copy-value-from-every-nth-column)

### [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct...

COLUMN function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

Related functions
-----------------

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Increment a calculation with ROW or COLUMN](https://exceljet.net/formulas/increment-a-calculation-with-row-or-column)
    
*   [Max of every nth column](https://exceljet.net/formulas/max-of-every-nth-column)
    
*   [Count with repeating values](https://exceljet.net/formulas/count-with-repeating-values)
    
*   [Fixed value every N columns](https://exceljet.net/formulas/fixed-value-every-n-columns)
    
*   [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    
*   [Convert column letter to number](https://exceljet.net/formulas/convert-column-letter-to-number)
    
*   [Sum every 3 cells](https://exceljet.net/formulas/sum-every-3-cells)
    
*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    
*   [Address of first cell in range](https://exceljet.net/formulas/address-of-first-cell-in-range)
    
*   [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    

### Videos

*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    

### Functions

*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

### Links

*   [Microsoft COLUMN function documentation](https://support.office.com/en-us/article/column-function-44e8c754-711c-4df3-9da4-47a55042554b)
    

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