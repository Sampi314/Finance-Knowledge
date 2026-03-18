# Volunteer hours requirement calculation - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/volunteer-hours-requirement-calculation

---

[Skip to main content](https://exceljet.net/formulas/volunteer-hours-requirement-calculation#main-content)

[](https://exceljet.net/formulas/volunteer-hours-requirement-calculation#)

*   [Previous](https://exceljet.net/formulas/value-is-within-tolerance)
    
*   Next

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Volunteer hours requirement calculation
=======================================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Volunteer hours requirement calculation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/volunteer%20hours%20requirement%20calculation.png "Excel formula: Volunteer hours requirement calculation")

Summary
-------

This example shows how to calculate a volunteer hour requirement. The requirement is to have 15 volunteer hours, with at least 5 in each category. The formula in F6 is:

    =AND(COUNTIF(C6:E6,">=5")=3,SUM(C6:E6)>=15)
    

Generic formula
---------------

    =AND(COUNTIF(rng,">=5")=3,SUM(rng)>=15)

Explanation 
------------

In this example, the goal create a formula that will return TRUE when a volunteer has successfully logged the required number of hours in each of the three categories. Two requirements must be satisfied:

1.  A volunteer should have at least 5 hours in each of the three categories.
2.  A volunteer needs to have at least 15 hours in total.

Both requirements are evaluated inside a single [AND function](https://exceljet.net/functions/and-function)
 in a formula like this:

    =AND(COUNTIF(C6:E6,">=5")=3,SUM(C6:E6)>=15)
    

The first requirement is at least 5 volunteer hours in each of the 3 categories: A, B, and C. This requirement is tested with a logical statement based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
:

    COUNTIF(C6:E6,">=5")=3
    

In the range C6:E6, we count numbers greater than or equal to 5. We need a result of 3 for this requirement to be satisfied, so we compare the result from COUNTIF to 3 directly. The result will be TRUE or FALSE.

The second requirement is to have at least 15 volunteer hours in total. This requirement is tested with a simple logical expression based on the [SUM function](https://exceljet.net/functions/sum-function)
:

    SUM(C6:E6)>=15)
    

Here, we use SUM to add up all ours in the range C6:C15 then we compare the result to the number 15 with the greater than or equal to operator (>=). As long as the sum is at least 15, this expression will return TRUE.

Finally the results from the two expressions above are evaluated by the AND function. If both the logical expressions return TRUE, the AND function will return TRUE. If either expression returns FALSE, AND will return FALSE.

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Videos

*   [How to use IF with AND and OR](https://exceljet.net/plc/how-to-use-if-with-and-and-or)
    

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