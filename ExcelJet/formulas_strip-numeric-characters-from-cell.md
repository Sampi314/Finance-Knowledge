# Strip numeric characters from cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/strip-numeric-characters-from-cell

---

[Skip to main content](https://exceljet.net/formulas/strip-numeric-characters-from-cell#main-content)

[](https://exceljet.net/formulas/strip-numeric-characters-from-cell#)

*   [Previous](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [Next](https://exceljet.net/formulas/translate-letters-to-numbers)
    

[Text](https://exceljet.net/formulas#Text)

Strip numeric characters from cell
==================================

by Dave Bruns · Updated 13 Apr 2021

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[MID](https://exceljet.net/functions/mid-function)

[ROW](https://exceljet.net/functions/row-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[LET](https://exceljet.net/functions/let-function)

![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")

Summary
-------

To remove numeric characters from a text string, you can use a formula based on the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. In the example shown, the formula in C5 is:

    =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(INDIRECT("1:100")),1)+0),MID(B5,ROW(INDIRECT("1:100")),1),""))
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Generic formula
---------------

    {=TEXTJOIN("",TRUE,IF(ISERR(MID(A1,ROW(INDIRECT("1:100")),1)+0),MID(A1,ROW(INDIRECT("1:100")),1),""))}

Explanation 
------------

Excel doesn't have a way to cast the letters in a text string to an [array](https://exceljet.net/glossary/array)
 directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is:

    =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(INDIRECT("1:100")),1)+0),MID(B5,ROW(INDIRECT("1:100")),1),""))
    

This looks pretty complicated but the gist is that we create an [array](https://exceljet.net/glossary/array)
 of all characters in B5, and test each character to see if it's a number. If so, we discard the value and replace it with an [empty string](https://exceljet.net/glossary/empty-string)
 (""). If not, we add the non-numeric character to a "processed" array. Finally, we use the TEXTJOIN function (new in Excel 2019) to concatenate all characters together, ignoring empty values.

Working from the inside out, the [MID function](https://exceljet.net/functions/mid-function)
 is used to extract the text in B5, one character at a time. The key is the [ROW](https://exceljet.net/functions/row-function)
 and [INDIRECT](https://exceljet.net/functions/indirect-function)
 snippet here:

    ROW(INDIRECT("1:100"))
    

which spins up an array containing 100 numbers like this:

{1,2,3,4,5,6,7,8....99,100}

_Note: 100 represents the maximum characters to process. Change to suit your data, or use the LEN function as explained below._

This array goes into the MID function as the **start\_num** argument. For **num\_chars**, we use 1.

The MID function returns an array like this:

    {"3";"4";"6";"5";"3";" ";"J";"i";"m";" ";"M";"c";"D";"o";"n";"a";"l";"d";"";"";"";...}
    

_Note: extra items in the array removed for readability._

To this array, we add zero. This is a simple trick that forces Excel to coerce text to a number. Numeric text values like "1","2","3","4" etc. are converted without errors, but non-numeric values will fail and throw a #VALUE error. We use the [IF function](https://exceljet.net/functions/if-function)
 with the [ISERR function](https://exceljet.net/functions/iserr-function)
 to catch these errors. When we see an error, we know we have a non-numeric character, so we bring that character into the processed [array](https://exceljet.net/glossary/array)
 with another MID function:

    MID(B5,ROW(INDIRECT("1:100")),1)
    

If _don't_ get an error, we know we have a number, so we insert an empty string ("") into the array in place of the number.

The final array result goes into the TEXTJOIN function as the _text1_ argument. For _delimiter_, we use an empty string ("") and for _ignore\_empty_ we supply TRUE. TEXTJOIN then [concatenates](https://exceljet.net/glossary/concatenation)
 all non-empty values in the array and returns the result.

### Precise array length

Instead of hardcoding a number like 100 into INDIRECT, you can use the [LEN function](https://exceljet.net/functions/len-function)
 to build an array with the actual number of characters in the cell like this:

    MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1)
    

LEN returns the count of characters in the cell as a number, which is used instead of 100. This allows the formula to scale up to any number of characters automatically.

### Removing extra space

When you strip numeric characters, you may have extra space characters left over. To strip leading and trailing spaces, and normalize spaces between words, you can wrap the formula shown on this page inside the [TRIM function](https://exceljet.net/functions/trim-function)
:

    =TRIM(formula)
    

### With SEQUENCE

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the new [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 can replace the ROW + INDIRECT code above:

    =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,SEQUENCE(LEN(B5)),1)+0),MID(B5,SEQUENCE(LEN(B5)),1),""))
    

Here, we use SEQUENCE + LEN to build an array of the correct length in one step.

### With LET

We can further streamline this formula with the [LET function](https://exceljet.net/functions/let-function)
. Because the array is created twice above with SEQUENCE and LEN, we can define array as a variable, and create it just once:

    =LET(array,SEQUENCE(LEN(B5)),TEXTJOIN("",TRUE,IF(ISERR(MID(B5,array,1)+0),MID(B5,array,1),"")))
    

Here value of **array** is set just once, then used twice inside the MID function.

### Strip non-numeric characters

You can use a [similar formula to remove non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
.

Related formulas
----------------

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

[![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")](https://exceljet.net/formulas/abbreviate-names-or-words)

### [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article...

[![Excel formula: LAMBDA strip characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20strip%20characters.png "Excel formula: LAMBDA strip characters")](https://exceljet.net/formulas/lambda-strip-characters)

### [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)

This is an experimental formula to strip characters from text. The experimental part is using character codes instead of regular characters as a way to make the formula case-sensitive, and providing a way to reverse the logic of the formula with the "keep" input parameter. Unlike the formula...

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [Strip html from text or numbers](https://exceljet.net/formulas/strip-html-from-text-or-numbers)
    
*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    
*   [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)
    

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    

### Articles

*   [CONCAT & TEXTJOIN](https://exceljet.net/articles/concat-textjoin)
    

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