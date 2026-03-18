# Sum entire row - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-entire-row

---

[Skip to main content](https://exceljet.net/formulas/sum-entire-row#main-content)

[](https://exceljet.net/formulas/sum-entire-row#)

*   [Previous](https://exceljet.net/formulas/sum-entire-column)
    
*   [Next](https://exceljet.net/formulas/sum-every-n-rows)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum entire row
==============

by Dave Bruns · Updated 10 Sep 2022

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Sum entire row](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20entire%20row.png "Excel formula: Sum entire row")

Summary
-------

To sum an _entire_ row without providing a specific range, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 with a [full row reference](https://exceljet.net/glossary/full-row-reference)
. In the example shown, the formula in C11, copied down, is:

    =SUM(5:5)
    

The result is the sum of all numbers in row 5. As new data is added to the table, the formula will continue to return a correct total.

Generic formula
---------------

    =SUM(1:1)

Explanation 
------------

In this example, the goal is to return the sum for an entire row in an Excel worksheet. One way to do this is to use a full row reference.

### Full row references

Excel supports full row references like this:

    =SUM(1:1) // sum all of row 1
    =SUM(3:3) // sum all of row 2
    =SUM(4:5) // sum all of rows 4 and 5
    

You can see how this works yourself by typing 1:1 or 3:3 into the [name box](https://exceljet.net/glossary/name-box)
 (left of the [formula bar](https://exceljet.net/glossary/formula-bar)
) and hitting return. You will see Excel select the entire row.

### Example

To solve the problem in the example worksheet, we can use a full row reference to row 5 with the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(5:5)
    

The result is the sum of all numeric values in row 5. As the formula is copied down, we get a sum for row 6 and row 7 as well:

    =SUM(5:5) // sum red
    =SUM(6:6) // sum blue
    =SUM(7:7) // sum green
    

As new entries for "Red" are added to the table in rows 5, 6, and 7, the formula will automatically include these new amounts.

### Advantages and risks

The main advantage to full row references is simplicity. Simple and very compact, a full row reference will automatically include _all data_ in a row, even when data is added or removed. However, full row references come with certain risks. One risk is that you may accidentally include extra data in a calculation. For example, if you use =SUM(5:5) to sum numbers in row 5, you are targeting over 16,000 cells to the right. If row 5 includes extra dates somewhere far to the right, the [numeric values](https://exceljet.net/glossary/excel-date)
 of these dates will be included, and SUM will return an incorrect result. 

Related formulas
----------------

[![Excel formula: Look up entire row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20row.png "Excel formula: Look up entire row")](https://exceljet.net/formulas/look-up-entire-row)

### [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)

In this example, the goal is to look up and retrieve an entire row of values in a set of data. For example, when a value like "Neptune" is entered into cell H5, all values in the range C11:F11 should be returned. For convenience and readability, project (B5:B16) and data (C5:F16) are named ranges...

[![Excel formula: Sum entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20entire%20column.png "Excel formula: Sum entire column")](https://exceljet.net/formulas/sum-entire-column)

### [Sum entire column](https://exceljet.net/formulas/sum-entire-column)

In this example, the goal is to return the total for an entire column in an Excel worksheet. One way to do this is to use a full column reference. Full column references Excel supports " full column " like this: =SUM(A:A) // sum all of column A =SUM(C:C) // sum all of column C =SUM(A:C) // sum all...

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

*   [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)
    
*   [Sum entire column](https://exceljet.net/formulas/sum-entire-column)
    

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