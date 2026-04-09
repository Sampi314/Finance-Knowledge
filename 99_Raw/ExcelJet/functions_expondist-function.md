# Excel EXPONDIST function | Exceljet

**Source:** https://exceljet.net/functions/expondist-function

---

[Skip to main content](https://exceljet.net/functions/expondist-function#main-content)

[](https://exceljet.net/functions/expondist-function#)

*   [Previous](https://exceljet.net/functions/expon.dist-function)
    
*   [Next](https://exceljet.net/functions/forecast-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

EXPONDIST Function
==================

by Kurt Bruns · Updated 15 Aug 2025

Related functions 
------------------

[EXPON.DIST](https://exceljet.net/functions/expon.dist-function)

![Excel EXPONDIST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_expondist_screenshot_cropped.png "Excel EXPONDIST function")

Summary
-------

The Excel EXPONDIST function calculates the exponential distribution. This is a legacy function that was replaced by the EXPON.DIST function in Excel 2010. Although EXPONDIST is still available for backward compatibility, Microsoft recommends using EXPON.DIST for new work, as it provides better accuracy and consistency with other modern statistical functions. For a detailed explanation of the exponential distribution and practical examples, see the [EXPON.DIST function](https://exceljet.net/functions/expon.dist-function)
.

Purpose 
--------

Get the PDF or CDF of the exponential distribution.

Return value 
-------------

A number representing the probability density or cumulative probability value.

Syntax
------

    =EXPONDIST(x,lambda,cumulative)

*   _x_ - The value at which to evaluate the distribution (must be ≥ 0).
*   _lambda_ - The rate parameter of the distribution (must be > 0).
*   _cumulative_ - A logical value that determines the form of the function. If TRUE, returns the cumulative distribution function; if FALSE, returns the probability density function.

Using the EXPONDIST function 
-----------------------------

The EXPONDIST function calculates values for the exponential distribution, which is a continuous probability distribution commonly used to model the time between events in a Poisson process. The exponential distribution is characterized by its "memoryless" property, meaning the probability of an event occurring in the next time interval is independent of how much time has already elapsed. This makes it ideal for modeling systems with constant event rates, such as radioactive decay, customer arrivals, and equipment failures with no aging effects.

For better accuracy and consistency with other modern statistical functions, it is recommended to use the [EXPON.DIST function](https://exceljet.net/functions/expon.dist-function)
. EXPON.DIST uses the same arguments and provides the same core functionality with improved numerical precision.

### Notes

*   EXPONDIST is a legacy function. For Excel 2010 and later, use the EXPON.DIST function.
*   If any argument is non-numeric, EXPONDIST returns the #VALUE! error.
*   If x < 0, EXPONDIST returns the #NUM! error.
*   If lambda ≤ 0, EXPONDIST returns the #NUM! error.

Related functions
-----------------

[![Excel EXPON.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/ExponentialDistribution_screenshot_cropped.png "Excel EXPON.DIST function")](https://exceljet.net/functions/expon.dist-function)

### [EXPON.DIST Function](https://exceljet.net/functions/expon.dist-function)

The Excel EXPON.DIST function calculates the exponential distribution, a continuous probability distribution commonly used to model the time between events in a Poisson process. The function can return either the probability density function (PDF) or the cumulative distribution function (CDF)...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [EXPON.DIST Function](https://exceljet.net/functions/expon.dist-function)
    

### Links

*   [Microsoft EXPONDIST function documentation](https://support.office.com/en-us/article/expondist-function-68ab45fd-cd6d-4887-9770-9357eb8ee06a)
    

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