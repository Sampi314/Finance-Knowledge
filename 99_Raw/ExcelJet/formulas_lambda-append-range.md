# LAMBDA append range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-append-range

---

[Skip to main content](https://exceljet.net/formulas/lambda-append-range#main-content)

[](https://exceljet.net/formulas/lambda-append-range#)

*   [Previous](https://exceljet.net/formulas/groupby-with-survey-results)
    
*   [Next](https://exceljet.net/formulas/lambda-append-range-horizontal)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA append range
===================

by Dave Bruns · Updated 19 Jan 2026

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[INDEX](https://exceljet.net/functions/index-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel formula: LAMBDA append range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20append%20range.png "Excel formula: LAMBDA append range")

Summary
-------

Excel does not provide a function to append ranges, but you can use the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to create a custom function to combine ranges. In the example below, the formula in cell B5 is:

    =AppendRange(E5:F9,H5:I10,"null")
    

This formula combines the two ranges provided (E5:F9 and H5:I10) by appending the second range to the first range, and returns an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 into B5:C15. The third argument provides a default value to use when the formula runs into errors combining ranges, for example, when ranges have different column counts.

Note: this example was created before the [VSTACK function](https://exceljet.net/functions/vstack-function)
 and [HSTACK function](https://exceljet.net/functions/hstack-function)
 _were introduced to Excel. VSTACK combines ranges vertically, and HSTACK combines ranges horizontally. These functions are a much easier way to append ranges, but this example is still useful as a way to understand how to approach more complicated problems with_ [_dynamic array formulas_](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. 

Generic formula
---------------

    =AppendRange(range1,range2,default)

Explanation 
------------

Note: this example was created before the [VSTACK function](https://exceljet.net/functions/vstack-function)
 and [HSTACK function](https://exceljet.net/functions/hstack-function)
 _were introduced to Excel. VSTACK combines ranges vertically and HSTACK combines ranges horizontally. These functions are a much easier way to append ranges, but this example is still useful as a way to understand how to approach more complicated problems with_ [_dynamic array formulas_](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. 

You can use the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to create a custom function to combine ranges. In the example below, the formula in cell C5 is:

    =AppendRange(E5:F9,H5:I10,"null")
    

This is a custom function created with LAMBDA, based on several Excel functions, including [INDEX](https://exceljet.net/functions/index-function)
, [SEQUENCE](https://exceljet.net/functions/sequence-function)
, [IFERROR](https://exceljet.net/functions/iferror-function)
, [ROWS](https://exceljet.net/functions/rows-function)
, [COLUMNS](https://exceljet.net/functions/columns-function)
, and [MAX](https://exceljet.net/functions/max-function)
. Holding the whole thing together are [LAMBDA](https://exceljet.net/functions/lambda-function)
 and [LET](https://exceljet.net/functions/let-function)
:

    =LAMBDA(range1,range2,default,
      LET(
      rows1,ROWS(range1),
      rows2,ROWS(range2),
      cols1,COLUMNS(range1),
      cols2,COLUMNS(range2),
      rowindex,SEQUENCE(rows1+rows2),
      colindex,SEQUENCE(1,MAX(cols1,cols2)),
      result,
      IF(
        rowindex<=rows1,
        INDEX(range1,rowindex,colindex),
        INDEX(range2,rowindex-rows1,colindex)
      ),
      IFERROR(result,default)
      )
    )
    

This formula is based on a [simplified formula explained here](https://exceljet.net/formulas/combine-ranges)
. It's a good example of how the LAMBDA function and LET function work well together. Inside the LET function, the first six lines of code simply assign values to variables. Once values are assigned, these variables drive the output of the function.

The core logic of the formula, the code that builds the combined array, is here:

      result,
      IF(
        rowindex<=rows1,
        INDEX(range1,rowindex,colindex),
        INDEX(range2,rowindex-rows1,colindex)
      ),
      IFERROR(result,default)
      )
    
    

This code can be tricky to read, especially if you're new to LAMBDA functions and [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 in general. With line breaks added for readability, it's tempting to read it like a loop, with **rowindex** as an incrementing counter, but in reality, **rowindex** is not one value, but an array of 11 values, created with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 earlier:

    rowindex,SEQUENCE(rows1+rows2) // assigns {1;2;3;4;5;6;7;8;9;10;11}
    

The [IF function](https://exceljet.net/functions/if-function)
 tests the values in **rowindex** all at once. If **rowindex** is less than or equal to the count of the rows in **range1** (5), [INDEX](https://exceljet.net/functions/index-function)
 fetches rows from **range1**. If the **rowindex** is greater than 5, INDEX fetches rows from **range2**. If we expand the values of the variables, the code looks something like this:

    =IF({1;2;3;4;5;6;7;8;9;10;11}<=5,
    INDEX(E5:F9,{1;2;3;4;5;6;7;8;9;10;11},{1,2}),
    INDEX(H5:I10,{1;2;3;4;5;6;7;8;9;10;11}-5,{1,2}))
    

This code can be tested directly on a worksheet, and it will return the same result as the formula.

The array that IF and INDEX create is assigned to the variable **result**, which is returned as a final value by the formula through the [IFERROR function](https://exceljet.net/functions/iferror-function)
. This is done as a way to catch errors that occur when ranges of different column counts are combined. For example if you combine a two-column range with a one-column range, INDEX will throw an error when it tries to get values from column 2, since column 2 does not exist. In this case, the default value will be output instead of an error.

Related formulas
----------------

[![Excel formula: LAMBDA split text to array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20split%20text%20to%20array.png "Excel formula: LAMBDA split text to array")](https://exceljet.net/formulas/lambda-split-text-to-array)

### [LAMBDA split text to array](https://exceljet.net/formulas/lambda-split-text-to-array)

Excel did not originally offer the TEXTSPLIT function. This article describes how to use the LAMBDA function to create a custom function that splits text as a workaround. It's a good example of how the LAMBDA function can be used to bridge a gap, but the workaround is no longer necessary. I leave...

[![Excel formula: LAMBDA replace characters recursive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20replace%20characters.png "Excel formula: LAMBDA replace characters recursive")](https://exceljet.net/formulas/lambda-replace-characters-recursive)

### [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)

The LAMBDA function can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. However, one disadvantage to recursive LAMBDA functions is that...

[![Excel formula: LAMBDA count words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20count%20words.png "Excel formula: LAMBDA count words")](https://exceljet.net/formulas/lambda-count-words)

### [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)

The LAMBDA function can be used to create reusable, custom functions in Excel without VBA or macros. The first step in creating a LAMBDA function is to verify the formula logic needed in a standard Excel formula. In this example, the base formula is: =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(LEN(...

[![Excel formula: LAMBDA contains one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20contains%20one%20of%20many.png "Excel formula: LAMBDA contains one of many")](https://exceljet.net/formulas/lambda-contains-one-of-many)

### [LAMBDA contains one of many](https://exceljet.net/formulas/lambda-contains-one-of-many)

Excel does not provide a dedicated "contains" function, but you can create a custom function to test if a cell contains one or many strings with the LAMBDA function . LAMBDA functions do not require VBA, but are only available in Excel 365 . The first step in creating a custom LAMBDA function is to...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [LAMBDA split text to array](https://exceljet.net/formulas/lambda-split-text-to-array)
    
*   [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    
*   [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)
    
*   [LAMBDA contains one of many](https://exceljet.net/formulas/lambda-contains-one-of-many)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

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