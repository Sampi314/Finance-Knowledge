# Area of a triangle - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/area-of-a-triangle

---

[Skip to main content](https://exceljet.net/formulas/area-of-a-triangle#main-content)

[](https://exceljet.net/formulas/area-of-a-triangle#)

*   [Previous](https://exceljet.net/formulas/area-of-a-trapezoid)
    
*   [Next](https://exceljet.net/formulas/circumference-of-a-circle)
    

[Geometry](https://exceljet.net/formulas#Geometry)

Area of a triangle
==================

by Dave Bruns · Updated 24 Jan 2021

![Excel formula: Area of a triangle](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/area%20of%20a%20triangle.png "Excel formula: Area of a triangle")

Summary
-------

To calculate the area of a triangle in Excel, you can use the standard formula, adapted with Excel's math operators. In the example shown, the formula in C5, copied down, is:

    =(B5*C5)/2
    

which calculates the area of a triangle given height from column B and base from column C.

Generic formula
---------------

    =(b*h)/2

Explanation 
------------

In geometry, the area enclosed by a triangle is defined by this formula:

where b represents the base of the triangle, and h represents the height, measured at right angles to the base. In Excel, the same formula can be represented like this:

    A=b*h/2
    

So, for example, to calculate the area of a triangle with a base of 4 and a height of 3:

    =4*3/2 // returns 6
    

 In the example shown, the goal is to calculate the area for eleven triangles with base given in column B and height given in column C. The formula in D5 is:

    =(B5*C5)/2
    

As this formula is copied down the table, it calculates a different area at each new row.

_Note: The parentheses in this formula are optional and for readability only. In Excel's [order of operations](https://exceljet.net/glossary/order-of-operations)
, multiplication will occur before division, so the parentheses are unnecessary._

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

[![Excel formula: Pythagorean theorem](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pythagorean%20theorem.png "Excel formula: Pythagorean theorem")](https://exceljet.net/formulas/pythagorean-theorem)

### [Pythagorean theorem](https://exceljet.net/formulas/pythagorean-theorem)

The Pythagorean theorem is a key principle in Euclidean geometry. It states that the square of the longest side of a right triangle (the hypotenuse) is equal to the sum of the squares of the other two sides. The theorem is written as an equation like this: a 2 + b 2 = c 2 When any two sides are...

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
    
*   [Pythagorean theorem](https://exceljet.net/formulas/pythagorean-theorem)
    

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