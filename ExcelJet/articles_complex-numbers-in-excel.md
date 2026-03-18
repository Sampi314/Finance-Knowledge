# Complex Numbers in Excel | Exceljet

**Source:** https://exceljet.net/articles/complex-numbers-in-excel

---

[Skip to main content](https://exceljet.net/articles/complex-numbers-in-excel#main-content)

[](https://exceljet.net/articles/complex-numbers-in-excel#)

*   [Previous](https://exceljet.net/articles/regular-expressions-in-excel)
    
*   [Next](https://exceljet.net/new-excel-functions)
    

Complex Numbers in Excel
========================

by Kurt Bruns · Updated 20 May 2025

![Complex numbers in Excel.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/exceljet_complex_numbers_in_excel_splash_smaller.png "Complex numbers in Excel.")

Summary
-------

Excel has supported the complex number system for years. Engineers use it to solve problems related to electronics, fluid dynamics, and signal processing. The way Excel's formula engine implements complex numbers is an example of functional programming, a paradigm that Microsoft has invested heavily in recently with the latest updates and functions.

### Introduction

The complex number system is an extension of real numbers. Historically, the invention of complex numbers allowed mathematicians to find the roots of previously unsolvable polynomials. Nowadays, engineers use complex numbers to solve problems related to electronics, signal processing, and fluid dynamics. Famous equations like Euler's Identity, Maxwell's equations, and Schrödinger's equation in quantum mechanics are examples of where the number system is used.

Excel supports complex numbers with functions that allow users to perform addition, multiplication, exponentiation, and other operations. The way the formula engine implements complex numbers is an example of functional programming. While complex functions have existed for years, Excel has recently evolved to provide more support for this paradigm with functions like [LET](https://exceljet.net/functions/let-function)
, [LAMBDA](https://exceljet.net/functions/lambda-function)
, [REDUCE](https://exceljet.net/functions/reduce-function)
, and [MAP](https://exceljet.net/functions/map-function)
. These new functions make it easier to use complex numbers in Excel without needing helper columns or array formulas.

Even if you don't plan to use complex numbers in Excel anytime soon, they are an interesting example of how a functional programming approach can solve many problems. This article gives an overview of complex numbers and their operations in Excel and provides an example that uses some of the new functions.

### What is a complex number?

A complex number is represented as "x+yi", where _x_ and _y_ are real numbers, and _i_ is the imaginary unit satisfying the equation _i2\=-1_. For example, the complex number "4+3i" has a real part of 4 and an imaginary part of 3. In Excel, we enter this complex number in a cell like this:

    ="4+3i" // the complex number z
    

We draw this complex number as an arrow in the complex plane.

![A complex number is drawn as an arrow.](https://exceljet.net/sites/default/files/images/articles/inline/DrawAsArrow.png "A complex number is drawn as an arrow.")

In Excel, complex numbers are passed to functions as strings containing the suffix "i" or "j". For example, to add two complex numbers together, we pass them to the [IMSUM](https://exceljet.net/functions/imsum-function)
 function like this.

    =IMSUM("2+3i", "5+7i") // returns "7+10i"
    

You can also construct a complex number using the [COMPLEX](https://exceljet.net/functions/complex-function)
 function, which avoids dealing with strings altogether.

    =COMPLEX(4,3) // returns "4+3i"
    

 To get the real part of the complex number, use the [IMREAL](https://exceljet.net/functions/imreal-function)
 function.

    =IMREAL(COMPLEX(4,3)) // returns 4
    

Use the [IMAGINARY](https://exceljet.net/functions/imaginary-function)
 function to get the imaginary part of the complex number.

    =IMAGINARY(COMPLEX(4,3)) // returns 3
    

Conceptually, the complex number system is a two-dimensional number system that describes rotations. In math, the property i² = -1 defines the number system algebraically and is how the number system encodes rotations.

![Defining property of complex numbers.](https://exceljet.net/sites/default/files/images/articles/inline/ImaginaryUnit.png "Defining property of complex numbers.")

Of course, Excel handles this logic for us, but knowing this property is useful because it's how you calculate the result of an operation with complex numbers by hand. For example, to multiply the complex numbers "i" and "4+3i" together, you apply this property to calculate the product.

![Rotate by "i" calculation.](https://exceljet.net/sites/default/files/images/articles/inline/RotateByICalculation.png "Rotate by "i" calculation.")

We perform this same multiplication in Excel using a function call.

    =IMPRODUCT("i", "4+3i") // returns -3+4i
    

Visually, multiplying a complex number like "4+3i" by "i" rotates the number 90 degrees counterclockwise around the origin.

![Rotate by "i".](https://exceljet.net/sites/default/files/images/articles/inline/RotateByI.png "Rotate by "i".")

As shown in this basic example, complex numbers describe rotations. Because of this, a complex number is often characterized by its radius and angle. The radius of the complex number "4+3i" we've been working with so far is 5, and the angle is 0.643501109 radians (approximately 37 degrees).

![Radius and angle of "4+3i".](https://exceljet.net/sites/default/files/images/articles/inline/ComplexNumberRadiusAndAngle.png "Radius and angle of "4+3i".")

The angle of a complex number is measured in [radians](https://exceljet.net/glossary/radians)
 from the positive real axis, where counterclockwise is positive. The angle is also referred to as the phase of the complex number. To get the angle of the complex number, use the [IMARGUMENT](https://exceljet.net/functions/imargument-function)
 function.

    =IMARGUMENT(COMPLEX(4,3)) // returns 0.643501109
    

To get the magnitude or length of the complex number, use the [IMABS](https://exceljet.net/IMABS)
 function.

    =IMABS(COMPLEX(4,3)) // returns 5

### Complex Operations

To add two complex numbers together, use the [IMSUM](https://exceljet.net/functions/imsum-function)
 function. For example, to add the complex numbers "4+3i" and "2-5i" together, use the following formula.

    =IMSUM(
        COMPLEX(4, 3),
        COMPLEX(2,-5)
    ) // returns "6-2i"

The sum of two complex numbers is drawn by arranging the arrows tip-to-tail and drawing an arrow from the origin to the tip of the second number. This arrow is equal to the sum of the complex numbers.

![Complex addition.](https://exceljet.net/sites/default/files/images/articles/inline/ComplexAddition.png "Complex addition.")

Use the [IMPRODUCT](https://exceljet.net/functions/improduct-function)
 function to multiply complex numbers together. For example, use the following formula to multiply the complex numbers "1+2i" and "3+5i" together.

    =IMPRODUCT(
        COMPLEX(1, 2),
        COMPLEX(3, 5)
    ) // returns -7+11i

We can visualize the product of the two numbers by transforming the coordinate system (shown in blue) so that the one (the green arrow) goes to the number "3+5i" in the complex plane. When we draw the transformed position of the other number, "1+2i", its tip sits at the result of the multiplication.

![Complex multiplication.](https://exceljet.net/sites/default/files/images/articles/inline/ComplexMultiplication.png "Complex multiplication.")

The [IMPRODUCT](https://exceljet.net/functions/improduct-function)
 page discusses this in more detail. The point is Excel has a whole suite of functions for performing complex operations in addition to [IMSUM](https://exceljet.net/functions/imsum-function)
 and [IMPRODUCT](https://exceljet.net/functions/improduct-function)
, such as [IMSUB](https://exceljet.net/functions/imsub-function)
, [IMDIV](https://exceljet.net/functions/imdiv-function)
, [IMSQRT](https://exceljet.net/functions/imsqrt-function)
, and [IMPOWER](https://exceljet.net/functions/impower-function)
. Each function corresponds to an operation that you perform with complex numbers.

### Complex Functions in Excel

Below is a table of the functions we've discussed so far. It also contains one function we haven't discussed yet, which is perhaps the most important function to know about complex numbers. The full list of 20+ complex functions is documented in the Engineering section of our functions reference [here](https://exceljet.net/functions#Engineering)
. 

| Function | Purpose |
| --- | --- |
| [COMPLEX](https://exceljet.net/functions/complex-function) | Creates a complex number |
| [IMREAL](https://exceljet.net/functions/imreal-function) | Get the real part of a complex number |
| [IMAGINARY](https://exceljet.net/functions/imaginary-function) | Get the imaginary part of a complex number |
| [IMABS](https://exceljet.net/functions/imabs-function) | Get the magnitude of a complex number |
| [IMARGUMENT](https://exceljet.net/functions/imargument-function) | Get the angle of a complex number |
| [IMSUM](https://exceljet.net/functions/imsum-function) | Get the sum of complex numbers |
| [IMPRODUCT](https://exceljet.net/functions/improduct-function) | Get the product of complex numbers |
| [IMEXP](https://exceljet.net/functions/imexp-function) | Get the exponential of a complex number |

In practice, using complex numbers in Excel involves translating math into a series of complex function calls. Nothing is a better example of this than [IMEXP](https://exceljet.net/functions/imexp-function)
 or the complex exponential function.

### The Complex Exponential Function

Anytime the letter _e_ is raised to a power containing the complex constant _"i"_ in equations and formulas, we express this in Excel using the [IMEXP](https://exceljet.net/functions/imexp-function)
 function. For example, the formula for a discrete Fourier transform looks like this.

![Discrete Fourier transformation example.](https://exceljet.net/sites/default/files/images/articles/inline/DiscreteFourierTransformExample.png "Discrete Fourier transformation example.")

We'll discuss the specifics of this example later. For now, know that raising _e_ to a complex number "z = x + yi" is the same as passing the complex number as input to the [IMEXP](https://exceljet.net/functions/imexp-function)
 function in Excel.

    =IMEXP(z) // we write e^z like this

Complex numbers typically appear with the exponential function. Quite famously, the output of this function for complex input is defined by the trigonometric functions sine and cosine.

    =IMEXP("θi") // returns cos(θ) + i sin(θ)

This formula is called **Euler's Formula**. One way to quickly understand why it is so useful is to use it to rotate a complex number in the complex plane. For example, to rotate "4 + 3i" around the origin by 270 degrees, multiply the complex number by the value produced by the formula and the angle.

    =IMPRODUCT(
      COMPLEX(4, 3),
      IMEXP(COMPLEX(0, RADIANS(270)))
    ) // returns "3-4i"

Visually, this corresponds to rotating the number counterclockwise around the origin by the angle.

![Rotate a complex number by an angle.](https://exceljet.net/sites/default/files/images/articles/inline/RotateByAngle.png "Rotate a complex number by an angle.")

Much more can be said about the [IMEXP](https://exceljet.net/functions/imexp-function)
 function's useful properties and how it relates to trigonometry. See also the related functions, such as [IMLN](https://exceljet.net/functions/imln-function)
, [IMSIN](https://exceljet.net/functions/imsin-function)
, [IMCOS](https://exceljet.net/functions/imcos-function)
, and more. Since complex numbers typically appear with the exponential function, it's a great place to learn more about the number system.

### Signal Processing Example

Complex numbers appear in contexts involving rotations, oscillations, and wave-like phenomena. In practice, we translate the math that describes these applications into a bunch of function calls to calculate results using complex numbers. This means using a function like [IMSUM](https://exceljet.net/functions/imsum-function)
 instead of the plus (+) operator to describe addition. Recently, Excel's formula engine has been changing to make these calculations easier without helper columns. New functions like [LET](https://exceljet.net/functions/let-function)
, [LAMBDA](https://exceljet.net/functions/lambda-function)
, [MAP](https://exceljet.net/functions/map-function)
, and [SEQUENCE](https://exceljet.net/functions/sequence-function)
 allow for a more functional programming approach when calculating results.

To be clear, using complex numbers in Excel is already an example of functional programming. These new functions just make the intermediate calculations easier to perform. A good example is the formula for a Discrete Fourier Transform.

![Discrete Fourier transform formula.](https://exceljet.net/sites/default/files/images/articles/inline/DiscreteFourierTransformFormula.png "Discrete Fourier transform formula.")

This formula is the same version as the one you'll find on the Discrete Fourier Transform [Wikipedia page](https://en.wikipedia.org/wiki/Discrete_Fourier_transform)
. We'll also use the small array of sample data and expected output that someone has provided on the Wikipedia page.

![Discrete Fourier transform sample data and expected result.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/DiscreteFourierTransfromExpected_screenshot_cropped.png "Discrete Fourier transform sample data and expected result.")

Given an array of sample data, this formula returns a complex number for k, where k is a number that starts at zero and goes to the sample size minus one. This formula has a lot going on, so let's break it down. Inside the summation, we multiply an element of the sample array by _e_ raised to some complex power, including π and some variables related to the sample data.

![Discrete Fourier transform intermediate calculation.](https://exceljet.net/sites/default/files/images/articles/inline/DiscreteFourierTransformIntermediateValue.png "Discrete Fourier transform intermediate calculation.")

In Excel, we calculate this intermediate value using the [IMPRODUCT](https://exceljet.net/functions/improduct-function)
 function and the [IMEXP](https://exceljet.net/functions/imexp-function)
 function.

    IMPRODUCT(
        INDEX(sampleArray, n),
        IMEXP(COMPLEX(0, -2 * PI() * k * (n - 1) / m))
    )

These intermediate values are wrapped in the summation operator, meaning we want to sum together the values for each value of n, ranging from 0 to the size of the sample array minus one. This is where the new functions come in handy. We can wrap the expression that calculates an intermediate value in a [LAMBDA](https://exceljet.net/functions/lambda-function)
 function that takes in an index of the sample array. This function is passed to [MAP](https://exceljet.net/functions/map-function)
 along with an array of indices to calculate all of the intermediate complex values, which we sum together with [IMSUM](https://exceljet.net/functions/imsum-function)
.

    =LET(
        sampleArray, B3:B6,
        m, ROWS(sampleArray),
        k, 0,
        IMSUM(
            MAP(
                SEQUENCE(m),
                LAMBDA(n,
                    IMPRODUCT(
                        INDEX(sampleArray, n),
                        IMEXP(COMPLEX(0, -2 * PI() * k * (n - 1) / m))
                    )
                )
            )
        )
    )

This formula calculates the sum for k=0, which, with our sample data, we expect to be 2. Note that _m_ has been substituted for _N_ because Excel does not distinguish the lowercase n from the capital N in the formula.

Now, you could use a helper column to provide values for k and copy this formula down to calculate the results of the discrete Fourier transform, but let's generate and pass in the values of k ourselves. This involves wrapping the previous formula in a lambda that takes k as input and passing that lambda to the [MAP](https://exceljet.net/functions/map-function)
 function. Here is the full formula, which "spills" the results in the cell's column.

    =LET(
        sampleArray, B3:B6,
        m, ROWS( sampleArray),
        kValues, SEQUENCE(m, 1, 0, 1),
        x_k, LAMBDA(k,
            IMSUM(
                MAP(
                    SEQUENCE(m),
                    LAMBDA(n,
                        IMPRODUCT(
                            INDEX(sampleArray, n),
                            IMEXP(COMPLEX(0, -2 * PI() * k * (n - 1) / m))
                        )
                    )
                )
            )
        ),
        MAP(kValues, x_k)
    )

This is the result when you enter the formula in Excel.

![Discrete Fourier transform sample data and actual result.](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/DiscreteFourierTransformActual_screenshot_cropped.png "Discrete Fourier transform sample data and actual result.")

There are a couple of things to note about calculating the results of a Discrete Fourier Transform in Excel this way. The first is that due to the error in floating-point arithmetic, the actual results are slightly different from what we expected. For example, when we compare the numbers for k=2, we expect the result to be -2i when we calculated it to be -3.33066907387547E-15-2.00000000000001i. This number is really close to the value of -2i but not quite exactly equal to -2i.

The second thing to note is that there are faster algorithms than this formula to calculate the discrete Fourier transform. When testing this formula on sample arrays of less than 500 samples, it performs well. However, when testing this formula on an array of 1024 samples, it took about 5 seconds to calculate the results (results may vary depending on your computer specs). Excel actually provides an implementation of Fast Fourier Transform in the [Analysis ToolPak](https://support.microsoft.com/en-us/office/use-the-analysis-toolpak-to-perform-complex-data-analysis-6c67ccf0-f4a9-487c-8dec-bdb5a2cefab6)
, which is an add-in provided for free by Microsoft. This completes almost immediately for the same-sized sample array. When using the FFT algorithm, the size of the array must be a power of 2 and can be no larger than 4096 samples.

The existence of this add-in does not diminish the fact that we calculated a Discrete Fourier Transform in Excel using a functional programming approach. It's a good example of how the new functions can be used to describe something quite complicated. It's not hard to imagine someone implementing an FFT algorithm using this kind of approach, but that certainly is out of the scope of this article.

This article was written by Kurt Bruns. He runs a math website called [_wumbo.net_](https://wumbo.net/)
, focused on math visual and explanations, much like the examples in this post.

Have you solved an interesting problem with complex numbers in Excel? [Let us know](https://exceljet.net/contact)
.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

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