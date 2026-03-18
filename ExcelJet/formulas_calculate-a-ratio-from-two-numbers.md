# Calculate a ratio from two numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-a-ratio-from-two-numbers

---

[Skip to main content](https://exceljet.net/formulas/calculate-a-ratio-from-two-numbers#main-content)

[](https://exceljet.net/formulas/calculate-a-ratio-from-two-numbers#)

*   [Previous](https://exceljet.net/formulas/build-hyperlink-with-vlookup)
    
*   [Next](https://exceljet.net/formulas/calculate-win-loss-tie-totals)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Calculate a ratio from two numbers
==================================

by Dave Bruns · Updated 20 Oct 2016

Related functions 
------------------

[GCD](https://exceljet.net/functions/gcd-function)

![Excel formula: Calculate a ratio from two numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_the_ratio_of_two_numbers.png "Excel formula: Calculate a ratio from two numbers")

Summary
-------

To generate the ratio of two numbers to each other (e.g. 4:3, 16:9, etc.), you can do using division, the GCD function, and concatenation. In the generic form of the formula (above) **num1** represents the first number (the antecedent) and **num2** represents the second number (the consequent).

In the example, the active cell contains this formula:

    =B4/GCD(B4,C4)&":"&C4/GCD(B4,C4)
    

_Note: the GCD function only works with integers._

Generic formula
---------------

    =num1/GCD(num1,num2)&":"&num2/GCD(num1,num2)

Explanation 
------------

This formula looks complicated, but, at the core, it is quite simple, and created in two parts like so:

    = (formula for number1) &":"& (formula for number2)
    

On the left, the GCD function is used to calculated the greatest common divisor (GCD) of the two numbers. Then the first number is divided by the GCD. On the right, the same operations are performed with the second number.

Next, the result of the right and left operations are joined together using concatenation, with the colon (":") as a separator. So, altogether, we have:

    =B4/(GCD(B4,C4)) &":"& C4/GCD(B4,C4)
    =1280/(GCD(1280,720)) &":"& 720/GCD(1280,720)
    =1280/80 &":"& 720/80
    =16 &":"& 9
    =16:9
    

Note that the final result of this formula is a text value.

Related functions
-----------------

[![Excel GCD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20gcd%20function.png "Excel GCD function")](https://exceljet.net/functions/gcd-function)

### [GCD Function](https://exceljet.net/functions/gcd-function)

The Excel GCD function returns the greatest common divisor of two or more integers. The greatest common divisor is the largest integer that goes into all supplied numbers without a remainder. For example, =GCD(60,36) returns 12.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [GCD Function](https://exceljet.net/functions/gcd-function)
    

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