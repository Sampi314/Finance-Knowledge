# Excel FIXED function | Exceljet

**Source:** https://exceljet.net/functions/fixed-function

---

[Skip to main content](https://exceljet.net/functions/fixed-function#main-content)

[](https://exceljet.net/functions/fixed-function#)

*   [Previous](https://exceljet.net/functions/find-function)
    
*   [Next](https://exceljet.net/functions/left-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

FIXED Function
==============

by Dave Bruns · Updated 24 Jun 2021

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

[DOLLAR](https://exceljet.net/functions/dollar-function)

![Excel FIXED function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20fixed%20function.png "Excel FIXED function")

Summary
-------

The Excel FIXED function converts a number to text with fixed number of decimals, rounding as needed with the given number of decimals. The FIXED function can be useful when concatenating a formatted number text.

Purpose 
--------

Format number as text with fixed decimals

Return value 
-------------

Number formatted as text

Syntax
------

    =FIXED(number,[decimals],[no_commas])

*   _number_ - The number to round and format.
*   _decimals_ - \[optional\] Number of decimals to use. Default is 2.
*   _no\_commas_ - \[optional\] Suppress commas. TRUE = no commas, FALSE = commas. Default is FALSE.

Using the FIXED function 
-------------------------

The FIXED function converts a number to text, rounding to a given number of decimals. Like the Number format available on the home tab of the ribbon, the FIXED function will round the number as needed using the given number of decimal places. The main difference between applying a number format and using FIXED is that the FIXED function converts the number to text, whereas a [number format](https://exceljet.net/glossary/number-format)
 just changes the way a number is displayed.

The FIXED function takes three [arguments](https://exceljet.net/glossary/function-argument)
, _number_, _decimals_, and _no\_commas_. _Number_ is the number to convert. _Decimals_ is the number of digits to which _number_ will be rounded on the right of the decimal point. If _decimals_ is negative, _number_ will be rounded to the left of the decimal point. _Decimals_ is optional and defaults to 2.

The _no\_commas_ argument is a Boolean that controls whether commas will be added to the result. _No\_commas_ is optional and defaults to FALSE. To _prevent_ commas, set _no\_commas_ to TRUE.

_Note: the FIXED function returns text and not a number, so the result cannot be used in a numeric calculation. If the goal is to format a number and retain its numeric property, applying a standard [number format](https://exceljet.net/glossary/number-format)
 is a better option. Video: [How to use number formatting](https://exceljet.net/videos/how-to-use-number-formatting-in-excel)
._

### Examples

In the example shown above, the formula in E5, copied down, is:

    =FIXED(B5,C5,D5)
    

At each new row, FIXED returns a result based on the number in column B, the decimals in column C, and comma setting in column D.

Number is the only required argument. By default, FIXED will round to 2 decimal places and insert commas for thousands:

    =FIXED(1000) // returns "1,000.00"
    =FIXED(1000,0) // returns "1,000"
    =FIXED(1000,0,FALSE) // returns "1000"
    

The FIXED function can be useful when you want to [concatenate](https://exceljet.net/glossary/concatenation)
 a number with other text. The example below shows how the output from the [PI function](https://exceljet.net/functions/pi-function)
 can be trimmed by FIXED:

    ="PI is about "&PI() // returns "PI is about 3.14159265358979"
    ="PI is about "&FIXED(PI()) // returns "PI is about 3.14"
    

### FIXED vs. TEXT

The FIXED function is a specialized function to apply Number formatting only. The [TEXT function](https://exceljet.net/functions/text-function)
 is a generalized function that does the same thing in a more flexible way. TEXT can convert numeric values to [many different number formats](https://exceljet.net/articles/custom-number-formats)
, including currency, date, time, percentage, and so on.

### Notes

*   The output from FIXED is text. To simply format a number, apply a [number format](https://exceljet.net/glossary/number-format)
     instead.
*   The FIXED function converts a number to text using a [number format](https://exceljet.net/articles/custom-number-formats)
     like: 0.00 or #,##0
*   The default for _decimals_ is 2. If _decimals_ is negative, _number_ will be rounded to the left of the decimal point.
*   The [TEXT function](https://exceljet.net/functions/text-function)
     is a more flexible way to achieve the same result.

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel DOLLAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20dollar%20function.png "Excel DOLLAR function")](https://exceljet.net/functions/dollar-function)

### [DOLLAR Function](https://exceljet.net/functions/dollar-function)

The Excel DOLLAR function converts a number to text using the Currency number format. The TEXT function can do the same thing, and is much more versatile.

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
    
*   [DOLLAR Function](https://exceljet.net/functions/dollar-function)
    

### Articles

*   [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
    

### Links

*   [Microsoft FIXED function documentation](https://support.office.com/en-us/article/fixed-function-ffd5723c-324c-45e9-8b96-e41be2a8274a)
    

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