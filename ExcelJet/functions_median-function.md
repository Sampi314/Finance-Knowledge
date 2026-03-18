# Excel MEDIAN function | Exceljet

**Source:** https://exceljet.net/functions/median-function

---

[Skip to main content](https://exceljet.net/functions/median-function#main-content)

[](https://exceljet.net/functions/median-function#)

*   [Previous](https://exceljet.net/functions/maxifs-function)
    
*   [Next](https://exceljet.net/functions/min-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

MEDIAN Function
===============

by Dave Bruns · Updated 24 Nov 2021

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[MODE](https://exceljet.net/functions/mode-function)

![Excel MEDIAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20median%20function.png "Excel MEDIAN function")

Summary
-------

The Excel MEDIAN function returns the median (middle number) in the supplied set of data. For example, =MEDIAN(1,2,3,4,5) returns 3.

Purpose 
--------

Get the median of a group of numbers

Return value 
-------------

A number representing the median.

Syntax
------

    =MEDIAN(number1,[number2],...)

*   _number1_ - A number or cell reference that refers to numeric values.
*   _number2_ - \[optional\] A number or cell reference that refers to numeric values.

Using the MEDIAN function 
--------------------------

The MEDIAN function returns the median (middle number) in a set of data. The calculation performed by MEDIAN varies according to the number of numeric values provided. When the number is odd, MEDIAN returns the middle number in the group. When the number is even, MEDIAN returns the average of the two numbers in the middle. 

The MEDIAN function takes multiple [arguments](https://exceljet.net/glossary/function-argument)
 in the form _number1_, _number2_, _number3_, etc. Arguments can be a hardcoded constant, a cell reference, or a range, in any combination. MEDIAN ignores empty cells, text values, and the logical values TRUE and FALSE. The MEDIAN function will accept up to 255 separate arguments. 

### Examples

When the number of values provided is odd, MEDIAN returns the middle number:

    =MEDIAN(1,2,3,4,5) // returns 3
    =MEDIAN(1,4,5,7,11) // returns 5
    

When the number of values provided is even, MEDIAN returns the average of the two middle numbers:

    =MEDIAN(1,2,3,4,5,6) // returns 3.5
    =MEDIAN(1,2,4,6,8,9) // returns 9
    

In the worksheet shown above, the formulas in H5 and H6 are:

    =MEDIAN(B5:B16) // returns 83.5
    =MEDIAN(D5:D16) // returns 80
    

Note that MEDIAN ignores the empty cell in D5:D16 and returns the middle number in the eleven values provided.

### Notes

*   When the count of numbers is odd, MEDIAN returns the middle number.
*   When the count of numbers is even, MEDIAN returns the average of the two middle numbers.
*   MEDIAN ignores empty cells, the logical values TRUE and FALSE, and [text](https://exceljet.net/glossary/text-value)
    .
*   MEDIAN returns a #NUM! error if no numeric values are provided.
*   Arguments can be numbers, names, [arrays](https://exceljet.net/glossary/array)
    , or references, up to 255 total.

MEDIAN function examples
------------------------

[![Excel formula: Cap percentage between 0 and 100](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20between%200%20and%20100.png "Excel formula: Cap percentage between 0 and 100")](https://exceljet.net/formulas/cap-percentage-between-0-and-100)

### [Cap percentage between 0 and 100](https://exceljet.net/formulas/cap-percentage-between-0-and-100)

In order to understand this problem, make sure you understand how percentage number formatting works . In a nutshell, percentages are decimal values: 0.1 is 10%, 0.2 is 20%, and so on. The number 1, when formatted as a percentage, is 100%. More on number formats here . The goal of this example is...

[![Excel formula: Conditional median with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20median%20with%20criteria.png "Excel formula: Conditional median with criteria")](https://exceljet.net/formulas/conditional-median-with-criteria)

### [Conditional median with criteria](https://exceljet.net/formulas/conditional-median-with-criteria)

The MEDIAN function has no built-in way to apply criteria. Given a range, it will return the MEDIAN (middle) number in that range. To apply criteria, we use the IF function inside MEDIAN to "filter" values. In this example, the IF function filters by group like this: IF(group=E5,data) This...

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel MODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")](https://exceljet.net/functions/mode-function)

### [MODE Function](https://exceljet.net/functions/mode-function)

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Conditional median with criteria](https://exceljet.net/formulas/conditional-median-with-criteria)
    
*   [Cap percentage between 0 and 100](https://exceljet.net/formulas/cap-percentage-between-0-and-100)
    

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [MODE Function](https://exceljet.net/functions/mode-function)
    

### Links

*   [Microsoft MEDIAN function documentation](https://support.office.com/en-us/article/median-function-d0916313-4753-414c-8537-ce85bdd967d2)
    

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