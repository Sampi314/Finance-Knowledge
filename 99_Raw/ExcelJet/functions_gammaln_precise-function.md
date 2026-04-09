# Excel GAMMALN.PRECISE function | Exceljet

**Source:** https://exceljet.net/functions/gammaln.precise-function

---

[Skip to main content](https://exceljet.net/functions/gammaln.precise-function#main-content)

[](https://exceljet.net/functions/gammaln.precise-function#)

*   [Previous](https://exceljet.net/functions/gammaln-function)
    
*   [Next](https://exceljet.net/functions/geomean-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

GAMMALN.PRECISE Function
========================

by Kurt Bruns · Updated 10 Jul 2025

Related functions 
------------------

[GAMMA](https://exceljet.net/functions/gamma-function)

[LN](https://exceljet.net/functions/ln-function)

[GAMMALN](https://exceljet.net/functions/gammaln-function)

![Excel GAMMALN.PRECISE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_gammaln_precise_function_main_screenshot_cropped.png "Excel GAMMALN.PRECISE function")

Summary
-------

The Excel GAMMALN.PRECISE function returns the natural logarithm of the gamma function for a given number. It is the more accurate, modern replacement for the older GAMMALN function, and is recommended for new work. This function is useful for calculations involving large factorials or products, as working with logarithms helps avoid overflow and increases numerical stability.

Purpose 
--------

To calculate the natural logarithm of the gamma function.

Return value 
-------------

A number representing the natural logarithm of the gamma function.

Syntax
------

    =GAMMALN.PRECISE(x)

*   _x_ - A positive real number for which you want to calculate the natural logarithm of the gamma function.

Using the GAMMALN.PRECISE function 
-----------------------------------

The GAMMALN.PRECISE function returns the natural logarithm of the gamma function, ln(Γ(n)), for a given number. This is useful in statistical calculations, such as those involving probability distributions, where the gamma function appears in the denominator and direct computation could result in very large or very small numbers.

For positive integers n, GAMMALN.PRECISE(n) is equivalent to LN((n-1)!). For example, the following formula calculates the natural logarithm of the gamma value for 5:

    =GAMMALN.PRECISE(5) // returns 3.17805383
    

### Key features

*   Returns the natural logarithm of the gamma function for decimal numbers
*   For positive integers n, GAMMALN.PRECISE(n) equals LN((n-1)!)
*   Accepts positive decimal numbers as input
*   Returns #NUM! error for zero and negative numbers
*   More accurate than the legacy [GAMMALN](https://exceljet.net/functions/gammaln-function)
     function

### Table of contents

*   [Key features](https://exceljet.net/functions/gammaln.precise-function#key-features)
    
*   [Example #1 - Basic calculations](https://exceljet.net/functions/gammaln.precise-function#example-1---basic-calculations)
    
*   [Example #2 - Relationship to gamma and factorials](https://exceljet.net/functions/gammaln.precise-function#example-2---relationship-to-gamma-and-factorials)
    
*   [Example #3 - Error conditions](https://exceljet.net/functions/gammaln.precise-function#example-3---error-conditions)
    
*   [Formula definition](https://exceljet.net/functions/gammaln.precise-function#formula-definition)
    

### Example #1 - Basic calculations

The GAMMALN.PRECISE function takes a single argument as input like this:

    =GAMMALN.PRECISE(x)
    

The argument _x_ is the value for which you want to calculate the natural logarithm of the gamma function. Here are some basic examples showing both integer and non-integer inputs:

    =GAMMALN.PRECISE(0.5) // returns 0.57236494...
    =GAMMALN.PRECISE(2.0) // returns 0
    =GAMMALN.PRECISE(2.5) // returns 0.28468287...
    =GAMMALN.PRECISE(4.0) // returns 1.79175947...
    

![Excel GAMMALN.PRECISE function basic calculations example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_gammaln_precise_function_example_1_basic_calculations_screenshot_cropped.png "Excel GAMMALN.PRECISE function basic calculations example")

### Example #2 - Relationship to gamma and factorials

In general, the GAMMALN.PRECISE function is equivalent to the natural logarithm of the gamma function:

    =GAMMALN.PRECISE(x) // returns LN(GAMMA(x))
    

This relationship makes the GAMMALN.PRECISE function useful for calculations involving large factorials, as it avoids direct computation of large numbers. For example, attempting to compute a large factorial directly with the GAMMA function can result in an error due to overflow:

    =GAMMA(172) // returns #NUM! error
    

In contrast, using GAMMALN.PRECISE allows you to work with the logarithm of the gamma function, which avoids this problem and provides a valid result even for large inputs.

![Excel table comparing GAMMA and GAMMALN.PRECISE for large x values, showing GAMMA returns huge numbers or #NUM! errors, while GAMMALN.PRECISE gives valid logarithmic results.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_gammaln_precise_function_example_2_relationship_to_gamma_screenshot_cropped.png "Excel example showing how GAMMALN.PRECISE provides valid results for large x values where GAMMA returns errors")

### Example #3 - Error conditions

The GAMMALN.PRECISE function returns #NUM! for zero and negative numbers, and #VALUE! for non-numeric inputs.

    =GAMMALN.PRECISE(0) // returns #NUM! error
    =GAMMALN.PRECISE(-1) // returns #NUM! error
    =GAMMALN.PRECISE(-2.5) // returns #NUM! error
    =GAMMALN.PRECISE("text") // returns #VALUE! error
    

![Excel GAMMALN.PRECISE function error examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_gammaln_precise_function_errors_screenshot_cropped.png "Excel GAMMALN.PRECISE function error examples")

### Formula definition

The GAMMALN.PRECISE function is defined as the natural logarithm of the gamma function. The function is mathematically equivalent to:

    GAMMALN.PRECISE(x) = LN(GAMMA(x))
    

The function is plotted below, where Γ(x) is the gamma function.

![Graph of the GAMMALN.PRECISE function, y = ln(Gamma(x)), showing a curve that decreases steeply for x near 0, reaches a minimum near x = 1, and then increases steadily for larger x, over the range x = 0 to x = 5.](https://exceljet.net/sites/default/files/images/functions/inline/GammaLNPrecise.png "Graph of the GAMMALN.PRECISE Function (Natural Logarithm of Gamma Function)")

Related functions
-----------------

[![Excel GAMMA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_function_main_screenshot_cropped.png "Excel GAMMA function")](https://exceljet.net/functions/gamma-function)

### [GAMMA Function](https://exceljet.net/functions/gamma-function)

The Excel GAMMA function returns the gamma function value for a given number. The gamma function is a mathematical extension of the factorial function to real numbers. For example, the following formula calculates the gamma value for 5:...

[![Excel LN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ln1.png "Excel LN function")](https://exceljet.net/functions/ln-function)

### [LN Function](https://exceljet.net/functions/ln-function)

The Excel LN function returns the natural logarithm of a given number.

[![Excel GAMMALN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gammaln_function_main_screenshot_cropped.png "Excel GAMMALN function")](https://exceljet.net/functions/gammaln-function)

### [GAMMALN Function](https://exceljet.net/functions/gammaln-function)

The Excel GAMMALN function returns the natural logarithm of the gamma function for a given number. This is useful for calculations involving large factorials or products, as working with logarithms helps avoid overflow and increases numerical stability. 

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

*   [GAMMA Function](https://exceljet.net/functions/gamma-function)
    
*   [LN Function](https://exceljet.net/functions/ln-function)
    
*   [GAMMALN Function](https://exceljet.net/functions/gammaln-function)
    

### Links

*   [Microsoft GAMMALN.PRECISE function documentation](https://support.office.com/en-us/article/gammaln-precise-function-5cdfe601-4e1e-4189-9d74-241ef1caa599)
    

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