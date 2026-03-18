# Surface area of a cylinder - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/surface-area-of-a-cylinder

---

[Skip to main content](https://exceljet.net/formulas/surface-area-of-a-cylinder#main-content)

[](https://exceljet.net/formulas/surface-area-of-a-cylinder#)

*   [Previous](https://exceljet.net/formulas/surface-area-of-a-cone)
    
*   [Next](https://exceljet.net/formulas/surface-area-of-a-sphere)
    

[Geometry](https://exceljet.net/formulas#Geometry)

Surface area of a cylinder
==========================

by Dave Bruns · Updated 9 Jul 2022

Related functions 
------------------

[PI](https://exceljet.net/functions/pi-function)

[POWER](https://exceljet.net/functions/power-function)

![Excel formula: Surface area of a cylinder](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/surface%20area%20of%20a%20cylinder.png "Excel formula: Surface area of a cylinder")

Summary
-------

To calculate the surface area of a cylinder, you can use the standard geometric formula based on the [PI function](https://exceljet.net/functions/pi-function)
 together with the exponent [operator](https://exceljet.net/glossary/math-operators)
 (^). In the example shown, the formula in D5, copied down, is:

    =2*PI()*B5*C5+2*PI()*B5^2
    

which returns the surface area of a cylinder with the radius given in column B and the height given in column C. Units are indicated generically with "u", and the resulting volume is units squared (u2).

Generic formula
---------------

    =2*PI()*r*h+2*PI()*r^2

Explanation 
------------

In geometry, the standard formula for calculating the surface area of a cylinder is: 

In essence, this formula first calculates the area of the side of the cylinder, based on the [circumference of the circle](https://exceljet.net/formulas/circumference-of-a-circle)
 times the height of the cylinder, then adds two times the [area of circle](https://exceljet.net/formulas/area-of-a-circle)
 to account for the ends of the cylinder.

The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the [PI function](https://exceljet.net/functions/pi-function)
, which returns the number 3.14159265358979, accurate to 15 digits:

    =PI() // returns 3.14159265358979
    

To square a number in Excel, you can use the exponentiation [operator](https://exceljet.net/glossary/math-operators)
 (^):

    =A1^2
    

Or, you can use the [POWER function](https://exceljet.net/functions/power-function)
:

    =POWER(A1,2)
    

Rewriting the formula for volume of a cylinder with Excel's [math operators](https://exceljet.net/glossary/math-operators)
, we get:

    =2*PI()*B5*C5+2*PI()*B5^2
    

Or, with the POWER function:

    =2*PI()*B5*C5+2*PI()*POWER(B5,2)
    

The result is the same for both formulas. Following Excel's [order of operations](https://exceljet.net/glossary/order-of-operations)
, exponentiation will occur before multiplication, which will occur before addition.

Related formulas
----------------

[![Excel formula: Area of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20circle.png "Excel formula: Area of a circle")](https://exceljet.net/formulas/area-of-a-circle)

### [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)

In geometry, the area enclosed by a circle with radius (r) is defined by the following formula: πr 2 The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Volume of a cylinder](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cylinder.png "Excel formula: Volume of a cylinder")](https://exceljet.net/formulas/volume-of-a-cylinder)

### [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)

In geometry, the formula for calculating the volume of a cylinder is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3.14159265358979, accurate to 15 digits: =PI...

[![Excel formula: Circumference of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/circumference%20of%20a%20circle.png "Excel formula: Circumference of a circle")](https://exceljet.net/formulas/circumference-of-a-circle)

### [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)

In geometry, the circumference of a circle with radius (r) is defined by the following formula: =2πr The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Volume of a sphere](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20sphere.png "Excel formula: Volume of a sphere")](https://exceljet.net/formulas/volume-of-a-sphere)

### [Volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)

In geometry, a sphere is defined as a set of points that are all the same distance (r) from a given point in a three-dimensional space. The formula for calculating the volume of a sphere is: Where r represents radius, and the Greek letter π ("pi") represents the ratio of the circumference of a...

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

*   [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)
    
*   [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)
    
*   [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)
    
*   [Volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)
    

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