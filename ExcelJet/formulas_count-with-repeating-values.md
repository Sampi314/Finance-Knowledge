# Count with repeating values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-with-repeating-values

---

[Skip to main content](https://exceljet.net/formulas/count-with-repeating-values#main-content)

[](https://exceljet.net/formulas/count-with-repeating-values#)

*   [Previous](https://exceljet.net/formulas/count-values-out-of-tolerance)
    
*   [Next](https://exceljet.net/formulas/course-completion-status-summary)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Count with repeating values
===========================

by Dave Bruns · Updated 7 Jun 2016

Related functions 
------------------

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[COLUMN](https://exceljet.net/functions/column-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Count with repeating values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20with%20repeating%20values.png "Excel formula: Count with repeating values")

Summary
-------

To count with repeating numbers (for example: 1111,2222,3333,4444, etc.) you can use a formula based on the ROUNDUP function, with help from either ROW or COLUMN.

In the example shown, the formula in C4 is:

    =ROUNDUP((COLUMN()-2)/$B4,0)
    

Generic formula
---------------

    =ROUNDUP((COLUMN()-offset)/repeat,0)

Explanation 
------------

The core of this formula is the ROUNDUP function. The ROUNDUP function works like the ROUND function except that when rounding, the ROUNDUP function will always round the numbers 1-9 up. In this formula, we use that fact to repeat values.

To supply a number to ROUNDUP, we are using this expression:

    (COLUMN()-2)/$B4
    

Without a reference, COLUMN generates the column number of the cell it appears in, in this case 3 for cell C4.

The number 2 is simply an offset value, to account for the fact column C is column 3. We subtract 2 to normalize back to 1.

Cell B4 holds the value that represents the number of times to "repeat" a count. We've locked the column reference so that the repeat value remains fixed as the formula is copied across the table.

The normalized column number is divided by the repeat value and the result is fed into ROUNDUP as the number to round. For number of places, we use zero, so that rounding goes to the next integer.

Once the column count is evenly divisible by the repeat value, the count advances.

### Rows instead of columns

If you need to count in rows, instead of columns, just adjust the formula like so:

    =ROUNDUP((ROW()-offset)/repeat,0)
    

Related functions
-----------------

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

[![Excel COLUMN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel%20column%20function2.png "Excel COLUMN function")](https://exceljet.net/functions/column-function)

### [COLUMN Function](https://exceljet.net/functions/column-function)

The Excel COLUMN function returns the column number for a reference. For example, COLUMN(C5) returns 3, since C is the third column in the spreadsheet. When no reference is provided, COLUMN returns the column number of the cell which contains the formula.

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

### Functions

*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [COLUMN Function](https://exceljet.net/functions/column-function)
    
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