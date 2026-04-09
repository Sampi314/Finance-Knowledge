# Excel COVAR function | Exceljet

**Source:** https://exceljet.net/functions/covar-function

---

[Skip to main content](https://exceljet.net/functions/covar-function#main-content)

[](https://exceljet.net/functions/covar-function#)

*   [Previous](https://exceljet.net/functions/countifs-function)
    
*   [Next](https://exceljet.net/functions/covariance.p-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

COVAR Function
==============

by Kurt Bruns · Updated 8 Jul 2025

Related functions 
------------------

[COVARIANCE.P](https://exceljet.net/functions/covariance.p-function)

[COVARIANCE.S](https://exceljet.net/functions/covariance.s-function)

[CORREL](https://exceljet.net/functions/correl-function)

[VAR](https://exceljet.net/functions/var-function)

![Excel COVAR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_covar_screenshot_cropped.png "Excel COVAR function")

Summary
-------

The Excel COVAR function calculates the covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they move in opposite directions. For example:

    =COVAR(B6:B10,C6:C10) // returns covariance between two arrays

Purpose 
--------

Get the population covariance between two arrays.

Return value 
-------------

Returns a number that represents the covariance.

Syntax
------

    =COVAR(array1,array2)

*   _array1_ - The first set of data values.
*   _array2_ - The second set of data values.

Using the COVAR function 
-------------------------

The COVAR function calculates the population covariance between two data sets. It measures the degree to which two variables vary together, providing insight into their linear relationship. The return value from the function is a single number that can be **positive, negative, or zero**, depending on the relationship between the variables. Unlike correlation, covariance is not standardized and depends on the units of measurement.

### Key features

*   Calculates population covariance (divides by N, not N-1)
*   Both arrays must have the same number of data points
*   Returns positive values when variables move together
*   Returns negative values when variables move in opposite directions
*   Returns values close to zero when variables are independent
*   Works with numbers only - text and logical values are ignored

> **Note:** Excel also provides [COVARIANCE.P](https://exceljet.net/functions/covariance.p-function)
>  (population) and [COVARIANCE.S](https://exceljet.net/functions/covariance.s-function)
>  (sample) functions in newer versions. COVAR is equivalent to [COVARIANCE.P](https://exceljet.net/functions/covariance.p-function)
> .

### Table of contents

*   [Example #1 - Positive Covariance](https://exceljet.net/functions/covar-function#example-1-positive-covariance)
    
*   [Example #2 - Negative Covariance](https://exceljet.net/functions/covar-function#example-2-negative-covariance)
    
*   [Example #3 - Zero Covariance](https://exceljet.net/functions/covar-function#example-3-zero-covariance)
    
*   [When to use COVAR](https://exceljet.net/functions/covar-function#when-to-use-covar)
    

### Example #1 - Positive Covariance

In this example, we'll examine the relationship between temperature (°F) and ice cream sales ($). As temperature increases, ice cream sales tend to increase as well, demonstrating positive covariance.

![Temperature and Ice Cream Sales - Positive covariance example ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_covar_example_positive_screenshot_cropped.png "Temperature and Ice Cream Sales - Positive covariance example ")

    =COVAR(B5:B9,C5:C9) // returns 335
    

The positive result indicates that temperature and ice cream sales have a positive relationship. As one increases, the other increases too.

### Example #2 - Negative Covariance

Here we examine the relationship between a car's mileage and its resale price. As mileage increases, the car's value typically decreases, showing negative covariance.

![Car Milage and Price - Negative covariance example ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_covar_example_negative_screenshot_cropped.png "Car Milage and Price - Negative covariance example ")

    =COVAR(B5:B9,C5:C9) // returns -160000000
    

The negative result confirms that mileage and car price have an inverse relationship. As one increases, the other decreases.

### Example #3 - Zero Covariance

This example illustrates two variables with no linear relationship: daily temperature and the result of a dice roll. These variables are completely independent of each other.

![Temperature and Dice Roll - Zero covariance example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_covar_example_zero_screenshot_cropped.png "Temperature and Dice Roll - Zero covariance example")

    =COVAR(B5:B14,C5:C14) // returns -0.5
    

The result close to zero indicates no meaningful relationship between temperature and dice roll outcomes.

### When to use COVAR

Use the COVAR function when you need to analyze paired data to understand whether a relationship exists between the two variables. A **positive covariance** indicates that the two variables tend to move in the same direction. A **negative covariance** suggests that the variables move in opposite directions. If the result is **near zero**, it implies there is little to no linear relationship between the two data sets.

The magnitude of the covariance depends on the units of measurement. As a result, it can be challenging to determine the strength of a relationship between two variables from covariance alone. When you care about the magnitude of change between variables, COVAR might be the appropriate function for your use case. Otherwise, for a standardized comparison, use the correlation function instead.

### Formula definition of COVAR

![Formula definition of COVAR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_covar_function_formula.png "Formula definition of COVAR function")

### Notes

*   Empty cells, text, and logical values are ignored
*   Returns #DIV/0! error if arrays are empty after ignoring non-numeric values
*   Returns #N/A error if arrays have different lengths
*   For sample covariance (divides by N-1), use COVARIANCE.S function

Related functions
-----------------

[![Excel COVARIANCE.P function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_covariance_p_function_main_screenshot_cropped.png "Excel COVARIANCE.P function")](https://exceljet.net/functions/covariance.p-function)

### [COVARIANCE.P Function](https://exceljet.net/functions/covariance.p-function)

The Excel COVARIANCE.P function calculates the population covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they move in opposite...

[![Excel COVARIANCE.S function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_covariance_s_function_main_screenshot_cropped.png "Excel COVARIANCE.S function")](https://exceljet.net/functions/covariance.s-function)

### [COVARIANCE.S Function](https://exceljet.net/functions/covariance.s-function)

The Excel COVARIANCE.S function calculates the sample covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they move in opposite...

[![Excel CORREL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_correl_function_screenshot_cropped.png "Excel CORREL function")](https://exceljet.net/functions/correl-function)

### [CORREL Function](https://exceljet.net/functions/correl-function)

The Excel CORREL function calculates the correlation coefficient between two data sets. Correlation measures the strength and direction of the linear relationship between two variables, returning a value between -1 and 1. Unlike covariance, correlation...

[![Excel VAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_var.png "Excel VAR function")](https://exceljet.net/functions/var-function)

### [VAR Function](https://exceljet.net/functions/var-function)

The Excel VAR function estimates the variance of a sample of data. If data represents the entire population, use the VARP function or the newer VAR.P function. VAR ignores text values and logicals in references.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COVARIANCE.P Function](https://exceljet.net/functions/covariance.p-function)
    
*   [COVARIANCE.S Function](https://exceljet.net/functions/covariance.s-function)
    
*   [CORREL Function](https://exceljet.net/functions/correl-function)
    
*   [VAR Function](https://exceljet.net/functions/var-function)
    

### Links

*   [Microsoft COVAR function documentation](https://support.office.com/en-us/article/covar-function-50479552-2c03-4daf-bd71-a5ab88b2db03)
    

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