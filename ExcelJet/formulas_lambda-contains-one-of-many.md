# LAMBDA contains one of many - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-contains-one-of-many

---

[Skip to main content](https://exceljet.net/formulas/lambda-contains-one-of-many#main-content)

[](https://exceljet.net/formulas/lambda-contains-one-of-many#)

*   [Previous](https://exceljet.net/formulas/lambda-append-range-horizontal)
    
*   [Next](https://exceljet.net/formulas/lambda-contains-which-things)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA contains one of many
===========================

by Dave Bruns · Updated 27 Aug 2022

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[SUM](https://exceljet.net/functions/sum-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel formula: LAMBDA contains one of many](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20contains%20one%20of%20many.png "Excel formula: LAMBDA contains one of many")

Summary
-------

Excel does not provide a dedicated "contains" function to test a cell for one or more text strings. However, you can use the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to create a custom function for this purpose. In the example below, the formula in cell C5 is:

    =ContainsOneOfMany(B5,{"red","blue","green"})
    

This formula will return TRUE if a cell contains any one of the strings passed into it. Because it is built with the [SEARCH function](https://exceljet.net/functions/search-function)
, it automatically performs partial matching and supports [wildcards](https://exceljet.net/glossary/wildcard)
.

Generic formula
---------------

    =LAMBDA(text,strings,SUM(--ISNUMBER(SEARCH(strings,text)))>0)

Explanation 
------------

Excel does not provide a dedicated "contains" function, but you can create a custom function to test if a cell contains one or many strings with the [LAMBDA function](https://exceljet.net/functions/lambda-function)
. LAMBDA functions do not require VBA, but are only available in [Excel 365](https://exceljet.net/glossary/excel-365)
.

The first step in creating a custom LAMBDA function is to verify the logic needed with a Excel standard formula. This LAMBDA formula is based on a Excel formula created with three functions: [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
, [ISNUMBER](https://exceljet.net/functions/isnumber-function)
, and [SEARCH](https://exceljet.net/functions/search-function)
:

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,A1)))>0
    

[Read a detailed description here](https://exceljet.net/formulas/cell-contains-one-of-many-things)
. Because the LAMBDA function is only available in the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, which handles [array formulas](https://exceljet.net/glossary/array-formula)
 natively, we are using SUM instead of SUMPRODUCT ([see note below](https://exceljet.net/formulas/lambda-contains-one-of-many#sumproduct_note)
), and renaming "things" to "strings" to make the formula arguments a bit more natural:

    =SUM(--ISNUMBER(SEARCH(strings,A1)))>0 // base formula
    

The screen below shows this formula in use with three strings "red", "blue", and "green":

![The standard Excel formula in action](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lambda%20contains%20one%20of%20many%20standard.png?itok=Kk-0qxds "The standard Excel formula in action")

This formula returns TRUE for any cell in column B that contains any one of the strings "red", "blue", or "green".

The next step is to convert this formula into a generic (unnamed) LAMBDA formula. We will need two input parameters, one for the text, and one for the strings to test. These need to appear as the first arguments in the LAMBDA formula. The final argument contains the calculation to perform, which is adapted from our standard Excel formula above. Here is the generic LAMBDA:

    =LAMBDA(text,strings,SUM(--ISNUMBER(SEARCH(strings,text)))>0)
    

The screen below shows this formula in action, with the testing syntax needed to provide values for text and strings:

    =LAMBDA(text,strings,SUM(--ISNUMBER(SEARCH(strings,text)))>0)(B5,{"red","blue","green"})
    

![Testing the generic LAMBDA formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lambda%20contains%20one%20of%20many%20generic.png?itok=EBhV1xf_ "Testing the generic LAMBDA formula")

Note that results are the same as above. The next step in creating a custom LAMBDA is to name and define the formula with the [Name Manager](https://exceljet.net/glossary/name-manager)
. In this case, we'll use the name "ContainsOneOfMany":

![LAMBDA version defined in Name Manager](https://exceljet.net/sites/default/files/images/formulas/inline/lambda%20contains%20one%20of%20many%20name%20manager.png "LAMBDA version defined in Name Manager")

Finally, we update the worksheet to use the new custom function, and confirm that results are the same:

![Custom LAMBDA function in action](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lambda%20contains%20one%20of%20many%20final.png?itok=BjkS37QL "Custom LAMBDA function in action")

### Notes

Although we are hard-coding the strings "red", "blue", and "green" as an [array constant](https://exceljet.net/glossary/array-constant)
 in this example for simplicity, the formula will work fine if we supply a range instead:

    =ContainsOneOfMany(A1,range)
    

In addition, the formula will also work correctly if we supply only one string:

    =ContainsOneOfMany(A1,"red")
    

_Note: Traditionally, [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 is often seen in array formulas, because it can handle arrays natively, without control + shift + enter. This makes the formula "more friendly" to most users. The [SUM function](https://exceljet.net/functions/sum-function)
 can also be used in these cases, but the formula must then be entered with control + shift + enter. In Excel 365, the SUM function will work in these cases without any special handling. Since LAMBDA is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
, this example uses SUM, since SUMPRODUCT provides no additional benefit._

Related formulas
----------------

[![Excel formula: Count total words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_total_words_in_cell.png "Excel formula: Count total words in a cell")](https://exceljet.net/formulas/count-total-words-in-a-cell)

### [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)

In this example, the goal is to count the total number of words in a cell. Excel doesn't have a dedicated function for counting words. However, with a little ingenuity, you can create a formula to perform this task using a combination of built-in functions. In newer versions of Excel, the best...

[![Excel formula: LAMBDA replace characters recursive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20replace%20characters.png "Excel formula: LAMBDA replace characters recursive")](https://exceljet.net/formulas/lambda-replace-characters-recursive)

### [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)

The LAMBDA function can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. However, one disadvantage to recursive LAMBDA functions is that...

[![Excel formula: LAMBDA count words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20count%20words.png "Excel formula: LAMBDA count words")](https://exceljet.net/formulas/lambda-count-words)

### [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)

The LAMBDA function can be used to create reusable, custom functions in Excel without VBA or macros. The first step in creating a LAMBDA function is to verify the formula logic needed in a standard Excel formula. In this example, the base formula is: =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(LEN(...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)
    
*   [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    
*   [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

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