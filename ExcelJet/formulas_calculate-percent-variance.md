# Calculate percent variance - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-percent-variance

---

[Skip to main content](https://exceljet.net/formulas/calculate-percent-variance#main-content)

[](https://exceljet.net/formulas/calculate-percent-variance#)

*   [Previous](https://exceljet.net/formulas/split-full-name-into-parts)
    
*   [Next](https://exceljet.net/formulas/calculate-percentage-of-number)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Calculate percent variance
==========================

by Dave Bruns · Updated 30 Jul 2021

Related functions 
------------------

[ABS](https://exceljet.net/functions/abs-function)

![Excel formula: Calculate percent variance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20percent%20variance.png "Excel formula: Calculate percent variance")

Summary
-------

To calculate a percent variance, subtract the original (baseline) number from the new number, then divide that result by the original. In the example shown, the formula in E5, copied down, is:

    =(D5-C5)/C5
    

The results in column E are decimal values with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied. The same formula can be used to calculate things like variance between this year and last year, variance between a budget and actual values, and so on.

Generic formula
---------------

    =(new-baseline)/baseline

Explanation 
------------

In this example, the goal is to calculate the variance between a Forecast (column C) and Actual (column D) as a percentage. For example, with a Forecast value of 100,000 and an Actual value of 112,000, we want to return a variance of 12%.

The concept of variance requires a baseline value and a "new" value. The baseline value is subtracted from the new value and the result is divided by the baseline value. The general formula, where "x" is the variance, is:

    x=(new-baseline)/baseline
    x=(112,000-100,000)/100,000
    x=12,000/100,000
    x=0.12
    

After converting to an Excel formula with cell references, the formula in E5, copied down, is:

    =(D5-C5)/C5
    =(112,000-100,000)/100,000
    =12,000/100,000
    =0.12
    =12%
    

As the formula is copied down, it returns a decimal number for each item in the list. When these numbers are formatted with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
, they are displayed as percentages.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 25% is read as "Twenty-five percent" and is equivalent to 25/100 or 0.25. Accordingly, the values in column E are _decimal values_, with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied. To convert these values to a whole number like 12, multiply by 100:

    =(D5-C5)/C5*100
    

### Negative numbers

If you have a negative value for the original number, the above formula won't work and can be adjusted by adding the [ABS function](https://exceljet.net/functions/abs-function)
:

    =(new-original)/ABS(original)
    

ABS stands for "absolute value", and it converts negative values to positive values. In this case, the ABS function ensures the original value is positive when the variance is calculated.

_Note: be aware that results negative values can be misleading, as explained by Jon Acampora in his [detailed article on the topic](https://www.excelcampus.com/functions/percentage-change-formula-negative-numbers/)
._

Related formulas
----------------

[![Excel formula: Percent of goal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20goal.png "Excel formula: Percent of goal")](https://exceljet.net/formulas/percent-of-goal)

### [Percent of goal](https://exceljet.net/formulas/percent-of-goal)

In this example, the objective is to calculate a percentage for each goal shown in column C of the table using the actual values in column D. In other words, given a goal of 100000, and an actual amount of 112000, we want to return 112% as the result. The general formula for this calculation, where...

[![Excel formula: Get percent change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20change2.png "Excel formula: Get percent change")](https://exceljet.net/formulas/get-percent-change)

### [Get percent change](https://exceljet.net/formulas/get-percent-change)

Following order of operations, Excel first calculates the difference between the values (the actual change in sales) then divides that result by the original, or "old" value to get the decimal value -0.3435: =(D6-C6)/C6 =(49500-75400)/75400 =-25900/75400 =0.0688 Note: you must format the result...

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

[![Excel formula: Get profit margin percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20profit%20margin%20percentage_0.png "Excel formula: Get profit margin percentage")](https://exceljet.net/formulas/get-profit-margin-percentage)

### [Get profit margin percentage](https://exceljet.net/formulas/get-profit-margin-percentage)

In this example, the goal is to calculate and display profit margin as a percentage for each of the items shown in the table. In other words, given a price of $5.00 and a cost of $4.00, we want to return a profit margin of 20%. Each item in the table has different price and cost, so the profit...

[![Excel formula: Forecast vs actual variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/forecast%20vs%20actual%20variance.png "Excel formula: Forecast vs actual variance")](https://exceljet.net/formulas/forecast-vs-actual-variance)

### [Forecast vs actual variance](https://exceljet.net/formulas/forecast-vs-actual-variance)

This is a pretty standard use of the SUMIFS function. In this case, we need to sum amounts based on two criteria: type (forecast or actual) and group. To sum by type, the range/criteria pair is: type,G$4 where type is the named range D5:D14, and G4 is a mixed reference with the row locked in order...

Related functions
-----------------

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

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

*   [Percent of goal](https://exceljet.net/formulas/percent-of-goal)
    
*   [Get percent change](https://exceljet.net/formulas/get-percent-change)
    
*   [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)
    
*   [Get profit margin percentage](https://exceljet.net/formulas/get-profit-margin-percentage)
    
*   [Forecast vs actual variance](https://exceljet.net/formulas/forecast-vs-actual-variance)
    

### Functions

*   [ABS Function](https://exceljet.net/functions/abs-function)
    

### Videos

*   [How to use percentage formatting in Excel](https://exceljet.net/videos/how-to-use-percentage-formatting-in-excel)
    

### Links

*   [Percentage change with negative numbers (excelcampus.com)](https://www.excelcampus.com/functions/percentage-change-formula-negative-numbers/)
    

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