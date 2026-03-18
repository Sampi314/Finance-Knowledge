# Get percentage discount - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-percentage-discount

---

[Skip to main content](https://exceljet.net/formulas/get-percentage-discount#main-content)

[](https://exceljet.net/formulas/get-percentage-discount#)

*   [Previous](https://exceljet.net/formulas/get-percent-change)
    
*   [Next](https://exceljet.net/formulas/get-percentage-of-total)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Get percentage discount
=======================

by Dave Bruns · Updated 17 May 2024

![Excel formula: Get percentage discount](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20percent%20discount_0.png "Excel formula: Get percentage discount")

Summary
-------

To calculate the percentage discount from an original price and a sale price, you can use a formula that divides the difference by the original price. In the example shown, the formula in E5, copied down, is:

    =(C5-D5)/C5
    

The result is a decimal value which is formatted with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

Generic formula
---------------

    =(original_price-sale_price)/original_price

Explanation 
------------

In this example, the goal is to determine the percentage discount for each item shown in the table, given an original price and a sale price. In other words, given the Charcoal grill has an original price of $70.00 and a Sale Price of $59.50, we want to calculate a percentage discount of 15%, based on a price decrease of $10.50. Note that a discount of 15% represents the price change ($10.50) expressed as a percentage of the original price. To solve for the percentage when the price change is known, we can use a general formula like this:

    original_price*x=price_change
    x=price_change/original_price
    x=10.50/70.00
    x =0.15
    

However, since the price change is not in the table as a separate column, we need to add a step:

    original_price*x=price_change
    original_price*x=(original_price-sale_price)
    x=(original_price-sale_price)/original_price
    x=(70.00-59.50)/70.00
    x=10.50/70.00
    x =0.15
    

Applying this approach to the worksheet as shown, the formula in cell E5, copied down, is:

    =(C5-D5)/C5
    =(70-59.5)/70
    =10.5/70
    =0.15
    

For each item in the table, Excel returns a calculated percentage.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 75% is read as "Seventy-five percent" and is equivalent to 75/100 or 0.75. Accordingly, the values in column E are decimals. To display these numbers as a percentage with the percent sign (%), the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 has been applied to E5:E15.

Related formulas
----------------

[![Excel formula: Get total from percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20total%20from%20percent_0.png "Excel formula: Get total from percentage")](https://exceljet.net/formulas/get-total-from-percentage)

### [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)

In this example, the goal is to work out the total of all expenses using a known percent of total of any one expense . If we know groceries are $200 and we know groceries represent 10.3% of total expenses, we want to calculate the total of all expenses ($1945). In other words, $200 is 10.3% of what...

[![Excel formula: Increase by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Increase%20by%20percent_0.png "Excel formula: Increase by percentage")](https://exceljet.net/formulas/increase-by-percentage)

### [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)

In this example, the goal is to increase the prices shown in column C by the percentages shown in column D. For example, given the original price of $70.00, and an increase of 10%, the result should be $77.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1+...

[![Excel formula: Decrease by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/decrease%20by%20percent.png "Excel formula: Decrease by percentage")](https://exceljet.net/formulas/decrease-by-percentage)

### [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)

In this example, the goal is to decrease the prices shown in column C by the percentages shown in column D. For example, given an original price of $70.00, and an decrease of 10% ($7.00), the result should be $63.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1...

[![Excel formula: Get original price from percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20original%20price%20from%20percent%20discount_0.png "Excel formula: Get original price from percentage discount")](https://exceljet.net/formulas/get-original-price-from-percentage-discount)

### [Get original price from percentage discount](https://exceljet.net/formulas/get-original-price-from-percentage-discount)

In this example, the goal is to determine the original price from a discounted price (sale price) and the percentage discount. For example, given a sale price of $60.00, and a discount of 10%, we want a result of $70.00 for the original price. The discounted price is in column C and the percentage...

[![Excel formula: Cap percentage at specific amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20specific%20amount.png "Excel formula: Cap percentage at specific amount")](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

### [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

This formula uses the MIN function to make a decision that might otherwise be handled with the IF function . Although MIN is usually used to return the minimum value in a data set with many numbers, it also works fine for the "lesser of the two" situations. Inside MIN, the value in C6 is multiplied...

[![Excel formula: Get profit margin percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20profit%20margin%20percentage_0.png "Excel formula: Get profit margin percentage")](https://exceljet.net/formulas/get-profit-margin-percentage)

### [Get profit margin percentage](https://exceljet.net/formulas/get-profit-margin-percentage)

In this example, the goal is to calculate and display profit margin as a percentage for each of the items shown in the table. In other words, given a price of $5.00 and a cost of $4.00, we want to return a profit margin of 20%. Each item in the table has different price and cost, so the profit...

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

*   [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)
    
*   [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)
    
*   [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)
    
*   [Get original price from percentage discount](https://exceljet.net/formulas/get-original-price-from-percentage-discount)
    
*   [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    
*   [Get profit margin percentage](https://exceljet.net/formulas/get-profit-margin-percentage)
    

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