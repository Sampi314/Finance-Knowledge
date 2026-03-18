# Get total from percentage - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-total-from-percentage

---

[Skip to main content](https://exceljet.net/formulas/get-total-from-percentage#main-content)

[](https://exceljet.net/formulas/get-total-from-percentage#)

*   [Previous](https://exceljet.net/formulas/get-profit-margin-percentage)
    
*   [Next](https://exceljet.net/formulas/increase-by-percentage)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Get total from percentage
=========================

by Dave Bruns · Updated 17 May 2021

![Excel formula: Get total from percentage](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20total%20from%20percent_0.png "Excel formula: Get total from percentage")

Summary
-------

To calculate a total when you know the amount and percentage of one part of the total, you can use a formula that simply divides the amount by the percentage. In the example shown, the formula in E6, copied down, is:

    =C6/D6
    

Generic formula
---------------

    =amount/percentage

Explanation 
------------

In this example, the goal is to work out the total of _all expenses_ using a known percent of total of _any one expense_. If we know groceries are $200 and we know groceries represent 10.3% of total expenses, we want to calculate the total of all expenses ($1945). In other words, $200 is 10.3% of what number? With "x" as the number we want to find, we have:

    25%*x=200
    0.25*x=200
    x=200/0.25
    x=1945
    

So, to perform this calculation in Excel, we need to divide the amount of the expense in column C by the percentage that expense represents in column D like this:

    =amount/percentage
    

In the example, the active cell E6, copied down, is:

    =C6/D6
    

Excel simply divides the value in cell C6 by the percentage value in cell D6:

    =700/0.359897 // returns 1945
    

The result is the number 1945 , which is the total of all expenses in this case. As the formula is copied down the table, the result is the same at each new row, since total for all expenses remains the same. 

The formula in cell C15 uses the [SUM function](https://exceljet.net/functions/sum-function)
 to check the results in column E:

    =SUM(C6:C14) // returns 1945
    

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 85% is read as "Eighty-five percent" and is equivalent to 85/100 or 0.85. Accordingly, the values in column D are decimal values.  For example, D6 is approximately 0.36, D7 is approximately 0.18, etc.

To format a number like this as a percentage with the percent sign (%), apply the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

Related formulas
----------------

[![Excel formula: Get amount with percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20amount%20with%20percent_0.png "Excel formula: Get amount with percentage")](https://exceljet.net/formulas/get-amount-with-percentage)

### [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)

In this example, the goal is to convert the percentages shown in column C to amounts, where the total of all amounts is given as $1945. In other words, if we know Rent is 36.0%, and the total of all expenses is $1945, we want to calculate that Rent is $700. With "x" as the number we want to find,...

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

[![Excel formula: Get percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20discount_0.png "Excel formula: Get percentage discount")](https://exceljet.net/formulas/get-percentage-discount)

### [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)

In this example, the goal is to determine the percentage discount for each item shown in the table, given an original price and a sale price. In other words, given the Charcoal grill has an original price of $70.00 and a Sale Price of $59.50, we want to calculate a percentage discount of 15%, based...

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

[![Excel formula: Summary count with percentage breakdown](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20%20couunt%20with%20percentage%20breakdown_0.png "Excel formula: Summary count with percentage breakdown")](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

### [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

In this example, the goal is to calculate a count and percentage for each category shown in column B. For convenience, the category values in column B are in the named range category (B5:B122). To generate the count, we use the COUNTIF function . The formula in G5, copied through the range G5:G9 is...

[![Excel formula: Percent of goal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20goal.png "Excel formula: Percent of goal")](https://exceljet.net/formulas/percent-of-goal)

### [Percent of goal](https://exceljet.net/formulas/percent-of-goal)

In this example, the objective is to calculate a percentage for each goal shown in column C of the table using the actual values in column D. In other words, given a goal of 100000, and an actual amount of 112000, we want to return 112% as the result. The general formula for this calculation, where...

[![Excel formula: Percent of students absent](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20students%20absent.png "Excel formula: Percent of students absent")](https://exceljet.net/formulas/percent-of-students-absent)

### [Percent of students absent](https://exceljet.net/formulas/percent-of-students-absent)

In this example, the goal is to answer the question "What percentage of students were absent from each class". In other words, given a class with 30 students total, 27 of which were present, we want to return 10% absent. The general formula for this calculation, where "x" is the percent absent is:...

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

*   [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)
    
*   [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)
    
*   [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)
    
*   [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)
    
*   [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)
    
*   [Get original price from percentage discount](https://exceljet.net/formulas/get-original-price-from-percentage-discount)
    
*   [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    
*   [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    
*   [Percent of goal](https://exceljet.net/formulas/percent-of-goal)
    
*   [Percent of students absent](https://exceljet.net/formulas/percent-of-students-absent)
    

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