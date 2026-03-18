# First row number in range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/first-row-number-in-range

---

[Skip to main content](https://exceljet.net/formulas/first-row-number-in-range#main-content)

[](https://exceljet.net/formulas/first-row-number-in-range#)

*   [Previous](https://exceljet.net/formulas/first-match-between-two-ranges)
    
*   [Next](https://exceljet.net/formulas/get-address-of-named-range-or-table)
    

[Range](https://exceljet.net/formulas#Range)

First row number in range
=========================

by Dave Bruns · Updated 25 Nov 2015

Related functions 
------------------

[ROW](https://exceljet.net/functions/row-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: First row number in range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/first%20row%20in%20range.png "Excel formula: First row number in range")

Summary
-------

You can get the first row (i.e. the starting row number) in a range with a formula based on the ROW function.

In the example shown, the formula in cell F5 is:

    =MIN(ROW(data))
    

where data is a named range for B5:D10

Generic formula
---------------

    =MIN(ROW(rng))

Explanation 
------------

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range that contains multiple rows, the ROW function will return an array that contains all row numbers for the range. In the example shown the array looks like this:

{5;6;7;8;9;10}

If you want only the first row number, you can use the MIN function to extract just the first row number, which will be the lowest number in the array.

### Simple version

Entered in a single cell, the ROW function will display only the first row number, even though it returns an array. This means, in practice, you can often just use the ROW function alone:

    =ROW(rng)
    

However, inside formulas more complex formulas, it's sometimes necessary to make sure you are dealing with only one item, and not an array. In that case, you'll want to use MIN to pull out just the first item.

### Index version

Since ROW (range) actually returns an array of every row number in the range, you can also use INDEX to fetch the first item:

    =ROW(INDEX(data,1,1))
    

Not tested, but this may be slightly faster than the MIN(ROW) formula in very large ranges.

Related formulas
----------------

[![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")](https://exceljet.net/formulas/last-row-number-in-range)

### [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range: {5;6;7;8;9;10} To get the first row number in a range, we use the MIN...

[![Excel formula: First column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20column%20in%20range.png "Excel formula: First column number in range")](https://exceljet.net/formulas/first-column-number-in-range)

### [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. In the example shown the array looks like this...

[![Excel formula: Last column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20column%20in%20range.png "Excel formula: Last column number in range")](https://exceljet.net/formulas/last-column-number-in-range)

### [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. If you want only the first column number, you...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

Related functions
-----------------

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

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

*   [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)
    
*   [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)
    
*   [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    

### Functions

*   [ROW Function](https://exceljet.net/functions/row-function)
    
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