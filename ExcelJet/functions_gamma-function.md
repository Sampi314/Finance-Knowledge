# Excel GAMMA function | Exceljet

**Source:** https://exceljet.net/functions/gamma-function

---

[Skip to main content](https://exceljet.net/functions/gamma-function#main-content)

[](https://exceljet.net/functions/gamma-function#)

*   [Previous](https://exceljet.net/functions/frequency-function)
    
*   [Next](https://exceljet.net/functions/gamma.dist-function)
    

Excel 2013

[Statistical](https://exceljet.net/functions#Statistical)

GAMMA Function
==============

by Kurt Bruns · Updated 17 Jun 2025

Related functions 
------------------

[FACT](https://exceljet.net/functions/fact-function)

[GAMMALN](https://exceljet.net/functions/gammaln-function)

[GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)

[GAMMA.INV](https://exceljet.net/functions/gamma.inv-function)

![Excel GAMMA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_gamma_function_main_screenshot_cropped.png "Excel GAMMA function")

Summary
-------

The Excel GAMMA function returns the gamma function value for a given number. The gamma function is a mathematical extension of the factorial function to real numbers. For example, the following formula calculates the gamma value for 5:

    =GAMMA(5) // returns 24

Purpose 
--------

Extends factorial calculations to decimal numbers

Return value 
-------------

Extended factorial for decimal numbers

Syntax
------

    =GAMMA(number)

*   _number_ - A decimal number for which you want to calculate the gamma function value.

Using the GAMMA function 
-------------------------

The GAMMA function returns the gamma function value Γ(n) for a given number. The key relationship to understand is that Γ(n) = (n - 1)!, which means Excel's GAMMA function essentially computes factorials shifted by one position. For example, GAMMA(5) returns 24, which is equivalent to 4! (4 factorial). Importantly, the gamma function extends this factorial concept to non-integer values, defining calculations like GAMMA(2.5) that would be undefined with traditional factorials.

The GAMMA function is used for statistical calculations, probability distributions, and advanced mathematical modeling.

### Key features

*   Returns the gamma function value for decimal numbers
*   For positive integers n, GAMMA(n) equals (n-1)!
*   Accepts positive decimal numbers as input
*   Returns #NUM! error for zero and negative integers

### Table of contents

*   [Example #1 - Basic calculations](https://exceljet.net/functions/gamma-function#example-1-basic-calculations)
    
*   [Example #2 - Relationship to factorials](https://exceljet.net/functions/gamma-function#example-2-relationship-to-factorials)
    
*   [Example #4 - Error conditions](https://exceljet.net/functions/gamma-function#example-3-error-conditions)
    
*   [Mathematical Definition](https://exceljet.net/functions/gamma-function#mathematical-definition)
    
*   [Notes](https://exceljet.net/functions/gamma-function#notes)
    

### Example #1 - Basic calculations

The GAMMA function takes a single argument in this syntax:

    =GAMMA(number)
    

The argument _number_ is the value for which you want to calculate the gamma function. Here are some basic examples showing both integer and non-integer inputs:

    =GAMMA(0.5) // returns 1.7724538509... (√π)
    =GAMMA(2) // returns 1
    =GAMMA(2.5) // returns 1.3293403881...
    =GAMMA(5) // returns 24
    

### Example #2 - Relationship to factorials

The example below demonstrates the relationship between the GAMMA function and factorials. For any positive integer n, GAMMA(n) equals (n-1)!.

    =GAMMA(n) // returns (n-1)!
    

![Gamma function - Relationship to factorials](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_gamma_function_example_1_screenshot_cropped.png "Gamma function - Relationship to factorials")

This relationship makes the GAMMA function particularly useful when you need factorial-like calculations for non-integer values or in statistical formulas.

### Example #3 - Error conditions

The GAMMA function returns #NUM! for zero and negative integers, and #VALUE! for non-numeric inputs.

    =GAMMA(0) // returns #NUM! error
    =GAMMA(-1) // returns #NUM! error
    =GAMMA(-2) // returns #NUM! error
    =GAMMA("text") // returns #VALUE! error
    

![Gamma function - Error conditions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_gamma_function_error_conditions_screenshot_cropped.png "Gamma function - Error conditions")

### Mathematical Definition

The gamma function is formally defined as an integral that extends the concept of factorials to real and complex numbers. The mathematical definition is:

![Gamma function - Integral definition formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_gamma_function_formula.png "Gamma function - Integral definition formula")

While the gamma function is mathematically defined for complex numbers, Excel's GAMMA function implementation only accepts positive real number inputs.

### Notes

*   Decimal and positive values are accepted and return valid results
*   For positive integers n, GAMMA(n) = (n-1)!
*   The function returns #NUM! error for zero and negative integers
*   The GAMMA function is used for advanced statistical and mathematical calculations

Related functions
-----------------

[![Excel FACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fact.png "Excel FACT function")](https://exceljet.net/functions/fact-function)

### [FACT Function](https://exceljet.net/functions/fact-function)

The Excel FACT function returns the factorial of a given number. For example, =FACT(3) returns 6, equivalent to 3 x 2 x 1.

[![Excel GAMMALN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gammaln_function_main_screenshot_cropped.png "Excel GAMMALN function")](https://exceljet.net/functions/gammaln-function)

### [GAMMALN Function](https://exceljet.net/functions/gammaln-function)

The Excel GAMMALN function returns the natural logarithm of the gamma function for a given number. This is useful for calculations involving large factorials or products, as working with logarithms helps avoid overflow and increases numerical stability. 

...

[![Excel GAMMA.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_dist_main_screenshot_cropped.png "Excel GAMMA.DIST function")](https://exceljet.net/functions/gamma.dist-function)

### [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)

The Excel GAMMA.DIST function calculates the gamma distribution, a continuous probability distribution used to model positive continuous variables. The function can return either the probability density function (PDF) to assess relative likelihood or the cumulative distribution...

[![Excel GAMMA.INV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_inv_main_screenshot_cropped.png "Excel GAMMA.INV function")](https://exceljet.net/functions/gamma.inv-function)

### [GAMMA.INV Function](https://exceljet.net/functions/gamma.inv-function)

The Excel GAMMA.INV function returns the inverse of the gamma cumulative distribution (the quantile function). Given a probability, GAMMA.INV calculates the value of x such that the probability of the gamma distribution being less than or equal to x is equal to the given probability. This...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FACT Function](https://exceljet.net/functions/fact-function)
    
*   [GAMMALN Function](https://exceljet.net/functions/gammaln-function)
    
*   [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)
    
*   [GAMMA.INV Function](https://exceljet.net/functions/gamma.inv-function)
    

### Links

*   [Microsoft GAMMA function documentation](https://support.office.com/en-us/article/gamma-function-ce1702b1-cf55-471d-8307-f83be0fc5297)
    

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