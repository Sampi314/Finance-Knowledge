# Distance formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/distance-formula

---

[Skip to main content](https://exceljet.net/formulas/distance-formula#main-content)

[](https://exceljet.net/formulas/distance-formula#)

*   [Previous](https://exceljet.net/formulas/circumference-of-a-circle)
    
*   [Next](https://exceljet.net/formulas/pythagorean-theorem)
    

[Geometry](https://exceljet.net/formulas#Geometry)

Distance formula
================

by Dave Bruns · Updated 23 May 2021

Related functions 
------------------

[SQRT](https://exceljet.net/functions/sqrt-function)

![Excel formula: Distance formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/distance%20formula.png "Excel formula: Distance formula")

Summary
-------

To compute the length of a 2D line given the coordinates of two points on the line, you can use the distance formula, adapted for Excel's formula syntax. In the example shown, the formula in G5, copied down, is:

    =SQRT((D5-B5)^2+(E5-C5)^2)
    

where the coordinates of the two points are given in columns B through E.

Generic formula
---------------

    =SQRT((x2-x1)^2+(y2-y1)^2)

Explanation 
------------

The length of a line can be calculated with the distance formula, which looks like this:

Distance is the square root of the change in x squared plus the change in y squared, where two points are given in the form (x1, y1) and (x2, y2). The distance formula is an example of the [Pythagorean Theorem](https://exceljet.net/formulas/pythagorean-theorem)
 applied, where the change in x and the change in y correspond to the two sides of a right triangle, and the hypotenuse is the distance being computed.

In Excel, the distance formula can be written with the exponent [operator](https://exceljet.net/glossary/math-operators)
 (^) and the [SQRT function](https://exceljet.net/functions/sqrt-function)
 like this:

    =SQRT((D5-B5)^2+(E5-C5)^2)
    

Following Excel's [order of operations](https://exceljet.net/glossary/order-of-operations)
, the change in x and the change in y is calculated, then squared, and the two results are added together and delivered to the SQRT function, which returns the square root of the sum as a final result:

    =SQRT((D5-B5)^2+(E5-C5)^2)
    =SQRT((6)^2+(8)^2)
    =SQRT(36+64)
    =SQRT(100)
    =10
    

The [POWER function](https://exceljet.net/functions/power-function)
 can also be used instead of the exponent operator (^) like this:

    =SQRT(POWER(D5-B5,2)+POWER(E5-C5,2))
    

with the same result.

Related formulas
----------------

[![Excel formula: Pythagorean theorem](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pythagorean%20theorem.png "Excel formula: Pythagorean theorem")](https://exceljet.net/formulas/pythagorean-theorem)

### [Pythagorean theorem](https://exceljet.net/formulas/pythagorean-theorem)

The Pythagorean theorem is a key principle in Euclidean geometry. It states that the square of the longest side of a right triangle (the hypotenuse) is equal to the sum of the squares of the other two sides. The theorem is written as an equation like this: a 2 + b 2 = c 2 When any two sides are...

[![Excel formula: Area of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20circle.png "Excel formula: Area of a circle")](https://exceljet.net/formulas/area-of-a-circle)

### [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)

In geometry, the area enclosed by a circle with radius (r) is defined by the following formula: πr 2 The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Area of a triangle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20triangle.png "Excel formula: Area of a triangle")](https://exceljet.net/formulas/area-of-a-triangle)

### [Area of a triangle](https://exceljet.net/formulas/area-of-a-triangle)

In geometry, the area enclosed by a triangle is defined by this formula: where b represents the base of the triangle, and h represents the height, measured at right angles to the base. In Excel, the same formula can be represented like this: A=b\*h/2 So, for example, to calculate the area of a...

[![Excel formula: Circumference of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/circumference%20of%20a%20circle.png "Excel formula: Circumference of a circle")](https://exceljet.net/formulas/circumference-of-a-circle)

### [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)

In geometry, the circumference of a circle with radius (r) is defined by the following formula: =2πr The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

Related functions
-----------------

[![Excel SQRT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sqrt%20function.png "Excel SQRT function")](https://exceljet.net/functions/sqrt-function)

### [SQRT Function](https://exceljet.net/functions/sqrt-function)

The Excel SQRT function returns the square root of a positive number. SQRT returns an error if _number_ is negative.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Pythagorean theorem](https://exceljet.net/formulas/pythagorean-theorem)
    
*   [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)
    
*   [Area of a triangle](https://exceljet.net/formulas/area-of-a-triangle)
    
*   [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)
    

### Functions

*   [SQRT Function](https://exceljet.net/functions/sqrt-function)
    

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