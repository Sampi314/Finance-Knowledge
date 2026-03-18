# Split text string at specific character - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-text-string-at-specific-character

---

[Skip to main content](https://exceljet.net/formulas/split-text-string-at-specific-character#main-content)

[](https://exceljet.net/formulas/split-text-string-at-specific-character#)

*   [Previous](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Next](https://exceljet.net/formulas/split-text-string-to-character-array)
    

[Text](https://exceljet.net/formulas#Text)

Split text string at specific character
=======================================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[LEFT](https://exceljet.net/functions/left-function)

[RIGHT](https://exceljet.net/functions/right-function)

[LEN](https://exceljet.net/functions/len-function)

[FIND](https://exceljet.net/functions/find-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8156/download?token=MR89-4WC)
 (21.55 KB)

![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")

Summary
-------

To split a text string at a specific character with a formula, you can use the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
. In the example shown, the formula in C5 is:

    =TEXTSPLIT(B5,"_")
    

As the formula is copied down, it returns the results seen in columns C and D. 

_Note: If you are using an older version of Excel that does not offer the TEXTSPLIT function, you can use a formula based on the LEFT, RIGHT, LEN, and FIND functions as explained below._

Generic formula
---------------

    =TEXTSPLIT(A1,"_")

Explanation 
------------

In this example, the goal is to split a [text string](https://exceljet.net/glossary/text-value)
 at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two basic approaches to solving this problem. If you are using Excel 365, the best approach is to use the TEXTBEFORE and TEXTAFTER functions. If you are using an older version of Excel without these functions, you can use a more complicated formula that combines the LEFT, RIGHT, LEN, and FIND functions. Both approaches are explained below.

> Note: in the worksheet shown, we split text at the underscore character ("\_"), but the solutions below can be adapted to split text at any character.

How to split text in Excel 365
------------------------------

The current version of Excel 365 contains three new functions that make this problem quite simple:

*   [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
     - split text at all given delimiters
*   [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
     - get the text _before_ a specific delimiter
*   [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
     - get the text _after_ a specific delimiter

Each option is described below. Choose the best option based on your specific needs.

### TEXTSPLIT function

The TEXTSPLIT function splits text at a given delimiter and returns the split text in an array that spills onto the worksheet into multiple cells. In the worksheet shown, the formula used to split text in cell C5 is:

    =TEXTSPLIT(B5,"_")

The text comes from cell B5 and the delimiter is provided as the underscore character wrapped in double quotes ("\_"). The result is an array with two values like this:

    {"Assessment","January 10"}

This array lands in cell C5 and spills into the range C5:D5. The result is "Assessment in cell C5 and "January 10" in cell D5. As the formula is copied down it performs the same operation on all values in column B.

Video demo: [Excel TEXTSPLIT function](https://exceljet.net/videos/excel-textsplit-function)

### With TEXTBEFORE and TEXTAFTER

Another way to solve this problem is to use the TEXTBEFORE and TEXTAFTER functions separately. You can extract text on the _left_ side of the underscore with the TEXTBEFORE function in cell C5 like this:

    =TEXTBEFORE(B5,"_") // left side
    

As the formula is copied down, it returns the text _before_ the underscore for each text string in B5:B16.

Video demo: [Excel TEXTBEFORE function](https://exceljet.net/videos/excel-textbefore-function)

To extract text on the _right_ side of the underscore, use the TEXTAFTER function in cell D5 like this:

    =TEXTAFTER(B5,"_") // right side
    

As the formula is copied down, it returns the text _after_ the underscore for each text string in B5:B16.

Video demo: [Excel TEXTAFTER function](https://exceljet.net/videos/excel-textafter-function)

How to split text in an older version of Excel
----------------------------------------------

Older versions of Excel do not offer the TEXTSPLIT, TEXTBEFORE, or TEXTAFTER functions. However, you can still split text at a specific character with a more complex formula that combines the [LEFT](https://exceljet.net/functions/left-function)
, [RIGHT](https://exceljet.net/functions/right-function)
, [LEN](https://exceljet.net/functions/len-function)
, and [FIND](https://exceljet.net/functions/find-function)
 functions.

![Formulas for splitting text in older versions of Excel](https://exceljet.net/sites/default/files/images/formulas/inline/split%20text%20string%20at%20specific%20character%20legacy.png "Formulas for splitting text in older versions of Excel")

### Left side

To extract the text on the _left_ side of the underscore, you can use a formula like this in cell C5:

    LEFT(B5,FIND("_",B5)-1) // left
    

Working from the inside out, this formula uses the [FIND function](https://exceljet.net/functions/find-function)
 to locate the underscore character ("\_") in the text, then subtracts 1 to move back one character:

    FIND("_",B5)-1 // returns 10
    

FIND returns 11, so the result after subtracting 1 is 10. This result is fed into the [LEFT function](https://exceljet.net/functions/left-function)
 as the _num\_chars_ argument, the number of characters to extract from B5, starting from the first character on the _left_:

    =LEFT(B5,10) // returns "Assessment"
    

The LEFT function returns the string "Assessment" as the final result. As this formula is copied down, it will return the same results seen in column C above.

### Right side

To extract text on the _right_ side of the underscore, you can use a formula like this in cell D5:

    RIGHT(B5,LEN(B5)-FIND("_",B5)) // right
    

As above, this formula also uses the FIND function to locate the underscore ("\_") at position 11. However, in this case, we want to extract text from the _right_ side of the string, so we need to calculate the number of characters to extract from the _right_. This is done by subtracting the result from FIND (11) from the total length of the text in B5 (21), which is calculated with the [LEN function](https://exceljet.net/functions/len-function)
:

    =LEN(B5)-FIND("_",B5)
    =21-11
    =10
    

The result is 10, which is returned to the RIGHT function as _num\_chars_, the number of characters to extract from the _right_:

    =RIGHT(B5,10) // returns "January 10"
    

The final result in D5 is the string "January 10". As this formula is copied down, it will return the same results seen in column D above.

Related formulas
----------------

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")](https://exceljet.net/formulas/get-last-word)

### [Get last word](https://exceljet.net/formulas/get-last-word)

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove any number of leading spaces. Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces: SUBSTITUTE(B6...

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

[![Excel formula: Trim text to n words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/trim%20text%20to%20n%20words.png "Excel formula: Trim text to n words")](https://exceljet.net/formulas/trim-text-to-n-words)

### [Trim text to n words](https://exceljet.net/formulas/trim-text-to-n-words)

We need a way to split text at a certain marker that corresponds to a certain number of words. Excel doesn't have a built-in function to parse text by word, so are using the SUBSTITUTE function's "instance" argument to replace an "nth space" character with the pound sign (#), then using FIND and...

Related functions
-----------------

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel_TEXTSPLIT_function_play.png)](https://exceljet.net/videos/excel-textsplit-function)

### [Excel TEXTSPLIT function](https://exceljet.net/videos/excel-textsplit-function)

In this video, we'll take a look at the TEXTSPLIT function. TEXTSPLIT is an Excel function designed to split text into separate cells using a given delimiter. In this worksheet, we have a list of email addresses. The goal is to split each email into a separate name and domain. As I start to enter...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The_TEXTBEFORE_function_Play.png)](https://exceljet.net/videos/excel-textbefore-function)

### [Excel TEXTBEFORE function](https://exceljet.net/videos/excel-textbefore-function)

In this video, we'll take a look at the TEXTBEFORE function. Like the name suggests, TEXTBEFORE is designed to extract text that occurs before a specific marker, called a "delimiter". A delimiter can be one or more characters. Let's look at an example. In this worksheet, we have a list of email...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The_TEXTAFTER_function_play.png)](https://exceljet.net/videos/excel-textafter-function)

### [Excel TEXTAFTER function](https://exceljet.net/videos/excel-textafter-function)

In this video, we'll take a look at the TEXTAFTER function. TEXTAFTER is designed to extract text that occurs after a specific "delimiter", which can be one or more characters. Let's look at an example. In this worksheet, we have a list of email addresses. The goal is to extract the domain portion...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    
*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    
*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Get last word](https://exceljet.net/formulas/get-last-word)
    
*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    
*   [Trim text to n words](https://exceljet.net/formulas/trim-text-to-n-words)
    

### Functions

*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

### Videos

*   [Excel TEXTSPLIT function](https://exceljet.net/videos/excel-textsplit-function)
    
*   [Excel TEXTBEFORE function](https://exceljet.net/videos/excel-textbefore-function)
    
*   [Excel TEXTAFTER function](https://exceljet.net/videos/excel-textafter-function)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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