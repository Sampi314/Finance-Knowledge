# Number is whole number - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/number-is-whole-number

---

[Skip to main content](https://exceljet.net/formulas/number-is-whole-number#main-content)

[](https://exceljet.net/formulas/number-is-whole-number#)

*   [Previous](https://exceljet.net/formulas/nth-root-of-number)
    
*   [Next](https://exceljet.net/formulas/odometer-gas-mileage-log)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Number is whole number
======================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

[TRUNC](https://exceljet.net/functions/trunc-function)

[INT](https://exceljet.net/functions/int-function)

![Excel formula: Number is whole number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/number%20is%20whole%20number.png "Excel formula: Number is whole number")

Summary
-------

To test if a number is a whole number, you can use the [MOD function](https://exceljet.net/functions/mod-function)
. In the example shown, the formula in C5, copied down, is:

    =MOD(B5,1)=0
    

This formula returns TRUE if a value is a whole number, and FALSE if not.

Generic formula
---------------

    =MOD(A1)=0

Explanation 
------------

In this example, the goal is to test if a numeric value is a whole number. There are several ways to go about this. One of the easiest ways is to use the [MOD function](https://exceljet.net/functions/mod-function)
 with a divisor of 1. Any whole number divided by 1 will result in a remainder of zero:

    =MOD(5,1)=0 // whole numbers return zero
    

Any decimal number will have a remainder equal to the decimal portion of the number:

    =MOD(5.25,1)=0.25
    

Therefore, we can simply compare the result to zero with a [logical expression](https://exceljet.net/glossary/logical-test)
 that returns TRUE or FALSE:

    =MOD(5,1)=0 // returns TRUE
    =MOD(5.5,1)=0 // returns FALSE
    

This is the approach taken in the worksheet as shown, where the formula in C5 is:

    =MOD(B5,1)=0
    

At each row in the data, the formula returns TRUE for whole numbers only.

### INT or TRUNC

Another way to solve the problem is with the [INT function](https://exceljet.net/functions/int-function)
 or the [TRUNC function](https://exceljet.net/functions/trunc-function)
. In this approach, we run the value through one of these functions and compare the result to the _original_ value. If the values match, we know we have a whole number. The formulas look like this:

    =A1=INT(A1)
    =A1=TRUNC(A1)
    

Both of these formulas compare the original value in A1 to the same value after removing the decimal portion of the number (if any). Both formulas work fine, but note they behave differently with negative decimal values. For example, if A1 contains -5.5:

    =A1=INT(A1)
    =-5.5=INT(-5.5)
    =-5.5=-6 // returns FALSE
    

whereas:

    =A1=TRUNC(A1)
    =-5.5=TRUNC(-5.5)
    =-5.5=-5 // returns FALSE
    

In short, the TRUNC function actually _removes_ the decimal portion of a number, while the INT function _always rounds the number down_ to the next whole value. This matters for negative values, because they are rounded away from zero (i.e. they become more negative). That said, it doesn't make a difference in this example. INT still returns the correct result for negative decimal numbers because the integer changes and the result of the comparison is always FALSE.

Related formulas
----------------

[![Excel formula: Highlight integers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20integers%20only.png "Excel formula: Highlight integers only")](https://exceljet.net/formulas/highlight-integers-only)

### [Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)

The MOD function returns the remainder after division. With a divisor of 1, MOD will return zero for any whole number. We use this fact to construct a simple formula that tests the result of MOD. When the result is zero (i.e. when the number is an integer) the formula returns TRUE, triggering the...

[![Excel formula: Get integer part of a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20integer%20part%20of%20a%20number.png "Excel formula: Get integer part of a number")](https://exceljet.net/formulas/get-integer-part-of-a-number)

### [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)

With TRUNC, no rounding takes place. The TRUNC function simply slices off the decimal part of the number with default settings. TRUNC actually takes an optional second argument to specify the precision of truncation, but when you don't supply this optional argument, it is assumed to be zero, and...

[![Excel formula: Extract date from a date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20date%20from%20date%20and%20time.png "Excel formula: Extract date from a date and time")](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

### [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)

Excel handles dates and time using a scheme in which dates are serial numbers and times are fractional values . For example, June 1, 2000 12:00 PM is represented in Excel as the number 36678.5, where 36678 is the date portion and .5 is the time portion. If you have dates that include time, you can...

Related functions
-----------------

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

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

*   [Highlight integers only](https://exceljet.net/formulas/highlight-integers-only)
    
*   [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)
    
*   [Extract date from a date and time](https://exceljet.net/formulas/extract-date-from-a-date-and-time)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    
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