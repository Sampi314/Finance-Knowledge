# Excel NORMSINV function | Exceljet

**Source:** https://exceljet.net/functions/normsinv-function

---

[Skip to main content](https://exceljet.net/functions/normsinv-function#main-content)

[](https://exceljet.net/functions/normsinv-function#)

*   [Previous](https://exceljet.net/functions/normsdist-function)
    
*   [Next](https://exceljet.net/functions/pearson-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

NORMSINV Function
=================

by Kurt Bruns · Updated 21 Aug 2025

Related functions 
------------------

[NORM.S.INV](https://exceljet.net/functions/norm.s.inv-function)

![Excel NORMSINV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_normsinv_function_screenshot_cropped.png "Excel NORMSINV function")

Summary
-------

The Excel NORMSINV function returns the inverse of the standard normal cumulative distribution. This is a legacy function that is replaced by the NORM.S.INV function. For complete documentation and examples, see the [NORM.S.INV function](https://exceljet.net/functions/norm.s.inv-function)
.

Purpose 
--------

Calculate the inverse of the standard normal cumulative distribution function (CDF) for a given probability.

Return value 
-------------

A z-score value representing the threshold for the given probability.

Syntax
------

    =NORMSINV(probability)

*   _probability_ - A probability corresponding to the standard normal distribution (CDF).

Using the NORMSINV function 
----------------------------

The NORMSINV function returns the inverse of the standard normal cumulative distribution. Given the probability of an event occurring below a threshold value, the function returns the z-score of the threshold. For example, NORMSINV(0.8413447) returns 1 since the probability of an event occurring below 1 standard deviation from the mean is 0.8413447.

The relationship between NORMSINV and NORMSDIST is:

    =NORMSINV(probability) // returns z-score
    

    =NORMSDIST(z-score) // returns probability
    

For better accuracy and consistency with other modern statistical functions, it is recommended to use the [NORM.S.INV function](https://exceljet.net/functions/norm.s.inv-function)
. NORM.S.INV provides the same inverse CDF functionality with improved numerical precision. See the [NORM.S.INV function](https://exceljet.net/functions/norm.s.inv-function)
 for more details.

Related functions
-----------------

[![Excel NORM.S.INV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_norm_s_inv.png "Excel NORM.S.INV function")](https://exceljet.net/functions/norm.s.inv-function)

### [NORM.S.INV Function](https://exceljet.net/functions/norm.s.inv-function)

The Excel NORM.S.INV function returns the inverse of the standard normal cumulative distribution.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [NORM.S.INV Function](https://exceljet.net/functions/norm.s.inv-function)
    

### Links

*   [Microsoft NORMSINV function documentation](https://support.office.com/en-us/article/normsinv-function-8d1bce66-8e4d-4f3b-967c-30eed61f019d)
    

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