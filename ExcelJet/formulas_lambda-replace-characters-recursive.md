# LAMBDA replace characters recursive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-replace-characters-recursive

---

[Skip to main content](https://exceljet.net/formulas/lambda-replace-characters-recursive#main-content)

[](https://exceljet.net/formulas/lambda-replace-characters-recursive#)

*   [Previous](https://exceljet.net/formulas/lambda-count-words)
    
*   [Next](https://exceljet.net/formulas/lambda-split-text-to-array)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA replace characters recursive
===================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: LAMBDA replace characters recursive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20replace%20characters.png "Excel formula: LAMBDA replace characters recursive")

Summary
-------

The [LAMBDA function](https://exceljet.net/functions/lambda-function)
 can be used to create a custom function to replace characters. In the example shown, cell C5 contains the custom LAMBDA function "ReplaceChars":

    =ReplaceChars(B5,"!@#$%^&*()[]<>-?.,","")
    

The ReplaceChars function is designed to accept three input parameters:  **str** is the text to perform replacements on, **chars** is a text string containing the characters to replace, and **sub** is the character (or characters) to substitute when a character is found. In the example shown, ReplaceChars is configured to find the punctuation characters seen in the second argument (_chars_) and replace them with an [empty string](https://exceljet.net/glossary/empty-string)
 (""). This custom LAMBDA formula illustrates a feature called recursion, in which a function calls itself.

Generic formula
---------------

    =LAMBDA(str,chars,sub,
      IF(chars="",str,
        ReplaceChars(
          SUBSTITUTE(str,LEFT(chars),sub),
          MID(chars,2,LEN(chars)-1),
          sub
        )
      )
    )
    
    

Explanation 
------------

The [LAMBDA function](https://exceljet.net/functions/lambda-function)
 can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. However, one disadvantage to recursive LAMBDA functions is that they are not easy to test. This is because they can't be debugged directly on the worksheet, since a generic (unnamed) LAMBDA does not yet have a name and therefore can't call itself.

When creating a recursive LAMBDA formula a key consideration is how the formula will "exit" the loop it performs by calling itself. One common approach is to deplete an input parameter each time the formula calls itself, then check if the input is fully depleted before each call, and exit if so. In this way, the input parameter acts like a counter, counting down to zero.

This is the approach taken in this formula – the _chars_ parameter acts like a counter and one character is removed each time the formula calls itself. Before the recursive call, the [IF function](https://exceljet.net/functions/if-function)
 is used to check if _chars_ is empty. If so, the formula returns the current value for _str_ as a final result and exits. If not, the formula calls itself:

    =LAMBDA(str,chars,sub,
      IF(chars="",str, // test and exit if needed
        REPLACECHARS( // recurse
          SUBSTITUTE(str,LEFT(chars),sub),
          MID(chars,2,LEN(chars)-1),
          sub
        )
      )
    )
    

The actual replacement of the characters named in chars with the value of sub is handled by the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 here:

    SUBSTITUTE(str,LEFT(chars),sub)
    

SUBSTITUTE can only perform one replacement at a time, which is why this formula is recursive. The parameter _str_ is originally the text string provided to the function for character replacement, but note this value is potentially changing each time the function calls itself. The character to replace is provided by the [LEFT function](https://exceljet.net/functions/left-function)
:

    LEFT(chars) // get first character of chars
    

The value to use for replacement comes from _sub_. The trick to understanding the formula is to see that the result from SUBSTITUTE is used directly to call the ReplaceChars function, and this result becomes the "next" _str_ parameter. In addition, each time ReplaceChars is called, the string _chars_ is depleted by one character with the [MID function](https://exceljet.net/functions/mid-function)
, and the result from MID becomes the next value for _chars_ used in the call to ReplaceChars.

    MID(chars,2,LEN(chars)-1) // remove first character of chars
    

Once _chars_ has been fully depleted (i.e. chars becomes an empty string), the logical test inside the IF function returns TRUE, and the formula returns the current value of _str_ as a final result.

### Extending the formula

Custom LAMBDA functions behave like other functions, so you can easily extend functionality by [nesting](https://exceljet.net/glossary/nesting)
. For example, you could strip punctuation and replace it with a space character (" "), then clean things up after by nesting ReplaceChars inside of the [TRIM function](https://exceljet.net/functions/trim-function)
 like this:

    =TRIM(ReplaceChars(B5,"!@#$%^&*()[]<>-?.,"," "))
    

The TRIM function will return leading and trailing spaces, and normalize space between words to one space. This will avoid the problem of words being combined when they are separated by punctuation only.

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

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

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
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
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