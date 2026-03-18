# Excel SWITCH function | Exceljet

**Source:** https://exceljet.net/functions/switch-function

---

[Skip to main content](https://exceljet.net/functions/switch-function#main-content)

[](https://exceljet.net/functions/switch-function#)

*   [Previous](https://exceljet.net/functions/or-function)
    
*   [Next](https://exceljet.net/functions/true-function)
    

Excel 2019

[Logical](https://exceljet.net/functions#Logical)

SWITCH Function
===============

by Dave Bruns · Updated 8 Mar 2026

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[IFS](https://exceljet.net/functions/ifs-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel SWITCH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20switch.png "Excel SWITCH function")

Summary
-------

The Excel SWITCH function compares one value against a list of values, and returns a result corresponding to the first match found. When no match is found, SWITCH can return an optional default value.

Purpose 
--------

Match multiple values, return first match

Return value 
-------------

Result corresponding with first match

Syntax
------

    =SWITCH(expression,val1/result1,[val2/result2],...,[default])

*   _expression_ - The value or expression to match against.
*   _val1/result1_ - The first value and result pair.
*   _val2/result2_ - \[optional\] The second value and result pair.
*   _default_ - \[optional\] The default value to use when no match is found.

Using the SWITCH function 
--------------------------

The SWITCH function compares one value against a list of values and returns a result that corresponds to the first match found. You can use the SWITCH function when you want to perform a "self-contained" exact match lookup with several possible results. When no match is found, SWITCH can return an optional default value.

The first [argument](https://exceljet.net/glossary/function-argument)
 in SWITCH is called "expression" and can be a hard-coded constant, a cell reference, or a formula that returns a specific value to match against. Matching values and corresponding results are entered in pairs. SWITCH can handle up to 126 pairs of values and results. The last argument, _default_, is an optional value to return when there is no match.

### Key features

*   Can handle up to 126 value/result pairs
*   Can match a value or result from a formula
*   Is _not_ case-sensitive and _does not_ support wildcards
*   Returns #N/A when no match is found by default
*   All expressions are evaluated (no short-circuit behavior)

### Example

In the example shown, the formula in D5 is:

    =SWITCH(C5,1,"Poor",2,"OK",3,"Good","?")
    

SWITCH only performs an exact match, so you can't include [logical operators](https://exceljet.net/glossary/logical-operators)
 like greater than (>) or less than (<) in the logic used to determine a match. You can work around this limitation by constructing a formula to match against TRUE like this:

    =SWITCH(TRUE,A1>=1000,"Gold",A1>=500,"Silver","Bronze")
    

However, in a case like this, the [IFS function](https://exceljet.net/functions/ifs-function)
 would likely be more straightforward.

### SWITCH and performance

You might expect SWITCH to stop evaluating once it finds a matching value, but in fact, Excel evaluates [every expression in the formula](https://fastexcel.wordpress.com/2023/01/03/short-circuiting-excel-formulas-if-choose-ifs-and-switch/)
, even for cases that are not used. This can degrade performance when any expressions involve complex or time-consuming calculations.

In recursive LAMBDA functions, this behavior can also cause problems because unused result branches are still evaluated, potentially causing unwanted recursion and a #NUM error.

If you need "short-circuit" behavior, where Excel stops evaluating after finding the first match, consider using nested [IF functions](https://exceljet.net/functions/if-function)
 instead. The IF function performs true short-circuit evaluation, skipping unnecessary calculations once a match is found.

### SWITCH versus IFS

Like the [IFS function](https://exceljet.net/functions/ifs-function)
, the SWITCH function allows you to test more than one condition without [nesting multiple IF statements](https://exceljet.net/formulas/nested-if-function-example)
 in a single self-contained formula. SWITCH therefore makes it easier to write (and read) a formula with many conditions. One advantage of SWITCH over IFS is that the expression appears just once in the function and does not need to be repeated. However,  SWITCH is limited to exact matching. It is not possible to use operators like greater than (>) or less than (<) with the standard syntax.  In contrast, the IFS function actually requires expressions for each condition, so you can use [logical operators](https://exceljet.net/glossary/logical-operators)
 as needed.

### Notes

*   Expression can be another formula that returns a specific value.
*   SWITCH can handle up to 126 value/result pairs.
*   Enter a final argument to set a default result when no match is found.
*   SWITCH does not have short-circuit behavior; all expressions are evaluated

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel IFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ifs.png "Excel IFS function")](https://exceljet.net/functions/ifs-function)

### [IFS Function](https://exceljet.net/functions/ifs-function)

The Excel IFS function can run multiple tests and return a value corresponding to the first TRUE result. Use the IFS function to evaluate multiple conditions without multiple nested IF statements. IFS allows shorter, easier to read formulas....

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [IFS Function](https://exceljet.net/functions/ifs-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Links

*   [Microsoft SWITCH function documentation](https://support.office.com/en-us/article/switch-function-47ab33c0-28ce-4530-8a45-d532ec4aa25e)
    
*   [Short-circuiting Excel Formulas - FastExcel (Charles Williams)](https://fastexcel.wordpress.com/2023/01/03/short-circuiting-excel-formulas-if-choose-ifs-and-switch/)
    

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