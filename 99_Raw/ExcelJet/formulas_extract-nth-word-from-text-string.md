# Extract nth word from text string - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-nth-word-from-text-string

---

[Skip to main content](https://exceljet.net/formulas/extract-nth-word-from-text-string#main-content)

[](https://exceljet.net/formulas/extract-nth-word-from-text-string#)

*   [Previous](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Next](https://exceljet.net/formulas/extract-substring)
    

[Text](https://exceljet.net/formulas#Text)

Extract nth word from text string
=================================

by Dave Bruns · Updated 10 Jan 2023

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[INDEX](https://exceljet.net/functions/index-function)

[TRIM](https://exceljet.net/functions/trim-function)

[MID](https://exceljet.net/functions/mid-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[REPT](https://exceljet.net/functions/rept-function)

[LEN](https://exceljet.net/functions/len-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7506/download?token=QM94VHlU)
 (17.3 KB)

![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")

Summary
-------

To extract the nth word in a text string, you can use a formula based on the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 and the [INDEX function](https://exceljet.net/functions/index-function)
. In the example shown, the formula in D5, copied down, is:

    =INDEX(TEXTSPLIT(B5," "),C5)
    

The result in column D is the nth word of the text in column B, where _n_ is given in column C.

_Note: The TEXTSPLIT function is new in Excel. See below for a formula that works in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

Generic formula
---------------

    =INDEX(TEXTSPLIT(text," "),n)

Explanation 
------------

In this example, the goal is to extract the nth word from the [text string](https://exceljet.net/glossary/text-value)
 given in column B. The article below explains two approaches. The first approach is based on the new [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
, which makes it very easy to split text with a custom delimiter. The second approach is a more complicated formula that works in older versions of Excel that do not provide the TEXTSPLIT function. See below for details.

### TEXTSPLIT function

The TEXTSPLIT function provides a simple way to solve this problem. As the name implies, TEXTSPLIT will split text into pieces using a custom delimiter. In the example shown, the formula in cell D5 is:

    =INDEX(TEXTSPLIT(B5," "),C5)
    

Working from the inside out, the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 is configured to split text at each space (" ") character:

    TEXTSPLIT(B5," ") // split at space
    

_Text_ comes from cell B5. The _col\_delimiter_ argument is provided as a single space (" "). The result from TEXTSPLIT is an [array](https://exceljet.net/glossary/array)
 that includes each word in the text:

    {"Better","the","devil","you","know"}
    

To retrieve the word at the nth position in this array, we use the [INDEX function](https://exceljet.net/functions/index-function)
. The array is returned directly to the [INDEX function](https://exceljet.net/functions/index-function)
 as the _array_ [argument](https://exceljet.net/glossary/function-argument)
. The _row\_num_ argument is provided as a reference to cell C5. With the number 3 in cell C5, INDEX returns the 3rd word in the array:

    =INDEX({"Better","the","devil","you","know"},3) // returns "devil"
    

The result from INDEX is the word "devil". As the formula is copied down, it returns the nth word from each text string in column B, where _n_ is provided in column C. If _n_ is changed to a different number in any row, INDEX will retrieve a new word. Note that if _n_ is greater than the number of words in a given text string, INDEX will return a #REF error.

### Removing extra space

The operation of this formula depends on there being a _single_ space between each word. If there is the possibility of more than one space between words, the formula may return incorrect results. To handle this situation, you can use the [TRIM function](https://exceljet.net/functions/trim-function)
 like this:

    =INDEX(TEXTSPLIT(TRIM(B5)," "),C5)
    

The TRIM function will remove any leading or trailing spaces from the text string in column B, and will normalize space between words as well. The resulting text is then passed into the TEXTSPLIT function as before. This ensures that the results from TEXTSPLIT will be consistent.

### Legacy Excel

If you are working in an older version of Excel without the TEXTSPLIT function, you can use a more complicated formula to extract the nth word. In the screen below the formula in D5 combines five Excel functions: [TRIM](https://exceljet.net/functions/trim-function)
, [MID](https://exceljet.net/functions/mid-function)
, [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
, [REPT](https://exceljet.net/functions/rept-function)
, and [LEN](https://exceljet.net/functions/len-function)
:

    =TRIM(MID(SUBSTITUTE(B5," ",REPT(" ",LEN(B5))), (C5-1)*LEN(B5)+1, LEN(B5)))
    

The result in column D is the nth word of the text in column B, where _n_ is given in column C:

![Alternate formula for older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/extract%20nth%20word%20from%20text%20string%20legacy.png?itok=5pbxnKcp "Alternate formula for older versions of Excel")

At the core, this formula takes a text string and "floods" it with a large number of space characters between words using [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 and [REPT](https://exceljet.net/functions/rept-function)
. Then it splits the text string between words and cleans up the result with the [TRIM function](https://exceljet.net/functions/trim-function)
. Working from the inside out, the [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
 function is used to replace all single spaces with many spaces:

    SUBSTITUTE(B5," ",REPT(" ",LEN(B5))) // replace 1 space with many
    

The [REPT function](https://exceljet.net/functions/rept-function)
 and LEN function are used to calculate the number of spaces to use:

    REPT(" ",LEN(B5)) 
    

LEN returns 25, so the REPT function returns a string of 25 spaces:

    REPT(" ",25) // returns "                         "
    

_Note: the number of spaces needs to be large enough to work in all cases. Using the LEN function to calculate the length of the original text string, and using this as the number of spaces, ensures that the formula will work even for very long words in the original text._

The result from REPT is returned directly to the SUBSTITUTE function:

    =SUBSTITUTE(B5," ","                         ") 
    

SUBSTITUTE then replaces every single space in the text from B5 with 25 spaces. You can think of the result at this point as "islands" of words floating in a sea of space :)

    ="Better                         the                         devil                         you                         know"
    

The result from SUBSTITUTE is returned directly to the MID function. The formula uses the [MID function](https://exceljet.net/functions/mid-function)
 to extract the nth word. The _start\_num_ is worked out with this snippet:

    (N-1)*LEN(B5)+1 // returns 51
    

This code is designed to calculate the correct starting point to extract text, _taking into account the fact that we've already flooded the text with extra space characters_. We are just repeating the logic used previously to calculate the number of spaces to use between words. The n-1 adjustment is needed because the extra space occurs _between_ words, i.e. the 3rd word occurs after the 2nd block of space, the 4th word occur after the 3rd block of space, etc. The length of the original text string is 25 characters and _n_ is 3, so we have:

    =(3-1)*25+1
    =2*25+1
    =51
    

The _num\_chars_ argument is provided as the original length of B5, which is 25. With this information, the MID function extracts 25 characters, beginning with character 51. The result is returned directly to the [TRIM function](https://exceljet.net/functions/trim-function)
:

    =TRIM("         devil           ")
    

TRIM strips the space and returns the final result: "devil".

### Alternate formula

It is also possible to extract the nth word from a text string in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
 with [this formula](https://exceljet.net/formulas/text-split-to-array)
, based on the [FILTERXML function](https://exceljet.net/functions/filterxml-function)
.

### Text to Columns

Don't forget that Excel has a built-in [Text to Columns](https://exceljet.net/glossary/text-to-columns)
 feature that can split text with a delimiter of your choice. If you just need to get the 3rd word from a lot of text strings, this formula may be more convenient (and dynamic), but Text to Columns is still useful in many situations.

Related formulas
----------------

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")](https://exceljet.net/formulas/get-last-word)

### [Get last word](https://exceljet.net/formulas/get-last-word)

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove any number of leading spaces. Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces: SUBSTITUTE(B6...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")](https://exceljet.net/formulas/abbreviate-names-or-words)

### [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article...

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

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
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    
*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [REPT Function](https://exceljet.net/functions/rept-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

### Links

*   [Efficient way to extract nth word from string (MrExcel forum)](http://www.mrexcel.com/forum/excel-questions/504050-efficient-way-extract-nth-word-string.html)
    

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