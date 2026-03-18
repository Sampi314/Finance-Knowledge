# Get original price from percentage discount - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-original-price-from-percentage-discount

---

[Skip to main content](https://exceljet.net/formulas/get-original-price-from-percentage-discount#main-content)

[](https://exceljet.net/formulas/get-original-price-from-percentage-discount#)

*   [Previous](https://exceljet.net/formulas/get-original-number-from-percent-change)
    
*   [Next](https://exceljet.net/formulas/get-percent-change)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Get original price from percentage discount
===========================================

by Dave Bruns · Updated 21 May 2021

![Excel formula: Get original price from percentage discount](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20original%20price%20from%20percent%20discount_0.png "Excel formula: Get original price from percentage discount")

Summary
-------

To calculate the original price from a sale price and percentage discount, you can use a formula that divides the sale price by 1 minus the discount percentage. In the example shown, the formula in cell E5 is:

    =C5/(1-D5)
    

The results in column E are decimal values with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Generic formula
---------------

    =price/(1-discount)

Explanation 
------------

In this example, the goal is to determine the original price from a discounted price (sale price) and the percentage discount. For example, given a sale price of $60.00, and a discount of 10%, we want a result of $70.00 for the original price. The discounted price is in column C and the percentage discount is in column D. The general formula for this calculation, where "x" is the original price, is:

    x=price/(1-discount)
    x=63/(1-10%)
    x=63/(0.90)
    x=70.00
    

Converting this to an Excel formula with cell references, the formula in E5 becomes:

    =C5/(1-D5)
    =63/(1-0.1)
    =63/0.9
    =70.00
    

As the formula is copied down, it returns the original for each item in the table, based on the percentages shown in column D.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 95% is read as "ninety-five percent" and is equivalent to 95/100 or 0.95. Accordingly, the values in column D are decimal values, with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
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

[![Excel formula: Get total from percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20total%20from%20percent_0.png "Excel formula: Get total from percentage")](https://exceljet.net/formulas/get-total-from-percentage)

### [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)

In this example, the goal is to work out the total of all expenses using a known percent of total of any one expense . If we know groceries are $200 and we know groceries represent 10.3% of total expenses, we want to calculate the total of all expenses ($1945). In other words, $200 is 10.3% of what...

[![Excel formula: Get amount with percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20amount%20with%20percent_0.png "Excel formula: Get amount with percentage")](https://exceljet.net/formulas/get-amount-with-percentage)

### [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)

In this example, the goal is to convert the percentages shown in column C to amounts, where the total of all amounts is given as $1945. In other words, if we know Rent is 36.0%, and the total of all expenses is $1945, we want to calculate that Rent is $700. With "x" as the number we want to find,...

[![Excel formula: Get percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20discount_0.png "Excel formula: Get percentage discount")](https://exceljet.net/formulas/get-percentage-discount)

### [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)

In this example, the goal is to determine the percentage discount for each item shown in the table, given an original price and a sale price. In other words, given the Charcoal grill has an original price of $70.00 and a Sale Price of $59.50, we want to calculate a percentage discount of 15%, based...

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

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
    
*   [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)
    
*   [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)
    
*   [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)
    
*   [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)
    

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