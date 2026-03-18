# Get original number from percent change - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-original-number-from-percent-change

---

[Skip to main content](https://exceljet.net/formulas/get-original-number-from-percent-change#main-content)

[](https://exceljet.net/formulas/get-original-number-from-percent-change#)

*   [Previous](https://exceljet.net/formulas/get-amount-with-percentage)
    
*   [Next](https://exceljet.net/formulas/get-original-price-from-percentage-discount)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Get original number from percent change
=======================================

by Dave Bruns · Updated 4 Jun 2024

![Excel formula: Get original number from percent change](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20original%20number%20from%20percent%20change_0.png "Excel formula: Get original number from percent change")

Summary
-------

To calculate the original number based on current value and known percentage change, you can use a simple formula that divides the current value by the percent + 1. In the example shown, the formula in cell E5 is:

    =D5/(C5+1)
    

The results in column E are decimal values with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Generic formula
---------------

    =current/(percent+1)

Explanation 
------------

In this example, the goal is to calculate the "original" value when the current value and percentage change are known. For example, if we know the current value is 1100, after an increase of 10%, we want to calculate the original value (1000) with an Excel formula. Although the language may vary, this kind of formula can be used in different ways:

*   To calculate an original value based on a known percentage change.
*   To calculate an original amount after a specific markup has been applied.
*   To calculate a pre-tax value after a specific tax rate has already been applied.

### General formula

Assuming a current value of 1100 and a after a known increase of 10%, the general formula for this calculation, where "x" is the original number, is:

    x=current/(percentage+1)
    x=1100/(10%+1)
    x=1100/1.10
    x=1000
    

### Excel formula

Converting this to an Excel formula with cell references, the formula in E5 becomes:

    =D5/(C5+1)
    =1100/(0.1+1)
    =1100/1.1
    =1000
    

As the formula is copied down, the formula returns the original price for each item in the table, based on the percentages shown in column C and the current values in column D.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 65% is read as "Sixty-five percent" and is equivalent to 65/100 or 0.65. Accordingly, the values in column C are _decimal values_, with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Related formulas
----------------

[![Excel formula: Increase by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Increase%20by%20percent_0.png "Excel formula: Increase by percentage")](https://exceljet.net/formulas/increase-by-percentage)

### [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)

In this example, the goal is to increase the prices shown in column C by the percentages shown in column D. For example, given the original price of $70.00, and an increase of 10%, the result should be $77.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1+...

[![Excel formula: Decrease by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/decrease%20by%20percent.png "Excel formula: Decrease by percentage")](https://exceljet.net/formulas/decrease-by-percentage)

### [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)

In this example, the goal is to decrease the prices shown in column C by the percentages shown in column D. For example, given an original price of $70.00, and an decrease of 10% ($7.00), the result should be $63.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1...

[![Excel formula: Percent of goal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20goal.png "Excel formula: Percent of goal")](https://exceljet.net/formulas/percent-of-goal)

### [Percent of goal](https://exceljet.net/formulas/percent-of-goal)

In this example, the objective is to calculate a percentage for each goal shown in column C of the table using the actual values in column D. In other words, given a goal of 100000, and an actual amount of 112000, we want to return 112% as the result. The general formula for this calculation, where...

[![Excel formula: Calculate percent variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20percent%20variance.png "Excel formula: Calculate percent variance")](https://exceljet.net/formulas/calculate-percent-variance)

### [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)

In this example, the goal is to calculate the variance between a Forecast (column C) and Actual (column D) as a percentage. For example, with a Forecast value of 100,000 and an Actual value of 112,000, we want to return a variance of 12%. The concept of variance requires a baseline value and a "new...

[![Excel formula: Get percent change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20change2.png "Excel formula: Get percent change")](https://exceljet.net/formulas/get-percent-change)

### [Get percent change](https://exceljet.net/formulas/get-percent-change)

Following order of operations, Excel first calculates the difference between the values (the actual change in sales) then divides that result by the original, or "old" value to get the decimal value -0.3435: =(D6-C6)/C6 =(49500-75400)/75400 =-25900/75400 =0.0688 Note: you must format the result...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_percentage_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-percentage-formatting-in-excel)

### [How to use percentage formatting in Excel](https://exceljet.net/videos/how-to-use-percentage-formatting-in-excel)

In this lesson we'll look at the Percentage format. The Percentage format is made to display fractional values as percentages. For instance, the value .05, formatted as a percent, will display as 5%. Let's take a look. In column B of our table we have a set of numbers in General format. Let's first...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)
    
*   [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)
    
*   [Percent of goal](https://exceljet.net/formulas/percent-of-goal)
    
*   [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)
    
*   [Get percent change](https://exceljet.net/formulas/get-percent-change)
    

### Videos

*   [How to use percentage formatting in Excel](https://exceljet.net/videos/how-to-use-percentage-formatting-in-excel)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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