# Abbreviate names or words - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/abbreviate-names-or-words

---

[Skip to main content](https://exceljet.net/formulas/abbreviate-names-or-words#main-content)

[](https://exceljet.net/formulas/abbreviate-names-or-words#)

*   [Previous](https://exceljet.net/formulas/10-most-common-text-values)
    
*   [Next](https://exceljet.net/formulas/add-a-line-break-with-a-formula)
    

[Text](https://exceljet.net/formulas#Text)

Abbreviate names or words
=========================

by Dave Bruns · Updated 16 Nov 2023

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[FILTER](https://exceljet.net/functions/filter-function)

[MID](https://exceljet.net/functions/mid-function)

[CODE](https://exceljet.net/functions/code-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")

Summary
-------

To abbreviate text using words that begin with capital letters, you can use a formula based on the TEXTSPLIT and TEXTJOIN functions. In the example shown, the formula in cell D5 is:

    =LET(
    text,B5,
    chars,LEFT(TEXTSPLIT(text," ")),
    codes,CODE(chars),
    capitals,FILTER(chars,(codes>=65)*(codes<=90)),
    TEXTJOIN("",1,capitals)
    )

As the formula is copied down, it builds an abbreviation using the first letter of words that begin with a capital letter. You can use this approach to create initials from names, or create acronyms from general text. Only capital letters will survive this formula, so the source text must include capitalized words. You can use the [PROPER function](https://exceljet.net/functions/proper-function)
 to capitalize words if needed.

_Note: the article below provides a more complex formula that will work in Excel 2019._

Generic formula
---------------

    =LET(
    text,A1,
    chars,LEFT(TEXTSPLIT(text," ")),
    codes,CODE(chars),
    capitals,FILTER(chars,(codes>=65)*(codes<=90)),
    TEXTJOIN("",1,capitals)
    )

Explanation 
------------

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article below explains 3 ways to do this. The first two methods require a current version of Excel. The last (and more complex method) is an array formula that will work in Excel 2019.

### Modern formula #1

In the worksheet shown, the formula in cell D5 looks like this:

    =LET(
    text,B5,
    chars,LEFT(TEXTSPLIT(text," ")),
    codes,CODE(chars),
    capitals,FILTER(chars,(codes>=65)*(codes<=90)),
    TEXTJOIN("",1,capitals)
    )

In brief, this formula splits the text in cell B5 into words, extracts the first letter of each word, removes all but the capital letters, and concatenates the result into a single string. The details work like this:

First, we use the [LET Function](https://exceljet.net/functions/let-function)
 to define four named variables (**text**, **chars**, **codes**, **capitals**) to make the formula easier to read and modify, as well as more efficient. The **text** variable is assigned the value in cell B5, and serves as the source text from which the capital letters will be extracted. Next, we assign a value to **chars** with this code:

    LEFT(TEXTSPLIT(text," "))

The [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 splits the text into an [array](https://exceljet.net/glossary/array)
 of words using spaces (" ") as the _delimiter_. Next, the [LEFT function](https://exceljet.net/functions/left-function)
 extracts the first character from each word in the array created by TEXTSPLIT. The final result is an array of the first letters of each word.

Next, we create a value for **codes** using the [CODE function](https://exceljet.net/functions/code-function)
:

    CODE(chars)

Here, CODE returns a numeric [ASCII value](https://exceljet.net/glossary/ascii)
 for each character in the **chars** array. The result is an array of ASCII numbers. We now have what we need to isolate capital letters only. This is done with the [FILTER function](https://exceljet.net/functions/filter-function)
:

    FILTER(chars,(codes>=65)*(codes<=90))

The FILTER function filters the **chars** array to include only those characters whose codes are between 65 and 90, which correspond to the uppercase letters (A-Z) in ASCII. The result from FILTER is an array that contains only the capital letters that appear at the beginning of a word. This array is the value assigned to the variable **capitals.**

Finally, the formula concatenates the capital letters in **capitals** into a single text string using the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. The _delimiter_ is set to an empty string (""), so no additional characters are inserted. The _ignore\_empty_ argument is given as 1 so that TEXTJOIN will ignore any empty values in the **capitals** array.

### Modern formula #2

The formula below shows another way to solve this problem in a modern version of Excel:

    =LET(
    text,B5,
    chars,MID(text,SEQUENCE(LEN(text)),1),
    codes,CODE(chars),
    capitals,FILTER(chars,(codes>= 65)*(codes<= 90)),
    TEXTJOIN("",1,capitals)
    )

As above, the LET function is used to declare variables, which are the same four as above: **text**, **chars**, **codes**, and **capitals**. The value for **text** comes from cell B5, and serves as the source text for the formula. The value for **chars** is defined by the following snippet:

    MID(text,SEQUENCE(LEN(text)),1)

This is a fairly common method in more advanced Excel formulas to [convert a text string to an array of characters](https://exceljet.net/formulas/split-text-string-to-character-array)
. The result is an array of every character in the source text. Next, we use the FILTER function to preserve only capital letters as before:

    FILTER(chars,(codes>= 65)*(codes<= 90))

The resulting array contains all the capital letters in **text.** Finally, we use the TEXTJOIN function to join the letters together:

    TEXTJOIN("",1,capitals)

The main thing to note in this approach is that we don't bother with words, we simply collect and filter _all the characters in the source text_. That means a capital letter _in any location_ will survive and appear in the final result.

### Legacy Excel solution

_The formulas above work well and I recommend you use them in a current version of Excel. I leave the example below mainly as a historical reminder of the state of Excel formulas not so long ago. Solving problems like this used to require insanely complex formulas because many key functions (i.e. TEXTSPLIT, FILTER, SEQUENCE, UNIQUE, SORT, etc.) were not available. As a result, the workarounds were ridiculously complicated._

Older versions of Excel do not contain TEXTSPLIT or FILTER. However, if you have Excel 2019, you have the TEXTJOIN function which can be used to solve this problem with a much more complex formula like this:

    =TEXTJOIN("",1,IF(ISNUMBER(MATCH(CODE(MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1)),ROW(INDIRECT("65:90")),0)),MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1),""))

_Note: this is a traditional [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter._

Working from the inside out, the MID function is used to cast the string into an array of individual letters:

    MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1)
    

In this part of the formula, [MID](https://exceljet.net/functions/mid-function)
, [ROW](https://exceljet.net/functions/row-function)
, [INDIRECT](https://exceljet.net/functions/indirect-function)
, and [LEN](https://exceljet.net/functions/len-function)
 are used to convert a string to an array of letters, [as described here](https://exceljet.net/formulas/convert-string-to-array)
. MID returns an array of all characters in the text.

    {"W";"i";"l";"l";"i";"a";"m";" ";"S";"h";"a";"k";"e";"s";"p";"e";"a";"r";"e"}

This array is fed into the [CODE function](https://exceljet.net/functions/code-function)
, which outputs an array of numeric ASCII codes, one for each letter. Separately, ROW and INDIRECT are used to create another numeric array:

    ROW(INDIRECT("65:90")
    

This is the clever bit. The numbers 65 to 90 correspond to the [ASCII codes](https://exceljet.net/glossary/ascii)
 for all capital letters between A-Z. This array goes into the [MATCH function](https://exceljet.net/functions/match-function)
 as the lookup array, and the original array of ASCII codes is provided as the lookup value.

MATCH then returns either a number (based on a position) or the #N/A error. Numbers represent capital letters, so the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 function is used together with the [IF function](https://exceljet.net/functions/if-function)
 to filter results. Only characters whose ASCII code is between 65 and 90 will make it into the final array, which is then reassembled with the TEXTJOIN function to create the final abbreviation or acronym.

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

[![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

### [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

Excel doesn't have a way to cast the letters in a text string to an array directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is: =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel CODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20code%20function.png "Excel CODE function")](https://exceljet.net/functions/code-function)

### [CODE Function](https://exceljet.net/functions/code-function)

The Excel CODE function returns a numeric code for a given character.  For example, CODE("a") returns the code 97....

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20CHAR%20and%20CODE%20functions-thumb.png)](https://exceljet.net/videos/how-to-use-char-and-code-functions)

### [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)

Each character you see displayed in Excel has a number. Excel has two functions that work with these numbers directly: CODE and CHAR (Character). Let's look first at the CODE function . The CODE function accepts one argument, which is the text for which you'd like a numeric code. If I use CODE with...

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
    
*   [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [CODE Function](https://exceljet.net/functions/code-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

### Videos

*   [How to use CHAR and CODE functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)
    

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