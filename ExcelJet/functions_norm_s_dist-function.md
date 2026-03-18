# Excel NORM.S.DIST function | Exceljet

**Source:** https://exceljet.net/functions/norm.s.dist-function

---

[Skip to main content](https://exceljet.net/functions/norm.s.dist-function#main-content)

[](https://exceljet.net/functions/norm.s.dist-function#)

*   [Previous](https://exceljet.net/functions/norm.inv-function)
    
*   [Next](https://exceljet.net/functions/norm.s.inv-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

NORM.S.DIST Function
====================

by Kurt Bruns · Updated 27 Sep 2021

Related functions 
------------------

[NORM.DIST](https://exceljet.net/functions/norm.dist-function)

[NORM.S.INV](https://exceljet.net/functions/norm.s.inv-function)

![Excel NORM.S.DIST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_norm_s_dist.png "Excel NORM.S.DIST function")

Summary
-------

The Excel NORM.S.DIST function returns output for the standard normal cumulative distribution (CDF) and the standard normal probability density function (PDF).

Purpose 
--------

Get the standard normal CDF and PDF.

Return value 
-------------

The standard normal cumulative distribution function

Syntax
------

    =NORM.S.DIST(z,cumulative)

*   _z_ - Numeric z-score value.
*   _cumulative_ - Logical value that determines the form of the function.

Using the NORM.S.DIST function 
-------------------------------

The NORM.S.DIST function returns values for the standard normal cumulative distribution function (CDF) and the standard normal probability density function (PDF). For example, NORM.S.DIST(1,TRUE) returns the value 0.8413 and NORM.S.DIST(1,FALSE) returns the value 0.2420. The parameter, _z,_ represents the output we are interested in and _cumulative_ flag indicates whether the CDF or PDF function is used.

    =NORM.S.DIST(1,TRUE)=0.8413 // Returns the standard normal CDF
    

    =NORM.S.DIST(1,FALSE)=0.2420 // Returns the standard normal PDF
    

### NORM.S.DIST expects Standardized Input

NORM.S.DIST expects standardized input in the form of a _z_\-score value. A _z_\-score value represents how far a value is from the mean of a distribution in terms of the standard deviation of the distribution. To calculate the _z_\-score, subtract the mean from the value and then divide by the standard deviation or use the [STANDARDIZE](https://exceljet.net/functions/standardize-function)
 function as shown in the two formulas below:

    =(x-mean)/standard_deviation // calculates z-score
    

    =STANDARDIZE(x, mean, standard_deviation) // calculates z-score
    

Note, see the [NORM.DIST](https://exceljet.net/functions/norm.dist-function)
 function for non-standardized input.

### Cumulative Flag

The _cumulative_ flag determines which distribution function is used. If the flag is set to FALSE, the standard normal PDF is used. If the flag is set to TRUE, the standard normal CDF is used. The output of the CDF corresponds to the area under the PDF to the left of a threshold value. For example, when the flag is set to TRUE the standard normal CDF is returned as shown in the graph below. The output of the CDF represents the likelihood of an event occurring below an input value.

    =NORM.S.DIST(1,TRUE)=0.8413
    

![Standard Normal Cumulative Distribution Function](https://exceljet.net/sites/default/files/images/functions/inline/standard-normal-CDF.png "Standard Normal Cumulative Distribution Function")

When the _cumulative_ flag is set to FALSE, the standard normal PDF is used. The output of the CDF corresponds to the area under the PDF to the left of a threshold value. For example, with an input of 1 and the _cumulative_ flag set to FALSE the return value is 0.242. For the same input, with the _cumulative_ flag set to TRUE, the function returns 0.841 which is the area to the left of 1 on the normal bell-shaped curve. This is shown below:

    =NORM.S.DIST(1,FALSE)=0.242
    

![Standard Normal Probability Distribution Function](https://exceljet.net/sites/default/files/images/functions/inline/standard-normal-PDF.png "Standard Normal Probability Distribution Function")

### Explanation

The standard normal PDF is a bell-shaped probability density function described by two values: The mean represents the center or "balancing point" of the distribution. The standard deviation represents how spread out around the distribution is around the mean. The standard normal distribution is a special case of a normal distribution where the mean is 0 and the standard deviation is 1.

#### Probabilities

Probability density functions model problems concerning continuous ranges. For example, the probability of a student scoring exactly 93.41% on a test is very unlikely. Instead, it makes sense to compute the probability of the student scoring between 90% and 95% on the test. In this example, using a PDF that describes the distribution of test scores, the probability of an event occurring between two thresholds is equal to the area under the PDF's curve for the two values.

Note: Historically, due to the complexity of computing values on and areas below the normal PDF, a standardized version was created to make looking up pre-computed values in a table easier.

#### Calculating Probability Below a Threshold

To calculate the probability of an event occurring below the z-score value _b_ the formula would be:

    =NORM.S.DIST(b, TRUE)// Returns probability x less than b
    

![CDF Probability Less than a Threshold](https://exceljet.net/sites/default/files/images/functions/inline/probability-x-less-than-b.png "CDF Probability Less than a Threshold")

#### Calculating Probability Above a Threshold

To calculate the probability of an event occurring above the z-score value _a_ the formula would be:

    =1-NORM.S.DIST(a, TRUE)// Returns probability x greater than a
    

![CDF Probability Greater than a Threshold](https://exceljet.net/sites/default/files/images/functions/inline/probability-x-greater-than-a.png "CDF Probability Greater than a Threshold")

#### Calculating Probability Between Thresholds

To calculate the probability of an event occurring above _a_ and below _b_, where _b_ is greater than _a_, the formula is:

    =NORM.S.DIST(b, TRUE) - NORM.S.DIST(a, TRUE)
    

![CDF Probability Greater than A and less than B](https://exceljet.net/sites/default/files/images/functions/inline/probability-x-greater-than-a-and-less-than-b.png "CDF Probability Greater than A and less than B")

### NORM.S.DIST versus NORM.DIST

The difference between the functions NORM.DIST and NORM.S.DIST is NORM.S.DIST uses the standard normal distribution which is a special case of the normal distribution where the mean is 0 and the standard deviation is 1.

    =NORM.DIST(x,0,1,cumulative)=NORM.S.DIST(x,cumulative)
    

When the cumulative flag is set to 0 or FALSE, the functions return the respective points along the distributions.

![Points on Standard Normal PDF](https://exceljet.net/sites/default/files/images/functions/inline/standard-normal-pdf-example-1.png "Points on Standard Normal PDF")

    =NORM.S.DIST(1,FALSE)=0.2420
    

    =NORM.S.DIST(2,FALSE)=0.0540
    

![Normal PDF Example](https://exceljet.net/sites/default/files/images/functions/inline/normal-PDF-example-1.png "Normal PDF Example")

    =NORM.DIST(1,3,2,FALSE)=0.1210
    

    =NORM.DIST(2,3,2,FALSE)=0.1760
    

When the cumulative flag is set to TRUE and the input to NORM.S.DIST is standardized (discussed above), the output of the two functions is the same.

    =NORM.S.DIST((x-mean)/standard_deviation, TRUE)
    

    =NORM.DIST(x, mean, standard_deviation, TRUE) 
    

One way to visualize the relationship between the two functions is to highlight the relative areas, divided by standard deviations, underneath the standard normal distribution and a more general normal distribution with a mean of 0 and a standard deviation of 1. This is shown in the graphic below:

![Relative Area Under Normal Distribution](https://exceljet.net/sites/default/files/images/functions/inline/area-under-normal-distribution.png "Relative Area Under Normal Distribution")

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

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

*   [Microsoft NORM.S.DIST function documentation](https://support.office.com/en-us/article/norm-s-dist-function-1e787282-3832-4520-a9ae-bd2a8d99ba88)
    

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