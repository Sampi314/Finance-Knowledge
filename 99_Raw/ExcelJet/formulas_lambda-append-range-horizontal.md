# LAMBDA append range horizontal - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-append-range-horizontal

---

[Skip to main content](https://exceljet.net/formulas/lambda-append-range-horizontal#main-content)

[](https://exceljet.net/formulas/lambda-append-range-horizontal#)

*   [Previous](https://exceljet.net/formulas/lambda-append-range)
    
*   [Next](https://exceljet.net/formulas/lambda-contains-one-of-many)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA append range horizontal
==============================

by Dave Bruns · Updated 26 Aug 2022

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[INDEX](https://exceljet.net/functions/index-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel formula: LAMBDA append range horizontal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20append%20range%20horizontal.png "Excel formula: LAMBDA append range horizontal")

Summary
-------

Excel does not provide a function to append ranges in a horizontal fashion, but you can use the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to create a custom function to combine two ranges, one next to the other. In the example below, the formula in cell C5 is:

    =AppendRangeHorizontal(B5:C12,E5:F10,"")
    

This formula combines the two ranges provided (B5:C12 and E5:F10), by appending the second range to the right of the first range. The result is returned as an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 into H5:K12. The third argument provides a default value to use when the formula runs into errors combining ranges, for example when ranges have different column or row counts.

Explanation 
------------

Excel does not provide a formula function to append or combine ranges, either horizontally or vertically. You can use Power Query for this task, and this makes sense for data transformations that must be automated and repeated on an on-going basis. However, you can also use the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to create a custom function to combine ranges. This makes sense when you have good control over the data and need a solution that updates automatically, without a refresh step.

In the example below, the formula in cell C5 is:

    =AppendRangeHorizontal(B5:C12,E5:F10,"")
    

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
      rowindex,SEQUENCE(MAX(rows1,rows2)),
      colindex,SEQUENCE(1,cols1+cols2),
      result,
      IF(
        colindex<=cols1,
        INDEX(range1,rowindex,colindex),
        INDEX(range2,rowindex,colindex-cols1)
      ),
      IFERROR(result,default)
      )
    )
    

This formula is based on a [formula explained here](https://exceljet.net/formulas/lambda-append-range)
, adapted to work with columns instead or rows. It's a good example of how the LAMBDA function and [LET function](https://exceljet.net/functions/let-function)
 work well together. Inside the LET function, the first six lines of code simply assign values to variables. Once values are assigned, these variables drive the output of the function.

The core logic of the formula, the code that builds the combined array, is here:

    result,
      IF(
        colindex<=cols1,
        INDEX(range1,rowindex,colindex),
        INDEX(range2,rowindex,colindex-cols1)
      ),
      IFERROR(result,default)
      )
    

This code can be tricky to read, especially if you're new to LAMBDA functions and [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 in general. With line breaks added for readability, it's tempting to read it like a loop, with **colindex** as an incrementing counter, but **colindex** is not one value, but an array of 4 values, created with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 earlier:

    colindex,SEQUENCE(1,cols1+cols2) // returns {1,2,3,4)
    

Similarly, **rowindex** is an array of 8 numbers:

    rowindex,SEQUENCE(rows1+rows2) // returns {1;2;3;4;5;6;7;8} 
    

The [IF function](https://exceljet.net/functions/if-function)
 tests the values in **colindex** all at once. If **colindex** is less than or equal to the count of the columns in **range1** (2), [INDEX](https://exceljet.net/functions/index-function)
 fetches columns from **range1**. If the **colindex** is greater than 2, INDEX fetches columns from **range2**. In both cases, **rowindex** is used to retrieve rows.

The array that IF and INDEX create is assigned to the variable **result**, which is returned as a final value by the formula through the [IFERROR function](https://exceljet.net/functions/iferror-function)
. This is done as a way to catch errors that occur when ranges of different row or column counts are combined. In this case, INDEX will throw an error when it tries to get a value from a non-existent row or column, and the default value will be output instead of the error.

Related formulas
----------------

[![Excel formula: LAMBDA append range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20append%20range.png "Excel formula: LAMBDA append range")](https://exceljet.net/formulas/lambda-append-range)

### [LAMBDA append range](https://exceljet.net/formulas/lambda-append-range)

Note: this example was created before the VSTACK function and HSTACK function were introduced to Excel. VSTACK combines ranges vertically and HSTACK combines ranges horizontally. These functions are a much easier way to append ranges, but this example is still useful as a way to understand how to...

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

*   [LAMBDA append range](https://exceljet.net/formulas/lambda-append-range)
    
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