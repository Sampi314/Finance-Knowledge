# Excel ROMAN function | Exceljet

**Source:** https://exceljet.net/functions/roman-function

---

[Skip to main content](https://exceljet.net/functions/roman-function#main-content)

[](https://exceljet.net/functions/roman-function#)

*   [Previous](https://exceljet.net/functions/randbetween-function)
    
*   [Next](https://exceljet.net/functions/round-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

ROMAN Function
==============

by Dave Bruns · Updated 18 Sep 2021

Related functions 
------------------

[ARABIC](https://exceljet.net/functions/arabic-function)

![Excel ROMAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20roman%20function.png "Excel ROMAN function")

Summary
-------

The Excel ROMAN function converts a number to a Roman numeral as text. For example, the formula =ROMAN(4) returns IV.

Purpose 
--------

Converts numbers to Roman numerals

Return value 
-------------

A Roman numeral in text

Syntax
------

    =ROMAN(number,[form])

*   _number_ - Number (in Arabic numeral) you want to convert to Roman numeral.
*   _form_ - \[optional\] The type of Roman numeral you want.

Using the ROMAN function 
-------------------------

The ROMAN function converts a number to a Roman numeral. For example:

    =ROMAN(4) // returns "IV"
    =ROMAN(9) // returns "IX"
    =ROMAN(99) // returns "XCIX"
    =ROMAN(100) // returns "C"
    

ROMAN takes two [arguments](https://exceljet.net/glossary/function-argument)
: _number_ and _form_. _Number_ should be a whole number between 1 and 3999. The _form_ argument controls the convention used for Roman numbers. The argument is optional and the default is zero (0), which results in classic non-abbreviated Roman numbers. Other possible values are 1-4, which specify progressively more concise output. For example:

    =ROMAN(1999,0) // returns "MCMXCIX"
    =ROMAN(1999,2) // returns "MXMIX"
    =ROMAN(1999,4) // returns "MIM"
    

See [more form samples below](https://exceljet.net/functions/roman-function#abbreviation)
.

### Roman numbers

The table below lists available Roman numbers with their equivalent Arabic number value.

| Symbol | Value |
| --- | --- |
| I   | 1   |
| V   | 5   |
| X   | 10  |
| L   | 50  |
| C   | 100 |
| D   | 500 |
| M   | 1000 |

The ROMAN function converts Arabic numbers to Roman numbers. Use the [ARABIC function](https://exceljet.net/functions/arabic-function)
 to convert Roman numbers to Arabic numbers.

### Abbreviated syntax

The ROMAN function can output Roman numbers in a more abbreviated syntax, controlled with the _form_ argument. The screen below shows how different values for _form_ affect output.

![ROMAN function form options example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet%20roman%20function%20form%20options.png?itok=Hn9TWv1K "ROMAN function form options example")

### Notes

*   _Number_ should be a positive number between 1 and 3999.
*   _Number_ should be a whole number; decimal values are ignored.
*   If _number_ is negative or out of range, ROMAN returns #VALUE!
*   The ROMAN function performs the opposite conversion as the [ARABIC function](https://exceljet.net/functions/arabic-function)
    .
*   The _form_ argument controls Roman numeral abbreviation. Valid inputs are 0-4.

ROMAN function examples
-----------------------

[![Excel formula: Sum Roman numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20roman%20numbers.png "Excel formula: Sum Roman numbers")](https://exceljet.net/formulas/sum-roman-numbers)

### [Sum Roman numbers](https://exceljet.net/formulas/sum-roman-numbers)

The goal in this example is to sum a range of Roman numbers. The challenge is that Roman numbers appear as text in Excel, not numeric values. If you try to use the SUM function to sum a range of Roman numbers directly, the result is zero (0). The solution is to use the ARABIC function to convert...

Related functions
-----------------

[![Excel ARABIC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_arabic.png "Excel ARABIC function")](https://exceljet.net/functions/arabic-function)

### [ARABIC Function](https://exceljet.net/functions/arabic-function)

The Excel ARABIC function converts a Roman numeral as text to an Arabic numeral. For example, the formula =ARABIC("VII") returns 7.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum Roman numbers](https://exceljet.net/formulas/sum-roman-numbers)
    

### Functions

*   [ARABIC Function](https://exceljet.net/functions/arabic-function)
    

### Links

*   [Microsoft ROMAN function documentation](https://support.office.com/en-us/article/roman-function-d6b0b99e-de46-4704-a518-b45a0f8b56f5)
    

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