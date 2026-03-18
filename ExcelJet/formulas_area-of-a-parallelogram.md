# Area of a parallelogram - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/area-of-a-parallelogram

---

[Skip to main content](https://exceljet.net/formulas/area-of-a-parallelogram#main-content)

[](https://exceljet.net/formulas/area-of-a-parallelogram#)

*   [Previous](https://exceljet.net/formulas/area-of-a-circle)
    
*   [Next](https://exceljet.net/formulas/area-of-a-trapezoid)
    

[Geometry](https://exceljet.net/formulas#Geometry)

Area of a parallelogram
=======================

by Dave Bruns · Updated 6 Jan 2021

![Excel formula: Area of a parallelogram](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/area%20of%20a%20parallelogram.png "Excel formula: Area of a parallelogram")

Summary
-------

To calculate the area of a parallelogram in Excel, you can use a standard formula with Excel's [multiplication operator](https://exceljet.net/glossary/math-operators)
. In the example shown, the formula in D5, copied down, is:

    =B5*C5
    

which calculates the area of a parallelogram given the base in column B, the height in column C. 

Generic formula
---------------

    =bh

Explanation 
------------

A parallelogram is a quadrilateral (4-sided) shape with two pairs of parallel sides. The opposite sides of a parallelogram are the same length, and the opposite angles have the same measure. In Euclidean geometry, the area enclosed by a parallelogram is defined by this formula: A=_bh_, where **b** stands for base and **h** stands for height.

In Excel, the same formula can be represented like this:

    =b*h
    

So, for example, to calculate the area of a parallelogram where **b** is 5, and **h** is 4, you can use a formula like this:

    =5*4 // returns 20
    

In the example shown, the goal is to calculate the area for eleven parallelograms using the base value in column B and the height value in column C. The formula in D5 is

    =B5*C5
    

Because both cells are entered as [relative references](https://exceljet.net/glossary/relative-reference)
, as the formula is copied down the table, it calculates a different area at each new row.

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

[![Excel formula: Area of a trapezoid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/area%20of%20a%20trapezoid.png "Excel formula: Area of a trapezoid")](https://exceljet.net/formulas/area-of-a-trapezoid)

### [Area of a trapezoid](https://exceljet.net/formulas/area-of-a-trapezoid)

In geometry, the area enclosed by a trapezoid is defined by this formula: where a is the length of side a, b is the length of side b, and h is the height, measured at a right angle to the base. In Excel, the same formula can be represented like this: =(a+b)/2\*h So, for example, to calculate the...

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
    
*   [Area of a trapezoid](https://exceljet.net/formulas/area-of-a-trapezoid)
    

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