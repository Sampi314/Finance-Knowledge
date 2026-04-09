# Change negative numbers to positive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/change-negative-numbers-to-positive

---

[Skip to main content](https://exceljet.net/formulas/change-negative-numbers-to-positive#main-content)

[](https://exceljet.net/formulas/change-negative-numbers-to-positive#)

*   [Previous](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)
    
*   [Next](https://exceljet.net/formulas/check-register-balance)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Change negative numbers to positive
===================================

by Dave Bruns · Updated 25 Jun 2019

Related functions 
------------------

[ABS](https://exceljet.net/functions/abs-function)

![Excel formula: Change negative numbers to positive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/change%20negative%20numbers%20to%20positive.png "Excel formula: Change negative numbers to positive")

Summary
-------

To change negative numbers to positive and leave positive numbers along (i.e. get absolute values) use the built-in [ABS function](https://exceljet.net/functions/abs-function)
. In the example shown the formula in C6 is:

    =ABS(B6)
    

Generic formula
---------------

    =ABS(number)

Explanation 
------------

The ABS function is fully automatic. All you need to do is supply a number and ABS will return the absolute value.

### Convert negative numbers in place

If you only need to convert negative numbers once, you can convert in-place with [Paste Special](https://exceljet.net/shortcuts/display-the-paste-special-dialog-box)
:

1.  Add -1 to a cell and copy to the clipboard
2.  Select the negative numbers you want to convert
3.  Use Paste Special > Values + Multiply

The [video on this page](https://exceljet.net/videos/shortcuts-for-paste-special)
 shows this technique and many other paste special shortcuts.

Related formulas
----------------

[![Excel formula: Count cells that contain negative numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20negative%20numbers.png "Excel formula: Count cells that contain negative numbers")](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)

### [Count cells that contain negative numbers](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)

In this example, the goal is to count the number of cells in a range that contain negative numbers. For convenience, the range B5:B15 is named data . This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both methods are explained below. COUNTIF function The COUNT...

[![Excel formula: Convert negative numbers to zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20negative%20numbers%20to%20zero.png "Excel formula: Convert negative numbers to zero")](https://exceljet.net/formulas/convert-negative-numbers-to-zero)

### [Convert negative numbers to zero](https://exceljet.net/formulas/convert-negative-numbers-to-zero)

In this example, the goal is to convert negative numbers in column B to zero and leave positive numbers unchanged. Essentially, we want to force negative numbers to zero. With the MAX function The MAX function provides an elegant solution: =MAX(B5,0) This formula takes advantage of the fact that...

Related functions
-----------------

[![Excel ABS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20abs%20function.png "Excel ABS function")](https://exceljet.net/functions/abs-function)

### [ABS Function](https://exceljet.net/functions/abs-function)

The Excel ABS function returns the absolute value of a number. ABS converts negative numbers to positive numbers, and positive numbers are unaffected.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain negative numbers](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)
    
*   [Convert negative numbers to zero](https://exceljet.net/formulas/convert-negative-numbers-to-zero)
    

### Functions

*   [ABS Function](https://exceljet.net/functions/abs-function)
    

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