# Excel SUMX2MY2 function | Exceljet

**Source:** https://exceljet.net/functions/sumx2my2-function

---

[Skip to main content](https://exceljet.net/functions/sumx2my2-function#main-content)

[](https://exceljet.net/functions/sumx2my2-function#)

*   [Previous](https://exceljet.net/functions/sumsq-function)
    
*   [Next](https://exceljet.net/functions/sumx2py2-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SUMX2MY2 Function
=================

by Dave Bruns · Updated 17 Sep 2021

Related functions 
------------------

[SUMSQ](https://exceljet.net/functions/sumsq-function)

[SUMX2MY2](https://exceljet.net/functions/sumx2my2-function)

[SUMX2PY2](https://exceljet.net/functions/sumx2py2-function)

[SUMXMY2](https://exceljet.net/functions/sumxmy2-function)

![Excel SUMX2MY2 function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sumx2my2.png "Excel SUMX2MY2 function")

Summary
-------

The Excel SUMX2PY2 function returns the sum of the difference of squares of corresponding values in two arrays. Values can be supplied as constants, cell references, or ranges.

Purpose 
--------

Sum of difference of squares in two arrays

Return value 
-------------

Calculated sum of difference of squares

Syntax
------

    =SUMX2MY2(array_x,array_y)

*   _array\_x_ - The first range or array containing numeric values.
*   _array\_y_ - The second range or array containing numeric values.

Using the SUMX2MY2 function 
----------------------------

The SUMX2MY2 function returns the sum of the difference of squares of corresponding values in two arrays. The "m" in the function name stands for "minus", as in "sum x2 _minus_ y2". 

SUMX2MY2 takes two [arguments](https://exceljet.net/glossary/function-argument)
, _array\_x_ and _array\_y_. _Array\_x_ is the first range or array or range of numbers, and _array\_y_ is the second range or array of numbers. Both arguments can be provided as an [array constant](https://exceljet.net/glossary/array-constant)
 or as a [range](https://exceljet.net/glossary/range)
.

### Examples

    =SUMX2MY2({0,1},{1,2}) // returns -4
    =SUMX2MY2({1,2,3},{1,2,3}) // returns 0
    

In the example shown above, the formula in E5 is:

    =SUMX2MY2(B5:B12,C5:C12)
    

which returns -144 as a result.

### Equation

The equation used to calculate the sum of squares is:

This formula can be created manually in Excel with the exponentiation [operator](https://exceljet.net/glossary/math-operators)
 (^) like this:

    =SUM((range1^2)-(range2^2))
    

With the example as shown, the formula below will return the same result as SUMX2MY2:

    =SUM((B5:B12^2)+(C5:C12^2)) // returns -144
    

### Notes

*   Arguments can be a mix of constants, names, arrays, or references that contain numbers.
*   Text values are ignored, but cells with zero values are included.
*   SUMX2MY2 returns #N/A if the arrays contain different numbers of cells.

Related functions
-----------------

[![Excel SUMSQ function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumsq%20function_0.png "Excel SUMSQ function")](https://exceljet.net/functions/sumsq-function)

### [SUMSQ Function](https://exceljet.net/functions/sumsq-function)

The Excel SUMSQ function returns the sum of the squares of the values provided. Values can be supplied as constants, cell references, or ranges.

[![Excel SUMX2MY2 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumx2my2.png "Excel SUMX2MY2 function")](https://exceljet.net/functions/sumx2my2-function)

### [SUMX2MY2 Function](https://exceljet.net/functions/sumx2my2-function)

The Excel SUMX2PY2 function returns the sum of the difference of squares of corresponding values in two arrays. Values can be supplied as constants, cell references, or ranges.

[![Excel SUMX2PY2 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumx2py2.png "Excel SUMX2PY2 function")](https://exceljet.net/functions/sumx2py2-function)

### [SUMX2PY2 Function](https://exceljet.net/functions/sumx2py2-function)

The Excel SUMX2PY2 function returns the sum of the sum of squares of corresponding values in two arrays. Values can be supplied as constants, cell references, or ranges.

[![Excel SUMXMY2 function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumxmy2.png "Excel SUMXMY2 function")](https://exceljet.net/functions/sumxmy2-function)

### [SUMXMY2 Function](https://exceljet.net/functions/sumxmy2-function)

The Excel SUMXMY2 function returns the sum of squares of differences between corresponding values in two arrays. Values can be supplied as constants, cell references, or ranges.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SUMSQ Function](https://exceljet.net/functions/sumsq-function)
    
*   [SUMX2MY2 Function](https://exceljet.net/functions/sumx2my2-function)
    
*   [SUMX2PY2 Function](https://exceljet.net/functions/sumx2py2-function)
    
*   [SUMXMY2 Function](https://exceljet.net/functions/sumxmy2-function)
    

### Links

*   [Microsoft SUMX2MY2 function documentation](https://support.office.com/en-us/article/sumx2my2-function-9e599cc5-5399-48e9-a5e0-e37812dfa3e9)
    

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