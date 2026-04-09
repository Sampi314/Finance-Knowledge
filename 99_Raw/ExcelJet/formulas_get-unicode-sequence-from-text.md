# Get Unicode Sequence from text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-unicode-sequence-from-text

---

[Skip to main content](https://exceljet.net/formulas/get-unicode-sequence-from-text#main-content)

[](https://exceljet.net/formulas/get-unicode-sequence-from-text#)

*   [Previous](https://exceljet.net/formulas/get-last-word)
    
*   [Next](https://exceljet.net/formulas/join-cells-with-comma)
    

[Text](https://exceljet.net/formulas#Text)

Get Unicode Sequence from text
==============================

by Kurt Bruns · Updated 24 Oct 2025

Related functions 
------------------

[UNICODE](https://exceljet.net/functions/unicode-function)

[REGEXEXTRACT](https://exceljet.net/functions/regexextract-function)

[BASE](https://exceljet.net/functions/base-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

![Excel formula: Get Unicode Sequence from text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/exceljet_get_unicode_sequence_of_text_main_0.png "Excel formula: Get Unicode Sequence from text")

Summary
-------

To decode a string into its Unicode sequence, you can use the [UNICODE](https://exceljet.net/functions/unicode-function)
 function combined with the [REGEXEXTRACT](https://exceljet.net/functions/regexextract-function)
, [BASE](https://exceljet.net/functions/base-function)
, and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 functions. For example, to convert the string "apple" into its Unicode sequence, you can use the following formula:

    =TEXTJOIN(" ",,BASE(UNICODE(REGEXEXTRACT("apple",".",1)),16,4))
    

This will return the Unicode sequence "0061 0070 0070 006C 0065", which represents the Unicode code points for each character in "apple".

Generic formula
---------------

    =TEXTJOIN(" ",,BASE(UNICODE(REGEXEXTRACT(str,".",1)),16,4))
    

Explanation 
------------

In this example, the goal is to convert each character in a text string into its corresponding Unicode code point and display the results as a space-separated sequence. This problem can be solved using several Excel functions working together to extract, convert, and format the Unicode values.

### The formula explained

The formula processes the input string through several steps:

    =TEXTJOIN(" ",,BASE(UNICODE(REGEXEXTRACT(B6,".",1)),16,4))
    

Working from the inside out:

1.  REGEXEXTRACT(B6,".",1) - Extracts each character individually {"a";"p";"p";"l";"e"}
2.  UNICODE(REGEXEXTRACT(...)) - Converts each character to its Unicode code point as decimal values {97;112;112;108;101}
3.  BASE(UNICODE(...),16,4) - Converts decimal numbers to hexadecimal (hex) with 4-digit padding {0061;0070;0070;006C;0065}
4.  TEXTJOIN(" ",, ...) - Joins all values with spaces as separators

The advantage of this formula over the standard [UNICODE](https://exceljet.net/functions/unicode-function)
 function is that it processes the entire string and returns the complete Unicode sequence for all characters. This makes it better for analyzing and understanding how entire text strings are represented internally.

For example, the standard UNICODE function returns the code point for only the first character of a string.

    =BASE(UNICODE("apple"),16,4) // returns 0061
    

While this formula returns the complete Unicode sequence for all characters:

    =TEXTJOIN(" ",,BASE(UNICODE(REGEXEXTRACT("apple",".",1)),16,4)) // returns "0061 0070 0070 006C 0065"
    

### Example #1 - Basic examples

Here are some examples of text strings and their corresponding Unicode sequences:

![Basic examples of getting Unicode sequences from text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/exceljet_unicode_sequences_basic_examples_screenshot_cropped_0.png "Basic examples of getting Unicode sequences from text")

> Note: As of this writing in October 2025, emojis in Excel Online (i.e. the web app) appear in color, but emojis in the desktop version of Excel appear in black and white only.

### Example #2 - Text with special characters

A practical use-case of this formula is to decode a string that contains special characters into its corresponding Unicode sequence.

For example, consider the mathematical formula "A = πr²" that describes the area of a circle. This string contains Unicode characters that are harder to type on the keyboard. Using the formula, we can decode the Unicode sequence:

    =TEXTJOIN(" ",,BASE(UNICODE(REGEXEXTRACT("A = πr²",".",1)),16,4)) // returns "0041 0020 003D 0020 03C0 0072 00B2"
    

Breaking down the Unicode sequence the formula returns:

*   0041 - "A" (Latin capital letter A)
*   0020 - " " (space)
*   003D - "=" (equals sign)
*   0020 - " " (space)
*   **03C0 - "π" (Greek small letter pi - U+03C0)**
*   0072 - "r" (Latin small letter r)
*   **00B2 - "²" (superscript two - U+00B2)**

There are two characters of interest: "π" (Greek small letter pi - U+03C0) and "²" (superscript two - U+00B2). If you didn't know what these characters are and wanted to find out more about them, you can use the Unicode value to search for them online. This is also useful to know for going the other way and encoding a string into its Unicode sequence using the [UNICHAR](https://exceljet.net/functions/unichar-function)
 function or [this formula](https://exceljet.net/formulas/encode-unicode-sequence-into-text)
 which is the reverse of this formula.

### Example #3 - Text with combining characters

The [Unicode standard](https://en.wikipedia.org/wiki/Unicode)
 defines a wide range of characters for expressing the written forms of many languages around the world in addition to emojis, mathematical symbols, and other special characters. Sometimes, this text can contain combining characters that modify how other characters are displayed but don't appear as separate visual elements.

For example, the heart emoji "❤️" is actually a combination of the basic heart symbol "❤" (U+2764) plus a variation selector (U+FE0F) that tells the system to display it as an emoji rather than a text symbol.

    =TEXTJOIN(" ",,BASE(UNICODE(REGEXEXTRACT("❤️",".",1)),16,4)) // returns "2764 FE0F"
    

This is why you see two code points for what appears to be a single character. You can always do a sanity check by checking the length of the text string too.

    =LEN("❤️") // returns 2
    

Now let's look at a more complex example. The mending heart emoji "❤️‍🩹" is a sequence of four Unicode code points:

    =TEXTJOIN(" ",,BASE(UNICODE(REGEXEXTRACT("❤️‍🩹",".",1)),16,4)) // returns "2764 FE0F 200D 1FA79"
    

This is because the mending heart emoji is a sequence of two Unicode code points: "❤️" and "‍🩹". The "❤️" is the heart emoji and the "‍🩹" is the mending heart emoji. These two emojis are combined into a single emoji by the "zero-width joiner" character (U+200D).

Related formulas
----------------

[![Excel formula: Encode Unicode sequence into text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_text_from_unicode_sequence_screenshot_cropped.png "Excel formula: Encode Unicode sequence into text")](https://exceljet.net/formulas/encode-unicode-sequence-into-text)

### [Encode Unicode sequence into text](https://exceljet.net/formulas/encode-unicode-sequence-into-text)

In this example, the goal is to convert a space-separated sequence of Unicode code points into a readable text string. We can solve this using several Excel functions working together to split, convert, and reconstruct the text. This is the reverse operation of this formula that converts text into...

Related functions
-----------------

[![Excel UNICODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unicode_function_0.png "Excel UNICODE function")](https://exceljet.net/functions/unicode-function)

### [UNICODE Function](https://exceljet.net/functions/unicode-function)

The Excel UNICODE function returns a decimal number (code point) corresponding to a Unicode character. Unicode is computing standard for the unified encoding, representation, and handling of text in most of the world's writing systems. ...

[![Excel REGEXEXTRACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexextract_function.png "Excel REGEXEXTRACT function")](https://exceljet.net/functions/regexextract-function)

### [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)

The Excel REGEXEXTRACT function extracts matching text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXEXTRACT will return the first match, but...

[![Excel BASE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20base%20function.png "Excel BASE function")](https://exceljet.net/functions/base-function)

### [BASE Function](https://exceljet.net/functions/base-function)

The Excel BASE function converts a number to the text representation of the same number in a given base, where base is provided as the radix argument.

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Encode Unicode sequence into text](https://exceljet.net/formulas/encode-unicode-sequence-into-text)
    

### Functions

*   [UNICODE Function](https://exceljet.net/functions/unicode-function)
    
*   [REGEXEXTRACT Function](https://exceljet.net/functions/regexextract-function)
    
*   [BASE Function](https://exceljet.net/functions/base-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    

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