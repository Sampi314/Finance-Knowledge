# Excel NORM.INV function | Exceljet

**Source:** https://exceljet.net/functions/norm.inv-function

---

[Skip to main content](https://exceljet.net/functions/norm.inv-function#main-content)

[](https://exceljet.net/functions/norm.inv-function#)

*   [Previous](https://exceljet.net/functions/norm.dist-function)
    
*   [Next](https://exceljet.net/functions/norm.s.dist-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

NORM.INV Function
=================

by Kurt Bruns · Updated 27 Sep 2021

Related functions 
------------------

[NORM.DIST](https://exceljet.net/functions/norm.dist-function)

[NORM.S.INV](https://exceljet.net/functions/norm.s.inv-function)

![Excel NORM.INV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_norm_inv.png "Excel NORM.INV function")

Summary
-------

The Excel NORM.INV function returns the inverse of the normal cumulative distribution for the specified mean and standard deviation. Given the probability of an event occurring below a threshold value, the function returns the threshold value associated with the probability.

Purpose 
--------

Get the inverse of normal cumulative distribution

Return value 
-------------

The threshold value associated with a probability

Syntax
------

    =NORM.INV(probability,mean,standard_dev)

*   _probability_ - The probability of an event occurring below a threshold.
*   _mean_ - The mean of the distribution.
*   _standard\_dev_ - The standard deviation of the distribution.

Using the NORM.INV function 
----------------------------

The NORM.INV function returns the inverse of the normal cumulative distribution. Given the probability of an event occurring below a threshold value, the function returns the threshold value associated with the _probability._ For example, NORM.INV(0.5, 3, 2) returns 3 since the probability of an event occurring below the _mean_ of the distribution is 0.5. Note, the area under a normal distribution within an interval corresponds to the probability of an event occurring within that interval.

    =NORM.INV(0.5,3,2 )// Returns 3
    

Let's look at another example using the same normal distribution defined by a mean of 3 and _standard deviation_ of 2.

    =NORM.INV(0.84134,3,2)// Returns 5
    

In this case, the threshold corresponding to the _probability_ of 0.84134 is equal to 5. In other words, the probability of an event occurring below 5 for this normal distribution is equal to 0.8413. 

#### Notes

*   The _mean_ describes the center or "balancing point" of the normal distribution.
*   The _standard deviation_ describes the shape of the bell-shaped curve.
*   Valid _probability_ input to the function is within the range (0,1), excluding 0 and 1.

Related functions
-----------------

[![Excel NORM.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_norm_dist.png "Excel NORM.DIST function")](https://exceljet.net/functions/norm.dist-function)

### [NORM.DIST Function](https://exceljet.net/functions/norm.dist-function)

The Excel NORM.DIST function returns values for the normal probability density function (PDF) and the normal cumulative distribution function (CDF). The PDF returns the values of points on the curve. The CDF returns the area under the curve to the left of a value.

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

*   [NORM.DIST Function](https://exceljet.net/functions/norm.dist-function)
    
*   [NORM.S.INV Function](https://exceljet.net/functions/norm.s.inv-function)
    

### Links

*   [Microsoft NORM.INV function documentation](https://support.office.com/en-us/article/norm-inv-function-54b30935-fee7-493c-bedb-2278a9db7e13)
    

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