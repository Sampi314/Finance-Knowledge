# Excel COUNTBLANK function | Exceljet

**Source:** https://exceljet.net/functions/countblank-function

---

[Skip to main content](https://exceljet.net/functions/countblank-function#main-content)

[](https://exceljet.net/functions/countblank-function#)

*   [Previous](https://exceljet.net/functions/counta-function)
    
*   [Next](https://exceljet.net/functions/countif-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

COUNTBLANK Function
===================

by Dave Bruns · Updated 29 Nov 2022

Related functions 
------------------

[COUNTA](https://exceljet.net/functions/counta-function)

[COUNT](https://exceljet.net/functions/count-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

![Excel COUNTBLANK function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20countblank%20function.png "Excel COUNTBLANK function")

Summary
-------

The Excel COUNTBLANK function returns a count of empty cells in a [range](https://exceljet.net/glossary/range)
. Cells that contain text, numbers, errors, spaces, etc. are _not_ counted. Formulas that return empty strings ("") _are_ counted as blank.

Purpose 
--------

Count cells that are blank

Return value 
-------------

A number representing blank cells

Syntax
------

    =COUNTBLANK(range)

*   _range_ - The range in which to count blank cells.

Using the COUNTBLANK function 
------------------------------

The COUNTBLANK function returns a count of empty cells in a range. Cells that contain text, numbers, errors, spaces, etc. are _not_ counted. Formulas that return an empty string ("") _are_ counted as blank. COUNTBLANK takes just one argument, range, which must be a cell [range](https://exceljet.net/glossary/range)
.

### Examples

In the example shown, the formula in cell E6 is:

    =COUNTBLANK(B5:B15) // returns 3
    

COUNTBLANK returns 3 since there are 3 blank cells in the range. Note that cell B12 is not included because it contains a space character (" "). Cell B13 contains a formula that returns an empty string:

    ="" // formula in B13
    

COUNTBLANK considers B13 blank and includes it in the count.

### Formulas that return empty strings

The [IF function](https://exceljet.net/functions/if-function)
 is often used to return empty strings. For example, if A1 contains 21, this formula in B1 will return an empty string:

    =IF(A1>30,"Overdue","")

The idea is that that cell B1 should be empty unless the value in A1 is greater than 30. The COUNTBLANK function will indeed count B1 as empty when the value in A1 is less than or equal to 30. However it's worth noting that [COUNTA](https://exceljet.net/functions/counta-function)
 and [COUNTIFS](https://exceljet.net/functions/countifs-function)
 will count B1 as _not empty_ in the same case. In other words they will see the empty string ("") returned by IF as _not blank_.

### Invisible characters

Some cells look empty, but actually contain invisible characters. To check which cells are blank use Go To > Special > Blanks:

1.  Select a range
2.  Open Go To dialog (Control + G)
3.  Press "Special"
4.  Select "Blanks"

### Functions for counting

*   To count numbers only, use the [COUNT function](https://exceljet.net/functions/count-function)
    .
*   To count numbers and text, use the [COUNTA function](https://exceljet.net/functions/counta-function)
    .
*   To count with one condition, use the [COUNTIF function](https://exceljet.net/functions/countif-function)
    
*   To count with multiple conditions, use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
    .
*   To count empty cells, use the [COUNTBLANK function](https://exceljet.net/functions/countblank-function)
    .

### Notes

*   Cells that contain text, numbers, errors, etc. _are not_ counted.
*   Cells with formulas that return an [empty string](https://exceljet.net/glossary/empty-string)
     ("") _are_ counted.
*   Cells that contain only a single quote (') _are_ counted.
*   Cells that contain zero _are not_ counted.

COUNTBLANK function examples
----------------------------

[![Excel formula: Return blank if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return_blank_if.png "Excel formula: Return blank if")](https://exceljet.net/formulas/return-blank-if)

### [Return blank if](https://exceljet.net/formulas/return-blank-if)

The goal is to display a blank cell based on a specific condition. In the worksheet shown, we want to return the value from column C, but only when the value in column B is "A". If the value in column B is anything else, we want to display nothing. The easiest way to solve this problem is with the...

[![Excel formula: Count cells that are not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20are%20not%20blank.png "Excel formula: Count cells that are not blank")](https://exceljet.net/formulas/count-cells-that-are-not-blank)

### [Count cells that are not blank](https://exceljet.net/formulas/count-cells-that-are-not-blank)

In this example, the goal is to count cells in a range that are not blank (i.e. not empty). There are several ways to go about this task, depending on your needs. The article below explains different approaches. COUNTA function While the COUNT function only counts numbers, the COUNTA function...

[![Excel formula: Count cells that are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20are%20blank_0.png "Excel formula: Count cells that are blank")](https://exceljet.net/formulas/count-cells-that-are-blank)

### [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)

In this example, the goal is to count cells in a range that are blank. Counting blank cells in Excel can be tricky because cells can look blank even when they are not actually empty. The article below explains three different approaches. COUNTBLANK function The simplest way to count empty cells in...

[![Excel formula: Highlight rows with blank cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20rows%20with%20blank%20cells.png "Excel formula: Highlight rows with blank cells")](https://exceljet.net/formulas/highlight-rows-with-blank-cells)

### [Highlight rows with blank cells](https://exceljet.net/formulas/highlight-rows-with-blank-cells)

Conditional formatting is applied to all cells in the active selection at the time a rule is created. In this case, the column references are locked to prevent columns from changing as the formula is evaluated, but the row references are relative so that row numbers are free to change. The result...

[![Excel formula: Only calculate if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20not%20blank%20then%20calculate2.png "Excel formula: Only calculate if not blank")](https://exceljet.net/formulas/only-calculate-if-not-blank)

### [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)

The goal is to verify the input of all required values before calculating a result. In the worksheet shown, the SUM function is used as an example only. You can use the same approach with any formula to prevent calculation until all required values are available. The logic can be adjusted in many...

COUNTBLANK function videos
--------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

Related functions
-----------------

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)
    
*   [Highlight rows with blank cells](https://exceljet.net/formulas/highlight-rows-with-blank-cells)
    
*   [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)
    
*   [Return blank if](https://exceljet.net/formulas/return-blank-if)
    
*   [Count cells that are not blank](https://exceljet.net/formulas/count-cells-that-are-not-blank)
    

### Videos

*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    

### Functions

*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    

### Links

*   [Microsoft COUNTBLANK function documentation](https://support.office.com/en-us/article/countblank-function-6a92d772-675c-4bee-b346-24af6bd3ac22)
    

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