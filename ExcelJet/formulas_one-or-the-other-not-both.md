# One or the other not both - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/one-or-the-other-not-both

---

[Skip to main content](https://exceljet.net/formulas/one-or-the-other-not-both#main-content)

[](https://exceljet.net/formulas/one-or-the-other-not-both#)

*   [Previous](https://exceljet.net/formulas/odometer-gas-mileage-log)
    
*   [Next](https://exceljet.net/formulas/pad-a-number-with-zeros)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

One or the other not both
=========================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[XOR](https://exceljet.net/functions/xor-function)

![Excel formula: One or the other not both](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/one%20or%20the%20other%20not%20both.png "Excel formula: One or the other not both")

Summary
-------

To check two items with exclusive OR (one or the other, but not both), you can use the XOR function. In the example shown, E5 contains the following formula:

    =XOR(C5="x",D5="x")
    

This formula returns TRUE when either coffee or tea has an "x". It returns FALSE if both coffee and tea have an "x", or if neither coffee nor team has an "x".

Generic formula
---------------

    =XOR(criteria1,criteria2)

Explanation 
------------

In this example, the XOR function contains two expressions, one to test for an "x" in column C, and one to test for an "x" in column D.

    C5="x" // TRUE if coffee is "x"
    D5="x" // TRUE if tea is "x"
    

With two logical criteria, XOR has a particular behavior, summarized in the table below:

| Coffee | Tea | Result |
| --- | --- | --- |
| TRUE | FALSE | TRUE |
| FALSE | TRUE | TRUE |
| TRUE | TRUE | FALSE |
| FALSE | FALSE | FALSE |

At each row in column E, XOR evaluates values in columns C and D and returns a TRUE or FALSE result. This behavior is sometimes referred to as "exclusive OR", meaning only one result can be true.

_Note: with more than two criteria, XOR behavior changes, as [explained on the XOR function page](https://exceljet.net/functions/xor-function)
._

Related formulas
----------------

[![Excel formula: Count cells equal to this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20this%20or%20that.png "Excel formula: Count cells equal to this or that")](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

### [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

In this example, the goal is to count cells in the range D5:D15 that contain "red" or "blue". For convenience, the D5:D15 is named color . Counting cells equal to this OR that is more complicated than it first appears because there is no built-in function for counting with OR logic. The COUNTIFS...

[![Excel formula: If cell is x or y and z](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_x_or_y_and_z.png "Excel formula: If cell is x or y and z")](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)

### [If cell is x or y and z](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)

The goal is to identify records where the color is "Red" or "Green" and the quantity is greater than 10. If a row meets all conditions, the formula should return "x". If any condition is not true, the formula should return an empty string (""). This problem can be solved with the IF function...

Related functions
-----------------

[![Excel XOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20xor.png "Excel XOR function")](https://exceljet.net/functions/xor-function)

### [XOR Function](https://exceljet.net/functions/xor-function)

The XOR function performs what is called "exclusive OR". With two logical statements, XOR returns TRUE if either statement is TRUE, but returns FALSE if both statements are TRUE. If neither is TRUE, XOR also returns FALSE.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)
    
*   [If cell is x or y and z](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)
    

### Functions

*   [XOR Function](https://exceljet.net/functions/xor-function)
    

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