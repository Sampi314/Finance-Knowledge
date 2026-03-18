# Normalize text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/normalize-text

---

[Skip to main content](https://exceljet.net/formulas/normalize-text#main-content)

[](https://exceljet.net/formulas/normalize-text#)

*   [Previous](https://exceljet.net/formulas/most-frequently-occurring-text)
    
*   [Next](https://exceljet.net/formulas/number-to-words)
    

[Text](https://exceljet.net/formulas#Text)

Normalize text
==============

by Dave Bruns · Updated 22 Jan 2019

Related functions 
------------------

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[TRIM](https://exceljet.net/functions/trim-function)

[LOWER](https://exceljet.net/functions/lower-function)

![Excel formula: Normalize text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/normalize%20text.png "Excel formula: Normalize text")

Summary
-------

To remove some of the natural complexity of text (strip punctuation, normalize case, remove extra spaces) you can use a formula based on the SUBSTITUTE function, with help from the TRIM and LOWER functions.

### Context

There may be times when you need to remove some of the variability of text before other processing. One example is when you want to count specific words inside larger text strings. Because Excel doesn't provide support for regular expressions, you can't construct precise matches. For example, if you want to count how many times the word "fox" appears in a cell, you will end up counting "foxes". You can look for "fox " (with a space) but that will fail with "fox," or "fox." One workaround is to simplify the text first with a formula in a [helper column](https://exceljet.net/glossary/helper-column)
, then run counts on the simplified version. The example on this page shows one way to do this.

Generic formula
---------------

    =LOWER(TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A1,"("," "),")"," "),"-"," "),":"," "),";"," "),"!"," "),","," "),"."," ")))

Explanation 
------------

The formula shown in this example uses a series of nested SUBSTITUTE functions to strip out parentheses, hyphens, colons, semi-colons, exclamation marks, commas, and periods. The process runs from the inside out, with each SUBSTITUTE replacing one character with a single space, then handing off to the next SUBSTITUTE. The inner most SUBSTITUTE removes the left parentheses, and the result is handed to the next SUBSTITUTE, which removes the right parentheses, and so on.

In the version below, line breaks have been added for readability, and to make it easier to edit replacements. Excel does not care about line breaks in formulas, so you can use the formula as-is.

    =
    LOWER(
    TRIM(
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    A1,
    "("," "),
    ")"," "),
    "-"," "),
    ":"," "),
    ";"," "),
    "!"," "),
    ","," "),
    "."," ")))
    

After all substitutions are complete, the result is run through TRIM to normalize spaces, then the LOWER function to force all text to lowercase.

_Note: You'll need to adjust the actual replacements to suit your data._

### Adding a leading and trailing space

In some cases you may want to add a space character to the start and end of the cleaned text. For example, if you want to count words precisely, you may want to look for the word surrounded by spaces (i.e. search for " fox ", " map ") to avoid false matches. To add a leading and trailing space, just concatenate a space (" ") to the start and end:

    =" "&formula&" "
    

Where "formula" is the longer formula above.

Related formulas
----------------

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

[![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

### [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

Excel doesn't have a way to cast the letters in a text string to an array directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is: =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(...

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

[![Excel formula: Find and replace multiple values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find-and-replace-multiple-values.png "Excel formula: Find and replace multiple values")](https://exceljet.net/formulas/find-and-replace-multiple-values)

### [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)

There is no built-in function to perform a series of find and replace operations in Excel, but you can create a formula that does the same thing. The goal in this example is to replace multiple ("find") values with corresponding ("replace") values in a single "replace all" operation. The text...

Related functions
-----------------

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel LOWER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lower%20function.png "Excel LOWER function")](https://exceljet.net/functions/lower-function)

### [LOWER Function](https://exceljet.net/functions/lower-function)

The Excel LOWER function converts a text string to all lowercase letters. Numbers, punctuation, and spaces are not affected.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    
*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)
    

### Functions

*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [LOWER Function](https://exceljet.net/functions/lower-function)
    

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