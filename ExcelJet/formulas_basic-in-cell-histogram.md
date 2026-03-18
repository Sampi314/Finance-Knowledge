# Basic in cell histogram - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-in-cell-histogram

---

[Skip to main content](https://exceljet.net/formulas/basic-in-cell-histogram#main-content)

[](https://exceljet.net/formulas/basic-in-cell-histogram#)

*   [Previous](https://exceljet.net/formulas/basic-error-trapping-example)
    
*   [Next](https://exceljet.net/formulas/basic-numeric-sort-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Basic in cell histogram
=======================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[REPT](https://exceljet.net/functions/rept-function)

[CHAR](https://exceljet.net/functions/char-function)

![Excel formula: Basic in cell histogram](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20in%20cell%20histogram.png "Excel formula: Basic in cell histogram")

Summary
-------

To create a simple in-cell histogram, you can use a formula based on the REPT function. This can be handy when you have straightforward data, and want to avoid the complexity of a separate chart.

    =REPT(CHAR(110),C11/100)
    

Generic formula
---------------

    =REPT(barchar,value/100)

Explanation 
------------

The REPT function simply repeats values. For example, this formula outputs 10 asterisks:

    =REPT("*",10) // outputs **********
    

You can use REPT to repeat any character(s) you like. In this example, we use the CHAR function to output a character with a code of 110. This character, when formatted with the Wingdings font, will output a solid square.

    CHAR(110) // square in Wingdings
    

To calculate the "number of times" for REPT, we scale values in column C by dividing each value by 100.

    C11/100 // scale values down
    

This has the effect of outputting one full square per 100 dollars of sales. Increase or decrease the divisor to suit the data and available space.

### Conditional formatting option

You can also use the "data bars" feature in conditional formatting to display an in cell bar.

Related formulas
----------------

[![Excel formula: Pad a number with zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20number%20with%20zeros.png "Excel formula: Pad a number with zeros")](https://exceljet.net/formulas/pad-a-number-with-zeros)

### [Pad a number with zeros](https://exceljet.net/formulas/pad-a-number-with-zeros)

In this example, the goal is to pad a number with zeros. To illustrate how Excel functions can be combined, the number of zeros to use is variable and comes from column C. The formula used to solve this problem combines the TEXT function and the REPT function . Fixed number The TEXT function...

Related functions
-----------------

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20CHAR%20and%20CODE%20functions-thumb.png)](https://exceljet.net/videos/how-to-use-char-and-code-functions)

### [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)

Each character you see displayed in Excel has a number. Excel has two functions that work with these numbers directly: CODE and CHAR (Character). Let's look first at the CODE function . The CODE function accepts one argument, which is the text for which you'd like a numeric code. If I use CODE with...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Pad a number with zeros](https://exceljet.net/formulas/pad-a-number-with-zeros)
    

### Functions

*   [REPT Function](https://exceljet.net/functions/rept-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    

### Videos

*   [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)
    

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