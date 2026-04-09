# Excel WEIBULL.DIST function | Exceljet

**Source:** https://exceljet.net/functions/weibull.dist-function

---

[Skip to main content](https://exceljet.net/functions/weibull.dist-function#main-content)

[](https://exceljet.net/functions/weibull.dist-function#)

*   [Previous](https://exceljet.net/functions/weibull-function)
    
*   [Next](https://exceljet.net/functions/encodeurl-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

WEIBULL.DIST Function
=====================

by Kurt Bruns · Updated 13 Aug 2025

Related functions 
------------------

[GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)

[EXPON.DIST](https://exceljet.net/functions/expon.dist-function)

![Excel WEIBULL.DIST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/WeibullDistributionMain_screenshot_cropped.png "Excel WEIBULL.DIST function")

Summary
-------

The Excel WEIBULL.DIST function calculates the Weibull distribution, a continuous probability distribution commonly used to model the time until failure of a component or system. The function can return either the probability density function (PDF) or the cumulative distribution function (CDF). WEIBULL.DIST is widely used in reliability engineering, survival analysis, and failure time analysis.

Purpose 
--------

Get the PDF or CDF of the Weibull distribution.

Return value 
-------------

A number representing the probability density or cumulative probability value.

Syntax
------

    =WEIBULL.DIST(x,alpha,beta,cumulative)

*   _x_ - The value at which to evaluate the distribution (must be ≥ 0).
*   _alpha_ - The shape parameter of the distribution (must be > 0).
*   _beta_ - The scale parameter of the distribution (must be > 0).
*   _cumulative_ - A logical value that determines the form of the function. If TRUE, returns the cumulative distribution function; if FALSE, returns the probability density function.

Using the WEIBULL.DIST function 
--------------------------------

The WEIBULL.DIST function calculates values for the Weibull distribution, which is a continuous probability distribution used to model the time until a specified event, such as the failure of a machine part. The Weibull distribution is especially useful in reliability analysis and life data analysis, as it can model increasing, constant, or decreasing failure rates depending on the value of the shape parameter (alpha).

### Key features

*   Returns either the probability density function (PDF) or the cumulative distribution function (CDF)
*   Shape parameter (alpha) controls the failure rate behavior
*   Scale parameter (beta) stretches or compresses the distribution
*   Can model a wide range of failure behaviors
*   All parameters must be positive numbers

> WEIBULL.DIST replaces the older [WEIBULL](https://exceljet.net/functions/weibull-function)
>  function, which is still available for backward compatibility. Microsoft recommends using WEIBULL.DIST for new work.

### Table of contents

*   [Key features](https://exceljet.net/functions/weibull.dist-function#key-features)
    
*   [Example #1 - Light bulb lifetime analysis](https://exceljet.net/functions/weibull.dist-function#example-1---light-bulb-lifetime-analysis)
    
*   [Example #2 - Effect of shape parameter (alpha)](https://exceljet.net/functions/weibull.dist-function#example-2---effect-of-shape-parameter-alpha)
    
*   [Example #3 - Effect of scale parameter (beta)](https://exceljet.net/functions/weibull.dist-function#example-3---effect-of-scale-parameter-beta)
    
*   [Example #4 - Cumulative vs. probability density](https://exceljet.net/functions/weibull.dist-function#example-4---cumulative-vs-probability-density)
    
*   [Example #5 - Error Conditions](https://exceljet.net/functions/weibull.dist-function#example-5---error-conditions)
    
*   [When to use the Weibull distribution](https://exceljet.net/functions/weibull.dist-function#when-to-use-the-weibull-distribution)
    
*   [Related functions](https://exceljet.net/functions/weibull.dist-function#related-functions)
    
*   [Formula definition](https://exceljet.net/functions/weibull.dist-function#formula-definition)
    

### Example #1 - Light bulb lifetime analysis

Suppose you are analyzing the lifetimes of a batch of light bulbs. Historical data suggests that the lifetimes follow a Weibull distribution with a **shape parameter (alpha) of 1.5** and a **scale parameter (beta) of 1000 hours**. You want to know the probability that a randomly selected bulb will fail **within 800 hours**.

To calculate this probability, use the cumulative distribution function (CDF):

    =WEIBULL.DIST(800, 1.5, 1000, TRUE) // returns 0.511
    

This formula returns the probability that a bulb fails at or before 800 hours. For example, if the result is 0.511, it means there is a 51.1% chance a bulb will fail within 800 hours.

To find the probability that a bulb lasts **longer than 800 hours**, subtract the CDF from 1:

    =1-WEIBULL.DIST(800, 1.5, 1000, TRUE) // returns 0.489
    

This gives the probability that a bulb survives past 800 hours.

The Weibull distribution is flexible and can model different types of failure rates. In this example, with alpha > 1, the failure rate increases over time, which is typical for aging products.

### Example #2 - Effect of shape parameter (alpha)

The shape parameter (alpha) determines the behavior of the failure rate:

*   If alpha < 1, the failure rate decreases over time (infant mortality)
*   If alpha = 1, the failure rate is constant (exponential distribution)
*   If alpha > 1, the failure rate increases over time (wear-out failures)

If alpha < 1: Failures are most likely to happen early in the item's life, and those that survive become less likely to fail as time goes on. This is typical for products with early-life defects.

![Weibull PDF with α = 0.5 showing decreasing failure rate](https://exceljet.net/sites/default/files/images/functions/inline/WeibullDistributionAlpha05.png "Weibull probability density function with shape parameter α = 0.5. The curve starts high near zero and decreases sharply, indicating early-life failures are most common.")

If alpha = 1: The chance of failure is always the same, no matter how long the item has lasted. This models random, unpredictable failures with no aging effect.

![Weibull PDF with α = 1.0 showing constant failure rate](https://exceljet.net/sites/default/files/images/functions/inline/WeibullDistributionAlpha10.png "Weibull probability density function with shape parameter α = 1.0. The curve shows exponential decay from 1 to 0, representing constant failure rate over time.")

If alpha > 1: The risk of failure grows as the item ages, which is common for products that wear out or degrade with use.

![Weibull PDF with α = 1.5 showing increasing failure rate](https://exceljet.net/sites/default/files/images/functions/inline/WeibullDistributionAlpha15.png "Weibull probability density function with shape parameter α = 1.5. The curve rises to a peak then decreases, indicating wear-out failures that become more likely with age.")

### Example #3 - Effect of scale parameter (beta)

The scale parameter (beta) stretches or compresses the distribution along the x-axis. In time-based applications, larger values of beta mean the event (e.g., failure) is expected to occur later. The scale parameter typically corresponds to time units such as hours, days, or years in reliability analysis, or distance units such as miles or kilometers for applications like automotive component wear.

![Weibull PDF with different scale parameters (beta)](https://exceljet.net/sites/default/files/images/functions/inline/WeibullDistributionScaleParameter.png "Weibull probability density function with different scale parameters (beta). The curve shifts right as beta increases, indicating longer expected lifetimes.")

For example, consider different brands of light bulbs with varying quality levels. All follow a Weibull distribution with shape parameter alpha = 2.0 (indicating wear-out failures), but they have different scale parameters representing their expected lifetimes. Compare the probability of failure by 800 hours for different scale parameters:

    =WEIBULL.DIST(800, 2.0, 1000, TRUE)   // returns 0.473
    =WEIBULL.DIST(800, 2.0, 1500, TRUE)   // returns 0.198
    =WEIBULL.DIST(800, 2.0, 2000, TRUE)   // returns 0.095
    

As beta increases, the probability of failure by 800 hours decreases, indicating longer expected lifetimes for higher-quality bulbs.

### Example #4 - Cumulative vs. probability density

The `cumulative` argument determines whether WEIBULL.DIST returns the cumulative distribution function (CDF) or the probability density function (PDF).

When `cumulative` is FALSE, the function returns the probability density function (PDF), which indicates the relative likelihood of a random variable taking on a value near a specific point. The PDF value is not a probability itself, but a measure of probability density. For example, at x = 2.5, the PDF value of 0.289 indicates the relative likelihood of failure at that specific point.

![Weibull PDF with alpha = 5.0, beta = 2.0, and x = 2.5](https://exceljet.net/sites/default/files/images/functions/inline/WeibullDistributionPDF.png "Weibull probability density function with shape parameter α = 5.0 and scale parameter β = 2.0. At x = 2.5, the PDF value is 0.289, indicating the relative likelihood of failure at that point.")

    =WEIBULL.DIST(2.5, 5.0, 2.0, FALSE) // returns 0.289 (PDF)
    

When `cumulative` is TRUE, the function returns the cumulative distribution function (CDF), which gives the probability of a random variable being less than or equal to a certain value. For example, at x = 2.5, the CDF value of 0.953 means there is a 95.3% probability that a failure will occur by that point.

![Weibull CDF with alpha = 5.0, beta = 2.0, and x = 2.5](https://exceljet.net/sites/default/files/images/functions/inline/WeibullDistributionCDF.png "Weibull cumulative distribution function with shape parameter α = 5.0 and scale parameter β = 2.0. At x = 2.5, the CDF value is 0.953, meaning there is a 95.3% probability of failure by that point.")

    =WEIBULL.DIST(2.5, 5.0, 2.0, TRUE)  // returns 0.953 (CDF)
    

The CDF has a characteristic S-shape, starting at 0 and smoothly increasing toward 1 as x grows larger. The CDF value at any point equals the area under the PDF curve to the left of that point. This relationship is visually demonstrated in the following image, where the total area under the PDF curve is 1.

![Relationship between Weibull PDF and CDF](https://exceljet.net/sites/default/files/images/functions/inline/WeibullDistributionPDFvsCDF.png "Relationship between Weibull PDF and CDF. The blue shaded area under the PDF curve to the left of x = 2.5 equals the CDF value of 0.953 at that point.")

Using the CDF, you can calculate probabilities for different scenarios. To calculate the probability of an event occurring below a threshold:

    =WEIBULL.DIST(threshold, alpha, beta, TRUE)
    

To calculate the probability of an event occurring above a threshold:

    =1 - WEIBULL.DIST(threshold, alpha, beta, TRUE)
    

To calculate the probability of an event occurring between two thresholds:

    =WEIBULL.DIST(upper, alpha, beta, TRUE) - WEIBULL.DIST(lower, alpha, beta, TRUE)
    

### Example #5 - Error Conditions

The WEIBULL.DIST function returns the following errors:

*   If x < 0, the function returns #NUM! error
*   If alpha ≤ 0 or beta ≤ 0, the function returns #NUM! error
*   If any argument is non-numeric, the function returns #VALUE! error

The following image shows the error conditions for the WEIBULL.DIST function.

![WEIBULL.DIST Error handling](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/WeibullDistributionErrorConditions_screenshot_cropped.png "WEIBULL.DIST Error handling")

### When to use the Weibull distribution

The Weibull distribution is ideal for modeling time-to-failure data in reliability engineering and survival analysis. Its key advantage is the flexible shape parameter (α) that can model different failure patterns:

*   α < 1 - Decreasing failure rate (early-life failures)
*   α = 1 - Constant failure rate (exponential distribution)
*   α > 1 - Increasing failure rate (wear-out failures)

For most reliability analyses, WEIBULL.DIST is preferred over alternatives like [GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)
, which is better suited for modeling aggregate waiting times rather than time-to-first-failure scenarios.

> The EXPON.DIST function (Exponential distribution) is a special case of the Weibull distribution when alpha = 1.

### Related functions

Excel provides several related functions for probability distributions:

*   [GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)
     - Gamma distribution (more general form)
*   EXPON.DIST - Exponential distribution (special case of Weibull, alpha = 1)
*   CHISQ.DIST - Chi-squared distribution
*   LOGNORM.DIST - Log-normal distribution

### Formula definition

The formulas for the PDF and CDF of the Weibull distribution are:

![Weibull distribution formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/WeibullDistributionFormulas.png "Weibull distribution formula")

Where:

*   f - probability density function
*   F - cumulative distribution function
*   x - the value at which to evaluate the distribution (must be ≥ 0)
*   α (alpha) - the shape parameter of the distribution (must be > 0)
*   β (beta) - the scale parameter of the distribution (must be > 0)

Related functions
-----------------

[![Excel GAMMA.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_dist_main_screenshot_cropped.png "Excel GAMMA.DIST function")](https://exceljet.net/functions/gamma.dist-function)

### [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)

The Excel GAMMA.DIST function calculates the gamma distribution, a continuous probability distribution used to model positive continuous variables. The function can return either the probability density function (PDF) to assess relative likelihood or the cumulative distribution...

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

*   [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)
    
*   [EXPON.DIST Function](https://exceljet.net/functions/expon.dist-function)
    

### Links

*   [Microsoft WEIBULL.DIST function documentation](https://support.office.com/en-us/article/weibull-dist-function-4e783c39-9325-49be-bbc9-a83ef82b45db)
    

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