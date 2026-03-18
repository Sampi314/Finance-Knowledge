# Excel GAMMA.INV function | Exceljet

**Source:** https://exceljet.net/functions/gamma.inv-function

---

[Skip to main content](https://exceljet.net/functions/gamma.inv-function#main-content)

[](https://exceljet.net/functions/gamma.inv-function#)

*   [Previous](https://exceljet.net/functions/gamma.dist-function)
    
*   [Next](https://exceljet.net/functions/gammadist-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

GAMMA.INV Function
==================

by Kurt Bruns · Updated 26 Jun 2025

Related functions 
------------------

[GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)

![Excel GAMMA.INV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_gamma_inv_main_screenshot_cropped.png "Excel GAMMA.INV function")

Summary
-------

The Excel GAMMA.INV function returns the inverse of the gamma cumulative distribution (the quantile function). Given a probability, GAMMA.INV calculates the value of x such that the probability of the gamma distribution being less than or equal to x is equal to the given probability. This is useful for finding threshold values, percentiles, or cutoffs in reliability analysis, queuing theory, and other applications.

Purpose 
--------

Get inverse of gamma cumulative distribution

Return value 
-------------

Threshold value of a probability

Syntax
------

    =GAMMA.INV(probability,alpha,beta)

*   _probability_ - The probability associated with the gamma distribution (must be between 0 and 1).
*   _alpha_ - The shape parameter of the distribution.
*   _beta_ - The scale parameter of the distribution.

Using the GAMMA.INV function 
-----------------------------

GAMMA.INV is used to find the value at which the cumulative gamma distribution reaches a specified probability. In other words, it answers the question: "For a given probability, what is the corresponding value of x in the gamma distribution?" This is also known as the quantile or percentile function.

### Key features

*   Returns the value of x for a given cumulative probability
*   Useful for calculating percentiles, thresholds, or cutoffs
*   Shape parameter (alpha) controls the distribution's shape
*   Scale parameter (beta) controls the distribution's spread
*   Requires all parameters to be positive numbers
*   Inverse of the GAMMA.DIST function with cumulative = TRUE

> GAMMA.INV is the updated version of [GAMMAINV](https://exceljet.net/functions/gammainv-function)
> . While GAMMAINV is still available for backward compatibility, Microsoft recommends using GAMMA.INV for new work as it provides better accuracy.

### Table of contents

*   [Key features](https://exceljet.net/functions/gamma.inv-function#key-features)
    
*   [Example #1 - Find a waiting time threshold](https://exceljet.net/functions/gamma.inv-function#example-1---find-a-waiting-time-threshold)
    
*   [Example #2 - Relationship to GAMMA.DIST](https://exceljet.net/functions/gamma.inv-function#example-2---relationship-to-gammadist)
    
*   [Example #3 - Calculate value at percentile](https://exceljet.net/functions/gamma.inv-function#example-3---calculate-value-at-percentile)
    
*   [How GAMMA.INV is approximated](https://exceljet.net/functions/gamma.inv-function#how-gammainv-is-approximated)
    
*   [Related functions](https://exceljet.net/functions/gamma.inv-function#related-functions)
    
*   [Notes](https://exceljet.net/functions/gamma.inv-function#notes)
    

### Example #1 - Find a waiting time threshold

Suppose you work at a stall at the farmers' market. Customers appear one at a time, at random, but historical data tell you they arrive **on average 10 per hour**. You want to know the maximum time you would have to wait for **the 20th customer** to show up, such that there is a 90% chance the 20th customer will have arrived by that time.

To set up the problem as a gamma distribution:

*   Rate (λ): 10 customers per hour
*   Shape parameter (alpha): 20 (the number of customers we're waiting for)
*   Scale parameter (beta): 1/λ = 0.1 hours per customer
*   Probability: 0.9 (90% chance)

To find the time by which there is a 90% chance the 20th customer will have arrived:

    =GAMMA.INV(0.9, 20, 0.1) // returns 2.590252861
    

This means there is a 90% chance that the 20th customer will arrive within 2.59 hours.

### Example #2 - Relationship to GAMMA.DIST

GAMMA.INV is the inverse of GAMMA.DIST with cumulative = TRUE. For example, using the result from above, you can check the probability of the 20th customer arriving within 2.59 hours with:

    =GAMMA.DIST(2.590252861, 20, 0.1, TRUE) // returns 0.9
    

In other words, GAMMA.INV finds the value for a given probability, and GAMMA.DIST with cumulative = TRUE finds the probability for a given value. Below is a graph of the gamma distribution CDF with the point where the probability is 0.9 showing the inverse relationship.

![Graph illustrating the inverse relationship between GAMMA.INV and the cumulative gamma distribution (CDF)](https://exceljet.net/sites/default/files/images/functions/inline/RelationshipToGammaCDF.png "GAMMA.INV and GAMMA.DIST (CDF) as inverse functions")

### Example #3 - Calculate value at percentile

In general, you can use GAMMA.INV to find the value at the percentile of a gamma distribution. For example, to find the value at the 25th, 50th, and 75th percentiles for a gamma distribution with alpha = 20 and beta = 0.1

    =GAMMA.INV(0.25, 20, 0.1) // returns 1.683014746
    =GAMMA.INV(0.50, 20, 0.1) // returns 1.966767242
    =GAMMA.INV(0.75, 20, 0.1) // returns 2.280800681
    

The percentile corresponds to the area under the probability density function (PDF) to the left of a specific threshold value. For example, the 75th percentile is the value at which 75% of the distribution lies to the left, representing a cumulative probability of 0.75.

![Gamma distribution PDF highlighting the 75th percentile](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionPDF75thPercentile.png "Gamma distribution PDF with 75th percentile marked")

### How GAMMA.INV is approximated

According to Microsoft, GAMMA.INV is calculated using an iterative search technique. Given a probability, GAMMA.INV seeks the value x such that `GAMMA.DIST(x, alpha, beta, TRUE)` equals the specified probability. The precision of GAMMA.INV depends on the precision of the GAMMA.DIST function. If the search does not converge after 64 iterations, GAMMA.INV returns the #N/A error value.

### Related functions

Excel offers several related functions for working with the gamma and other distributions:

*   [GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)
     - Calculate gamma distribution values (PDF or CDF)
*   GAMMALN - Calculate natural logarithm of gamma function
*   WEIBULL.DIST - Calculate Weibull distribution (related to gamma)
*   EXP.DIST - Calculate exponential distribution (special case of gamma)
*   CHISQ.INV - Inverse of the chi-squared distribution (special case of gamma)

### Notes

*   All parameters (probability, alpha, beta) must be positive numbers
*   Probability must be between 0 and 1 (exclusive)
*   If probability < 0 or ≥ 1, the function returns #NUM! error
*   If alpha ≤ 0 or beta ≤ 0, the function returns #NUM! error
*   If any argument is non-numeric, the function returns a #VALUE! error
*   GAMMA.INV provides improved accuracy over the legacy GAMMAINV function

Related functions
-----------------

[![Excel GAMMA.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_dist_main_screenshot_cropped.png "Excel GAMMA.DIST function")](https://exceljet.net/functions/gamma.dist-function)

### [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)

The Excel GAMMA.DIST function calculates the gamma distribution, a continuous probability distribution used to model positive continuous variables. The function can return either the probability density function (PDF) to assess relative likelihood or the cumulative distribution...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)
    

### Links

*   [Microsoft GAMMA.INV function documentation](https://support.office.com/en-us/article/gamma-inv-function-74991443-c2b0-4be5-aaab-1aa4d71fbb18)
    

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