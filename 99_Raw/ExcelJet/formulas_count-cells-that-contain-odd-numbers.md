# Count cells that contain odd numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-that-contain-odd-numbers

---

[Skip to main content](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers#main-content)

[](https://exceljet.net/formulas/count-cells-that-contain-odd-numbers#)

*   [Previous](https://exceljet.net/formulas/count-cells-that-contain-numbers)
    
*   [Next](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)
    

[Count](https://exceljet.net/formulas#Count)

Count cells that contain odd numbers
====================================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISODD](https://exceljet.net/functions/isodd-function)

[MOD](https://exceljet.net/functions/mod-function)

[ISEVEN](https://exceljet.net/functions/iseven-function)

![Excel formula: Count cells that contain odd numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20that%20contain%20odd%20numbers.png "Excel formula: Count cells that contain odd numbers")

Summary
-------

To count cells that contain only odd numbers, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and the [ISODD function](https://exceljet.net/functions/isodd-function)
. In the example shown, the formula in cell E6 is:

    =SUMPRODUCT(--ISODD(+data))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15. The result is 4 since there are four odd numbers in the range B5:B15.

Generic formula
---------------

    =SUMPRODUCT(--ISODD(+range))

Explanation 
------------

In this example, the goal is to count odd numbers in the range B5:B15, which is named **data**. This can be done with the SUMPRODUCT function together with the ISODD function. Instead of ISODD, the MOD function can also be used. Both approaches are explained below.

### SUMPRODUCT with ISODD

The SUMPRODUCT function works directly with arrays. One thing you can do quite easily with SUMPRODUCT is perform a [logical test](https://exceljet.net/glossary/logical-test)
 on a range, then count the results. In this case, we want to count odd numbers, and the simplest way to do that is with the [ISODD function](https://exceljet.net/functions/isodd-function)
. The ISODD function returns TRUE when given an odd number and FALSE when given an even number:

    =ISODD(9)// returns FALSE
    =ISODD(4)// returns TRUE
    

In the worksheet shown, the formula in E6 is:

    =SUMPRODUCT(--ISODD(+data))
    

Working from the inside out, the logical test is based on the ISODD function:

    ISODD(+data)
    

In this case, because **data** (B5:B15) contains 11 values, the ISODD function returns 11 results in an array like this\*:

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

_\* There are a small number of functions in Excel that will not [spill](https://exceljet.net/glossary/spill)
 when given a range of values. ISODD is one of these functions. The + operator is an easy way to make ISODD return all results._

In this array, the TRUE values correspond to cells that contain odd numbers, and the FALSE values represent cells that contain even numbers. To convert the TRUE and FALSE values to 1s and 0s, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --{FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

The resulting array inside the SUMPRODUCT function looks like this:

    =SUMPRODUCT({0;0;1;0;0;0;0;1;1;0;1}) // returns 4
    

With a single array to process, SUMPRODUCT sums the array and returns 4 as the result.

### SUMPRODUCT with MOD

Another way to solve this problem is to use the [MOD function](https://exceljet.net/functions/mod-function)
 like this:

    =SUMPRODUCT(--(MOD(data,2)=1))
    

Here the logical test for odd numbers looks is this expression:

    MOD(data,2)=1
    

MOD returns a remainder after division. Since, the divisor is 2, MOD will return a remainder of 1 for any odd integer, and a remainder of zero for an even integer. We therefore test for 1. Since there are 11 values in **data** (B5:B15), the result is an array of 11 TRUE / FALSE values:

    {FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

To convert the TRUE and FALSE values to 1s and 0s, we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --{FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

The resulting array inside the SUMPRODUCT function looks like this:

    =SUMPRODUCT({0;0;1;0;0;0;0;1;1;0;1}) // returns 4
    

With a single array to process, SUMPRODUCT sums the array and returns 4 as the result.

### Counting even numbers

As you might guess, you can count even numbers in a range by making small adjustments to the formulas above. To adapt the ISODD version of the formula to count even numbers, simply replace the ISODD function with the [ISEVEN function](https://exceljet.net/functions/iseven-function)
 like this:

    =SUMPRODUCT(--ISEVEN(+data)) // returns 7
    

To adapt the MOD function version of the formula, adjust the logic to check for zero instead of 1:

    =SUMPRODUCT(--(MOD(data,2)=0)) // returns 7
    

The behavior of these formulas is the same as described previously, and both formulas return 7, since the range B5:B15 contains 7 even numbers.

Related formulas
----------------

[![Excel formula: Count cells that contain numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20numbers.png "Excel formula: Count cells that contain numbers")](https://exceljet.net/formulas/count-cells-that-contain-numbers)

### [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)

In this example, the goal is to count the number of cells in a range that contain numbers. This problem can be solved with the COUNT function or the SUMPRODUCT function. Both methods are explained below. COUNT function The COUNT function counts the number of cells in a range that contain numeric...

[![Excel formula: Count cells over n characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20over%20n%20characters.png "Excel formula: Count cells over n characters")](https://exceljet.net/formulas/count-cells-over-n-characters)

### [Count cells over n characters](https://exceljet.net/formulas/count-cells-over-n-characters)

In this example, the goal is to count the number of cells in a range that are over a certain number of characters in length, where the number ( n ) is provided as a variable in cell F4. This problem can be solved with the SUMPRODUCT and LEN functions like this: =SUMPRODUCT(N(LEN(B5:B15)>F4)) //...

[![Excel formula: Count cells that contain negative numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20negative%20numbers.png "Excel formula: Count cells that contain negative numbers")](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)

### [Count cells that contain negative numbers](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)

In this example, the goal is to count the number of cells in a range that contain negative numbers. For convenience, the range B5:B15 is named data . This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both methods are explained below. COUNTIF function The COUNT...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISODD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isodd%20function.png "Excel ISODD function")](https://exceljet.net/functions/isodd-function)

### [ISODD Function](https://exceljet.net/functions/isodd-function)

The Excel ISODD function returns TRUE when a value is an odd number, and FALSE when a value is an even number. ISODD will return the #VALUE error if a value is not numeric.

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel ISEVEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iseven%20function.png "Excel ISEVEN function")](https://exceljet.net/functions/iseven-function)

### [ISEVEN Function](https://exceljet.net/functions/iseven-function)

The Excel ISEVEN function returns TRUE when a value is an even number, and FALSE when a value is an odd number. ISEVEN will return the #VALUE error if a value is not numeric.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)
    
*   [Count cells over n characters](https://exceljet.net/formulas/count-cells-over-n-characters)
    
*   [Count cells that contain negative numbers](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISODD Function](https://exceljet.net/functions/isodd-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [ISEVEN Function](https://exceljet.net/functions/iseven-function)
    

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