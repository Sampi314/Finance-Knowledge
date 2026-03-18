# XLOOKUP return blank if blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-return-blank-if-blank

---

[Skip to main content](https://exceljet.net/formulas/xlookup-return-blank-if-blank#main-content)

[](https://exceljet.net/formulas/xlookup-return-blank-if-blank#)

*   [Previous](https://exceljet.net/formulas/xlookup-rearrange-columns)
    
*   [Next](https://exceljet.net/formulas/xlookup-two-way-exact-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP return blank if blank
=============================

by Dave Bruns · Updated 16 Jun 2022

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[IF](https://exceljet.net/functions/if-function)

[LET](https://exceljet.net/functions/let-function)

![Excel formula: XLOOKUP return blank if blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20if%20blank%20return%20blank.png "Excel formula: XLOOKUP return blank if blank")

Summary
-------

To make XLOOKUP display a blank cell when a lookup result is blank, you can use a formula based on [LET](https://exceljet.net/functions/let-function)
, [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, and the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in cell H9 is:

    =LET(x,XLOOKUP(G9,B5:B16,D5:D16),IF(x="","",x))
    

Because the lookup result in cell D9 is empty, the final result is an [empty string](https://exceljet.net/glossary/empty-string)
 (""). By contrast, a standard XLOOKUP formula in cell H5 returns nothing, which displays as "0-Jan-00".

Explanation 
------------

When [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 can't find a value in a lookup array, it returns an #N/A error. You can use the [IFNA function](https://exceljet.net/functions/ifna-function)
 or [IFERROR function](https://exceljet.net/functions/iferror-function)
 to trap this error and return a different result. However, when the result is an _empty cell_, XLOOKUP does not throw an error. Instead, XLOOKUP returns an empty result, which behaves like a zero. This can make it look like the lookup result has a value even though the original cell is empty.

In this example, the goal is to trap an empty lookup result from the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 and display the result as an empty cell. For example, in the worksheet shown, the formula in cell H5 is:

    =XLOOKUP(G5,B5:B16,D5:D16)
    

Because H5 is formatted as a date, and because the result comes from cell D9 (which is empty) the result from XLOOKUP behaves like zero and displays as "0-Jan-00". The goal is to display a _blank cell_, as seen in cell H9, which contains a modified XLOOKUP formula.

### Without LET

One way to solve this problem is with the [IF function](https://exceljet.net/functions/if-function)
 and two XLOOKUP function calls like this:

    =IF(XLOOKUP(G5,B5:B16,D5:D16)="","",XLOOKUP(G5,B5:B16,D5:D16))
    

_Translation: If the result from XLOOKUP is nothing, then return an [empty string](https://exceljet.net/glossary/empty-string)
 (""), otherwise, return the result from XLOOKUP._

The structure of the formula is redundant, since the XLOOKUP function appears twice, but the formula itself will work fine, and the same idea can be used with [older functions like VLOOKUP](https://exceljet.net/formulas/vlookup-if-blank-return-blank)
.

### With LET

One way to eliminate the second instance of XLOOKUP in the formula is to use the [LET function](https://exceljet.net/functions/let-function)
. The LET function makes it possible to declare named variables in a formula. With LET, the same formula can be written like this:

    =LET(x,XLOOKUP(G9,B5:B16,D5:D16),IF(x="","",x))
    

_Translation: create a variable named "x" and use the result from XLOOKUP to assign a value to x. If x is empty, then return an empty string (""). Otherwise, return the value of x._

The result is the same but notice this streamlined version of the formula only uses the XLOOKUP function one time.

### Multiple values

Because the IF function will process each item in an [array](https://exceljet.net/glossary/array)
 separately, you can use the same pattern above to handle multiple results like this:

    =LET(results,XLOOKUP(G9,B5:B16,C5:E16),IF(results="","",results))
    

The return array in this formula covers three columns, so XLOOKUP will return 3 values in an array. Each value in the array is processed separately by the IF function. The variable name "results" is entirely arbitrary.

Related formulas
----------------

[![Excel formula: VLOOKUP if blank return blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20if%20blank%20return%20blank.png "Excel formula: VLOOKUP if blank return blank")](https://exceljet.net/formulas/vlookup-if-blank-return-blank)

### [VLOOKUP if blank return blank](https://exceljet.net/formulas/vlookup-if-blank-return-blank)

In this example, the goal is create a VLOOKUP formula that will return an empty cell when the lookup result is an empty cell. When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. You can use the IFNA function or IFERROR function to trap this error. However, when the result...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

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

*   [VLOOKUP if blank return blank](https://exceljet.net/formulas/vlookup-if-blank-return-blank)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
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