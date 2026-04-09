# Excel GAMMA.DIST function | Exceljet

**Source:** https://exceljet.net/functions/gamma.dist-function

---

[Skip to main content](https://exceljet.net/functions/gamma.dist-function#main-content)

[](https://exceljet.net/functions/gamma.dist-function#)

*   [Previous](https://exceljet.net/functions/gamma-function)
    
*   [Next](https://exceljet.net/functions/gamma.inv-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

GAMMA.DIST Function
===================

by Kurt Bruns · Updated 14 Aug 2025

Related functions 
------------------

[GAMMA.INV](https://exceljet.net/functions/gamma.inv-function)

[GAMMALN](https://exceljet.net/functions/gammaln-function)

[GAMMA](https://exceljet.net/functions/gamma-function)

[EXPON.DIST](https://exceljet.net/functions/expon.dist-function)

![Excel GAMMA.DIST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_gamma_dist_main_screenshot_cropped.png "Excel GAMMA.DIST function")

Summary
-------

The Excel GAMMA.DIST function calculates the gamma distribution, a continuous probability distribution used to model positive continuous variables. The function can return either the probability density function (PDF) to assess relative likelihood or the cumulative distribution function (CDF) to calculate probabilities. GAMMA.DIST is particularly useful for modeling skewed data and for applications like reliability analysis, queuing theory, and analyzing waiting times until a specific number of events occur.

Purpose 
--------

Get the PDF or CDF of the gamma distribution

Return value 
-------------

Probability density or cumulative probability value

Syntax
------

    =GAMMA.DIST(x,alpha,beta,cumulative)

*   _x_ - The value at which to evaluate the distribution.
*   _alpha_ - The shape parameter of the distribution.
*   _beta_ - The scale parameter of the distribution.
*   _cumulative_ - A logical value that determines the form of the function. If TRUE, returns the cumulative distribution function; if FALSE, returns the probability density function.

Using the GAMMA.DIST function 
------------------------------

The GAMMA.DIST function calculates values for the gamma distribution, which is a continuous probability distribution commonly used in statistical analysis. The gamma distribution is particularly useful for modeling positive continuous variables and has applications in reliability analysis, queuing theory, and meteorology.

### Key features

*   Returns either the probability density function (PDF) or the cumulative distribution function (CDF)
*   Requires all parameters to be positive numbers
*   Shape parameter (alpha) controls the distribution's shape
*   Scale parameter (beta) controls the distribution's spread
*   Reduces to the exponential distribution when alpha = 1
*   Uses a scale parameter (beta), not a rate parameter

> The GAMMA.DIST function is the updated version of [GAMMADIST](https://exceljet.net/functions/gammadist-function)
> . While GAMMADIST is still available for backward compatibility, Microsoft recommends using GAMMA.DIST for new work as it provides better accuracy.

### Table of contents

*   [Example #1 - Farmers market stall customers](https://exceljet.net/functions/gamma.dist-function#example-1-farmers-market-stall-customers)
    
*   [Example #2 - Shape and scale parameters](https://exceljet.net/functions/gamma.dist-function#example-2-shape-and-scale-parameters)
    
*   [Example #3 - Basic probability density calculations](https://exceljet.net/functions/gamma.dist-function#example-3-basic-probability-density-calculations)
    
*   [Example #4 - Cumulative distribution calculations](https://exceljet.net/functions/gamma.dist-function#example-4-cumulative-distribution-calculations)
    
*   [Example #5 - Parameter estimation](https://exceljet.net/functions/gamma.dist-function#example-5-parameter-estimation)
    
*   [Formula definition](https://exceljet.net/functions/gamma.dist-function#formula-definition)
    
*   [Related functions](https://exceljet.net/functions/gamma.dist-function#related-functions)
    
*   [Notes](https://exceljet.net/functions/gamma.dist-function#notes)
    

### Example #1 - Farmers market stall customers

Suppose you work at a stall at the farmers' market. Customers appear one at a time, at random, but historical data tell you they arrive **on average 10 per hour**. How long will you wait until **the 20th customer** shows up? This scenario is a good example of when to use the gamma distribution, because it models the time until the k-th event occurs in a Poisson process (random arrivals at a constant average rate).

To set up the problem as a gamma distribution:

*   Rate (λ): 10 customers per hour
*   Shape parameter (alpha): 20 (the number of customers we're waiting for)
*   Scale parameter (beta): 1/λ = 0.1 hours per customer
*   Function type: Use CDF (cumulative = TRUE) to calculate probabilities of waiting times, rather than PDF, which gives relative likelihood at specific points

To calculate the chance of waiting ≤ x hours for the 20th customer, we calculate the probability like this:

    =GAMMA.DIST(x, 20, 0.1, TRUE)
    

To calculate the chance of waiting > x hours for the 20th customer:

    =1-GAMMA.DIST(x, 20, 0.1, TRUE)
    

For example, to find the probability that the 20th customer arrives in **2 hours or less**, use:

    =GAMMA.DIST(2, 20, 0.1, TRUE) // 53% chance of waiting ≤ 2 hours
    

The spreadsheet below shows different waiting times and their corresponding probabilities:

![Excel spreadsheet showing GAMMA.DIST used to calculate probabilities of waiting times for the 20th customer, with various times in hours.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_gamma_dist_example_1_screenshot_cropped_0.png "Gamma distribution example - farmers market stall customers")

The gamma distribution is **right-skewed**, meaning it has a long tail to the right. This reflects the fact that while it's unlikely to wait a very long time for the 20th customer, it's still possible, due to random gaps between customer arrivals. In practice, there's a small chance you might wait far longer than average. There's also a decent chance that you'll reach 20 customers _sooner_ than the average, which is why the probability of reaching the 20th customer at or before 2 hours is 53%, not 50%.

This skewness is more pronounced when the shape parameter α (alpha) is small. As α increases, the gamma distribution becomes more symmetric and resembles a normal distribution. The right skew is a defining characteristic of the gamma distribution that makes it well-suited for modeling real-world waiting-time problems like the one described.

### Example #2 - Shape and scale parameters

The shape parameter (alpha) controls the shape of the distribution. For lower values of alpha, the distribution is more exponential-like, with a longer tail to the right. As the value of alpha increases, the distribution becomes more symmetric and resembles a normal distribution.

![Graph showing how the gamma distribution's shape changes for different values of the alpha parameter.](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionShape.png "Effect of the shape parameter (alpha) on the gamma distribution")

The scale parameter (beta) controls the scale of the distribution. As the value of beta increases, the distribution becomes more spread out.

![Graph showing how the gamma distribution becomes more spread out as the scale parameter (beta) increases.](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionScale.png "Effect of the scale parameter (beta) on the gamma distribution")

The function uses the standard parameterization where beta is the **scale parameter** (not rate parameter). Sometimes you'll see the gamma distribution defined with a rate parameter instead. To convert from rate to scale, use `scale = 1/rate`.

### Example #3 - Basic probability density calculations

This example shows how to use GAMMA.DIST with the `cumulative` argument set to FALSE to calculate the probability density function (PDF). The PDF indicates the relative likelihood of a random variable taking on a value near a specific point.

In this example, we'll calculate the PDF for a gamma distribution with a shape (alpha) of 3 and a scale (beta) of 0.2. The formula is:

    =GAMMA.DIST(x, 3, 0.2, FALSE)
    

The peak of the distribution (the mode) can be found with `(alpha - 1) * beta`, which is `(3 - 1) * 0.2 = 0.4`. We can calculate the PDF at this peak, and at other values, to see how the likelihood changes.

    =GAMMA.DIST(0.4, 3, 0.2, FALSE) // returns 1.353, the peak likelihood
    =GAMMA.DIST(0.2, 3, 0.2, FALSE) // returns 0.981
    =GAMMA.DIST(0.8, 3, 0.2, FALSE) // returns 0.903
    

It's important to understand that PDF values are not probabilities. A PDF value is a measure of probability _density_; it indicates the relative likelihood that a random variable will be found _near_ a particular value. A higher PDF value means it is more likely that the variable's value will be close to that point. Shown below is a graph of the PDF for the gamma distribution with alpha = 3 and beta = 0.2.

![Graph of the probability density function (PDF) for a gamma distribution with alpha = 3 and beta = 0.2, showing the peak likelihood at x = 0.4.](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionPDF.png "Probability density function (PDF) of a gamma distribution.")

To find the actual probability of the variable falling within a specific range, you must calculate the _area under the PDF curve_ over that interval. The area under the curve between two points represents the probability of the variable falling within that range.

![Graph of a gamma distribution's PDF showing the shaded area under the curve between two points, which represents the probability of the variable falling within that range.](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionPDFAreaBetween.png "Area under the PDF curve for a gamma distribution")

The Cumulative Distribution Function (CDF), as shown in the next example, is a practical way to compute this area.

### Example #4 - Cumulative distribution calculations

Setting the `cumulative` argument to TRUE returns the cumulative distribution function (CDF), which gives the probability of a random variable being less than or equal to a certain value. For example, using the same gamma distribution with alpha = 3 and beta = 0.2, the CDF at 0.7 is 0.679.

    =GAMMA.DIST(0.7, 3, 0.2, TRUE) // returns 0.679
    

This value is equal to the area under the PDF curve to the left of 0.7.

![Graph of a gamma distribution's PDF showing the shaded area to the left of x = 0.7, representing the cumulative distribution function (CDF) at that point.](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionPDFAreaLeft.png "Area under the PDF curve representing the CDF")

The cumulative distribution has a characteristic S-shape. It starts at 0 for x = 0 and smoothly increases toward 1 as x grows larger, which illustrates how the probability accumulates.

![Graph of the S-shaped cumulative distribution function (CDF) for a gamma distribution with alpha = 3 and beta = 0.2.](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionCDF.png "Cumulative distribution function (CDF) of a gamma distribution")

To find the probability of a value falling within a specific range, we can subtract the CDF value at the lower bound from the CDF value at the upper bound.

For instance, to find the probability that a value from a gamma distribution with alpha = 3 and beta = 0.2 falls between 0.3 and 0.7, we calculate the CDF at both points and find the difference:

    =GAMMA.DIST(0.7, 3, 0.2, TRUE) // P(X <= 0.7) = 0.679
    =GAMMA.DIST(0.3, 3, 0.2, TRUE) // P(X <= 0.3) = 0.191
    

The probability of the value being between 0.3 and 0.7 is:

    =GAMMA.DIST(0.7, 3, 0.2, TRUE) - GAMMA.DIST(0.3, 3, 0.2, TRUE) // returns 0.488
    

The spreadsheet below shows the CDF values for different values of x.

![Excel spreadsheet showing the calculation of cumulative distribution function (CDF) values for a gamma distribution at different points of x.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_gamma_dist_example_4_screenshot_cropped.png "Chart of cumulative distribution function (CDF) values")

### Example #5 - Parameter estimation

Sometimes you need to work backwards from sample data to estimate the gamma distribution parameters. While GAMMA.DIST doesn't directly estimate parameters, you can estimate the parameters using the method of moments.

The method of moments estimators are:

*   Shape (α) = (sample mean)² / (sample variance)
*   Scale (β) = (sample variance) / (sample mean)

### Formula definition

The gamma distribution is a continuous probability distribution that is defined by two parameters: the shape parameter (alpha) and the scale parameter (beta). The formula for the gamma distribution (PDF) is:

![The mathematical formula for the probability density function (PDF) of the gamma distribution.](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionPDFFormula.png "Formula for the gamma distribution PDF")

The cumulative distribution function (CDF) is the integral of the PDF from 0 to x:

![The mathematical formula for the cumulative distribution function (CDF) of the gamma distribution, shown as the integral of the PDF.](https://exceljet.net/sites/default/files/images/functions/inline/GammaDistributionCDFFormula.png "Formula for the gamma distribution CDF")

In practice, Excel calculates the GAMMA.DIST function using numerical methods. The CDF formula, in particular, involves an integral that does not have a simple, closed-form solution, so Excel uses a numerical approximation to calculate the value of the CDF.

### Related functions

Excel offers several functions for working with the gamma distribution and other related probability distributions:

*   [GAMMA.INV](https://exceljet.net/functions/gamma.inv-function)
     - Calculate inverse gamma distribution (quantiles)
*   [GAMMALN.PRECISE](https://exceljet.net/functions/gammaln.precise-function)
     - Calculate natural logarithm of gamma function
*   [WEIBULL.DIST](https://exceljet.net/functions/weibull.dist-function)
     - Calculate Weibull distribution (related to gamma)
*   EXPON.DIST - Calculate exponential distribution (special case of gamma)
*   CHISQ.DIST - Calculate chi-squared distribution (special case of gamma)

### Notes

*   All parameters (x, alpha, beta) must be positive numbers
*   If x < 0, the function returns #NUM! error
*   If alpha ≤ 0 or beta ≤ 0, the function returns #NUM! error
*   The cumulative argument must be TRUE or FALSE (or equivalent logical values)
*   When alpha = 1, the gamma distribution becomes the exponential distribution
*   GAMMA.DIST provides improved accuracy over the legacy GAMMADIST function
*   When modeling failure rates that change over time, see WEIBULL.DIST which is often preferred for this scenario in reliability analysis.
*   The chi-squared distribution is a special case of the gamma distribution where alpha = degrees of freedom / 2 and beta = 2

Related functions
-----------------

[![Excel GAMMA.INV function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_inv_main_screenshot_cropped.png "Excel GAMMA.INV function")](https://exceljet.net/functions/gamma.inv-function)

### [GAMMA.INV Function](https://exceljet.net/functions/gamma.inv-function)

The Excel GAMMA.INV function returns the inverse of the gamma cumulative distribution (the quantile function). Given a probability, GAMMA.INV calculates the value of x such that the probability of the gamma distribution being less than or equal to x is equal to the given probability. This...

[![Excel GAMMALN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gammaln_function_main_screenshot_cropped.png "Excel GAMMALN function")](https://exceljet.net/functions/gammaln-function)

### [GAMMALN Function](https://exceljet.net/functions/gammaln-function)

The Excel GAMMALN function returns the natural logarithm of the gamma function for a given number. This is useful for calculations involving large factorials or products, as working with logarithms helps avoid overflow and increases numerical stability. 

...

[![Excel GAMMA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_function_main_screenshot_cropped.png "Excel GAMMA function")](https://exceljet.net/functions/gamma-function)

### [GAMMA Function](https://exceljet.net/functions/gamma-function)

The Excel GAMMA function returns the gamma function value for a given number. The gamma function is a mathematical extension of the factorial function to real numbers. For example, the following formula calculates the gamma value for 5:...

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

*   [GAMMA.INV Function](https://exceljet.net/functions/gamma.inv-function)
    
*   [GAMMALN Function](https://exceljet.net/functions/gammaln-function)
    
*   [GAMMA Function](https://exceljet.net/functions/gamma-function)
    
*   [EXPON.DIST Function](https://exceljet.net/functions/expon.dist-function)
    

### Links

*   [Microsoft GAMMA.DIST function documentation](https://support.office.com/en-us/article/gamma-dist-function-9b6f1538-d11c-4d5f-8966-21f6a2201def)
    

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