# Get percentage of total - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-percentage-of-total

---

[Skip to main content](https://exceljet.net/formulas/get-percentage-of-total#main-content)

[](https://exceljet.net/formulas/get-percentage-of-total#)

*   [Previous](https://exceljet.net/formulas/get-percentage-discount)
    
*   [Next](https://exceljet.net/formulas/get-profit-margin-percentage)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Get percentage of total
=======================

by Dave Bruns · Updated 17 May 2021

![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")

Summary
-------

To calculate the percent of a total (i.e. calculate a percent distribution), you can use a formula that simply divides a given amount by the total. In the example shown, the formula in D6 is:

    =C6/total
    

where **total** is the [named range](https://exceljet.net/glossary/named-range)
 C15.

_Note: the result is formatted with [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 to show 36%, 18%, etc._

Generic formula
---------------

    =amount/total

Explanation 
------------

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total.

The total already exists in the [named range](https://exceljet.net/glossary/named-range)
 **total** (C15) which contains a formula based on the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM(C6:C14)
    

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 85% is read as "Eighty-five percent" and is equivalent to 85/100 or 0.85. To calculate the "percent of total" for a given expense, we need to divide the amount of the expense by the total of all expenses. In cell D6, the ratio is 700/1945, which is approximately 0.36 (36% when [formatted](https://exceljet.net/glossary/number-format)
 as a percentage). The formula in D6, copied down, is:

    =C6/total // returns 0.3599
    

using the named range **total** (C15). Without the named range, we need to use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to "lock" the address to C15 so the reference doesn't change as the formula is copied down column D. The formula becomes:

    =C6/$C$15 // returns 0.3599
    

As the formula is copied down, we get a percent of total for each item shown in the table.

### Formatting percentages in Excel

The numbers in column D are decimal values that express a ratio. In cell D6, the ratio is 700/1945, which is approximately 0.36. To format a number like this as a percentage with the percent sign (%), apply the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

### Percentage vs. number

To display a percentage in Excel, use the Percentage [number format](https://exceljet.net/glossary/number-format)
, which will automatically display a decimal value as a percentage. If you want instead a simple number _without_ a percent sign, just multiply by 100:

    =(C6/total)*100
    =(C6/$C$15)*100
    

The result is a number like 36, 18, 12.9, etc.

Related formulas
----------------

[![Excel formula: Percent of goal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20goal.png "Excel formula: Percent of goal")](https://exceljet.net/formulas/percent-of-goal)

### [Percent of goal](https://exceljet.net/formulas/percent-of-goal)

In this example, the objective is to calculate a percentage for each goal shown in column C of the table using the actual values in column D. In other words, given a goal of 100000, and an actual amount of 112000, we want to return 112% as the result. The general formula for this calculation, where...

[![Excel formula: Get total from percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20total%20from%20percent_0.png "Excel formula: Get total from percentage")](https://exceljet.net/formulas/get-total-from-percentage)

### [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)

In this example, the goal is to work out the total of all expenses using a known percent of total of any one expense . If we know groceries are $200 and we know groceries represent 10.3% of total expenses, we want to calculate the total of all expenses ($1945). In other words, $200 is 10.3% of what...

[![Excel formula: Get percent change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20change2.png "Excel formula: Get percent change")](https://exceljet.net/formulas/get-percent-change)

### [Get percent change](https://exceljet.net/formulas/get-percent-change)

Following order of operations, Excel first calculates the difference between the values (the actual change in sales) then divides that result by the original, or "old" value to get the decimal value -0.3435: =(D6-C6)/C6 =(49500-75400)/75400 =-25900/75400 =0.0688 Note: you must format the result...

[![Excel formula: Increase by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Increase%20by%20percent_0.png "Excel formula: Increase by percentage")](https://exceljet.net/formulas/increase-by-percentage)

### [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)

In this example, the goal is to increase the prices shown in column C by the percentages shown in column D. For example, given the original price of $70.00, and an increase of 10%, the result should be $77.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1+...

[![Excel formula: Decrease by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/decrease%20by%20percent.png "Excel formula: Decrease by percentage")](https://exceljet.net/formulas/decrease-by-percentage)

### [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)

In this example, the goal is to decrease the prices shown in column C by the percentages shown in column D. For example, given an original price of $70.00, and an decrease of 10% ($7.00), the result should be $63.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1...

[![Excel formula: Get amount with percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20amount%20with%20percent_0.png "Excel formula: Get amount with percentage")](https://exceljet.net/formulas/get-amount-with-percentage)

### [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)

In this example, the goal is to convert the percentages shown in column C to amounts, where the total of all amounts is given as $1945. In other words, if we know Rent is 36.0%, and the total of all expenses is $1945, we want to calculate that Rent is $700. With "x" as the number we want to find,...

[![Excel formula: Get percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20discount_0.png "Excel formula: Get percentage discount")](https://exceljet.net/formulas/get-percentage-discount)

### [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)

In this example, the goal is to determine the percentage discount for each item shown in the table, given an original price and a sale price. In other words, given the Charcoal grill has an original price of $70.00 and a Sale Price of $59.50, we want to calculate a percentage discount of 15%, based...

[![Excel formula: Project complete percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/project%20complete%20percentage_0.png "Excel formula: Project complete percentage")](https://exceljet.net/formulas/project-complete-percentage)

### [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)

In this example if a task is marked "Done", then it is considered complete. The goal is to calculate the percent complete for the project by showing the ratio of complete tasks to total tasks, expressed as a percentage. The formula in F6 is: =COUNTA(C5:C11)/COUNTA(B5:B11) At the core, this formula...

[![Excel formula: Get original price from percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20original%20price%20from%20percent%20discount_0.png "Excel formula: Get original price from percentage discount")](https://exceljet.net/formulas/get-original-price-from-percentage-discount)

### [Get original price from percentage discount](https://exceljet.net/formulas/get-original-price-from-percentage-discount)

In this example, the goal is to determine the original price from a discounted price (sale price) and the percentage discount. For example, given a sale price of $60.00, and a discount of 10%, we want a result of $70.00 for the original price. The discounted price is in column C and the percentage...

[![Excel formula: Cap percentage at specific amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20specific%20amount.png "Excel formula: Cap percentage at specific amount")](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

### [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

This formula uses the MIN function to make a decision that might otherwise be handled with the IF function . Although MIN is usually used to return the minimum value in a data set with many numbers, it also works fine for the "lesser of the two" situations. Inside MIN, the value in C6 is multiplied...

[![Excel formula: Summary count with percentage breakdown](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20%20couunt%20with%20percentage%20breakdown_0.png "Excel formula: Summary count with percentage breakdown")](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

### [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

In this example, the goal is to calculate a count and percentage for each category shown in column B. For convenience, the category values in column B are in the named range category (B5:B122). To generate the count, we use the COUNTIF function . The formula in G5, copied through the range G5:G9 is...

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

[![Excel formula: Get profit margin percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20profit%20margin%20percentage_0.png "Excel formula: Get profit margin percentage")](https://exceljet.net/formulas/get-profit-margin-percentage)

### [Get profit margin percentage](https://exceljet.net/formulas/get-profit-margin-percentage)

In this example, the goal is to calculate and display profit margin as a percentage for each of the items shown in the table. In other words, given a price of $5.00 and a cost of $4.00, we want to return a profit margin of 20%. Each item in the table has different price and cost, so the profit...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Percent of goal](https://exceljet.net/formulas/percent-of-goal)
    
*   [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)
    
*   [Get percent change](https://exceljet.net/formulas/get-percent-change)
    
*   [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)
    
*   [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)
    
*   [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)
    
*   [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)
    
*   [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)
    
*   [Get original price from percentage discount](https://exceljet.net/formulas/get-original-price-from-percentage-discount)
    
*   [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    
*   [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    
*   [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)
    
*   [Get profit margin percentage](https://exceljet.net/formulas/get-profit-margin-percentage)
    

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