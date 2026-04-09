# Excel EXPON.DIST function | Exceljet

**Source:** https://exceljet.net/functions/expon.dist-function

---

[Skip to main content](https://exceljet.net/functions/expon.dist-function#main-content)

[](https://exceljet.net/functions/expon.dist-function#)

*   [Previous](https://exceljet.net/functions/devsq-function)
    
*   [Next](https://exceljet.net/functions/expondist-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

EXPON.DIST Function
===================

by Kurt Bruns · Updated 15 Aug 2025

Related functions 
------------------

[WEIBULL.DIST](https://exceljet.net/functions/weibull.dist-function)

[GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)

[NORM.DIST](https://exceljet.net/functions/norm.dist-function)

![Excel EXPON.DIST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/ExponentialDistribution_screenshot_cropped.png "Excel EXPON.DIST function")

Summary
-------

The Excel EXPON.DIST function calculates the exponential distribution, a continuous probability distribution commonly used to model the time between events in a Poisson process. The function can return either the probability density function (PDF) or the cumulative distribution function (CDF). EXPON.DIST is used in queuing theory, reliability engineering, and modeling systems with constant event rates such as radioactive decay and customer arrivals.

Purpose 
--------

Get the PDF or CDF of the exponential distribution.

Return value 
-------------

A number representing the probability density or cumulative probability value.

Syntax
------

    =EXPON.DIST(x,lambda,cumulative)

*   _x_ - The value at which to evaluate the distribution (must be ≥ 0).
*   _lambda_ - The rate parameter of the distribution (must be > 0).
*   _cumulative_ - A logical value that determines the form of the function. If TRUE, returns the cumulative distribution function; if FALSE, returns the probability density function.

Using the EXPON.DIST function 
------------------------------

The EXPON.DIST function calculates values for the exponential distribution, which is a continuous probability distribution used to model the time between events in a Poisson process. The exponential distribution is characterized by its "memoryless" property, meaning the probability of an event occurring in the next time interval is independent of how much time has already elapsed. This makes it ideal for modeling systems with constant event rates, such as radioactive decay, customer arrivals, and equipment failures with no aging effects.

### Key features

*   Returns either the probability density function (PDF) or the cumulative distribution function (CDF)
*   Rate parameter (lambda) controls the average time between events
*   Constant failure rate over time

> EXPON.DIST replaces the older [EXPONDIST function](https://exceljet.net/functions/expondist-function)
> , which is still available for backward compatibility. Microsoft recommends using EXPON.DIST for new work.

### Table of contents

*   [Key features](https://exceljet.net/functions/expon.dist-function#key-features)
    
*   [Example #1 - Customer arrival analysis](https://exceljet.net/functions/expon.dist-function#example-1---customer-arrival-analysis)
    
*   [Example #2 - Effect of rate parameter (lambda)](https://exceljet.net/functions/expon.dist-function#example-2---effect-of-rate-parameter-lambda)
    
*   [Example #3 - Cumulative vs. probability density](https://exceljet.net/functions/expon.dist-function#example-3---cumulative-vs-probability-density)
    
*   [Example #4 - Error Conditions](https://exceljet.net/functions/expon.dist-function#example-4---error-conditions)
    
*   [When to use the exponential distribution](https://exceljet.net/functions/expon.dist-function#when-to-use-the-exponential-distribution)
    
*   [Related functions](https://exceljet.net/functions/expon.dist-function#related-functions)
    
*   [Formula definition](https://exceljet.net/functions/expon.dist-function#formula-definition)
    

### Example #1 - Customer arrival analysis

Suppose we are analyzing customer arrivals at a coffee shop. Historical data suggests that customers arrive following a Poisson process with an average rate of 12 customers per hour.

This scenario is a good example of the exponential distribution because it models systems with constant arrival rates. Customers arrive independently at a constant average rate, and the probability of the next arrival doesn't depend on how long it's been since the last customer arrived.

To calculate the probability that the next customer will arrive within 10 minutes, we can use the cumulative distribution function (CDF):

    =EXPON.DIST(10/60, 12, TRUE) // returns 0.865
    

This formula returns the probability that the next customer arrives within 10 minutes (10/60 = 0.167 hours). For example, the result 0.865 means there is an 86.5% chance the next customer will arrive within 10 minutes.

To find the probability that the next customer arrives after 10 minutes, subtract the CDF from 1:

    =1-EXPON.DIST(10/60, 12, TRUE) // returns 0.135
    

This gives the probability that the next customer arrives after 10 minutes.

![Customer arrival analysis](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/ExponentialDistributionCustomerArrival_screenshot_cropped.png "Customer arrival analysis using EXPON.DIST function")

The table above shows customer arrival probabilities for different time intervals. It calculates both the probability density function (PDF) and cumulative distribution function (CDF) for arrival times ranging from 1 minute to 1 hour, using a rate of 12 customers per hour (λ = 12).

### Example #2 - Effect of rate parameter (lambda)

The rate parameter (lambda) determines the average time between events. The mean time between events is equal to 1/lambda.

*   Higher lambda values mean events occur more frequently (shorter average time between events)
*   Lower lambda values mean events occur less frequently (longer average time between events)

![Exponential PDF with different rate parameters (lambda)](https://exceljet.net/sites/default/files/images/functions/inline/ExponentialDistributionLambda.png "Exponential probability density function with different rate parameters (lambda). Higher lambda values result in steeper curves, indicating more frequent events.")

For example, consider different coffee shops with varying customer traffic levels. All follow an exponential distribution, but they have different rate parameters representing their customer arrival frequencies. Compare the probability of the next customer arriving within 5 minutes for different arrival rates:

    =EXPON.DIST(5/60,  6, TRUE)  // returns 0.393
    =EXPON.DIST(5/60, 12, TRUE)  // returns 0.632
    =EXPON.DIST(5/60, 24, TRUE)  // returns 0.865
    

As lambda increases, the probability of the next customer arriving within 5 minutes increases, indicating more frequent arrivals at busier locations.

### Example #3 - Cumulative vs. probability density

The _cumulative_ argument determines whether EXPON.DIST returns the cumulative distribution function (CDF) or the probability density function (PDF).

When _cumulative_ is FALSE, the function returns the probability density function (PDF), which indicates the relative likelihood of a random variable taking on a value near a specific point. The PDF value is not a probability itself, but a measure of probability density.

![Exponential PDF with lambda = 2.0](https://exceljet.net/sites/default/files/images/functions/inline/ExponentialDistributionPDF.png "Exponential probability density function with rate parameter λ = 2.0. At x = 1.5, the PDF value is 0.100, indicating the relative likelihood of failure at that point.")

    =EXPON.DIST(1.5, 2.0, FALSE) // returns 0.100 (PDF)
    

When _cumulative_ is TRUE, the function returns the cumulative distribution function (CDF), which gives the probability of a random variable being less than or equal to a certain value.

![Exponential CDF with lambda = 2.0](https://exceljet.net/sites/default/files/images/functions/inline/ExponentialDistributionCDF.png "Exponential cumulative distribution function with rate parameter λ = 2.0. At x = 1.5, the CDF value is 0.950, meaning there is a 95.0% probability of failure by that point.")

    =EXPON.DIST(1.5, 2.0, TRUE)  // returns 0.950 (CDF)
    

The CDF has a characteristic S-shape, starting at 0 and smoothly increasing toward 1 as x grows larger. The CDF value at any point equals the area under the PDF curve to the left of that point.

![Relationship between Exponential PDF and CDF](https://exceljet.net/sites/default/files/images/functions/inline/ExponentialDistributionPDFAreaUnderCurve.png "Relationship between Exponential PDF and CDF. The blue shaded area under the PDF curve to the left of x = 1.5 equals the CDF value of 0.950 at that point.")

Using the CDF, you can easily calculate probabilities for different scenarios. To calculate the probability of an event occurring below a threshold:

    =EXPON.DIST(threshold, lambda, TRUE)
    

To calculate the probability of an event occurring above a threshold:

    =1 - EXPON.DIST(threshold, lambda, TRUE)
    

To calculate the probability of an event occurring between two thresholds:

    =EXPON.DIST(upper, lambda, TRUE) - EXPON.DIST(lower, lambda, TRUE)
    

### Example #4 - Error Conditions

The EXPON.DIST function returns the following errors:

*   If x < 0, the function returns #NUM! error
*   If lambda ≤ 0, the function returns #NUM! error
*   If any argument is non-numeric, the function returns #VALUE! error

### When to use the exponential distribution

The exponential distribution is ideal for modeling time-between-events data where the events occur independently at a constant average rate. Its key characteristics make it suitable for:

*   **Poisson processes** - Modeling the time between events in a Poisson process
*   **Radioactive decay** - Modeling the time until radioactive particles decay
*   **Queuing theory** - Modeling inter-arrival times in service systems (banks, restaurants, call centers)
*   **Reliability analysis** - Modeling time-to-failure for equipment with constant failure rates

The exponential distribution is a special case of the [Weibull distribution](https://exceljet.net/functions/weibull.dist-function)
 when the shape parameter (alpha) equals 1, representing constant failure rates. It's also a special case of the [gamma distribution](https://exceljet.net/functions/gamma.dist-function)
 when the shape parameter (alpha) equals 1.

> For reliability analysis and failure modeling, the exponential distribution assumes no aging or wear-out effects. If your system shows increasing or decreasing failure rates over time, consider using the [Weibull distribution](https://exceljet.net/functions/weibull.dist-function)
>  instead. For modeling the time until multiple events occur, use the [gamma distribution](https://exceljet.net/functions/gamma.dist-function)
> .

### Related functions

Excel provides several related functions for probability distributions:

*   [WEIBULL.DIST](https://exceljet.net/functions/weibull.dist-function)
     - Weibull distribution (more general form, includes exponential as special case)
*   [GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function)
     - Gamma distribution (sum of exponential random variables)
*   POISSON.DIST - Poisson distribution (number of events in time period)
*   [NORM.DIST](https://exceljet.net/functions/norm.dist-function)
     - Normal distribution

### Formula definition

The formulas for the PDF and CDF of the exponential distribution are:

![Exponential distribution formula](https://exceljet.net/sites/default/files/images/functions/inline/ExponentialDistributionFormula.png "Exponential distribution formula")

Where:

*   f - probability density function
*   F - cumulative distribution function
*   x - the value at which to evaluate the distribution (must be ≥ 0)
*   lambda - the rate parameter of the distribution (must be > 0)
*   e - the exponential function ([EXP function](https://exceljet.net/functions/exp-function)
    )

Related functions
-----------------

[![Excel WEIBULL.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/WeibullDistributionMain_screenshot_cropped.png "Excel WEIBULL.DIST function")](https://exceljet.net/functions/weibull.dist-function)

### [WEIBULL.DIST Function](https://exceljet.net/functions/weibull.dist-function)

The Excel WEIBULL.DIST function calculates the Weibull distribution, a continuous probability distribution commonly used to model the time until failure of a component or system. The function can return either the probability density function (PDF) or the cumulative distribution function (CDF)...

[![Excel GAMMA.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_gamma_dist_main_screenshot_cropped.png "Excel GAMMA.DIST function")](https://exceljet.net/functions/gamma.dist-function)

### [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)

The Excel GAMMA.DIST function calculates the gamma distribution, a continuous probability distribution used to model positive continuous variables. The function can return either the probability density function (PDF) to assess relative likelihood or the cumulative distribution...

[![Excel NORM.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_norm_dist.png "Excel NORM.DIST function")](https://exceljet.net/functions/norm.dist-function)

### [NORM.DIST Function](https://exceljet.net/functions/norm.dist-function)

The Excel NORM.DIST function returns values for the normal probability density function (PDF) and the normal cumulative distribution function (CDF). The PDF returns the values of points on the curve. The CDF returns the area under the curve to the left of a value.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [WEIBULL.DIST Function](https://exceljet.net/functions/weibull.dist-function)
    
*   [GAMMA.DIST Function](https://exceljet.net/functions/gamma.dist-function)
    
*   [NORM.DIST Function](https://exceljet.net/functions/norm.dist-function)
    

### Links

*   [Microsoft EXPON.DIST function documentation](https://support.office.com/en-us/article/expon-dist-function-4c12ae24-e563-4155-bf3e-8b78b6ae140e)
    
*   [Wikipedia Exponential Distribution](https://en.wikipedia.org/wiki/Exponential_distribution)
    

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