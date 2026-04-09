# nth root of number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nth-root-of-number

---

[Skip to main content](https://exceljet.net/formulas/nth-root-of-number#main-content)

[](https://exceljet.net/formulas/nth-root-of-number#)

*   [Previous](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)
    
*   [Next](https://exceljet.net/formulas/number-is-whole-number)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

nth root of number
==================

by Dave Bruns · Updated 5 Oct 2020

Related functions 
------------------

[POWER](https://exceljet.net/functions/power-function)

![Excel formula: nth root of number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nth%20root%20of%20number.png "Excel formula: nth root of number")

Summary
-------

To get the nth root of a number, you can use the caret(^) operator with 1/n as the exponent in a simple formula, or you can use the [POWER function](https://exceljet.net/functions/power-function)
. In the example shown, the formula in D5 is:

    =B5^(1/C5)
    

Generic formula
---------------

    =number^(1/n)

Explanation 
------------

By definition, the nth root of a number can be calculated by raising that number to the power of 1/n. Exponents are entered using the [exponentiation operator](https://exceljet.net/glossary/math-operators)
 (^), with a number on the left and power on the right. So, in this example we get the numbers from column B and powers from column C:

    =B5^(1/C5)
    

### With the POWER function

The [POWER function](https://exceljet.net/functions/power-function)
 is another way to perform exponentiation in Excel. To get the nth root of a number with POWER, use the number with 1/n for the _power_ argument:

    =POWER(number,1/n)
    

So for the example shown, the formula in D5 would be:

    =POWER(B5,1/C5)
    

Related formulas
----------------

[![Excel formula: Square root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/square%20root.png "Excel formula: Square root of number")](https://exceljet.net/formulas/square-root-of-number)

### [Square root of number](https://exceljet.net/formulas/square-root-of-number)

The SQRT function is fully automatic and will return the square root of any positive number. For example, to get the square root of 25, you can use: =SQRT(25) // returns 5 To get the square root of 16: =SQRT(16) // returns 4 To get the square root of a number in cell A1: =SQRT(A1) // square root of...

[![Excel formula: Cube root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cube%20root%20of%20number.png "Excel formula: Cube root of number")](https://exceljet.net/formulas/cube-root-of-number)

### [Cube root of number](https://exceljet.net/formulas/cube-root-of-number)

The cube root of a number can be calculated manually with the exponentiation operator (^) or with the POWER function . Manually with ^ The cube root of a number can be calculated manually by raising a number to the (1/3) using the exponentiation operator (^). In the example shown, the formula in C5...

[![Excel formula: Square root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/square%20root.png "Excel formula: Square root of number")](https://exceljet.net/formulas/square-root-of-number)

### [Square root of number](https://exceljet.net/formulas/square-root-of-number)

The SQRT function is fully automatic and will return the square root of any positive number. For example, to get the square root of 25, you can use: =SQRT(25) // returns 5 To get the square root of 16: =SQRT(16) // returns 4 To get the square root of a number in cell A1: =SQRT(A1) // square root of...

Related functions
-----------------

[![Excel POWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20power%20function.png "Excel POWER function")](https://exceljet.net/functions/power-function)

### [POWER Function](https://exceljet.net/functions/power-function)

The Excel POWER function returns a number raised to a given power. The POWER function is an alternative to the [exponent operator](https://exceljet.net/glossary/math-operators)
 (^).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Square root of number](https://exceljet.net/formulas/square-root-of-number)
    
*   [Cube root of number](https://exceljet.net/formulas/cube-root-of-number)
    
*   [Square root of number](https://exceljet.net/formulas/square-root-of-number)
    

### Functions

*   [POWER Function](https://exceljet.net/functions/power-function)
    

### Links

*   [Rational exponents and radicals (Kahn Academy)](https://www.khanacademy.org/math/algebra/rational-exponents-and-radicals/rational-exponents-intro/v/basic-fractional-exponents)
    

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