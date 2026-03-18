# LAMBDA split text to array - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-split-text-to-array

---

[Skip to main content](https://exceljet.net/formulas/lambda-split-text-to-array#main-content)

[](https://exceljet.net/formulas/lambda-split-text-to-array#)

*   [Previous](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    
*   [Next](https://exceljet.net/formulas/lambda-strip-characters)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA split text to array
==========================

by Dave Bruns · Updated 19 Jan 2026

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[FILTERXML](https://exceljet.net/functions/filterxml-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

![Excel formula: LAMBDA split text to array](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20split%20text%20to%20array.png "Excel formula: LAMBDA split text to array")

Summary
-------

When dynamic arrays were [first introduced](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, Excel did not offer a function to split a text string into an array, like PHP's explode(), or Python's split(). However, with the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 it was possible to create a custom function that worked the same way. In the example below, the formula in cell C5 is:

    =SplitTextToArray(B5,",")
    

This formula splits the text in B5 using a comma (",") as the delimiter. The result is a horizontal [array](https://exceljet.net/glossary/array)
 that [spills](https://exceljet.net/glossary/spill)
 into columns D through H. The delimiter is provided as the second argument to the function, and can be changed to suit the situation.

> Note: This is an interesting and useful LAMBDA example, but Excel 365 now provides the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
> , which makes this workaround unnecessary in newer versions of Excel.

Generic formula
---------------

    =LAMBDA(text,delim,TRANSPOSE(FILTERXML("<x><y>"&SUBSTITUTE(text,delim,"</y><y>")&"</y></x>","//y")))

Explanation 
------------

> Excel did not originally offer the TEXTSPLIT function. This article describes how to use the [LAMBDA function](https://exceljet.net/functions/lambda-function)
>  to create a custom function that splits text as a workaround. It's a good example of how the LAMBDA function can be used to bridge a gap, but the workaround is no longer necessary. I leave the article below for historical reference only. - Dave

The first step in creating a custom LAMBDA function is to verify the logic needed using standard formula. This LAMBDA formula is based on an interesting Excel formula created with the [FILTERXML](https://exceljet.net/functions/filterxml-function)
, [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
, and [TRANSPOSE](https://exceljet.net/functions/transpose-function)
 functions:

    =TRANSPOSE(FILTERXML("<x><y>"&SUBSTITUTE(B5,",","</y><y>")&"</y></x>","//y"))
    

In a nutshell, this formula transforms the original text into a primitive XML format, and then parses the XML with the FILTERXML function. [Read a detailed description here](https://exceljet.net/formulas/text-split-to-array)
. Although this formula works, the formula itself is a bit messy and non-intuitive, and therefore a good candidate for a custom LAMBDA function, which will hide the complexity and make the formula easier to use.

Since we already know [the formula works](https://exceljet.net/formulas/text-split-to-array)
, the next step is to convert the formula into a generic (unnamed) LAMBDA formula. We will need two input parameters: one for the text to be split, and one for the delimiter to use when splitting. These need to appear as the first arguments in the LAMBDA formula, followed by a third argument containing the formula to execute, adapted to use the first two arguments by name. The result looks like this:

    =LAMBDA(text,delim,TRANSPOSE(FILTERXML("<x><y>"&SUBSTITUTE(text,delim,"</y><y>")&"</y></x>","//y")))
    

This formula can be tested on the worksheet using the LAMBDA testing syntax, which places the input arguments in a separate set of parentheses at the end:

    =LAMBDA(text,delim,TRANSPOSE(FILTERXML("<x><y>"&SUBSTITUTE(text,delim,"</y><y>")&"</y></x>","//y")))(B5,",")
    

Finally, we define and name the generic LAMBDA using the Name Manager (see the examples [on this page](https://exceljet.net/functions/lambda-function)
 for a more detailed explanation). Once the named formula has been created, it can be used anywhere in the workbook.

### Other delimiters

The design of this custom function allows the delimiter to be easily changed to suit the situation:

    =SplitTextToArray(A1,",") // split by comma
    =SplitTextToArray(A1," ") // split by space (words)
    =SplitTextToArray(A1,"-") // split by hyphen
    

The size resulting array will depend on how many delimiters exist in the original text string.

Related formulas
----------------

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

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

[![Excel FILTERXML function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20filterxml.png "Excel FILTERXML function")](https://exceljet.net/functions/filterxml-function)

### [FILTERXML Function](https://exceljet.net/functions/filterxml-function)

The Excel FILTERXML function returns specific data from XML text using the specified XPath expression.

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    
*   [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    
*   [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)
    
*   [LAMBDA contains one of many](https://exceljet.net/formulas/lambda-contains-one-of-many)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [FILTERXML Function](https://exceljet.net/functions/filterxml-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    

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