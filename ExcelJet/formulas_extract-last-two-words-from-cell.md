# Extract last two words from cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-last-two-words-from-cell

---

[Skip to main content](https://exceljet.net/formulas/extract-last-two-words-from-cell#main-content)

[](https://exceljet.net/formulas/extract-last-two-words-from-cell#)

*   [Previous](https://exceljet.net/formulas/encode-unicode-sequence-into-text)
    
*   [Next](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    

[Text](https://exceljet.net/formulas#Text)

Extract last two words from cell
================================

by Dave Bruns · Updated 27 Nov 2020

Related functions 
------------------

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Extract last two words from cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Extract%20last%20two%20words%20from%20cell.png "Excel formula: Extract last two words from cell")

Summary
-------

To extract the last two words from a cell, you can use a formula built with several Excel functions, including MID, FIND, SUBSTITUTE, and LEN. In the example shown, the formula in C5 is:

    =MID(B5,FIND("@",SUBSTITUTE(B5," ","@",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))-1))+1,100)
    

Generic formula
---------------

    =MID(A1,FIND("@",SUBSTITUTE(A1," ","@",LEN(A1)-LEN(SUBSTITUTE(A1," ",""))-1))+1,100)

Explanation 
------------

At the core, this formula uses the MID function to extract characters starting at the _second to last_ space. The MID function takes 3 arguments: the text to work with, the starting position, and the number of characters to extract.

The text comes from column B, and the number of characters can be any large number that will ensure the last two words are extracted. The challenge is to determine the starting position, which is just after the second to last space. The clever work is done primarily with the SUBSTITUTE function, which has an optional argument called instance number. This feature is used to replace the second to last space in the text with the "@" character, which is then located with the FIND function.

Working from the inside out, the snippet below figures out how many spaces are in the text total, from which 1 is subtracted.

    LEN(B5)-LEN(SUBSTITUTE(B5," ",""))-1
    

In the example shown, there are 5 spaces in the text, so the code above returns 4. This number is fed into the outer SUBSTITUTE function as instance number:

    SUBSTITUTE(B5," ","@",4)
    

This causes SUBSTITUTE to replace the fourth space character with "@". The choice of @ is arbitrary. You can use any character that will not appear in the original text.

Next, the FIND locates the "@" character in the text:

    FIND("@","A stitch in time@saves nine")
    

The result of FIND is 17, to which 1 is added to get 18. This is the starting position, and goes into the MID function as the second argument. For simplicity, the number of characters to extract is hardcoded as 100. This number is arbitrary and can be adjusted to fit the situation.

### Extract last N words from cell

This formula can be generalized to extract the last N words from a cell by replacing the hardcoded 1 in the example with (N-1). In addition, if you are extracting many words, you may want to replace the hardcoded argument in MID, 100, with a larger number. To guarantee you the number is large enough, you could simply use the LEN function as follows:

    =MID(B5,FIND("@",SUBSTITUTE(B5," ","@",LEN(B5)-LEN(SUBSTITUTE(B5," ",""))-(N-1)))+1,LEN(B5))
    

Related formulas
----------------

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Find nth occurrence of character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find%20nth%20occurrence%20of%20character.png "Excel formula: Find nth occurrence of character")](https://exceljet.net/formulas/find-nth-occurrence-of-character)

### [Find nth occurrence of character](https://exceljet.net/formulas/find-nth-occurrence-of-character)

In this example, the goal is to determine the position of the nth occurrence of a specific character (delimiter) in the text strings in column B. This article explains two approaches: A modern formula based on the TEXTBEFORE function. A more traditional formula for older versions of Excel. The...

Related functions
-----------------

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

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

*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Find nth occurrence of character](https://exceljet.net/formulas/find-nth-occurrence-of-character)
    

### Functions

*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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