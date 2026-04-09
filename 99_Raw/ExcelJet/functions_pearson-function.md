# Excel PEARSON function | Exceljet

**Source:** https://exceljet.net/functions/pearson-function

---

[Skip to main content](https://exceljet.net/functions/pearson-function#main-content)

[](https://exceljet.net/functions/pearson-function#)

*   [Previous](https://exceljet.net/functions/normsinv-function)
    
*   [Next](https://exceljet.net/functions/percentile-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

PEARSON Function
================

by Kurt Bruns · Updated 8 Jul 2025

Related functions 
------------------

[CORREL](https://exceljet.net/functions/correl-function)

[COVARIANCE.P](https://exceljet.net/functions/covariance.p-function)

[COVARIANCE.S](https://exceljet.net/functions/covariance.s-function)

![Excel PEARSON function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_pearson_function_main_screenshot_cropped.png "Excel PEARSON function")

Summary
-------

The Excel PEARSON function calculates the Pearson correlation coefficient between two data sets. This coefficient measures the strength and direction of the linear relationship between two variables, returning a standardized value between -1 and 1.

Purpose 
--------

To measure the strength and direction of the linear relationship between two variables.

Return value 
-------------

A number between -1 and 1, inclusive.

Syntax
------

    =PEARSON(array1,array2)

*   _array1_ - The first set of data values.
*   _array2_ - The second set of data values.

Using the PEARSON function 
---------------------------

The PEARSON function computes the Pearson product-moment correlation coefficient for two arrays of numbers. It quantifies both the strength and direction of a linear relationship, with results ranging from -1 (perfect negative correlation) to 1 (perfect positive correlation).

### Key features

*   Returns values between -1 and 1 (inclusive)
*   Positive values close to 1 indicate a strong positive correlation
*   Negative values close to -1 indicate a strong negative correlation
*   Values near zero indicate weak or no linear correlation
*   Standardized and unit-independent
*   Both arrays must have the same number of data points
*   Ignores text and logical values; works with numbers only

> **Note:** The PEARSON function is functionally identical to [CORREL](https://exceljet.net/functions/correl-function)
> . Both return the Pearson correlation coefficient.

### Table of contents

*   [Key features](https://exceljet.net/functions/pearson-function#key-features)
    
*   [Example #1 - Strong Positive Correlation](https://exceljet.net/functions/pearson-function#example-1---strong-positive-correlation)
    
*   [Example #2 - Strong Negative Correlation](https://exceljet.net/functions/pearson-function#example-2---strong-negative-correlation)
    
*   [Example #3 - Weak Correlation](https://exceljet.net/functions/pearson-function#example-3---weak-correlation)
    
*   [Example #4 - Edge cases and error handling](https://exceljet.net/functions/pearson-function#example-4---edge-cases-and-error-handling)
    
*   [When to use PEARSON](https://exceljet.net/functions/pearson-function#when-to-use-pearson)
    
*   [Formula definition](https://exceljet.net/functions/pearson-function#formula-definition)
    

### Example #1 - Strong Positive Correlation

In this example, we'll examine the relationship between temperature (°F) and ice cream sales ($). As temperature increases, ice cream sales tend to increase as well, demonstrating a strong positive correlation.

![Excel PEARSON function example showing strong positive correlation between temperature and ice cream sales](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_pearson_example_1_strong_positive_correlation_screenshot_cropped.png "PEARSON function: strong positive correlation between temperature and ice cream sales in Excel")

    =PEARSON(B5:B9,C5:C9) // returns 0.997447985
    

The result indicates a strong positive correlation between temperature and ice cream sales.

### Example #2 - Strong Negative Correlation

Here we examine the relationship between a car's mileage (miles) and its resale value. As mileage increases, the car's value decreases proportionally, showing a strong negative correlation.

![Excel PEARSON function example showing strong negative correlation between car mileage and resale value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_pearson_example_2_strong_negative_correlation_screenshot_cropped.png "PEARSON function: strong negative correlation between car mileage and resale value in Excel")

    =PEARSON(B5:B9,C5:C9) // returns -1
    

The result confirms a strong negative correlation between car mileage and its market value.

### Example #3 - Weak Correlation

This example illustrates two variables with a weak relationship: daily temperature and coffee sales. While there might be some relationship, it's not very strong.

![Excel PEARSON function example showing weak correlation between temperature and coffee sales](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_pearson_example_3_weak_correlation_screenshot_cropped.png "PEARSON function: weak correlation between temperature and coffee sales in Excel")

    =PEARSON(B5:B9,C5:C9) // returns -0.057
    

The result close to zero indicates a weak negative correlation between temperature and coffee sales.

### Example #4 - Edge cases and error handling

If either array contains a text value or an empty cell in a given position, PEARSON ignores the pair of data at that position. In the first screenshot below, the arrays contain a text value and an empty cell. These pairs are ignored, and the function calculates the correlation using only the remaining numeric pairs.

![Excel PEARSON function handling edge cases with text and empty cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_pearson_example_4_edge_case_screenshot_cropped.png "PEARSON function edge case: ignoring text and empty cells in Excel")

The second screenshot demonstrates two common errors:  
\- **#DIV/0! error**: This occurs when either array has zero variance (all values are identical), so the correlation is undefined.  
\- **#N/A error**: This occurs when the arrays have different lengths.

![Excel PEARSON function error examples: #DIV/0! and #N/A](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_pearson_function_4_errors_screenshot_cropped.png "PEARSON function error handling: #DIV/0! and #N/A in Excel")

### When to use PEARSON

Use PEARSON when you need to measure the linear relationship between two sets of numerical data in Excel. Choose PEARSON (or [CORREL](https://exceljet.net/functions/correl-function)
) when you want a standardized, unit-independent measure of correlation. Use covariance functions ([COVARIANCE.P](https://exceljet.net/functions/covariance.p-function)
 or [COVARIANCE.S](https://exceljet.net/functions/covariance.s-function)
) if you need to know the magnitude of change as well as direction.

PEARSON only measures linear relationships; it does not detect non-linear associations.

**Key advantages**

*   Standardized scale (-1 to +1) for easy interpretation
*   Unit-independent, allowing comparison across different measurement scales
*   Indicates both direction and strength of relationship
*   Widely used and recognized in statistics

### Formula definition

The PEARSON function uses the following formula:

![Mathematical formula for the Excel PEARSON function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_pearson_function_formula.png "Mathematical definition of the PEARSON correlation coefficient in Excel")

Related functions
-----------------

[![Excel CORREL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_correl_function_screenshot_cropped.png "Excel CORREL function")](https://exceljet.net/functions/correl-function)

### [CORREL Function](https://exceljet.net/functions/correl-function)

The Excel CORREL function calculates the correlation coefficient between two data sets. Correlation measures the strength and direction of the linear relationship between two variables, returning a value between -1 and 1. Unlike covariance, correlation...

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

*   [CORREL Function](https://exceljet.net/functions/correl-function)
    
*   [COVARIANCE.P Function](https://exceljet.net/functions/covariance.p-function)
    
*   [COVARIANCE.S Function](https://exceljet.net/functions/covariance.s-function)
    

### Links

*   [Microsoft PEARSON function documentation](https://support.office.com/en-us/article/pearson-function-0c3e30fc-e5af-49c4-808a-3ef66e034c18)
    

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