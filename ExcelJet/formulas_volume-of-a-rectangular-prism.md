# Volume of a rectangular prism - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/volume-of-a-rectangular-prism

---

[Skip to main content](https://exceljet.net/formulas/volume-of-a-rectangular-prism#main-content)

[](https://exceljet.net/formulas/volume-of-a-rectangular-prism#)

*   [Previous](https://exceljet.net/formulas/volume-of-a-cylinder)
    
*   [Next](https://exceljet.net/formulas/volume-of-a-sphere)
    

[Geometry](https://exceljet.net/formulas#Geometry)

Volume of a rectangular prism
=============================

by Dave Bruns · Updated 11 Jan 2021

![Excel formula: Volume of a rectangular prism](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/volume%20of%20rectangular%20prism.png "Excel formula: Volume of a rectangular prism")

Summary
-------

To calculate the volume of a rectangular prism, you can use Excel's multiplication [operator](https://exceljet.net/glossary/math-operators)
 (\*) with measurements for length, width, and height. In the example shown, the formula in E5, copied down, is:

    =B5*C5*D5
    

which calculates the volume of a rectangular prism, given the length in column B (l), the width in column C (w) and the height in column D (h). Units are indicated generically with "u", and the resulting volume is in units cubed (u3).

Generic formula
---------------

    =l*w*h

Explanation 
------------

In geometry, the formula for calculating the volume of a rectangular prism is: 

    =lwh
    

This formula can be represented in Excel with the multiplication [operator](https://exceljet.net/glossary/math-operators)
 (\*) like this

    =l*w*h
    

In the example shown, the formula in E5 is:

    =B5*C5*D5 // returns 0.13
    

As the formula is copied down the column, it calculates a new volume in each row, using the length in column B (l), the width in column C (w) and the height in column D (h).

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