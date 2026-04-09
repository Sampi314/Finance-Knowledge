# Excel PRODUCT function | Exceljet

**Source:** https://exceljet.net/functions/product-function

---

[Skip to main content](https://exceljet.net/functions/product-function#main-content)

[](https://exceljet.net/functions/product-function#)

*   [Previous](https://exceljet.net/functions/power-function)
    
*   [Next](https://exceljet.net/functions/quotient-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

PRODUCT Function
================

by Dave Bruns · Updated 11 Nov 2024

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel PRODUCT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20product%20function.png "Excel PRODUCT function")

Summary
-------

The Excel PRODUCT function returns the product of numbers provided as arguments. The PRODUCT function is helpful when multiplying many cells together. The formula =PRODUCT(A1:A3) is the same as =A1\*A2\*A3.

Purpose 
--------

Get the product of supplied numbers

Return value 
-------------

Product of supplied numbers

Syntax
------

    =PRODUCT(number1,[number2],...)

*   _number1_ - The first number or range to multiply.
*   _number2_ - \[optional\] The second number or range to multiply.

Using the PRODUCT function 
---------------------------

The Excel PRODUCT function returns the product of numbers provided as arguments. Because it can accept a [range](https://exceljet.net/glossary/range)
 of cells as an [argument](https://exceljet.net/glossary/function-argument)
, PRODUCT is useful when multiplying many cells together

The PRODUCT function takes multiple arguments in the form _number1_, _number2_, _number3_, etc. up to 255 total. Arguments can be a hardcoded constant, a cell reference, or a range. All numbers in the arguments provided are multiplied together. Empty cells and text values are ignored.

> Note: The PRODUCT function works differently from the multiplication [operator](https://exceljet.net/glossary/math-operators)
>  (\*) in that it simply _ignores_ text and empty cells. For example, if A1 contains 2 and B1 contains nothing (i.e. is blank), =PRODUCT(A1,B1) returns 2, while =A1\*A2 returns zero.

### Examples

The PRODUCT function returns the product of supplied arguments:

    =PRODUCT(3,8) // returns 24
    =PRODUCT(3,8,4) // returns 96
    

PRODUCT multiplies all numeric values together, so the following formulas are equivalent:

    =PRODUCT(A1:A5)
    =PRODUCT(A1,A2,A3,A4,A5)
    =PRODUCT(A1:A2,A3:A5)
    

PRODUCT ignores text values and empty cells. The formulas below will return the same result with all cells have numeric values:

    =PRODUCT(A1:A5)
    =A1*A2*A3*A4*A5
    

However, the second formula will return zero (0) if any cells are empty, and a #VALUE! error if any cells contain [text](https://exceljet.net/glossary/text-value)
.

### Notes

*   Numbers can be supplied individually or in ranges.
*   PRODUCT can accept up to 255 arguments total.
*   Only numbers in the array or reference are multiplied.
*   Empty cells, logical values, and text in the array or reference are ignored.

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Links

*   [Microsoft PRODUCT function documentation](https://support.office.com/en-us/article/product-function-8e6b5b24-90ee-4650-aeec-80982a0512ce)
    

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