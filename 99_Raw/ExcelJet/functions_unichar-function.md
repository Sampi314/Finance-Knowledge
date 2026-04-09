# Excel UNICHAR function | Exceljet

**Source:** https://exceljet.net/functions/unichar-function

---

[Skip to main content](https://exceljet.net/functions/unichar-function#main-content)

[](https://exceljet.net/functions/unichar-function#)

*   [Previous](https://exceljet.net/functions/trim-function)
    
*   [Next](https://exceljet.net/functions/unicode-function)
    

Excel 2013

[Text](https://exceljet.net/functions#Text)

UNICHAR Function
================

by Dave Bruns · Updated 22 Oct 2025

Related functions 
------------------

[UNICHAR](https://exceljet.net/functions/unichar-function)

[CHAR](https://exceljet.net/functions/char-function)

[UNICODE](https://exceljet.net/functions/unicode-function)

[CODE](https://exceljet.net/functions/code-function)

![Excel UNICHAR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_unichar_function.png "Excel UNICHAR function")

Summary
-------

The Excel UNICHAR function returns the Unicode character at a given code point

Purpose 
--------

Get Unicode character by number

Return value 
-------------

Unicode character

Syntax
------

    =UNICHAR(number)

*   _number_ - Code point for a Unicode character in decimal.

Using the UNICHAR function 
---------------------------

The UNICHAR function returns the Unicode character at a given code point, provided as a number in _decimal format_. To illustrate, the Euro symbol (€) has a code point of 8364 in decimal notation. The following formula will return the Euro character:

    =UNICHAR(8364) // returns euro sign "€"
    

### Unicode numbers

Unicode assigns each character a unique numeric value and name. This numeric value is referred to as a "code point". Code points are typically represented by the "U+" notation followed by hexadecimal numbers. For example, the code point for the capital letter A is U+0041, and the code point for the "😊" emoji is U+1F60A. It is important to understand that the UNICHAR function _does not_ accept Unicode numbers in hexadecimal format, it requires numbers in decimal format. In decimal representation, the code point for "A" is 65, and the code point for the "😊" emoji  is 128522, therefore:

    =UNICHAR(65) // returns "A"
    =UNICHAR(128522) // returns "😊"
    

In Excel, you can use the [HEX2DEC function](https://exceljet.net/functions/hex2dec-function)
 to translate numbers from hexadecimal to decimal if needed.

    =UNICHAR(HEX2DEC("1F642")) // returns "🙂"

### About Unicode

Excel supports [Unicode](https://en.wikipedia.org/wiki/Unicode)
 characters, which are characters that can represent most of the world's writing systems. Unicode is a computing standard that assigns a unique number (code point) to each character, regardless of the font, platform, or program. Because Unicode is a superset of other character sets, it is very large. The first 128 code points in Unicode align exactly with the ASCII characters. In total, Unicode contains over 140,000 characters spanning more than 160 modern and historic scripts, plus thousands of symbols and emoji. 

Unicode can be implemented in different encodings, most commonly UTF-8 and UTF-16. It is estimated that over 90% of websites on the internet use UTF-8.

### Examples

The Unicode character "★" is code point 9733 in decimal notation, therefore:

    =UNICHAR(9733) // returns "★"
    

To display a different character, change the number to match the symbol you want:

    =UNICHAR(10003) // returns "✓"
    =UNICHAR(10007) // returns "✗"
    =UNICHAR(128578) // returns "😊"
    

Here are some more useful Unicode symbols in Excel:

![Useful Unicode symbols in Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/useful_unicode_symbols_in_excel.png "Useful Unicode symbols in Excel")

_Note: As of this writing in May 2023, emojis in Excel Online (i.e. the web app)  appear in color, but emojis in the desktop version of Excel appear in black and white only. See_ [_Emoji Wizard_](https://emojiwizard.net/)
 _for emoji and their corresponding unicode sequence._

### UNICHAR in a formula

The UNICHAR function offers a straightforward way to display a Unicode symbol in a formula. The formula below uses UNICHAR inside the IF function to display a checkmark when a task is complete:

    =IF(C5="complete",UNICHAR(10003),"")

![If function with unichar function to display checkmark](https://exceljet.net/sites/default/files/images/formulas/inline/If_function_with_unichar_function_to_display_checkmark.png "If function with unichar function to display checkmark")

A key advantage of this approach is that it is easy to display a different symbol. For example, to display an "X" instead of a check mark, use 10007:

    =IF(C5="complete",UNICHAR(10007),"")

![If function with unicode x character](https://exceljet.net/sites/default/files/images/formulas/inline/If_function_with_unicode_x_character.png "If function with unicode x character")

[This page](https://exceljet.net/formulas/if-complete-show-checkmark)
 has an overview of ways to insert a checkmark in a formula.

### UNICHAR versus UNICODE

The UNICHAR function translates a given _code_ in decimal number format into a Unicode _character_. To perform the _opposite conversion,_ see the [UNICODE function](https://exceljet.net/functions/unicode-function)
, which translates a Unicode _character_ into a _code_ in decimal number format.

### Notes

*   If _number_ is out-of-range, UNICHAR returns #VALUE!
*   If _number_ is not a recognized number, UNICHAR returns #VALUE!

UNICHAR function examples
-------------------------

[![Excel formula: Encode Unicode sequence into text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_text_from_unicode_sequence_screenshot_cropped.png "Excel formula: Encode Unicode sequence into text")](https://exceljet.net/formulas/encode-unicode-sequence-into-text)

### [Encode Unicode sequence into text](https://exceljet.net/formulas/encode-unicode-sequence-into-text)

In this example, the goal is to convert a space-separated sequence of Unicode code points into a readable text string. We can solve this using several Excel functions working together to split, convert, and reconstruct the text. This is the reverse operation of this formula that converts text into...

[![Excel formula: If complete show checkmark](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_complete_show_checkmark.png "Excel formula: If complete show checkmark")](https://exceljet.net/formulas/if-complete-show-checkmark)

### [If complete show checkmark](https://exceljet.net/formulas/if-complete-show-checkmark)

The goal is to display a checkmark (also called a "tick mark" in British English) when a task is marked complete. The easiest way to do this is with the IF function and the mark you would like to display. The article below explains several options. IF with a plain checkmark The simplest approach,...

Related functions
-----------------

[![Excel UNICHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unichar_function.png "Excel UNICHAR function")](https://exceljet.net/functions/unichar-function)

### [UNICHAR Function](https://exceljet.net/functions/unichar-function)

The Excel UNICHAR function returns the Unicode character at a given code point

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

[![Excel UNICODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unicode_function_0.png "Excel UNICODE function")](https://exceljet.net/functions/unicode-function)

### [UNICODE Function](https://exceljet.net/functions/unicode-function)

The Excel UNICODE function returns a decimal number (code point) corresponding to a Unicode character. Unicode is computing standard for the unified encoding, representation, and handling of text in most of the world's writing systems. ...

[![Excel CODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20code%20function.png "Excel CODE function")](https://exceljet.net/functions/code-function)

### [CODE Function](https://exceljet.net/functions/code-function)

The Excel CODE function returns a numeric code for a given character.  For example, CODE("a") returns the code 97....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If complete show checkmark](https://exceljet.net/formulas/if-complete-show-checkmark)
    
*   [Encode Unicode sequence into text](https://exceljet.net/formulas/encode-unicode-sequence-into-text)
    

### Functions

*   [UNICHAR Function](https://exceljet.net/functions/unichar-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    
*   [UNICODE Function](https://exceljet.net/functions/unicode-function)
    
*   [CODE Function](https://exceljet.net/functions/code-function)
    

### Links

*   [Microsoft UNICHAR function documentation](https://support.office.com/en-us/article/unichar-function-ffeb64f5-f131-44c6-b332-5cd72f0659b8)
    
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