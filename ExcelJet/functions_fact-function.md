# Excel FACT function | Exceljet

**Source:** https://exceljet.net/functions/fact-function

---

[Skip to main content](https://exceljet.net/functions/fact-function#main-content)

[](https://exceljet.net/functions/fact-function#)

*   [Previous](https://exceljet.net/functions/exp-function)
    
*   [Next](https://exceljet.net/functions/factdouble-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

FACT Function
=============

by Dave Bruns · Updated 13 Sep 2021

Related functions 
------------------

[COMBIN](https://exceljet.net/functions/combin-function)

[PERMUT](https://exceljet.net/functions/permut-function)

[FACTDOUBLE](https://exceljet.net/functions/factdouble-function)

![Excel FACT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_fact.png "Excel FACT function")

Summary
-------

The Excel FACT function returns the factorial of a given number. For example, =FACT(3) returns 6, equivalent to 3 x 2 x 1.

Purpose 
--------

Find the factorial of a number

Return value 
-------------

The factorial of a number

Syntax
------

    =FACT(number)

*   _number_ - The number to get the factorial of.

Using the FACT function 
------------------------

The Excel FACT function returns the factorial of a given number. In mathematics, the factorial of a non-negative integer **n** is the product of all positive integers less than or equal to **n**, represented with the syntax **n!**

FACT takes just one [argument](https://exceljet.net/glossary/function-argument)
, _number_, which should be a positive integer. If _number_ is not an integer, the decimal portion of _number_ will be removed before the factorial is calculated.

### Examples

    =FACT(3) // returns 6
    =FACT(4) // returns 24
    =FACT(5) // returns 120
    

If _number_ is not an integer it will be truncated to an integer:

    =FACT(3.2) // returns 6
    

When number is zero, FACT returns 1:

    =FACT(0) // returns 1
    

If number is negative, FACT returns the #NUM! error:

    =FACT(-3) // returns  #NUM!
    

### Notes

*   _Number_ cannot be negative or FACT will return the #NUM error.
*   If _number_ is not an integer it will be truncated to an integer, then solved.

Related functions
-----------------

[![Excel COMBIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20combin.png "Excel COMBIN function")](https://exceljet.net/functions/combin-function)

### [COMBIN Function](https://exceljet.net/functions/combin-function)

The Excel COMBIN function returns the number of combinations for a given number of items. The COMBIN function _does not_ allow repetitions. To count combinations that _allow_ repetitions, use the [COMBINA function](https://exceljet.net/functions/combina-function)
.

[![Excel PERMUT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20permut.png "Excel PERMUT function")](https://exceljet.net/functions/permut-function)

### [PERMUT Function](https://exceljet.net/functions/permut-function)

The Excel PERMUT function returns the number of permutations (combinations where order is significant) for a given number of items. The PERMUT function _does not_ allow repetitions. To allow permutations with repetitions, use the [PERMUTATIONA](https://exceljet.net/functions/permutationa-function)
...

[![Excel FACTDOUBLE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_factdouble_function.png "Excel FACTDOUBLE function")](https://exceljet.net/functions/factdouble-function)

### [FACTDOUBLE Function](https://exceljet.net/functions/factdouble-function)

The Excel FACTDOUBLE function returns the double factorial of a number. A double factorial is symbolized by two exclamation marks (!!).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COMBIN Function](https://exceljet.net/functions/combin-function)
    
*   [PERMUT Function](https://exceljet.net/functions/permut-function)
    
*   [FACTDOUBLE Function](https://exceljet.net/functions/factdouble-function)
    

### Links

*   [Microsoft FACT function documentation](https://support.office.com/en-us/article/fact-function-ca8588c2-15f2-41c0-8e8c-c11bd471a4f3)
    

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