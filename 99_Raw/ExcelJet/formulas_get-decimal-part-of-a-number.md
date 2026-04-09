# Get decimal part of a number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-decimal-part-of-a-number

---

[Skip to main content](https://exceljet.net/formulas/get-decimal-part-of-a-number#main-content)

[](https://exceljet.net/formulas/get-decimal-part-of-a-number#)

*   [Previous](https://exceljet.net/formulas/rank-without-ties)
    
*   [Next](https://exceljet.net/formulas/get-integer-part-of-a-number)
    

[Round](https://exceljet.net/formulas#Round)

Get decimal part of a number
============================

by Dave Bruns · Updated 22 Sep 2020

Related functions 
------------------

[TRUNC](https://exceljet.net/functions/trunc-function)

![Excel formula: Get decimal part of a number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20decimal%20part%20of%20a%20number.png "Excel formula: Get decimal part of a number")

Summary
-------

To get just the decimal part of a number, you can use a formula based on the [TRUNC function](https://exceljet.net/functions/trunc-function)
. In the example shown, the formula in cell C6 is:

    =B6-TRUNC(B6)
    

Generic formula
---------------

    =number-TRUNC(number)

Explanation 
------------

Excel contains a number of rounding functions. Two of these functions, the [INT function](https://exceljet.net/functions/int-function)
 and the [TRUNC function](https://exceljet.net/functions/trunc-function)
 will return the integer portion of a number that contains  a decimal value.

The INT function behaves a bit differently with negative values, so in this example we are using the TRUNC function. The TRUNC function simply truncates (i.e. removes) decimal values if they exist – it doesn't do any rounding.

In the example shown, cell C6 contains this formula:

    =B6-TRUNC(B6)
    

The TRUNC function returns the integer portion of the number which is then subtracted from the original value. The result is the decimal portion of the number.

If the original number is an integer to begin with, the result of this formula is zero.

Related formulas
----------------

[![Excel formula: Get integer part of a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20integer%20part%20of%20a%20number.png "Excel formula: Get integer part of a number")](https://exceljet.net/formulas/get-integer-part-of-a-number)

### [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)

With TRUNC, no rounding takes place. The TRUNC function simply slices off the decimal part of the number with default settings. TRUNC actually takes an optional second argument to specify the precision of truncation, but when you don't supply this optional argument, it is assumed to be zero, and...

Related functions
-----------------

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)
    

### Functions

*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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