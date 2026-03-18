# Excel REPT function | Exceljet

**Source:** https://exceljet.net/functions/rept-function

---

[Skip to main content](https://exceljet.net/functions/rept-function#main-content)

[](https://exceljet.net/functions/rept-function#)

*   [Previous](https://exceljet.net/functions/replace-function)
    
*   [Next](https://exceljet.net/functions/right-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

REPT Function
=============

by Dave Bruns · Updated 5 Aug 2021

Related functions 
------------------

[FIND](https://exceljet.net/functions/find-function)

[REPLACE](https://exceljet.net/functions/replace-function)

![Excel REPT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")

Summary
-------

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

Purpose 
--------

Repeat text as specified

Return value 
-------------

The repeated text.

Syntax
------

    =REPT(text,number_times)

*   _text_ - The text to repeat.
*   _number\_times_ - The number of times to repeat text.

Using the REPT function 
------------------------

The REPT function repeats characters a specified number of times. Although REPT can repeat numbers as well as text, the result from REPT is always a [text value](https://exceljet.net/glossary/text-value)
. REPT takes two arguments, _text_ and _number\_times_. _Text_ is the character(s) to repeat, and _number\_times_ is the number of times _text_ should be repeated. 

REPT can be used to [pad values to a certain length](https://exceljet.net/formulas/pad-text-to-equal-length)
 or to build a [simple in-cell histogram](https://exceljet.net/formulas/basic-in-cell-histogram)
. To pad numeric values with zeros, a [custom number format](https://exceljet.net/articles/custom-number-formats)
 may be a better option.

### Examples

To repeat "x" five times, you can use the following formula:

    =REPT("x",5) // returns "xxxxx"

Inputs to REPT can be variable. In the example shown above, REPT is configured to repeat the values in column B using the count in column C.  The formula in D5 is:

    =REPT(B5,C5) // returns "-----"
    

REPT can be combined with other functions to calculate a variable count. For example, to pad a [text string](https://exceljet.net/glossary/text-value)
 with a specific character so that all strings are the same length, you can use REPT together with the [LEN function](https://exceljet.net/functions/len-function)
 like this:

    =A1&REPT("*",count-LEN(A1))
    

In this formula, "count" is the desired final length in characters. [Detailed explanation here](https://exceljet.net/formulas/pad-text-to-equal-length)
.

The REPT function appears in more advanced formulas that [solve some tricky problems](https://exceljet.net/formulas/extract-nth-word-from-text-string)
. See below for more examples.

### Notes

*   REPT can repeat numbers but the result is text.
*   _Number\_times_ should be zero or a positive integer, otherwise, REPT will return #VALUE!
*   If _number\_times_ is zero, REPT returns an [empty string](https://exceljet.net/glossary/empty-string)
     ("").

REPT function examples
----------------------

[![Excel formula: Basic in cell histogram](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20in%20cell%20histogram.png "Excel formula: Basic in cell histogram")](https://exceljet.net/formulas/basic-in-cell-histogram)

### [Basic in cell histogram](https://exceljet.net/formulas/basic-in-cell-histogram)

The REPT function simply repeats values. For example, this formula outputs 10 asterisks: =REPT("\*",10) // outputs \*\*\*\*\*\*\*\*\*\* You can use REPT to repeat any character(s) you like. In this example, we use the CHAR function to output a character with a code of 110. This character, when formatted with...

[![Excel formula: Convert inches to feet and inches](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Convert%20inches%20to%20feet%20and%20inches.png "Excel formula: Convert inches to feet and inches")](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

### [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)

In this example, the goal is to create a formula that converts a numeric value in inches to a format that displays inches and feet, as seen in the table below: Input Output 9 0' 9" 12 1' 0" 30 2' 6" 75 6' 3" The math for this problem is fairly simple, but the problem is more complex because we need...

[![Excel formula: Last row in text data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Last%20row%20in%20text%20data.png "Excel formula: Last row in text data")](https://exceljet.net/formulas/last-row-in-text-data)

### [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)

This formula uses the MATCH function in approximate match mode to locate the last text value in a range. Approximate match enabled by setting by the 3rd argument in MATCH to 1, or omitting this argument, which defaults to 1. The lookup value is a so-called "big text" (sometimes abbreviated "bigtext...

[![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")](https://exceljet.net/formulas/get-last-word)

### [Get last word](https://exceljet.net/formulas/get-last-word)

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove any number of leading spaces. Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces: SUBSTITUTE(B6...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Count cells that contain n characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20n%20characters.png "Excel formula: Count cells that contain n characters")](https://exceljet.net/formulas/count-cells-that-contain-n-characters)

### [Count cells that contain n characters](https://exceljet.net/formulas/count-cells-that-contain-n-characters)

In this example, the goal is to count the number of cells in B5:B15 that contain a given number of characters, where the number of characters n is provided as a variable in cell E4. SUMPRODUCT with LEN One way to solve this problem is to use the SUMPRODUCT function with the LEN function . In the...

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

[![Excel formula: Pad a number with zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20number%20with%20zeros.png "Excel formula: Pad a number with zeros")](https://exceljet.net/formulas/pad-a-number-with-zeros)

### [Pad a number with zeros](https://exceljet.net/formulas/pad-a-number-with-zeros)

In this example, the goal is to pad a number with zeros. To illustrate how Excel functions can be combined, the number of zeros to use is variable and comes from column C. The formula used to solve this problem combines the TEXT function and the REPT function . Fixed number The TEXT function...

[![Excel formula: Pad text to equal length](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20text%20to%20equal%20length.png "Excel formula: Pad text to equal length")](https://exceljet.net/formulas/pad-text-to-equal-length)

### [Pad text to equal length](https://exceljet.net/formulas/pad-text-to-equal-length)

This formula concatenates the original value in column B to a string of asterisks (\*) assembled with the REPT function so that the final result is always 12 characters: REPT("\*",12-LEN(B5)) Inside the REPT function, the text to repeat is provided as a single asterisk ("\*"). The number of asterisks...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Conditional message with REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20message%20with%20REPT.png "Excel formula: Conditional message with REPT function")](https://exceljet.net/formulas/conditional-message-with-rept-function)

### [Conditional message with REPT function](https://exceljet.net/formulas/conditional-message-with-rept-function)

This formula uses boolean logic to output a conditional message. If the value in column C is less than 100, the formula returns "low". If not, the formula returns an empty string (""). Boolean logic is a technique of handling TRUE and FALSE values like 1 and 0. In cell C5, the formula is evaluated...

[![Excel formula: Extract word containing specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20containing%20specific%20text.png "Excel formula: Extract word containing specific text")](https://exceljet.net/formulas/extract-word-containing-specific-text)

### [Extract word containing specific text](https://exceljet.net/formulas/extract-word-containing-specific-text)

The gist: this formula "floods" the space between words in a text string with a large number of spaces, finds and extracts the substring of interest, and uses the TRIM function to clean up the mess. Working from the inside out, the original text in B5 is flooded with spaces using SUBSTITUTE:...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Get last line in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20line%20in%20cell.png "Excel formula: Get last line in cell")](https://exceljet.net/formulas/get-last-line-in-cell)

### [Get last line in cell](https://exceljet.net/formulas/get-last-line-in-cell)

This formula takes advantage of the fact that TRIM will remove any number of leading spaces. We look for line breaks and "flood" the text with spaces where we find one. Then we come back and grab text from the right. Working from the inside out, we use the SUBSTITUTE function to find all line...

REPT function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20REPT%20function%20to%20repeat%20things-thumb.png)](https://exceljet.net/videos/how-to-use-the-rept-function-to-repeat-things)

### [How to use the REPT function to repeat things](https://exceljet.net/videos/how-to-use-the-rept-function-to-repeat-things)

In this video we'll look at how to use the REPT function in Excel to repeat text. Excel contains a special function for repeating text named REPT which stands for "repeat." The REPT function takes two arguments: the text to repeat, and the number of times to repeat the text. So, if I enter an upper...

Related functions
-----------------

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel REPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20replace%20function.png "Excel REPLACE function")](https://exceljet.net/functions/replace-function)

### [REPLACE Function](https://exceljet.net/functions/replace-function)

The Excel REPLACE function replaces characters at a specified position in a given text string with another text string. REPLACE a good solution when the text to replace can't easily be matched, but the location is predictable.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that contain n characters](https://exceljet.net/formulas/count-cells-that-contain-n-characters)
    
*   [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Basic in cell histogram](https://exceljet.net/formulas/basic-in-cell-histogram)
    
*   [Conditional message with REPT function](https://exceljet.net/formulas/conditional-message-with-rept-function)
    
*   [Extract word containing specific text](https://exceljet.net/formulas/extract-word-containing-specific-text)
    
*   [Pad a number with zeros](https://exceljet.net/formulas/pad-a-number-with-zeros)
    
*   [Last row in text data](https://exceljet.net/formulas/last-row-in-text-data)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Pad text to equal length](https://exceljet.net/formulas/pad-text-to-equal-length)
    
*   [Convert inches to feet and inches](https://exceljet.net/formulas/convert-inches-to-feet-and-inches)
    

### Videos

*   [How to use the REPT function to repeat things](https://exceljet.net/videos/how-to-use-the-rept-function-to-repeat-things)
    

### Functions

*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    

### Links

*   [Microsoft REPT function documentation](https://support.office.com/en-us/article/rept-function-04c4d778-e712-43b4-9c15-d656582bb061)
    

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