# Count values out of tolerance - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-values-out-of-tolerance

---

[Skip to main content](https://exceljet.net/formulas/count-values-out-of-tolerance#main-content)

[](https://exceljet.net/formulas/count-values-out-of-tolerance#)

*   [Previous](https://exceljet.net/formulas/count-consecutive-monthly-orders)
    
*   [Next](https://exceljet.net/formulas/count-with-repeating-values)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Count values out of tolerance
=============================

by Dave Bruns · Updated 30 Aug 2018

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ABS](https://exceljet.net/functions/abs-function)

![Excel formula: Count values out of tolerance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20values%20out%20of%20tolerance.png "Excel formula: Count values out of tolerance")

Summary
-------

To count values that are out of tolerance in a set of data, you can use a formula based on the SUMPRODUCT and ABS functions. In the example shown, the formula in F6 is:

    =SUMPRODUCT(--(ABS(data-target)>tolerance))
    

where "data" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B14, "target" is the named range F4, and "tolerance" is the named range F5.

Generic formula
---------------

    =SUMPRODUCT(--(ABS(data-target)>tolerance))

Explanation 
------------

This formula counts how many values are not in range of a fixed tolerance. The variation of each value is calculated with this:

    ABS(data-target)
    

Because the [named range](https://exceljet.net/glossary/named-range)
 "data" contains 10 values, subtracting the target value in F4 will created an array with 10 results:

    {0.001;-0.002;-0.01;0.003;0.008;0;-0.003;-0.01;0.002;-0.006}
    

The ABS function changes any negative values to positive:

    {0.001;0.002;0.01;0.003;0.008;0;0.003;0.01;0.002;0.006}
    

This array is compared to the fixed tolerance in F5:

    ABS(data-target)>tolerance
    

The result is an array or TRUE FALSE values, and the double negative changes these to ones and zeros. Inside SUMPRODUCT, the final array looks like this:

    {0;0;1;0;1;0;0;1;0;1}
    

where zeros represent values within tolerance, and 1s represent values out of tolerance. SUMPRODUCT then sums the items in the array, and returns a final result, 4.

### All values within tolerance

To return "Yes" if all values in a data range are within a given tolerance, and "No" if not, you can adapt the formula like this:

    =IF(SUMPRODUCT(--(ABS(data-target)>tolerance)),"Yes","No")
    

If SUMPRODUCT returns any number greater than zero, IF will evaluate the logical test as TRUE. A zero result will be evaluated as FALSE.

### Highlight values out of tolerance

You can highlight values out of tolerance with a conditional formatting rule based on a formula like this:

    =ABS(B5-target)>tolerance
    

![Highlight values out of tolerance](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20values%20out%20of%20tolerance2.png?itok=bq3DRVxN "Highlight values out of tolerance")

[This page](https://exceljet.net/conditional-formatting-formulas)
 lists more examples of conditional formatting with formulas.

Related formulas
----------------

[![Excel formula: Value is between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/value%20is%20between%20two%20numbers.png "Excel formula: Value is between two numbers")](https://exceljet.net/formulas/value-is-between-two-numbers)

### [Value is between two numbers](https://exceljet.net/formulas/value-is-between-two-numbers)

At the core, this formula runs two tests on a value like this: =D5>MIN(B5,C5) // is D5 greater than smaller? =D5<MAX(B5,C5)) // is D5 less than larger? In the first expression, the value is compared to the smaller of the two numbers, determined by the MIN function. In the second expression,...

[![Excel formula: Value is within tolerance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value%20is%20within%20tolerance.png "Excel formula: Value is within tolerance")](https://exceljet.net/formulas/value-is-within-tolerance)

### [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)

In this example the goal is to check if values in column B are within a tolerance of .005. If a value is within tolerance, the formula should return "OK". If the value is out of tolerance, the formula should return "Fail". The expected value is listed in column C, and the allowed tolerance is...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

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
    
*   [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
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