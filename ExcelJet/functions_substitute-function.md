# Excel SUBSTITUTE function | Exceljet

**Source:** https://exceljet.net/functions/substitute-function

---

[Skip to main content](https://exceljet.net/functions/substitute-function#main-content)

[](https://exceljet.net/functions/substitute-function#)

*   [Previous](https://exceljet.net/functions/search-function)
    
*   [Next](https://exceljet.net/functions/text-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

SUBSTITUTE Function
===================

by Dave Bruns · Updated 23 Jan 2026

Related functions 
------------------

[REPLACE](https://exceljet.net/functions/replace-function)

[REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)

![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")

Summary
-------

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards.

Purpose 
--------

Replace text based on content

Return value 
-------------

The processed text

Syntax
------

    =SUBSTITUTE(text,old_text,new_text,[instance_num])

*   _text_ - The text to change.
*   _old\_text_ - The text to replace.
*   _new\_text_ - The text to replace with.
*   _instance\_num_ - \[optional\] The instance to replace. If not supplied, all instances are replaced.

Using the SUBSTITUTE function 
------------------------------

The SUBSTITUTE function is a way to perform a find‑and‑replace with a formula. Use it when you know what text you want to change, but you don’t know (or care) where it appears in a text string. By default, SUBSTITUTE will replace _all instances_ of a text string with another text string. Optionally, you can specify which _instance_ of text to replace by providing a number. To completely remove matched text (_old\_text_), enter an [empty string](https://exceljet.net/glossary/empty-string)
 ("") for the _new\_text_ argument.

### Key features

*   Replaces text by _matching_, not by _position_.
*   Will replace _all instances_ of matched text by default.
*   Use _instance\_num_ to target only the 1st, 2nd, 3rd… match.
*   _Is_ case-sensitive and _does not_ support wildcards.
*   Works in all versions of Excel.

> Because SUBSTITUTE doesn't support wildcards, it can't perform pattern matching. If you need pattern matching, see the [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
> , which brings the power of [regular expressions](https://exceljet.net/articles/regular-expressions-in-excel)
>  to Excel formulas. If you want to replace text at a specific known _position_, see the [REPLACE function](https://exceljet.net/functions/replace-function)
> .

### Table of contents

*   [Example #1 – Basic usage](https://exceljet.net/functions/substitute-function#basic_usage)
    
*   [Example #2 – Replace all](https://exceljet.net/functions/substitute-function#replace_all)
    
*   [Example #3 – Replace nth instance](https://exceljet.net/functions/substitute-function#replace_nth)
    
*   [Example #4 – Replace line breaks](https://exceljet.net/functions/substitute-function#replace_line_breaks)
    
*   [Example #5 – Remove unwanted text](https://exceljet.net/functions/substitute-function#remove_unwanted_text)
    
*   [Example #6 – Remove parentheses](https://exceljet.net/functions/substitute-function#remove_parentheses)
    
*   [Related functions](https://exceljet.net/functions/substitute-function#related_functions)
    
*   [Notes](https://exceljet.net/functions/substitute-function#notes)
    

### Example #1 - Basic usage

The SUBSTITUTE function is used to replace one text string with another using a generic syntax like this:

    =SUBSTITUTE(text,old_text,new_text,[instance_num])

Where _text_ is the value to process (typically a cell reference), _old\_text_ is the text to find, _new\_text_ is the text to replace with, and _instance\_num_ is an optional argument to target only a _specific instance_ of _old\_text_ by number. You can see how this works below. The formulas starting in cell D5 look like this:

    =SUBSTITUTE(B5,"t","b") // replace all t's with b's
    =SUBSTITUTE(B6,"t","b",1) // replace first t with b
    =SUBSTITUTE(B7,"t","b") // replace all t's with b's
    =SUBSTITUTE(B8,"cat","dog") // replace cat with dog
    =SUBSTITUTE(B9,"#","") // replace # with nothing
    =SUBSTITUTE(B10,"-",", ") // replace hyphens with commas
    

![SUBSTITUTE example - quick demo of features](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/substitute_example_-_quick_demo.png "SUBSTITUTE example - quick demo of features")

### Example #2 - Replace all

By default, the SUBSTITUTE function will replace _all instances_ of one text string with another. You can see this behavior in the worksheet below, where we use SUBSTITUTE to replace periods (.) with hyphens (-). The formula in cell D5 looks like this:

    =SUBSTITUTE(B5,".","-")

![SUBSTITUTE example - replace all periods (.) with hyphens (-)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/substitute_example_-_replace_all.png "SUBSTITUTE example - replace all periods (.) with hyphens (-)")

Notice the hyphen that already exists in cell B7 is unaffected.

### Example #3 - Replace nth instance

By default, SUBSTITUTE will replace all instances of one text string with another. The optional fourth argument, called _instance\_num,_ can be used to replace just a specific instance. You can see this in the worksheet below, where we have configured SUBSTITUTE to replace only the _second space_ with a hyphen. The formula in cell D5 copied down is:

    =SUBSTITUTE(B5," ","-",2)

![SUBSTITUTE example - replace 2nd space with a hyphen (-)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/substitute_example_-_replace_nth_instance.png "SUBSTITUTE example - replace 2nd space with a hyphen (-)")

Notice that _instance\_num_ is provided as 2 to target the _second_ space character.

### Example #4 - Replace line breaks

SUBSTITUTE can be combined with other functions to solve more difficult problems. The example below uses the SUBSTITUTE function to replace line breaks with a comma and a space. This is a tricky problem because the line breaks aren't visible. However, because line breaks in Excel are [ASCII](https://exceljet.net/glossary/ascii)
 character 10, we can use the [CHAR function](https://exceljet.net/functions/char-function)
 to inject a line break character for _old\_text_ inside SUBSTITUTE. The formula in cell D5 is:

    =SUBSTITUTE(B5,CHAR(10),", ")

![SUBSTITUTE example - replace line breaks with a comma and space](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/substitute_example_-_replace_line_breaks.png "SUBSTITUTE example - replace line breaks with a comma and space")

### Example #5 - Remove unwanted text

You can use the SUBSTITUTE function to completely remove unwanted text by providing an empty string for the _new\_text_ argument. You can see this approach below, where we use SUBSTITUTE to strip all asterisks (\*) from the numbers in column B. The formula in cell D5 looks like this:

    =SUBSTITUTE(B5:B16,"*","")+0

![SUBSTITUTE example - remove all asterisks (*) from numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/substitute_example_-_remove_unwanted_text.png "SUBSTITUTE example - remove all asterisks (*) from numbers")

Why add zero? Adding zero to the result forces Excel to convert text values to numbers when possible. You can see that it works in this case because the numbers in column D are now right-aligned. Also, notice we have provided the range B5:B16 as the _text_ argument. Because we provide 12 values, SUBSTITUTE returns 12 results that [spill](https://exceljet.net/glossary/spill)
 into the range D5:D16.

### Example #6 - Remove parentheses

SUBSTITUTE cannot replace more than one text string at a time. However, as a workaround, you can _nest_ one SUBSTITUTE function inside another. You can see an example of this approach in the worksheet below, where we use SUBSTITUTE twice in one formula to remove the parentheses from the values in column B. This requires that we perform two replacements: one for the left parentheses and one for the right parentheses. The formula in D5 looks like this:

    =SUBSTITUTE(SUBSTITUTE(B5,"(",""),")","")

![SUBSTITUTE example - remove parentheses from text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/substitute_example_-_remove_parentheses.png "SUBSTITUTE example - remove parentheses from text")

This is an example of _nesting_ one SUBSTITUTE inside another. The _inner_ SUBSTITUTE runs first, replacing the _left_ parenthesis with an empty string. The result is returned directly to the _outer_ SUBSTITUTE, which replaces the _right_ parentheses with an empty string. The final result in column D contains no parentheses.

> See a more advanced example of this approach in a formula to [normalize telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers#formula-for-older-versions-of-excel)
> .

### Related functions

Excel contains several functions that can help you find and replace text:

*   [REPLACE](https://exceljet.net/functions/replace-function)
     – Replace text by position when you know the starting point.
*   [FIND](https://exceljet.net/functions/find-function)
     / [SEARCH](https://exceljet.net/functions/search-function)
     – Find the numeric position of text.
*   [REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)
     – Pattern‑based find and replace (Excel 365 only).

### Notes

*   SUBSTITUTE replaces _old\_text_ with _new\_text_ in a text string.
*   By default, _all_ instances of _old\_text_ are replaced with _new\_text_.
*   _Instance\_num_ limits replacement to a particular instance of _old\_text_.
*   SUBSTITUTE is case-sensitive and does not support [wildcards](https://exceljet.net/glossary/wildcard)
    .
*   Use REGEXREPLACE (Excel 365) for more advanced replacement scenarios.
*   SUBSTITUTE can only perform one replacement at a time.

SUBSTITUTE function examples
----------------------------

[![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

### [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell. TRIM with CLEAN If you also need to remove line breaks from cells...

[![Excel formula: Count line breaks in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20line%20breaks%20in%20cell.png "Excel formula: Count line breaks in cell")](https://exceljet.net/formulas/count-line-breaks-in-cell)

### [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)

First, the LEN function counts total characters in the cell B5. Next SUBSTITUTE removes all "line returns" from the text in B5 by looking for CHAR(10) which is the character code for the return character in Windows. LEN returns the result inside of a second LEN, which counts characters without...

[![Excel formula: Get last line in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20line%20in%20cell.png "Excel formula: Get last line in cell")](https://exceljet.net/formulas/get-last-line-in-cell)

### [Get last line in cell](https://exceljet.net/formulas/get-last-line-in-cell)

This formula takes advantage of the fact that TRIM will remove any number of leading spaces. We look for line breaks and "flood" the text with spaces where we find one. Then we come back and grab text from the right. Working from the inside out, we use the SUBSTITUTE function to find all line...

[![Excel formula: Remove line breaks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20line%20breaks.png "Excel formula: Remove line breaks")](https://exceljet.net/formulas/remove-line-breaks)

### [Remove line breaks](https://exceljet.net/formulas/remove-line-breaks)

First, you should know that Excel contains two functions, CLEAN and TRIM, that can automatically remove line breaks and extra spaces from text. For example to strip all line breaks from a cell, you could use: =CLEAN(B5) For a quick demo of CLEAN and TRIM, watch this video . In this case, however,...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Count total words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_in_range.png "Excel formula: Count total words in a range")](https://exceljet.net/formulas/count-total-words-in-a-range)

### [Count total words in a range](https://exceljet.net/formulas/count-total-words-in-a-range)

For each cell in the range, SUBSTITUTE removes all spaces from the text, then LEN calculates the length of the text without spaces. This number is then subtracted from the length of the text with spaces, and the number 1 is added to the final result, since the number of words is the number of...

[![Excel formula: Extract word containing specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20containing%20specific%20text.png "Excel formula: Extract word containing specific text")](https://exceljet.net/formulas/extract-word-containing-specific-text)

### [Extract word containing specific text](https://exceljet.net/formulas/extract-word-containing-specific-text)

The gist: this formula "floods" the space between words in a text string with a large number of spaces, finds and extracts the substring of interest, and uses the TRIM function to clean up the mess. Working from the inside out, the original text in B5 is flooded with spaces using SUBSTITUTE:...

[![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")](https://exceljet.net/formulas/get-last-word)

### [Get last word](https://exceljet.net/formulas/get-last-word)

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove any number of leading spaces. Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces: SUBSTITUTE(B6...

[![Excel formula: Normalize text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/normalize%20text.png "Excel formula: Normalize text")](https://exceljet.net/formulas/normalize-text)

### [Normalize text](https://exceljet.net/formulas/normalize-text)

The formula shown in this example uses a series of nested SUBSTITUTE functions to strip out parentheses, hyphens, colons, semi-colons, exclamation marks, commas, and periods. The process runs from the inside out, with each SUBSTITUTE replacing one character with a single space, then handing off to...

[![Excel formula: Extract last two words from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Extract%20last%20two%20words%20from%20cell.png "Excel formula: Extract last two words from cell")](https://exceljet.net/formulas/extract-last-two-words-from-cell)

### [Extract last two words from cell](https://exceljet.net/formulas/extract-last-two-words-from-cell)

At the core, this formula uses the MID function to extract characters starting at the second to last space. The MID function takes 3 arguments: the text to work with, the starting position, and the number of characters to extract. The text comes from column B, and the number of characters can be...

[![Excel formula: Count specific words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_1.png "Excel formula: Count specific words in a cell")](https://exceljet.net/formulas/count-specific-words-in-a-cell)

### [Count specific words in a cell](https://exceljet.net/formulas/count-specific-words-in-a-cell)

B4 is the cell we're counting words in, and C4 contains the substring (word or any substring) you are counting. SUBSTITUTE removes the substring from the original text and LEN calculates the length of the text without the substring. This number is then subtracted from the length of the original...

[![Excel formula: Remove last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20last%20word.png "Excel formula: Remove last word")](https://exceljet.net/formulas/remove-last-word)

### [Remove last word](https://exceljet.net/formulas/remove-last-word)

In this example, the goal is to remove the last word from the text strings in column B. This article explains two approaches: A modern formula based on the TEXTBEFORE function. A more traditional formula for older versions in Excel. The first option is much simpler, and you should use it if you...

SUBSTITUTE function videos
--------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20all%20in%20one%20formulas_Thumb.png)](https://exceljet.net/videos/how-to-build-all-in-one-formulas)

### [How to build all-in-one formulas](https://exceljet.net/videos/how-to-build-all-in-one-formulas)

In this video we're going to build a formula that counts the number of words in a cell. This cell has eight words in it, and we're going to build a formula step by step that gives us the number "8". We're going to use "helper" formulas to do that, and when we're finished, we'll take those helper...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20count%20characters%20with%20the%20LEN%20function-thumb.png)](https://exceljet.net/videos/how-to-count-characters-with-the-len-function)

### [How to count characters with the LEN function](https://exceljet.net/videos/how-to-count-characters-with-the-len-function)

Excel has a simple function called LEN, for length, that calculates the number of characters in a text string which is a surprisingly useful function. Let's take a look. The LEN function takes just one argument: the text you want to count. If I supply the address B5, which contains the text "Susan...

Related functions
-----------------

[![Excel REPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20replace%20function.png "Excel REPLACE function")](https://exceljet.net/functions/replace-function)

### [REPLACE Function](https://exceljet.net/functions/replace-function)

The Excel REPLACE function replaces characters at a specified position in a given text string with another text string. REPLACE a good solution when the text to replace can't easily be matched, but the location is predictable.

[![Excel REGEXREPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexreplace_function.png "Excel REGEXREPLACE function")](https://exceljet.net/functions/regexreplace-function)

### [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)

The Excel REGEXREPLACE function replaces text matching a specific regex pattern in a given text string. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXREPLACE will...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count specific characters in text string](https://exceljet.net/formulas/count-specific-characters-in-text-string)
    
*   [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    
*   [Replace one character with another](https://exceljet.net/formulas/replace-one-character-with-another)
    
*   [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)
    
*   [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    
*   [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)
    
*   [Convert feet and inches to inches](https://exceljet.net/formulas/convert-feet-and-inches-to-inches)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)
    

### Videos

*   [How to count characters with the LEN function](https://exceljet.net/videos/how-to-count-characters-with-the-len-function)
    
*   [How to build all-in-one formulas](https://exceljet.net/videos/how-to-build-all-in-one-formulas)
    

### Functions

*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    
*   [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)
    

### Links

*   [Microsoft SUBSTITUTE function documentation](https://support.office.com/en-us/article/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332)
    

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