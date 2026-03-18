# Excel WEIBULL function | Exceljet

**Source:** https://exceljet.net/functions/weibull-function

---

[Skip to main content](https://exceljet.net/functions/weibull-function#main-content)

[](https://exceljet.net/functions/weibull-function#)

*   [Previous](https://exceljet.net/functions/varpa-function)
    
*   [Next](https://exceljet.net/functions/weibull.dist-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

WEIBULL Function
================

by Kurt Bruns · Updated 13 Aug 2025

Related functions 
------------------

[WEIBULL.DIST](https://exceljet.net/functions/weibull.dist-function)

![Excel WEIBULL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/WeibullFunction_screenshot_cropped.png "Excel WEIBULL function")

Summary
-------

The Excel WEIBULL function calculates the Weibull distribution. This is a legacy function that was replaced by the `WEIBULL.DIST` function in Excel 2010. Although `WEIBULL` is still available for backward compatibility, Microsoft recommends using `WEIBULL.DIST` for new work, as it provides better accuracy and consistency with other modern statistical functions. For a detailed explanation of the Weibull distribution and practical examples, see the [WEIBULL.DIST function](https://exceljet.net/functions/weibull.dist-function)
.

Purpose 
--------

Get the PDF or CDF of the Weibull distribution.

Return value 
-------------

A number representing the probability density or cumulative probability value.

Syntax
------

    =WEIBULL(x,alpha,beta,cumulative)

*   _x_ - The value at which to evaluate the distribution (must be ≥ 0).
*   _alpha_ - The shape parameter of the distribution (must be > 0).
*   _beta_ - The scale parameter of the distribution (must be > 0).
*   _cumulative_ - A logical value that determines the form of the function. If TRUE, returns the cumulative distribution function; if FALSE, returns the probability density function.

Using the WEIBULL function 
---------------------------

The WEIBULL function calculates values for the Weibull distribution, which is a continuous probability distribution commonly used to model the time until failure of a component or system. The Weibull distribution is particularly useful in reliability engineering, survival analysis, and failure time analysis, as it can model increasing, constant, or decreasing failure rates depending on the value of the shape parameter (alpha).

For better accuracy and consistency with other modern statistical functions, it is recommended to use the [WEIBULL.DIST function](https://exceljet.net/functions/weibull.dist-function)
. `WEIBULL.DIST` uses the same arguments and provides the same core functionality with improved numerical precision. See the [WEIBULL.DIST function](https://exceljet.net/functions/weibull.dist-function)
 for more details.

### Notes

*   `WEIBULL` is a legacy function. For Excel 2010 and later, use the `WEIBULL.DIST` function.
*   If any argument is non-numeric, `WEIBULL` returns the #VALUE! error.
*   If x < 0, `WEIBULL` returns the #NUM! error.
*   If alpha ≤ 0 or beta ≤ 0, `WEIBULL` returns the #NUM! error.

Related functions
-----------------

[![Excel WEIBULL.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/WeibullDistributionMain_screenshot_cropped.png "Excel WEIBULL.DIST function")](https://exceljet.net/functions/weibull.dist-function)

### [WEIBULL.DIST Function](https://exceljet.net/functions/weibull.dist-function)

The Excel WEIBULL.DIST function calculates the Weibull distribution, a continuous probability distribution commonly used to model the time until failure of a component or system. The function can return either the probability density function (PDF) or the cumulative distribution function (CDF)...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [WEIBULL.DIST Function](https://exceljet.net/functions/weibull.dist-function)
    

### Links

*   [Microsoft WEIBULL function documentation](https://support.office.com/en-us/article/weibull-function-b83dc2c6-260b-4754-bef2-633196f6fdcc)
    

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