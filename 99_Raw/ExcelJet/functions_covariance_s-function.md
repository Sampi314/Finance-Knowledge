# Excel COVARIANCE.S function | Exceljet

**Source:** https://exceljet.net/functions/covariance.s-function

---

[Skip to main content](https://exceljet.net/functions/covariance.s-function#main-content)

[](https://exceljet.net/functions/covariance.s-function#)

*   [Previous](https://exceljet.net/functions/covariance.p-function)
    
*   [Next](https://exceljet.net/functions/devsq-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

COVARIANCE.S Function
=====================

by Kurt Bruns · Updated 14 Jun 2025

Related functions 
------------------

[COVAR](https://exceljet.net/functions/covar-function)

[COVARIANCE.P](https://exceljet.net/functions/covariance.p-function)

[CORREL](https://exceljet.net/functions/correl-function)

![Excel COVARIANCE.S function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_covariance_s_function_main_screenshot_cropped.png "Excel COVARIANCE.S function")

Summary
-------

The Excel COVARIANCE.S function calculates the sample covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they move in opposite directions.

Purpose 
--------

Get the sample covariance between paired data

Return value 
-------------

A number representing the covariance

Syntax
------

    =COVARIANCE.S(array1,array2)

*   _array1_ - The first set of data values.
*   _array2_ - The second set of data values.

Using the COVARIANCE.S function 
--------------------------------

The COVARIANCE.S function calculates the sample covariance between two data sets. It measures the degree to which two variables vary together, providing insight into their linear relationship. The return value from the function is a single number that can be **positive, negative, or zero**, depending on the relationship between the variables. Unlike correlation, covariance is not standardized and depends on the units of measurement.

### Key features

*   Calculates sample covariance (divides by N-1, not N)
*   Both arrays must have the same number of data points
*   Returns positive values when variables move together
*   Returns negative values when variables move in opposite directions
*   Returns values close to zero when variables are independent
*   Works with numbers only - text and logical values are ignored

> **Note:** Excel also provides [COVARIANCE.P](https://exceljet.net/functions/covariance.p-function)
>  (population) function for population covariance. Use COVARIANCE.S when working with a sample from a larger population, and COVARIANCE.P when working with the entire population.

### Table of contents

*   [Example #1 - Positive Sample Covariance](https://exceljet.net/functions/covariance.s-function#example-1-positive-sample-covariance)
    
*   [Example #2 - Negative Sample Covariance](https://exceljet.net/functions/covariance.s-function#example-2-negative-sample-covariance)
    
*   [Example #3 - Zero Sample Covariance](https://exceljet.net/functions/covariance.s-function#example-3-zero-sample-covariance)
    
*   [When to use COVARIANCE.S](https://exceljet.net/functions/covariance.s-function#when-to-use-covariance-s)
    
*   [COVARIANCE.S vs COVARIANCE.P](https://exceljet.net/functions/covariance.s-function#covariance-s-vs-covariance-p)
    

### Example #1 - Positive Sample Covariance

In this example, we'll examine the relationship between temperature (°F) and ice cream sales ($) from a sample of 5 days. As temperature increases, ice cream sales tend to increase as well, demonstrating positive covariance.

![Temperature and Ice Cream Sales - Positive covariance example ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_covariance_s_function_example_positive_covariance_screenshot_cropped.png "Temperature and Ice Cream Sales - Positive covariance example ")

    =COVARIANCE.S(B5:B9,C5:C9) // returns positive sample covariance
    

The positive result indicates that temperature and ice cream sales have a positive relationship in this sample. As one increases, the other increases too.

### Example #2 - Negative Sample Covariance

Here we examine the relationship between a car's mileage and its resale price from a sample of vehicles. As mileage increases, the car's value typically decreases, showing negative covariance.

![Car Milage and Price - Negative covariance example ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_covariance_s_function_example_negative_covariance_screenshot_cropped.png "Car Milage and Price - Negative covariance example ")

    =COVARIANCE.S(B5:B9,C5:C9) // returns negative sample covariance
    

The negative result confirms that mileage and car price have an inverse relationship in this sample. As one increases, the other decreases.

### Example #3 - Zero Sample Covariance

This example illustrates two variables with no linear relationship: daily temperature and the result of a dice roll from a 10-day sample. These variables are completely independent of each other.

![Temperature and Dice Roll - Zero covariance example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_covariance_s_function_example_zero_covariance_screenshot_cropped.png "Temperature and Dice Roll - Zero covariance example")

    =COVARIANCE.S(B5:B14,C5:C14) // returns value close to zero
    

The result close to zero indicates no meaningful relationship between temperature and dice roll outcomes in this sample.

### When to use COVARIANCE.S

Use the COVARIANCE.S function when you need to analyze paired sample data to understand whether a relationship exists between the two variables in the broader population. A **positive covariance** indicates that the two variables tend to move in the same direction. A **negative covariance** suggests that the variables move in opposite directions. If the result is **near zero**, it implies there is little to no linear relationship between the two data sets.

The magnitude of the covariance depends on the units of measurement. As a result, it can be challenging to determine the strength of a relationship between two variables from covariance alone. When you care about the magnitude of change between variables in a sample, COVARIANCE.S might be the appropriate function for your use case. Otherwise, for a standardized comparison, use the [correlation function](https://exceljet.net/functions/correl-function)
.

### COVARIANCE.S vs COVARIANCE.P

The key difference between COVARIANCE.S and COVARIANCE.P lies in how they calculate the covariance:

*   **COVARIANCE.S** (Sample Covariance): Divides by N-1, where N is the number of data points. Use this when your data represents a sample from a larger population.
*   **COVARIANCE.P** (Population Covariance): Divides by N. Use this when your data represents the entire population of interest.

For most practical applications where you're working with sample data, COVARIANCE.S is the appropriate choice as it provides an unbiased estimate of the population covariance.

### Formula definition of COVARIANCE.S

![Sample covariance formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_covariance_sample_function_formula.png "Sample covariance formula")

### Notes

*   Empty cells, text, and logical values are ignored
*   Returns #DIV/0! error if arrays are empty after ignoring non-numeric values
*   Returns #N/A error if arrays have different lengths
*   Requires at least 2 data points to calculate (since it divides by N-1)
*   For population covariance (divides by N), use COVARIANCE.P function

Related functions
-----------------

[![Excel COVAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_covar_screenshot_cropped.png "Excel COVAR function")](https://exceljet.net/functions/covar-function)

### [COVAR Function](https://exceljet.net/functions/covar-function)

The Excel COVAR function calculates the covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they...

[![Excel COVARIANCE.P function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_covariance_p_function_main_screenshot_cropped.png "Excel COVARIANCE.P function")](https://exceljet.net/functions/covariance.p-function)

### [COVARIANCE.P Function](https://exceljet.net/functions/covariance.p-function)

The Excel COVARIANCE.P function calculates the population covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they move in opposite...

[![Excel CORREL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_correl_function_screenshot_cropped.png "Excel CORREL function")](https://exceljet.net/functions/correl-function)

### [CORREL Function](https://exceljet.net/functions/correl-function)

The Excel CORREL function calculates the correlation coefficient between two data sets. Correlation measures the strength and direction of the linear relationship between two variables, returning a value between -1 and 1. Unlike covariance, correlation...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COVAR Function](https://exceljet.net/functions/covar-function)
    
*   [COVARIANCE.P Function](https://exceljet.net/functions/covariance.p-function)
    
*   [CORREL Function](https://exceljet.net/functions/correl-function)
    

### Links

*   [Microsoft COVARIANCE.S function documentation](https://support.office.com/en-us/article/covariance-s-function-0a539b74-7371-42aa-a18f-1f5320314977)
    

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