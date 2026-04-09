# Sum entire column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-entire-column

---

[Skip to main content](https://exceljet.net/formulas/sum-entire-column#main-content)

[](https://exceljet.net/formulas/sum-entire-column#)

*   [Previous](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)
    
*   [Next](https://exceljet.net/formulas/sum-entire-row)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum entire column
=================

by Dave Bruns · Updated 10 Sep 2022

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Sum entire column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20entire%20column.png "Excel formula: Sum entire column")

Summary
-------

To sum an _entire_ column without providing a specific range, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 with a [full column reference](https://exceljet.net/glossary/full-column-reference)
. In the example shown, the formula in F5 is:

    =SUM(D:D)
    

The result is the sum of all numbers in column D. As data is added to the table, the formula will continue to return a correct total.

Generic formula
---------------

    =SUM(A:A)

Explanation 
------------

In this example, the goal is to return the total for an entire column in an Excel worksheet. One way to do this is to use a full column reference.

### Full column references

Excel supports "[full column](https://exceljet.net/glossary/full-column-reference)
" like this:

    =SUM(A:A) // sum all of column A
    =SUM(C:C) // sum all of column C
    =SUM(A:C) // sum all of columns A:C
    

You can see how this works yourself by typing A:A or C:C into the [name box](https://exceljet.net/glossary/name-box)
 (left of the [formula bar](https://exceljet.net/glossary/formula-bar)
) and hitting return. You will see Excel select the entire column.

### Example

To solve the problem in the example worksheet, we can use a full column reference to column D with the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(D:D)
    

The result is the sum of all numeric values in column D. One advantage to full column references is that they will automatically include new data. As entries are added to the table, the formula will automatically include the new amounts.

### Advantages and risks

The main advantage to full column references is simplicity. Simple and very compact, a full column reference will automatically include all data in a column, even as data is added or removed. However, full column references come with certain risks. One risk is that you may accidentally include extra data in a calculation. For example, if you use =SUM(A:A) to sum numbers in column A, you are targeting over 1 million cells. If column A includes forgotten dates somewhere far below in the worksheet, the [numeric value](https://exceljet.net/glossary/excel-date)
 of these dates will be included, and SUM will return an incorrect result. Another risk is performance. Because so many cells are included, full column references can cause severe performance problems in certain worksheets or formulas.

### Alternatives

There are good alternatives to full column references. If you need to target data that may change in size, a good solution is an [Excel Table](https://exceljet.net/glossary/excel-table)
, which will automatically adapt to changing data. Another option is to use a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
.

Related formulas
----------------

[![Excel formula: Sum last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_columns.png "Excel formula: Sum last n columns")](https://exceljet.net/formulas/sum-last-n-columns)

### [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)

In this example, the goal is to sum the last n columns in a set of data, where n is a variable that can be changed at any time. In the latest version of Excel, the easiest way to solve this problem is with the TAKE function . In older versions of Excel you can use the OFFSET function , as explained...

[![Excel formula: Look up entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20column.png "Excel formula: Look up entire column")](https://exceljet.net/formulas/look-up-entire-column)

### [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)

In this example, the goal is to look up and retrieve an entire column of values in a set of data. For example, when a value like "Q3" is entered into cell H4, all values in the range E5:E16 should be returned. For convenience and readability, quarter (C4:F4) and data (C5:F16) are named ranges ...

[![Excel formula: Look up entire row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20row.png "Excel formula: Look up entire row")](https://exceljet.net/formulas/look-up-entire-row)

### [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)

In this example, the goal is to look up and retrieve an entire row of values in a set of data. For example, when a value like "Neptune" is entered into cell H5, all values in the range C11:F11 should be returned. For convenience and readability, project (B5:B16) and data (C5:F16) are named ranges...

[![Excel formula: Sum entire row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20entire%20row.png "Excel formula: Sum entire row")](https://exceljet.net/formulas/sum-entire-row)

### [Sum entire row](https://exceljet.net/formulas/sum-entire-row)

In this example, the goal is to return the sum for an entire row in an Excel worksheet. One way to do this is to use a full row reference. Full row references Excel supports full row references like this: =SUM(1:1) // sum all of row 1 =SUM(3:3) // sum all of row 2 =SUM(4:5) // sum all of rows 4 and...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)
    
*   [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)
    
*   [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)
    
*   [Sum entire row](https://exceljet.net/formulas/sum-entire-row)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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