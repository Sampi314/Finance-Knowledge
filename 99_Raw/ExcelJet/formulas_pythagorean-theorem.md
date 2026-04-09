# Pythagorean theorem - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/pythagorean-theorem

---

[Skip to main content](https://exceljet.net/formulas/pythagorean-theorem#main-content)

[](https://exceljet.net/formulas/pythagorean-theorem#)

*   [Previous](https://exceljet.net/formulas/distance-formula)
    
*   [Next](https://exceljet.net/formulas/surface-area-of-a-cone)
    

[Geometry](https://exceljet.net/formulas#Geometry)

Pythagorean theorem
===================

by Dave Bruns · Updated 14 May 2024

![Excel formula: Pythagorean theorem](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/pythagorean%20theorem.png "Excel formula: Pythagorean theorem")

Summary
-------

To calculate the longest side (the hypotenuse) of a right triangle in Excel, you can use a formula based on the Pythagorean theorem, adapted to use Excel's [math operators](https://exceljet.net/glossary/math-operators)
 and functions. In the example shown, the formula in D5, copied down, is:

    =SQRT(B5^2+C5^2)
    

which returns the length of the hypotenuse, given lengths of side a and aside b, given in columns B and C respectively.

Explanation 
------------

The Pythagorean theorem is a key principle in Euclidean geometry. It states that the square of the longest side of a right triangle (the hypotenuse) is equal to the sum of the squares of the other two sides. The theorem is written as an equation like this:

a2 + b2 = c2

When any two sides are know, this equation can be used to solve for the third side. When a and b are known, the length of the hypotenuse can be calculated with:

When b and c are known, the length of side a can be calculated with:

When a and c are known, length of side b can be calculated with:

To translate the above into Excel formula syntax, use the [exponentiation operator](https://exceljet.net/glossary/math-operators)
 (^) and the [SQRT function](https://exceljet.net/functions/sqrt-function)
, as seen below. The Pythagorean theorem can be written as:

    =a^2+b^2=c^2 // Pythagorean theorem
    

And the formulas below can be used to solve for each of the three sides:

    c=SQRT(a^2+b^2) // hypotenuse
    a=SQRT(c^2-b^2) // side a
    b=SQRT(c^2-a^2) // side b
    

Instead of the exponentiation operator, you can also use the POWER function like this:

    c=SQRT(POWER(a,2)+POWER(b,2))
    a=SQRT(POWER(c,2)-POWER(b,2))
    b=SQRT(POWER(c,2)-POWER(a,2))
    

The formulas above are an example of [nesting](https://exceljet.net/glossary/nesting)
 one function inside another.

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

[![Excel formula: Distance formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/distance%20formula.png "Excel formula: Distance formula")](https://exceljet.net/formulas/distance-formula)

### [Distance formula](https://exceljet.net/formulas/distance-formula)

The length of a line can be calculated with the distance formula, which looks like this: Distance is the square root of the change in x squared plus the change in y squared, where two points are given in the form (x 1 , y 1 ) and (x 2 , y 2 ). The distance formula is an example of the Pythagorean...

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
    
*   [Distance formula](https://exceljet.net/formulas/distance-formula)
    

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