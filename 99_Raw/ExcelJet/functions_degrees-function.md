# Excel DEGREES function | Exceljet

**Source:** https://exceljet.net/functions/degrees-function

---

[Skip to main content](https://exceljet.net/functions/degrees-function#main-content)

[](https://exceljet.net/functions/degrees-function#)

*   [Previous](https://exceljet.net/functions/csch-function)
    
*   [Next](https://exceljet.net/functions/radians-function)
    

Excel 2003

[Trigonometry](https://exceljet.net/functions#Trigonometry)

DEGREES Function
================

by Dave Bruns · Updated 24 Oct 2023

Related functions 
------------------

[RADIANS](https://exceljet.net/functions/radians-function)

[PI](https://exceljet.net/functions/pi-function)

![Excel DEGREES function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_degrees_0.png "Excel DEGREES function")

Summary
-------

The Excel DEGREES function converts angles (expressed in radians) to degrees. For example, the formula =DEGREES(PI()) returns 180.

Purpose 
--------

Converts radians to degrees

Return value 
-------------

Degrees

Syntax
------

    =DEGREES(angle)

*   _angle_ - Angle in radians that you want to convert to degrees.

Using the DEGREES function 
---------------------------

The DEGREES function takes an angle in radians and converts it to degrees. [Radians measure angles using the radius of a circle](https://wumbo.net/concepts/radian-angle-system/)
, as illustrated in this image:

![Radians measure angles using the radius of a circle](https://exceljet.net/sites/default/files/images/functions/inline/radians_0.png "Radians measure angles using the radius of a circle")

To convert degrees back to radians, you can use the [RADIANS function](https://exceljet.net/functions/radians-function)
.

### Converting degrees to radians manually

Because Pi = 180°, the general formula for degrees to radians is **degrees \* PI()/180**. For example, to convert 45° to radians, the Excel formula would be 45\*PI( )/180 which equals 0.7854 radians. More examples in the table below:

| Formula | Degrees |
| --- | --- |
| \=2\*PI() | 360 |
| \=PI() | 180 |
| \=90\*PI()/180 | 90  |
| \=45\*PI()/180 | 45  |
| \=30\*PI()/180 | 30  |
| \=20\*PI()/180 | 20  |

Related functions
-----------------

[![Excel RADIANS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_radians_2.png "Excel RADIANS function")](https://exceljet.net/functions/radians-function)

### [RADIANS Function](https://exceljet.net/functions/radians-function)

The Excel RADIANS function converts degrees to radians. For example, =RADIANS(180) returns 3.1415 or the value of π (pi)....

[![Excel PI function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20pi%20function.png "Excel PI function")](https://exceljet.net/functions/pi-function)

### [PI Function](https://exceljet.net/functions/pi-function)

The Excel PI function returns the value of the geometric constant π (pi). The value represents a half-rotation in the radian angle system. The constant appears in many formulas relating the circle, such as the area of a circle....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [RADIANS Function](https://exceljet.net/functions/radians-function)
    
*   [PI Function](https://exceljet.net/functions/pi-function)
    

### Links

*   [Microsoft DEGREES function documentation](https://support.office.com/en-us/article/degrees-function-4d6ec4db-e694-4b94-ace0-1cc3f61f9ba1)
    
*   [Illustrated article on radians (wumbo.net)](https://wumbo.net/concepts/radian-angle-system/)
    

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