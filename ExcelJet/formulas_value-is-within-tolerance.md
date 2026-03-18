# Value is within tolerance - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/value-is-within-tolerance

---

[Skip to main content](https://exceljet.net/formulas/value-is-within-tolerance#main-content)

[](https://exceljet.net/formulas/value-is-within-tolerance#)

*   [Previous](https://exceljet.net/formulas/value-is-between-two-numbers)
    
*   [Next](https://exceljet.net/formulas/volunteer-hours-requirement-calculation)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Value is within tolerance
=========================

by Dave Bruns · Updated 28 Jan 2022

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[ABS](https://exceljet.net/functions/abs-function)

![Excel formula: Value is within tolerance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Value%20is%20within%20tolerance.png "Excel formula: Value is within tolerance")

Summary
-------

To test if a value is within expected tolerance or not, you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
 and the [ABS function](https://exceljet.net/functions/abs-function)
. In the example shown, the formula in E5, copied down, is:

    =IF(ABS(B5-C5)<=D5,"OK","Fail")
    

When the value in column B is within +/- .005 of 0.250 (from column C), the formula returns "OK". If not, the formula returns "Fail".

Generic formula
---------------

    =IF(ABS(actual-expected)<=tolerance,"OK","Fail")

Explanation 
------------

In this example the goal is to check if values in column B are within a tolerance of .005. If a value is within tolerance, the formula should return "OK". If the value is out of tolerance, the formula should return "Fail". The expected value is listed in column C, and the allowed tolerance is listed in column D. The solution is based on the IF function together with the ABS function.

### Core logic

To check if a value is within a given tolerance, we can use a simple [logical test](https://exceljet.net/glossary/logical-test)
 like this:

    =ABS(actual-expected)<=tolerance // logical test
    

Inside the ABS function, the actual value is subtracted from the expected value. The result may be positive or negative, depending on the actual value, so the [ABS function](https://exceljet.net/functions/abs-function)
 is used to convert the result to a positive number: negative values become positive and positive values are unchanged. The result from ABS is compared to the allowed tolerance with the [logical operator](https://exceljet.net/glossary/logical-operators)
 less than or equal (<=).  The expression returns TRUE when a value is less than or equal to the allowed tolerance, and FALSE if not.

### IF function

To complete the solution, we need to place the generic logical expression  above into the IF function and providing values for a TRUE and FALSE result. The first step is to revise the generic expression above to use worksheet references:

    ABS(B5-C5)<=D5 // logical test
    

Then, we drop the expression into the IF function as the _logical\_test_ [argument](https://exceljet.net/glossary/function-argument)
:

    =IF(ABS(B5-C5)<=D5,"OK","Fail") // final formula
    

When the logical test returns TRUE, IF returns "OK". When the logical test returns FALSE, IF returns "Fail". These messages can be customized as needed.

### List all values within tolerance

The basic concept explained above can be extended to [list values within tolerance or out of tolerance](https://exceljet.net/formulas/filter-values-within-tolerance)
 with the [FILTER function](https://exceljet.net/functions/filter-function)
.

Related formulas
----------------

[![Excel formula: Value is between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/value%20is%20between%20two%20numbers.png "Excel formula: Value is between two numbers")](https://exceljet.net/formulas/value-is-between-two-numbers)

### [Value is between two numbers](https://exceljet.net/formulas/value-is-between-two-numbers)

At the core, this formula runs two tests on a value like this: =D5>MIN(B5,C5) // is D5 greater than smaller? =D5<MAX(B5,C5)) // is D5 less than larger? In the first expression, the value is compared to the smaller of the two numbers, determined by the MIN function. In the second expression,...

[![Excel formula: Count values out of tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20values%20out%20of%20tolerance.png "Excel formula: Count values out of tolerance")](https://exceljet.net/formulas/count-values-out-of-tolerance)

### [Count values out of tolerance](https://exceljet.net/formulas/count-values-out-of-tolerance)

This formula counts how many values are not in range of a fixed tolerance. The variation of each value is calculated with this: ABS(data-target) Because the named range "data" contains 10 values, subtracting the target value in F4 will created an array with 10 results: {0.001;-0.002;-0.01;0.003;0...

[![Excel formula: Filter values within tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20values%20within%20tolerance.png "Excel formula: Filter values within tolerance")](https://exceljet.net/formulas/filter-values-within-tolerance)

### [Filter values within tolerance](https://exceljet.net/formulas/filter-values-within-tolerance)

In this example, the goal is to list values in a given group that are within a given tolerance. The group is set in cell G4, and the target value is entered in cell G5. The allowed tolerance is entered in cell G6. The data comes from an Excel Table called data in the range B5:D16. The solution is...

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

*   [Value is between two numbers](https://exceljet.net/formulas/value-is-between-two-numbers)
    
*   [Count values out of tolerance](https://exceljet.net/formulas/count-values-out-of-tolerance)
    
*   [Filter values within tolerance](https://exceljet.net/formulas/filter-values-within-tolerance)
    

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