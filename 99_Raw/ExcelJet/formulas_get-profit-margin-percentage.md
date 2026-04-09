# Get profit margin percentage - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-profit-margin-percentage

---

[Skip to main content](https://exceljet.net/formulas/get-profit-margin-percentage#main-content)

[](https://exceljet.net/formulas/get-profit-margin-percentage#)

*   [Previous](https://exceljet.net/formulas/get-percentage-of-total)
    
*   [Next](https://exceljet.net/formulas/get-total-from-percentage)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Get profit margin percentage
============================

by Dave Bruns · Updated 19 May 2021

![Excel formula: Get profit margin percentage](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20profit%20margin%20percentage_0.png "Excel formula: Get profit margin percentage")

Summary
-------

To calculate profit margin as a percentage with a formula, subtract the cost from the price and divide the result by the price. In the example shown, the formula in cell E5 is:

    =(C5-D5)/C5
    

The results in column E are _decimal values_ with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Generic formula
---------------

    =(price-cost)/price

Explanation 
------------

In this example, the goal is to calculate and display profit margin as a percentage for each of the items shown in the table. In other words, given a price of $5.00 and a cost  of $4.00, we want to return a profit margin of 20%. Each item in the table has different price and cost, so the profit varies across items. 

Profit margin is the ratio of profit divided by revenue. The general formula where "x" is profit margin is:

    x=profit/price
    

In the table shown, we have price and cost, but profit is not broken out separately in another column, so we need to calculate profit by subtracting Cost from Price:

    x=(price-cost)/price
    x=(5-4)/5
    x=1/5
    x=0.20
    

and profit is calculated by subtracting Cost from Price. After we convert this to an Excel formula with cell references, we have this formula in E5:

    =(C5-D5)/C5
    =(5-4)/5
    =1/5
    =0.20
    

Make sure you use parentheses to control the [order of operations](https://exceljet.net/glossary/order-of-operations)
. As the formula is copied down, we get profit margin for each item in the table. Note the result will be a decimal number like .10, .25, .30, etc. To display this result as a percentage, apply [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
. You can use the [shortcut](https://exceljet.net/shortcuts)
 Control + Shift + %.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 95% is read as "Ninety-five percent" and is equivalent to 95/100 or 0.95. To display these numbers with a percent sign (%), apply [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
. To convert these numbers to a whole number like 95, multiply by 100:

    =(C5-D5)/C5*100
    

Then apply a standard [number format](https://exceljet.net/glossary/number-format)
 of your choice.

Related formulas
----------------

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

[![Excel formula: Get percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20discount_0.png "Excel formula: Get percentage discount")](https://exceljet.net/formulas/get-percentage-discount)

### [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)

In this example, the goal is to determine the percentage discount for each item shown in the table, given an original price and a sale price. In other words, given the Charcoal grill has an original price of $70.00 and a Sale Price of $59.50, we want to calculate a percentage discount of 15%, based...

[![Excel formula: Calculate percent variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20percent%20variance.png "Excel formula: Calculate percent variance")](https://exceljet.net/formulas/calculate-percent-variance)

### [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)

In this example, the goal is to calculate the variance between a Forecast (column C) and Actual (column D) as a percentage. For example, with a Forecast value of 100,000 and an Actual value of 112,000, we want to return a variance of 12%. The concept of variance requires a baseline value and a "new...

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

*   [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)
    
*   [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)
    
*   [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)
    
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