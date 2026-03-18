# Extract substring - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-substring

---

[Skip to main content](https://exceljet.net/formulas/extract-substring#main-content)

[](https://exceljet.net/formulas/extract-substring#)

*   [Previous](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Next](https://exceljet.net/formulas/extract-text-between-parentheses)
    

[Text](https://exceljet.net/formulas#Text)

Extract substring
=================

by Dave Bruns · Updated 26 Nov 2018

Related functions 
------------------

[MID](https://exceljet.net/functions/mid-function)

![Excel formula: Extract substring](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/excel%20substring.png "Excel formula: Extract substring")

Summary
-------

To extract a substring with an Excel formula, you can use the MID function. In the example shown, the formula in E5 is:

    =MID(B5,C5,D5-C5+1)
    

which, on row 5, returns "Perfect".

Generic formula
---------------

    =MID(A1,start,end-start+1)

Explanation 
------------

_Note: in this example, we are calculating the end position in order to extract a substring with a literal start and end position. However, if you know the number of characters to extract, you can just plug in that number directly._

In the example on this page, we are using the MID function to extract text based on a start and end position. The MID function accepts three arguments: a text string, a starting position, and the number of characters to extract. The text comes from column B, and the starting position comes from column C. The number of characters to extract is calculated by subtracting the start from end, and adding 1. In cell E6:

    =MID(B5,C5,D5-C5+1)
    =MID("Perfect is the enemy of good",1,7-1+1)
    =MID(B5,1,7) // returns "Perfect"
    

### Functions to extract substrings

Excel provides three primary functions for extracting substrings:

    =MID(txt,start,chars) // extract from middle
    =LEFT(txt,chars) // extract from left
    =RIGHT(txt,chars) // extract from right
    

Click on function names above for details and linked examples.

### Finding start and end positions with a formula

In the example shown, start and end positions are based on hardcoded values. However, it is possible to calculate positions with the [FIND function](https://exceljet.net/functions/find-function)
 and [SEARCH function](https://exceljet.net/functions/search-function)
. See links below for examples.

Related formulas
----------------

[![Excel formula: Extract text between parentheses](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20text%20in%20parentheses.png "Excel formula: Extract text between parentheses")](https://exceljet.net/formulas/extract-text-between-parentheses)

### [Extract text between parentheses](https://exceljet.net/formulas/extract-text-between-parentheses)

The foundation of this formula is the MID function, which extracts a specific number of characters from text, starting at a specific location. To figure out where to start extracting text, we use this expression: SEARCH("(",B5)+1 This locates the left parentheses and adds 1 to get the position of...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

Related functions
-----------------

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract text between parentheses](https://exceljet.net/formulas/extract-text-between-parentheses)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    

### Functions

*   [MID Function](https://exceljet.net/functions/mid-function)
    

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