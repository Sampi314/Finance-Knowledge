# Excel UNICODE function | Exceljet

**Source:** https://exceljet.net/functions/unicode-function

---

[Skip to main content](https://exceljet.net/functions/unicode-function#main-content)

[](https://exceljet.net/functions/unicode-function#)

*   [Previous](https://exceljet.net/functions/unichar-function)
    
*   [Next](https://exceljet.net/functions/upper-function)
    

Excel 2013

[Text](https://exceljet.net/functions#Text)

UNICODE Function
================

by Dave Bruns · Updated 22 Oct 2025

Related functions 
------------------

[UNICODE](https://exceljet.net/functions/unicode-function)

[UNICHAR](https://exceljet.net/functions/unichar-function)

[CODE](https://exceljet.net/functions/code-function)

[CHAR](https://exceljet.net/functions/char-function)

![Excel UNICODE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_unicode_function_0.png "Excel UNICODE function")

Summary
-------

The Excel UNICODE function returns a decimal number (code point) corresponding to a Unicode character. Unicode is computing standard for the unified encoding, representation, and handling of text in most of the world's writing systems. 

Purpose 
--------

Get number from Unicode character

Return value 
-------------

Unicode code point in decimal notation

Syntax
------

    =UNICODE(text)

*   _text_ - Unicode character to convert to number.

Using the UNICODE function 
---------------------------

The Excel UNICODE function returns a number (code point) corresponding to a Unicode character given as text. The result is a number in decimal notation. For example, the Euro symbol (€) is code point 8364 in decimal notation, so UNICODE returns 8364:

    =UNICODE("€") // returns 8364
    

To get the hexadecimal value, which is usually how unicode code points are expressed, you can use the [DEC2HEX](https://exceljet.net/functions/dec2hex-function)
 function like this:

    =DEC2HEX(UNICODE("€")) // returns 20AC

If text is more than one character, UNICODE returns the number of the _first_ character:

    =UNICODE("a") // returns 97
    =UNICODE("apple") // returns 97
    

Note: the [UNICHAR function](https://exceljet.net/functions/unichar-function)
 performs the opposite conversion, returning the Unicode _character_ at a given code point.

### Unicode numbers

Unicode assigns each character a unique numeric value and name. This numeric value is referred to as a "code point". Code points are typically represented by the "U+" notation followed by hexadecimal numbers. For example, the code point for the capital letter A is U+0041, and the code point for the "😊" emoji is U+1F60A. It is important to understand that the UNICODE function _does not_ return Unicode code points in hexadecimal number format, but rather in decimal number format.

### Examples

In decimal representation, the code point for "A" is 65, and the code point for the "😊" emoji is 128522, therefore:

    =UNICODE("A") // returns 65
    =UNICODE("😊") // returns 128522
    

In Excel, you can use the [DEC2HEX](https://exceljet.net/functions/dec2hex-function)
 function to translate numbers from hexadecimal to decimal if needed.

    =DEC2HEX(UNICODE("😊")) // returns 1F60A

Here are some more useful Unicode symbols in Excel, along with the decimal number code point:

![Useful Unicode symbols in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/useful_unicode_symbols_in_excel.png "Useful Unicode symbols in Excel")

_Note: As of this writing in October 2025, emojis in Excel Online (i.e. the web app)  appear in color, but emojis in the desktop version of Excel appear in black and white only. See_ [_Emoji Wizard_](https://emojiwizard.net/)
 _for a comprehensive list of emoji and their corresponding unicode sequences._

### About Unicode

Excel supports [Unicode](https://en.wikipedia.org/wiki/Unicode)
 characters, which are characters that can represent most of the world's writing systems. Unicode is a computing standard that assigns a unique number (code point) to each character, regardless of the font, platform, or program. Because Unicode is a superset of other character sets, it is very large. The first 128 code points in Unicode align exactly with the ASCII characters. In total, Unicode contains over 140,000 characters spanning more than 160 modern and historic scripts, plus thousands of symbols and emoji.

Unicode can be implemented in different encodings, most commonly UTF-8 and UTF-16. It is estimated that over 90% of websites on the internet use UTF-8.

### UNICODE versus UNICHAR 

The UNICODE function translates a Unicode _character_ into a _code_ in decimal number format. To perform the _opposite conversion,_ see the [UNICHAR function](https://exceljet.net/functions/unichar-function)
, which translates a given _code_ in decimal number format into a Unicode _character_.

    =UNICHAR(HEX2DEC("1F60A")) // returns "😊"

UNICODE function examples
-------------------------

[![Excel formula: Get Unicode Sequence from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_unicode_sequence_of_text_main_0.png "Excel formula: Get Unicode Sequence from text")](https://exceljet.net/formulas/get-unicode-sequence-from-text)

### [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)

In this example, the goal is to convert each character in a text string into its corresponding Unicode code point and display the results as a space-separated sequence. This problem can be solved using several Excel functions working together to extract, convert, and format the Unicode values. The...

Related functions
-----------------

[![Excel UNICODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unicode_function_0.png "Excel UNICODE function")](https://exceljet.net/functions/unicode-function)

### [UNICODE Function](https://exceljet.net/functions/unicode-function)

The Excel UNICODE function returns a decimal number (code point) corresponding to a Unicode character. Unicode is computing standard for the unified encoding, representation, and handling of text in most of the world's writing systems. ...

[![Excel UNICHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unichar_function.png "Excel UNICHAR function")](https://exceljet.net/functions/unichar-function)

### [UNICHAR Function](https://exceljet.net/functions/unichar-function)

The Excel UNICHAR function returns the Unicode character at a given code point

[![Excel CODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20code%20function.png "Excel CODE function")](https://exceljet.net/functions/code-function)

### [CODE Function](https://exceljet.net/functions/code-function)

The Excel CODE function returns a numeric code for a given character.  For example, CODE("a") returns the code 97....

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)
    

### Functions

*   [UNICODE Function](https://exceljet.net/functions/unicode-function)
    
*   [UNICHAR Function](https://exceljet.net/functions/unichar-function)
    
*   [CODE Function](https://exceljet.net/functions/code-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    

### Links

*   [Microsoft UNICODE function documentation](https://support.office.com/en-us/article/unicode-function-adb74aaa-a2a5-4dde-aff6-966e4e81f16f)
    
*   [List of Unicode characters (wikipedia)](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
    

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