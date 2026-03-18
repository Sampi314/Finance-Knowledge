# Difference is within specific percentage - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/difference-is-within-specific-percentage

---

[Skip to main content](https://exceljet.net/formulas/difference-is-within-specific-percentage#main-content)

[](https://exceljet.net/formulas/difference-is-within-specific-percentage#)

*   [Previous](https://exceljet.net/formulas/decrease-by-percentage)
    
*   [Next](https://exceljet.net/formulas/get-amount-with-percentage)
    

[Percentage](https://exceljet.net/formulas#Percentage)

Difference is within specific percentage
========================================

by Dave Bruns · Updated 10 Jun 2022

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[ABS](https://exceljet.net/functions/abs-function)

![Excel formula: Difference is within specific percentage](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/difference%20is%20within%20specific%20percentage.png "Excel formula: Difference is within specific percentage")

Summary
-------

To test the difference between two values, and return a message when the difference is less or greater than a target percentage you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
 and the [ABS function](https://exceljet.net/functions/abs-function)
. In the example shown, the formula in E5, copied down, is:

    =IF(ABS(D5)<=target,"Yes","No")
    

where **target** is the [named range](https://exceljet.net/glossary/named-range)
 G5. In cell E5, the result is "Yes", because the difference in D5 is less than or equal to 5%.

Generic formula
---------------

    =IF(ABS(percentage)<=target,"Yes","No")

Explanation 
------------

In this example, the goal to calculate the difference as a percentage between two values then check the result to see if its within a given target percentage. The values come from the Expected and Actual columns in the worksheet. The challenge is that the difference might be negative or positive, and we need to cater to both.

### Difference as percentage

To calculate the difference as a percentage, we can use a general formula like this:

    =(actual-expected)/expected
    

After converting this to cell references, we have:

    =(C5-B5)/B5
    

As the formula is copied down, it returns a percentage difference in each row. Note that some values are negative.

_Note: the results are decimal values like 0.05 and they must be formatted with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 to display as 5%, 7%, etc._

### Compare to target

To compare the percentages to the target percentage, we use the [IF function](https://exceljet.net/functions/if-function)
 like this in cell E5:

    =IF(ABS(D5)<=target,"Yes","No")
    

where **target** is the [named range](https://exceljet.net/glossary/named-range)
 G5. This formula uses the [ABS function](https://exceljet.net/functions/abs-function)
 to convert the percentages in column D to positive numbers. Then it uses the IF function to compare the result from ABS to the target (set to 5% in the example shown). If the logical test returns TRUE, the difference is within 5% and IF returns "Yes". Otherwise, IF returns "No". Notice both results are [text values](https://exceljet.net/glossary/text-value)
 wrapped in double quotes ("").

As the formula is copied down, we get a new result in each row. If the value in G5 is changed to a new percentage, all results recalculate.

### All-in-one-formula

In the example shown, column D is used to calculate the difference as a percentage, in order to make the example easier to understand. However, you can combine both formulas above into a single formula like this if needed:

    =IF(ABS((C5-B5)/B5)<=target,"Yes","No")
    

The result is the same, but this version does not need to use column D as a [helper column](https://exceljet.net/glossary/helper-column)
.

Related formulas
----------------

[![Excel formula: Get percent change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20change2.png "Excel formula: Get percent change")](https://exceljet.net/formulas/get-percent-change)

### [Get percent change](https://exceljet.net/formulas/get-percent-change)

Following order of operations, Excel first calculates the difference between the values (the actual change in sales) then divides that result by the original, or "old" value to get the decimal value -0.3435: =(D6-C6)/C6 =(49500-75400)/75400 =-25900/75400 =0.0688 Note: you must format the result...

[![Excel formula: Increase by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Increase%20by%20percent_0.png "Excel formula: Increase by percentage")](https://exceljet.net/formulas/increase-by-percentage)

### [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)

In this example, the goal is to increase the prices shown in column C by the percentages shown in column D. For example, given the original price of $70.00, and an increase of 10%, the result should be $77.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1+...

[![Excel formula: Forecast vs actual variance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/forecast%20vs%20actual%20variance.png "Excel formula: Forecast vs actual variance")](https://exceljet.net/formulas/forecast-vs-actual-variance)

### [Forecast vs actual variance](https://exceljet.net/formulas/forecast-vs-actual-variance)

This is a pretty standard use of the SUMIFS function. In this case, we need to sum amounts based on two criteria: type (forecast or actual) and group. To sum by type, the range/criteria pair is: type,G$4 where type is the named range D5:D14, and G4 is a mixed reference with the row locked in order...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get percent change](https://exceljet.net/formulas/get-percent-change)
    
*   [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)
    
*   [Forecast vs actual variance](https://exceljet.net/formulas/forecast-vs-actual-variance)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [ABS Function](https://exceljet.net/functions/abs-function)
    

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