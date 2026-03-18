# Excel CHAR function | Exceljet

**Source:** https://exceljet.net/functions/char-function

---

[Skip to main content](https://exceljet.net/functions/char-function#main-content)

[](https://exceljet.net/functions/char-function#)

*   [Previous](https://exceljet.net/functions/vlookup-function)
    
*   [Next](https://exceljet.net/functions/clean-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

CHAR Function
=============

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[CHAR](https://exceljet.net/functions/char-function)

[UNICHAR](https://exceljet.net/functions/unichar-function)

[CODE](https://exceljet.net/functions/code-function)

[UNICODE](https://exceljet.net/functions/unicode-function)

![Excel CHAR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")

Summary
-------

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

Purpose 
--------

Get a character from a number

Return value 
-------------

A single character specified by a number.

Syntax
------

    =CHAR(number)

*   _number_ - A number between 1 and 255.

Using the CHAR function 
------------------------

The CHAR function returns a character when given a valid character code. Use the CHAR to translate ASCII code page numbers into actual characters. For example:

    =CHAR(65) // returns "A"
    =CHAR(97) // returns "a"
    

the CHAR function takes just one [argument](https://exceljet.net/glossary/function-argument)
, _number_, which must be an integer between 0-255. The result from CHAR is a [text value](https://exceljet.net/glossary/text-value)
.

The CHAR function was designed to operate in an [ASCII](https://exceljet.net/glossary/ascii)
/ANSI world and only understands numbers 0-255. For extended character support on modern Unicode systems, see the [UNICHAR function](https://exceljet.net/functions/unichar-function)
.

CHAR can be useful when you want to specify characters in formulas or functions that are awkward or impossible to type directly. For example, you can use CHAR(10) to add a line break in a formula like this:

    ="line 1"&CHAR(10)&"Line 2" // add line break
    

_Notes: [Text wrap](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)
 must be enabled to see the line break take effect. Older versions of Excel on the Mac use character 13 for a line break._

### Reverse CHAR

To get the numeric code for a character, you can use the [CODE function](https://exceljet.net/functions/code-function)
:

    =CODE("A") // returns 65
    

CODE performs the reverse of CHAR, taking a character as text and returning a number.

### ASCII and ANSI

The numbers returned by the CHAR function come from ASCII. ASCII stands for "American Standard Code for Information Interchange" and is a 7-bit character set that contains characters from 0 to 127.

The original [ASCII specification](https://en.wikipedia.org/wiki/ASCII)
 encodes 128 characters into numbers. These include the numbers 0 to 9, lowercase a-z, uppercase A-Z, and punctuation. The first 32 characters are non-printing "control codes", most of which are no longer used, with the exception of the carriage return (13), line feed (10), and tab (9).

ANSI (American National Standards Institute) is a generic term for 8-bit character sets, the default in Windows 95 and Windows NT. ANSI includes the same ASCII codes 0-127, and adds an additional 128 characters (128-255) to handle special characters which can change based on the language being represented.

### Notes

*   If _number_ is out of range, CHAR returns #VALUE!
*   If _number_ is not numeric, CHAR returns #VALUE!

CHAR function examples
----------------------

[![Excel formula: If complete show checkmark](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_complete_show_checkmark.png "Excel formula: If complete show checkmark")](https://exceljet.net/formulas/if-complete-show-checkmark)

### [If complete show checkmark](https://exceljet.net/formulas/if-complete-show-checkmark)

The goal is to display a checkmark (also called a "tick mark" in British English) when a task is marked complete. The easiest way to do this is with the IF function and the mark you would like to display. The article below explains several options. IF with a plain checkmark The simplest approach,...

[![Excel formula: Basic in cell histogram](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20in%20cell%20histogram.png "Excel formula: Basic in cell histogram")](https://exceljet.net/formulas/basic-in-cell-histogram)

### [Basic in cell histogram](https://exceljet.net/formulas/basic-in-cell-histogram)

The REPT function simply repeats values. For example, this formula outputs 10 asterisks: =REPT("\*",10) // outputs \*\*\*\*\*\*\*\*\*\* You can use REPT to repeat any character(s) you like. In this example, we use the CHAR function to output a character with a code of 110. This character, when formatted with...

[![Excel formula: Add line break based on OS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20line%20break%20based%20on%20OS.png "Excel formula: Add line break based on OS")](https://exceljet.net/formulas/add-line-break-based-on-os)

### [Add line break based on OS](https://exceljet.net/formulas/add-line-break-based-on-os)

In older versions of Excel (before Excel 2016?), the character used for line breaks is different depending on whether Excel is running on a Mac or Windows computer: On Windows Excel, the line break character is ASCII 10. In older versions of Excel on a Mac, the line break character is ASCII 13...

[![Excel formula: Add a line break with a formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_a_line_break_with_a_formula.png "Excel formula: Add a line break with a formula")](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

### [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

In this example, the goal is to join together three text values separated by line breaks. In Excel, you can use the keyboard shortcut Alt + Enter to add a line break in a cell that contains text, but the same approach won't work in a formula. The trick is to use the CHAR function with the ASCII...

[![Excel formula: Double quotes inside a formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/double%20quotes%20inside%20a%20formula.png "Excel formula: Double quotes inside a formula")](https://exceljet.net/formulas/double-quotes-inside-a-formula)

### [Double quotes inside a formula](https://exceljet.net/formulas/double-quotes-inside-a-formula)

To include double quotes inside a formula, you can use additional double quotes as escape characters . By escaping a character, you are telling Excel to treat the " character as literal text. You'll also need to include double quotes wherever you would normally in a formula. For example, if cell A1...

[![Excel formula: Count line breaks in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20line%20breaks%20in%20cell.png "Excel formula: Count line breaks in cell")](https://exceljet.net/formulas/count-line-breaks-in-cell)

### [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)

First, the LEN function counts total characters in the cell B5. Next SUBSTITUTE removes all "line returns" from the text in B5 by looking for CHAR(10) which is the character code for the return character in Windows. LEN returns the result inside of a second LEN, which counts characters without...

[![Excel formula: Generate random text strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/generate%20random%20strings.png "Excel formula: Generate random text strings")](https://exceljet.net/formulas/generate-random-text-strings)

### [Generate random text strings](https://exceljet.net/formulas/generate-random-text-strings)

The new dynamic array formulas in Excel 365 make it much easier to solve certain tricky problems with formulas. In this example, the goal is to generate a list of random 6-character codes. The randomness is handled by the RANDARRAY function , a new function in Excel 365. RANDARRAY returns 6 random...

[![Excel formula: Replace one delimiter with another](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/replace_one_delimiter_with_another.png "Excel formula: Replace one delimiter with another")](https://exceljet.net/formulas/replace-one-delimiter-with-another)

### [Replace one delimiter with another](https://exceljet.net/formulas/replace-one-delimiter-with-another)

In this example, the goal is to replace the comma-separated values in column B with the line break-separated values seen in column D. In a problem like this, the first step is to identify the delimiter , which is the character (or characters) that separate each value we want to process. In this...

[![Excel formula: Remove unwanted characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20unwanted%20characters.png "Excel formula: Remove unwanted characters")](https://exceljet.net/formulas/remove-unwanted-characters)

### [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)

The SUBSTITUTE function can find and replace text in a cell, wherever it occurs. In this case, we are using SUBSTITUTE to find a character with code number 202, and replace it with an empty string (""), which effectively removes the character completely. How can you figure out which character(s)...

[![Excel formula: Get last line in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20line%20in%20cell.png "Excel formula: Get last line in cell")](https://exceljet.net/formulas/get-last-line-in-cell)

### [Get last line in cell](https://exceljet.net/formulas/get-last-line-in-cell)

This formula takes advantage of the fact that TRIM will remove any number of leading spaces. We look for line breaks and "flood" the text with spaces where we find one. Then we come back and grab text from the right. Working from the inside out, we use the SUBSTITUTE function to find all line...

CHAR function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20concatenate%20with%20line%20breaks-thumb.png)](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

### [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

In the real world, you often need to concatenate values in a way that includes line breaks and other punctuation. In this video we'll look at a clever way to make this task easier and less error-prone. A common example of a situation that requires concatenation is assembling a mailing address from...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20CHAR%20and%20CODE%20functions-thumb.png)](https://exceljet.net/videos/how-to-use-char-and-code-functions)

### [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)

Each character you see displayed in Excel has a number. Excel has two functions that work with these numbers directly: CODE and CHAR (Character). Let's look first at the CODE function . The CODE function accepts one argument, which is the text for which you'd like a numeric code. If I use CODE with...

Related functions
-----------------

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

[![Excel UNICHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unichar_function.png "Excel UNICHAR function")](https://exceljet.net/functions/unichar-function)

### [UNICHAR Function](https://exceljet.net/functions/unichar-function)

The Excel UNICHAR function returns the Unicode character at a given code point

[![Excel CODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20code%20function.png "Excel CODE function")](https://exceljet.net/functions/code-function)

### [CODE Function](https://exceljet.net/functions/code-function)

The Excel CODE function returns a numeric code for a given character.  For example, CODE("a") returns the code 97....

[![Excel UNICODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unicode_function_0.png "Excel UNICODE function")](https://exceljet.net/functions/unicode-function)

### [UNICODE Function](https://exceljet.net/functions/unicode-function)

The Excel UNICODE function returns a decimal number (code point) corresponding to a Unicode character. Unicode is computing standard for the unified encoding, representation, and handling of text in most of the world's writing systems. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Double quotes inside a formula](https://exceljet.net/formulas/double-quotes-inside-a-formula)
    
*   [Generate random text strings](https://exceljet.net/formulas/generate-random-text-strings)
    
*   [If complete show checkmark](https://exceljet.net/formulas/if-complete-show-checkmark)
    
*   [Replace one delimiter with another](https://exceljet.net/formulas/replace-one-delimiter-with-another)
    
*   [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)
    
*   [Basic in cell histogram](https://exceljet.net/formulas/basic-in-cell-histogram)
    
*   [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)
    
*   [Get last line in cell](https://exceljet.net/formulas/get-last-line-in-cell)
    
*   [Add line break based on OS](https://exceljet.net/formulas/add-line-break-based-on-os)
    
*   [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)
    

### Videos

*   [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)
    
*   [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)
    

### Functions

*   [CHAR Function](https://exceljet.net/functions/char-function)
    
*   [UNICHAR Function](https://exceljet.net/functions/unichar-function)
    
*   [CODE Function](https://exceljet.net/functions/code-function)
    
*   [UNICODE Function](https://exceljet.net/functions/unicode-function)
    

### Links

*   [Microsoft CHAR function documentation](https://support.office.com/en-us/article/char-function-bbd249c8-b36e-4a91-8017-1c133f9b837a)
    

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