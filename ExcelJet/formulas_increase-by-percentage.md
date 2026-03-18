# Increase by percentage - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/increase-by-percentage

---

[Skip to main content](https://exceljet.net/formulas/increase-by-percentage#main-content)

[](https://exceljet.net/formulas/increase-by-percentage#)

*   [Previous](https://exceljet.net/formulas/get-total-from-percentage)
    
*   [Next](https://exceljet.net/formulas/percent-of-goal)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Increase by percentage
======================

by Dave Bruns · Updated 19 May 2021

![Excel formula: Increase by percentage](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Increase%20by%20percent_0.png "Excel formula: Increase by percentage")

Summary
-------

To increase a number by a certain percentage, you can use a simple formula that multiplies the number times the percentage + 1. In the example shown, the formula in cell E5 is:

    =C5*(1+D5)
    

The results in column E are decimal values with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Generic formula
---------------

    =number*(1+percent)

Explanation 
------------

In this example, the goal is to increase the prices shown in column C by the percentages shown in column D. For example, given the original price of $70.00, and an increase of 10%, the result should be $77.00. The general formula for this calculation, where "x" is the new price, is:

    x=old*(1+percentage)
    x=70*(1+10%)
    x=70*1.10
    x=77.00
    

Converting this to an Excel formula with cell references, the formula in E5 becomes:

    =C5*(1+D5)
    =70*(1+0.1)
    =70*1.10
    =77.00
    

As the formula is copied down, the formula returns a new price for each item in the table, based on the percentages shown in column D.

### Negative percentages

Negative percentages will have the effect of _decreasing_ the original price. For example, with -10% in cell D5 (-0.10), the formula evaluates like this:

    =C5*(1+D5)
    =70*(1+-0.1)
    =70*0.9
    =63.00
    

[This example](https://exceljet.net/formulas/increase-by-percentage)
 explains the general formula for _increasing_ a number by a given percentage.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 95% is read as "Ninety-five percent" and is equivalent to 95/100 or 0.95. Accordingly, the values in column D are decimal values, with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Related formulas
----------------

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

[![Excel formula: Get total from percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20total%20from%20percent_0.png "Excel formula: Get total from percentage")](https://exceljet.net/formulas/get-total-from-percentage)

### [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)

In this example, the goal is to work out the total of all expenses using a known percent of total of any one expense . If we know groceries are $200 and we know groceries represent 10.3% of total expenses, we want to calculate the total of all expenses ($1945). In other words, $200 is 10.3% of what...

[![Excel formula: Get percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20discount_0.png "Excel formula: Get percentage discount")](https://exceljet.net/formulas/get-percentage-discount)

### [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)

In this example, the goal is to determine the percentage discount for each item shown in the table, given an original price and a sale price. In other words, given the Charcoal grill has an original price of $70.00 and a Sale Price of $59.50, we want to calculate a percentage discount of 15%, based...

[![Excel formula: Decrease by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/decrease%20by%20percent.png "Excel formula: Decrease by percentage")](https://exceljet.net/formulas/decrease-by-percentage)

### [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)

In this example, the goal is to decrease the prices shown in column C by the percentages shown in column D. For example, given an original price of $70.00, and an decrease of 10% ($7.00), the result should be $63.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1...

[![Excel formula: Get percent change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20change2.png "Excel formula: Get percent change")](https://exceljet.net/formulas/get-percent-change)

### [Get percent change](https://exceljet.net/formulas/get-percent-change)

Following order of operations, Excel first calculates the difference between the values (the actual change in sales) then divides that result by the original, or "old" value to get the decimal value -0.3435: =(D6-C6)/C6 =(49500-75400)/75400 =-25900/75400 =0.0688 Note: you must format the result...

[![Excel formula: Calculate percent variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20percent%20variance.png "Excel formula: Calculate percent variance")](https://exceljet.net/formulas/calculate-percent-variance)

### [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)

In this example, the goal is to calculate the variance between a Forecast (column C) and Actual (column D) as a percentage. For example, with a Forecast value of 100,000 and an Actual value of 112,000, we want to return a variance of 12%. The concept of variance requires a baseline value and a "new...

[![Excel formula: Get original number from percent change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20original%20number%20from%20percent%20change_0.png "Excel formula: Get original number from percent change")](https://exceljet.net/formulas/get-original-number-from-percent-change)

### [Get original number from percent change](https://exceljet.net/formulas/get-original-number-from-percent-change)

In this example, the goal is to calculate the "original" value when the current value and percentage change are known. For example, if we know the current value is 1100, after an increase of 10%, we want to calculate the original value (1000) with an Excel formula. Although the language may vary,...

[![Excel formula: Get original price from percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20original%20price%20from%20percent%20discount_0.png "Excel formula: Get original price from percentage discount")](https://exceljet.net/formulas/get-original-price-from-percentage-discount)

### [Get original price from percentage discount](https://exceljet.net/formulas/get-original-price-from-percentage-discount)

In this example, the goal is to determine the original price from a discounted price (sale price) and the percentage discount. For example, given a sale price of $60.00, and a discount of 10%, we want a result of $70.00 for the original price. The discounted price is in column C and the percentage...

[![Excel formula: Cap percentage at specific amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20specific%20amount.png "Excel formula: Cap percentage at specific amount")](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

### [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

This formula uses the MIN function to make a decision that might otherwise be handled with the IF function . Although MIN is usually used to return the minimum value in a data set with many numbers, it also works fine for the "lesser of the two" situations. Inside MIN, the value in C6 is multiplied...

[![Excel formula: Percent sold](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20sold_0.png "Excel formula: Percent sold")](https://exceljet.net/formulas/percent-sold)

### [Percent sold](https://exceljet.net/formulas/percent-sold)

In this example, the goal is to calculate the percentage sold for each item listed in the table, where original number (Total) is in column C and the Sold number is in column D. In other words, if we know we started with 144 apples, and sold 108 apples, we want to calculate that 75% of the apples...

[![Excel formula: Percent of students absent](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20students%20absent.png "Excel formula: Percent of students absent")](https://exceljet.net/formulas/percent-of-students-absent)

### [Percent of students absent](https://exceljet.net/formulas/percent-of-students-absent)

In this example, the goal is to answer the question "What percentage of students were absent from each class". In other words, given a class with 30 students total, 27 of which were present, we want to return 10% absent. The general formula for this calculation, where "x" is the percent absent is:...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)
    
*   [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)
    
*   [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)
    
*   [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)
    
*   [Get percent change](https://exceljet.net/formulas/get-percent-change)
    
*   [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)
    
*   [Get original number from percent change](https://exceljet.net/formulas/get-original-number-from-percent-change)
    
*   [Get original price from percentage discount](https://exceljet.net/formulas/get-original-price-from-percentage-discount)
    
*   [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    
*   [Percent sold](https://exceljet.net/formulas/percent-sold)
    
*   [Percent of students absent](https://exceljet.net/formulas/percent-of-students-absent)
    

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