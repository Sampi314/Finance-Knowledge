# Excel LEN function | Exceljet

**Source:** https://exceljet.net/functions/len-function

---

[Skip to main content](https://exceljet.net/functions/len-function#main-content)

[](https://exceljet.net/functions/len-function#)

*   [Previous](https://exceljet.net/functions/left-function)
    
*   [Next](https://exceljet.net/functions/lower-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

LEN Function
============

by Dave Bruns · Updated 8 Jan 2025

Related functions 
------------------

[RIGHT](https://exceljet.net/functions/right-function)

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

![Excel LEN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")

Summary
-------

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

Purpose 
--------

Get the length of text.

Return value 
-------------

Number of characters

Syntax
------

    =LEN(text)

*   _text_ - The text for which to calculate length.

Using the LEN function 
-----------------------

The LEN function returns the number of characters in a given text string. LEN takes just one argument, _text_. LEN counts the number of characters in _text_, including space and punctuation, and returns a number as the result. If _text_ is an [empty string](https://exceljet.net/glossary/empty-string)
 ("") or text is a reference to an empty cell, LEN returns zero. LEN will also count characters in numbers, but number formatting is not included.

### Examples

LEN returns the count of characters in a text string:

    =LEN("apple") // returns 5
    

Space characters are included in the count:

    =LEN("apple ") // returns 6
    

LEN also works with numeric values, but number formatting is not included:

    =LEN(1000) // returns 4
    =LEN($1,000) // returns 4
    

The LEN function often appears in other formulas that manipulate text in some way. For example, it can be used with the [RIGHT](https://exceljet.net/functions/right-function)
 and [FIND](https://exceljet.net/functions/find-function)
 functions to extract text to the right of a given character:

    =RIGHT(A1,LEN(A1)-FIND(char,A1)) // get text to right of char
    

FIND returns the position of the character, which is subtracted from length, calculated with LEN. RIGHT returns the text to the _right_ of that position.  [Full explanation here](https://exceljet.net/formulas/split-text-string-at-specific-character)
.

### Notes

*   LEN returns the length of text as a number.
*   LEN works with numbers, but number formatting is not included.
*   LEN returns zero if a value is empty.

### Technical Notes

For some characters, the LEN function returns the number of UTF-16 code units used to encode the string rather than the number of user-perceived characters. For example, given the character 🙂 (U+1F642) as input, the LEN function returns two.

    =LEN("🙂") // returns 2

Characters in the Basic Multilingual Plane (U+0000 to U+FFFF), like basic letters (A-Z) and symbols like π (U+03C0) and ✓ (U+2713), are encoded with one code unit. For these characters, the LEN function returns a length of one.

    =LEN("π") // returns 1

Supplementary characters beyond the BMP (Basic Multilingual Plane), such as emoji, require 2 code units in UTF-16. For these characters, the LEN function returns a length of two. The behavior of the LEN function is different from the [LEFT](https://exceljet.net/functions/left-function)
 and [RIGHT](https://exceljet.net/functions/right-function)
 functions, which expect the number of characters (**code points**) as input as opposed to **code units**, which LEN returns.

    =LEFT("😊😐🙁",1) // returns 😊
    =RIGHT("😊😐🙁",2) // returns 😐🙁

LEN function examples
---------------------

[![Excel formula: Count specific words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_words_in_range.png "Excel formula: Count specific words in a range")](https://exceljet.net/formulas/count-specific-words-in-a-range)

### [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)

In the generic version of the formula, rng represents the range to check, and txt is the word or substring to count. In the example shown, B5:B8 is the range to check, and C2 contains the text (word or substring) to count. For each cell in the range, SUBSTITUTE removes the substring from the...

[![Excel formula: Remove last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20last%20word.png "Excel formula: Remove last word")](https://exceljet.net/formulas/remove-last-word)

### [Remove last word](https://exceljet.net/formulas/remove-last-word)

In this example, the goal is to remove the last word from the text strings in column B. This article explains two approaches: A modern formula based on the TEXTBEFORE function. A more traditional formula for older versions in Excel. The first option is much simpler, and you should use it if you...

[![Excel formula: LAMBDA count words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20count%20words.png "Excel formula: LAMBDA count words")](https://exceljet.net/formulas/lambda-count-words)

### [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)

The LAMBDA function can be used to create reusable, custom functions in Excel without VBA or macros. The first step in creating a LAMBDA function is to verify the formula logic needed in a standard Excel formula. In this example, the base formula is: =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(LEN(...

[![Excel formula: Get top level domain (TLD)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_top_level_domain_TLD.png "Excel formula: Get top level domain (TLD)")](https://exceljet.net/formulas/get-top-level-domain-tld)

### [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)

In this example, the goal is to extract the top-level domain (TLD) from a list of domains. A top-level domain is the last segment of text in a domain name, for example, ".com", ".net", or ".net". In the current version of Excel, the TEXTAFTER function is a simple way to solve this problem. In an...

[![Excel formula: Strip html from text or numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20html%20from%20text%20or%20numbers.png "Excel formula: Strip html from text or numbers")](https://exceljet.net/formulas/strip-html-from-text-or-numbers)

### [Strip html from text or numbers](https://exceljet.net/formulas/strip-html-from-text-or-numbers)

The MID function returns characters using a fixed starting point and ending point. In this case, the markup consists of the html bold tag, which appears at the start of each cell and the associated closing tag, which appears at the end. The MID function has been configured to always start at 4,...

[![Excel formula: Find nth occurrence of character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find%20nth%20occurrence%20of%20character.png "Excel formula: Find nth occurrence of character")](https://exceljet.net/formulas/find-nth-occurrence-of-character)

### [Find nth occurrence of character](https://exceljet.net/formulas/find-nth-occurrence-of-character)

In this example, the goal is to determine the position of the nth occurrence of a specific character (delimiter) in the text strings in column B. This article explains two approaches: A modern formula based on the TEXTBEFORE function. A more traditional formula for older versions of Excel. The...

[![Excel formula: Count line breaks in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20line%20breaks%20in%20cell.png "Excel formula: Count line breaks in cell")](https://exceljet.net/formulas/count-line-breaks-in-cell)

### [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)

First, the LEN function counts total characters in the cell B5. Next SUBSTITUTE removes all "line returns" from the text in B5 by looking for CHAR(10) which is the character code for the return character in Windows. LEN returns the result inside of a second LEN, which counts characters without...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

[![Excel formula: Count specific characters in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_specific_characters_in_range.png "Excel formula: Count specific characters in a range")](https://exceljet.net/formulas/count-specific-characters-in-a-range)

### [Count specific characters in a range](https://exceljet.net/formulas/count-specific-characters-in-a-range)

For each cell in the range, SUBSTITUTE removes all the o's from the text, then LEN calculates the length of the text without o's. This number is then subtracted from the length of the text with o's. Because we are using SUMPRODUCT, the result of all this calculation is a list of items (an array),...

[![Excel formula: Count total words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_in_range.png "Excel formula: Count total words in a range")](https://exceljet.net/formulas/count-total-words-in-a-range)

### [Count total words in a range](https://exceljet.net/formulas/count-total-words-in-a-range)

For each cell in the range, SUBSTITUTE removes all spaces from the text, then LEN calculates the length of the text without spaces. This number is then subtracted from the length of the text with spaces, and the number 1 is added to the final result, since the number of words is the number of...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: LAMBDA strip trailing characters recursive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20strip%20trailing%20characters%20recursive.png "Excel formula: LAMBDA strip trailing characters recursive")](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive)

### [LAMBDA strip trailing characters recursive](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive)

LAMBDA function can be used to create custom, reusable functions in Excel. This example illustrates a feature called recursion, in which a function calls itself. Recursion can be used to create elegant, compact, non-redundant code. This example is primarily proof of concept, to show a very simple...

[![Excel formula: Remove first character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20first%20character.png "Excel formula: Remove first character")](https://exceljet.net/formulas/remove-first-character)

### [Remove first character](https://exceljet.net/formulas/remove-first-character)

This formula uses the REPLACE function to replace the first character in a cell with an empty string (""). The arguments for REPLACE are configured as follows: old\_text is the original value from column B start\_num is hardcoded as the number 1 num\_chars comes from column C new\_text is entered as an...

LEN function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20convert%20booleans%20to%20numbers-PLay.png)](https://exceljet.net/videos/how-to-convert-booleans-to-numbers)

### [How to convert Booleans to numbers](https://exceljet.net/videos/how-to-convert-booleans-to-numbers)

In this video, we'll look at some ways you can convert TRUE and FALSE values in Excel to 1s and 0s. When working with more advanced formulas, especially array formulas, you need to know how to convert TRUE and FALSE values in Excel to their numeric equivalents, 1 and 0. This is best explained with...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20count%20characters%20with%20the%20LEN%20function-thumb.png)](https://exceljet.net/videos/how-to-count-characters-with-the-len-function)

### [How to count characters with the LEN function](https://exceljet.net/videos/how-to-count-characters-with-the-len-function)

Excel has a simple function called LEN, for length, that calculates the number of characters in a text string which is a surprisingly useful function. Let's take a look. The LEN function takes just one argument: the text you want to count. If I supply the address B5, which contains the text "Susan...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20conditional%20formatting%20to%20check%20line%20length-Thumb.png)](https://exceljet.net/videos/how-to-check-line-length-with-conditional-formatting)

### [How to check line length with conditional formatting](https://exceljet.net/videos/how-to-check-line-length-with-conditional-formatting)

How to use conditional formatting with the LEN function to highlight text that is too long. Have you ever had to check to make sure certain lines of text aren't too long? For example, maybe you need to check values being imported to a database or website that only allows a certain number of...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20REPT%20function%20to%20repeat%20things-thumb.png)](https://exceljet.net/videos/how-to-use-the-rept-function-to-repeat-things)

### [How to use the REPT function to repeat things](https://exceljet.net/videos/how-to-use-the-rept-function-to-repeat-things)

In this video we'll look at how to use the REPT function in Excel to repeat text. Excel contains a special function for repeating text named REPT which stands for "repeat." The REPT function takes two arguments: the text to repeat, and the number of times to repeat the text. So, if I enter an upper...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Dynamic%20arrays%20are%20native-PLay.png)](https://exceljet.net/videos/dynamic-arrays-are-native)

### [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)

In this video we'll look at how dynamic array behavior is native and deeply integrated in Excel. Although new dynamic array functions will get a lot of attention, it's important to understand that dynamic array behavior is native and deeply integrated. All formulas will now run on a new calculation...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20all%20in%20one%20formulas_Thumb.png)](https://exceljet.net/videos/how-to-build-all-in-one-formulas)

### [How to build all-in-one formulas](https://exceljet.net/videos/how-to-build-all-in-one-formulas)

In this video we're going to build a formula that counts the number of words in a cell. This cell has eight words in it, and we're going to build a formula step by step that gives us the number "8". We're going to use "helper" formulas to do that, and when we're finished, we'll take those helper...

Related functions
-----------------

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

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
    
*   [Validate strong password](https://exceljet.net/formulas/validate-strong-password)
    
*   [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Count numbers that begin with](https://exceljet.net/formulas/count-numbers-that-begin-with)
    
*   [Highlight blank cells](https://exceljet.net/formulas/highlight-blank-cells)
    
*   [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)
    
*   [Count specific words in a range](https://exceljet.net/formulas/count-specific-words-in-a-range)
    
*   [Pad text to equal length](https://exceljet.net/formulas/pad-text-to-equal-length)
    
*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    

### Videos

*   [How to check line length with conditional formatting](https://exceljet.net/videos/how-to-check-line-length-with-conditional-formatting)
    
*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to use the REPT function to repeat things](https://exceljet.net/videos/how-to-use-the-rept-function-to-repeat-things)
    
*   [How to count characters with the LEN function](https://exceljet.net/videos/how-to-count-characters-with-the-len-function)
    
*   [How to build all-in-one formulas](https://exceljet.net/videos/how-to-build-all-in-one-formulas)
    
*   [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)
    
*   [How to convert Booleans to numbers](https://exceljet.net/videos/how-to-convert-booleans-to-numbers)
    

### Functions

*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    

### Links

*   [Microsoft LEN function documentation](https://support.office.com/en-us/article/len-lenb-functions-29236f94-cedc-429d-affd-b5e33d2c67cb)
    

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