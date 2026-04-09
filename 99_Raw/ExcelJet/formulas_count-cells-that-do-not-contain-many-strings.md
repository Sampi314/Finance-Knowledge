# Count cells that do not contain many strings - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings#main-content)

[](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-end-with)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that do not contain many strings
============================================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

[MMULT](https://exceljet.net/functions/mmult-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

![Excel formula: Count cells that do not contain many strings](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20do%20not%20contain%20many%20strings.png "Excel formula: Count cells that do not contain many strings")

Summary
-------

To count cells that do not contain many different strings, you can use a rather complex formula based on the [MMULT function](https://exceljet.net/functions/mmult-function)
. In the example shown, the formula in F5 is:

    {=SUM(1-(MMULT(--(ISNUMBER(SEARCH(TRANSPOSE(exclude),data))),ROW(exclude)^0)>0))}
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B14, and **exclude** is the named range D5:D7. This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
.

_Note: This formula is complex. See [below](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings#reduce_function)
 for a more streamlined version of the formula based on the [REDUCE function](https://exceljet.net/functions/reduce-function)
._

Generic formula
---------------

    {=SUM(1-(MMULT(--(ISNUMBER(SEARCH(TRANSPOSE(exclude),data))),ROW(exclude)^0)>0))}

Explanation 
------------

The goal in this example is to count cells in a range that do not contain a given number of strings. The cells to evaluate are in the [named range](https://exceljet.net/glossary/named-range)
 **data** (B5:B14) and the strings to exclude are listed in the named range **exclude** (D5:D7). If your needs are simple, you can use the COUNTIFS function to solve this problem. In more complicated scenarios, you can use the SUMPRODUCT function in combination with ISNUMBER and SEARCH. In Excel 365, you can use the REDUCE function to streamline the formula somewhat. The formulas for all three approaches are below.

_Note: This formula is complicated by the "contains" requirement. If you just need a formula to count cells that do not \*equal\* many things, you can use a [more straightforward formula based on the MATCH function](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
._

### COUNTIFS function

If you have a limited number of strings to exclude, you can use the COUNTIFS function like this:

    =COUNTIFS(data,"<>*pink*",data,"<>*orange*",data,"<>*black*")
    

This formula uses the not equal to [operator](https://exceljet.net/glossary/logical-operators)
 (<>) with the asterisk (\*) [wildcard](https://exceljet.net/glossary/wildcard)
 to count cells that do not contain each string anywhere. However, with this approach, you must enter a new pair of range/criteria arguments for each string to exclude. In contrast, the formula explained below can handle a large number of strings to exclude entered directly in a range on the worksheet.

### MMULT function

In the example shown, the formula in cell F5 is:

    {=SUM(1-(MMULT(--(ISNUMBER(SEARCH(TRANSPOSE(exclude),data))),ROW(exclude)^0)>0))}
    

This is a complex formula built around the MMULT function, which is designed to perform matrix multiplication. However, the core of the formula is based on the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
 functions:

    ISNUMBER(SEARCH(TRANSPOSE(exclude),data))
    

Here, we transpose the items in the [named range](https://exceljet.net/glossary/named-range)
 "exclude", then feed the result to SEARCH as the _find\_text_, with **data** provided as _within\_text_. The SEARCH function returns a 2d [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values, 10 rows by 3 columns, like this:

    {3,#VALUE!,12;#VALUE!,4,#VALUE!;#VALUE!,#VALUE!,#VALUE!;#VALUE!,#VALUE!,#VALUE!;#VALUE!,#VALUE!,3;14,#VALUE!,#VALUE!;#VALUE!,#VALUE!,#VALUE!;#VALUE!,#VALUE!,#VALUE!;#VALUE!,#VALUE!,#VALUE!;3,#VALUE!,12}
    

For each value in **data**, we have 3 results (one per search string) that are either #VALUE errors or numbers. Numbers represent the position of a found text string, and errors represent text strings not found. The TRANSPOSE function is needed to generate the 10 x 3 array of complete results.

This array is fed into ISNUMBER to get TRUE FALSE values, which we convert to 1s and 0s with a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) operator. The result is an array like this:

    {1,0,1;0,1,0;0,0,0;0,0,0;0,0,1;1,0,0;0,0,0;0,0,0;0,0,0;1,0,1}
    

### MMULT function

The array above is provided to the MMULT function as _array1_. Following the rules of matrix multiplication, number of columns in _array1_ must equal the number of rows in _array2_. To generate _array2_, we use the ROW function like this:

    ROW(exclude)^0
    

This yields an array of 1s, 3 rows by 1 column:

    {1;1;1}
    

which goes into MMULT as _array2_. After array multiplication, we have an array dimensioned to match the original data:

    {2;1;0;0;1;1;0;0;0;2}
    

In this array, any non-zero number represents a value where at least one of the excluded strings has been found. Zeros indicate no excluded strings were found. To force all non-zero values to 1, we use greater than zero:

    {2;1;0;0;1;1;0;0;0;2}>0
    

which creates yet another array of TRUE and FALSE values:

    {TRUE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;FALSE;FALSE;TRUE}
    

Our final goal is to count only text values _where no excluded strings were found_, so we need to _reverse_ these values. We do this by subtracting the array from 1. This is an example of [boolean logic](https://exceljet.net/glossary/boolean-logic)
. The math operation automatically coerces TRUE and FALSE values to 1s and 0s, and we finally have an array to return to the SUM function:

    =SUM({0;0;1;1;0;0;1;1;1;0})
    

The SUM function returns a final result of 5.

### REDUCE function

The [REDUCE function](https://exceljet.net/functions/reduce-function)
, available in [Excel 365](https://exceljet.net/glossary/excel-365)
, offers a more straightforward way to solve this problem. REDUCE loops over a range of data and applies a custom calculation to each cell, aggregating results to a single value using the calculation of your choice. To solve this problem with REDUCE, you can use a formula like this:

    =REDUCE(0,data,LAMBDA(a,b,a+NOT(SUM(--ISNUMBER(SEARCH(exclude,b))))))
    

The logic is similar to the formula described above, but simplified somewhat since we only need to check one cell at a time.

Related formulas
----------------

[![Excel formula: Count cells not equal to many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20many.png "Excel formula: Count cells not equal to many things")](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

### [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

First, a little context. Normally, if you have just a couple things you don't want to count, you can use COUNTIFS like this: =COUNTIFS(range,"<>apple",range,"<>orange") But this doesn't scale very well if you have a list of many things, because you'll have to add an additional range/...

[![Excel formula: Count cells not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to.png "Excel formula: Count cells not equal to")](https://exceljet.net/formulas/count-cells-not-equal-to)

### [Count cells not equal to](https://exceljet.net/formulas/count-cells-not-equal-to)

In this example, the goal is to count the number of cells in column D that are not equal to a given color. The simplest way to do this is with the COUNTIF function , as explained below. Not equal to In Excel, the operator for not equal to is "<>". For example: =A1<>10 // A1 is not equal...

[![Excel formula: Count cells not equal to x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20x%20or%20y_1.png "Excel formula: Count cells not equal to x or y")](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

### [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

In this example, the goal is to count the number of cells in data (B5:B15) that are not equal to "red" or "blue". This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. Not equal to The not equal to operator in Excel is <>. For example, with the...

[![Excel formula: Count not equal to multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20not%20equal%20to%20multiple%20criteria.png "Excel formula: Count not equal to multiple criteria")](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

### [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

In this example, the goal is to count rows in a set of data using multiple criteria and "not equals to" logic. Specifically, we want to count males that are not in group A or B. All data is in an Excel Table named data in the range B5:D15. This problem can be solved with the COUNTIFS function or...

Related functions
-----------------

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel MMULT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mmult%20function.png "Excel MMULT function")](https://exceljet.net/functions/mmult-function)

### [MMULT Function](https://exceljet.net/functions/mmult-function)

The Excel MMULT function returns the matrix product of two arrays. The result from MMULT is an [array](https://exceljet.net/glossary/array)
 that contains the same number of rows as _array1_ and the same number of columns as _array2_. 

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    
*   [Count cells not equal to](https://exceljet.net/formulas/count-cells-not-equal-to)
    
*   [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
    
*   [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)
    

### Functions

*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [MMULT Function](https://exceljet.net/functions/mmult-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    

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