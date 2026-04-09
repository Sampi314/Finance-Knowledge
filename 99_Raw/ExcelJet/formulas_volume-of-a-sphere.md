# Volume of a sphere - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/volume-of-a-sphere

---

[Skip to main content](https://exceljet.net/formulas/volume-of-a-sphere#main-content)

[](https://exceljet.net/formulas/volume-of-a-sphere#)

*   [Previous](https://exceljet.net/formulas/volume-of-a-rectangular-prism)
    
*   [Next](https://exceljet.net/formulas/count-errors-in-all-sheets)
    

[Geometry](https://exceljet.net/formulas#Geometry)

Volume of a sphere
==================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[PI](https://exceljet.net/functions/pi-function)

[POWER](https://exceljet.net/functions/power-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6433/download?token=zUGhFh2f)
 (13.79 KB)

![Excel formula: Volume of a sphere](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/volume%20of%20a%20sphere.png "Excel formula: Volume of a sphere")

Summary
-------

To calculate the volume of a sphere, you can use the [PI function](https://exceljet.net/functions/pi-function)
 together with the exponent [operator](https://exceljet.net/glossary/math-operators)
 (^). In the example shown, the formula in C5, copied down, is:

    =4/3*PI()*B5^3
    

which calculates the volume of a sphere with the radius given in column B. Units are indicated generically with "u", and the result is units cubed (u3).

Generic formula
---------------

    =4/3*PI()*A1^3

Explanation 
------------

In geometry, a sphere is defined as a set of points that are all the same distance (r) from a given point in a three-dimensional space. The formula for calculating the volume of a sphere is: 

Where r represents radius, and the Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the [PI function](https://exceljet.net/functions/pi-function)
, which returns the number 3.14159265358979, accurate to 15 digits:

    =PI() // returns 3.14159265358979
    

To cube a number in Excel, you can use the exponentiation [operator](https://exceljet.net/glossary/math-operators)
 (^):

    =A1^3
    

Or, you can use the [POWER function](https://exceljet.net/functions/power-function)
:

    =POWER(A1,3)
    

Rewriting the formula using Excel's [math operators](https://exceljet.net/glossary/math-operators)
 we get:

    =4/3*PI()*B5^3
    

Or, with the POWER function:

    =4/3*PI()*POWER(B5,3)
    

The result is the same for both formulas. Following Excel's [order of operations](https://exceljet.net/glossary/order-of-operations)
, exponentiation will occur before multiplication.

Related formulas
----------------

[![Excel formula: Volume of a cylinder](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cylinder.png "Excel formula: Volume of a cylinder")](https://exceljet.net/formulas/volume-of-a-cylinder)

### [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)

In geometry, the formula for calculating the volume of a cylinder is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3.14159265358979, accurate to 15 digits: =PI...

[![Excel formula: Volume of a cone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cone.png "Excel formula: Volume of a cone")](https://exceljet.net/formulas/volume-of-a-cone)

### [Volume of a cone](https://exceljet.net/formulas/volume-of-a-cone)

In geometry, the formula for calculating the volume of a cone is: The formula for calculating the volume of a cone is based on the formula for calculating the volume of a pyramid. Since the base of a cone is a circular, the formula for area of a circle is included. The Greek letter π ("pi")...

[![Excel formula: Area of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20circle.png "Excel formula: Area of a circle")](https://exceljet.net/formulas/area-of-a-circle)

### [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)

In geometry, the area enclosed by a circle with radius (r) is defined by the following formula: πr 2 The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Area of a triangle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20triangle.png "Excel formula: Area of a triangle")](https://exceljet.net/formulas/area-of-a-triangle)

### [Area of a triangle](https://exceljet.net/formulas/area-of-a-triangle)

In geometry, the area enclosed by a triangle is defined by this formula: where b represents the base of the triangle, and h represents the height, measured at right angles to the base. In Excel, the same formula can be represented like this: A=b\*h/2 So, for example, to calculate the area of a...

[![Excel formula: Circumference of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/circumference%20of%20a%20circle.png "Excel formula: Circumference of a circle")](https://exceljet.net/formulas/circumference-of-a-circle)

### [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)

In geometry, the circumference of a circle with radius (r) is defined by the following formula: =2πr The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Pythagorean theorem](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pythagorean%20theorem.png "Excel formula: Pythagorean theorem")](https://exceljet.net/formulas/pythagorean-theorem)

### [Pythagorean theorem](https://exceljet.net/formulas/pythagorean-theorem)

The Pythagorean theorem is a key principle in Euclidean geometry. It states that the square of the longest side of a right triangle (the hypotenuse) is equal to the sum of the squares of the other two sides. The theorem is written as an equation like this: a 2 + b 2 = c 2 When any two sides are...

Related functions
-----------------

[![Excel PI function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pi%20function.png "Excel PI function")](https://exceljet.net/functions/pi-function)

### [PI Function](https://exceljet.net/functions/pi-function)

The Excel PI function returns the value of the geometric constant π (pi). The value represents a half-rotation in the radian angle system. The constant appears in many formulas relating the circle, such as the area of a circle....

[![Excel POWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20power%20function.png "Excel POWER function")](https://exceljet.net/functions/power-function)

### [POWER Function](https://exceljet.net/functions/power-function)

The Excel POWER function returns a number raised to a given power. The POWER function is an alternative to the [exponent operator](https://exceljet.net/glossary/math-operators)
 (^).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)
    
*   [Volume of a cone](https://exceljet.net/formulas/volume-of-a-cone)
    
*   [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)
    
*   [Area of a triangle](https://exceljet.net/formulas/area-of-a-triangle)
    
*   [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)
    
*   [Pythagorean theorem](https://exceljet.net/formulas/pythagorean-theorem)
    

### Functions

*   [PI Function](https://exceljet.net/functions/pi-function)
    
*   [POWER Function](https://exceljet.net/functions/power-function)
    

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