# Excel PROB function | Exceljet

**Source:** https://exceljet.net/functions/prob-function

---

[Skip to main content](https://exceljet.net/functions/prob-function#main-content)

[](https://exceljet.net/functions/prob-function#)

*   [Previous](https://exceljet.net/functions/phi-function)
    
*   [Next](https://exceljet.net/functions/quartile-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

PROB Function
=============

by Kurt Bruns · Updated 20 Aug 2025

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

[PERCENTILE](https://exceljet.net/functions/percentile-function)

[BINOM.DIST](https://exceljet.net/functions/binom.dist-function)

[NORM.DIST](https://exceljet.net/functions/norm.dist-function)

![Excel PROB function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_prob_function_screenshot_cropped.png "Excel PROB function")

Summary
-------

The Excel PROB function calculates the probability that values in a range fall within specified limits. The function works with a range of values and their corresponding probabilities, making it useful for discrete probability distributions and statistical analysis.

Purpose 
--------

Calculate the probability that values in a range fall within specified limits.

Return value 
-------------

A number between 0 and 1 representing the probability.

Syntax
------

    =PROB(x_range,prob_range,lower_limit,[upper_limit])

*   _x\_range_ - A range of numeric values representing the possible outcomes.
*   _prob\_range_ - A range of probabilities corresponding to the values in x\_range (must sum to 1).
*   _lower\_limit_ - The lower bound for the probability calculation.
*   _upper\_limit_ - \[optional\] The upper bound for the probability calculation. If omitted, PROB returns the probability that x equals lower\_limit.

Using the PROB function 
------------------------

The PROB function calculates probabilities for discrete probability distributions by summing the probabilities of all values in the _x\_range_ that fall within the specified limits. When upper\_limit is omitted, PROB returns probability of the lower\_limit value. This function is useful for analyzing discrete data where you have known outcomes and their associated probabilities.

### Key features

*   Works with discrete probability distributions
*   Requires probabilities in _prob\_range_ to sum to 1
*   Can calculate probability for a single value or a range of values
*   When upper\_limit is omitted, returns probability of the lower\_limit value
*   Returns #NUM! error if probabilities don't sum to 1

### Table of contents

*   [Key features](https://exceljet.net/functions/prob-function#key-features)
    
*   [Example #1 - Single value probability](https://exceljet.net/functions/prob-function#example-1---single-value-probability)
    
*   [Example #2 - Range probability](https://exceljet.net/functions/prob-function#example-2---range-probability)
    
*   [Example #3 - Error conditions](https://exceljet.net/functions/prob-function#example-3---error-conditions)
    
*   [When to use PROB](https://exceljet.net/functions/prob-function#when-to-use-prob)
    

### Example #1 - Single value probability

In this example, we have a dataset showing quiz scores and their corresponding probabilities. To find the probability of getting exactly a score of 7, we pass in 7 for the value of _lower\_limit_.

![PROB Function Example 1](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_prob_function_example_1_screenshot_cropped.png "PROB Function Example 1")

    =PROB(B5:B15, C5:C15, E5)
    

This formula returns 0.20, meaning there is a 20% chance of getting exactly a score of 7.

The function works by:  
1\. Finding the value 7 in the x\_range (B5:B15)  
2\. Returning the corresponding probability from prob\_range (C5:C15)  
3\. Since 7 appears in the table, it returns the probability of 0.20

### Example #2 - Range probability

To find the probability of getting a score between 5 and 8 (inclusive), we use both the lower\_limit and upper\_limit arguments:

![PROB Function Example 2](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_prob_function_example_2_screenshot_cropped.png "PROB Function Example 2")

    =PROB(B5:B15, C5:C15, E5, F5)
    

This formula returns 0.68, meaning there is a 68% chance of getting a score between 5 and 8 inclusive.

The function works by:  
1\. Finding all values in x\_range that are >= 5 and <= 8  
2\. Summing the corresponding probabilities from prob\_range  
3\. For scores 5, 6, 7, and 8: the probabilities sum to 0.68

### Example #3 - Error conditions

The PROB function returns the following errors:

If the probabilities in prob\_range don't sum to 1, the function returns #NUM! error

    =PROB({1,2,3},{0.2,0.3,0.4},2) // returns #NUM!
    

If x\_range and prob\_range have different numbers of values, the function returns #N/A error

    =PROB({1,2,3},{0.2,0.3},2) // returns #N/A
    

If any argument is non-numeric or contains non-numeric values (e.g., text), the function returns #NUM! error

    =PROB({"1",2,3},{0.2,0.3,0.5},2) // returns #NUM!
    

### When to use PROB

The PROB function is ideal for analyzing discrete probability distributions like calculating probabilities for survey results. These are scenarios where you have a complete set of possible outcomes and their associated probabilities. For continuous probability distributions, Excel provides distribution functions like [NORM.DIST](https://exceljet.net/functions/norm.dist-function)
, [EXPON.DIST](https://exceljet.net/functions/expon.dist-function)
, or [WEIBULL.DIST](https://exceljet.net/functions/weibull.dist-function)
.

Related functions
-----------------

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel PERCENTILE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_percentile.png "Excel PERCENTILE function")](https://exceljet.net/functions/percentile-function)

### [PERCENTILE Function](https://exceljet.net/functions/percentile-function)

The Excel PERCENTILE function calculates the "kth percentile" for a set of data. A percentile is a value below which a given percentage of values in a data set fall. You can use PERCENTILE to determine the 90th percentile, the 80th percentile, etc.

[![Excel BINOM.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20binom.dist%20function.png "Excel BINOM.DIST function")](https://exceljet.net/functions/binom.dist-function)

### [BINOM.DIST Function](https://exceljet.net/functions/binom.dist-function)

The Excel BINOM.DIST function returns the individual term binomial distribution probability. You can use BINOM.DIST to calculate probabilities that an event will occur a certain number of times in a given number of trials.

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

*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [PERCENTILE Function](https://exceljet.net/functions/percentile-function)
    
*   [BINOM.DIST Function](https://exceljet.net/functions/binom.dist-function)
    
*   [NORM.DIST Function](https://exceljet.net/functions/norm.dist-function)
    

### Links

*   [Microsoft PROB function documentation](https://support.office.com/en-us/article/prob-function-9ac30561-c81c-4259-8253-34f0a238fc49)
    

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