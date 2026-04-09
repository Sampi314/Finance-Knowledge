# Excel CHOOSEROWS function | Exceljet

**Source:** https://exceljet.net/functions/chooserows-function

---

[Skip to main content](https://exceljet.net/functions/chooserows-function#main-content)

[](https://exceljet.net/functions/chooserows-function#)

*   [Previous](https://exceljet.net/functions/choosecols-function)
    
*   [Next](https://exceljet.net/functions/detectlanguage-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

CHOOSEROWS Function
===================

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

[TAKE](https://exceljet.net/functions/take-function)

[DROP](https://exceljet.net/functions/drop-function)

[EXPAND](https://exceljet.net/functions/expand-function)

![Excel CHOOSEROWS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20chooserows%20function.png "Excel CHOOSEROWS function")

Summary
-------

The Excel CHOOSEROWS function returns specific rows from an array or range. The rows to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a row in the given array.

Purpose 
--------

Return specific rows from an array

Return value 
-------------

Extracted rows in a single array

Syntax
------

    =CHOOSEROWS(array,row_num1,[row_num2],...)

*   _array_ - The array to extract rows from.
*   _row\_num1_ - The numeric index of the first row to return.
*   _row\_num2_ - \[optional\] The numeric index of the second row to return.

Using the CHOOSEROWS function 
------------------------------

The Excel CHOOSEROWS function returns specific rows from an [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
. The rows to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a row in the source array. The result from CHOOSEROWS is always a single array that [spills](https://exceljet.net/glossary/spill)
 onto the worksheet.

The first argument in the CHOOSEROWS function is _array_. _Array_ can be a range, or an array from another formula. Additional arguments are in the form row_\_num1_, row_\_num2_, row_\_num3_, etc. Each number represents a specific row to extract from the array, and should be supplied as a whole number.

### Basic usage

To get rows 1 and 3 from an array, you can use CHOOSEROWS like this:

    =CHOOSEROWS(A1:A5,1,3) // rows 1 and 3
    

To get the same two rows in reverse order:

    =CHOOSEROWS(A1:A5,3,1) // rows 3 and 1
    

CHOOSEROWS will return a #VALUE! error if a requested row number is out of range:

    =CHOOSEROWS(A1:A5,6) // returns #VALUE!
    

### With array constants

Another option for specifying which rows to return is to use an [array constant](https://exceljet.net/glossary/array-constant)
 like {1,4,7} as the second [argument](https://exceljet.net/glossary/function-argument)
 (_row\_num1)_. In the example below, the formula in H3 is:

    =CHOOSEROWS(B3:F9,{1,4,7})
    

With the array constant {1,4,7} given as the second argument, CHOOSEROWS returns rows 1, 4, and 7:

![CHOOSEROWS function with array constant](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/CHOOSEROWS%20function%20with%20array%20constant.png?itok=cVXl3Jv6 "CHOOSEROWS function with array constant")

The array constant can be provided in the form {1,2,3} or {1;2;3}.

### With negative row numbers

A nice feature of CHOOSEROWS is that you can use _negative_ row numbers to extract rows from the _end_ of a range. For example, to get the last row of a range, you can use a formula like this:

    =CHOOSEROWS(range,-1)

To get the second to last row, you can use:

    =CHOOSEROWS(range,-2)

To get the last three rows in the order that they appear:

    =CHOOSEROWS(range,-3,-2,-1)

You can also mix negative and positive row numbers. To return the first and last row at the same time:

    =CHOOSEROWS(range,1,-1)

### With arrays

As seen above, you can use an [array constant](https://exceljet.net/glossary/array-constant)
 as the second argument in CHOOSEROWS to indicate rows. You can also use an array created with a formula. For example, the formula below uses CHOOSEROWS and the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 to reverse the order of rows in an array:

    =CHOOSEROWS(B3:D9,SEQUENCE(ROWS(B3:D9),,ROWS(B3:D9),-1))
    

When given a 7-row range or array, SEQUENCE returns {7;6;5;4;3;2;1} to CHOOSEROWS, and CHOOSEROWS returns the 7 rows in reverse order:

![CHOOSEROWS function to reverse row order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/CHOOSEROWS%20function%20to%20reverse%20rows.png?itok=qC0-fZXc "CHOOSEROWS function to reverse row order")

The formula returns all the rows in Array, starting with the last row.

### Notes

*   CHOOSEROWS will return a #VALUE error if a row number is out of range.

CHOOSEROWS function examples
----------------------------

[![Excel formula: Random list of names](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random-list-of-names.png "Excel formula: Random list of names")](https://exceljet.net/formulas/random-list-of-names)

### [Random list of names](https://exceljet.net/formulas/random-list-of-names)

In this example, the goal is to create a list of 10 random names from a larger list of 100 names. In other words, we want to select a random subset of names from a larger list. The names to select from are in column B, starting in row 5. The formula should handle any number of names in the input...

[![Excel formula: Get nth match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match.png "Excel formula: Get nth match")](https://exceljet.net/formulas/get-nth-match)

### [Get nth match](https://exceljet.net/formulas/get-nth-match)

The goal is to retrieve the nth matching record in a set of data, after filtering on a specific product. In the worksheet shown, the product in H4 and the value for n in H5 are inputs that can be changed at any time. For instance, if the product in H4 is "A" and the value in H5 is 3, the formula...

[![Excel formula: Repeat range of values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat_range_of_values.png "Excel formula: Repeat range of values")](https://exceljet.net/formulas/repeat-range-of-values)

### [Repeat range of values](https://exceljet.net/formulas/repeat-range-of-values)

In this example, the goal is to repeat a range of values. This can be done in various ways in Excel, but I think the CHOOSEROWS/ CHOOSECOLS functions are the easiest way to retrieve values from the range for now. Both functions work natively with two-dimensional ranges and can accept a single array...

Related functions
-----------------

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

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

*   [Get nth match](https://exceljet.net/formulas/get-nth-match)
    
*   [Repeat range of values](https://exceljet.net/formulas/repeat-range-of-values)
    
*   [Random list of names](https://exceljet.net/formulas/random-list-of-names)
    

### Functions

*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    
*   [EXPAND Function](https://exceljet.net/functions/expand-function)
    

### Links

*   [Microsoft CHOOSEROWS function documentation](https://support.microsoft.com/en-us/office/chooserows-function-51ace882-9bab-4a44-9625-7274ef7507a3)
    

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