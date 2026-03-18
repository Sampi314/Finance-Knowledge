# Get integer part of a number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-integer-part-of-a-number

---

[Skip to main content](https://exceljet.net/formulas/get-integer-part-of-a-number#main-content)

[](https://exceljet.net/formulas/get-integer-part-of-a-number#)

*   [Previous](https://exceljet.net/formulas/get-decimal-part-of-a-number)
    
*   [Next](https://exceljet.net/formulas/get-number-at-place-value)
    

[Round](https://exceljet.net/formulas#Round)

Get integer part of a number
============================

by Dave Bruns · Updated 6 Jul 2021

Related functions 
------------------

[TRUNC](https://exceljet.net/functions/trunc-function)

[INT](https://exceljet.net/functions/int-function)

![Excel formula: Get integer part of a number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20integer%20part%20of%20a%20number.png "Excel formula: Get integer part of a number")

Summary
-------

To remove the decimal part of a number and return only the integer portion, you can use the [TRUNC function](https://exceljet.net/functions/trunc-function)
 to slice off the decimal. In the example, cell C6 contains this formula:

    =TRUNC(B6)
    

The TRUNC function simply truncates (i.e. removes) numbers; it doesn't not round at all.

Generic formula
---------------

    =TRUNC(number)

Explanation 
------------

With TRUNC, no rounding takes place. The [TRUNC function](https://exceljet.net/functions/trunc-function)
 simply slices off the decimal part of the number with default settings.

TRUNC actually takes an optional second argument to specify the precision of truncation, but when you don't supply this optional argument, it is assumed to be zero, and truncation happens at the decimal.

### What about INT or ROUND?

You might wonder if you can use [INT function](https://exceljet.net/functions/int-function)
, or the [ROUND function](https://exceljet.net/functions/round-function)
 instead.

The behavior of INT is identical to TRUNC (with default settings) for positive numbers — the INT function will round a number down to the next integer and then return only the integer portion of the number.

However, for negative numbers, the rounding that INT does is a bit strange. This is because INT rounds negative numbers down away from zero, no matter what the decimal value. See the last 2 examples in the screen above for an example. Because of this behavior, TRUNC is a safer option if you want the original integer portion of a number.

As you would expect, the ROUND function rounds numbers down. If you want to round to the _nearest integer_, (positive or negative) use:

    =ROUND(A1,0)
    

But be aware that the integer value _may be different_ than the number you started with due to rounding. As above, TRUNC is a safer option if you want the original integer portion of a number.

Related formulas
----------------

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

Related functions
-----------------

[![Excel TRUNC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trunc%20function.png "Excel TRUNC function")](https://exceljet.net/functions/trunc-function)

### [TRUNC Function](https://exceljet.net/functions/trunc-function)

The Excel TRUNC function returns a truncated number based on an (optional) number of digits. For example, TRUNC(4.9) will return 4, and TRUNC(-3.5) will return -3. The TRUNC function does no rounding, it simply truncates as specified.

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    

### Functions

*   [TRUNC Function](https://exceljet.net/functions/trunc-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    

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