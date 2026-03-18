# Translate letters to numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/translate-letters-to-numbers

---

[Skip to main content](https://exceljet.net/formulas/translate-letters-to-numbers#main-content)

[](https://exceljet.net/formulas/translate-letters-to-numbers#)

*   [Previous](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    
*   [Next](https://exceljet.net/formulas/trim-text-to-n-words)
    

[Text](https://exceljet.net/formulas#Text)

Translate letters to numbers
============================

by Dave Bruns · Updated 6 Aug 2019

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[MID](https://exceljet.net/functions/mid-function)

[ROW](https://exceljet.net/functions/row-function)

[T](https://exceljet.net/functions/t-function)

![Excel formula: Translate letters to numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/translate%20letters%20to%20numbers.png "Excel formula: Translate letters to numbers")

Summary
-------

To translate letters in a string to numbers, you can use an array formula based on the TEXTJOIN and VLOOKUP functions, with a defined translation table to provide the necessary lookups. In the example shown, the formula in C5 is:

    {=TEXTJOIN("",1,VLOOKUP(T(IF(1,MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1))),xtable,2,0))}
    

where "xtable" is the [named range](https://exceljet.net/glossary/named-range)
 E5:F10.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Generic formula
---------------

    {=TEXTJOIN("",1,VLOOKUP(T(IF(1,MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1))),xtable,2,0))}

Explanation 
------------

At the core, this formula uses an array operation to generate an [array](https://exceljet.net/glossary/array)
 of letters from the input text, translates each letter individually to a number, then joins all numbers together again and returns the output as a string.

To parse the input string into an array or letters, we use MID, ROW, LEN and INDIRECT functions like this:

    MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1)
    

LEN returns the length of the input text, which is concatenated to "1:" and handed off to INDIRECT as text. INDIRECT evaluates the text as a row reference, and the ROW function returns an array of numbers to MID:

    MID(B5,{1;2;3},1)
    

MID then extracts one character for at each starting position and we have:

    =TEXTJOIN("",1,VLOOKUP(T(IF(1,{"a";"b";"c"})),xtable,2,0))
    

Essentially, we are asking VLOOKUP to find a match for "a", "b", and "c" at the same time. [For obscure reasons](https://excelxor.com/2014/09/05/index-returning-an-array-of-values/)
, we need to "dereference" this array in a particular way using both the T and IF functions. After VLOOKUP runs, we have:

    =TEXTJOIN("",1,{9;4;6})
    

and TEXTJOIN returns the string "946".

### Output a number

To output a number as final result (instead of a string), add zero. The math operation will coerce the string into a number.

### Sum numbers

To sum the numbers together instead of listing them, you can replace TEXTJOIN with SUM like this:

    =SUM(VLOOKUP(T(IF(1,MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1))),xtable,2,0))
    

_Note: the TEXTJOIN function was introduced via the Office 365 subscription program in 2018._

Related formulas
----------------

[![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")](https://exceljet.net/formulas/abbreviate-names-or-words)

### [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article...

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

[![Excel formula: Strip html from text or numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20html%20from%20text%20or%20numbers.png "Excel formula: Strip html from text or numbers")](https://exceljet.net/formulas/strip-html-from-text-or-numbers)

### [Strip html from text or numbers](https://exceljet.net/formulas/strip-html-from-text-or-numbers)

The MID function returns characters using a fixed starting point and ending point. In this case, the markup consists of the html bold tag, which appears at the start of each cell and the associated closing tag, which appears at the end. The MID function has been configured to always start at 4,...

[![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

### [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

Excel doesn't have a way to cast the letters in a text string to an array directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is: =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(...

[![Excel formula: Sum text values like numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20text%20values%20like%20numbers.png "Excel formula: Sum text values like numbers")](https://exceljet.net/formulas/sum-text-values-like-numbers)

### [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)

The heart of this formula is a basic INDEX and MATCH formula, used to translate text values into numbers as defined in a lookup table. For example, to translate "EX" to the corresponding number, we would use: =INDEX(value,MATCH("EX",code,0)) which would return 4. The twist in this problem however...

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel T function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20t%20function.png "Excel T function")](https://exceljet.net/functions/t-function)

### [T Function](https://exceljet.net/functions/t-function)

The Excel T function returns text when given a text value and an empty string ("") for numbers, dates, and the logical values TRUE and FALSE. You can use the T function to remove values that are not text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    
*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [Strip html from text or numbers](https://exceljet.net/formulas/strip-html-from-text-or-numbers)
    
*   [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    
*   [Sum text values like numbers](https://exceljet.net/formulas/sum-text-values-like-numbers)
    

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [T Function](https://exceljet.net/functions/t-function)
    

### Articles

*   [CONCAT & TEXTJOIN](https://exceljet.net/articles/concat-textjoin)
    

### Links

*   [Get initials from name (Chandoo)](https://chandoo.org/wp/2008/09/02/get-initials-from-name-excel-formula/)
    

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