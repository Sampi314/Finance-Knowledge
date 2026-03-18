# Extract text between parentheses - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-text-between-parentheses

---

[Skip to main content](https://exceljet.net/formulas/extract-text-between-parentheses#main-content)

[](https://exceljet.net/formulas/extract-text-between-parentheses#)

*   [Previous](https://exceljet.net/formulas/extract-substring)
    
*   [Next](https://exceljet.net/formulas/extract-word-containing-specific-text)
    

[Text](https://exceljet.net/formulas#Text)

Extract text between parentheses
================================

by Dave Bruns · Updated 25 Nov 2018

Related functions 
------------------

[MID](https://exceljet.net/functions/mid-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel formula: Extract text between parentheses](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract%20text%20in%20parentheses.png "Excel formula: Extract text between parentheses")

Summary
-------

To extract text between parentheses, braces, brackets, etc. you can use a formula based on the MID function, with help from SEARCH function. In the example shown, the formula in C5 is:

    =MID(B5,SEARCH("(",B5)+1,SEARCH(")",B5)-SEARCH("(",B5)-1)+0
    

Generic formula
---------------

    =MID(txt,SEARCH("(",txt)+1,SEARCH(")",txt)-SEARCH("(",txt)-1)

Explanation 
------------

The foundation of this formula is the MID function, which extracts a specific number of characters from text, starting at a specific location. To figure out where to start extracting text, we use this expression:

    SEARCH("(",B5)+1
    

This locates the left parentheses and adds 1 to get the position of the first character inside the parentheses. To figure out how many characters to extract, we use this expression:

    SEARCH(")",B5)-SEARCH("(",B5)-1
    

This locates the second parentheses in the text, and subtracts the position of the first parentheses (less one) to get the total number of characters that need to be extracted. With this information, MID extracts just the text inside the parentheses.

Finally, because we want a number as the final result in this particular example, we add zero to text value returned by MID:

    +0
    

This math operation causes Excel to coerce text values to numbers. If you don't need or want a number at the end, this step is _not required_.

Related formulas
----------------

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

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    

### Functions

*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

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