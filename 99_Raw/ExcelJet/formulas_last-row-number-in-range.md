# Last row number in range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-row-number-in-range

---

[Skip to main content](https://exceljet.net/formulas/last-row-number-in-range#main-content)

[](https://exceljet.net/formulas/last-row-number-in-range#)

*   [Previous](https://exceljet.net/formulas/last-row-in-text-data)
    
*   [Next](https://exceljet.net/formulas/multiple-cells-are-equal)
    

[Range](https://exceljet.net/formulas#Range)

Last row number in range
========================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[ROW](https://exceljet.net/functions/row-function)

[ROWS](https://exceljet.net/functions/rows-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")

Summary
-------

To get the last row number in a range, you can use a formula based on the [ROW](https://exceljet.net/functions/row-function)
, [ROWS](https://exceljet.net/functions/rows-function)
, and [MIN](https://exceljet.net/functions/min-function)
 functions. In the example shown, the formula in cell F5 is:

    =MIN(ROW(data))+ROWS(data)-1
    

where "data" is the named range B5:D10

Generic formula
---------------

    =MIN(ROW(rng))+ROWS(rng)-1

Explanation 
------------

When given a single cell reference, the [ROW function](https://exceljet.net/functions/row-function)
 returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range:

    {5;6;7;8;9;10}
    

To get the first row number in a range, we use the [MIN function](https://exceljet.net/functions/min-function)
 like this:

    MIN(ROW(data))
    

which returns the lowest number in the array, 5.

Once we have the first row, we can add the total rows in the range and then subtract 1 to get the last row number. We get total rows in the range with the [ROWS function](https://exceljet.net/functions/rows-function)
, and a final result is determined like this:

    =5+ROWS(data)-1
    =5+6-1
    =10
    

### Index version

Instead of MIN, you can also use INDEX to get the last row number:

    =ROW(INDEX(data,1,1))+ROWS(data)-1
    

This is possibly a bit faster for large ranges since INDEX returns just a single cell to ROW.

### Simple version in older versions of Excel

In Excel 2019 and older, when a formula returns an array result, Excel will display the first item in the array if the formula is entered in a single cell. This means that you will sometimes see a simplified version of the formula like this:

    =ROW(data)+ROWS(data)-1
    

If you only want the last row number in a cell, it works. If you are using this code inside another formula, you may need to ensure you are dealing with only one item and not an array. In that case, you'll want to use the MIN or INDEX version above. In Excel 2021 and later, the formula above will spill a sequence of row numbers _starting with the last row number_ directly on the worksheet. 

Related formulas
----------------

[![Excel formula: Get value of last non-empty cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_value_of_last_non-empty_cell.png "Excel formula: Get value of last non-empty cell")](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

### [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)

In this example, the goal is to get the last value in column B, even when data may contain empty cells. A secondary goal is to get the corresponding value in column C. This is useful for analyzing datasets where the most recent or last entry is significant. In the current version of Excel, a good...

[![Excel formula: First row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20row%20in%20range.png "Excel formula: First row number in range")](https://exceljet.net/formulas/first-row-number-in-range)

### [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range that contains multiple rows, the ROW function will return an array that contains all row numbers for the range. In the example shown the array looks like this: {5;6;7;8;9;10}...

[![Excel formula: Total rows in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20rows%20in%20range.png "Excel formula: Total rows in range")](https://exceljet.net/formulas/total-rows-in-range)

### [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)

The ROWS function is fully automatic. When you provide a range to ROWS, it will return a count of all rows in the range. In the example, the formula in F5 returns 6, because there are 6 rows in the range B5:C10: =ROWS(B5:C10) // count rows ROWS counts the number of rows in any supplied range and...

[![Excel formula: First column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20column%20in%20range.png "Excel formula: First column number in range")](https://exceljet.net/formulas/first-column-number-in-range)

### [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. In the example shown the array looks like this...

[![Excel formula: Last column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20column%20in%20range.png "Excel formula: Last column number in range")](https://exceljet.net/formulas/last-column-number-in-range)

### [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. If you want only the first column number, you...

[![Excel formula: Address of last cell in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/address%20of%20last%20cell%20in%20range.png "Excel formula: Address of last cell in range")](https://exceljet.net/formulas/address-of-last-cell-in-range)

### [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)

The ADDRESS function creates a reference based on a given a row and column number. In this case, we want to get the last row and the last column used by the named range data (B5:D14). To get the last row used, we use the ROW function together with the MAX function like this: MAX(ROW(data)) Because...

Related functions
-----------------

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get value of last non-empty cell](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    
*   [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)
    
*   [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)
    
*   [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)
    
*   [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)
    
*   [Address of last cell in range](https://exceljet.net/formulas/address-of-last-cell-in-range)
    

### Functions

*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

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