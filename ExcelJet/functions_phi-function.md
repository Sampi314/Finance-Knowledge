# Excel PHI function | Exceljet

**Source:** https://exceljet.net/functions/phi-function

---

[Skip to main content](https://exceljet.net/functions/phi-function#main-content)

[](https://exceljet.net/functions/phi-function#)

*   [Previous](https://exceljet.net/functions/permutationa-function)
    
*   [Next](https://exceljet.net/functions/prob-function)
    

Excel 2013

[Statistical](https://exceljet.net/functions#Statistical)

PHI Function
============

by Kurt Bruns · Updated 2 Jul 2025

Related functions 
------------------

[NORM.S.DIST](https://exceljet.net/functions/norm.s.dist-function)

[NORM.DIST](https://exceljet.net/functions/norm.dist-function)

[NORM.INV](https://exceljet.net/functions/norm.inv-function)

[STANDARDIZE](https://exceljet.net/functions/standardize-function)

![Excel PHI function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_phi_function_main_screenshot_cropped.png "Excel PHI function")

Summary
-------

The Excel PHI function returns the value of the density function for a standard normal distribution (mean = 0, standard deviation = 1) at a given point. This is often used in statistical analysis, data science, and financial modeling to understand how likely a value is within a standard normal distribution.

Purpose 
--------

Get value of the density function for standard normal distribution

Return value 
-------------

The value of the standard normal density function at the given point

Syntax
------

    =PHI(x)

*   _x_ - The value (z-score) for which you want the density of the standard normal distribution.

Using the PHI function 
-----------------------

The PHI function calculates the value of the probability density function for a standard normal distribution at a given point. The standard normal distribution is a normal distribution with a mean of 0 and a standard deviation of 1. The PHI function is often used in statistical analysis, data science, and financial modeling to understand how likely a value is within a standard normal distribution.

For example, the following formula returns the value of the standard normal density function at 1:

    =PHI(1) // returns 0.241970725
    

### Key features

*   Returns the relative likelihood of a value in the standard normal distribution
*   Useful for statistical analysis, anomaly detection, and model building
*   Works only with standard normal distributions (mean = 0, standard deviation = 1)

> Note: PHI returns the value of the density function, not the cumulative probability. PHI is equivalent to [NORM.S.DIST](https://exceljet.net/functions/norm.s.dist-function)
>  with the cumulative flag set to FALSE. To get the cumulative probability, use [NORM.S.DIST](https://exceljet.net/functions/norm.s.dist-function)
>  with the cumulative flag set to TRUE.

### Table of contents

*   [Key features](https://exceljet.net/functions/phi-function#key-features)
    
*   [Example #1 - Basic usage](https://exceljet.net/functions/phi-function#example-1---basic-usage)
    
*   [Example #2 - Using z-scores](https://exceljet.net/functions/phi-function#example-2---using-z-scores)
    
*   [Example #3 - Error handling](https://exceljet.net/functions/phi-function#example-3---error-handling)
    
*   [When to use](https://exceljet.net/functions/phi-function#when-to-use)
    
*   [Related functions](https://exceljet.net/functions/phi-function#related-functions)
    

### Example #1 - Basic usage

The PHI function takes a single argument, _x_, and returns the value of the standard normal density function at that point:

    =PHI(-2) // returns 0.053990967
    =PHI(-1) // returns 0.241970725
    =PHI(0)  // returns 0.398942280
    =PHI(1)  // returns 0.241970725
    =PHI(2)  // returns 0.053990967
    

### Example #2 - Using z-scores

The PHI function can be used to calculate PDF values for normal distributions with different means and standard deviations. For example, suppose you have a list of values from a normal distribution with a mean of 83 and a standard deviation of 5. To find the probability density for each value, you first calculate the z-score, then use the PHI function.

    =PHI(STANDARDIZE(93,83,5)) // returns 0.0539909665
    

The z-score of a value, which measures how many standard deviations a value is from the mean, can be calculated using the [STANDARDIZE](https://exceljet.net/functions/standardize-function)
 function:

    =STANDARDIZE(93,83,5) // returns 2
    

or manually like this:

    z = (value - mean) / stdev
    

The following table shows the density for each value in the normal distribution with a mean of 83 and a standard deviation of 5:

![Table showing calculated z-scores and PHI function results for values from a normal distribution with mean 83 and standard deviation 5 in Excel.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_phi_function_example_2_using_z_scores_screenshot_cropped.png "PHI function example: Calculating probability density for a normal distribution using z-scores in Excel")

This approach allows you to use PHI to calculate the PDF for any normal distribution, not just the standard normal.

### Example #3 - Error handling

The PHI function returns the #VALUE! error if _x_ is not numeric.

    =PHI("apple") // returns #VALUE!
    

### When to use

Use the PHI function when you need the value of the standard normal density function (mean = 0, standard deviation = 1) at a specific point. PHI is equivalent to `NORM.S.DIST(x, FALSE)`. For cumulative probability, use `NORM.S.DIST(x, TRUE)`.

If you need the density for a normal distribution with a different mean or standard deviation, first convert your value to a z-score (see Example #2), or use the [NORM.DIST](https://exceljet.net/functions/norm.dist-function)
 function.

### Related functions

Excel provides several related functions for working with normal distributions:

*   [NORM.S.DIST](https://exceljet.net/functions/norm.s.dist-function)
     - Returns the cumulative distribution or density for the standard normal distribution.
*   [NORM.DIST](https://exceljet.net/functions/norm.dist-function)
     - Returns the cumulative distribution or density for a normal distribution with specified mean and standard deviation.
*   [NORM.INV](https://exceljet.net/functions/norm.inv-function)
     - Returns the inverse of the normal cumulative distribution.
*   [STANDARDIZE](https://exceljet.net/functions/standardize-function)
     - Converts a value to a z-score.

Related functions
-----------------

[![Excel NORM.S.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_norm_s_dist.png "Excel NORM.S.DIST function")](https://exceljet.net/functions/norm.s.dist-function)

### [NORM.S.DIST Function](https://exceljet.net/functions/norm.s.dist-function)

The Excel NORM.S.DIST function returns output for the standard normal cumulative distribution (CDF) and the standard normal probability density function (PDF).

[![Excel NORM.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_norm_dist.png "Excel NORM.DIST function")](https://exceljet.net/functions/norm.dist-function)

### [NORM.DIST Function](https://exceljet.net/functions/norm.dist-function)

The Excel NORM.DIST function returns values for the normal probability density function (PDF) and the normal cumulative distribution function (CDF). The PDF returns the values of points on the curve. The CDF returns the area under the curve to the left of a value.

[![Excel NORM.INV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_norm_inv.png "Excel NORM.INV function")](https://exceljet.net/functions/norm.inv-function)

### [NORM.INV Function](https://exceljet.net/functions/norm.inv-function)

The Excel NORM.INV function returns the inverse of the normal cumulative distribution for the specified mean and standard deviation. Given the probability of an event occurring below a threshold value, the function returns the threshold value associated with the probability.

[![Excel STANDARDIZE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_standardize.png "Excel STANDARDIZE function")](https://exceljet.net/functions/standardize-function)

### [STANDARDIZE Function](https://exceljet.net/functions/standardize-function)

The Excel STANDARDIZE function returns a normalized value (z-score) based on the mean and standard deviation.

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
    
*   [NORM.DIST Function](https://exceljet.net/functions/norm.dist-function)
    
*   [NORM.INV Function](https://exceljet.net/functions/norm.inv-function)
    
*   [STANDARDIZE Function](https://exceljet.net/functions/standardize-function)
    

### Links

*   [Microsoft PHI function documentation](https://support.office.com/en-us/article/phi-function-23e49bc6-a8e8-402d-98d3-9ded87f6295c)
    

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