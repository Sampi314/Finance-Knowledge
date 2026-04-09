# Excel PI function | Exceljet

**Source:** https://exceljet.net/functions/pi-function

---

[Skip to main content](https://exceljet.net/functions/pi-function#main-content)

[](https://exceljet.net/functions/pi-function#)

*   [Previous](https://exceljet.net/functions/odd-function)
    
*   [Next](https://exceljet.net/functions/power-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

PI Function
===========

by Dave Bruns · Updated 6 Nov 2022

Related functions 
------------------

[RADIANS](https://exceljet.net/functions/radians-function)

[DEGREES](https://exceljet.net/functions/degrees-function)

![Excel PI function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20pi%20function.png "Excel PI function")

Summary
-------

The Excel PI function returns the value of the geometric constant π (pi). The value represents a half-rotation in the radian angle system. The constant appears in many formulas relating the circle, such as the area of a circle.

Purpose 
--------

Get the value of π

Return value 
-------------

3.14159265358979

Syntax
------

    =PI()

Using the PI function 
----------------------

The PI function returns the value of π (pi) accurate to 15 digits. The value of π represents a half-turn in [radians](https://exceljet.net/glossary/radians)
 and appears in many formulas relating to the circle. The PI function takes no [arguments](https://exceljet.net/glossary/function-argument)
:

    =PI() // returns 3.14159265358979
    

### Circumference of a circle

The constant π appears in many math formulas relating to the circle. The formula for the [circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)
 is 2πr. Given a radius of 3, the same formula in Excel is:

    =2*PI()*3 // circumference of circle, r=3
    

### Area of a circle

The [area enclosed by a circle](https://exceljet.net/formulas/area-of-a-circle)
 with radius (r) is defined by the following formula: πr2. With radius in cell A1, the same formula in Excel with the PI() function is:

    =PI()*A1^2
    

### Radians to degrees

To convert an angle measured in radians in terms of π, the [DEGREES function](https://exceljet.net/functions/degrees-function)
 can be used to get the corresponding angle in degrees:

    =DEGREES(PI()) // Returns 180°
    =DEGREES(2*PI()) // Returns 360°
    

See [wumbo.net](https://wumbo.net/)
 for a more detailed explanation of key math concepts and formulas. 

PI function examples
--------------------

[![Excel formula: Surface area of a cone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/surface%20area%20of%20a%20cone.png "Excel formula: Surface area of a cone")](https://exceljet.net/formulas/surface-area-of-a-cone)

### [Surface area of a cone](https://exceljet.net/formulas/surface-area-of-a-cone)

In geometry, the formula for calculating the surface area of a right cone is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3.14159265358979, accurate to 15...

[![Excel formula: Volume of a cone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cone.png "Excel formula: Volume of a cone")](https://exceljet.net/formulas/volume-of-a-cone)

### [Volume of a cone](https://exceljet.net/formulas/volume-of-a-cone)

In geometry, the formula for calculating the volume of a cone is: The formula for calculating the volume of a cone is based on the formula for calculating the volume of a pyramid. Since the base of a cone is a circular, the formula for area of a circle is included. The Greek letter π ("pi")...

[![Excel formula: Surface area of a sphere](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/surface%20area%20of%20a%20sphere.png "Excel formula: Surface area of a sphere")](https://exceljet.net/formulas/surface-area-of-a-sphere)

### [Surface area of a sphere](https://exceljet.net/formulas/surface-area-of-a-sphere)

In geometry, a sphere is defined as the set of points that are all the same distance (r) from a given point in a three-dimensional space. The formula for calculating the surface area of a sphere is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In...

[![Excel formula: Circumference of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/circumference%20of%20a%20circle.png "Excel formula: Circumference of a circle")](https://exceljet.net/formulas/circumference-of-a-circle)

### [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)

In geometry, the circumference of a circle with radius (r) is defined by the following formula: =2πr The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Area of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20circle.png "Excel formula: Area of a circle")](https://exceljet.net/formulas/area-of-a-circle)

### [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)

In geometry, the area enclosed by a circle with radius (r) is defined by the following formula: πr 2 The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

[![Excel formula: Volume of a sphere](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20sphere.png "Excel formula: Volume of a sphere")](https://exceljet.net/formulas/volume-of-a-sphere)

### [Volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)

In geometry, a sphere is defined as a set of points that are all the same distance (r) from a given point in a three-dimensional space. The formula for calculating the volume of a sphere is: Where r represents radius, and the Greek letter π ("pi") represents the ratio of the circumference of a...

[![Excel formula: Surface area of a cylinder](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/surface%20area%20of%20a%20cylinder.png "Excel formula: Surface area of a cylinder")](https://exceljet.net/formulas/surface-area-of-a-cylinder)

### [Surface area of a cylinder](https://exceljet.net/formulas/surface-area-of-a-cylinder)

In geometry, the standard formula for calculating the surface area of a cylinder is: In essence, this formula first calculates the area of the side of the cylinder, based on the circumference of the circle times the height of the cylinder, then adds two times the area of circle to account for the...

[![Excel formula: Volume of a cylinder](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cylinder.png "Excel formula: Volume of a cylinder")](https://exceljet.net/formulas/volume-of-a-cylinder)

### [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)

In geometry, the formula for calculating the volume of a cylinder is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3.14159265358979, accurate to 15 digits: =PI...

Related functions
-----------------

[![Excel RADIANS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_radians_2.png "Excel RADIANS function")](https://exceljet.net/functions/radians-function)

### [RADIANS Function](https://exceljet.net/functions/radians-function)

The Excel RADIANS function converts degrees to radians. For example, =RADIANS(180) returns 3.1415 or the value of π (pi)....

[![Excel DEGREES function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_degrees_0.png "Excel DEGREES function")](https://exceljet.net/functions/degrees-function)

### [DEGREES Function](https://exceljet.net/functions/degrees-function)

The Excel DEGREES function converts angles (expressed in radians) to degrees. For example, the formula =DEGREES(PI()) returns 180.

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
    
*   [Surface area of a cone](https://exceljet.net/formulas/surface-area-of-a-cone)
    
*   [Volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)
    
*   [Volume of a cone](https://exceljet.net/formulas/volume-of-a-cone)
    
*   [Surface area of a cylinder](https://exceljet.net/formulas/surface-area-of-a-cylinder)
    
*   [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)
    
*   [Surface area of a sphere](https://exceljet.net/formulas/surface-area-of-a-sphere)
    
*   [Circumference of a circle](https://exceljet.net/formulas/circumference-of-a-circle)
    

### Functions

*   [RADIANS Function](https://exceljet.net/functions/radians-function)
    
*   [DEGREES Function](https://exceljet.net/functions/degrees-function)
    

### Links

*   [Microsoft PI function documentation](https://support.office.com/en-us/article/pi-function-264199d0-a3ba-46b8-975a-c4a04608989b)
    

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