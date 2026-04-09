# Excel TOROW function | Exceljet

**Source:** https://exceljet.net/functions/torow-function

---

[Skip to main content](https://exceljet.net/functions/torow-function#main-content)

[](https://exceljet.net/functions/torow-function#)

*   [Previous](https://exceljet.net/functions/tocol-function)
    
*   [Next](https://exceljet.net/functions/translate-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

TOROW Function
==============

by Dave Bruns · Updated 9 Apr 2025

Related functions 
------------------

[TOCOL](https://exceljet.net/functions/tocol-function)

[WRAPROWS](https://exceljet.net/functions/wraprows-function)

[WRAPCOLS](https://exceljet.net/functions/wrapcols-function)

[TRIMRANGE](https://exceljet.net/functions/trimrange-function)

![Excel TOROW function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20torow%20function.png "Excel TOROW function")

Summary
-------

The Excel TOROW function transforms an array into a single row. By default, TOROW will scan values by row, but TOROW can also scan values by column.

Purpose 
--------

Transform array to single row

Return value 
-------------

A single row of values

Syntax
------

    =TOROW(array,ignore,scan_by_column)

*   _array_ - The array to transform.
*   _ignore_ - Control to ignore blanks and errors.
*   _scan\_by\_column_ - Scan array by column. TRUE = by column, FALSE = by row (default).

Using the TOROW function 
-------------------------

The TOROW function transforms an [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
 into a single row. TOROW can scan values by row, left to right (default) or by column, top to bottom.

The TOROW function takes three arguments: _array_, _ignore_, and _scan\_by\_column_. _Array_ is the only required argument and represents the array or range to be transformed. The _ignore_ argument controls what values TOROW will optionally ignore. The options for _ignore_ are as follows:

| Value | Purpose |
| --- | --- |
| 0 (default) | Keep all values |
| 1   | Ignore blanks |
| 2   | Ignore errors |
| 3   | Ignore blanks and errors |

The _scan\_by\_column_ argument is a boolean value that controls how TOROW reads values from the source array. By default, _scan\_by\_column_ is FALSE and TOROW will read values "by row" from left to right. At the end of each row, TOROW will move down and read values from the _next row_ in the same order. To read values instead by column, set _scan\_by\_column_ to TRUE or 1. In this mode, TOROW will read values from top to bottom in the first column, then move one column to the right, and read the next column from top to bottom.

Use the TOROW function to transform an array into a single _row_ and the [TOCOL function](https://exceljet.net/functions/tocol-function)
 to transform an array into a single _row_. The [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 will transpose an array from horizontal to vertical and vice versa, but it won't restructure the array.

### **Basic usage**

By default, the TOROW function transforms a two-dimensional array into a single row, one row at a time. In the example below, the formula in F4 is:

    =TOROW(B4:D5)
    

![TOROW basic example](https://exceljet.net/sites/default/files/images/functions/inline/TOROW%20basic%20example.png "TOROW basic example")

TOROW converts the 2 x 3 array in B4:D5 into the 1 x 6 array in F4:K4.

_Note: in Excel,_ [_arrays map directly to ranges_](https://exceljet.net/glossary/array)
_. Technically, the array is converted and the result lands in cell F4, where it spills into the range F4:K4._

### Ignore blanks and errors

The _ignore_ argument in TOROW can be set to ignore blanks and/or errors like this:

    =TOROW(array,1) // ignore blanks
    =TOROW(array,2) // ignore errors
    =TOROW(array,3) // ignore blanks and errors
    

The screen below shows how these options work with the range B3:D6.

![TOROW function - ignore blanks and errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TOROW%20function%20ignore%20blanks%20and%20errors.png?itok=l286reNK "TOROW function - ignore blanks and errors")

### Scan by column

By default, TOROW will read values "by row" from left to right. To read values instead by column, set _scan\_by\_column_ to TRUE or 1. The worksheet below shows the default "by row" behavior in F4. In cell F7, _scan\_by\_column_ is set to TRUE:

    =TOROW(B4:D5,,TRUE)
    

![TOROW function - scan by column](https://exceljet.net/sites/default/files/images/functions/inline/TOROW%20scan%20by%20column.png "TOROW function - scan by column")

Notice the resulting array is the same size, but the values appear in a different order.

TOROW function examples
-----------------------

[![Excel formula: Extract numbers from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_numbers_from_text.png "Excel formula: Extract numbers from text")](https://exceljet.net/formulas/extract-numbers-from-text)

### [Extract numbers from text](https://exceljet.net/formulas/extract-numbers-from-text)

In this example, the goal is to extract the numbers from a set of property listings which describe the number of bedrooms and bathrooms, the size of the house in sq. ft., and the size of the lot in acres. Traditionally, this kind of problem has been quite difficult in Excel because each number must...

Related functions
-----------------

[![Excel TOCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20tocol%20function.png "Excel TOCOL function")](https://exceljet.net/functions/tocol-function)

### [TOCOL Function](https://exceljet.net/functions/tocol-function)

The Excel TOCOL function transforms an array into a single column. By default, TOCOL will scan values by row, but TOCOL can also scan values by column.

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

*   [Extract numbers from text](https://exceljet.net/formulas/extract-numbers-from-text)
    

### Functions

*   [TOCOL Function](https://exceljet.net/functions/tocol-function)
    
*   [WRAPROWS Function](https://exceljet.net/functions/wraprows-function)
    
*   [WRAPCOLS Function](https://exceljet.net/functions/wrapcols-function)
    
*   [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)
    

### Links

*   [Microsoft TOROW function documentation](https://support.microsoft.com/en-us/office/torow-function-b90d0964-a7d9-44b7-816b-ffa5c2fe2289)
    

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