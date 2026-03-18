# Clean and reformat telephone numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/clean-and-reformat-telephone-numbers

---

[Skip to main content](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#main-content)

[](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#)

*   [Previous](https://exceljet.net/formulas/cell-equals-one-of-many-things)
    
*   [Next](https://exceljet.net/formulas/compare-two-strings)
    

[Text](https://exceljet.net/formulas#Text)

Clean and reformat telephone numbers
====================================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8116/download?token=6fuiZwnT)
 (24.67 KB)

![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")

Summary
-------

To clean up telephone numbers with inconsistent formatting, you can use a formula based on TEXTSPLIT and TEXTJOIN. In the worksheet shown, the formula in cell D5 is:

    =TEXTJOIN("",1,TEXTSPLIT(B5,{"(",")","-"," ","."},,1))+0

As the formula is copied down, it removes spaces, dashes, periods, and parentheses and returns a single numeric value. In cell F5, Excel's built-in telephone [Phone Number format](https://exceljet.net/articles/custom-number-formats)
 has been applied to display the numbers in a format common in the US. Alternatively, you can concatenate values manually as explained below.

_Note: TEXTSPLIT is only available in Excel 365. See below for an alternative formula that will work in older versions of Excel._

Generic formula
---------------

    =TEXTJOIN("",1,TEXTSPLIT(A1,{"(",")","-"," ","."},,1))

Explanation 
------------

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are removed, we can use Excel's [number format system](https://exceljet.net/articles/custom-number-formats)
 to format the numbers consistently. In the worksheet shown, the formula used to learn the numbers looks like this:

    =TEXTJOIN("",1,TEXTSPLIT(B5,{"(",")","-"," ","."},,1))+0

### Table of contents

*   [Removing extra characters](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#removing-extra-characters)
    
*   [Joining the numbers with punctuation](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#joining-the-numbers-with-punctuation)
    
*   [Creating a single numeric value](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#creating-a-single-numeric-value)
    
*   [Applying number formatting with Format Cells](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#applying-number-formatting-with-format-cells)
    
*   [Applying number formatting with the TEXT function](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#applying-number-formatting-with-text-function)
    
*   [All in one spill formula with the BYROW function](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#all-in-one-spill-formula-with-byrow-function)
    
*   [Formula for older versions of Excel](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#formula-for-older-versions-of-excel)
    
*   [Line wrap trick for better readability](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#line-wrap-trick-for-better-readability)
    

### Removing extra characters

The first task is to remove the extra characters in the raw telephone numbers. These include the right and left parentheses "()", dashes or hyphens "-", space characters " ", and periods ".". The traditional approach to removing more than one value in an Excel formula is to nest together multiple SUBSTITUTE functions (see details below). However, since we have a limited number of characters to remove, a clever approach in this case is to use the TEXTSPLIT function like this:

    TEXTSPLIT(B5,{"(",")","-"," ","."},,1)

Where the inputs to TEXTSPLIT are as follows:

*   _text_ - the text in cell B5
*   _col\_delimiter_ - the array constant {"(",")","-"," ","."}
*   _row\_delimiter_ - omitted
*   _ignore\_empty_ - 1 (same as TRUE)

The key in this formula is the [array constant](https://exceljet.net/glossary/array-constant)
 with five values. Essentially, we are asking TEXTSPLIT to split the text at each parenthesis, dash, space, and period. We are also asking TEXTSPLIT to ignore any empty values that are generated. This is important because some of these delimiters have no actual value between them. The result is that the original telephone numbers are neatly split into three parts, and all five delimiters have been removed:

![The result with TEXTSPLIT only and five delimiters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/clean_and_reformat_telephone_numbers_TEXTSPLIT_only.png "The result with TEXTSPLIT only and five delimiters")

> What's interesting about this (to me at least) is that when you use TEXTSPLIT to split text with different delimiters, the delimiters themselves are _discarded in the process_. This makes TEXTSPLIT an interesting way to remove multiple characters at the same time. The only drawback is that you have to combine the split text again, which is why we have TEXTJOIN in there as well. The [CONCAT function](https://exceljet.net/functions/concat-function)
>  would work equally well to join the numbers.

_Note: if you have a lot of characters to remove, you can use a different formula to_ [_strip all non-numeric values at once_](https://exceljet.net/formulas/strip-non-numeric-characters)
_, without calling out individual characters._

### Joining the numbers with punctuation

To create a final formatted result, one approach is to use manual [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
 to join the numbers together using the exact syntax you prefer. For example, in the screen below, the formula in cell H5 is:

    ="("&D5&") "&E5&" -"&F5

![Using manual concatenation to join numbers and punctuation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/clean_and_reformat_telephone_numbers_manual_concatenation.png "Using manual concatenation to join numbers and punctuation")

The key benefit of this approach is total control over the final result. You can insert specific characters with any logic you like. However, in the original worksheet shown above, we take a different approach: we create a single number, and then apply number formatting.

### Creating a single numeric value

After the TEXTSPLIT splits the numbers and removes delimiters, the resulting array is returned to the TEXTJOIN function like this:

    =TEXTJOIN("",1,{"801","456","8765"})+0

Because we have provided an empty string as the delimiter, the result from TEXTJOIN is a single text string like this:

    ="8014568765"+0

We then add zero to force Excel to convert the text value to the number 8014568765. Note: leading zeros will be removed when the value is converted to a number. If you need leading zeros, the simplest approach will be to concatenate manually as explained previously. There are pros and cons to both approaches.

### Applying number formatting with Format Cells

The final step in this problem is to apply Excel's built-in telephone number format. To show this as a separate step, the worksheet below just pulls the value from column D into column F:

![The formula used in column F simply copies column D](https://exceljet.net/sites/default/files/images/formulas/inline/clean_and_reformat_telephone_numbers_final_formula.png "The formula used in column F simply copies column D")

Next, select the range F5:F16 and use the [keyboard shortcut](https://exceljet.net/shortcuts)
 Control + 1 to open the Format Cells window. Then apply the "Phone Number" format:

![Applying the Phone Number format in Format Cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/clean_and_reformat_telephone_numbers_number_format.png "Applying the Phone Number format in Format Cells")

### Applying number formatting with the TEXT function

Another good way to apply number formatting is to use the [TEXT function](https://exceljet.net/functions/text-function)
 with a custom number format like this:

    TEXT(A1,"(000) 000-0000")

The result from TEXT will be a text string with the number in a format like (877) 437-8365.

### All-in-one spill formula with the BYROW function

Matt Hanchett, a super smart subscriber to the Exceljet newsletter, emailed me to suggest this cool all-in-one dynamic array formula that will [spill](https://exceljet.net/glossary/spill)
 all cleaned and formatted numbers in one step:

    =LET(
    phoneList,B5:B16,
    cleanList,BYROW(phoneList,LAMBDA(n,LET(chars,MID(n,SEQUENCE(LEN(n)),1),CONCAT(FILTER(chars,ISNUMBER(chars+0)))))),
    validLen,IFERROR(LEN(cleanList),0)=10,
    return,IF(validLen,TEXT(cleanList,"(000) 000-0000"),"Missing or invalid number."),
    return
    )

Unlike the original formula, which removes specific punctuation, this formula uses the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [CONCAT function](https://exceljet.net/functions/concat-function)
 to [strip all non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
. This code is packaged in a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 called by the [BYROW function](https://exceljet.net/functions/byrow-function)
, which iterates through all phone numbers one row at a time. It also features a nice error-checking step to confirm a 10-digit number and bail out with a friendly message when a number is not 10 digits. Note the definition of the "validLen" variable in the code above and how it is used in the next line.

### Formula for older versions of Excel

Older versions of Excel do not provide the TEXTJOIN or TEXTSPLIT function, so we need a different formula. One traditional approach is to nest multiple SUBSTITUTE functions in a single formula like this:

    =SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(B5,"(",""),")",""),"-","")," ",""),".","")+0

The formula runs from the inside out, with each SUBSTITUTE removing one character. The innermost SUBSTITUTE removes the left parentheses, and the result is handed to the next SUBSTITUTE, which removes the right parentheses, and so on. The workbook below shows the formula in action:

![Cleaning phone numbers with nested SUBSTITUTE functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/clean_and_reformat_telephone_numbers_with_substitute_function.png "Cleaning phone numbers with nested SUBSTITUTE functions")

Whenever you use the SUBSTITUTE function, the result will be text. Because you can't apply a number format to text, we need to convert the text to a number. One way to do that is to add zero (+0), which automatically converts numbers in text format to numbers in numeric format. Finally, the "Special" telephone number format is applied to column D as explained above.

This page [explains custom number formats](https://exceljet.net/articles/custom-number-formats)
 with many examples.

### Line wrap trick for better readability

When nesting multiple functions, it can be difficult to read the formula and keep all parentheses balanced. Excel doesn't care about extra white space in a formula, so you can [add line breaks in the formula](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 to make the formula more readable. For example, the formula above can be written as follows:

    =
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    SUBSTITUTE(
    A1,
    "(",""),
    ")",""),
    "-",""),
    " ",""),
    ".","")
    

Note that the cell appears in the middle, with function names above and substitutions below. Not only does this make the formula easier to read, but it also makes it easier to add and remove substitutions. You can use this same trick to [make nested IF statements easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
 as well.

Related formulas
----------------

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Remove text by matching](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20text%20by%20matching.png "Excel formula: Remove text by matching")](https://exceljet.net/formulas/remove-text-by-matching)

### [Remove text by matching](https://exceljet.net/formulas/remove-text-by-matching)

The SUBSTITUTE function lets you replace text by matching content. In this case, we want to remove hyphens from telephone numbers. The SUBSTITUTE function can handle this easily — we just need to provide a cell reference (B6), the text to remove ("-"), and the an empty string ("") for replacement...

[![Excel formula: Remove unwanted characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20unwanted%20characters.png "Excel formula: Remove unwanted characters")](https://exceljet.net/formulas/remove-unwanted-characters)

### [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)

The SUBSTITUTE function can find and replace text in a cell, wherever it occurs. In this case, we are using SUBSTITUTE to find a character with code number 202, and replace it with an empty string (""), which effectively removes the character completely. How can you figure out which character(s)...

[![Excel formula: Find and replace multiple values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find-and-replace-multiple-values.png "Excel formula: Find and replace multiple values")](https://exceljet.net/formulas/find-and-replace-multiple-values)

### [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)

There is no built-in function to perform a series of find and replace operations in Excel, but you can create a formula that does the same thing. The goal in this example is to replace multiple ("find") values with corresponding ("replace") values in a single "replace all" operation. The text...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20make%20a%20nested%20IF%20formula%20easier%20to%20read.png)](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

### [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

In this video we're going to look at how to make a nested IF formula more readable by adding line breaks. Here I have a worksheet that calculates sales commissions based on the commission structure shown in the table. For example, we can see that King sold $124,500 and gets a commission of 5%,...

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
    
*   [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    
*   [Remove text by matching](https://exceljet.net/formulas/remove-text-by-matching)
    
*   [Remove unwanted characters](https://exceljet.net/formulas/remove-unwanted-characters)
    
*   [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

### Videos

*   [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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