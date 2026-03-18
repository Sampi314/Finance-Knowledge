# Copy value from every nth row - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/copy-value-from-every-nth-row

---

[Skip to main content](https://exceljet.net/formulas/copy-value-from-every-nth-row#main-content)

[](https://exceljet.net/formulas/copy-value-from-every-nth-row#)

*   [Previous](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    
*   [Next](https://exceljet.net/formulas/cost-of-living-adjustment)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Copy value from every nth row
=============================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[OFFSET](https://exceljet.net/functions/offset-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Copy value from every nth row](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/copy%20value%20every%20nth%20row_0.png "Excel formula: Copy value from every nth row")

Summary
-------

To copy values or generate references with a pattern like every 3rd row, every 7th line, etc. you can use a formula based on the [OFFSET](https://exceljet.net/functions/offset-function)
 and [ROW](https://exceljet.net/functions/row-function)
 functions. In the example shown, the formula in D5 is:

    =OFFSET($B$5,ROW(D1)*3-1,0)
    

Which copies values from every 3rd row in column B as the formula is copied down.

Generic formula
---------------

    =OFFSET($B$5,ROW(A1)*n-1,0)

Explanation 
------------

In this example, the goal is to copy every nth value from column B, where n is a variable that can be changed as needed.

In Excel, it's difficult to create formulas that skip rows following a certain pattern, because the references in the formula will automatically change as the formula is copied in 1-step increments across cells. However, with a little work it's possible to construct formula references that follow specific patterns. In this example, we are using the [OFFSET function](https://exceljet.net/functions/offset-function)
, which is designed to create references to other cells, or cell ranges, based on a given starting point, or origin.

### Starting at n

In the example shown, the formula in D5, copied down, is:

    =OFFSET($B$5,ROW(D1)*3-1,0)
    

which copies every third value from the [range](https://exceljet.net/glossary/range)
 B5:B59, starting at B7, which is the third cell in the range. The starting point inside the [OFFSET function](https://exceljet.net/functions/offset-function)
 is the _reference_ [argument](https://exceljet.net/glossary/function-argument)
, provided as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
:

    =OFFSET($B$5
    

The reference to B5 is locked so that it won't change as the formula is copied down. The next argument is _rows_, which indicates the desired row offset from the starting reference. Rather than a typical hardcoded number, rows is provided as an expression that calculates the required offset:

    ROW(D1)*3)-1 // calculate rows offset
    

This is where n is provided as 3, in order to copy every third value. Here, the [ROW function](https://exceljet.net/functions/row-function)
 is used to get the row number for cell D1. We start with D1 because we want to start with 1 for the first value. As the formula is copied down the column, the value returned by ROW increments by 1 because the reference to D1 is [relative](https://exceljet.net/glossary/relative-reference)
. This result from ROW is multiplied by n, which is what creates the "every nth" pattern, in this case, "every 3rd". As the formula is copied down, the expression is evaluated like this:

    ROW(D1)*3-1 // returns 2
    ROW(D2)*3-1 // returns 5
    ROW(D3)*3-1 // returns 8
    

These numbers may look odd to you in the context of "every 3rd value" but remember, this is an _offset_, starting with cell B5. The reason we subtract 1 is because the OFFSET function doesn't include the reference cell when the rows argument is applied. In other words, offsetting by one row from A1 returns A2:

    =OFFSET(A1,1,0) // returns A2
    

Subtracting 1 takes this behavior into account.

Finally, the columns argument is provided as zero (0), since we don't want any column offset; we want to stay in column B. As the formula is copied down, it returns the required references:

    =OFFSET($B$5,ROW(D1)*3-1,0) // returns B7
    =OFFSET($B$5,ROW(D2)*3-1,0) // returns B10
    =OFFSET($B$5,ROW(D3)*3-1,0) // returns B13
    

The number n can be changed as needed. For example, if n is changed to 5, the formula will pick up every 5th value.

### Starting at 1

To start copying at the first row in a given range, then follow the "every nth" pattern afterward, you can adjust the formula like this:

    =OFFSET($B$5,(ROW(A1)-1)*n,0)
    

In this version, we subtract 1 directly from the result from the ROW function. This "zeros out" the first instance of rows, so that OFFSET returns a reference to the current cell. The formula in cell F5 uses this approach:

    =OFFSET($B$5,(ROW(F1)-1)*3,0)
    

The results can be seen in column F.

Related formulas
----------------

[![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")](https://exceljet.net/formulas/copy-value-from-every-nth-column)

### [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Sum every n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20n%20rows.png "Excel formula: Sum every n rows")](https://exceljet.net/formulas/sum-every-n-rows)

### [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)

In this example, the goal is to calculate a weekly total using the data as shown. Notice each week corresponds to 5 rows of data (Monday-Friday) so we will need to sum values in every 5 rows. To build a range that corresponds to the correct 5 rows for each week, we use the OFFSET function. To sum...

[![Excel formula: Unwrap column into fields](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unwrap%20column%20into%20fields.png "Excel formula: Unwrap column into fields")](https://exceljet.net/formulas/unwrap-column-into-fields)

### [Unwrap column into fields](https://exceljet.net/formulas/unwrap-column-into-fields)

In this example the goal is to "unwrap" a column of values into separate fields. The values are spaced evenly apart, and the result should be all related values on one row, where each column corresponds to a field of information. The input data appears in column B. Each "record" in the data has...

Related functions
-----------------

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

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

*   [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)
    
*   [Unwrap column into fields](https://exceljet.net/formulas/unwrap-column-into-fields)
    

### Functions

*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
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