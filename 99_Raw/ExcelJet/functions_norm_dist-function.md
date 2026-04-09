# Excel NORM.DIST function | Exceljet

**Source:** https://exceljet.net/functions/norm.dist-function

---

[Skip to main content](https://exceljet.net/functions/norm.dist-function#main-content)

[](https://exceljet.net/functions/norm.dist-function#)

*   [Previous](https://exceljet.net/functions/mode.sngl-function)
    
*   [Next](https://exceljet.net/functions/norm.inv-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

NORM.DIST Function
==================

by Kurt Bruns · Updated 11 May 2024

Related functions 
------------------

[NORM.S.DIST](https://exceljet.net/functions/norm.s.dist-function)

[NORM.INV](https://exceljet.net/functions/norm.inv-function)

![Excel NORM.DIST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_norm_dist.png "Excel NORM.DIST function")

Summary
-------

The Excel NORM.DIST function returns values for the normal probability density function (PDF) and the normal cumulative distribution function (CDF). The PDF returns the values of points on the curve. The CDF returns the area under the curve to the left of a value.

Purpose 
--------

Get values and areas for the normal distribution

Return value 
-------------

Output of the normal PDF and CDF

Syntax
------

    =NORM.DIST(x,mean,standard_dev,cumulative)

*   _x_ - The input value x.
*   _mean_ - The center of the distribution.
*   _standard\_dev_ - The standard deviation of the distribution.
*   _cumulative_ - A boolean value that determines whether the probability density function or the cumulative distribution function is used.

Using the NORM.DIST function 
-----------------------------

The NORM.DIST function returns values for the normal probability density function (PDF) and the normal cumulative distribution function (CDF). For example, NORM.DIST(5,3,2,TRUE) returns the output 0.841 which corresponds to the area to the left of 5 under the bell-shaped curve described by a mean of 3 and a standard deviation of 2. If the cumulative flag is set to FALSE, as in NORM.DIST(5,3,2,FALSE), the output is 0.121 which corresponds to the point on the curve at 5.

    =NORM.DIST(5,3,2,TRUE)=0.841
    

    =NORM.DIST(5,3,2,FALSE)=0.121
    

The output of the function is visualized by drawing the bell-shaped curve defined by the input to the function. If the cumulative flag is set to TRUE, the return value is equal to the area to the left of the input. If the cumulative flag is set to FALSE, the return value is equal to the value on the curve.

![Normal PDF Example](https://exceljet.net/sites/default/files/images/functions/inline/normal-pdf-example.png "Normal PDF Example")

### Explanation

The normal PDF is a bell-shaped probability density function described by two values: the mean and standard deviation. The mean represents the center or "balancing point" of the distribution. The _standard deviation_ represents how spread out the distribution is around the mean. The area under the normal distribution is always equal to 1 and is proportional to the standard deviation as shown in the figure below. For example, 68.3% of the area will always lie within one standard deviation of the mean.

![Normal Distribution Standard Deviation Areas](https://exceljet.net/sites/default/files/images/functions/inline/normal-distribution.png "Normal Distribution Standard Deviation Areas")

Probability density functions model problems over continuous ranges. The area under the function represents the probability of an event occurring in that range. For example, the probability of a student scoring exactly 93.41% on a test is very unlikely. Instead, it is reasonable to compute the probability of the student scoring between 90% and 95% on the test. Assuming that the test scores are normally distributed, the probability can be calculated using the output of the cumulative distribution function as shown in the formula below.

    =NORM.DIST(95,μ,σ,TRUE)-NORM.DIST(90,μ,σ,TRUE)
    

In this example, if we substitute a mean of 80 in for _μ_ and a standard deviation of 10 in for _σ_, then the probability of the student scoring between 90 and 95 out of 100 is 9.18%.

    =NORM.DIST(95,80,10,TRUE)-NORM.DIST(90,80,10,TRUE)=0.0918
    

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

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

*   [Microsoft NORM.DIST function documentation](https://support.office.com/en-us/article/norm-dist-function-edb1cc14-a21c-4e53-839d-8082074c9f8d)
    

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