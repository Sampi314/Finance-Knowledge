# Unwrap column into fields - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/unwrap-column-into-fields

---

[Skip to main content](https://exceljet.net/formulas/unwrap-column-into-fields#main-content)

[](https://exceljet.net/formulas/unwrap-column-into-fields#)

*   [Previous](https://exceljet.net/formulas/transpose-table-without-zeros)
    
*   [Next](https://exceljet.net/formulas/validate-input-with-check-mark)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Unwrap column into fields
=========================

by Dave Bruns · Updated 2 Jan 2024

Related functions 
------------------

[OFFSET](https://exceljet.net/functions/offset-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Unwrap column into fields](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/unwrap%20column%20into%20fields.png "Excel formula: Unwrap column into fields")

Summary
-------

To unwrap a column of values into separate fields, where field values are spaced evenly apart, you can use a formula based on the [OFFSET function](https://exceljet.net/functions/offset-function)
, with help from the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
. In the example shown, the formula in D5, copied down, is:

    =TRANSPOSE(OFFSET($B$5,(ROW(D1)-1)*4,0,3))
    

As the formula is copied down, the data is separated into three fields: Name, Street, and City/State/Zip.

_Note: In the generic version formula, n represents the number of cells between records, and k represents the number of fields to extract._

> This formula requires Excel 2021 or later to work correctly.

Generic formula
---------------

    =TRANSPOSE(OFFSET($A$1,(ROW(A1)-1)*n,0,k))

Explanation 
------------

In this example the goal is to "unwrap" a column of values into separate fields. The values are spaced evenly apart, and the result should be all related values on one row, where each column corresponds to a field of information. The input data appears in column B. Each "record" in the data has three values:  Name, Street, and City/State/Zip (combined). New records start every 4th row, and records are separated by an empty cell, which can be thought of as a fourth field that will be ignored. The formula in D5 is:

    =TRANSPOSE(OFFSET($B$5,(ROW(D1)-1)*4,0,3))
    

As this formula is copied down, it extracts the values for each record into cells in a single row.

_Note: the formula explained below builds on more [basic examples explained here](https://exceljet.net/formulas/copy-value-from-every-nth-row)
._

### Collect fields

Working from the inside out, the core of the solution is the [OFFSET function](https://exceljet.net/functions/offset-function)
:

    OFFSET($B$5,(ROW(D1)-1)*4,0,3)
    

The OFFSET function is designed to create a reference that is "offset" from a starting point by a given number of _rows_ and _columns_.  In addition, OFFSET has an optional _width_ and height _arguments_, which specify the size of the reference to be returned.

The starting point inside the [OFFSET function](https://exceljet.net/functions/offset-function)
 is the _reference_ [argument](https://exceljet.net/glossary/function-argument)
, provided as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
:

    =OFFSET($B$5
    

The reference to B5 is locked so that it won't change as the formula is copied down. The next argument is _rows_, which indicates the desired row offset from the starting reference. Rather than a hardcoded number, _rows_ is provided as an expression that calculates the required offset:

    (ROW(D1)-1)*4 // calculate rows offset
    

This is where n is provided as 4, in order to reference every fourth value. The [ROW function](https://exceljet.net/functions/row-function)
 is used to get the row number for cell D1. We start with D1, because we want to start with the number 1.  We subtract 1, because we want the first _rows_ offset to be zero. In other words, we want to zero out the _rows_ argument and start with cell B5. As the formula is copied down the column, the value returned by ROW increments by 1, and creates the logic needed to reference every 4th value. [See this formula example for a more detailed explanation](https://exceljet.net/formulas/copy-value-from-every-nth-row)
.

The last two arguments provided to OFFSET are _cols_ and _height_.  _Cols_ is hardcoded as 0 because we want to stay in column B. The _height_ argument is hardcoded as 3, because each record contains 3 cells of information stacked vertically, and we are intentionally ignoring the empty cell between records. As the formula is copied down, the OFFSET function generates the following references:

    OFFSET($B$5,(ROW(D1)-1)*4,0,3) // returns B5:B7
    OFFSET($B$5,(ROW(D2)-1)*4,0,3) // returns B9:B11
    OFFSET($B$5,(ROW(D3)-1)*4,0,3) // returns B13:B15
    

[More examples of OFFSET here](https://exceljet.net/functions/offset-function)
.

### Transpose fields

The OFFSET function does almost all of the work in this formula, collecting all three field values for each record. However, the result from OFFSET is a _vertical_ [array](https://exceljet.net/glossary/array)
 of values, and we need a _horizontal_ array as a final result. To convert the horizontal array into a vertical array, use the TRANSPOSE function. In the final formula, OFFSET is nested inside TRANSPOSE like this:

    =TRANSPOSE(OFFSET($B$5,(ROW(D1)-1)*4,0,3))
    

OFFSET returns a vertical array like:

    {"Micheal Lam";"228 James Street";"Minneapolis, MN 55420"}
    
    

And TRANSPOSE catches this array and changes it into a horizontal array like this:

    {"Micheal Lam","228 James Street";"Minneapolis, MN 55420"}
    

Note the commas have replaced the semi-colons. The [array](https://exceljet.net/glossary/array)
 is returned to cell D5 and the three values [spill](https://exceljet.net/glossary/spill)
 into the range D5:F5.

Related formulas
----------------

[![Excel formula: Copy value from every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20row_0.png "Excel formula: Copy value from every nth row")](https://exceljet.net/formulas/copy-value-from-every-nth-row)

### [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)

In this example, the goal is to copy every nth value from column B, where n is a variable that can be changed as needed. In Excel, it's difficult to create formulas that skip rows following a certain pattern, because the references in the formula will automatically change as the formula is copied...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Sum every n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20n%20rows.png "Excel formula: Sum every n rows")](https://exceljet.net/formulas/sum-every-n-rows)

### [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)

In this example, the goal is to calculate a weekly total using the data as shown. Notice each week corresponds to 5 rows of data (Monday-Friday) so we will need to sum values in every 5 rows. To build a range that corresponds to the correct 5 rows for each week, we use the OFFSET function. To sum...

Related functions
-----------------

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)
    

### Functions

*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

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