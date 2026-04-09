# Surface area of a cone - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/surface-area-of-a-cone

---

[Skip to main content](https://exceljet.net/formulas/surface-area-of-a-cone#main-content)

[](https://exceljet.net/formulas/surface-area-of-a-cone#)

*   [Previous](https://exceljet.net/formulas/pythagorean-theorem)
    
*   [Next](https://exceljet.net/formulas/surface-area-of-a-cylinder)
    

[Geometry](https://exceljet.net/formulas#Geometry)

Surface area of a cone
======================

by Dave Bruns · Updated 17 Jan 2021

Related functions 
------------------

[PI](https://exceljet.net/functions/pi-function)

[POWER](https://exceljet.net/functions/power-function)

![Excel formula: Surface area of a cone](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/surface%20area%20of%20a%20cone.png "Excel formula: Surface area of a cone")

Summary
-------

To calculate the surface area of a cone, you can use the [PI function](https://exceljet.net/functions/pi-function)
 together with the exponent [operator](https://exceljet.net/glossary/math-operators)
 (^) and the [SQRT function](https://exceljet.net/functions/sqrt-function)
. In the example shown, the formula in D5, copied down, is:

    =1/3*PI()*B5^2*C5
    

The formula returns the surface area of a cone with radius given in column B and height given in column C. Units are indicated generically with "u", and the resulting area is units squared (u2).

Generic formula
---------------

    =PI()*r*(r+SQRT(h^2+r^2))

Explanation 
------------

In geometry, the formula for calculating the surface area of a right cone is: 

The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the [PI function](https://exceljet.net/functions/pi-function)
, which returns the number 3.14159265358979, accurate to 15 digits:

    =PI() // returns 3.14159265358979
    

To square a number in Excel, you can use the exponentiation [operator](https://exceljet.net/glossary/math-operators)
 (^):

    =A1^2
    

To get the square root of a number, you can use the [SQRT function](https://exceljet.net/functions/sqrt-function)
:

    =SQRT(A1)
    

Rewriting the formula for surface area of a cone with Excel's [math operators](https://exceljet.net/glossary/math-operators)
, we get:

    =PI()*B5*(B5+SQRT(C5^2+B5^2))
    

Following Excel's [order of operations](https://exceljet.net/glossary/order-of-operations)
, exponentiation will occur before multiplication.

Related formulas
----------------

[![Excel formula: Area of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20circle.png "Excel formula: Area of a circle")](https://exceljet.net/formulas/area-of-a-circle)

### [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)

In geometry, the area enclosed by a circle with radius (r) is defined by the following formula: πr 2 The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Area of a triangle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20triangle.png "Excel formula: Area of a triangle")](https://exceljet.net/formulas/area-of-a-triangle)

### [Area of a triangle](https://exceljet.net/formulas/area-of-a-triangle)

In geometry, the area enclosed by a triangle is defined by this formula: where b represents the base of the triangle, and h represents the height, measured at right angles to the base. In Excel, the same formula can be represented like this: A=b\*h/2 So, for example, to calculate the area of a...

[![Excel formula: Circumference of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/circumference%20of%20a%20circle.png "Excel formula: Circumference of a circle")](https://exceljet.net/formulas/circumference-of-a-circle)

### [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)

In geometry, the circumference of a circle with radius (r) is defined by the following formula: =2πr The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Volume of a sphere](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20sphere.png "Excel formula: Volume of a sphere")](https://exceljet.net/formulas/volume-of-a-sphere)

### [Volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)

In geometry, a sphere is defined as a set of points that are all the same distance (r) from a given point in a three-dimensional space. The formula for calculating the volume of a sphere is: Where r represents radius, and the Greek letter π ("pi") represents the ratio of the circumference of a...

[![Excel formula: Volume of a cylinder](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cylinder.png "Excel formula: Volume of a cylinder")](https://exceljet.net/formulas/volume-of-a-cylinder)

### [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)

In geometry, the formula for calculating the volume of a cylinder is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3.14159265358979, accurate to 15 digits: =PI...

[![Excel formula: Volume of a cone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cone.png "Excel formula: Volume of a cone")](https://exceljet.net/formulas/volume-of-a-cone)

### [Volume of a cone](https://exceljet.net/formulas/volume-of-a-cone)

In geometry, the formula for calculating the volume of a cone is: The formula for calculating the volume of a cone is based on the formula for calculating the volume of a pyramid. Since the base of a cone is a circular, the formula for area of a circle is included. The Greek letter π ("pi")...

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
    
*   [Area of a triangle](https://exceljet.net/formulas/area-of-a-triangle)
    
*   [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)
    
*   [Volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)
    
*   [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)
    
*   [Volume of a cone](https://exceljet.net/formulas/volume-of-a-cone)
    

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