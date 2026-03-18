# Excel SUMSQ function | Exceljet

**Source:** https://exceljet.net/functions/sumsq-function

---

[Skip to main content](https://exceljet.net/functions/sumsq-function#main-content)

[](https://exceljet.net/functions/sumsq-function#)

*   [Previous](https://exceljet.net/functions/sumproduct-function)
    
*   [Next](https://exceljet.net/functions/sumx2my2-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SUMSQ Function
==============

by Dave Bruns · Updated 17 Sep 2021

Related functions 
------------------

[SUMSQ](https://exceljet.net/functions/sumsq-function)

[SUMX2MY2](https://exceljet.net/functions/sumx2my2-function)

[SUMX2PY2](https://exceljet.net/functions/sumx2py2-function)

[SUMXMY2](https://exceljet.net/functions/sumxmy2-function)

![Excel SUMSQ function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sumsq%20function_0.png "Excel SUMSQ function")

Summary
-------

The Excel SUMSQ function returns the sum of the squares of the values provided. Values can be supplied as constants, cell references, or ranges.

Purpose 
--------

Get sum of squares of supplied values

Return value 
-------------

Calculated sum of squares

Syntax
------

    =SUMSQ(number1,[number2],...)

*   _number1_ - The first argument containing numeric values.
*   _number2_ - \[optional\] The first argument containing numeric values.

Using the SUMSQ function 
-------------------------

The SUMSQ function returns the sum of the squares of the numbers provided. SUMSQ takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a [range](https://exceljet.net/glossary/range)
. All numbers in the arguments provided are squared then summed. The SUMSQ function automatically ignores empty cells and text values.

### Examples

    =SUMSQ(1,2) // returns 5
    =SUMSQ(1,2,3) // returns 14
    =SUMSQ({1,2,3}) // returns 14
    

In the worksheet shown, the formula in H5, copied down, is:

    =SUMSQ(B5:F5) // returns 5
    

Notice that SUMSQ automatically ignores empty cells and text values.

### Notes

*   Arguments can be a mix of constants, names, arrays, or references that contain numbers.
*   Empty cells, logical values, and text values are ignored when they appear in arrays or references.
*   The logical values TRUE and FALSE are evaluated as 1 and 0 respectively, but only when they are hardcoded as arguments.
*   Numbers entered as text (i.e. "1", "3", etc.) are evaluated, but only when they are hardcoded as arguments.

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

*   [Microsoft SUMSQ function documentation](https://support.office.com/en-us/article/sumsq-function-e3313c02-51cc-4963-aae6-31442d9ec307)
    

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