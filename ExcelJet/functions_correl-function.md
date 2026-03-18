# Excel CORREL function | Exceljet

**Source:** https://exceljet.net/functions/correl-function

---

[Skip to main content](https://exceljet.net/functions/correl-function#main-content)

[](https://exceljet.net/functions/correl-function#)

*   [Previous](https://exceljet.net/functions/binomdist-function)
    
*   [Next](https://exceljet.net/functions/count-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

CORREL Function
===============

by Kurt Bruns · Updated 13 Jun 2025

Related functions 
------------------

[PEARSON](https://exceljet.net/functions/pearson-function)

[COVAR](https://exceljet.net/functions/covar-function)

[COVARIANCE.P](https://exceljet.net/functions/covariance.p-function)

[COVARIANCE.S](https://exceljet.net/functions/covariance.s-function)

![Excel CORREL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_correl_function_screenshot_cropped.png "Excel CORREL function")

Summary
-------

The Excel CORREL function calculates the correlation coefficient between two data sets. Correlation measures the strength and direction of the linear relationship between two variables, returning a value between -1 and 1. Unlike covariance, correlation is standardized and unit-independent.

Purpose 
--------

Get correlation coefficient between two data sets

Return value 
-------------

A number between -1 and 1 representing the correlation coefficient.

Syntax
------

    =CORREL(array1,array2)

*   _array1_ - The first set of data values.
*   _array2_ - The second set of data values.

Using the CORREL function 
--------------------------

The CORREL function calculates the Pearson correlation coefficient between two data sets. It measures both the strength and direction of the linear relationship between variables, providing a standardized measure that ranges from -1 to 1.

### Key features

*   Returns values between -1 and 1 (inclusive)
*   Positive values close to 1 indicate positive correlation
*   Negative values close to -1 indicate negative correlation
*   Values close to zero indicate weak correlation
*   Unit-independent and standardized measure
*   Both arrays must have the same number of data points
*   Works with numbers only - text and logical values are ignored

> **Note:** Excel also provides PEARSON function which is identical to CORREL. Both calculate the Pearson product-moment correlation coefficient.

### Table of contents

*   [Example #1 - Strong Positive Correlation](https://exceljet.net/functions/correl-function#example-1-strong-positive-correlation)
    
*   [Example #2 - Strong Negative Correlation](https://exceljet.net/functions/correl-function#example-2-strong-negative-correlation)
    
*   [Example #3 - Weak Correlation](https://exceljet.net/functions/correl-function#example-3-weak-correlation)
    
*   [When to use CORREL](https://exceljet.net/functions/correl-function#when-to-use-correl)
    
*   [Formula Definition](https://exceljet.net/functions/correl-function#formula-definition)
    
*   [Notes](https://exceljet.net/functions/correl-function#notes)
    

### Example #1 - Strong Positive Correlation

In this example, we'll examine the relationship between temperature (°F) and ice cream sales ($). As temperature increases, ice cream sales tend to increase as well, demonstrating a strong positive correlation.

![Temperature and Ice Cream Sales - Strong Positive Correlation Example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_correl_example_positive_screenshot_cropped.png "Temperature and Ice Cream Sales - Strong Positive Correlation Example")

    =CORREL(B5:B9,C5:C9) // returns 0.997447985
    

The result indicates a strong positive correlation between temperature and ice cream sales.

### Example #2 - Strong Negative Correlation

Here we examine the relationship between a car's mileage (miles) and its resale value. As mileage increases, the car's value decreases proportionally, showing a strong negative correlation.

![Temperature and Ice Cream Sales - Strong Negative Correlation Example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_correl_example_negative_screenshot_cropped.png "Temperature and Ice Cream Sales - Strong Negative Correlation Example")

    =CORREL(B5:B9,C5:C9) // returns -1
    

The result confirms a strong negative correlation between car mileage and its market value.

### Example #3 - Weak Correlation

This example illustrates two variables with a weak relationship: daily temperature and coffee sales. While there might be some relationship, it's not very strong.

![Temperature and Coffee Sales - Weak Correlation Example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_correl_example_weak_screenshot_cropped.png "Temperature and Coffee Sales - Weak Correlation Example")

    =CORREL(B5:B9,C5:C9) // returns -0.057
    

The result close to zero indicates a weak negative correlation between temperature and coffee sales.

### When to use CORREL

Use CORREL when you need to quantify the linear relationship between two sets of numerical data in Excel. Choose CORREL over COVARIANCE.P or COVARIANCE.S (covariance functions) when you want a standardized measure that's easy to interpret regardless of the units involved. Use the covariance functions when you care about the magnitude of change in addition to the direction and strength of the relationship between variables.

**Key advantages**

*   Standardized scale (-1 to +1) makes interpretation easier
*   Unit-independent - can compare relationships across different measurement scales
*   Provides both direction and strength of relationship
*   Widely recognized and understood statistical measure

### **Formula definition**

![CORREL Function Formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_correl_function_formula.png "CORREL Function Formula")

### Notes

*   Both arrays must contain the same number of values
*   Empty cells, text, and logical values are ignored
*   Returns #DIV/0! error if either array has zero variance (all values are identical)
*   Returns #N/A error if arrays have different lengths
*   Only measures linear relationships - may miss non-linear associations

Related functions
-----------------

[![Excel PEARSON function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_pearson_function_main_screenshot_cropped.png "Excel PEARSON function")](https://exceljet.net/functions/pearson-function)

### [PEARSON Function](https://exceljet.net/functions/pearson-function)

The Excel PEARSON function calculates the Pearson correlation coefficient between two data sets. This coefficient measures the strength and direction of the linear relationship between two variables, returning a standardized value between -1 and 1.

...

[![Excel COVAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_covar_screenshot_cropped.png "Excel COVAR function")](https://exceljet.net/functions/covar-function)

### [COVAR Function](https://exceljet.net/functions/covar-function)

The Excel COVAR function calculates the covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they...

[![Excel COVARIANCE.P function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_covariance_p_function_main_screenshot_cropped.png "Excel COVARIANCE.P function")](https://exceljet.net/functions/covariance.p-function)

### [COVARIANCE.P Function](https://exceljet.net/functions/covariance.p-function)

The Excel COVARIANCE.P function calculates the population covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they move in opposite...

[![Excel COVARIANCE.S function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_covariance_s_function_main_screenshot_cropped.png "Excel COVARIANCE.S function")](https://exceljet.net/functions/covariance.s-function)

### [COVARIANCE.S Function](https://exceljet.net/functions/covariance.s-function)

The Excel COVARIANCE.S function calculates the sample covariance between two data sets. Covariance measures how much two variables change together. A positive result indicates the variables tend to increase and decrease in tandem, while a negative result means they move in opposite...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [PEARSON Function](https://exceljet.net/functions/pearson-function)
    
*   [COVAR Function](https://exceljet.net/functions/covar-function)
    
*   [COVARIANCE.P Function](https://exceljet.net/functions/covariance.p-function)
    
*   [COVARIANCE.S Function](https://exceljet.net/functions/covariance.s-function)
    

### Links

*   [Microsoft CORREL function documentation](https://support.office.com/en-us/article/correl-function-995dcef7-0c0a-4bed-a3fb-239d7b68ca92)
    

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