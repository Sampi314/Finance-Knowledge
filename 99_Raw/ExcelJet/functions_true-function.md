# Excel TRUE function | Exceljet

**Source:** https://exceljet.net/functions/true-function

---

[Skip to main content](https://exceljet.net/functions/true-function#main-content)

[](https://exceljet.net/functions/true-function#)

*   [Previous](https://exceljet.net/functions/switch-function)
    
*   [Next](https://exceljet.net/functions/xor-function)
    

Excel 2003

[Logical](https://exceljet.net/functions#Logical)

TRUE Function
=============

by Dave Bruns · Updated 25 May 2021

Related functions 
------------------

[FALSE](https://exceljet.net/functions/false-function)

[IF](https://exceljet.net/functions/if-function)

![Excel TRUE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20true.png "Excel TRUE function")

Summary
-------

The Excel TRUE function returns the Boolean value TRUE. The TRUE function is classified as a "compatibility function", needed only for compatibility with other spreadsheet applications. There is no need to use TRUE() if you are creating a spreadsheet in Excel.

Purpose 
--------

Generate the logical value TRUE

Return value 
-------------

The logical value TRUE

Syntax
------

    =TRUE()

Using the TRUE function 
------------------------

The TRUE function returns the Boolean value TRUE. In other words, the two formulas below based on the [IF function](https://exceljet.net/functions/if-function)
 are functionally equivalent:

    =IF(A1>65,TRUE())
    =IF(A1>65,TRUE)
    

Both formulas return TRUE if the value in A1 is greater than 65.

The TRUE function is provided for compatibility with other spreadsheet applications and there is no need to use it if you are creating a spreadsheet in Excel. To return TRUE as a result in a formula, just enter TRUE directly into a cell or formula. 

Note that [logical expressions](https://exceljet.net/glossary/logical-test)
 will automatically generate TRUE and FALSE results. For example, the formula below will TRUE or FALSE:

    =A1>90
    

To test a condition and return different results based on whether the results are TRUE or FALSE, [see the examples on this page](https://exceljet.net/functions/if-function)
.

Related functions
-----------------

[![Excel FALSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20false.png "Excel FALSE function")](https://exceljet.net/functions/false-function)

### [FALSE Function](https://exceljet.net/functions/false-function)

The Excel FALSE function returns the Boolean value FALSE.  The FALSE function is classified as a "compatibility function", needed only for compatibility with other spreadsheet applications. There is no need to use FALSE() if you are creating a spreadsheet in Excel.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FALSE Function](https://exceljet.net/functions/false-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

### Links

*   [Microsoft TRUE function documentation](https://support.office.com/en-us/article/true-function-7652c6e3-8987-48d0-97cd-ef223246b3fb)
    

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