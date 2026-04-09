# Excel GROWTH function | Exceljet

**Source:** https://exceljet.net/functions/growth-function

---

[Skip to main content](https://exceljet.net/functions/growth-function#main-content)

[](https://exceljet.net/functions/growth-function#)

*   [Previous](https://exceljet.net/functions/geomean-function)
    
*   [Next](https://exceljet.net/functions/harmean-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

GROWTH Function
===============

by Kurt Bruns · Updated 23 Aug 2025

Related functions 
------------------

[FORECAST](https://exceljet.net/functions/forecast-function)

[LINEST](https://exceljet.net/functions/linest-function)

![Excel GROWTH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_growth_function_main_screenshot_cropped.png "Excel GROWTH function")

Summary
-------

The Excel GROWTH function returns values along an exponential trend. GROWTH returns the y-values for a series of new x-values that you specify. The function fits an exponential curve to existing data and predicts future values based on that curve.

Purpose 
--------

Forecast exponential growth by fitting an exponential curve to existing data and predicts values.

Return value 
-------------

Returns an array of predicted y-values for the specified new x-values.

Syntax
------

    =GROWTH(known_y,[known_x],[new_x],const)

*   _known\_y_ - The set of y-values you already know in the relationship y = b\*m^x.
*   _known\_x_ - \[optional\] The set of x-values that correspond to known\_y. If omitted, known\_x is assumed to be {1,2,3,...}.
*   _new\_x_ - \[optional\] The new x-values for which you want GROWTH to return corresponding y-values. If omitted, new\_x is assumed to be the same as known\_x.
*   _const_ - A logical value that controls whether the exponential curve starts at a calculated base value or at 1. If TRUE or omitted, the function calculates the optimal starting value (b) for the curve y = b\*m^x. If FALSE, the function forces the curve to start at 1, using the form y = m^x.

Using the GROWTH function 
--------------------------

The GROWTH function calculates exponential growth predictions based on existing data points. It fits an exponential curve (y = b\*m^x) to your known data and then uses that curve to predict future values. GROWTH is particularly useful for forecasting trends that follow exponential patterns, such as population growth, compound interest, or viral spread.

### Key features

*   Fits an exponential curve to existing data points
*   Predicts values based on the fitted curve
*   Can be used for both interpolation and extrapolation

> GROWTH assumes your data follows an exponential pattern y = b\*m^x or y = m^x . If your data follows a different pattern (linear, logarithmic, etc.), consider using the related functions listed above instead.

### Table of contents

*   [Key features](https://exceljet.net/functions/growth-function#key-features)
    
*   [Example #1 - Basic GROWTH calculation](https://exceljet.net/functions/growth-function#example-1---basic-growth-calculation)
    
*   [Example #2 - Predict future and past values](https://exceljet.net/functions/growth-function#example-2---predict-future-and-past-values)
    
*   [Example #3 - Interpolate fractional values](https://exceljet.net/functions/growth-function#example-3---interpolate-fractional-values)
    
*   [Example #4 - Using the const parameter](https://exceljet.net/functions/growth-function#example-4---using-the-const-parameter)
    
*   [Example #5 - Error Conditions](https://exceljet.net/functions/growth-function#example-5---error-conditions)
    
*   [How it works](https://exceljet.net/functions/growth-function#how-it-works)
    
*   [Notes](https://exceljet.net/functions/growth-function#notes)
    

### Example #1 - Basic GROWTH calculation

The GROWTH function takes up to four arguments in this syntax:

    =GROWTH(known_y, [known_x], [new_x], [const])
    

In its simplest form, you can use GROWTH with known y-values and x-values, plus new x-values for prediction. Here is an example:

    =GROWTH({100,150},{1,2},{2,3,4}) // spills {150,225,337.5}
    

The function fits an exponential curve to your data and returns predicted values for the specified new x-values.

### Example #2 - Predict future and past values

In the example below, we have data for years 3-7 and want to predict values for years 0-10 (both past and future). The formula in cell F5 is:

    =GROWTH(C5:C9,B5:B9,E5:E15)
    

![GROWTH function example - predict future and past values](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_growth_function_predict_values_screenshot_cropped.png "GROWTH function example - predict future and past values")

The GROWTH function:  
1\. Fits an exponential curve to the known data (years 3-7)  
2\. Uses that curve to predict values for the new x-values  
3\. Returns the predicted values as an array, showing both past predictions (years 0-2) and future predictions (years 8-10)

> **Note:** The predicted values for the known data points (years 3-7) may differ slightly from the actual values shown in the data. This is because GROWTH fits the best exponential curve to all the data points, and the curve may not pass exactly through each individual point. The function prioritizes finding the overall exponential trend rather than matching each data point exactly.

### Example #3 - Interpolate fractional values

In this example, we use GROWTH to interpolate values between existing data points, including fractional years. Imagine a business that has enjoyed exceptional growth over the past 5 years and wants to track their progress quarterly to ensure they're on track for the next year. We have data for years 3-7 and want to find values for each quarter between years 6 and 8. The fractional years represent quarters:

*   6.00 = Start of year 6 (Q1)
*   6.25 = End of Q1 in year 6
*   6.50 = End of Q2 in year 6
*   6.75 = End of Q3 in year 6
*   7.00 = End of Q4 in year 6
*   And so on...

The formula in cell F5 is:

    =GROWTH(D5:D9,C5:C9,E5:E13)
    

![GROWTH function example - interpolate fractional values](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_growth_function_interpolate_values_screenshot_cropped.png "GROWTH function example - interpolate fractional values")

The GROWTH function:  
1\. Fits an exponential curve to the known data points (years 3-7)  
2\. Uses that curve to calculate values for the specified x-values  
3\. Returns the interpolated values as an array, showing predictions for fractional time periods

### Example #4 - Using the const parameter

The `const` parameter controls whether the exponential curve starts at one or some base amount at x=0. For example, when `const=TRUE` (the default behavior), GROWTH calculates the optimal starting value by fitting the best exponential curve of the form y = b\*m^x, where both b and m are calculated to best fit your data:

    =GROWTH(C5:C9,B5:B9,E5:E15,TRUE)
    

![GROWTH function example - const=TRUE](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_growth_function_const_true_screenshot_cropped.png "GROWTH function example - const=TRUE")

In this case, the function fits the exponential curve to the data, where the starting value is b = 16,469.13 and the growth rate is m ≈ 1.737.

In contrast, when `const=FALSE`, GROWTH sets the constant b to equal 1, fitting the curve y = m^x:

    =GROWTH(C5:C9,B5:B9,E5:E15,FALSE)
    

![GROWTH function example - const=FALSE](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_growth_function_const_false_screenshot_cropped.png "GROWTH function example - const=FALSE")

With `const=FALSE`, the function sets b = 1, so the curve passes through (0,1), and calculates the value for m (growth rate) that best fits the data. For this data, setting `const` to FALSE does not produce a better fit. The constraint of forcing the curve through (0,1) creates a much steeper growth rate that overestimates the actual values by orders of magnitude.

You should use `const=FALSE` when it makes sense for the exponential curve to start at 1. For example, when working with relative growth rates where the starting point is naturally one.

### Example #5 - Error Conditions

The GROWTH function returns #NUM! if any of the known\_y values are zero or negative.

    =GROWTH({0,4,8},{1,2,3}) // returns #NUM!
    

The GROWTH function returns #VALUE! if any arguments are non-numeric.

    =GROWTH({"1",4,8},{1,2,3}) // returns #VALUE!
    

The Growth function returns #REF! if the known\_x and new\_x arrays have different lengths.

    =GROWTH({2,4,8},{1,2}) // returns #REF!
    

### How it works

The GROWTH function fits an exponential curve to your data and returns predicted values for the specified new x-values. The curve is defined by the equation:

`y = b * m^x`

Where:  
\- `b` is the base amount  
\- `m` is the growth multiplier  
\- `x` is the independent variable (time)

To calculate the exponential curve manually, we use an equivalent form that makes the calculations easier:

`y = b * EXP(k * x)`

Where:  
\- `EXP` is the [Exponential function](https://exceljet.net/functions/exp-function)
  
\- `k` is the growth coefficient (related to `m` by `m = EXP(k)`)  
\- `b` and `x` are the same as above

This form makes it easier to calculate the growth coefficient and base amount manually using Excel's [SLOPE](https://exceljet.net/functions/slope-function)
 and [INTERCEPT](https://exceljet.net/functions/intercept-function)
 functions.

**Step 1: Calculate growth coefficient** `**k**`**:**

To calculate the growth coefficient `k`, we calculate the natural log of the y-values and then use the SLOPE function to calculate the slope of the line.

    =SLOPE(ln_y_values, x_values) // returns k
    

**Step 2: Calculate base amount** `**b**`**:**

To calculate the base amount `b`, we use the INTERCEPT function to calculate the y-intercept of the line, then apply the exponential function.

    =EXP(INTERCEPT(ln_y_values, x_values)) // returns b
    

**Step 3: Predict values:**

To predict values using the exponential curve, we use the formula:

    =b * EXP(k * new_x)
    

This returns the same results as the GROWTH function. For example, given data that starts at 10 and doubles each time (10, 20, 40, 80, 160, 320, 640), we can calculate the exponential curve manually as shown in the screenshot below.

![Manual exponential growth implementation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_growth_function_how_it_works_screenshot_cropped.png "Manual exponential growth implementation")

**Step 4: (Optional) Calculate growth multiplier** `**m**`**:**

If you prefer to write the exponential curve in the form `y = b*m^x` instead of `y = b * EXP(k * x)`, you can calculate the growth multiplier `m` by applying the exponential function to the growth coefficient `k`:

    =EXP(k) // returns m
    

Then you can write the prediction formula as:

    =b * m^x
    

This gives you the same exponential curve, just expressed in a different form.

### Notes

*   GROWTH is an array function that returns multiple values when you specify multiple new\_x values.
*   In Excel 365, simply press Enter to enter the formula. In Excel 2019 and earlier, use Ctrl+Shift+Enter for array formulas.
*   When using GROWTH with a single new\_x value, it returns a single result and behaves like a regular function.

Related functions
-----------------

[![Excel FORECAST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/forecast%20function.png "Excel FORECAST function")](https://exceljet.net/functions/forecast-function)

### [FORECAST Function](https://exceljet.net/functions/forecast-function)

The Excel FORECAST function predicts a value based on existing values along a linear trend. FORECAST calculates future value predictions using linear regression, and can be used to predict numeric values like sales, inventory, expenses, measurements, etc.

_Note: Starting with_...

[![Excel LINEST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20linest%20function.png "Excel LINEST function")](https://exceljet.net/functions/linest-function)

### [LINEST Function](https://exceljet.net/functions/linest-function)

The Excel LINEST function returns statistics for a best fit straight line through supplied x and y values. The values returned by LINEST include slope, intercept, standard error values, and more. To find the best fit of a line to the data, LINEST uses the "least squares" method....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FORECAST Function](https://exceljet.net/functions/forecast-function)
    
*   [LINEST Function](https://exceljet.net/functions/linest-function)
    

### Links

*   [Microsoft GROWTH function documentation](https://support.office.com/en-us/article/growth-function-541a91dc-3d5e-437d-b156-21324e68b80d)
    

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