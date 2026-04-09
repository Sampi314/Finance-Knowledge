# Combine ranges - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/combine-ranges

---

[Skip to main content](https://exceljet.net/formulas/combine-ranges#main-content)

[](https://exceljet.net/formulas/combine-ranges#)

*   [Previous](https://exceljet.net/formulas/combine-data-in-multiple-worksheets)
    
*   [Next](https://exceljet.net/formulas/count-unique-dates-ignore-time)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Combine ranges
==============

by Dave Bruns · Updated 25 Oct 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[ROWS](https://exceljet.net/functions/rows-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

[LET](https://exceljet.net/functions/let-function)

![Excel formula: Combine ranges](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/combine_ranges.png "Excel formula: Combine ranges")

Summary
-------

To combine or concatenate ranges in Excel with a formula, you can use the [VSTACK function](https://exceljet.net/functions/vstack-function)
 or the [HSTACK function](https://exceljet.net/functions/hstack-function)
. In the example below, the formula in cell F5 is:

    =VSTACK(range1,range2)

where **range1** (B5:B8) and **range2** (D5:D9) are [named ranges](https://exceljet.net/glossary/named-range)
. The formula appends the second range to the first range and the result [spills](https://exceljet.net/glossary/spill)
 into F5:F13.

_Note: Before the VSTACK and HSTACK functions where introduced, but after [dynamic array formulas were available](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, it was possible to combine ranges with a more complex formula using the SEQUENCE function. See below for a detailed explanation._

Explanation 
------------

In this example, the goal is to combine ranges. With the introduction of the VSTACK function and the HSTACK function, this is quite a simple task. To combine ranges vertically, stacking one range on top of another, you can use the VSTACK function like this:

    =VSTACK(range1,range2)

To combine ranges horizontally, you can use the HSTACK function like this:

    =HSTACK(range1,range2)

In both formulas above, **range1** (B5:B8) and **range2** (D5:D9) are [named ranges](https://exceljet.net/glossary/named-range)
. The named ranges are for convenience only, you can use the raw cell references with the same result. For details on how these functions work see our documentation here: [VSTACK function](https://exceljet.net/functions/vstack-function)
, [HSTACK function](https://exceljet.net/functions/hstack-function)
.

Manual approach
---------------

Before the VSTACK and HSTACK functions where introduced, but after [dynamic array formulas were available](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, it was possible to combine ranges with a more complex formula using the SEQUENCE function together with the LET function, the INDEX function, and the IF function. This is a much more manual approach, but it is an interesting example of how you can iterate through cells in a range keeping track of where you are as you go. The original formulas are below for reference. They are still useful for understanding how you can manipulate arrays in a formula.

### Single column ranges

![Manual formula to combine single column ranges](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/combine_ranges_manual.png "Manual formula to combine single column ranges")

The formula to combine single column ranges is based on [INDEX function](https://exceljet.net/functions/index-function)
, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
, the [IF function](https://exceljet.net/functions/if-function)
, and the [LET function](https://exceljet.net/functions/let-function)
. In the example above, the formula in cell F5 is:

    =LET(a,range1,b,range2,s,SEQUENCE(ROWS(a)+ROWS(b)),IF(s>ROWS(a),INDEX(b,s-ROWS(a)),INDEX(a,s)))
    

Adding line breaks to make the formula more readable, we have:

    =LET(
       a,range1,
       b,range2,
       s,SEQUENCE(ROWS(a)+ROWS(b)),
       IF(s>ROWS(a),
          INDEX(b,s-ROWS(a)),
          INDEX(a,s)))
    

where **range1** (B5:B8) and **range2** (D5:D9) are [named ranges](https://exceljet.net/glossary/named-range)
. The first two lines inside let assign **range1** to the variable "a" and assign **range2** to the variable "b".

_Note: **Range1** and **Range2** do not have to be provided as named ranges; you could instead use B5:B8 and D5:D9._

Next, the SEQUENCE function creates a numeric "row index" to cover all rows in both ranges:

    =SEQUENCE(ROWS(a)+ROWS(b))
    =SEQUENCE(9)
    ={1;2;3;4;5;6;7;8;9}
    

The resulting [array](https://exceljet.net/glossary/array)
 is assigned to the variable "s". In the next line, the IF function is used to iterate through the array. If the current value **s** is greater than the rows in **a**, the INDEX function returns the value of **b** at row **s** minus the row count of **a**:

    INDEX(b,s-ROWS(a)) // value from b
    

Otherwise, the INDEX function returns the value of **a** at row **s**:

    INDEX(a,s) // value from a
    

The resulting values [spill](https://exceljet.net/glossary/spill)
 into the range F5:F13.

_Note: a reader mentioned this formula to me based on the [stackoverflow answer here](https://stackoverflow.com/a/70561154)
._

### Multiple column ranges

The formula to combine ranges with multiple columns is more complex. In the worksheet below, the formula in B5 looks like this

    =LET(
       a,range1,
       b,range2,
       r,SEQUENCE(ROWS(a)+ROWS(b)),
       c,SEQUENCE(1,COLUMNS(a)),
       IF(
          r<=ROWS(a),
          INDEX(a,r,c),
          INDEX(b,r-ROWS(a),c))
    )
    

where **range1** (E5:F9) and **range2** (H5:I10) are [named ranges](https://exceljet.net/glossary/named-range)
. Note that [line breaks](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 have been added for readability. 

![Formula to combine ranges with multiple columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/combine%20ranges%20with%20multiple%20columns2.png?itok=pa206_CY "Formula to combine ranges with multiple columns")

Like the formula above, this formula figures out how many rows are in both ranges, and uses the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 to create a "row index" with the SEQUENCE function here:

    SEQUENCE(ROWS(a)+ROWS(b)) // returns {1;2;3;4;5;6;7;8;9;10;11}
    

In a similar way, SEQUENCE is also used to create a "column index", named "c":

    SEQUENCE(1,COLUMNS(a)) // returns {1,2}
    

The [IF function](https://exceljet.net/functions/if-function)
 tests all values in the row index sequence with the row count for range 1. When a row index value is less than or equal to the count of the rows in **a** (5), the INDEX function is used to fetch a row from range **a** at the current index value (r)**:**

    INDEX(a,r,c) // from range a
    

When a row index value is greater than 5, INDEX is used to fetch rows from **b**:

    INDEX(b,r-ROWS(a),c))
    

Note **c** remains constant as {1,2} , the column index for range **a**. This is a shortcut to keep things simple. This formula does not try to figure out if the column counts for both ranges are the same or not. It simply assumes the column counts are the same and requests both columns.

### Custom function with LAMBDA

The [LAMBDA function](https://exceljet.net/functions/lambda-function)
 can be used to create custom functions. The formula on this page is a good candidate, because it is relatively complex. When converted to a custom LAMBDA function, it is much easier to call:

    =AppendRange(range1,range2)
    

See [this article](https://exceljet.net/formulas/lambda-append-range)
 for more detail.

Related formulas
----------------

[![Excel formula: LAMBDA append range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20append%20range.png "Excel formula: LAMBDA append range")](https://exceljet.net/formulas/lambda-append-range)

### [LAMBDA append range](https://exceljet.net/formulas/lambda-append-range)

Note: this example was created before the VSTACK function and HSTACK function were introduced to Excel. VSTACK combines ranges vertically and HSTACK combines ranges horizontally. These functions are a much easier way to append ranges, but this example is still useful as a way to understand how to...

[![Excel formula: Unique values from multiple ranges ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20from%20multiple%20ranges.png "Excel formula: Unique values from multiple ranges ")](https://exceljet.net/formulas/unique-values-from-multiple-ranges)

### [Unique values from multiple ranges](https://exceljet.net/formulas/unique-values-from-multiple-ranges)

In this example, the goal is to extract unique values from three separate ranges at the same time: range1 (C5:C16), range2 (D5:D15), and range3 (F5:F13). At one time, this was a difficult problem, since UNIQUE is programmed to accept only one array and there is no obvious way to provide another...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [LAMBDA append range](https://exceljet.net/formulas/lambda-append-range)
    
*   [Unique values from multiple ranges](https://exceljet.net/formulas/unique-values-from-multiple-ranges)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    

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