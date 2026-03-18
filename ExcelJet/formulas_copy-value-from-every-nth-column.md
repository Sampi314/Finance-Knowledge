# Copy value from every nth column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/copy-value-from-every-nth-column

---

[Skip to main content](https://exceljet.net/formulas/copy-value-from-every-nth-column#main-content)

[](https://exceljet.net/formulas/copy-value-from-every-nth-column#)

*   [Previous](https://exceljet.net/formulas/convert-pounds-to-kilograms)
    
*   [Next](https://exceljet.net/formulas/copy-value-from-every-nth-row)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Copy value from every nth column
================================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[OFFSET](https://exceljet.net/functions/offset-function)

[COLUMN](https://exceljet.net/functions/column-function)

![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")

Summary
-------

To copy values or generate references with a pattern like every 3rd column, every 5th column, etc. you can use a formula based on the [OFFSET](https://exceljet.net/functions/offset-function)
 and [COLUMN](https://exceljet.net/functions/column-function)
 functions. In the example shown, the formula in C8 is:

    =OFFSET($C$5,0,(COLUMN(A8)*3)-1)
    

Which can be copied across row 8 to pick up every 3rd value from row 5.

Generic formula
---------------

    =OFFSET($C$5,0,(COLUMN(A8)*n)-1)

Explanation 
------------

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct formula references that will follow a specific pattern using the OFFSET function.

The OFFSET function is designed to create references by using "offsets" from a starting cell. In the example shown, the starting cell is C5, provided to OFFSET as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 so it won't change as the formula is copied:

    =OFFSET($C$5
    

For the rows argument, we provide zero, since we want to stay in the same row. For the columns argument, we use a sub-formula to calculate the required offset value:

    (COLUMN(A8)*3)-1
    

We use A8 inside COLUMN to return 1 (since A is the first column), then multiply by n (which is 3 in this case) to get 3.

As the formula is copied across the row to the right, the value returned by COLUMN increments by 1, which is what creates the "nth pattern".

### Starting at 1

If you want to start copying at the first value, you can adjust the formula like this:

    =OFFSET($C$5,0,(COLUMN(A11)-1)*3)
    

By subtracting 1, we force a column offset of zero in the first formula.

### Copy to rows instead of columns

To copy from columns into rows, you can modify the formula like this:

    =OFFSET($C$5,0,(ROW(C1)*3)-1)
    

Here, the COLUMN function has been replaced with the [ROW function](https://exceljet.net/functions/row-function)
, and a reference to the first row in the column, so that incrementing works correctly as the formula is copied down into multiple rows.

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

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

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
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    

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