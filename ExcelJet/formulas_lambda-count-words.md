# LAMBDA count words - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lambda-count-words

---

[Skip to main content](https://exceljet.net/formulas/lambda-count-words#main-content)

[](https://exceljet.net/formulas/lambda-count-words#)

*   [Previous](https://exceljet.net/formulas/lambda-contains-which-things)
    
*   [Next](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

LAMBDA count words
==================

by Dave Bruns · Updated 27 Aug 2022

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[TRIM](https://exceljet.net/functions/trim-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: LAMBDA count words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/lambda%20count%20words.png "Excel formula: LAMBDA count words")

Summary
-------

The [LAMBDA function](https://exceljet.net/functions/lambda-function)
 can be used to create a custom function to count total words in a cell. In the example shown, cell C5 contains the custom function "CountWords", based on this formula:

    =LAMBDA(text,LEN(TRIM(text))-LEN(SUBSTITUTE(text," ",""))+(LEN(TRIM(text))>0))
    

Where **text** represents a text string. As the formula is copied down, CountWords returns the count of words in column B.

_Note: the LAMBDA function is available through the beta channel of [Excel 365](https://exceljet.net/glossary/excel-365)
 only._

Explanation 
------------

The [LAMBDA function](https://exceljet.net/functions/lambda-function)
 can be used to create reusable, custom functions in Excel without VBA or macros. The first step in creating a LAMBDA function is to verify the formula logic needed in a standard Excel formula. In this example, the base formula is:

    =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(LEN(TRIM(B5))>0)
    

This formula uses three built-in functions: [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
, [TRIM](https://exceljet.net/functions/trim-function)
, and [LEN](https://exceljet.net/functions/len-function)
. Here is the formula in action below. You can [read a detailed explanation here](https://exceljet.net/formulas/count-total-words-in-a-cell)
.

![Standard Excel formula for counting words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lambda%20count%20words%20standard%20formula.png?itok=2ydTO7QG "Standard Excel formula for counting words")

The formula only requires one input parameter, the text in cell B5, so the LAMBDA function will have two arguments, the text from a cell, and the calculation to perform. Here is the formula converted to LAMBDA:

    =LAMBDA(text,LEN(TRIM(text))-LEN(SUBSTITUTE(text," ",""))+(LEN(TRIM(text))>0)
    

Notice _text_ appears as the first argument, and the word count calculation is the second argument. To test the LAMBDA version of the formula, use the syntax below:

    =LAMBDA(text,LEN(TRIM(text))-LEN(SUBSTITUTE(text," ",""))+(LEN(TRIM(text))>0) (B5)
    

Note the reference to B5 in parentheses at the end is used for the _text_ argument**.**

![Unnamed LAMBDA formula for counting words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lambda%20count%20words%20generic.png?itok=xXnyWjlo "Unnamed LAMBDA formula for counting words")

The results from the generic LAMBDA formula are the same as the original formula, so the next step is to name the formula "CountWords" in the [Name Manager](https://exceljet.net/glossary/name-manager)
. Once the name has been created, CountWords function can now be used in the workbook:

![Custom CountWords function now available](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lambda%20count%20words%20function%20available.png?itok=rrlKYK2M "Custom CountWords function now available")

In the screen below, we've replaced the generic (unnamed) LAMBDA formula with the named LAMBDA version, and entered B5 for text.

![Custom CountWords function now available](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/lambda%20count%20words%20function%20in%20action.png?itok=bpR65MZe "Custom CountWords function now available")

Like all custom LAMBDA function, any changes to the formula defined in the Name Manager will propagate to all instances of the function in the worksheet. 

Related formulas
----------------

[![Excel formula: Count total words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_total_words_in_cell.png "Excel formula: Count total words in a cell")](https://exceljet.net/formulas/count-total-words-in-a-cell)

### [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)

In this example, the goal is to count the total number of words in a cell. Excel doesn't have a dedicated function for counting words. However, with a little ingenuity, you can create a formula to perform this task using a combination of built-in functions. In newer versions of Excel, the best...

[![Excel formula: LAMBDA replace characters recursive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20replace%20characters.png "Excel formula: LAMBDA replace characters recursive")](https://exceljet.net/formulas/lambda-replace-characters-recursive)

### [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)

The LAMBDA function can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. However, one disadvantage to recursive LAMBDA functions is that...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

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

*   [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)
    
*   [LAMBDA replace characters recursive](https://exceljet.net/formulas/lambda-replace-characters-recursive)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
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