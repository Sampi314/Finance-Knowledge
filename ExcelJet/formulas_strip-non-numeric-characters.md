# Strip non-numeric characters - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/strip-non-numeric-characters

---

[Skip to main content](https://exceljet.net/formulas/strip-non-numeric-characters#main-content)

[](https://exceljet.net/formulas/strip-non-numeric-characters#)

*   [Previous](https://exceljet.net/formulas/strip-html-from-text-or-numbers)
    
*   [Next](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    

[Text](https://exceljet.net/formulas#Text)

Strip non-numeric characters
============================

by Dave Bruns · Updated 11 Jul 2025

Related functions 
------------------

[REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[ROW](https://exceljet.net/functions/row-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")

Summary
-------

To remove all non-numeric characters from a text string, you can use a formula based on the [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
. In the example shown, the formula in D5 is:

    =REGEXREPLACE(B5,"[^0-9]","")+0
    

As the formula is copied down, REGEXREPLACE removes all characters except the digits between 0-9 from the text strings in column B, when we add zero (+0) to make Excel convert the result to a numeric value.

> Note: REGEXREPLACE is available in Excel 365. For older versions of Excel, see below.

Generic formula
---------------

    =REGEXREPLACE(A1,"[^0-9]","")+0

Explanation 
------------

In this example, the goal is to strip (i.e., remove) non-numeric characters from a [text string](https://exceljet.net/glossary/text-value)
 with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into an array of characters where they could be easily processed with other functions. However, with the introduction of [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
 in late 2024, the problem became much simpler. In the article below, we look first at the REGEXEXTRACT function, then we explore more complex ways of accomplishing the same thing in older versions of Excel.

> Note: Adding zero (+0) is a trick to convert text into numbers. [Read more here](https://exceljet.net/formulas/convert-text-to-numbers)
> .

### Table of contents

*   [Excel 365](https://exceljet.net/formulas/strip-non-numeric-characters#excel-365)
    
*   [Older versions of Excel](https://exceljet.net/formulas/strip-non-numeric-characters#older-versions)
    *   [Creating an array of characters](https://exceljet.net/formulas/strip-non-numeric-characters#creating-an-array-of-characters)
        
    *   [Testing for numeric values](https://exceljet.net/formulas/strip-non-numeric-characters#testing-for-numeric-values)
        
    *   [Removing non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters#removing-non-numeric-characters)
        
    *   [Creating the final numeric value](https://exceljet.net/formulas/strip-non-numeric-characters#creating-the-final-numeric-value)
        
    *   [A better formula?](https://exceljet.net/formulas/strip-non-numeric-characters#a-better-formula)
        
    *   [Excel 2019](https://exceljet.net/formulas/strip-non-numeric-characters#excel-2019)
        
    *   [Removing numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters#strip-numeric-characters)
        

Excel 365
---------

In Excel 365, we now have formula support for [Regular Expressions](https://exceljet.net/articles/regular-expressions-in-excel)
 in the form of three new functions: REGEXTEST, REGEXEXTRACT, and REGEXREPLACE. This drastically simplifies the problem because we can easily use a regex pattern like \[^0-9\] to target non-numeric characters. One way to do this is to use the REGEXREPLACE function to match non-numeric characters and replace them with an empty string (""). This is the approach used in the worksheet shown, where the formula in D5 looks like this:

    =REGEXREPLACE(B5,"[^0-9]","")+0
    

The [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
 replaces text matching a specific regex pattern in a given text string. In this problem, we configure REGEXREPLACE as follows:

*   _text_ - the text to process (B5)
*   _pattern_ - the pattern to use when matching text (\[^0-9\])
*   _replacement_ - the text to use for replacing matches

The power of this formula comes from the pattern \[^0-9\], which can be roughly translated to "match anything that is NOT a digit from 0 to 9." The meaning breaks down like this:

*   The square brackets \[ \] create what's called a "character class" - a group of characters to match
*   The caret ^ at the beginning inside the brackets means "NOT" - it negates everything that follows
*   0-9 represents all digits from 0 to 9
*   So together, \[^0-9\] tells the regular expression engine: "Find any character that is not a digit."

When we use \[^0-9\] with the replacement text ", we are saying: "Find any character that's not a number and replace it with nothing," - which leaves only the numbers behind. It's a bit like a sieve that only lets numbers pass through while filtering out everything else.

The last step in the formula is to change the text result from REGEXREPLACE, which always returns a text string, into a proper number. In this instance, we do this by adding zero. This is a short way of forcing Excel to try and evaluate the text as a number without changing the number. The [VALUE function](https://exceljet.net/functions/value-function)
 is another way to do the same thing.

### Preserving the decimal point

If you have numbers with decimal places, you can adjust the formula as follows to also keep the period (.) character:

    =REGEXREPLACE(B5,"[^0-9.]","")+0

The only change is adding the period (.) to the pattern `[^0-9.]` inside the square brackets.

Older versions of Excel
-----------------------

In older versions of Excel, this is a harder problem to solve. The solutions described below involve [converting the text string to an array of characters](https://exceljet.net/formulas/split-text-string-to-character-array)
 and then removing non-numeric characters before joining things together again with TEXTJOIN. The screen below shows one approach:

![Removing non-numeric characters in an older version of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/strip_non-numeric_characters_older_excel_versions.png "Removing non-numeric characters in an older version of Excel")

### Creating an array of characters

Working from the inside out, the first step in this problem is to create an array of characters from the text string in column B. This is done with the snippet of code below:

    MID(B5,SEQUENCE(LEN(B5)),1)

First, the [LEN function](https://exceljet.net/functions/len-function)
 runs and returns a count of 10, since there are 10 characters in the text string "100 apples". This result is returned to the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 as the _rows_ argument:

    MID(B5,SEQUENCE(10),1)

Next, SEQUENCE generates a numeric array of the numbers 1-10, which is returned to the MID function as the _start\_num_ argument:

    MID(B5,{1;2;3;4;5;6;7;8;9;10},1)

This is the current solution for creating an array of characters in an Excel formula. In this configuration, the [MID function](https://exceljet.net/functions/mid-function)
 extracts the text in B5, one character at a time, and returns an array that looks like this:

    {"1";"0";"0";" ";"a";"p";"p";"l";"e";"s"}

We now have an array that contains all characters in cell B5. The next step is to figure out which characters are numbers. 

### Testing for numeric values

Since we have an array of characters ready to go, you might think we can just pass them into the ISNUMBER function like this:

    =ISNUMBER(array)

The problem, though, is that the numbers in the array (if any) are actually represented as text values like "1", "0", etc. If we try to use ISNUMBER like this, it will return FALSE for every character! One solution is to use a small hack to "force" Excel to convert numbers by adding zero. A math operation like this Excel to try to convert the character to a number. Adding zero to a non-numeric character like "a", will result in a #VALUE! error. However, adding zero to "1" will convert "1" to the number 1:

    ="a"+0 // returns #VALUE!
    ="1"+0 // returns 1

This is the trick used in the formula, where we add zero to the array of characters returned by the MID function:

    {"1";"0";"0";" ";"a";"p";"p";"l";"e";"s"}+0

Because the array contains 10 characters, we get back an array of 10 results like this:

    {1;0;0;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}

Notice that only the first 3 characters have survived this operation (since they are numbers), and the remaining characters are now #VALUE! errors. This is the final piece we need to remove the non-numeric characters.

### Removing non-numeric characters

The way we remove non-numeric characters in this formula is also tricky - we use the [IFERROR function](https://exceljet.net/functions/iferror-function)
 like this:

    IFERROR(MID(B5,SEQUENCE(LEN(B5)),1)+0,"")

By wrapping a formula in IFERROR, we force another result when the formula returns an error. When the formula _does not_ return an error, the result passes through IFERROR unchanged. The snippet uses this behavior to convert errors to an empty string (""). After the IFERROR function processes the array returned by MID, it returns an array like this:

    {1;0;0;"";"";"";"";"";"";""}

Notice the #VALUE! errors are now gone, replaced by empty strings. At this point, the remaining task is to assemble the remaining numbers into a final numeric value.

### Creating the final numeric value

The last step in this problem is to join the surviving numeric values into a single number. The tool we use to perform this step is the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
, which is designed to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 values in a range or array. In this formula, the result from IFERROR is returned to TEXTJOIN as the _text1_ argument like this:

    =TEXTJOIN("",TRUE,{1;0;0;"";"";"";"";"";"";""})

Notice that we provide _delimiter_ as an empty string ("") because we don't want any extra characters in the final result and we supply TRUE for _ignore\_empty_ because we don't want to include the empty strings in the final result. In this configuration, TEXTJOIN returns the three numbers in a text string like this:

    ="100"

So close! But notice we again have a text value because TEXTJOIN performs concatenation, which always results in a text string. The final step is to again add zero to force Excel to convert the text to a number:

    ="100"+0 // returns 100

_Note: if you prefer, you can use the_ [_VALUE function_](https://exceljet.net/functions/value-function)
 _instead of adding a zero to convert numbers as text values into numeric values. Adding zero is just a shortcut._

### A better formula?

After I finished documenting the formula above, upgrading it to use the SEQUENCE function, I realized that a better approach is probably to use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [LET function](https://exceljet.net/functions/let-function)
 like this:

    =LET(
    chars,MID(B5,SEQUENCE(LEN(B5)),1),
    TEXTJOIN("",1,FILTER(chars,ISNUMBER(chars+0)))+0
    )

FILTER is a more natural solution because it is designed to filter out unwanted values. The catch though is that we need to use the character array created by MID + SEQUENCE more than once, which means we should introduce the LET function for efficiency. In the formula above, we store the result from MID in a variable named "chars", then we use that variable twice inside FILTER like this:

    =FILTER(chars,ISNUMBER(chars+0))

Inside the include argument of FILTER we add zero to the array to force Excel to try to convert the characters to numbers. As explained above, chars + 0 will return an array like this:

    {1;0;0;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}

Then, the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 will return an array like this:

    {TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}

The final result from FILTER is an array that contains just the three numbers:

    {"1";"0";"0"}

We then join the numbers with TEXTJOIN and (again) force a numeric result by adding zero:

    =TEXTJOIN("",1,{"1";"0";"0"})+0
    ="100"+0
    =100

The final result is 100, the same as before. This formula is slightly more verbose than the original, but it is easier to adapt to filter characters in different ways. For example, if you want to preserve decimal points or periods (.), you could adjust the formula like this:

    =LET(
    chars,MID(D37,SEQUENCE(LEN(D37)),1),
    TEXTJOIN("",1,FILTER(chars,ISNUMBER(chars+0)+(chars=".")))+0
    )

The original formula is shorter but more cryptic and works best for the intended task only.

### Excel 2019

If you happen to be using Excel 2019, which provides the TEXTJOIN function but not the SEQUENCE function, you can use an alternative formula like this:

    =TEXTJOIN("",TRUE,IFERROR(MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1)+0,""))

_Note: In Excel 2019 this is an_ [_array formula_](https://exceljet.net/articles/what-is-an-array-formula)
 _and must be entered with control + shift + enter._

The [ROW](https://exceljet.net/functions/row-function)
 + [INDIRECT](https://exceljet.net/functions/indirect-function)
 construction is another way in older versions of Excel to create a numeric array with a variable length:

    =ROW(INDIRECT("1:"&LEN(B5))
    =ROW(INDIRECT("1:"&10))
    =ROW(INDIRECT("1:10"))
    ={1;2;3;4;5;6;7;8;9;10}

The resulting array is the same as that returned by the SEQUENCE function above. Note that INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
 that can cause performance problems so this approach should be avoided in later versions of Excel.

### Strip numeric characters

To remove _numeric_ characters from a text string use the formulas [explained here](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
.

Related formulas
----------------

[![Excel formula: Convert text to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert_text_to_numbers.png "Excel formula: Convert text to numbers")](https://exceljet.net/formulas/convert-text-to-numbers)

### [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)

In this example, the goal is to convert the text values seen in column B to the numeric values seen in column D. There are several ways to fix this problem in Excel, but this article focuses on a formula-based approach to convert text values to numbers. It also explains how to convert values in...

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

[![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

### [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

Excel doesn't have a way to cast the letters in a text string to an array directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is: =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(...

[![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")](https://exceljet.net/formulas/abbreviate-names-or-words)

### [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article...

[![Excel formula: LAMBDA strip characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20strip%20characters.png "Excel formula: LAMBDA strip characters")](https://exceljet.net/formulas/lambda-strip-characters)

### [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)

This is an experimental formula to strip characters from text. The experimental part is using character codes instead of regular characters as a way to make the formula case-sensitive, and providing a way to reverse the logic of the formula with the "keep" input parameter. Unlike the formula...

[![Excel formula: Split text string to character array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_to_character_array_0.png "Excel formula: Split text string to character array")](https://exceljet.net/formulas/split-text-string-to-character-array)

### [Split text string to character array](https://exceljet.net/formulas/split-text-string-to-character-array)

In this example, the goal is to use a formula to split a text string into an array of characters. For example, if the text string is "Apple", the resulting array should be {"A","p","p","l","e"}. For a long time, this was quite a difficult problem that required a complicated array formula approach...

Related functions
-----------------

[![Excel REGEXREPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexreplace_function.png "Excel REGEXREPLACE function")](https://exceljet.net/functions/regexreplace-function)

### [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)

The Excel REGEXREPLACE function replaces text matching a specific regex pattern in a given text string. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXREPLACE will...

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Convert text to numbers](https://exceljet.net/formulas/convert-text-to-numbers)
    
*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    
*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    
*   [LAMBDA strip characters](https://exceljet.net/formulas/lambda-strip-characters)
    
*   [Split text string to character array](https://exceljet.net/formulas/split-text-string-to-character-array)
    

### Functions

*   [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

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