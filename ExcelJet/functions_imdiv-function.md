# Excel IMDIV function | Exceljet

**Source:** https://exceljet.net/functions/imdiv-function

---

[Skip to main content](https://exceljet.net/functions/imdiv-function#main-content)

[](https://exceljet.net/functions/imdiv-function#)

*   [Previous](https://exceljet.net/functions/imcsch-function)
    
*   [Next](https://exceljet.net/functions/imexp-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMDIV Function
==============

by Dave Bruns · Updated 31 Jan 2025

Related functions 
------------------

[IMPRODUCT](https://exceljet.net/functions/improduct-function)

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMCONJUGATE](https://exceljet.net/functions/imconjugate-function)

![Excel IMDIV function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imdiv_function_screenshot_cropped.png "Excel IMDIV function")

Summary
-------

The Excel IMDIV function returns the quotient of two complex numbers.

Purpose 
--------

Get quotient of two complex numbers.

Return value 
-------------

The result of dividing two complex numbers.

Syntax
------

    =IMDIV(complex_num1,complex_num2)

*   _complex\_num1_ - The first complex number.
*   _complex\_num2_ - The second complex number.

Using the IMDIV function 
-------------------------

The Excel IMDIV function returns the quotient of two complex numbers. For example, given "-7+11i" and "3+5i" as input, the function returns the quotient "1+2i", which is the result of dividing the first number by the second.

    =IMDIV(COMPLEX(-7,11),COMPLEX(3,5)) // returns 1+2i

The quotient of two complex numbers can be visualized by uniformly stretching and rotating the coordinate system so that "1" goes to the complex number, which is the divisor. In this case, the transformed coordinate system (shown in blue) is stretched and rotated so that "1" (shown as the green arrow) goes to the point "3+5i". The quotient represents how to get to the first complex number, "-7 +11i", in terms of the transformed coordinates.

![The quotient of two complex numbers.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_imdiv_function_visualize_quotient.png "The quotient of two complex numbers.")

Here's another example: the result of dividing "-14-2i" by "4+2i" is equal to "-3+i". 

    =IMDIV(COMPLEX(-14,-2),COMPLEX(4,2)) // returns -3+i

If we uniformly stretch and rotate the coordinate system so that the green arrow, "1", goes to the point "4+2i", we can see that to get to the point  "-14-2i" we travel "-3+i" units in the transformed coordinate system. 

![The quotient of two complex numbers example.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_imdiv_function_visualize_quotient_example2.png "The quotient of two complex numbers example.")

We can visualize the example that corresponds to this one by switching the divisor with the quotient. In other words, the result of dividing "-14-2i" by "-3+i" is equal to "4+2i".

    =IMDIV(COMPLEX(-14,-2),COMPLEX(-3,1)) // returns 4+2i

When we uniformly stretch and rotate the coordinate system so that the green arrow, "1",  goes to the point "-3+i", now we travel "4+2i" units in the transformed coordinate system to get to the point "-14-2i".

![The quotient of two complex numbers example other way.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/exceljet_imdiv_function_visualize_quotient_example2_other_way.png "The quotient of two complex numbers example other way.")

### Explanation

When dividing complex numbers, it's not obvious how to calculate the result by hand.

![How do we divide complex numbers?](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imdiv_function_how_do_we_divide_complex_numbers_0.png "How do we divide complex numbers?")

Compare this to complex multiplication, where we can use algebra to multiply two complex numbers.

![Complex multiplication.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imdiv_function_compare_to_complex_multiplication.png "Complex multiplication.")

The key to dividing two complex numbers is to convert the problem into one we know how to solve. This is done by using the fact that multiplying a complex number by its conjugate equals a real number.

![Complex division expressed as multiplication.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imdiv_function_expressed_as_multiplication_0.png "Complex division expressed as multiplication.")

This changes the denominator into a real number, which we know how to divide by. This is how we can manually calculate the quotient of two complex numbers in Excel.

![Complex division manually calculate.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imdiv_function_division_by_hand_screenshot_cropped.png "Complex division manually calculate.")

There is a slight difference between this formula and the IMDIV function because IMDIV returns a #NUM! error instead of #DIV/0! when dividing by zero.

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

Related functions
-----------------

[![Excel IMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_improduct_function_screenshot_cropped_0.png "Excel IMPRODUCT function")](https://exceljet.net/functions/improduct-function)

### [IMPRODUCT Function](https://exceljet.net/functions/improduct-function)

The Excel IMPRODUCT function returns the product of one or more complex numbers.

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMCONJUGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imconjugate_function_screenshot_cropped.png "Excel IMCONJUGATE function")](https://exceljet.net/functions/imconjugate-function)

### [IMCONJUGATE Function](https://exceljet.net/functions/imconjugate-function)

The Excel IMCONJUGATE function returns the conjugate of a complex number. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [IMPRODUCT Function](https://exceljet.net/functions/improduct-function)
    
*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    
*   [IMCONJUGATE Function](https://exceljet.net/functions/imconjugate-function)
    

### Articles

*   [Complex Numbers in Excel](https://exceljet.net/articles/complex-numbers-in-excel)
    

### Links

*   [Microsoft IMDIV function documentation](https://support.office.com/en-us/article/imdiv-function-a505aff7-af8a-4451-8142-77ec3d74d83f)
    

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