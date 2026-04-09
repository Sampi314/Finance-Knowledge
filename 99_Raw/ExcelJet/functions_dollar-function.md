# Excel DOLLAR function | Exceljet

**Source:** https://exceljet.net/functions/dollar-function

---

[Skip to main content](https://exceljet.net/functions/dollar-function#main-content)

[](https://exceljet.net/functions/dollar-function#)

*   [Previous](https://exceljet.net/functions/concatenate-function)
    
*   [Next](https://exceljet.net/functions/exact-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

DOLLAR Function
===============

by Dave Bruns · Updated 26 Jul 2021

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

![Excel DOLLAR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20dollar%20function.png "Excel DOLLAR function")

Summary
-------

The Excel DOLLAR function converts a number to text using the Currency number format. The TEXT function can do the same thing, and is much more versatile.

Purpose 
--------

Convert a number to text in currency format

Return value 
-------------

A number as text in currency format.

Syntax
------

    =DOLLAR(number,decimals)

*   _number_ - The number to convert.
*   _decimals_ - The number of digits to the right of the decimal point. Default is 2.

Using the DOLLAR function 
--------------------------

The DOLLAR function converts a number to text, formatted as currency. The name of the function and the currency symbol used is based on language settings of the computer.

It's important to understand that DOLLAR returns text and not a number, so the result cannot be used in a numeric calculation. If the goal is simply to format a number as Currency, applying a standard [number format](https://exceljet.net/glossary/number-format)
 is a better option. Video: [How to use number formatting](https://exceljet.net/videos/how-to-use-number-formatting-in-excel)
.

The DOLLAR function takes two arguments, _number_ and _decimals_. _Number_ is the number to format, _decimals_ controls how the number is rounded and specifies the number of digits to the right of the decimal point. _Decimals_ is optional and defaults to 2. For example:

    =DOLLAR(169.49) // returns "$169.49"
    =DOLLAR(169.49,2) // returns "$169.49"
    =DOLLAR(169.49,0) // returns "$169"
    

One use of the DOLLAR function is to [concatenate](https://exceljet.net/glossary/concatenation)
 a formatted number to a text string, since number formatting is lost during concatenation. For example, with the number $99.00 in cell A1, formatted as Currency, the following formula does not show Currency:

    ="The price is "&A1 // returns "The price is 99"
    

With the DOLLAR function, formatting can be maintained:

    ="The price is "&DOLLAR(A1) // returns "The price is $99.00"
    

### DOLLAR vs. TEXT

The DOLLAR function is a specialized function to apply Currency formatting only. The [TEXT function](https://exceljet.net/functions/text-function)
 is a generalized function that does the same thing. TEXT can convert numeric values to text in any number format, including currency, date, time, percentage, and so on.

### Notes

*   The DOLLAR function converts a number to text using currency number format: $#,##0.00\_);($#,##0.00).
*   The default for _decimals_ is 2. If _decimals_ is negative, number will be rounded to the left of the decimal point.
*   The name of the function and the currency symbol used is based on language settings of the computer.
*   The [TEXT function](https://exceljet.net/functions/text-function)
     is a more flexible way to achieve the same result.

Related functions
-----------------

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

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Links

*   [Microsoft DOLLAR function documentation](https://support.office.com/en-us/article/dollar-function-a6cd05d9-9740-4ad3-a469-8109d18ff611)
    

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