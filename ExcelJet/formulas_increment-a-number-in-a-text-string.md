# Increment a number in a text string - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/increment-a-number-in-a-text-string

---

[Skip to main content](https://exceljet.net/formulas/increment-a-number-in-a-text-string#main-content)

[](https://exceljet.net/formulas/increment-a-number-in-a-text-string#)

*   [Previous](https://exceljet.net/formulas/increment-a-calculation-with-row-or-column)
    
*   [Next](https://exceljet.net/formulas/increment-cell-reference-with-indirect)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Increment a number in a text string
===================================

by Dave Bruns · Updated 2 Nov 2016

Related functions 
------------------

[RIGHT](https://exceljet.net/functions/right-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Increment a number in a text string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/increment%20a%20number%20in%20a%20text%20string.png "Excel formula: Increment a number in a text string")

Summary
-------

This formula looks at one way to increment a number that is embedded in a text string. The purpose of this example to show how multiple functions can be combined to split, manipulate, and rejoin values.

In the example shown, the formula in D5 is:

    ="Item "&TEXT(RIGHT(B5,3)+C5,"000")
    

This formula increments the number in column B by the value in column C, and outputs a string in the original format.

Generic formula
---------------

    ="Item "&TEXT(RIGHT(A1,3)+increment,"000")

Explanation 
------------

At the core, this formula extracts the number, adds the increment, and joins the number to the original text in the right format.

Working from the inside out, this formula first extracts the numeric portion of the string in column B using the RIGHT function:

    RIGHT(B5,3) // returns "001"
    

The result returned is actually text like "001", "003", etc. but when we add the numeric value from C, Excel automatically changes the next to a number and performs the addition:

    RIGHT(B5,3)+C5 // returns 2
    

Next, this numeric result goes into the TEXT function as the value, with a number format of "000". This pads the number with zeros as needed:

    TEXT(2,"000") // returns "002"
    

Finally, this text string is joined to the text "Item " using concatenation:

    ="Item "&TEXT(2,"000")
    

Which returns a final result of "Item 002".

Related formulas
----------------

[![Excel formula: Pad a number with zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20number%20with%20zeros.png "Excel formula: Pad a number with zeros")](https://exceljet.net/formulas/pad-a-number-with-zeros)

### [Pad a number with zeros](https://exceljet.net/formulas/pad-a-number-with-zeros)

In this example, the goal is to pad a number with zeros. To illustrate how Excel functions can be combined, the number of zeros to use is variable and comes from column C. The formula used to solve this problem combines the TEXT function and the REPT function . Fixed number The TEXT function...

Related functions
-----------------

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

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

*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

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