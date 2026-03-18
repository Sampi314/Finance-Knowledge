# Excel TOCOL function | Exceljet

**Source:** https://exceljet.net/functions/tocol-function

---

[Skip to main content](https://exceljet.net/functions/tocol-function#main-content)

[](https://exceljet.net/functions/tocol-function#)

*   [Previous](https://exceljet.net/functions/textsplit-function)
    
*   [Next](https://exceljet.net/functions/torow-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

TOCOL Function
==============

by Dave Bruns · Updated 9 Apr 2025

Related functions 
------------------

[TOROW](https://exceljet.net/functions/torow-function)

[WRAPROWS](https://exceljet.net/functions/wraprows-function)

[WRAPCOLS](https://exceljet.net/functions/wrapcols-function)

[TRIMRANGE](https://exceljet.net/functions/trimrange-function)

![Excel TOCOL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20tocol%20function.png "Excel TOCOL function")

Summary
-------

The Excel TOCOL function transforms an array into a single column. By default, TOCOL will scan values by row, but TOCOL can also scan values by column.

Purpose 
--------

Transform array to single column

Return value 
-------------

A single column of values

Syntax
------

    =TOCOL(array,ignore,scan_by_column)

*   _array_ - The array to transform.
*   _ignore_ - Setting to ignore blanks and errors.
*   _scan\_by\_column_ - Scan array by column. TRUE = by column, FALSE = by row (default).

Using the TOCOL function 
-------------------------

The TOCOL function transforms an [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
 into a single column. By default, TOCOL will scan values by row, left to right. However, TOCOL can also be configured to scan the array by column, top to bottom. TOCOL also provides options for skipping empty cells and errors.

The TOCOL function takes three arguments: _array_, _ignore_, and _scan\_by\_column_. _Array_ is the only required argument and represents the array or range to be transformed. The _ignore_ argument controls what values TOCOL will optionally ignore. The options for _ignore_ are as follows:

| Value | Purpose |
| --- | --- |
| 0 (default) | Keep all values |
| 1   | Ignore blanks |
| 2   | Ignore errors |
| 3   | Ignore blanks and errors |

The _scan\_by\_column_ argument is a boolean value that controls how TOCOL reads values from the source array. By default, _scan\_by\_column_ is FALSE and TOCOL will read values "by row" from left to right. At the end of each row, TOCOL will drop down and read values from the next row in the same order. To read values instead by column, set _scan\_by\_column_ to TRUE or 1. In this mode, TOCOL will read values from top to bottom in the first column in the array, then move one column to the right, and read the next column in the same order.

Use the TOCOL function to transform an array into a single _column_ and the [TOROW function](https://exceljet.net/functions/torow-function)
 to transform an array into a single _row_. The [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 will transpose an array from horizontal to vertical and vice versa, but it won't restructure the array.

### Basic usage

By default, the TOCOL function transforms a two-dimensional array into a single column, working through the array one row at a time. In the example below, the formula in F4 is:

    =TOCOL(B4:D5)
    

![TOROW basic example](https://exceljet.net/sites/default/files/images/functions/inline/TOCOL%20function%20basic%20example.png "TOROW basic example")

TOCOL converts the 2 x 3 array in B4:D5 into the 6 x 1 array in F4:K9.

_Note: In Excel,_ [_arrays map directly to ranges_](https://exceljet.net/glossary/array)
_. Technically, the array is converted and the result lands in cell F4, where it_ [_spills_](https://exceljet.net/glossary/spill)
 _into the range F4:F9._

### Ignore blanks and errors

The _ignore_ argument in TOCOL can be set to ignore blanks and/or errors like this:

    =TOCOL(array) // default
    =TOCOL(array,1) // ignore blanks
    =TOCOL(array,2) // ignore errors
    =TOCOL(array,3) // ignore blanks and errors
    

The screen below shows how these options work with the range B4:D7, which contains both blanks and errors.

![TOCOL example - ignore blanks and errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TOCOL%20example%20-%20ignore%20blanks%20and%20errors.png?itok=egWCBZun "TOCOL example - ignore blanks and errors")

### Scan by column

By default, TOCOL will read values "by row" from left to right. To read values instead by column, set _scan\_by\_column_ to TRUE or 1. The worksheet below shows the default "by row" behavior in F4. In cell H4, _scan\_by\_column_ is set to TRUE:

    =TOCOL(B4:D5,,TRUE)
    

![TOCOL example - scan values by column](https://exceljet.net/sites/default/files/images/functions/inline/TOCOL%20example%20-%20scan%20values%20by%20column.png "TOCOL example - scan values by column")

Notice the resulting array is the same size, but the values appear in a different order. Also note the optional _ignore_ argument has been left empty.

TOCOL function examples
-----------------------

[![Excel formula: Get address of named range or table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_address_of_named_range_or_table.png "Excel formula: Get address of named range or table")](https://exceljet.net/formulas/get-address-of-named-range-or-table)

### [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)

The goal is to return the full address of a range or named range as text. The purpose of this formula is informational, not functional. It provides a way to inspect the current range for a named range, an Excel Table, or even the result of a formula. The core of the solutions explained below is the...

[![Excel formula: Get location of value in 2D array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_location_of_value_in_2D_array.png "Excel formula: Get location of value in 2D array")](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

### [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

In this example, the goal is to return a list of the locations for a specific value in a 2D array of values (i.e., a table). The target value is entered in cell N5, and the table being tested is in the range C4:L16. The coordinates are supplied from row 4 and column B, as seen in the worksheet. In...

Related functions
-----------------

[![Excel TOROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20torow%20function.png "Excel TOROW function")](https://exceljet.net/functions/torow-function)

### [TOROW Function](https://exceljet.net/functions/torow-function)

The Excel TOROW function transforms an array into a single row. By default, TOROW will scan values by row, but TOROW can also scan values by column.

[![Excel WRAPROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20wraprows%20function.png "Excel WRAPROWS function")](https://exceljet.net/functions/wraprows-function)

### [WRAPROWS Function](https://exceljet.net/functions/wraprows-function)

The Excel WRAPROWS function converts a one-dimensional array into a two-dimensional array by wrapping values into separate rows. The length of each row is given as the _wrap\_count_ argument: when the count is reached, WRAPROWS starts a new row....

[![Excel WRAPCOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20wrapcols%20function.png "Excel WRAPCOLS function")](https://exceljet.net/functions/wrapcols-function)

### [WRAPCOLS Function](https://exceljet.net/functions/wrapcols-function)

The Excel WRAPCOLS function converts a one-dimensional array into a two-dimensional array by wrapping values into separate columns. The length of each column is given as the _wrap\_count_ argument: when the count is reached, WRAPCOLS starts a new column....

[![Excel TRIMRANGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_trimrange_function.png "Excel TRIMRANGE function")](https://exceljet.net/functions/trimrange-function)

### [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)

The Excel TRIMRANGE function removes empty rows and columns from the outer edges of a range of data. The result is a "trimmed" range that only includes data from the used portion of the range. Because it is a formula, TRIMRANGE will update the range dynamically when data is added or removed...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)
    
*   [Get address of named range or table](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    

### Functions

*   [TOROW Function](https://exceljet.net/functions/torow-function)
    
*   [WRAPROWS Function](https://exceljet.net/functions/wraprows-function)
    
*   [WRAPCOLS Function](https://exceljet.net/functions/wrapcols-function)
    
*   [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)
    

### Links

*   [Microsoft TOCOL function documentation](https://support.microsoft.com/en-us/office/tocol-function-22839d9b-0b55-4fc1-b4e6-2761f8f122ed)
    

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