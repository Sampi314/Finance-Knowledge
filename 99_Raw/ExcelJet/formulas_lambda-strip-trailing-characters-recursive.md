# LAMBDA strip trailing characters recursive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive

---

[Skip to main content](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive#main-content)

[](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive#)

*   [Previous](https://exceljet.net/formulas/lambda-strip-characters)
    
*   [Next](https://exceljet.net/formulas/list-upcoming-birthdays)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA strip trailing characters recursive
==========================================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: LAMBDA strip trailing characters recursive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20strip%20trailing%20characters%20recursive.png "Excel formula: LAMBDA strip trailing characters recursive")

Summary
-------

The [LAMBDA function](https://exceljet.net/functions/lambda-function)
 can be used to create custom, reusable functions. In the example shown, cell D5 contains the custom LAMBDA function "StripTrailingChars":

    =StripTrailingChars(B5,C5)
    

The StripTrailingChars function is designed to accept two input parameters:  **str** is the text from which to remove trailing characters, and **char** is the trailing character to remove. In the example shown, StripTrailingChars is configured to remove the characters seen in column C from the text seen in column B. These characters will only be removed when they are "trailing", i.e. when they appear at the end of the string. This custom LAMBDA formula illustrates a feature called recursion, in which a function calls itself.

_Note: the [LAMBDA function](https://exceljet.net/functions/lambda-function)
 is available through the beta channel of [Excel 365](https://exceljet.net/glossary/excel-365)
 only._

Generic formula
---------------

    =LAMBDA(str,char,
      IF(RIGHT(str)<>char,str,
        StripTrailingChars(
          MID(str,1,LEN(str)-1),
          char
        )
      )
    )

Explanation 
------------

[LAMBDA function](https://exceljet.net/functions/lambda-function)
 can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. This example is primarily proof of concept, to show a very simple recursive LAMBDA function.

When creating a recursive LAMBDA formula a key consideration is how the formula will "exit" the loop it performs by calling itself. In this example, before the recursive call happens, the [IF function](https://exceljet.net/functions/if-function)
 is used to check the last character of the input text string (**str**). If the last character is not equal to the target character (**char**) the function exits and returns the current value of **str**. Otherwise, the formula calls itself:

    =LAMBDA(str,char,
      IF(RIGHT(str)<>char,str, // test and exit if needed
        StripTrailingChars( // recurse
          MID(str,1,LEN(str)-1),
          char
        )
      )
    )
    

The actual removal of the trailing character is handled by the [MID function](https://exceljet.net/functions/mid-function)
 and [LEN function](https://exceljet.net/functions/len-function)
:

    MID(str,1,LEN(str)-1)
    

The MID function returns the value of **str** without the last character. MID strips one character at a time, which is why this formula is recursive. The result is given to the StripTrailingChars function, along with the original value for **char**. When all the target trailing characters have been removed, the function returns the current value for **str**.

You can find more general information about the LAMBDA function [here](https://exceljet.net/functions/lambda-function)
.

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

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

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
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

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