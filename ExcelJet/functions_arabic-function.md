# Excel ARABIC function | Exceljet

**Source:** https://exceljet.net/functions/arabic-function

---

[Skip to main content](https://exceljet.net/functions/arabic-function#main-content)

[](https://exceljet.net/functions/arabic-function#)

*   [Previous](https://exceljet.net/functions/aggregate-function)
    
*   [Next](https://exceljet.net/functions/base-function)
    

Excel 2013

[Math](https://exceljet.net/functions#Math)

ARABIC Function
===============

by Dave Bruns · Updated 4 Aug 2021

Related functions 
------------------

[ROMAN](https://exceljet.net/functions/roman-function)

![Excel ARABIC function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_arabic.png "Excel ARABIC function")

Summary
-------

The Excel ARABIC function converts a Roman numeral as text to an Arabic numeral. For example, the formula =ARABIC("VII") returns 7.

Purpose 
--------

Converts a Roman numerals to an Arabic numerals

Return value 
-------------

A number (in Arabic numeral)

Syntax
------

    =ARABIC(roman_text)

*   _roman\_text_ - The Roman numeral in text that you want to convert.

Using the ARABIC function 
--------------------------

The ARABIC function converts a Roman numeral to a number in Arabic numeral form. The result from ARABIC is a numeric value.

ARABIC takes just one argument, _roman\_text_, which should be a Roman number provided as a [text string](https://exceljet.net/glossary/text-value)
. For example, the formula below converts "VII" to the number 7:

     =ARABIC("VII") // returns 7
    

### Other examples

     =ARABIC("L") // returns 50
     =ARABIC("C") // returns 100
     =ARABIC("M") // returns 1000
     =ARABIC("MM")+1 // returns 2001
    

The [ROMAN function](https://exceljet.net/functions/roman-function)
 performs the opposite conversion:

    =ROMAN(2021) // returns "MMXXI"
    =ARABIC("MMXXI") // returns 2021
    

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

### Notes

*   The maximum length of _roman\_text_ is 255 characters.
*   The ARABIC function performs the opposite conversion as the [ROMAN function](https://exceljet.net/functions/roman-function)
    .
*   If _roman\_text_ is not recognized as a Roman number, ARABIC returns #VALUE!
*   ARABIC can process Roman numbers in upper or lower case.

ARABIC function examples
------------------------

[![Excel formula: Sum Roman numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20roman%20numbers.png "Excel formula: Sum Roman numbers")](https://exceljet.net/formulas/sum-roman-numbers)

### [Sum Roman numbers](https://exceljet.net/formulas/sum-roman-numbers)

The goal in this example is to sum a range of Roman numbers. The challenge is that Roman numbers appear as text in Excel, not numeric values. If you try to use the SUM function to sum a range of Roman numbers directly, the result is zero (0). The solution is to use the ARABIC function to convert...

Related functions
-----------------

[![Excel ROMAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roman%20function.png "Excel ROMAN function")](https://exceljet.net/functions/roman-function)

### [ROMAN Function](https://exceljet.net/functions/roman-function)

The Excel ROMAN function converts a number to a Roman numeral as text. For example, the formula =ROMAN(4) returns IV.

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

*   [ROMAN Function](https://exceljet.net/functions/roman-function)
    

### Links

*   [Microsoft ARABIC function documentation](https://support.office.com/en-us/article/arabic-function-9a8da418-c17b-4ef9-a657-9370a30a674f)
    

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