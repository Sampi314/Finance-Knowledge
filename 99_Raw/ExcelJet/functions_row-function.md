# Excel ROW function | Exceljet

**Source:** https://exceljet.net/functions/row-function

---

[Skip to main content](https://exceljet.net/functions/row-function#main-content)

[](https://exceljet.net/functions/row-function#)

*   [Previous](https://exceljet.net/functions/offset-function)
    
*   [Next](https://exceljet.net/functions/rows-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

ROW Function
============

by Dave Bruns · Updated 16 Jun 2021

Related functions 
------------------

[ROWS](https://exceljet.net/functions/rows-function)

[COLUMN](https://exceljet.net/functions/column-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

![Excel ROW function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")

Summary
-------

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Purpose 
--------

Get the row number of a reference

Return value 
-------------

A number representing the row.

Syntax
------

    =ROW([reference])

*   _reference_ - \[optional\] A reference to a cell or range of cells.

Using the ROW function 
-----------------------

The ROW function returns the row number for a cell or range. For example, =ROW(C3) returns 3, since C3 is the third row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula. ROW takes just one argument, called _reference_, which can be empty, a cell reference, or a range. When no reference is provided, ROW returns the row number of the cell which contains the formula.

### Examples

With a single cell reference, ROW returns the associated row number:

    =ROW(A1) // returns 1
    =ROW(E3) // returns 3
    

When a reference is not provided, ROW returns the row number of the cell the formula resides in. For example, if the following formula is entered in cell D6, the result is 6:

    =ROW() // returns 6 in D6
    

When ROW is given a range, it returns the row numbers for that range:

    =ROW(E4:G6) // returns {4,5,6}
    

In [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the result is an [array](https://exceljet.net/glossary/array)
 {4,5,6} that [spills](https://exceljet.net/glossary/spill)
 vertically into three cells, starting with the cell that contains the formula. In earlier Excel versions, the first item of the array (4) will display in one cell only.

To get Excel 365 to return a single value, you can use the [implicit intersection](https://exceljet.net/glossary/implicit-intersection)
 operator (@):

    =@ROW(E4:G6) // returns 4
    

 This @ symbol disables array behavior and tells Excel you want a single value.

### Notes

*   _Reference_ can be a single cell address or a range of cells.
*   _Reference_ is optional and will default to the cell in which the ROW function exists.
*   _Reference_ cannot include multiple references or addresses.
*   To get _column_ numbers, see the [COLUMN function](https://exceljet.net/functions/column-function)
    .
*   To _count_ rows, see the [ROWS function](https://exceljet.net/functions/rows-function)
    .
*   To _lookup_ a row number, see the [MATCH function](https://exceljet.net/functions/match-function)
    .

ROW function examples
---------------------

[![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")](https://exceljet.net/formulas/last-row-number-in-range)

### [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range: {5;6;7;8;9;10} To get the first row number in a range, we use the MIN...

[![Excel formula: Get nth match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match.png "Excel formula: Get nth match")](https://exceljet.net/formulas/get-nth-match)

### [Get nth match](https://exceljet.net/formulas/get-nth-match)

The goal is to retrieve the nth matching record in a set of data, after filtering on a specific product. In the worksheet shown, the product in H4 and the value for n in H5 are inputs that can be changed at any time. For instance, if the product in H4 is "A" and the value in H5 is 3, the formula...

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

[![Excel formula: Last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last-n-rows.png "Excel formula: Last n rows")](https://exceljet.net/formulas/last-n-rows)

### [Last n rows](https://exceljet.net/formulas/last-n-rows)

When you are working with a large table that extends beyond the visible area of a worksheet, you might want to see the most recent data in the table without scrolling to the bottom of the table. Examples of this kind of data include things like: Recent deposits or expenses Recent transactions...

[![Excel formula: Copy value from every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20row_0.png "Excel formula: Copy value from every nth row")](https://exceljet.net/formulas/copy-value-from-every-nth-row)

### [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)

In this example, the goal is to copy every nth value from column B, where n is a variable that can be changed as needed. In Excel, it's difficult to create formulas that skip rows following a certain pattern, because the references in the formula will automatically change as the formula is copied...

[![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

### [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

Excel doesn't have a way to cast the letters in a text string to an array directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is: =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(...

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

[![Excel formula: First row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20row%20in%20range.png "Excel formula: First row number in range")](https://exceljet.net/formulas/first-row-number-in-range)

### [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range that contains multiple rows, the ROW function will return an array that contains all row numbers for the range. In the example shown the array looks like this: {5;6;7;8;9;10}...

[![Excel formula: Count unique text values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20text%20values%20in%20a%20range.png "Excel formula: Count unique text values in a range")](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

### [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

This formula is more complicated than a similar formula that uses FREQUENCY to count unique numeric values because FREQUENCY doesn't normally work with non-numeric values. As a result, a large part of the formula simply transforms the non-numeric data into numeric data that FREQUENCY can handle...

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

[![Excel formula: Translate letters to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/translate%20letters%20to%20numbers.png "Excel formula: Translate letters to numbers")](https://exceljet.net/formulas/translate-letters-to-numbers)

### [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)

At the core, this formula uses an array operation to generate an array of letters from the input text, translates each letter individually to a number, then joins all numbers together again and returns the output as a string. To parse the input string into an array or letters, we use MID, ROW, LEN...

[![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")](https://exceljet.net/formulas/automatic-row-numbers)

### [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a...

[![Excel formula: Sum bottom n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values.png "Excel formula: Sum bottom n values")](https://exceljet.net/formulas/sum-bottom-n-values)

### [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)

In this example, the goal is to sum the smallest n values in a set of data, where n is a variable that can be easily changed. At a high level, the solution breaks down into two steps (1) extract the n smallest values from the data set and (2) sum the extracted values. This problem can be solved...

[![Excel formula: Get column totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20column%20totals.png "Excel formula: Get column totals")](https://exceljet.net/formulas/get-column-totals)

### [Get column totals](https://exceljet.net/formulas/get-column-totals)

In this example, the goal is to return an array with 7 subtotals, one for each day of the week, as seen in columns C:I. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We...

ROW function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Shade%20groups%20of%20rows%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)

### [Shade groups of rows with conditional formatting](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade alternating groups of rows. For example, you can use this approach to shade groups of 3 rows, groups of 4 rows, and so on. This can be a nice way to make certain tables easier to read. Here we have a table with 3 rows of data...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20function%20arguments-thumb.png)](https://exceljet.net/videos/how-to-use-function-arguments)

### [How to use function arguments](https://exceljet.net/videos/how-to-use-function-arguments)

You've probably noticed that functions use parentheses, and inside those parentheses are certain inputs. These inputs have a special name: arguments. Let's look at some examples. Arguments can be required or optional. Some functions take three or more arguments, and some functions don't take any...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20a%20named%20range%20to%20an%20existing%20formula-thumb.png)](https://exceljet.net/videos/how-to-apply-a-named-range-to-an-existing-formula)

### [How to apply a named range to an existing formula](https://exceljet.net/videos/how-to-apply-a-named-range-to-an-existing-formula)

Sometimes you might create named ranges after you've already built formulas. In that case, Excel will not automatically update the formulas to use the named ranges. However, there are a couple of ways you can apply named ranges to formulas that already exist. Let's take a look. Here we have a table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

Related functions
-----------------

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

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

*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    
*   [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)
    
*   [Count with repeating values](https://exceljet.net/formulas/count-with-repeating-values)
    
*   [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)
    
*   [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)
    
*   [Automatic row numbers in Table](https://exceljet.net/formulas/automatic-row-numbers-in-table)
    
*   [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    

### Videos

*   [How to apply a named range to an existing formula](https://exceljet.net/videos/how-to-apply-a-named-range-to-an-existing-formula)
    
*   [How to use function arguments](https://exceljet.net/videos/how-to-use-function-arguments)
    
*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    
*   [Shade groups of rows with conditional formatting](https://exceljet.net/videos/shade-groups-of-rows-with-conditional-formatting)
    

### Functions

*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    

### Links

*   [Microsoft ROW function documentation](https://support.office.com/en-us/article/row-function-3a63b74a-c4d0-4093-b49a-e76eb49a6d8d)
    

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