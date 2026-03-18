# Excel NORM.S.INV function | Exceljet

**Source:** https://exceljet.net/functions/norm.s.inv-function

---

[Skip to main content](https://exceljet.net/functions/norm.s.inv-function#main-content)

[](https://exceljet.net/functions/norm.s.inv-function#)

*   [Previous](https://exceljet.net/functions/norm.s.dist-function)
    
*   [Next](https://exceljet.net/functions/normsdist-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

NORM.S.INV Function
===================

by Kurt Bruns · Updated 27 Jun 2020

Related functions 
------------------

[NORM.S.DIST](https://exceljet.net/functions/norm.s.dist-function)

[NORM.INV](https://exceljet.net/functions/norm.inv-function)

![Excel NORM.S.INV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_norm_s_inv.png "Excel NORM.S.INV function")

Summary
-------

The Excel NORM.S.INV function returns the inverse of the standard normal cumulative distribution.

Purpose 
--------

Get inverse of the standard normal cumulative distribution

Return value 
-------------

Returns the threshold value of a probability.

Syntax
------

    =NORM.S.INV(probability)

*   _probability_ - A probability corresponding to the standard normal distribution.

Using the NORM.S.INV function 
------------------------------

The NORM.S.INV function returns the inverse of the standard normal cumulative distribution. Given the probability of an event occurring below a threshold value, the function returns the z-score of the threshold. For example, NORM.S.INV(0.8413) returns 1 since the probability of an event occurring below 1 standard deviation from the mean is 0.8413.

    =NORM.S.INV(0.8413)=1
    

    =NORM.S.DIST(1, TRUE)=0.8413
    

### Notes

*   The return value is a z-score, which represents how far the value is from the mean of the distribution in terms of the standard deviation. See NORM.INV for non-standardized input.
*   Probability input outside of the range of (0,1) results in an error. 
*   The **standard** normal distribution is a special case of the normal distribution with a mean of 0 and a standard deviation of 1.
*   The standard normal **cumulative** distribution function returns the probability of an event occurring below a threshold value. This probability is equal to the area under the bell-shaped curve to the left of the threshold value.

Related functions
-----------------

[![Excel NORM.S.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_norm_s_dist.png "Excel NORM.S.DIST function")](https://exceljet.net/functions/norm.s.dist-function)

### [NORM.S.DIST Function](https://exceljet.net/functions/norm.s.dist-function)

The Excel NORM.S.DIST function returns output for the standard normal cumulative distribution (CDF) and the standard normal probability density function (PDF).

[![Excel NORM.INV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_norm_inv.png "Excel NORM.INV function")](https://exceljet.net/functions/norm.inv-function)

### [NORM.INV Function](https://exceljet.net/functions/norm.inv-function)

The Excel NORM.INV function returns the inverse of the normal cumulative distribution for the specified mean and standard deviation. Given the probability of an event occurring below a threshold value, the function returns the threshold value associated with the probability.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [NORM.S.DIST Function](https://exceljet.net/functions/norm.s.dist-function)
    
*   [NORM.INV Function](https://exceljet.net/functions/norm.inv-function)
    

### Links

*   [Microsoft NORM.S.INV function documentation](https://support.office.com/en-us/article/norm-s-inv-function-d6d556b4-ab7f-49cd-b526-5a20918452b1)
    

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