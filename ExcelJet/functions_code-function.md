# Excel CODE function | Exceljet

**Source:** https://exceljet.net/functions/code-function

---

[Skip to main content](https://exceljet.net/functions/code-function#main-content)

[](https://exceljet.net/functions/code-function#)

*   [Previous](https://exceljet.net/functions/clean-function)
    
*   [Next](https://exceljet.net/functions/concat-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

CODE Function
=============

by Dave Bruns · Updated 13 Nov 2022

Related functions 
------------------

[CODE](https://exceljet.net/functions/code-function)

[CHAR](https://exceljet.net/functions/char-function)

[UNICODE](https://exceljet.net/functions/unicode-function)

[UNICHAR](https://exceljet.net/functions/unichar-function)

![Excel CODE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20code%20function.png "Excel CODE function")

Summary
-------

The Excel CODE function returns a numeric code for a given character.  For example, CODE("a") returns the code 97.

Purpose 
--------

Get the code for a character

Return value 
-------------

A numeric code representing a character.

Syntax
------

    =CODE(text)

*   _text_ - The text for which you want a numeric code.

Using the CODE function 
------------------------

The CODE function returns a numeric code for a given character. For example, CODE("a") returns the code 97:

    =CODE("a") // returns 97
    

With the character "a" in cell A1, the formula below returns the same result:

    =CODE(A1) // returns 97
    

The CODE function takes a single [argument](https://exceljet.net/glossary/function-argument)
, _text_, which is normally a text value. If text contains more than one character, the CODE function returns a numeric code for the _first_ character:

    =CODE("A") // returns 65
    =CODE("Apple") // returns 65
    

The CODE function will handle numeric input for the numbers 0-9:

    =CODE(1) // returns 49
    

Generally speaking, the number returned by CODE is the code for a character in ASCII decimal notation. The CODE function was designed to operate in an [ASCII](https://exceljet.net/glossary/ascii)
/ANSI world, and only understands how to map characters that correspond to numbers 0-255. For extended character support on modern Unicode systems, see the [UNICODE function](https://exceljet.net/functions/unicode-function)
.

### Reverse CODE

To get a character for a given numeric code, you can use the CHAR function:

    =CHAR(65) // returns "A"
    

CHAR performs the reverse of CODE, taking a numeric code and returning the corresponding character.

CODE function examples
----------------------

[![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")](https://exceljet.net/formulas/abbreviate-names-or-words)

### [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article...

[![Excel formula: Remove unwanted characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20unwanted%20characters.png "Excel formula: Remove unwanted characters")](https://exceljet.net/formulas/remove-unwanted-characters)

### [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)

The SUBSTITUTE function can find and replace text in a cell, wherever it occurs. In this case, we are using SUBSTITUTE to find a character with code number 202, and replace it with an empty string (""), which effectively removes the character completely. How can you figure out which character(s)...

CODE function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20CHAR%20and%20CODE%20functions-thumb.png)](https://exceljet.net/videos/how-to-use-char-and-code-functions)

### [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)

Each character you see displayed in Excel has a number. Excel has two functions that work with these numbers directly: CODE and CHAR (Character). Let's look first at the CODE function . The CODE function accepts one argument, which is the text for which you'd like a numeric code. If I use CODE with...

Related functions
-----------------

[![Excel CODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20code%20function.png "Excel CODE function")](https://exceljet.net/functions/code-function)

### [CODE Function](https://exceljet.net/functions/code-function)

The Excel CODE function returns a numeric code for a given character.  For example, CODE("a") returns the code 97....

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

[![Excel UNICODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unicode_function_0.png "Excel UNICODE function")](https://exceljet.net/functions/unicode-function)

### [UNICODE Function](https://exceljet.net/functions/unicode-function)

The Excel UNICODE function returns a decimal number (code point) corresponding to a Unicode character. Unicode is computing standard for the unified encoding, representation, and handling of text in most of the world's writing systems. ...

[![Excel UNICHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unichar_function.png "Excel UNICHAR function")](https://exceljet.net/functions/unichar-function)

### [UNICHAR Function](https://exceljet.net/functions/unichar-function)

The Excel UNICHAR function returns the Unicode character at a given code point

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)
    
*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    

### Videos

*   [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)
    

### Functions

*   [CODE Function](https://exceljet.net/functions/code-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    
*   [UNICODE Function](https://exceljet.net/functions/unicode-function)
    
*   [UNICHAR Function](https://exceljet.net/functions/unichar-function)
    

### Links

*   [Microsoft CODE function documentation](https://support.office.com/en-us/article/code-function-c32b692b-2ed0-4a04-bdd9-75640144b928)
    

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