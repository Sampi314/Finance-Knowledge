# Get percent change - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-percent-change

---

[Skip to main content](https://exceljet.net/formulas/get-percent-change#main-content)

[](https://exceljet.net/formulas/get-percent-change#)

*   [Previous](https://exceljet.net/formulas/get-original-price-from-percentage-discount)
    
*   [Next](https://exceljet.net/formulas/get-percentage-discount)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Get percent change
==================

by Dave Bruns · Updated 28 Feb 2019

![Excel formula: Get percent change](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20percent%20change2.png "Excel formula: Get percent change")

Summary
-------

To calculate the percentage change between two values in Excel, you can use a formula that divides the difference between two values by the "old" value. In the example shown, E6 contains this formula:

    =(D6-C6)/C6
    

When formatted as a percentage with zero decimal places, the result is 7%.

Generic formula
---------------

    =(new_value-old_value)/old_value

Explanation 
------------

Following order of operations, Excel first calculates the difference between the values (the actual change in sales) then divides that result by the original, or "old" value to get the decimal value -0.3435:

    =(D6-C6)/C6
    =(49500-75400)/75400
    =-25900/75400
    =0.0688
    

_Note: you must format the result using Percentage number format to display the final result as 7%_

Related formulas
----------------

[![Excel formula: Calculate percent variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20percent%20variance.png "Excel formula: Calculate percent variance")](https://exceljet.net/formulas/calculate-percent-variance)

### [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)

In this example, the goal is to calculate the variance between a Forecast (column C) and Actual (column D) as a percentage. For example, with a Forecast value of 100,000 and an Actual value of 112,000, we want to return a variance of 12%. The concept of variance requires a baseline value and a "new...

[![Excel formula: Get original number from percent change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20original%20number%20from%20percent%20change_0.png "Excel formula: Get original number from percent change")](https://exceljet.net/formulas/get-original-number-from-percent-change)

### [Get original number from percent change](https://exceljet.net/formulas/get-original-number-from-percent-change)

In this example, the goal is to calculate the "original" value when the current value and percentage change are known. For example, if we know the current value is 1100, after an increase of 10%, we want to calculate the original value (1000) with an Excel formula. Although the language may vary,...

[![Excel formula: Percent sold](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20sold_0.png "Excel formula: Percent sold")](https://exceljet.net/formulas/percent-sold)

### [Percent sold](https://exceljet.net/formulas/percent-sold)

In this example, the goal is to calculate the percentage sold for each item listed in the table, where original number (Total) is in column C and the Sold number is in column D. In other words, if we know we started with 144 apples, and sold 108 apples, we want to calculate that 75% of the apples...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)
    
*   [Get original number from percent change](https://exceljet.net/formulas/get-original-number-from-percent-change)
    
*   [Percent sold](https://exceljet.net/formulas/percent-sold)
    

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