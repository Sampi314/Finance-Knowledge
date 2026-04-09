# LAMBDA strip characters - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-strip-characters

---

[Skip to main content](https://exceljet.net/formulas/lambda-strip-characters#main-content)

[](https://exceljet.net/formulas/lambda-strip-characters#)

*   [Previous](https://exceljet.net/formulas/lambda-split-text-to-array)
    
*   [Next](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA strip characters
=======================

by Dave Bruns · Updated 27 Feb 2021

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[MID](https://exceljet.net/functions/mid-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: LAMBDA strip characters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20strip%20characters.png "Excel formula: LAMBDA strip characters")

Summary
-------

This is an experimental formula to strip characters from text using a formula created with the [LET](https://exceljet.net/functions/let-function)
 and [LAMBDA](https://exceljet.net/functions/lambda-function)
 functions. In the example shown, the formula in F5, copied down, is:

    =LET(text,B5,chars,C5,rep,D5,keep,E5,
    textarr,CODE(MID(text,SEQUENCE(LEN(text)),1)),
    chararr,CODE(MID(chars,SEQUENCE(LEN(chars)),1)),
    TEXTJOIN("",1,IF(ABS(keep-ISNUMBER(MATCH(textarr,chararr,0))),rep&"",CHAR(textarr)))
    )
    

Unlike the [formula explained here](https://exceljet.net/formulas/lambda-replace-characters-recursive)
, this formula is not recursive.

Explanation 
------------

This is an experimental formula to strip characters from text. The experimental part is using [character codes](https://exceljet.net/videos/how-to-use-char-and-code-functions)
 instead of regular characters as a way to make the formula case-sensitive, and providing a way to reverse the logic of the formula with the "keep" input parameter. Unlike the [formula explained here](https://exceljet.net/formulas/lambda-replace-characters-recursive)
, this formula is not recursive.

The formula takes four inputs:

**text** - the incoming text  
**chars** - the characters to strip  
**rep** - the character to replace stripped characters with  
**keep** - strip or preserve chars (FALSE = strip, TRUE = preserve)

The **keep** parameter is a boolean that "flips" the behavior of the function from stripping characters to preserving characters.

In a nutshell, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is used to generate two [arrays](https://exceljet.net/glossary/array)
: one for the **text**, one for **chars**. In order to make the function case-sensitive, these arrays are composed not of characters but of the ASCII codes for each character.

    textarr,CODE(MID(text,SEQUENCE(LEN(text)),1)),
    chararr,CODE(MID(chars,SEQUENCE(LEN(chars)),1))
    

The [MID function](https://exceljet.net/functions/mid-function)
 extracts one character at a time, and [CODE](https://exceljet.net/functions/code-function)
 returns the numeric code. Inside the [IF function](https://exceljet.net/functions/if-function)
, the logical test is:

    ABS(keep-ISNUMBER(MATCH(textarr,chararr,0))) // logical test
    

The [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [MATCH](https://exceljet.net/functions/match-function)
 combo checks each code in **textarr** against codes in **chararr**. The [ABS function](https://exceljet.net/functions/abs-function)
 is used as a way to reverse the logic of the formula. If **keep** is set to FALSE or zero, the ISNUMBER+MATCH logic is unchanged and **chars** are stripped. If **keep** is TRUE (or 1) the logic is reversed – **chars** are preserved and other characters are stripped.

### LAMBDA version

To convert the formula to the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 so that the formula can be named and reused throughout the workbook, the four input arguments are moved to the front, followed by the calculation, wrapped in LET:

    =LAMBDA(text,chars,rep,keep,
    LET(
    textarr,CODE(MID(text,SEQUENCE(LEN(text)),1)),
    chararr,CODE(MID(chars,SEQUENCE(LEN(chars)),1)),
    TEXTJOIN("",1,IF(ABS(keep-ISNUMBER(MATCH(textarr,chararr,0))),rep&"",CHAR(textarr)))
    ))
    

After the LAMBDA function is named "StripCharacters" the function can be called like this:

    =StripCharacters(B5,"()-","",FALSE)
    

Per the example shown, the text is in cell B5, the characters to strip are "()-", the replacement string is "", and preserve mode is set to FALSE.

Related formulas
----------------

[![Excel formula: LAMBDA count words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20count%20words.png "Excel formula: LAMBDA count words")](https://exceljet.net/formulas/lambda-count-words)

### [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)

The LAMBDA function can be used to create reusable, custom functions in Excel without VBA or macros. The first step in creating a LAMBDA function is to verify the formula logic needed in a standard Excel formula. In this example, the base formula is: =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(LEN(...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

[![Excel formula: LAMBDA replace characters recursive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20replace%20characters.png "Excel formula: LAMBDA replace characters recursive")](https://exceljet.net/formulas/lambda-replace-characters-recursive)

### [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)

The LAMBDA function can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. However, one disadvantage to recursive LAMBDA functions is that...

[![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

### [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

Excel doesn't have a way to cast the letters in a text string to an array directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is: =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    
*   [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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