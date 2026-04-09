# Excel SKEW.P function | Exceljet

**Source:** https://exceljet.net/functions/skew.p-function

---

[Skip to main content](https://exceljet.net/functions/skew.p-function#main-content)

[](https://exceljet.net/functions/skew.p-function#)

*   [Previous](https://exceljet.net/functions/skew-function)
    
*   [Next](https://exceljet.net/functions/slope-function)
    

Excel 2013

[Statistical](https://exceljet.net/functions#Statistical)

SKEW.P Function
===============

by Dave Bruns · Updated 8 Nov 2020

Related functions 
------------------

[SKEW](https://exceljet.net/functions/skew-function)

![Excel SKEW.P function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20skew.p%20function.png "Excel SKEW.P function")

Summary
-------

The Excel SKEW.P function returns the _skewness_ of a distribution, which is a measure of symmetry. A positive result indicates a distribution that tails off to the right. A negative result indicates a distribution that tails off to the left. 

Purpose 
--------

Get skewness of a distribution based on population

Return value 
-------------

A positive or negative value

Syntax
------

    =SKEW.P(number1,[number2],...)

*   _number1_ - A range or reference that contains numeric values.
*   _number2_ - \[optional\] A range or reference that contains numeric values.

Using the SKEW.P function 
--------------------------

The SKEW.P function returns the "skewness" of a distribution. SKEW.P measures the _symmetry_ of a distribution. A positive skew result indicates a distribution that tails off to the right. A negative skew result indicates a distribution that tails off to the left. In a perfectly symmetrical distribution, the skew is zero.

### Example

In the example shown, there are 11 numeric values in two groups, A and B. The count of values in each group are the inverse of each other. There are four 1's in group A, four 5's in group B, etc. The formula in cell F12 returns a positive skew:

    =SKEW.P(B5:B15) // returns 0.7658
    
    

The formula in J12 returns a negative skew:

    =SKEW.P(C5:C15) // returns -0.7658
    

Excel also contains the [SKEW function](https://exceljet.net/functions/skew-function)
, which measures _sample_ skewness. The difference in calculation is related to an adjustment (n-1) made when data represents a sample versus the entire population. [More details here](https://exceljet.net/formulas/standard-deviation-calculation)
.

Related functions
-----------------

[![Excel SKEW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20skew%20function.png "Excel SKEW function")](https://exceljet.net/functions/skew-function)

### [SKEW Function](https://exceljet.net/functions/skew-function)

The Excel SKEW function returns the _skewness_ of a distribution, which is a measure of symmetry. A positive result indicates a distribution that tails off to the right. A negative result indicates a distribution that tails off to the left. 

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SKEW Function](https://exceljet.net/functions/skew-function)
    

### Links

*   [Microsoft SKEW.P function documentation](https://support.office.com/en-us/article/skew-p-function-76530a5c-99b9-48a1-8392-26632d542fcb)
    

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