# Excel PERMUT function | Exceljet

**Source:** https://exceljet.net/functions/permut-function

---

[Skip to main content](https://exceljet.net/functions/permut-function#main-content)

[](https://exceljet.net/functions/permut-function#)

*   [Previous](https://exceljet.net/functions/percentrank.inc-function)
    
*   [Next](https://exceljet.net/functions/permutationa-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

PERMUT Function
===============

by Dave Bruns · Updated 29 Nov 2021

Related functions 
------------------

[COMBIN](https://exceljet.net/functions/combin-function)

[COMBINA](https://exceljet.net/functions/combina-function)

[PERMUT](https://exceljet.net/functions/permut-function)

[PERMUTATIONA](https://exceljet.net/functions/permutationa-function)

[FACT](https://exceljet.net/functions/fact-function)

![Excel PERMUT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20permut.png "Excel PERMUT function")

Summary
-------

The Excel PERMUT function returns the number of permutations (combinations where order is significant) for a given number of items. The PERMUT function _does not_ allow repetitions. To allow permutations with repetitions, use the [PERMUTATIONA function](https://exceljet.net/functions/permutationa-function)
.

Purpose 
--------

Get number of permutations without repetitions

Return value 
-------------

Number of permutations as an integer

Syntax
------

    =PERMUT(number,number_chosen)

*   _number_ - The total number of items.
*   _number\_chosen_ - The number of items in each combination.

Using the PERMUT function 
--------------------------

The PERMUT function returns the number of permutations for a given number of items. A permutation is a combination where order matters. In other words, a permutation is an ordered combination.

There are two types of permutations:

1.  Permutations where repetition _is not_ allowed (i.e. 123)
2.  Permutations where repetition _is_ allowed (i.e. 333)

The PERMUT function calculates permutations where repetitions are not allowed. To calculate permutations where repetitions are allowed, use the [PERMUTATIONA function](https://exceljet.net/functions/permutationa-function)
.

### Example

To use PERMUT, specify the total number of items and "_number\_chosen_", which represents the number of items in each combination. For example, to calculate 3-number permutations for the numbers 0-9, there are 10 numbers and 3 chosen, so the formula is:

    =PERMUT(10,3) // returns 720
    

This result can be seen in cell D8 in the example shown.

### Notes

*   A permutation is a group of items in which order/sequence _matters_.
*   If order is not significant, see the [COMBIN function](https://exceljet.net/functions/combin-function)
    .
*   Arguments that contain decimal values are truncated to integers.
*   PERMUT returns a #VALUE! error value if either argument is not numeric.
*   PERMUT returns #NUM! if _number_ is less than _number\_chosen._

Related functions
-----------------

[![Excel COMBIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20combin.png "Excel COMBIN function")](https://exceljet.net/functions/combin-function)

### [COMBIN Function](https://exceljet.net/functions/combin-function)

The Excel COMBIN function returns the number of combinations for a given number of items. The COMBIN function _does not_ allow repetitions. To count combinations that _allow_ repetitions, use the [COMBINA function](https://exceljet.net/functions/combina-function)
.

[![Excel COMBINA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20combina.png "Excel COMBINA function")](https://exceljet.net/functions/combina-function)

### [COMBINA Function](https://exceljet.net/functions/combina-function)

The Excel COMBINA function returns the number of combinations with repetitions _allowed_. To count combinations that _do not_ allow repetitions, use the [COMBIN function](https://exceljet.net/functions/combin-function)
.

[![Excel PERMUT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20permut.png "Excel PERMUT function")](https://exceljet.net/functions/permut-function)

### [PERMUT Function](https://exceljet.net/functions/permut-function)

The Excel PERMUT function returns the number of permutations (combinations where order is significant) for a given number of items. The PERMUT function _does not_ allow repetitions. To allow permutations with repetitions, use the [PERMUTATIONA](https://exceljet.net/functions/permutationa-function)
...

[![Excel PERMUTATIONA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20permutationa.png "Excel PERMUTATIONA function")](https://exceljet.net/functions/permutationa-function)

### [PERMUTATIONA Function](https://exceljet.net/functions/permutationa-function)

The Excel PERMUTATIONA function returns the number of permutations (combinations where order is significant) for a given number of items. The PERMUTATIONA function _allows_ repetitions. To calculate the number of permutations _without_ repetitions, use the...

[![Excel FACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fact.png "Excel FACT function")](https://exceljet.net/functions/fact-function)

### [FACT Function](https://exceljet.net/functions/fact-function)

The Excel FACT function returns the factorial of a given number. For example, =FACT(3) returns 6, equivalent to 3 x 2 x 1.

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
    
*   [COMBINA Function](https://exceljet.net/functions/combina-function)
    
*   [PERMUT Function](https://exceljet.net/functions/permut-function)
    
*   [PERMUTATIONA Function](https://exceljet.net/functions/permutationa-function)
    
*   [FACT Function](https://exceljet.net/functions/fact-function)
    

### Links

*   [Microsoft PERMUT function documentation](https://support.office.com/en-us/article/permut-function-3bd1cb9a-2880-41ab-a197-f246a7a602d3)
    

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