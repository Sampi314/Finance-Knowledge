# Excel MAXA function | Exceljet

**Source:** https://exceljet.net/functions/maxa-function

---

[Skip to main content](https://exceljet.net/functions/maxa-function#main-content)

[](https://exceljet.net/functions/maxa-function#)

*   [Previous](https://exceljet.net/functions/max-function)
    
*   [Next](https://exceljet.net/functions/maxifs-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

MAXA Function
=============

by Dave Bruns · Updated 13 Oct 2021

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[MINA](https://exceljet.net/functions/mina-function)

[SMALL](https://exceljet.net/functions/small-function)

[RANK](https://exceljet.net/functions/rank-function)

![Excel MAXA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20maxa%20function.png "Excel MAXA function")

Summary
-------

The Excel MAXA function returns the largest numeric value in a range of values. The MAXA function ignores empty cells, but evaluates the logical values TRUE and FALSE as 1 and 0, and evaluates text as zero.

Purpose 
--------

Return largest value.

Return value 
-------------

Largest numeric value

Syntax
------

    =MAXA(value1,[value2],...)

*   _value1_ - Number, reference to numeric value, or range that contains numeric values.
*   _value2_ - \[optional\] Number, reference to numeric value, or range that contains numeric values.

Using the MAXA function 
------------------------

The MAXA function returns the largest numeric value in a range of values. Like the [MAX function](https://exceljet.net/functions/max-function)
, MAXA ignores empty cells. However, _unlike_ the MAX function, MAXA evaluates the logical values TRUE and FALSE as 1 and 0, and evaluates text as zero when these values appear in a [range](https://exceljet.net/glossary/range)
 or cell reference.

The MAXA function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a range, in any combination. 

### Examples

Like the [MAX function](https://exceljet.net/functions/max-function)
, the MAXA function returns the largest number in the supplied data:

    =MAX(12,17,25,11,23) // returns 25
    =MAXA(12,17,25,11,23) // returns 25
    

MAXA can be used with constants, cell references, or ranges:

    =MAXA(5,10)
    =MAXA(A1,A2,A3)
    =MAXA(A1:A10)
    

### MAXA vs. MAX

The primary difference between MAX and MAXA is that MAXA evaluates TRUE and FALSE values as 1 and 0, and text values as zero when these values appear in a range or in a cell reference. You can see this behavior in the range I7:I12 of the example shown. While the MAX function _ignores_ the logical and text values completely, the MAXA function _includes_ these values when calculating a maximum value.

Note that MAX and MAXA _both_ evaluate numbers as text when supplied directly as arguments:

    =MAXA(5,"10") // returns 10
    =MAX(5,"10") // also returns 10
    

### Notes

*   MAXA ignores empty cells, but evaluates logical values and text values.
*   Arguments can be provided as numbers, names, arrays, or references.
*   If arguments contain no numeric values, MAXA returns 0.
*   To ignore logical values and text, see the [MAX function](https://exceljet.net/functions/max-function)
    .

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MINA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mina%20function.png "Excel MINA function")](https://exceljet.net/functions/mina-function)

### [MINA Function](https://exceljet.net/functions/mina-function)

The Excel MINA function returns the smallest numeric value in a range of values. The MINA function ignores empty cells, but evaluates the logical values TRUE and FALSE as 1 and 0, and evaluates text as zero when these values appear in a [range](https://exceljet.net/glossary/range)
 or cell reference.

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

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MINA Function](https://exceljet.net/functions/mina-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    

### Links

*   [Microsoft MAXA function documentation](https://support.office.com/en-us/article/maxa-function-814bda1e-3840-4bff-9365-2f59ac2ee62d)
    

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