# Percent of goal - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/percent-of-goal

---

[Skip to main content](https://exceljet.net/formulas/percent-of-goal#main-content)

[](https://exceljet.net/formulas/percent-of-goal#)

*   [Previous](https://exceljet.net/formulas/increase-by-percentage)
    
*   [Next](https://exceljet.net/formulas/percent-of-students-absent)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Percent of goal
===============

by Dave Bruns · Updated 19 May 2021

![Excel formula: Percent of goal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/percent%20of%20goal.png "Excel formula: Percent of goal")

Summary
-------

To calculate the percentage of a goal attained, you can use a simple formula that divides the actual by the goal amount, with the result formatted using the percentage number format. In the example shown, the formula in cell E5 is:

    =D5/C5
    

The results in column E are decimal values with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied. This same formula can be used to calculate things like percent of target, percent of budget, percent of forecast, and so on.

Generic formula
---------------

    =actual/goal

Explanation 
------------

In this example, the objective is to calculate a percentage for each goal shown in column C of the table using the actual values in column D. In other words, given a goal of 100000, and an actual amount of 112000, we want to return 112% as the result. The general formula for this calculation, where "x" is the percentage achieved is:

    x=actual/goal
    x=112000/100000
    x=1.12
    

Converting this to an Excel formula with cell references, the formula in E5 becomes:

    =D5/C5
    =112000/100000
    =1.12
    =112%
    

As the formula is copied down, the formula returns a decimal number for each city in the list. When these numbers are formatted with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
, they are displayed as percentages.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 25% is read as "Twenty-five percent" and is equivalent to 25/100 or 0.25. Accordingly, the values in column E are _decimal values_, with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

### Negative goal

If you have a negative goal, the formula above won't calculate correctly. In this case, you can [calculate the variance as explained here](https://exceljet.net/formulas/calculate-percent-variance)
, then add the variance to 100% to get the percent of goal:

    =(actual-goal)/ABS(goal)+100%
    

Related formulas
----------------

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

[![Excel formula: Calculate percent variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20percent%20variance.png "Excel formula: Calculate percent variance")](https://exceljet.net/formulas/calculate-percent-variance)

### [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)

In this example, the goal is to calculate the variance between a Forecast (column C) and Actual (column D) as a percentage. For example, with a Forecast value of 100,000 and an Actual value of 112,000, we want to return a variance of 12%. The concept of variance requires a baseline value and a "new...

[![Excel formula: Project complete percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/project%20complete%20percentage_0.png "Excel formula: Project complete percentage")](https://exceljet.net/formulas/project-complete-percentage)

### [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)

In this example if a task is marked "Done", then it is considered complete. The goal is to calculate the percent complete for the project by showing the ratio of complete tasks to total tasks, expressed as a percentage. The formula in F6 is: =COUNTA(C5:C11)/COUNTA(B5:B11) At the core, this formula...

[![Excel formula: Percent sold](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20sold_0.png "Excel formula: Percent sold")](https://exceljet.net/formulas/percent-sold)

### [Percent sold](https://exceljet.net/formulas/percent-sold)

In this example, the goal is to calculate the percentage sold for each item listed in the table, where original number (Total) is in column C and the Sold number is in column D. In other words, if we know we started with 144 apples, and sold 108 apples, we want to calculate that 75% of the apples...

[![Excel formula: Percent of students absent](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20students%20absent.png "Excel formula: Percent of students absent")](https://exceljet.net/formulas/percent-of-students-absent)

### [Percent of students absent](https://exceljet.net/formulas/percent-of-students-absent)

In this example, the goal is to answer the question "What percentage of students were absent from each class". In other words, given a class with 30 students total, 27 of which were present, we want to return 10% absent. The general formula for this calculation, where "x" is the percent absent is:...

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

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
    
*   [Calculate percent variance](https://exceljet.net/formulas/calculate-percent-variance)
    
*   [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)
    
*   [Percent sold](https://exceljet.net/formulas/percent-sold)
    
*   [Percent of students absent](https://exceljet.net/formulas/percent-of-students-absent)
    
*   [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)
    

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