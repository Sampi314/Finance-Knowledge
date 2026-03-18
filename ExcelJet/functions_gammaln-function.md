# Excel GAMMALN function | Exceljet

**Source:** https://exceljet.net/functions/gammaln-function

---

[Skip to main content](https://exceljet.net/functions/gammaln-function#main-content)

[](https://exceljet.net/functions/gammaln-function#)

*   [Previous](https://exceljet.net/functions/gammainv-function)
    
*   [Next](https://exceljet.net/functions/gammaln.precise-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

GAMMALN Function
================

by Kurt Bruns · Updated 10 Jul 2025

Related functions 
------------------

[GAMMALN.PRECISE](https://exceljet.net/functions/gammaln.precise-function)

[GAMMA](https://exceljet.net/functions/gamma-function)

[LN](https://exceljet.net/functions/ln-function)

![Excel GAMMALN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_gammaln_function_main_screenshot_cropped.png "Excel GAMMALN function")

Summary
-------

The Excel GAMMALN function returns the natural logarithm of the gamma function for a given number. This is useful for calculations involving large factorials or products, as working with logarithms helps avoid overflow and increases numerical stability. 

Purpose 
--------

Calculate the natural logarithm of the gamma function.

Return value 
-------------

A number representing the natural logarithm of the gamma function.

Syntax
------

    =GAMMALN(x)

*   _x_ - A positive real number for which you want to calculate the natural logarithm of the gamma function.

Using the GAMMALN function 
---------------------------

The GAMMALN function returns the natural logarithm of the gamma function, ln(Γ(n)), for a given number. This is especially useful in statistical calculations, such as those involving probability distributions, where the gamma function appears in the denominator and direct computation could result in very large or very small numbers. For positive integers n, GAMMALN(n) is equivalent to LN((n-1)!).

For example, the following formula calculates the natural logarithm of the gamma value for 5:

    =GAMMALN(5) // returns 3.17805383
    

### Key features

*   Returns the natural logarithm of the gamma function for decimal numbers
*   For positive integers n, GAMMALN(n) equals LN((n-1)!)
*   Accepts positive decimal numbers as input
*   Returns #NUM! error for zero and negative numbers

### Table of contents

*   [Key features](https://exceljet.net/functions/gammaln-function#key-features)
    
*   [Example #1 - Basic calculations](https://exceljet.net/functions/gammaln-function#example-1---basic-calculations)
    
*   [Example #2 - Relationship to gamma and factorials](https://exceljet.net/functions/gammaln-function#example-2---relationship-to-gamma-and-factorials)
    
*   [Example #3 - Error conditions](https://exceljet.net/functions/gammaln-function#example-3---error-conditions)
    
*   [Formula definition](https://exceljet.net/functions/gammaln-function#formula-definition)
    

> GAMMALN is still available for compatibility with earlier versions of Excel, but has been replaced by [GAMMALN.PRECISE](https://exceljet.net/functions/gammaln.precise-function)
> , which provides improved accuracy. Microsoft recommends using GAMMALN.PRECISE for new work.

### Example #1 - Basic calculations

The GAMMALN function takes a single argument as input like this:

    =GAMMALN(x)
    

The argument _x_ is the value for which you want to calculate the natural logarithm of the gamma function. Here are some basic examples showing both integer and non-integer inputs:

    =GAMMALN(0.5) // returns 0.57236494...
    =GAMMALN(2.0) // returns 0
    =GAMMALN(2.5) // returns 0.28468287...
    =GAMMALN(4.0) // returns 1.79175947...
    

### Example #2 - Relationship to gamma and factorials

In general, the GAMMALN function is equivalent to the natural logarithm of the [GAMMA function](https://exceljet.net/functions/gamma-function)
:

    =GAMMALN(x) // returns LN(GAMMA(x))
    

This relationship makes the GAMMALN function useful for calculations involving large factorials, as it avoids direct computation of large numbers. For example, attempting to compute a large factorial directly with the GAMMA function can result in an error due to overflow:

    =GAMMA(172) // returns #NUM! error
    

In contrast, using GAMMALN allows you to work with the logarithm of the gamma function, which avoids this problem and provides a valid result even for large inputs.

![Excel table comparing GAMMA and GAMMALN for large x values, showing GAMMA returns huge numbers or #NUM! errors, while GAMMALN gives valid logarithmic results.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_gammaln_function_example_2_relationship_to_gamma_screenshot_cropped.png "Excel example showing how GAMMALN provides valid results for large x values where GAMMA returns errors")

### Example #3 - Error conditions

The GAMMALN function returns #NUM! for zero and negative numbers, and #VALUE! for non-numeric inputs.

    =GAMMALN(0) // returns #NUM! error
    =GAMMALN(-1) // returns #NUM! error
    =GAMMALN(-2.5) // returns #NUM! error
    =GAMMALN("text") // returns #VALUE! error
    

### Formula definition

The GAMMALN function is defined as the natural logarithm of the gamma function. Shown below is the plot of the GAMMALN function, where Γ(x) is the gamma function.

![Plot of the GAMMALN function (ln(GAMMA(x))) showing a smooth curve that rises steeply toward positive infinity as x approaches 0 from the right, reaches its minimum between x = 1 and x = 2, and then increases steadily for larger x. The x-axis ranges from 0 to 5, and the y-axis from -1 to 3." src="images/GammaNaturalLogarithmFunction.png](https://exceljet.net/sites/default/files/images/functions/inline/GammaNaturalLogarithmFunction.png "Plot of the GAMMALN function (ln(GAMMA(x))) with x from 0 to 5, showing its minimum between x = 1 and x = 2, and that as x approaches 0 from the right, the function rises steeply toward positive infinity.")

Related functions
-----------------

[![Excel GAMMALN.PRECISE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gammaln_precise_function_main_screenshot_cropped.png "Excel GAMMALN.PRECISE function")](https://exceljet.net/functions/gammaln.precise-function)

### [GAMMALN.PRECISE Function](https://exceljet.net/functions/gammaln.precise-function)

The Excel GAMMALN.PRECISE function returns the natural logarithm of the gamma function for a given number. It is the more accurate, modern replacement for the older GAMMALN function, and is recommended for new work. This function is useful for calculations involving large factorials or...

[![Excel GAMMA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_function_main_screenshot_cropped.png "Excel GAMMA function")](https://exceljet.net/functions/gamma-function)

### [GAMMA Function](https://exceljet.net/functions/gamma-function)

The Excel GAMMA function returns the gamma function value for a given number. The gamma function is a mathematical extension of the factorial function to real numbers. For example, the following formula calculates the gamma value for 5:...

[![Excel LN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ln1.png "Excel LN function")](https://exceljet.net/functions/ln-function)

### [LN Function](https://exceljet.net/functions/ln-function)

The Excel LN function returns the natural logarithm of a given number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [GAMMALN.PRECISE Function](https://exceljet.net/functions/gammaln.precise-function)
    
*   [GAMMA Function](https://exceljet.net/functions/gamma-function)
    
*   [LN Function](https://exceljet.net/functions/ln-function)
    

### Links

*   [Microsoft GAMMALN function documentation](https://support.office.com/en-us/article/gammaln-function-b838c48b-c65f-484f-9e1d-141c55470eb9)
    

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