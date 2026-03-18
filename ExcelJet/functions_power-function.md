# Excel POWER function | Exceljet

**Source:** https://exceljet.net/functions/power-function

---

[Skip to main content](https://exceljet.net/functions/power-function#main-content)

[](https://exceljet.net/functions/power-function#)

*   [Previous](https://exceljet.net/functions/pi-function)
    
*   [Next](https://exceljet.net/functions/product-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

POWER Function
==============

by Dave Bruns · Updated 22 Aug 2021

Related functions 
------------------

[SQRT](https://exceljet.net/functions/sqrt-function)

[LOG](https://exceljet.net/functions/log-function)

![Excel POWER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20power%20function.png "Excel POWER function")

Summary
-------

The Excel POWER function returns a number raised to a given power. The POWER function is an alternative to the [exponent operator](https://exceljet.net/glossary/math-operators)
 (^).

Purpose 
--------

Raise a number to a power

Return value 
-------------

Number raised to power

Syntax
------

    =POWER(number,power)

*   _number_ - Number to raise to a power.
*   _power_ - Power to raise number to (the exponent).

Using the POWER function 
-------------------------

The POWER function returns a number raised to a given power. POWER is an alternative to the [exponent operator](https://exceljet.net/glossary/math-operators)
 (^) in a math equation.

The POWER function takes two arguments: _number_ and _power_. _Number_ should be a numeric value, provided as a hardcoded constant or as a cell reference. The _power_ argument functions as the exponent, indicating the power to which _number_ should be raised.

### Examples

To raise 2 to the 3rd power, you can use POWER like this:

    =POWER(2,3) // returns 8
    

To raise 2 to the 8th power:

    =POWER(2,8) // returns 256
    

To cube the value in cell A1:

    =POWER(A1,3) // cube A1
    

### Fractional exponents

To use the power function with a fractional exponent, enter the fraction directly as the _power_ argument:

    =POWER(27,1/3) // returns 3
    =POWER(81,1/4) // returns 3
    =POWER(256,1/8) // returns 2
    

### Exponent operator

In Excel, exponentiation can also be handled with the exponent (^) [operator](https://exceljet.net/glossary/math-operators)
, so:

    =2^2=POWER(2,2)=4
    =2^3=POWER(2,3)=8
    =2^4=POWER(2,4)=16
    

POWER function examples
-----------------------

[![Excel formula: Volume of a cylinder](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cylinder.png "Excel formula: Volume of a cylinder")](https://exceljet.net/formulas/volume-of-a-cylinder)

### [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)

In geometry, the formula for calculating the volume of a cylinder is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3.14159265358979, accurate to 15 digits: =PI...

[![Excel formula: Surface area of a sphere](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/surface%20area%20of%20a%20sphere.png "Excel formula: Surface area of a sphere")](https://exceljet.net/formulas/surface-area-of-a-sphere)

### [Surface area of a sphere](https://exceljet.net/formulas/surface-area-of-a-sphere)

In geometry, a sphere is defined as the set of points that are all the same distance (r) from a given point in a three-dimensional space. The formula for calculating the surface area of a sphere is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In...

[![Excel formula: BMI calculation formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/bmi%20calculation%20formula.png "Excel formula: BMI calculation formula")](https://exceljet.net/formulas/bmi-calculation-formula)

### [BMI calculation formula](https://exceljet.net/formulas/bmi-calculation-formula)

This example shows one way to calculate BMI (Body Mass Index) in Excel. The standard BMI formula is: BMI = weight (kg) / height (m) 2 The approach used here is to first convert height in inches and feet to meters, and weight in pounds to kilograms, then use the standard metric formula for BMI. This...

[![Excel formula: Cube root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cube%20root%20of%20number.png "Excel formula: Cube root of number")](https://exceljet.net/formulas/cube-root-of-number)

### [Cube root of number](https://exceljet.net/formulas/cube-root-of-number)

The cube root of a number can be calculated manually with the exponentiation operator (^) or with the POWER function . Manually with ^ The cube root of a number can be calculated manually by raising a number to the (1/3) using the exponentiation operator (^). In the example shown, the formula in C5...

[![Excel formula: Square root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/square%20root.png "Excel formula: Square root of number")](https://exceljet.net/formulas/square-root-of-number)

### [Square root of number](https://exceljet.net/formulas/square-root-of-number)

The SQRT function is fully automatic and will return the square root of any positive number. For example, to get the square root of 25, you can use: =SQRT(25) // returns 5 To get the square root of 16: =SQRT(16) // returns 4 To get the square root of a number in cell A1: =SQRT(A1) // square root of...

[![Excel formula: Surface area of a cone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/surface%20area%20of%20a%20cone.png "Excel formula: Surface area of a cone")](https://exceljet.net/formulas/surface-area-of-a-cone)

### [Surface area of a cone](https://exceljet.net/formulas/surface-area-of-a-cone)

In geometry, the formula for calculating the surface area of a right cone is: The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3.14159265358979, accurate to 15...

[![Excel formula: nth root of number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth%20root%20of%20number.png "Excel formula: nth root of number")](https://exceljet.net/formulas/nth-root-of-number)

### [nth root of number](https://exceljet.net/formulas/nth-root-of-number)

By definition, the nth root of a number can be calculated by raising that number to the power of 1/n. Exponents are entered using the exponentiation operator (^), with a number on the left and power on the right. So, in this example we get the numbers from column B and powers from column C: =B5^(1/...

[![Excel formula: Surface area of a cylinder](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/surface%20area%20of%20a%20cylinder.png "Excel formula: Surface area of a cylinder")](https://exceljet.net/formulas/surface-area-of-a-cylinder)

### [Surface area of a cylinder](https://exceljet.net/formulas/surface-area-of-a-cylinder)

In geometry, the standard formula for calculating the surface area of a cylinder is: In essence, this formula first calculates the area of the side of the cylinder, based on the circumference of the circle times the height of the cylinder, then adds two times the area of circle to account for the...

[![Excel formula: Volume of a cone](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20cone.png "Excel formula: Volume of a cone")](https://exceljet.net/formulas/volume-of-a-cone)

### [Volume of a cone](https://exceljet.net/formulas/volume-of-a-cone)

In geometry, the formula for calculating the volume of a cone is: The formula for calculating the volume of a cone is based on the formula for calculating the volume of a pyramid. Since the base of a cone is a circular, the formula for area of a circle is included. The Greek letter π ("pi")...

[![Excel formula: Volume of a sphere](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volume%20of%20a%20sphere.png "Excel formula: Volume of a sphere")](https://exceljet.net/formulas/volume-of-a-sphere)

### [Volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)

In geometry, a sphere is defined as a set of points that are all the same distance (r) from a given point in a three-dimensional space. The formula for calculating the volume of a sphere is: Where r represents radius, and the Greek letter π ("pi") represents the ratio of the circumference of a...

[![Excel formula: Area of a circle](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20circle.png "Excel formula: Area of a circle")](https://exceljet.net/formulas/area-of-a-circle)

### [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)

In geometry, the area enclosed by a circle with radius (r) is defined by the following formula: πr 2 The Greek letter π ("pi") represents the ratio of the circumference of a circle to its diameter. In Excel, π is represented in a formula with the PI function , which returns the number 3...

Related functions
-----------------

[![Excel SQRT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sqrt%20function.png "Excel SQRT function")](https://exceljet.net/functions/sqrt-function)

### [SQRT Function](https://exceljet.net/functions/sqrt-function)

The Excel SQRT function returns the square root of a positive number. SQRT returns an error if _number_ is negative.

[![Excel LOG function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_log_new.png "Excel LOG function")](https://exceljet.net/functions/log-function)

### [LOG Function](https://exceljet.net/functions/log-function)

The Excel LOG function returns the logarithm of a given number, using a supplied base. The base argument defaults to 10 if not supplied.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Square root of number](https://exceljet.net/formulas/square-root-of-number)
    
*   [Surface area of a cylinder](https://exceljet.net/formulas/surface-area-of-a-cylinder)
    
*   [Volume of a cylinder](https://exceljet.net/formulas/volume-of-a-cylinder)
    
*   [Volume of a cone](https://exceljet.net/formulas/volume-of-a-cone)
    
*   [nth root of number](https://exceljet.net/formulas/nth-root-of-number)
    
*   [Surface area of a sphere](https://exceljet.net/formulas/surface-area-of-a-sphere)
    
*   [Volume of a sphere](https://exceljet.net/formulas/volume-of-a-sphere)
    
*   [Area of a circle](https://exceljet.net/formulas/area-of-a-circle)
    
*   [BMI calculation formula](https://exceljet.net/formulas/bmi-calculation-formula)
    
*   [Surface area of a cone](https://exceljet.net/formulas/surface-area-of-a-cone)
    

### Functions

*   [SQRT Function](https://exceljet.net/functions/sqrt-function)
    
*   [LOG Function](https://exceljet.net/functions/log-function)
    

### Links

*   [Microsoft POWER function documentation](https://support.office.com/en-us/article/power-function-d3f2908b-56f4-4c3f-895a-07fb519c362a)
    

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