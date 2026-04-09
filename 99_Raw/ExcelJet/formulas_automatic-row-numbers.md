# Automatic row numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/automatic-row-numbers

---

[Skip to main content](https://exceljet.net/formulas/automatic-row-numbers#main-content)

[](https://exceljet.net/formulas/automatic-row-numbers#)

*   [Previous](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)
    
*   [Next](https://exceljet.net/formulas/combine-ranges-with-choose)
    

[Range](https://exceljet.net/formulas#Range)

Automatic row numbers
=====================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[ROW](https://exceljet.net/functions/row-function)

[INDEX](https://exceljet.net/functions/index-function)

[COUNTA](https://exceljet.net/functions/counta-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7748/download?token=Xoj2OvYn)
 (25.86 KB)

![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")

Summary
-------

To add automatic row numbers to a list with a formula, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. In the example shown, the formula in B5 is:

    =SEQUENCE(COUNTA(C:C)-1)
    

The result is a dynamic list of row numbers that match the data in column B. If new items are added to the list, the row numbers automatically increase. If items are removed, the row numbers decrease.

Generic formula
---------------

    =SEQUENCE(COUNTA(A:A)-offset)

Explanation 
------------

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a tricky problem in Excel because there is no built-in function to create and maintain row numbers. The article below explains several options. The best option for you will depend on what Excel version you use, and on your particular requirements.

### Row numbers with the Fill Handle

The examples below use formulas to automatically generate row numbers. However, if you only need to enter row numbers on a one-time basis, you can use the [fill handle](https://exceljet.net/glossary/fill-handle)
 to automate most of the process. The trick is to enter the first two numbers to help Excel understand what you want. Then select the two cells, and double click the fill handle to send it down, or simply drag the fill handle to the desired location. The animation below shows the basic process:

![Automatic row numbers with the fill handle](https://exceljet.net/sites/default/files/images/formulas/inline/automatic_row_numbers_with_fill_handle.gif "Automatic row numbers with the fill handle")

The advantage of this approach is you don't need to use any formulas at all. The disadvantage of this approach is that you will need to repeat the process if you add or remove items from the list, or if you otherwise want to generate a new set of row numbers.

### Automatic row numbers with SEQUENCE

In the [current version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the easiest way to create automatic row numbers is to use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
.  The SEQUENCE function generates a list of sequential numbers that [spill](https://exceljet.net/glossary/spill)
 directly on the worksheet. For example, to create numbers between 1-3 you can use SEQUENCE like this:

    =SEQUENCE(3) // returns {1;2;3}
    

If you change _rows_ to 5, SEQUENCE returns an array with 5 numbers:

    =SEQUENCE(5) // returns {1;2;3;4;5}
    

Video: [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

The output from SEQUENCE is an [array](https://exceljet.net/glossary/array)
 of values that will [spill](https://exceljet.net/glossary/spill)
 into multiple cells. The challenge in this example is how to calculate the number of rows needed for the list or table. We do this with the [COUNTA function](https://exceljet.net/functions/counta-function)
 and a [full column reference](https://exceljet.net/glossary/full-column-reference)
 to column C like this:

    =COUNTA(C:C) // returns 12 

COUNTA returns 12, because there are 11 items in the list, plus the column header in cell C4. Because we are not assigning a row number to the header row, we need to subtract 1 to get a correct count:

    =COUNTA(C:C)-1 // returns 11

Putting it all together, we have this formula in cell B5:

    =SEQUENCE(COUNTA(C:C)-1)
    

Working from the inside out, COUNTA returns 12, from which 1 is subtracted, leaving 11:

    =SEQUENCE(11)
    

SEQUENCE then returns an [array](https://exceljet.net/glossary/array)
 that contains 11 numbers as a final result:

    ={1;2;3;4;5;6;7;8;9;10;11}
    

This array lands in cell B5 and [spills](https://exceljet.net/glossary/spill)
 into the range B5:B15. If the number of items in column C changes, COUNTA returns a new count, and SEQUENCE returns a new array of row numbers. Note that if there are other cells in column C that contain content that is not part of the data with row numbers, you have two choices. One option is to subtract a different number from COUNTA. For example, if there are two non-blank cells above the list in column C, you would subtract 2:

    =SEQUENCE(COUNTA(C:C)-2)
    

Another option is to remove the full column range C:C and make the range more specific. For example:

    =SEQUENCE(COUNTA(C5:C100))

Here the idea is that there will never be more than 100 items in the list, so we are only counting non-blank cells in the range C5:C100. This also means we will get a correct count from COUNTA with no need to subtract anything from the result.

### Legacy Excel

In older versions of Excel that do not include the SEQUENCE function, you can use a more manual formula based on the [ROW function](https://exceljet.net/functions/row-function)
. As the name implies, the ROW function returns the row number for a reference:

    =ROW(A1) // returns 1
    =ROW(E3) // returns 3
    

When a reference is _not provided_, ROW returns the row number of the cell the formula lives in. For example, if ROW is entered in cell B5, the result is 5:

    =ROW() // returns 5 in B5
    

This means we can create sequential row numbers beginning with 1 by subtracting an appropriate offset value. For example to start numbering in cell B5, we can subtract 4 like this:

    =ROW()-4 // returns 1 in B5
    

The catch with this formula is that you will need to manually copy it down column B to keep it in sync with the items in the list. This formula will continue to work as long as rows are not added or deleted _above_ the first row of data. If rows are added or deleted above the data, or if you start the list in a different row, the hardcoded offset value 4 will need to be adjusted as needed.

### Row numbers in an Excel Table

If you need to add automatic row numbers to an [Excel Table](https://exceljet.net/articles/excel-tables)
, you can't use the SEQUENCE function, because Excel tables do not yet support [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. However, you can use a special formula based on the [ROW function](https://exceljet.net/functions/row-function)
 like this:

    =ROW()-ROW(Table1[#Headers])

In this formula, the required offset is calculated based on the row number of the table header. In the worksheet shown, the header is in row 4. However, if the table exists at (or is moved to) another location, the formula will continue to work correctly.

![Automatic row numbers in an Excel table](https://exceljet.net/sites/default/files/images/formulas/inline/automatic_row_numbers_in_excel_table_0.png "Automatic row numbers in an Excel table")

[See this article](https://exceljet.net/formulas/automatic-row-numbers-in-table)
 for a detailed explanation.

### Row numbers for a named range

The approach for creating sequential row numbers in a table can be adapted to work with a [named range](https://exceljet.net/glossary/named-range)
 like this:

    =ROW()-ROW(INDEX(data,1,1))+1
    

Here, we are working with a single named range called **data**. To calculate the required offset, we use [INDEX](https://exceljet.net/functions/index-function)
 to get the location of the first cell in the range, then feed that result into the ROW function:

    ROW(INDEX(data,1,1))
    

We pass the named range **data** into INDEX and request the cell at row 1, column 1. In other words, we are asking INDEX for the first (upper left) cell in the range. INDEX returns that cell as an address, and the ROW function returns the row number of that cell, which is used as the offset value explained above. The advantage of this formula is that it is portable. It won't break when the formula is moved, and it will work with any named range.

Related formulas
----------------

[![Excel formula: Add row numbers and skip blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20row%20numbers%20and%20skip%20blanks.png "Excel formula: Add row numbers and skip blanks")](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)

### [Add row numbers and skip blanks](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)

In the example shown, the goal is to add row numbers in column B only when there is a value in column C. The formula in B5 is: =IF(ISBLANK(C5),"",COUNTA($C$5:C5)) The IF function first checks if cell C5 has a value with the ISBLANK function : ISBLANK(C5) // TRUE if empty, FALSE if not If C5 is...

[![Excel formula: Automatic row numbers in Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic%20row%20number%20in%20excel%20table.png "Excel formula: Automatic row numbers in Table")](https://exceljet.net/formulas/automatic-row-numbers-in-table)

### [Automatic row numbers in Table](https://exceljet.net/formulas/automatic-row-numbers-in-table)

When no argument is provided, the ROW function returns the "current row", that is, the row number of the cell that contains it. When a cell reference is provided, ROW returns the row number of the cell. When a range is provided, ROW returns the first row number in the range. In the example shown,...

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: First row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20row%20in%20range.png "Excel formula: First row number in range")](https://exceljet.net/formulas/first-row-number-in-range)

### [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range that contains multiple rows, the ROW function will return an array that contains all row numbers for the range. In the example shown the array looks like this: {5;6;7;8;9;10}...

[![Excel formula: Add row numbers and skip blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20row%20numbers%20and%20skip%20blanks.png "Excel formula: Add row numbers and skip blanks")](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)

### [Add row numbers and skip blanks](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)

In the example shown, the goal is to add row numbers in column B only when there is a value in column C. The formula in B5 is: =IF(ISBLANK(C5),"",COUNTA($C$5:C5)) The IF function first checks if cell C5 has a value with the ISBLANK function : ISBLANK(C5) // TRUE if empty, FALSE if not If C5 is...

[![Excel formula: Basic outline numbering](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20outline%20numbering.png "Excel formula: Basic outline numbering")](https://exceljet.net/formulas/basic-outline-numbering)

### [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)

At the core, this formula builds a level 1 and level 2 number and concatenates the two numbers together with a period (".") as a separator. The result is a value like "1.1". The "level 1" number is generated with COUNTA like this: =COUNTA($B$5:B5) Note the range is an expanding reference , so it...

[![Excel formula: Last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last-n-rows.png "Excel formula: Last n rows")](https://exceljet.net/formulas/last-n-rows)

### [Last n rows](https://exceljet.net/formulas/last-n-rows)

When you are working with a large table that extends beyond the visible area of a worksheet, you might want to see the most recent data in the table without scrolling to the bottom of the table. Examples of this kind of data include things like: Recent deposits or expenses Recent transactions...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_enter_custom_patterns_with_the_fill_handle-thumb.png)](https://exceljet.net/videos/how-to-enter-custom-patterns-with-the-fill-handle-in-excel)

### [How to enter custom patterns with the fill handle in Excel](https://exceljet.net/videos/how-to-enter-custom-patterns-with-the-fill-handle-in-excel)

In this lesson, we'll look at the fill handle's most powerful feature—its ability to recognize and repeat custom patterns that you specify. To use the fill handle to enter data following a custom pattern, start the pattern by entering data in at least two cells. Then, select those cells, and drag...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add row numbers and skip blanks](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)
    
*   [Automatic row numbers in Table](https://exceljet.net/formulas/automatic-row-numbers-in-table)
    
*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [First row number in range](https://exceljet.net/formulas/first-row-number-in-range)
    
*   [Add row numbers and skip blanks](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)
    
*   [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)
    
*   [Last n rows](https://exceljet.net/formulas/last-n-rows)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [How to enter custom patterns with the fill handle in Excel](https://exceljet.net/videos/how-to-enter-custom-patterns-with-the-fill-handle-in-excel)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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