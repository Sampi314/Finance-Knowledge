# Excel GAMMAINV function | Exceljet

**Source:** https://exceljet.net/functions/gammainv-function

---

[Skip to main content](https://exceljet.net/functions/gammainv-function#main-content)

[](https://exceljet.net/functions/gammainv-function#)

*   [Previous](https://exceljet.net/functions/gammadist-function)
    
*   [Next](https://exceljet.net/functions/gammaln-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

GAMMAINV Function
=================

by Kurt Bruns · Updated 26 Jun 2025

Related functions 
------------------

[GAMMA.INV](https://exceljet.net/functions/gamma.inv-function)

[GAMMADIST](https://exceljet.net/functions/gammadist-function)

![Excel GAMMAINV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_gammainv_main_screenshot_cropped.png "Excel GAMMAINV function")

Summary
-------

The Excel GAMMAINV function returns the inverse of the gamma cumulative distribution. This is a legacy function that was replaced by the GAMMA.INV function in Excel 2010. Microsoft recommends using GAMMA.INV for new work, as it provides better accuracy. For a detailed explanation of the gamma inverse distribution and practical examples, see the [GAMMA.INV function](https://exceljet.net/functions/gamma.inv-function)
.

Purpose 
--------

Get inverse of the gamma cumulative distribution

Return value 
-------------

The value of a probability

Syntax
------

    =GAMMAINV(probability,alpha,beta)

*   _probability_ - The probability associated with the gamma distribution (must be between 0 and 1).
*   _alpha_ - The shape parameter of the distribution.
*   _beta_ - The scale parameter of the distribution.

Using the GAMMAINV function 
----------------------------

The GAMMAINV function returns the value at which the cumulative gamma distribution reaches a specified probability. For better accuracy and consistency with other modern statistical functions, it is recommended to use the [GAMMA.INV function](https://exceljet.net/functions/gamma.inv-function)
. GAMMA.INV uses the same arguments and provides the same core functionality with improved numerical precision. See the [GAMMA.INV function](https://exceljet.net/functions/gamma.inv-function)
 for more details and examples.

### Notes

*   GAMMAINV is a legacy function. For Excel 2010 and later, use the GAMMA.INV function.
*   If any argument is non-numeric, GAMMAINV returns the #VALUE! error.
*   If probability < 0 or ≥ 1, GAMMAINV returns the #NUM! error.
*   If alpha ≤ 0 or beta ≤ 0, GAMMAINV returns the #NUM! error.
*   GAMMA.INV provides improved accuracy over the legacy GAMMAINV function.

Related functions
-----------------

[![Excel GAMMA.INV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_inv_main_screenshot_cropped.png "Excel GAMMA.INV function")](https://exceljet.net/functions/gamma.inv-function)

### [GAMMA.INV Function](https://exceljet.net/functions/gamma.inv-function)

The Excel GAMMA.INV function returns the inverse of the gamma cumulative distribution (the quantile function). Given a probability, GAMMA.INV calculates the value of x such that the probability of the gamma distribution being less than or equal to x is equal to the given probability. This...

[![Excel GAMMADIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gammadist_main_screenshot_cropped.png "Excel GAMMADIST function")](https://exceljet.net/functions/gammadist-function)

### [GAMMADIST Function](https://exceljet.net/functions/gammadist-function)

The Excel GAMMADIST function calculates the gamma distribution. This is a legacy function that was replaced by the [GAMMA.DIST function](https://exceljet.net/functions/gamma.dist-function)
 in Excel 2010. Although GAMMADIST is still available for backward compatibility, Microsoft recommends using...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [GAMMA.INV Function](https://exceljet.net/functions/gamma.inv-function)
    
*   [GAMMADIST Function](https://exceljet.net/functions/gammadist-function)
    

### Links

*   [Microsoft GAMMAINV function documentation](https://support.office.com/en-us/article/gammainv-function-06393558-37ab-47d0-aa63-432f99e7916d)
    

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