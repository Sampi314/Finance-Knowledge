# Convert negative numbers to zero - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/convert-negative-numbers-to-zero

---

[Skip to main content](https://exceljet.net/formulas/convert-negative-numbers-to-zero#main-content)

[](https://exceljet.net/formulas/convert-negative-numbers-to-zero#)

*   [Previous](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)
    
*   [Next](https://exceljet.net/formulas/convert-numbers-to-1-or-0)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Convert negative numbers to zero
================================

by Dave Bruns · Updated 4 Dec 2021

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

![Excel formula: Convert negative numbers to zero](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/convert%20negative%20numbers%20to%20zero.png "Excel formula: Convert negative numbers to zero")

Summary
-------

To convert negative numbers to zero without affecting positive numbers, you can use a formula based on the [MAX function](https://exceljet.net/functions/max-function)
. In the example shown, the formula in D5, copied down, is:

    =MAX(B5,0)
    

If the number in column B is negative, MAX returns zero. Otherwise, MAX returns the original number.

Generic formula
---------------

    =MAX(A1,0)

Explanation 
------------

In this example, the goal is to convert negative numbers in column B to zero and leave positive numbers unchanged. Essentially, we want to force negative numbers to zero.

### With the MAX function

The [MAX function](https://exceljet.net/functions/max-function)
 provides an elegant solution:

    =MAX(B5,0)
    

This formula takes advantage of the fact that the MAX function works fine with small sets of data — even two values. If the value in B5 is a positive number, MAX will return the number as-is, since positive numbers are always greater than zero. However, if the number is B5 is negative, MAX will return zero, since 0 is greater than any negative number.

### With the IF function

This problem can also be solved with the [IF function](https://exceljet.net/videos/the-if-function)
 like this:

    =IF(B5<0,0,B5)
    

This formula returns exactly the same result. If B5 is less than zero, IF returns zero. Otherwise, IF returns the original number. Both formulas work fine. The MAX formula above is just an elegant way to replace the slightly more complex IF formula. However, if you need to customize the results returned after a [logical test](https://exceljet.net/glossary/logical-test)
, the IF function is more flexible.

Related formulas
----------------

[![Excel formula: Change negative numbers to positive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/change%20negative%20numbers%20to%20positive.png "Excel formula: Change negative numbers to positive")](https://exceljet.net/formulas/change-negative-numbers-to-positive)

### [Change negative numbers to positive](https://exceljet.net/formulas/change-negative-numbers-to-positive)

The ABS function is fully automatic. All you need to do is supply a number and ABS will return the absolute value. Convert negative numbers in place If you only need to convert negative numbers once, you can convert in-place with Paste Special : Add -1 to a cell and copy to the clipboard Select the...

[![Excel formula: Count cells that contain negative numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20negative%20numbers.png "Excel formula: Count cells that contain negative numbers")](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)

### [Count cells that contain negative numbers](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)

In this example, the goal is to count the number of cells in a range that contain negative numbers. For convenience, the range B5:B15 is named data . This problem can be solved with the COUNTIF function or the SUMPRODUCT function. Both methods are explained below. COUNTIF function The COUNT...

[![Excel formula: Cap percentage at specific amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20specific%20amount.png "Excel formula: Cap percentage at specific amount")](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

### [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

This formula uses the MIN function to make a decision that might otherwise be handled with the IF function . Although MIN is usually used to return the minimum value in a data set with many numbers, it also works fine for the "lesser of the two" situations. Inside MIN, the value in C6 is multiplied...

[![Excel formula: Convert numbers to 1 or 0](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20numbers%20to%201%20or%200.png "Excel formula: Convert numbers to 1 or 0")](https://exceljet.net/formulas/convert-numbers-to-1-or-0)

### [Convert numbers to 1 or 0](https://exceljet.net/formulas/convert-numbers-to-1-or-0)

In this example, the goal is to convert the numbers in column B to either 1 or 0, depending on whether the number is greater than zero or not. If the number in column B is greater than zero, the result should be 1. If the number in column B is less than or equal to zero, the result should be zero...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Change negative numbers to positive](https://exceljet.net/formulas/change-negative-numbers-to-positive)
    
*   [Count cells that contain negative numbers](https://exceljet.net/formulas/count-cells-that-contain-negative-numbers)
    
*   [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    
*   [Convert numbers to 1 or 0](https://exceljet.net/formulas/convert-numbers-to-1-or-0)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    

### Articles

*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

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