# Basic error trapping example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-error-trapping-example

---

[Skip to main content](https://exceljet.net/formulas/basic-error-trapping-example#main-content)

[](https://exceljet.net/formulas/basic-error-trapping-example#)

*   [Previous](https://exceljet.net/formulas/basic-attendance-tracking-formula)
    
*   [Next](https://exceljet.net/formulas/basic-in-cell-histogram)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Basic error trapping example
============================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[IFERROR](https://exceljet.net/functions/iferror-function)

![Excel formula: Basic error trapping example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20error%20trapping%20example.png "Excel formula: Basic error trapping example")

Summary
-------

To catch errors that a formula might encounter in a worksheet, you can use the IFERROR function to display a custom message, or nothing at all. In the example shown, the formula in E5 is:

    =IFERROR(C5/D5,"")
    

If C5/D5 returns a value, that value is returned. If C5/D5 returns an error, IFERROR returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

Generic formula
---------------

    =IFERROR(formula,value_if_error)

Explanation 
------------

In this example, the IFERROR function is used to trap and suppress the #DIV/0! error that occurs when there is no value for Orders (column D). Without IFERROR, the formula C5/D5 would display a #DIV/0! error in E6 and E9.

The IFERROR function takes two arguments: a value (usually entered as a formula), and a result to display if the formula returns an error. The second argument is only used if the first argument throws an error.

In this case, the first argument is the simple formula for calculating the average order size, which divides total sales by the order count:

    =C5/D5
    

The second argument is entered as an empty string (""). When the formula returns a normal result, the result is displayed. When the formula returns #DIV/0!, an [empty string](https://exceljet.net/glossary/empty-string)
 is returned and nothing is displayed.

Related formulas
----------------

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

Related functions
-----------------

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    

### Functions

*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    

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