# Percent sold - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/percent-sold

---

[Skip to main content](https://exceljet.net/formulas/percent-sold#main-content)

[](https://exceljet.net/formulas/percent-sold#)

*   [Previous](https://exceljet.net/formulas/percent-of-students-absent)
    
*   [Next](https://exceljet.net/formulas/project-complete-percentage)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Percent sold
============

by Dave Bruns · Updated 19 May 2021

![Excel formula: Percent sold](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/percent%20sold_0.png "Excel formula: Percent sold")

Summary
-------

To calculate the percentage sold any given item you can use a simple formula that divides sold amount by the total amount. In the example shown, the formula in E6 is

    =D6/C6
    

The results in column E are decimal values with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Generic formula
---------------

    =sold/total

Explanation 
------------

In this example, the goal is to calculate the percentage sold for each item listed in the table, where original number (Total) is in column C and the Sold number is in column D. In other words, if we know we started with 144 apples, and sold 108 apples, we want to calculate that 75% of the apples were sold. The general formula for this calculation, where "x" is the percentage sold, is:

    x=total/sold
    x=144/108
    x=0.75
    

Converting this to an Excel formula with cell references, the formula in E5 becomes:

    =C5/D5
    =144/108
    =0.75
    

When the result the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 is applied, 0.75 is displayed as 75%. As the formula is copied down, the formula returns percentage sold for item in the table.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 45% is read as "Forty-five percent" and is equivalent to 45/100 or 0.45. Accordingly, the results in column E are _decimal values_, with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Related formulas
----------------

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

[![Excel formula: Percent of goal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20goal.png "Excel formula: Percent of goal")](https://exceljet.net/formulas/percent-of-goal)

### [Percent of goal](https://exceljet.net/formulas/percent-of-goal)

In this example, the objective is to calculate a percentage for each goal shown in column C of the table using the actual values in column D. In other words, given a goal of 100000, and an actual amount of 112000, we want to return 112% as the result. The general formula for this calculation, where...

[![Excel formula: Get amount with percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20amount%20with%20percent_0.png "Excel formula: Get amount with percentage")](https://exceljet.net/formulas/get-amount-with-percentage)

### [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)

In this example, the goal is to convert the percentages shown in column C to amounts, where the total of all amounts is given as $1945. In other words, if we know Rent is 36.0%, and the total of all expenses is $1945, we want to calculate that Rent is $700. With "x" as the number we want to find,...

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

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

*   [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)
    
*   [Percent of goal](https://exceljet.net/formulas/percent-of-goal)
    
*   [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)
    
*   [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)
    
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