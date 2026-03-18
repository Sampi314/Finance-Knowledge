# Excel MINA function | Exceljet

**Source:** https://exceljet.net/functions/mina-function

---

[Skip to main content](https://exceljet.net/functions/mina-function#main-content)

[](https://exceljet.net/functions/mina-function#)

*   [Previous](https://exceljet.net/functions/min-function)
    
*   [Next](https://exceljet.net/functions/minifs-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

MINA Function
=============

by Dave Bruns · Updated 13 Oct 2021

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

[MAXA](https://exceljet.net/functions/maxa-function)

[SMALL](https://exceljet.net/functions/small-function)

[RANK](https://exceljet.net/functions/rank-function)

![Excel MINA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20mina%20function.png "Excel MINA function")

Summary
-------

The Excel MINA function returns the smallest numeric value in a range of values. The MINA function ignores empty cells, but evaluates the logical values TRUE and FALSE as 1 and 0, and evaluates text as zero when these values appear in a [range](https://exceljet.net/glossary/range)
 or cell reference.

Purpose 
--------

Return smallest value.

Return value 
-------------

Smallest numeric value

Syntax
------

    =MINA(value1,[value2],...)

*   _value1_ - Number, reference to numeric value, or range that contains numeric values.
*   _value2_ - \[optional\] Number, reference to numeric value, or range that contains numeric values.

Using the MINA function 
------------------------

The MINA function returns the smallest numeric value in a range of values. Like the [MIN function](https://exceljet.net/functions/min-function)
, MINA ignores empty cells. However, _unlike_ the MIN function, MINA evaluates the logical values TRUE and FALSE as 1 and 0, and evaluates text as zero when these values appear in a [range](https://exceljet.net/glossary/range)
 or cell reference.

The MINA function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a range, in any combination. 

### Examples

Like the [MIN function](https://exceljet.net/functions/min-function)
, the MINA function returns the smallest number in the supplied data:

    =MIN(12,17,25,11,23) // returns 11
    =MINA(12,17,25,11,23) // returns 11
    

MINA can be used with constants, cell references, or ranges:

    =MINA(5,10)
    =MINA(A1,A2,A3)
    =MINA(A1:A10)
    

### MINA vs. MIN

The primary difference between MIN and MINA is that MINA evaluates TRUE and FALSE values as 1 and 0, and text values as zero when these values appear in a range or in a cell reference. You can see this behavior in the range I8:I12 of the example shown. While the MIN function _ignores_ the logical and text values completely, the MINA function _includes_ these values when calculating a minimum value.

Note that MIN and MINA _both_ evaluate numbers as text when supplied directly as arguments:

    =MINA(5,"3") // returns 3
    =MIN(5,"3") // returns 3
    

### Notes

*   MINA ignores empty cells, but evaluates logical values and text values.
*   Arguments can be provided as numbers, names, arrays, or references.
*   If arguments contain no numeric values, MINA returns 0.
*   To ignore logical values and text, see the [MIN function](https://exceljet.net/functions/min-function)
    .

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAXA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxa%20function.png "Excel MAXA function")](https://exceljet.net/functions/maxa-function)

### [MAXA Function](https://exceljet.net/functions/maxa-function)

The Excel MAXA function returns the largest numeric value in a range of values. The MAXA function ignores empty cells, but evaluates the logical values TRUE and FALSE as 1 and 0, and evaluates text as zero.

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MAXA Function](https://exceljet.net/functions/maxa-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    

### Links

*   [Microsoft MINA function documentation](https://support.office.com/en-us/article/mina-function-245a6f46-7ca5-4dc7-ab49-805341bc31d3)
    

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