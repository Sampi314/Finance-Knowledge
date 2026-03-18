# Get relative row numbers in range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-relative-row-numbers-in-range

---

[Skip to main content](https://exceljet.net/formulas/get-relative-row-numbers-in-range#main-content)

[](https://exceljet.net/formulas/get-relative-row-numbers-in-range#)

*   [Previous](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
    
*   [Next](https://exceljet.net/formulas/last-column-number-in-range)
    

[Range](https://exceljet.net/formulas#Range)

Get relative row numbers in range
=================================

by Dave Bruns · Updated 30 Oct 2023

Related functions 
------------------

[ROW](https://exceljet.net/functions/row-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[ROWS](https://exceljet.net/functions/rows-function)

![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")

Summary
-------

To get a full set of relative row numbers in a range, you can use an array formula based on the ROW function. In the example shown, the formula in B5:B11 is:

    {=ROW(B5:B11)-ROW(B5)+1}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with Control + Shift + Enter. If you're entering this on the worksheet (and not inside another formula), make a selection that includes more than one row, enter the formula, and confirm with Control + Shift + Enter._

This formula will continue to generate relative numbers even when the range is moved. However, it's not a good choice if rows need to be sorted, deleted, or added because the array formula will prevent changes. The [formula options explained here](https://exceljet.net/formulas/automatic-row-numbers)
 will work better.

Generic formula
---------------

    {=ROW(range)-ROW(range.firstcell)+1}

Explanation 
------------

The first ROW function generates an array of 7 numbers like this:

    {5;6;7;8;9;10;11}
    

The second ROW function generates an array with just one item like this:

    {5}
    

which is then subtracted from the first array to yield:

    {0;1;2;3;4;5;6}
    

Finally, 1 is added to get:

    {1;2;3;4;5;6;7}
    

### Generic version with named range

With a [named range](https://exceljet.net/glossary/named-range)
, you can create a more generic version of the formula using the MIN function or the INDEX function. For example, with the named range "list", you can use MIN like this:

    {ROW(list)-MIN(ROW(list))+1}
    

With INDEX, we fetch the first reference in the named range, and using ROW on that:

    {=ROW(list)-ROW(INDEX(list,1,1))+1}
    

You'll often see "relative row" formulas like this inside complex array formulas that need row numbers to calculate a result.

### With SEQUENCE

With the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 the formula to return relative row numbers for a range is simple:

    =SEQUENCE(ROWS(range))
    

The [ROWS function](https://exceljet.net/functions/rows-function)
 provides the count of rows, which is returned to the SEQUENCE function. SEQUENCE then builds an array of numbers, starting with the number 1.  So, following the original example above, the formula below returns the same result:

    =SEQUENCE(ROWS(B5:B11)) // returns {1;2;3;4;5;6;7}
    

_Note: the SEQUENCE formula is a new [dynamic array function](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 available only in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Related formulas
----------------

[![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")](https://exceljet.net/formulas/automatic-row-numbers)

### [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a...

[![Excel formula: Last row number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20row%20in%20range.png "Excel formula: Last row number in range")](https://exceljet.net/formulas/last-row-number-in-range)

### [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)

When given a single cell reference, the ROW function returns the row number for that reference. However, when given a range with multiple rows, the ROW function will return an array that contains all row numbers for the range: {5;6;7;8;9;10} To get the first row number in a range, we use the MIN...

[![Excel formula: First column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20column%20in%20range.png "Excel formula: First column number in range")](https://exceljet.net/formulas/first-column-number-in-range)

### [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. In the example shown the array looks like this...

[![Excel formula: Last column number in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20column%20in%20range.png "Excel formula: Last column number in range")](https://exceljet.net/formulas/last-column-number-in-range)

### [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)

When given a single cell reference, the COLUMN function returns the column number for that reference. However, when given a range that contains multiple columns, the COLUMN function will return an array that contains all column numbers for the range. If you want only the first column number, you...

[![Excel formula: Get relative column numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20column%20numbers%20in%20range.png "Excel formula: Get relative column numbers in range")](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

### [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

The first COLUMN function generates an array of 7 numbers like this: {2,3,4,5,6,7,8} The second COLUMN function generates an array with just one item like this: {2} which is then subtracted from the first array to yield: {0,1,2,3,4,5,6} Finally, 1 is added to get: {1,2,3,4,5,6,7} With a named range...

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

[![Excel formula: INDEX and MATCH all partial matches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_all_partial_matches.png "Excel formula: INDEX and MATCH all partial matches")](https://exceljet.net/formulas/index-and-match-all-partial-matches)

### [INDEX and MATCH all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)

Note: in the current version of Excel, the FILTER function is a better way to solve this problem. The INDEX and MATCH formula explained here is meant for legacy versions of Excel that do not provide the FILTER function. The core of this formula is the INDEX function, with AGGREGATE used to figure...

Related functions
-----------------

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

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
    
*   [Last row number in range](https://exceljet.net/formulas/last-row-number-in-range)
    
*   [First column number in range](https://exceljet.net/formulas/first-column-number-in-range)
    
*   [Last column number in range](https://exceljet.net/formulas/last-column-number-in-range)
    
*   [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
    
*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)
    
*   [INDEX and MATCH all partial matches](https://exceljet.net/formulas/index-and-match-all-partial-matches)
    

### Functions

*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

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