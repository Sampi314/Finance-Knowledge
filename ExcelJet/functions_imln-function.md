# Excel IMLN function | Exceljet

**Source:** https://exceljet.net/functions/imln-function

---

[Skip to main content](https://exceljet.net/functions/imln-function#main-content)

[](https://exceljet.net/functions/imln-function#)

*   [Previous](https://exceljet.net/functions/imexp-function)
    
*   [Next](https://exceljet.net/functions/imlog10-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMLN Function
=============

by Dave Bruns · Updated 17 Oct 2024

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[LN](https://exceljet.net/functions/ln-function)

[IMABS](https://exceljet.net/functions/imabs-function)

[IMARGUMENT](https://exceljet.net/functions/imargument-function)

![Excel IMLN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imln_function_screenshot_cropped.png "Excel IMLN function")

Summary
-------

The Excel IMLN function returns the natural logarithm of a complex number.

Purpose 
--------

Get natural log complex number

Return value 
-------------

Returns the logarithm of the complex number.

Syntax
------

    =IMLN(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMLN function 
------------------------

The Excel IMLN function returns the natural logarithm of a complex number. For example, given the complex number "3+4i" as input, the function returns the logarithm of the complex number.

    =IMLN(COMPLEX(3,4)) // returns 1.6094379124341 + 0.927295218001612i

The real part of the output is equal to the natural logarithm of the distance from the origin to the point "3+4i" in the complex plane.

    =LN(IMABS(COMPLEX(3,4))) // returns 1.609437912

The imaginary part of the output is equal to the angle in radians of the complex number relative to the positive real axis.

    =IMARGUMENT(COMPLEX(3,4)) // returns 0.927295218

### Explanation

Given a complex number _z_, the complex logarithm is defined as:

![The definition of the complex logarithm.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imln_function_definition.png "The definition of the complex logarithm.")

*   The radius _r_ represents the distance from the origin to the point _z_ in the complex plane.
*   The angle _θ_ represents the angle in radians of the complex number _z_ relative to the positive real axis.

![Radius and angle of a complex number.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/RadiusAndAngleOfComplexNumber.png "Radius and angle of a complex number.")

In Excel, the complex logarithm is equal to the following formula where cell B6 contains a complex number:

    =COMPLEX(LN(IMABS(B6)),IMARGUMENT(B6))

### Visualizing the Output

The 3D graph below visualizes the real part of the function's output. The horizontal _XY_\-plane represents the input in the complex plane, and the vertical axis represents the function's real output.

![Real output of the complex logarithm.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imln_function_real_output_highlight_ln_for_reals.png "Real output of the complex logarithm.")

Geometrically, the real part of the function's output equals the natural logarithm of the distance from the origin to the point in the complex plane.

    =IMREAL(IMLN(COMPLEX(3,4))) // returns 1.609437912434100

The 3D graph below visualizes the imaginary part of the function's output. The horizontal _XY_\-plane represents the input in the complex plane, and the vertical axis represents the function's imaginary output.

![Imaginary output of complex natural logarithm.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imln_function_imaginary_output.png "Imaginary output of complex natural logarithm.")

Geometrically, the imaginary part equals the angle in radians of the complex number output by the function.

    =IMAGINARY(IMLN(COMPLEX(3,4))) // returns 0.927295218

### Relationship to the Exponential

In the context of complex numbers, the logarithm and exponential function have a slightly different relationship than they do in the context of real numbers, where they are inverses of each other. Their relationship is the same when you pass the output of the logarithm to the exponential; the result is the original input.

    =IMEXP(IMLN(COMPLEX(x,y))) // always returns x+yi

However, their relationship is different when you pass the output of the exponential to the logarithm; the result isn't necessarily the original input.

    =IMLN(IMEXP(COMPLEX(x,y))) // doesn't necessarily return x+yi

The difference is because of the exponential function's periodic nature. For example, consider a complex number written in terms of its radius and angle (polar form).

![The definition of the complex logarithm polar form.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imln_function_definition_polar_form.png "The definition of the complex logarithm polar form.")

The angle that describes the number can take on infinitely many values. Because if you add 2π to any angle, you get an equivalent complex number. This is why the complex logarithm is **multivalued** and could be expressed like this, where _k_ is some integer.

![The complex logarithm in multivalued.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imln_function_definition_multivalued.png "The complex logarithm is multivalued.")

To make the complex logarithm single-valued, the angle is restricted to a particular range from -π to π. This is called a **branch cut**, and it removes the ambiguity of the multiple angles that can describe the same complex number. The consequence of the branch cut is the function sometimes returns an equivalent angle mapped to the range from -π to π, which includes π and excludes -π.

For example, given the expression IMEXP("2 + 3π i") as input, the complex logarithm returns "2+π i".

    =IMLN(IMEXP(COMPLEX(2,3*PI()))) // returns 2+πi

### Branch Cut

The behavior of the complex logarithm for its branch cut can be demonstrated with the complex number "-1-1i". If you rotate the positive direction to the point in the complex plane, the rotation is equal to 5/4 π radians. Equivalently, if you rotate in the negative direction to the point in the complex plane, the rotation is equal to -3/4 π radians.

![Two angles describing a complex number.](https://exceljet.net/sites/default/files/styles/wumbo_watermark/public/images/functions/inline/ComplexNumberPositiveAndNegativeAngle.png "Two angles describing a complex number.")

In this case, the complex logarithm returns the branch cut from -π to π, so the returned angle is -3/4 π.

    =IMAGINARY(IMLN(COMPLEX(-1,-1))) // returns -3/4π

Of course, many more angles correspond to the point "-1-1i". Any angle outside the range -π to π gets mapped to the branch cut.

![Complex logarithm branch cut.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imln_function_tree_annotated.jpg "Complex logarithm branch cut.")

The range of the branch cut is (-π, π\], which excludes -π and includes π. This means that for points that lie on the negative real axis, where the branch cut occurs, the returned angle is π.

    =IMAGINARY(IMLN(COMPLEX(-1,0))) // returns π

The discontinuous jump of the branch cut is visualized by the 3D plot below.

![The range of imaginary output for the complex logarithm function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imln_function_imaginary_output_annotated.jpg "The range of imaginary output for the complex logarithm function.")

_Images courtesy of [wumbo.net](https://wumbo.net/)
._

### Notes

*   The function returns a #NUM! error when given zero input

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel LN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ln1.png "Excel LN function")](https://exceljet.net/functions/ln-function)

### [LN Function](https://exceljet.net/functions/ln-function)

The Excel LN function returns the natural logarithm of a given number.

[![Excel IMABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imabs_screenshot_cropped.png "Excel IMABS function")](https://exceljet.net/functions/imabs-function)

### [IMABS Function](https://exceljet.net/functions/imabs-function)

The Excel IMABS function returns the absolute value of a complex number.

[![Excel IMARGUMENT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imargument_function_screenshot_cropped_0.png "Excel IMARGUMENT function")](https://exceljet.net/functions/imargument-function)

### [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)

The Excel IMARGUMENT function returns the angle of a complex number expressed in radians. The **argument**, also known as the phase, is the angle between the positive real axis and the line the complex number lies on in the complex plane.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [COMPLEX Function](https://exceljet.net/functions/complex-function)
    
*   [LN Function](https://exceljet.net/functions/ln-function)
    
*   [IMABS Function](https://exceljet.net/functions/imabs-function)
    
*   [IMARGUMENT Function](https://exceljet.net/functions/imargument-function)
    

### Links

*   [Microsoft IMLN function documentation](https://support.office.com/en-us/article/imln-function-32b98bcf-8b81-437c-a636-6fb3aad509d8)
    

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