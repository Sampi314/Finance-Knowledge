# Encode Unicode sequence into text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/encode-unicode-sequence-into-text

---

[Skip to main content](https://exceljet.net/formulas/encode-unicode-sequence-into-text#main-content)

[](https://exceljet.net/formulas/encode-unicode-sequence-into-text#)

*   [Previous](https://exceljet.net/formulas/double-quotes-inside-a-formula)
    
*   [Next](https://exceljet.net/formulas/extract-last-two-words-from-cell)
    

[Text](https://exceljet.net/formulas#Text)

Encode Unicode sequence into text
=================================

by Kurt Bruns · Updated 10 Nov 2025

Related functions 
------------------

[UNICHAR](https://exceljet.net/functions/unichar-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[HEX2DEC](https://exceljet.net/functions/hex2dec-function)

![Excel formula: Encode Unicode sequence into text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/exceljet_get_text_from_unicode_sequence_screenshot_cropped.png "Excel formula: Encode Unicode sequence into text")

Summary
-------

To encode a Unicode sequence into a readable string, you can use the [UNICHAR](https://exceljet.net/functions/unichar-function)
 function with [HEX2DEC](https://exceljet.net/functions/hex2dec-function)
, [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
, and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 functions. This is the reverse operation of the [this formula](https://exceljet.net/formulas/get-unicode-sequence-from-text)
 which converts text into Unicode sequences.

For example, the Unicode sequence "0061 0070 0070 006C 0065" represents the text "apple". Using the formula, we can encode the Unicode sequence into a readable string:

    =TEXTJOIN("",,UNICHAR(HEX2DEC(TEXTSPLIT("0061 0070 0070 006C 0065"," ")))) // returns "apple"
    

Generic formula
---------------

    =TEXTJOIN("",,UNICHAR(HEX2DEC(TEXTSPLIT(str," "))))

Explanation 
------------

In this example, the goal is to convert a space-separated sequence of Unicode code points into a readable text string. We can solve this using several Excel functions working together to split, convert, and reconstruct the text. This is the reverse operation of [this formula](https://exceljet.net/formulas/get-unicode-sequence-from-text)
 that converts text into Unicode sequence.

### The formula explained

The formula processes the Unicode sequence through several steps:

    =TEXTJOIN("",,UNICHAR(HEX2DEC(TEXTSPLIT("0061 0070 0070 006C 0065"," "))))
    

Working from the inside out:

1.  **TEXTSPLIT("0061 0070 0070 006C 0065"," ")** - Splits the sequence string by spaces {"0061";"0070";"0070";"006C";"0065"}
2.  **HEX2DEC(TEXTSPLIT(...))** - Converts each hexadecimal value to decimal {97;112;112;108;101}
3.  **UNICHAR(HEX2DEC(...))** - Converts each decimal number to its corresponding character {"a";"p";"p";"l";"e"}
4.  **TEXTJOIN("",, ...)** - Joins all characters together without separators

The advantage of this formula over the standard [UNICHAR](https://exceljet.net/functions/unichar-function)
 function is that it processes an entire Unicode sequence and returns the complete reconstructed string. This makes it perfect for converting Unicode sequences back to their original text form.

For example, the standard UNICHAR function only converts a single Unicode code point:

    =UNICHAR(97) // returns "a"
    

While this formula processes the complete Unicode sequence:

    =TEXTJOIN("",,UNICHAR(HEX2DEC(TEXTSPLIT("0061 0070 0070 006C 0065"," ")))) // returns "apple"
    

This is especially useful for more complicated Unicode sequences like those that contain special characters or combining characters.

### Example #1 - Basic examples

Here are some examples of Unicode sequences and their corresponding text strings:

![Unicode encoding examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/exceljet_get_text_from_unicode_sequence_screenshot_cropped.png "Unicode encoding examples")

> _Note: As of this writing in October 2025, emojis in Excel Online (i.e. the web app) appear in color, but emojis in the desktop version of Excel appear in black and white only._

### Example #2 - Text with special characters

A practical use-case of this formula is to encode a Unicode sequence that contains special characters back into its corresponding text string.

For example, consider the Unicode sequence "0041 0020 003D 0020 03C0 0072 00B2" that represents the mathematical formula "A = πr²". Using the formula, we can encode the Unicode sequence to text:

    =TEXTJOIN("",,UNICHAR(HEX2DEC(TEXTSPLIT("0041 0020 003D 0020 03C0 0072 00B2"," ")))) // returns "A = πr²"
    

Breaking down the Unicode sequence the formula processes:

*   0041 - "A" (Latin capital letter A)
*   0020 - " " (space)
*   003D - "=" (equals sign)
*   0020 - " " (space)
*   **03C0 - "π" (Greek small letter pi - U+03C0)**
*   0072 - "r" (Latin small letter r)
*   **00B2 - "²" (superscript two - U+00B2)**

This is particularly useful when you have a Unicode sequence from an external source and need to convert it back to readable text.

### Example #3 - Text with combining characters

The formula can also handle Unicode sequences that contain combining characters, such as emojis with variation selectors.

For example, the Unicode sequence "2764 FE0F" represents the heart emoji "❤️". It's a combination of the basic heart symbol "❤" (U+2764) plus a variation selector (U+FE0F) that tells the system to display it as an emoji rather than a text symbol.

    =TEXTJOIN("",,UNICHAR(HEX2DEC(TEXTSPLIT("2764 FE0F"," ")))) // returns "❤️"
    

For an even more complex example, consider the mending heart emoji "❤️‍🩹". It's a combination of the basic heart symbol "❤" (U+2764) plus a variation selector (U+FE0F) plus a zero-width joiner (U+200D) plus the mending heart symbol "🩹" (U+1FA79). Putting this all together, the Unicode sequence "2764 FE0F 200D 1FA79" represents the mending heart emoji "❤️‍🩹".

    =TEXTJOIN("",,UNICHAR(HEX2DEC(TEXTSPLIT("2764 FE0F 200D 1FA79"," ")))) // returns "❤️‍🩹"
    

For a list of all emojis and their corresponding Unicode sequences, see the [Emoji Wizard](https://emojiwizard.net/)
.

Related formulas
----------------

[![Excel formula: Get Unicode Sequence from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_unicode_sequence_of_text_main_0.png "Excel formula: Get Unicode Sequence from text")](https://exceljet.net/formulas/get-unicode-sequence-from-text)

### [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)

In this example, the goal is to convert each character in a text string into its corresponding Unicode code point and display the results as a space-separated sequence. This problem can be solved using several Excel functions working together to extract, convert, and format the Unicode values. The...

Related functions
-----------------

[![Excel UNICHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unichar_function.png "Excel UNICHAR function")](https://exceljet.net/functions/unichar-function)

### [UNICHAR Function](https://exceljet.net/functions/unichar-function)

The Excel UNICHAR function returns the Unicode character at a given code point

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel HEX2DEC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_hex2dec.png "Excel HEX2DEC function")](https://exceljet.net/functions/hex2dec-function)

### [HEX2DEC Function](https://exceljet.net/functions/hex2dec-function)

The Excel HEX2DEC function converts a hexadecimal number to its decimal equivalent.

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

*   [UNICHAR Function](https://exceljet.net/functions/unichar-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [HEX2DEC Function](https://exceljet.net/functions/hex2dec-function)
    

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