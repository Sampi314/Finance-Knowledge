# Extract multiple lines from a cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-multiple-lines-from-a-cell

---

[Skip to main content](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell#main-content)

[](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell#)

*   [Previous](https://exceljet.net/formulas/extract-last-two-words-from-cell)
    
*   [Next](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    

[Text](https://exceljet.net/formulas#Text)

Extract multiple lines from a cell
==================================

by Dave Bruns · Updated 5 Jun 2021

Related functions 
------------------

[TRIM](https://exceljet.net/functions/trim-function)

[MID](https://exceljet.net/functions/mid-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[REPT](https://exceljet.net/functions/rept-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")

Summary
-------

To extract lines from a multi-line cell, you can use a clever (and intimidating) formula that combines 5 Excel functions: [TRIM](https://exceljet.net/functions/trim-function)
, [MID](https://exceljet.net/functions/mid-function)
, [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
, [REPT](https://exceljet.net/functions/rept-function)
, and [LEN](https://exceljet.net/functions/len-function)
. In the example shown, the formula in D5 is:

    =TRIM(MID(SUBSTITUTE($C5,CHAR(10),REPT(" ",LEN($C5))), (D$4-1)*LEN($C5)+1, LEN($C5)))
    

In the generic formula above, "N" represents the "nth line".

Generic formula
---------------

    =TRIM(MID(SUBSTITUTE(A1,delim,REPT(" ",LEN(A1))), (N-1)*LEN(A1)+1, LEN(A1)))

Explanation 
------------

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions.

_Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The [CHAR function](https://exceljet.net/functions/char-function)
 returns a character based on it's numeric code._

The number of spaces used to replace the line delimiter is based on the total length the text in the cell. The formula then uses the MID function to extract the desired line. The starting point is worked out with:

    (N-1)*LEN(A1)+1 // start_num
    

Where "N" stands for "nth line", which is picked up from row 4 with the D$4 reference.

The total characters extracted is equal to the length of the full text string:

    LEN(A1) // num_chars
    

At this point, we have the "nth line", surrounded by spaces.

Finally, the TRIM function slices off all extra space characters and returns just the line text.

### Text to Columns

Don't forget that Excel has a built-in [Text to Columns feature](https://exceljet.net/glossary/text-to-columns)
 that can split text according to the delimiter of your choice, though it is not a dynamic solution like a formula. On Windows, you can type Control + J to enter the equivalent of a new line character for the "Other" delimiter. You can also use Control + J for new line during search and replace operations.

I'm not sure how to enter a new line character in Mac Excel, as a delimiter, or in the search and replace dialog. If you know how, please leave a comment below.

Related formulas
----------------

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")](https://exceljet.net/formulas/get-last-word)

### [Get last word](https://exceljet.net/formulas/get-last-word)

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove any number of leading spaces. Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces: SUBSTITUTE(B6...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Count line breaks in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20line%20breaks%20in%20cell.png "Excel formula: Count line breaks in cell")](https://exceljet.net/formulas/count-line-breaks-in-cell)

### [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)

First, the LEN function counts total characters in the cell B5. Next SUBSTITUTE removes all "line returns" from the text in B5 by looking for CHAR(10) which is the character code for the return character in Windows. LEN returns the result inside of a second LEN, which counts characters without...

[![Excel formula: Remove line breaks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20line%20breaks.png "Excel formula: Remove line breaks")](https://exceljet.net/formulas/remove-line-breaks)

### [Remove line breaks](https://exceljet.net/formulas/remove-line-breaks)

First, you should know that Excel contains two functions, CLEAN and TRIM, that can automatically remove line breaks and extra spaces from text. For example to strip all line breaks from a cell, you could use: =CLEAN(B5) For a quick demo of CLEAN and TRIM, watch this video . In this case, however,...

Related functions
-----------------

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20concatenate%20with%20line%20breaks-thumb.png)](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

### [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

In the real world, you often need to concatenate values in a way that includes line breaks and other punctuation. In this video we'll look at a clever way to make this task easier and less error-prone. A common example of a situation that requires concatenation is assembling a mailing address from...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20CHAR%20and%20CODE%20functions-thumb.png)](https://exceljet.net/videos/how-to-use-char-and-code-functions)

### [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)

Each character you see displayed in Excel has a number. Excel has two functions that work with these numbers directly: CODE and CHAR (Character). Let's look first at the CODE function . The CODE function accepts one argument, which is the text for which you'd like a numeric code. If I use CODE with...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Get last word](https://exceljet.net/formulas/get-last-word)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)
    
*   [Remove line breaks](https://exceljet.net/formulas/remove-line-breaks)
    

### Functions

*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [REPT Function](https://exceljet.net/functions/rept-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

### Videos

*   [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)
    
*   [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)
    

### Links

*   [Efficient way to extract nth word from string (MrExcel forum)](http://www.mrexcel.com/forum/excel-questions/504050-efficient-way-extract-nth-word-string.html)
    

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