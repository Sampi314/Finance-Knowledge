# Percent of students absent - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/percent-of-students-absent

---

[Skip to main content](https://exceljet.net/formulas/percent-of-students-absent#main-content)

[](https://exceljet.net/formulas/percent-of-students-absent#)

*   [Previous](https://exceljet.net/formulas/percent-of-goal)
    
*   [Next](https://exceljet.net/formulas/percent-sold)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Percent of students absent
==========================

by Dave Bruns · Updated 16 May 2024

![Excel formula: Percent of students absent](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/percent%20of%20students%20absent.png "Excel formula: Percent of students absent")

Summary
-------

To calculate the percentage of students absent in a given class, you can use a formula that calculates the number of students absent and then divides this number by the total number of students.  In the example shown, the formula in E5, copied down, is:

    =(C5-D5)/C5
    

The result is a decimal value formatted with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

Generic formula
---------------

    =(total-attended)/total

Explanation 
------------

In this example, the goal is to answer the question "What percentage of students were absent from each class". In other words, given a class with 30 students total, 27 of which were present, we want to return 10% absent. The general formula for this calculation, where "x" is the percent absent is:

    x=absent/total
    

However, since we don't have a column for the number of students absent in the table, we need to calculate this number as part of the formula:

    x=(total-attended)/total
    x=(30-27)/30
    x=3/30
    x=0.10
    

After we convert this to an Excel formula with cell references, the formula in E5 becomes:

    =(C5-D5)/C5
    =(30-27)/30
    =3/30
    =0.10
    

As the formula is copied down, the formula returns the calculated "percent absent" for each class listed in the table. These results are decimal numbers formatted with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 55% is read as "Fifty-five percent" and is equivalent to 55/100 or 0.55. To display values with a percent sign (%), apply [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

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

[![Excel formula: Percent sold](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20sold_0.png "Excel formula: Percent sold")](https://exceljet.net/formulas/percent-sold)

### [Percent sold](https://exceljet.net/formulas/percent-sold)

In this example, the goal is to calculate the percentage sold for each item listed in the table, where original number (Total) is in column C and the Sold number is in column D. In other words, if we know we started with 144 apples, and sold 108 apples, we want to calculate that 75% of the apples...

[![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")](https://exceljet.net/formulas/get-percent-of-year-complete)

### [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year. \*By default, the YEARFRAC function uses a 30/360-day...

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
    
*   [Percent sold](https://exceljet.net/formulas/percent-sold)
    
*   [Get percent of year complete](https://exceljet.net/formulas/get-percent-of-year-complete)
    

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