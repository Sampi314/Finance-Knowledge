# Excel GAMMADIST function | Exceljet

**Source:** https://exceljet.net/functions/gammadist-function

---

[Skip to main content](https://exceljet.net/functions/gammadist-function#main-content)

[](https://exceljet.net/functions/gammadist-function#)

*   [Previous](https://exceljet.net/functions/gamma.inv-function)
    
*   [Next](https://exceljet.net/functions/gammainv-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

GAMMADIST Function
==================

by Kurt Bruns · Updated 22 Jun 2025

Related functions 
------------------

[GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)

[GAMMA](https://exceljet.net/functions/gamma-function)

![Excel GAMMADIST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_gammadist_main_screenshot_cropped.png "Excel GAMMADIST function")

Summary
-------

The Excel GAMMADIST function calculates the gamma distribution. This is a legacy function that was replaced by the [GAMMA.DIST function](https://exceljet.net/functions/gamma.dist-function)
 in Excel 2010. Although GAMMADIST is still available for backward compatibility, Microsoft recommends using GAMMA.DIST for new work, as it provides better accuracy. For a detailed explanation of the gamma distribution and practical examples, see the [GAMMA.DIST function](https://exceljet.net/functions/gamma.dist-function)
.

Purpose 
--------

Get the PDF or CDF of the gamma distribution

Return value 
-------------

Probability density or cumulative probability value

Syntax
------

    =GAMMADIST(x,alpha,beta,cumulative)

*   _x_ - The value at which to evaluate the distribution.
*   _alpha_ - The shape parameter of the distribution.
*   _beta_ - The scale parameter of the distribution.
*   _cumulative_ - A logical value that determines the form of the function. If TRUE, returns the cumulative distribution function; if FALSE, returns the probability density function.

Using the GAMMADIST function 
-----------------------------

The GAMMADIST function calculates values for the gamma distribution, which is a continuous probability distribution commonly used in statistical analysis. The gamma distribution is particularly useful for modeling positive continuous variables and has applications in reliability analysis, queuing theory, and meteorology.

For better accuracy and consistency with other modern statistical functions, it is recommended to use the [GAMMA.DIST function](https://exceljet.net/functions/gamma.dist-function)
. GAMMA.DIST uses the same arguments and provides the same core functionality with improved numerical precision. See the [GAMMA.DIST function](https://exceljet.net/functions/gamma.dist-function)
 for more details.

### Notes

*   GAMMADIST is a legacy function. For Excel 2010 and later, use the GAMMA.DIST function.
*   If any argument is non-numeric, GAMMADIST returns the #VALUE! error.
*   If x < 0, GAMMADIST returns the #NUM! error.
*   If alpha ≤ 0 or beta ≤ 0, GAMMADIST returns the #NUM! error.
*   In Excel 2007, this is a Statistical function

Related functions
-----------------

[![Excel GAMMA.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_dist_main_screenshot_cropped.png "Excel GAMMA.DIST function")](https://exceljet.net/functions/gamma.dist-function)

### [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)

The Excel GAMMA.DIST function calculates the gamma distribution, a continuous probability distribution used to model positive continuous variables. The function can return either the probability density function (PDF) to assess relative likelihood or the cumulative distribution...

[![Excel GAMMA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_function_main_screenshot_cropped.png "Excel GAMMA function")](https://exceljet.net/functions/gamma-function)

### [GAMMA Function](https://exceljet.net/functions/gamma-function)

The Excel GAMMA function returns the gamma function value for a given number. The gamma function is a mathematical extension of the factorial function to real numbers. For example, the following formula calculates the gamma value for 5:...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)
    
*   [GAMMA Function](https://exceljet.net/functions/gamma-function)
    

### Links

*   [Microsoft GAMMADIST function documentation](https://support.office.com/en-us/article/gammadist-function-7327c94d-0f05-4511-83df-1dd7ed23e19e)
    

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