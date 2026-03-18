# Split text with delimiter - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-text-with-delimiter

---

[Skip to main content](https://exceljet.net/formulas/split-text-with-delimiter#main-content)

[](https://exceljet.net/formulas/split-text-with-delimiter#)

*   [Previous](https://exceljet.net/formulas/split-text-string-to-character-array)
    
*   [Next](https://exceljet.net/formulas/strip-html-from-text-or-numbers)
    

[Text](https://exceljet.net/formulas#Text)

Split text with delimiter
=========================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[TRIM](https://exceljet.net/functions/trim-function)

[MID](https://exceljet.net/functions/mid-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[REPT](https://exceljet.net/functions/rept-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")

Summary
-------

To split text at an arbitrary delimiter (comma, space, pipe, etc.) you can use a formula based on the TRIM, MID, SUBSTITUTE, REPT, and LEN functions. In the example shown, the formula in C5 is:

    =TRIM(MID(SUBSTITUTE($B5,"|",REPT(" ",LEN($B5))),(C$4-1)*LEN($B5)+1,LEN($B5)))
    

_Note: references to B5 and C4 are [mixed references](https://exceljet.net/glossary/mixed-reference)
 to allow the formula to be copied across and down._

Generic formula
---------------

    =TRIM(MID(SUBSTITUTE(A1,delim,REPT(" ",LEN(A1))),(N-1)*LEN(A1)+1,LEN(A1)))

Explanation 
------------

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space.

In this snippet, the delimiter (_delim_) is replaced with the number of spaces equal to the total length of the string:

    SUBSTITUTE(A1,delim,REPT(" ",LEN(A1)))
    

Then the formula uses the MID function to extract the nth substring. The starting point is calculated with the code below, where N represents "nth":

    (N-1)*LEN(A1)+1
    

The total number of characters extracted is equal to the length of the text string. The TRIM function then removes all extra spaces and returns just the nth string.

### Extract just one instance

Although the example is set up to extract 5 substrings from the text in column B, you can easily extract just 1 instance. For example, to extract just the 4th item (city), you could use:

    =TRIM(MID(SUBSTITUTE(B5,"|",REPT(" ",LEN(B5))),(4-1)*LEN(B5)+1,LEN(B5)))
    

### Text to Columns feature

For manual, one-off conversions, Excel has a built-in feature called "[Text to Columns](https://exceljet.net/glossary/text-to-columns)
" that can split text into cells with a delimiter of your choice. You'll find this feature on the Data tab of the ribbon in the Data Tools section.

Related formulas
----------------

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")](https://exceljet.net/formulas/get-last-word)

### [Get last word](https://exceljet.net/formulas/get-last-word)

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove any number of leading spaces. Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces: SUBSTITUTE(B6...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")](https://exceljet.net/formulas/abbreviate-names-or-words)

### [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article...

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

Related functions
-----------------

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

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

*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Get last word](https://exceljet.net/formulas/get-last-word)
    
*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    
*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    

### Functions

*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [REPT Function](https://exceljet.net/functions/rept-function)
    
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