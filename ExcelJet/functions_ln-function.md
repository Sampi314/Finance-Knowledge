# Excel LN function | Exceljet

**Source:** https://exceljet.net/functions/ln-function

---

[Skip to main content](https://exceljet.net/functions/ln-function#main-content)

[](https://exceljet.net/functions/ln-function#)

*   [Previous](https://exceljet.net/functions/lcm-function)
    
*   [Next](https://exceljet.net/functions/log-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

LN Function
===========

by Dave Bruns · Updated 13 Sep 2021

Related functions 
------------------

[LOG](https://exceljet.net/functions/log-function)

[EXP](https://exceljet.net/functions/exp-function)

![Excel LN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_ln1.png "Excel LN function")

Summary
-------

The Excel LN function returns the natural logarithm of a given number.

Purpose 
--------

Get the natural logarithm of a number

Return value 
-------------

The natural logarithm

Syntax
------

    =LN(number)

*   _number_ - A number to take the natural logarithm of.

Using the LN function 
----------------------

The LN function returns the natural logarithm of a given number. The natural logarithm is equivalent to log base _e_ of a number, where _e_ is [Euler's number](https://en.wikipedia.org/wiki/E_(mathematical_constant))
, a mathematical constant  with the approximate value 2.71828182845904. The LN function is the inverse of the [EXP function](https://exceljet.net/functions/exp-function)
 and is used to model exponential decay.

The LN function takes just one argument, _number_, which should be a positive number.

### Examples

    =LN(1) // returns 0
    =LN(e) // returns 1
    =LN(e^2) // returns 2

The equivalent form of the natural logarithm function is given by:

    =LN(number)=LOG(number,e) // Where e ≈ 2.7128 or EXP(1)
    

### Graphs

Below is a graph of the natural log logarithm:

![Graph of the natural logarithm function.](https://exceljet.net/sites/default/files/images/functions/inline/natural-logarithm-function.png "Graph of the natural logarithm function.")

The natural logarithm function and exponential function are the inverse of each other, as you can see in the graph below:

![Graph of the natural logarithm and exponential function.](https://exceljet.net/sites/default/files/images/functions/inline/exponential-and-logarithm-function-graph.png "Graph of the natural logarithm and exponential function.")

This inverse relationship can be represented with the formulas below, where the input to the LN function is the output of the [EXP function](https://exceljet.net/functions/exp-function)
:

    = LN(EXP(1)) // returns 1
    = LN(EXP(2)) // returns 2
    = LN(EXP(n)) // returns n
    

See [wumbo.net](https://wumbo.net/)
 for a more detailed explanation of key math concepts and formulas. 

### Notes

*   The natural logarithm function can be defined as the area under a hyperbola. 
*   The function is used in applications relating to compound interest.

Related functions
-----------------

[![Excel LOG function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_log_new.png "Excel LOG function")](https://exceljet.net/functions/log-function)

### [LOG Function](https://exceljet.net/functions/log-function)

The Excel LOG function returns the logarithm of a given number, using a supplied base. The base argument defaults to 10 if not supplied.

[![Excel EXP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_exp.png "Excel EXP function")](https://exceljet.net/functions/exp-function)

### [EXP Function](https://exceljet.net/functions/exp-function)

The Excel EXP function returns the result of the constant e raised to the power of a number. The constant e is a numeric constant relating to exponential growth and decay whose value is approximately 2.71828. The EXP function is the inverse of the [LN (natural](https://exceljet.net/functions/ln-function)
...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [LOG Function](https://exceljet.net/functions/log-function)
    
*   [EXP Function](https://exceljet.net/functions/exp-function)
    

### Links

*   [Microsoft LN function documentation](https://support.office.com/en-us/article/ln-function-81fe1ed7-dac9-4acd-ba1d-07a142c6118f)
    

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