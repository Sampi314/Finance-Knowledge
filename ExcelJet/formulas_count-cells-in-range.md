# Count cells in range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-in-range

---

[Skip to main content](https://exceljet.net/formulas/count-cells-in-range#main-content)

[](https://exceljet.net/formulas/count-cells-in-range#)

*   [Previous](https://exceljet.net/formulas/combine-ranges-with-choose)
    
*   [Next](https://exceljet.net/formulas/count-visible-columns)
    

[Range](https://exceljet.net/formulas#Range)

Count cells in range
====================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[ROWS](https://exceljet.net/functions/rows-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

[COUNTA](https://exceljet.net/functions/counta-function)

![Excel formula: Count cells in range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count_cells_in_range.png "Excel formula: Count cells in range")

Summary
-------

To count the total number of cells in a range, you can use a formula based on the [ROWS](https://exceljet.net/functions/rows-function)
 and [COLUMNS](https://exceljet.net/functions/columns-function)
 functions. In the example shown, the formula in cell J5 is:

    =ROWS(B4:H16)*COLUMNS(B4:H16)
    

The result is 91, the total number of cells in the range B4:H16.

Generic formula
---------------

    =ROWS(range)*COLUMNS(range)

Explanation 
------------

The goal is to count the number of cells in a given range, regardless of whether the cells are empty or not. Although Excel has several functions designed to count cells based on their contents, there is no built-in function for counting the total number of cells in a range. The classic solution is to use a formula based on the ROWS function and the COLUMNS function. It is also possible to force the COUNTA function to count all cells, empty or not. Both approaches are explained below.

### ROWS + COLUMNS

One way to count all cells in a range is to use the [ROWS function](https://exceljet.net/functions/rows-function)
 with the [COLUMNS function](https://exceljet.net/functions/columns-function)
 in a formula like this:

    =ROWS(range)*COLUMNS(range)

This is the approach used in the worksheet shown, where the formula in cell J5 is:

    =ROWS(B4:H16)*COLUMNS(B4:H16)

The ROWS function returns the _count of rows_ in a range. Since there are 12 rows in the range B4:H16, ROWS returns 12. In the same way, the COLUMNS function returns the _count of columns_ in a range, which is 7 in this case. The formula is evaluated by Excel like this:

    =ROWS(B4:H16)*COLUMNS(B4:H16)
    =12*7
    =91
    

### Count all cells in a worksheet

The ROWS and COLUMNS functions can work with a rectangular range of any size. For example, the formula below uses the ROWS function to count all rows in column A, and the COLUMNS function to count all columns in row 1:

    =ROWS(A:A)*COLUMNS(1:1) // count all cells in worksheet
    

ROWS returns a count of 1,048,576, and COLUMNS returns a count of 16,384, so the final result is 17,179,869,184. This is the total number of cells in an Excel worksheet. The formula below uses the range 1:1048576 to achieve the same result:

    =ROWS(1:1048576)*COLUMNS(1:1048576) // returns 17179869184
     

_Tip: Excel will enter the range 1:1048576 for you if you click the upper-left corner of the spreadsheet while entering a formula._

### COUNTA alternative

If you find the ROWS + COLUMNS formula cumbersome, you can try the formula below, which is based on the COUNTA function:

    =COUNTA(range+0)

This formula is a bit of a hack. The [COUNTA function](https://exceljet.net/functions/counta-function)
 will count cells that contain numbers, text, or errors. It will not count empty cells. If we use COUNTA with the range itself, we get a result of 82, since the range contains 9 empty cells:

    =COUNTA(B4:H16) // returns 82

However, when we add zero:

    =COUNTA(B4:H16+0)

The match operation will cause Excel to evaluate the empty cells as zeros, and it will return a combination of numbers and errors. In this example, the [array](https://exceljet.net/glossary/array)
 created inside COUNTA looks like this:

    =COUNTA({0,18,46,54,#VALUE!,23,13;10,#VALUE!,76,#VALUE!,64,14,64;44,34,0,39,30,0,#VALUE!;81,90,#VALUE!,58,#VALUE!,#VALUE!,75;32,79,56,14,1,9,70;79,#VALUE!,8,0,92,64,#VALUE!;#VALUE!,56,89,18,42,43,44;48,38,#VALUE!,68,#VALUE!,0,91;32,0,59,#VALUE!,1,#VALUE!,#VALUE!;41,#VALUE!,39,55,72,0,57;61,68,#VALUE!,#VALUE!,18,87,#VALUE!;80,65,48,96,5,36,0;11,92,#VALUE!,36,#VALUE!,0,65})

Notice that empty cells are now zero (0), and errors represent cells that contain text. Because all cells represented by the array have a value, COUNTA will now return the same result as the original formula above, 91.

_Caution: this formula will work fine on fine on typical size ranges. However, the performance will suffer on very large ranges, and you might notice a delay when the formula is entered or recalculated._

Related formulas
----------------

[![Excel formula: Total rows in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20rows%20in%20range.png "Excel formula: Total rows in range")](https://exceljet.net/formulas/total-rows-in-range)

### [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)

The ROWS function is fully automatic. When you provide a range to ROWS, it will return a count of all rows in the range. In the example, the formula in F5 returns 6, because there are 6 rows in the range B5:C10: =ROWS(B5:C10) // count rows ROWS counts the number of rows in any supplied range and...

[![Excel formula: Total columns in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/total%20columns%20in%20range.png "Excel formula: Total columns in range")](https://exceljet.net/formulas/total-columns-in-range)

### [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)

The COLUMNS function is fully automatic. When you provide a range to COLUMNS, it will return a count of all columns in the range. In the example, the formula in F6 returns 2, because there are 2 columns in the range B5:C10: =COLUMNS(B5:C10) // count columns COLUMNS counts the number of columns in...

Related functions
-----------------

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Total rows in range](https://exceljet.net/formulas/total-rows-in-range)
    
*   [Total columns in range](https://exceljet.net/formulas/total-columns-in-range)
    

### Functions

*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

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