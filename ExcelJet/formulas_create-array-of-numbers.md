# Create array of numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/create-array-of-numbers

---

[Skip to main content](https://exceljet.net/formulas/create-array-of-numbers#main-content)

[](https://exceljet.net/formulas/create-array-of-numbers#)

*   [Previous](https://exceljet.net/formulas/course-completion-summary-with-criteria)
    
*   [Next](https://exceljet.net/formulas/cube-root-of-number)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Create array of numbers
=======================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[INDIRECT](https://exceljet.net/functions/indirect-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")

Summary
-------

To create an array of numbers like {1;2;3;4;5} you can use a formula based on the [ROW](https://exceljet.net/functions/row-function)
 and [INDIRECT](https://exceljet.net/functions/indirect-function)
 functions. This technique is most often used in [array formulas](https://exceljet.net/glossary/array-formula)
 that need a numeric [array](https://exceljet.net/glossary/array)
 for processing of some kind. In the example shown, the formula in D5 is:

    {=ROW(INDIRECT(B5&":"&C5))}
    

which returns an array like {1;2;3;4;5}.

_Note: when entered in a single cell, Excel will display only the first item in the array. [Use F9 in the formula bar](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
 to see the actual array result. Normally, you will use this formula inside a larger array formula, entered with control + shift + enter._

Generic formula
---------------

    {=ROW(INDIRECT(start&":"&end))}

Explanation 
------------

_Note: In [Excel 365](https://exceljet.net/glossary/excel-365)
, the new [SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
 is a better and easier way to create an array of numbers. The method explained below will work in previous versions._

The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string into INDIRECT like this:

    =ROW(INDIRECT("1:10"))
    

The INDIRECT function interprets this text to mean the range 1:10 (10 rows) and the ROW function returns the row number for each row in that range inside an array.

The example shown uses a more generic version of the formula that picks up the start and end numbers from B5 and C5 respectively, so the solution looks like this:

    =ROW(INDIRECT(B5&":"&C5))
    =ROW(INDIRECT(1&":"&5))
    =ROW(INDIRECT("1:5"))
    =ROW(1:5)
    ={1;2;3;4;5}
    

The reason INDIRECT is used in the formula is to guard against worksheet changes. Without INDIRECT, inserting or deleting rows can change the range reference, for example:

    =ROW(1:5)
    

will change to:

    =ROW(1:4)
    

If row 1 is deleted. Because INDIRECT works with a reference constructed with text, it isn't affected by changes on the worksheet.

### Relative row numbers in a range

If you need an array that consists of the relative row numbers of a range, you can use a formula like this:

    =ROW(range)-ROW(range.firstcell)+1
    

See [this page](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
 for a full explanation.

### Negative values

The ROW function won't handle negative numbers, so you can't mix negative numbers in for **start** and **end**. However, you can apply math operations to the array created by ROW. For example, the following formula will create this array: {-5;-4;-3;-2;-1}

    =ROW(INDIRECT(1&":"&5))-6
    

### Numbers in reverse order, n to 1

To create an array of positive numbers in descending order, from n to 1, you can use a formula like this:

    =ABS(ROW(INDIRECT("1:"&n))-(n+1))
    

Related formulas
----------------

[![Excel formula: Get relative row numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20row%20numbers%20in%20range.png "Excel formula: Get relative row numbers in range")](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

### [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)

The first ROW function generates an array of 7 numbers like this: {5;6;7;8;9;10;11} The second ROW function generates an array with just one item like this: {5} which is then subtracted from the first array to yield: {0;1;2;3;4;5;6} Finally, 1 is added to get: {1;2;3;4;5;6;7} Generic version with...

[![Excel formula: Get relative column numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20column%20numbers%20in%20range.png "Excel formula: Get relative column numbers in range")](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

### [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

The first COLUMN function generates an array of 7 numbers like this: {2,3,4,5,6,7,8} The second COLUMN function generates an array with just one item like this: {2} which is then subtracted from the first array to yield: {0,1,2,3,4,5,6} Finally, 1 is added to get: {1,2,3,4,5,6,7} With a named range...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Return array with INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return%20array%20with%20INDEX%20function.png "Excel formula: Return array with INDEX function")](https://exceljet.net/formulas/return-array-with-index-function)

### [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)

It is surprisingly tricky to get INDEX to return more than one value to another function. To illustrate, the following formula can be used to return the first three items in the named range "data", when entered as a multi-cell array formula. {=INDEX(data,{1,2,3})} The results can be seen in the...

Related functions
-----------------

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

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

### Formulas

*   [Get relative row numbers in range](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
    
*   [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)
    

### Functions

*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
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