# Project complete percentage - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/project-complete-percentage

---

[Skip to main content](https://exceljet.net/formulas/project-complete-percentage#main-content)

[](https://exceljet.net/formulas/project-complete-percentage#)

*   [Previous](https://exceljet.net/formulas/percent-sold)
    
*   [Next](https://exceljet.net/formulas/random-date-between-two-dates)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Project complete percentage
===========================

by Dave Bruns · Updated 16 May 2021

Related functions 
------------------

[COUNTA](https://exceljet.net/functions/counta-function)

![Excel formula: Project complete percentage](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/project%20complete%20percentage_0.png "Excel formula: Project complete percentage")

Summary
-------

To calculate the percentage complete for a project with a list of tasks, you can use a simple formula based on the [COUNTA function](https://exceljet.net/functions/counta-function)
. In the example shown, the formula in F6 is:

    =COUNTA(C5:C11)/COUNTA(B5:B11)
    

Generic formula
---------------

    =COUNTA(range1)/COUNTA(range2)

Explanation 
------------

In this example if a task is marked "Done", then it is considered complete. The goal is to calculate the percent complete for the project by showing the ratio of complete tasks to total tasks, expressed as a percentage. The formula in F6 is:

    =COUNTA(C5:C11)/COUNTA(B5:B11)
    

At the core, this formula simply divides tasks complete by the total task count:

    =complete/total
    

which is then [formatted as a percentage](https://exceljet.net/glossary/number-format)
. To count _completed_ tasks, we count non-blank cells in the range C5:C11 with the [COUNTA function](https://exceljet.net/functions/counta-function)
:

    =COUNTA(C5:C11) // returns 4
    

Unlike the [COUNT function](https://exceljet.net/functions/count-function)
, which counts _only numeric values_, [COUNTA](https://exceljet.net/functions/counta-function)
 will count cells that include numbers or text.

To count _total_ tasks, we count non-blank cells in the range C5:C11, again with COUNTA:

    COUNTA(B5:B11) // returns 7
    

After COUNTA runs, we can simply the formula to:

    =4/7 // 0.571428571428571
    

Four divided by 7 results in the decimal number 0.571428571428571 which is displayed as 57% once the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 is applied.

Related formulas
----------------

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

[![Excel formula: Percent of goal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20goal.png "Excel formula: Percent of goal")](https://exceljet.net/formulas/percent-of-goal)

### [Percent of goal](https://exceljet.net/formulas/percent-of-goal)

In this example, the objective is to calculate a percentage for each goal shown in column C of the table using the actual values in column D. In other words, given a goal of 100000, and an actual amount of 112000, we want to return 112% as the result. The general formula for this calculation, where...

[![Excel formula: Get percent change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20change2.png "Excel formula: Get percent change")](https://exceljet.net/formulas/get-percent-change)

### [Get percent change](https://exceljet.net/formulas/get-percent-change)

Following order of operations, Excel first calculates the difference between the values (the actual change in sales) then divides that result by the original, or "old" value to get the decimal value -0.3435: =(D6-C6)/C6 =(49500-75400)/75400 =-25900/75400 =0.0688 Note: you must format the result...

Related functions
-----------------

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

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
    
*   [Get percent change](https://exceljet.net/formulas/get-percent-change)
    

### Functions

*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

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