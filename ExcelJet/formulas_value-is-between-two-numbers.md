# Value is between two numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/value-is-between-two-numbers

---

[Skip to main content](https://exceljet.net/formulas/value-is-between-two-numbers#main-content)

[](https://exceljet.net/formulas/value-is-between-two-numbers#)

*   [Previous](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Next](https://exceljet.net/formulas/value-is-within-tolerance)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Value is between two numbers
============================

by Dave Bruns · Updated 9 Aug 2023

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[MAX](https://exceljet.net/functions/max-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Value is between two numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/value%20is%20between%20two%20numbers.png "Excel formula: Value is between two numbers")

Summary
-------

To test if a numeric value falls between two numbers, you can use the AND function with two logical tests. In the example shown, the formula in E5 is:

    =AND(D5>MIN(B5,C5),D5<MAX(B5,C5))
    

Generic formula
---------------

    =AND(val>MIN(num1,num2),val<MAX(num1,num2))

Explanation 
------------

At the core, this formula runs two tests on a value like this:

    =D5>MIN(B5,C5) // is D5 greater than smaller?
    =D5<MAX(B5,C5)) // is D5 less than larger?
    

In the first expression, the value is compared to the smaller of the two numbers, determined by the MIN function.

In the second expression, the value is compared to the larger of the two numbers, determined by the MAX function.

The AND function will return TRUE only when the value is greater than the smaller number and less than the larger number.

### Include boundaries

To include the boundary numbers (num1 and num2), adjust the [logical operators](https://exceljet.net/glossary/logical-operators)
 like this:

    =AND(D5>=MIN(B5,C5),D5<=MAX(B5,C5))
    

Now the AND function will return TRUE only when the value is greater than or equal to the smaller number and less than or equal to the larger number.

### Simple version

The formula in the example is more complex because there is no assumption that num1 is less than num2 (or vice versa). If it's safe to assume that _num1_ is less than _num2_, the formula can be simplified like this:

    =AND(value>num1,val<num2)
    

Related formulas
----------------

[![Excel formula: Value is within tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value%20is%20within%20tolerance.png "Excel formula: Value is within tolerance")](https://exceljet.net/formulas/value-is-within-tolerance)

### [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)

In this example the goal is to check if values in column B are within a tolerance of .005. If a value is within tolerance, the formula should return "OK". If the value is out of tolerance, the formula should return "Fail". The expected value is listed in column C, and the allowed tolerance is...

[![Excel formula: Count values out of tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20values%20out%20of%20tolerance.png "Excel formula: Count values out of tolerance")](https://exceljet.net/formulas/count-values-out-of-tolerance)

### [Count values out of tolerance](https://exceljet.net/formulas/count-values-out-of-tolerance)

This formula counts how many values are not in range of a fixed tolerance. The variation of each value is calculated with this: ABS(data-target) Because the named range "data" contains 10 values, subtracting the target value in F4 will created an array with 10 results: {0.001;-0.002;-0.01;0.003;0...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)
    
*   [Count values out of tolerance](https://exceljet.net/formulas/count-values-out-of-tolerance)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

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