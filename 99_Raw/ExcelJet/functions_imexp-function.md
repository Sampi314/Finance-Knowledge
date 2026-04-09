# Excel IMEXP function | Exceljet

**Source:** https://exceljet.net/functions/imexp-function

---

[Skip to main content](https://exceljet.net/functions/imexp-function#main-content)

[](https://exceljet.net/functions/imexp-function#)

*   [Previous](https://exceljet.net/functions/imdiv-function)
    
*   [Next](https://exceljet.net/functions/imln-function)
    

Excel 2003

[Engineering](https://exceljet.net/functions#Engineering)

IMEXP Function
==============

by Dave Bruns · Updated 17 Oct 2024

Related functions 
------------------

[COMPLEX](https://exceljet.net/functions/complex-function)

[IMLN](https://exceljet.net/functions/imln-function)

![Excel IMEXP function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_imexp_screenshot_cropped.png "Excel IMEXP function")

Summary
-------

The Excel IMEXP function returns the exponential of a complex number.

Purpose 
--------

Get exponential of complex number.

Return value 
-------------

Returns the exponential of a complex number.

Syntax
------

    =IMEXP(complex_num)

*   _complex\_num_ - The complex number in the form "x+yi".

Using the IMEXP function 
-------------------------

The Excel IMEXP function returns the exponential of a complex number. For example, given "0+πi" as input, the function returns "-1+3.23108914886517E-15i" as output. The output is essentially -1, but due to floating point precision, it contains a very small imaginary component. 

    =IMEXP(COMPLEX(0,PI())) // returns -1 + 3.23108914886517E-15i
    

Given real number input, the function behaves like the exponential function and models exponential growth.

    =IMEXP(COMPLEX(1,0)) // returns 2.71828182845905
    

Given imaginary input representing an angle, the function returns the corresponding point on the unit circle in the complex plane.

    =IMEXP(COMPLEX(0,PI()/3)) // returns cos(π/3) + sin(π/3)i
    
    

### Notation

The complex exponential function often appears as the Latin letter e to some power. This notation is equivalent to passing the complex number as input to the exponential function.

![Complex exponential function notation.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_function_notation.png "Complex exponential function notation.")

In Excel, we write the exponential of a complex number "z=x+yi" like this:

    =IMEXP(COMPLEX(x,y))

### Euler's Formula

The complex exponential function appears in a famous math formula called "Euler's Formula," which relates i, π, and -1 together.

![Euler's formula with π radians.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_eulers_formula_pi.png "Euler's formula with π radians.")

We can write another version of this formula that better describes what's happening in terms of the angle θ.

![Euler's formula in terms of the angle θ.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_eulers_formula.png "Euler's formula in terms of the angle θ.")

Given imaginary input representing an angle, the function returns the corresponding point on the unit circle in the complex plane. For example, given the input "i π/3" the function returns the point on the unit circle corresponding to the angle of π/3 radians.

![Example output on the complex unit circle.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_eulers_formula_unit_circle.png "Example output on the complex unit circle.")

In Excel, we can see this behavior in the following formula:

    =IMEXP(COMPLEX(0,PI()/3)) // returns 0.5 + 0.866025404i

### Explanation

In math, the exponential of a complex number can be expanded using the additive property of exponentials.

![Expand complex exponential with additive property.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_expand_with_additive_property.png "Expand complex exponential with additive property.")

The right expression can be expanded further using Euler's Formula.

![Expanded exponential function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_expanded_version.png "Expanded exponential function.")

In Excel, the complex exponential function is equivalent to this formula.

    =IMPRODUCT(
        COMPLEX(EXP(x), 0), 
        COMPLEX(COS(y), SIN(y))
    )

From this, we can see the real part of the input governs the [magnitude](https://exceljet.net/functions/imabs-function)
 of the output, and the imaginary part of the input governs the [phase](https://exceljet.net/functions/imargument-function)
 (angle) of the output. For example, given the input "2+π/3", the function returns a complex number with a magnitude of EXP(2) and an angle of π/3 radians. 

    =IMEXP(COMPLEX(2,PI()/3)) // returns 3.694528049 + 6.399110292i

We can draw the returned complex number in the complex plane like this.

![Example output of the exponential function.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_example_output.png "Example output of the exponential function.")

In general, the function's output can be visualized with the 3D plot below. The horizontal XY plane represents input in the complex plane, and the vertical axis represents the magnitude of the output. The plot's surface is colored using the output's phase (angle).

![Magnitude and phase of complex exponential.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_imexp_function_output_magnitude_and_phase_0.png "Magnitude and phase of complex exponential.")

### Polar Form

The complex exponential function can express a complex number in its polar form by describing the number in terms of its radius and angle.

![Polar form of a complex number.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_polar_form_of_complex_number_equation.png "Polar form of a complex number.")

For example, to write the complex number z in Excel with a radius of 5 and an angle of π/4, we scale the point on the complex unit circle given by EXP(iθ) by the radius like this:

    =IMPRODUCT(
        COMPLEX(5,0),
        IMEXP(COMPLEX(0,PI()/4))
    ) // returns 3.535533906 + 3.535533906i

We can draw this complex number on the complex plane to visualize its coordinates.

![Polar form of a complex number.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_polar_form_of_complex_number.png "Polar form of a complex number.")

### Inverse

The inverse of the complex exponential function is the complex natural logarithm. For example, if we pass the output of the exponential function for "2+πi" to the natural logarithm, we get "2+πi" as a result.

    =IMLN(IMEXP(COMPLEX(2,PI()))) // returns 2 + πi

In general, given a complex number, the natural logarithm function returns the natural logarithm of the radius of the number for the real part and the angle of the number for the imaginary part.

![Definition of complex logarithm.](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_imexp_imln_definition.png "Definition of complex logarithm.")

Sometimes, this can result in a branch cut, where a different-but-equivalent angle is returned instead.

    =IMLN(IMEXP(COMPLEX(2,3*PI()))) // returns 2 + πi

This is discussed in more depth in the complex natural logarithm article.

_Images courtesy of_ [wumbo.net](https://wumbo.net/)
_._

Related functions
-----------------

[![Excel COMPLEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_complex_function_screenshot_cropped.png "Excel COMPLEX function")](https://exceljet.net/functions/complex-function)

### [COMPLEX Function](https://exceljet.net/functions/complex-function)

The Excel COMPLEX function returns the string representation of a complex number.

[![Excel IMLN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_imln_function_screenshot_cropped.png "Excel IMLN function")](https://exceljet.net/functions/imln-function)

### [IMLN Function](https://exceljet.net/functions/imln-function)

The Excel IMLN function returns the natural logarithm of a complex number.

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
    
*   [IMLN Function](https://exceljet.net/functions/imln-function)
    

### Links

*   [Microsoft IMEXP function documentation](https://support.office.com/en-us/article/imexp-function-c6f8da1f-e024-4c0c-b802-a60e7147a95f)
    

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