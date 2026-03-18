# Count cells that contain negative numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-negative-numbers

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-n-characters)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-numbers)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain negative numbers
=========================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count cells that contain negative numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20negative%20numbers.png "Excel formula: Count cells that contain negative numbers")

Summary
-------

To count the number of cells that contain negative numbers in a [range](https://exceljet.net/glossary/range)
, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, cell E6 contains this formula:

    =COUNTIF(data,"<0")
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The result is 3, since there are three cells in B5:B15 that contain numbers less than zero.

Generic formula
---------------

    =COUNTIF(range,"<0")

Explanation 
------------

In this example, the goal is to count the number of cells in a range that contain negative numbers. For convenience, the range B5:B15 is [named](https://exceljet.net/glossary/named-range)
 **data**. This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both methods are explained below.

### COUNTIF function

The [COUNT function](https://exceljet.net/functions/countif-function)
 counts the number of cells in a range that match the supplied criteria. For example, you can use COUNTIF like this:

    =COUNTIF(range,"red") // count cells equal to "red"
    =COUNTIF(range,100) // count cells equal to 100
    =COUNTIF(range,">10") // count cells greater than 10
    

To count negative numbers in this example, we need to use the less than [operator](https://exceljet.net/glossary/logical-operators)
 (<) with zero like this:

    =COUNTIF(data,"<0") // returns 3
    

To include zero in the count, use the less than or equal to operator (>=):

    =COUNTIF(data,"<=0") // returns 4
    

Notice that the _criteria_ is enclosed in double quotes (""). COUNTIFS is in a [group of eight functions](https://exceljet.net/articles/excels-racon-functions)
 that share this syntax.

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
:

    =SUMPRODUCT(--(data<0))
    

Working from the inside out, this expression checks if values in **data** (B5:B15) are less than zero:

    data<0
    

Because **data** contains eleven cells, the result from this expression is an [array](https://exceljet.net/glossary/array)
 that contains 11 TRUE and FALSE values:

    {FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE}
    

To convert the TRUE and FALSE values to 1s and 0s, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --{FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE}
    

The resulting array inside the SUMPRODUCT function looks like this:

    =SUMPRODUCT({0;0;0;1;0;0;1;0;1;0;0}) // returns 3
    

With a single array to process, SUMPRODUCT sums the array and returns 3 as the result.

Related formulas
----------------

[![Excel formula: Count cells that contain positive numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cell%20that%20contain%20positive%20numbers.png "Excel formula: Count cells that contain positive numbers")](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)

### [Count cells that contain positive numbers](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)

In this example, the goal is to count the number of cells in a range that contain positive numbers. For convenience, the range B5:B15 is named data . This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both methods are explained below. COUNTIF function The COUNT...

[![Excel formula: Count cells that contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20errors.png "Excel formula: Count cells that contain errors")](https://exceljet.net/formulas/count-cells-that-contain-errors)

### [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)

In this example, the goal is to count errors in the range B5:B15, which is named data for convenience. The article below explains several different approaches, depending on your needs. For background, this article: Excel Formula Errors . COUNTIF function One way to count individual errors is with...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain positive numbers](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)
    
*   [Count cells that contain errors](https://exceljet.net/formulas/count-cells-that-contain-errors)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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