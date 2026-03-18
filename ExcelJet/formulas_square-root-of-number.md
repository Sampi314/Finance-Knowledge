# Square root of number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/square-root-of-number

---

[Skip to main content](https://exceljet.net/formulas/square-root-of-number#main-content)

[](https://exceljet.net/formulas/square-root-of-number#)

*   [Previous](https://exceljet.net/formulas/split-payment-across-months)
    
*   [Next](https://exceljet.net/formulas/standard-deviation-calculation)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Square root of number
=====================

by Dave Bruns · Updated 20 Apr 2022

Related functions 
------------------

[SQRT](https://exceljet.net/functions/sqrt-function)

[POWER](https://exceljet.net/functions/power-function)

[ABS](https://exceljet.net/functions/abs-function)

![Excel formula: Square root of number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/square%20root.png "Excel formula: Square root of number")

Summary
-------

To calculate the square root of a number in Excel, you can use the [SQRT function](https://exceljet.net/functions/sqrt-function)
. In the example shown, the formula in C5 (copied down) is:

    =SQRT(B5)
    

The result is the square root of each number in column B.

Generic formula
---------------

    =SQRT(number)

Explanation 
------------

The [SQRT function](https://exceljet.net/functions/sqrt-function)
 is fully automatic and will return the square root of any positive number. For example, to get the square root of 25, you can use:

    =SQRT(25) // returns 5
    

To get the square root of 16:

    =SQRT(16)  // returns 4
    

To get the square root of a number in cell A1:

    =SQRT(A1) // square root of A1
    

### Negative numbers

If you give SQRT a negative number, it returns a #NUM! error:

    =SQRT(-4) // returns #NUM!
    

To use the SQRT function with negative numbers you [nest](https://exceljet.net/glossary/nesting)
 the [ABS function](https://exceljet.net/functions/abs-function)
 inside SQRT like this:

    =SQRT(ABS(-4)) // returns 2
    

The ABS function converts the negative number to a positive number and returns the result to the SQRT function, which calculates a final result.

### Exponent operator (^)

Another way to get the square root of a number in Excel is to use the [exponent operator](https://exceljet.net/glossary/math-operators)
 , the caret (^). To return the square root of a number in A1, you can use a formula like this:

    =A1^(1/2) // square root
    

The screen below shows how this formula looks in a worksheet:

![Square root of number with exponent](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/square%20root%20of%20number%20with%20exponent.png?itok=SjYDEL1K "Square root of number with exponent")

### Nth root

Excel does not have a built-in function to get the nth root of a number. However, you can calculate the nth root of a number by raising the number to the power of 1/n:

    =A1^(1/n) // nth root
    

The screen below shows this formula in use:

![Calculate nth root of a number](https://exceljet.net/sites/default/files/images/formulas/inline/calculate%20nth%20root%20of%20a%20number.png "Calculate nth root of a number")

### Square root with POWER

You can get also get the square root or nth root of a number with the [POWER function](https://exceljet.net/functions/power-function)
.  POWER is a general function for raising a number to a given power, for example:

    =POWER(2,2) // returns 4
    =POWER(2,3) // returns 8
    =POWER(2,4) // returns 16
    

The general form for getting the nth root with POWER is:

    =POWER(A1,1/n) // nth root
    

For example:

    =POWER(A1,1/2) // square root
    =POWER(A1,1/3) // cube root
    =POWER(A1,1/4) // fourth root
    

The screen below shows how the POWER function can be used to calculate square root of the numbers in column A:

![Square root of number with POWER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/square%20root%20of%20number%20with%20power.png?itok=f0TQ97cG "Square root of number with POWER function")

Related formulas
----------------

[![Excel formula: Cube root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cube%20root%20of%20number.png "Excel formula: Cube root of number")](https://exceljet.net/formulas/cube-root-of-number)

### [Cube root of number](https://exceljet.net/formulas/cube-root-of-number)

The cube root of a number can be calculated manually with the exponentiation operator (^) or with the POWER function . Manually with ^ The cube root of a number can be calculated manually by raising a number to the (1/3) using the exponentiation operator (^). In the example shown, the formula in C5...

[![Excel formula: nth root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth%20root%20of%20number.png "Excel formula: nth root of number")](https://exceljet.net/formulas/nth-root-of-number)

### [nth root of number](https://exceljet.net/formulas/nth-root-of-number)

By definition, the nth root of a number can be calculated by raising that number to the power of 1/n. Exponents are entered using the exponentiation operator (^), with a number on the left and power on the right. So, in this example we get the numbers from column B and powers from column C: =B5^(1/...

Related functions
-----------------

[![Excel SQRT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sqrt%20function.png "Excel SQRT function")](https://exceljet.net/functions/sqrt-function)

### [SQRT Function](https://exceljet.net/functions/sqrt-function)

The Excel SQRT function returns the square root of a positive number. SQRT returns an error if _number_ is negative.

[![Excel POWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20power%20function.png "Excel POWER function")](https://exceljet.net/functions/power-function)

### [POWER Function](https://exceljet.net/functions/power-function)

The Excel POWER function returns a number raised to a given power. The POWER function is an alternative to the [exponent operator](https://exceljet.net/glossary/math-operators)
 (^).

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cube root of number](https://exceljet.net/formulas/cube-root-of-number)
    
*   [nth root of number](https://exceljet.net/formulas/nth-root-of-number)
    

### Functions

*   [SQRT Function](https://exceljet.net/functions/sqrt-function)
    
*   [POWER Function](https://exceljet.net/functions/power-function)
    
*   [ABS Function](https://exceljet.net/functions/abs-function)
    

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