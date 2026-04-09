# Excel EXPAND function | Exceljet

**Source:** https://exceljet.net/functions/expand-function

---

[Skip to main content](https://exceljet.net/functions/expand-function#main-content)

[](https://exceljet.net/functions/expand-function#)

*   [Previous](https://exceljet.net/functions/drop-function)
    
*   [Next](https://exceljet.net/functions/filter-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

EXPAND Function
===============

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[DROP](https://exceljet.net/functions/drop-function)

[TAKE](https://exceljet.net/functions/take-function)

[CHOOSEROWS](https://exceljet.net/functions/chooserows-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

![Excel EXPAND function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20expand%20function.png "Excel EXPAND function")

Summary
-------

The EXPAND function expands an array by adding rows and columns, which are supplied as separate arguments. The numbers given for rows and columns represent the dimensions of the final array.

Purpose 
--------

Expand array by adding rows or columns

Return value 
-------------

Expanded array

Syntax
------

    =EXPAND(array,[rows],[columns],[pad_with])

*   _array_ - The array to expand.
*   _rows_ - \[optional\] The final number of rows. Default is total rows.
*   _columns_ - \[optional\] The final number of columns. Default is total columns.
*   _pad\_with_ - \[optional\] Value to use for new cells. Default is #N/A.

Using the EXPAND function 
--------------------------

The EXPAND function expands an array by adding rows and columns, which are supplied as separate arguments. The values given for rows and columns represent the dimensions of the final array, not the number of rows or columns to add.

The EXPAND function takes four arguments: _array_, _rows_, _columns_, and _pad\_with_. _Array_ is required, along with at least one value for _rows_ or _columns_. _Array_ can be a [range](https://exceljet.net/glossary/range)
 or an [array](https://exceljet.net/glossary/array)
 from another formula. _Rows_ and _columns_ must be positive numbers that are at least the same size as the given _array_. If not provided, both rows and columns will default to the dimensions of _array_.

### Basic usage

To expand an array to be 5 rows by 4 columns, you can use EXPAND like this:

    =EXPAND(array,5,4) // expand to 5 x 4
    

By default, any new cells created will be filled with #N/A errors. To expand an array to be 10 rows by 3 columns, and fill new cells with "x":

    =EXPAND(array,10,3,"x") // expand to 10 x 3, fill with "x"
    

Note that the numbers given for rows and columns represent _final_ dimensions, not new rows and columns.

### Default and custom padding

In the example below, we are adding 2 rows to an existing array with 5 rows. The result is an array with 7 rows. The formula in F3 is:

    =EXPAND(B3:D7,7) // default padding
    

![ EXPAND function - add two rows default padding](https://exceljet.net/sites/default/files/images/functions/inline/EXPAND%20function%20-%20add%20two%20rows%20default%20padding.png " EXPAND function - add two rows default padding")

Notice that by default, EXPAND fills the new empty cells with the #N/A error. In the screen, the formula in F3 has been modified to provide zero (0) for the pad\_with argument:

    =EXPAND(B3:D7,7,,0) // pad with 0
    

![ EXPAND function - add two rows custom padding](https://exceljet.net/sites/default/files/images/functions/inline/EXPAND%20function%20-%20add%20two%20rows%20custom%20padding.png " EXPAND function - add two rows custom padding")

Notice the new cells now contain zero. Also notice that because we are not providing a value for _columns_, we need to add another comma after _rows_, in order to place the zero in the right location as the _pad\_with_ argument.

### Notes

*   If _rows_ is less than the row count in _array_, EXPAND will return a #VALUE! error.
*   If _columns_ is less than the column count in _array_, EXPAND will return a #VALUE! error.

Related functions
-----------------

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel CHOOSEROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20chooserows%20function.png "Excel CHOOSEROWS function")](https://exceljet.net/functions/chooserows-function)

### [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)

The Excel CHOOSEROWS function returns specific rows from an array or range. The rows to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a row in the given array.

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [DROP Function](https://exceljet.net/functions/drop-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    

### Links

*   [Microsoft EXPAND function documentation](https://support.microsoft.com/en-us/office/expand-function-7433fba5-4ad1-41da-a904-d5d95808bc38)
    

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