# Add row numbers and skip blanks - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-row-numbers-and-skip-blanks

---

[Skip to main content](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks#main-content)

[](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks#)

*   [Previous](https://exceljet.net/formulas/randomly-assign-people-to-groups)
    
*   [Next](https://exceljet.net/formulas/address-of-first-cell-in-range)
    

[Range](https://exceljet.net/formulas#Range)

Add row numbers and skip blanks
===============================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[COUNTA](https://exceljet.net/functions/counta-function)

[IF](https://exceljet.net/functions/if-function)

[ISBLANK](https://exceljet.net/functions/isblank-function)

![Excel formula: Add row numbers and skip blanks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add%20row%20numbers%20and%20skip%20blanks.png "Excel formula: Add row numbers and skip blanks")

Summary
-------

To add sequential row numbers to a list of data, skipping cells that are blank, you can use a formula based on [COUNTA](https://exceljet.net/functions/counta-function)
, [ISBLANK](https://exceljet.net/functions/isblank-function)
, and [IF](https://exceljet.net/functions/if-function)
. In the example shown, the formula in B5 is:

    =IF(ISBLANK(C5),"",COUNTA($C$5:C5))
    

As the formula is copied down the column, rows where there is a value are numbered and empty rows are skipped.

Generic formula
---------------

    =IF(ISBLANK(A1),"",COUNTA($A$1:A1))

Explanation 
------------

In the example shown, the goal is to add row numbers in column B only when there is a value in column C. The formula in B5 is:

    =IF(ISBLANK(C5),"",COUNTA($C$5:C5))
    

The [IF function](https://exceljet.net/functions/if-function)
 first checks if cell C5 has a value with the [ISBLANK function](https://exceljet.net/functions/isblank-function)
:

    ISBLANK(C5) // TRUE if empty, FALSE if not
    

If C5 is empty, ISBLANK returns TRUE and the IF function returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("") as the result. If C5 is not empty, ISBLANK returns FALSE and the IF function returns [COUNTA function](https://exceljet.net/functions/counta-function)
 with an [expanding reference](https://exceljet.net/glossary/expanding-reference)
 like this:

    COUNTA($C$5:C5) // expanding range
    

As the formula is copied down, the range expands, and COUNTA returns the  "current" count of all non-blank cells in the range as defined in each row. COUNTA will count both numbers and text.

### Alternatives

Both of the formulas below perform the same task, but with different syntax:

    =IF(C5="","",COUNTA($C$5:C5))
    

Same logic as above, but using ="" instead of ISBLANK.

    =IF(C5<>"",COUNTA($C$5:C5),"")
    

Logic reversed. If C5 is not blank, return the count, otherwise return an empty string. This version uses the not equal to [operator](https://exceljet.net/glossary/logical-operators)
 (<>).

Related formulas
----------------

[![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")](https://exceljet.net/formulas/automatic-row-numbers)

### [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a...

[![Excel formula: Automatic row numbers in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic%20row%20number%20in%20excel%20table.png "Excel formula: Automatic row numbers in Table")](https://exceljet.net/formulas/automatic-row-numbers-in-table)

### [Automatic row numbers in Table](https://exceljet.net/formulas/automatic-row-numbers-in-table)

When no argument is provided, the ROW function returns the "current row", that is, the row number of the cell that contains it. When a cell reference is provided, ROW returns the row number of the cell. When a range is provided, ROW returns the first row number in the range. In the example shown,...

[![Excel formula: Last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last-n-rows.png "Excel formula: Last n rows")](https://exceljet.net/formulas/last-n-rows)

### [Last n rows](https://exceljet.net/formulas/last-n-rows)

When you are working with a large table that extends beyond the visible area of a worksheet, you might want to see the most recent data in the table without scrolling to the bottom of the table. Examples of this kind of data include things like: Recent deposits or expenses Recent transactions...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: First row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20row%20in%20range.png "Excel formula: First row number in range")](https://exceljet.net/formulas/first-row-number-in-range)

### [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range that contains multiple rows, the ROW function will return an array that contains all row numbers for the range. In the example shown the array looks like this: {5;6;7;8;9;10}...

[![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")](https://exceljet.net/formulas/last-row-number-in-range)

### [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range: {5;6;7;8;9;10} To get the first row number in a range, we use the MIN...

[![Excel formula: First column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20column%20in%20range.png "Excel formula: First column number in range")](https://exceljet.net/formulas/first-column-number-in-range)

### [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. In the example shown the array looks like this...

[![Excel formula: Basic outline numbering](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20outline%20numbering.png "Excel formula: Basic outline numbering")](https://exceljet.net/formulas/basic-outline-numbering)

### [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)

At the core, this formula builds a level 1 and level 2 number and concatenates the two numbers together with a period (".") as a separator. The result is a value like "1.1". The "level 1" number is generated with COUNTA like this: =COUNTA($B$5:B5) Note the range is an expanding reference , so it...

Related functions
-----------------

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

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

*   [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)
    
*   [Automatic row numbers in Table](https://exceljet.net/formulas/automatic-row-numbers-in-table)
    
*   [Last n rows](https://exceljet.net/formulas/last-n-rows)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)
    
*   [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)
    
*   [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)
    
*   [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)
    

### Functions

*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    

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