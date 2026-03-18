# Trim text to n words - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/trim-text-to-n-words

---

[Skip to main content](https://exceljet.net/formulas/trim-text-to-n-words#main-content)

[](https://exceljet.net/formulas/trim-text-to-n-words#)

*   [Previous](https://exceljet.net/formulas/translate-letters-to-numbers)
    
*   [Next](https://exceljet.net/formulas/validate-strong-password)
    

[Text](https://exceljet.net/formulas#Text)

Trim text to n words
====================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[LEFT](https://exceljet.net/functions/left-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Trim text to n words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/trim%20text%20to%20n%20words.png "Excel formula: Trim text to n words")

Summary
-------

To trim text to a certain number of words, you can use a formula based on the [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
, [FIND](https://exceljet.net/functions/find-function)
, and [LEFT](https://exceljet.net/functions/left-function)
 functions. In the example shown, the formula in D5 is:

    =LEFT(B5,FIND("#",SUBSTITUTE(B5," ","#",C5))-1)
    

The result is "The cat sat" since the value for n in C5 is 3.

Generic formula
---------------

    =LEFT(txt,FIND("#",SUBSTITUTE(txt," ","#",n))-1)

Explanation 
------------

We need a way to split text at a certain marker that corresponds to a certain number of words. Excel doesn't have a built-in function to parse text by word, so are using the SUBSTITUTE function's "instance" argument to replace an "nth space" character with the pound sign (#), then using FIND and LEFT to discard all text after the marker.

Working from the inside out, SUBSTITUTE is configured to replace the nth occurrence of a space character, where n comes from column C, the text comes from column B, and "#" is hard coded.

    =SUBSTITUTE(B5," ","#",C5)
    =SUBSTITUTE("The cat sat on the mat."," ","#",3)
    ="The cat sat#on the mat."
    

The resulting string is returned to the FIND function, configured to look for "#".

    =FIND("#","The cat sat#on the mat.)
    

Since the "#" is the 12th character in the text, FIND returns 12. We don't want to include the space character itself in, so we subtract 1:

    =LEFT(B5,12-1)
    =LEFT(B5,11)
    

LEFT returns the final result from the formula, "The cat sat".

_Note: the pound character ("#") is arbitrary and can be replaced with any character that won't appear in the text._

### Add ellipses or another character

To add "..." to the end of the trimmed text, use [concatenation](https://exceljet.net/glossary/concatenation)
 like this:

    =LEFT(B5,FIND("#",SUBSTITUTE(B5," ","#",C5))-1)&"..."
    

You can replace "..." with anything you like.

Related formulas
----------------

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")](https://exceljet.net/formulas/get-last-word)

### [Get last word](https://exceljet.net/formulas/get-last-word)

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove any number of leading spaces. Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces: SUBSTITUTE(B6...

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

Related functions
-----------------

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    
*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Get last word](https://exceljet.net/formulas/get-last-word)
    
*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    

### Functions

*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

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