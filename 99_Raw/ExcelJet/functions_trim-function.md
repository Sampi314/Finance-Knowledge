# Excel TRIM function | Exceljet

**Source:** https://exceljet.net/functions/trim-function

---

[Skip to main content](https://exceljet.net/functions/trim-function#main-content)

[](https://exceljet.net/functions/trim-function#)

*   [Previous](https://exceljet.net/functions/textjoin-function)
    
*   [Next](https://exceljet.net/functions/unichar-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

TRIM Function
=============

by Dave Bruns · Updated 3 Dec 2022

Related functions 
------------------

[CLEAN](https://exceljet.net/functions/clean-function)

![Excel TRIM function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")

Summary
-------

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

Purpose 
--------

Remove extra spaces from text

Return value 
-------------

Text with extra spaces removed.

Syntax
------

    =TRIM(text)

*   _text_ - The text from which to remove extra space.

Using the TRIM function 
------------------------

The TRIM function strips extra spaces from text, leaving only a single space between words, and removing any leading or trailing space. For example:

    =TRIM("   A stitch    in time.   ")  // returns "A stitch in time."
    

The TRIM function can be used together with the CLEAN function to remove extra space and strip out other non-printing characters:

    =TRIM(CLEAN(A1)) // trim and clean
    

TRIM often appears in other more advanced text formulas. For example, the formula below will count the number of words in cell A1:

    LEN(TRIM(A1))-LEN(SUBSTITUTE(A1," ",""))+1
    

Because this formula depends on single spaces to get an accurate word count, TRIM is used to normalize space before the count is calculated. [Full description here](https://exceljet.net/formulas/count-total-words-in-a-cell)
.

### Notes

*   TRIM strips extra spaces from text, leaving only single spaces between words and no space characters at the start or end of the text.
*   TRIM is useful when cleaning up text that has come from other applications or environments.
*   TRIM only removes the ASCII space character (32) from text.
*   Unicode text often contains a non-breaking space character (160) that appears in web pages as an HTML entity. This will not be removed with TRIM. 
*   The [CLEAN function](https://exceljet.net/functions/clean-function)
     strips the first 32 non-printing characters (ASCII values 0 through 31) from text.

TRIM function examples
----------------------

[![Excel formula: Get last line in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20line%20in%20cell.png "Excel formula: Get last line in cell")](https://exceljet.net/formulas/get-last-line-in-cell)

### [Get last line in cell](https://exceljet.net/formulas/get-last-line-in-cell)

This formula takes advantage of the fact that TRIM will remove any number of leading spaces. We look for line breaks and "flood" the text with spaces where we find one. Then we come back and grab text from the right. Working from the inside out, we use the SUBSTITUTE function to find all line...

[![Excel formula: LAMBDA count words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20count%20words.png "Excel formula: LAMBDA count words")](https://exceljet.net/formulas/lambda-count-words)

### [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)

The LAMBDA function can be used to create reusable, custom functions in Excel without VBA or macros. The first step in creating a LAMBDA function is to verify the formula logic needed in a standard Excel formula. In this example, the base formula is: =LEN(TRIM(B5))-LEN(SUBSTITUTE(B5," ",""))+(LEN(...

[![Excel formula: Extract word containing specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20containing%20specific%20text.png "Excel formula: Extract word containing specific text")](https://exceljet.net/formulas/extract-word-containing-specific-text)

### [Extract word containing specific text](https://exceljet.net/formulas/extract-word-containing-specific-text)

The gist: this formula "floods" the space between words in a text string with a large number of spaces, finds and extracts the substring of interest, and uses the TRIM function to clean up the mess. Working from the inside out, the original text in B5 is flooded with spaces using SUBSTITUTE:...

[![Excel formula: Get last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20word.png "Excel formula: Get last word")](https://exceljet.net/formulas/get-last-word)

### [Get last word](https://exceljet.net/formulas/get-last-word)

This formula is an interesting example of a "brute force" approach that takes advantage of the fact that TRIM will remove any number of leading spaces. Working from the inside out, we use the SUBSTITUTE function to find all spaces in the text, and replace each space with 100 spaces: SUBSTITUTE(B6...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Sort comma separated values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort_comma_separated_values.png "Excel formula: Sort comma separated values")](https://exceljet.net/formulas/sort-comma-separated-values)

### [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)

In this example the goal is to sort the comma separated values in column B in alphabetical order. In the latest version of Excel, you can solve this problem with a formula based on TEXTSPLIT, SORT, and TEXTJOIN. In earlier versions of Excel the problem is more complicated. See below for a couple of...

[![Excel formula: Count total words in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_words_in_range.png "Excel formula: Count total words in a range")](https://exceljet.net/formulas/count-total-words-in-a-range)

### [Count total words in a range](https://exceljet.net/formulas/count-total-words-in-a-range)

For each cell in the range, SUBSTITUTE removes all spaces from the text, then LEN calculates the length of the text without spaces. This number is then subtracted from the length of the text with spaces, and the number 1 is added to the final result, since the number of words is the number of...

[![Excel formula: Count total words in a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_total_words_in_cell.png "Excel formula: Count total words in a cell")](https://exceljet.net/formulas/count-total-words-in-a-cell)

### [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)

In this example, the goal is to count the total number of words in a cell. Excel doesn't have a dedicated function for counting words. However, with a little ingenuity, you can create a formula to perform this task using a combination of built-in functions. In newer versions of Excel, the best...

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Remove leading and trailing spaces from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20leading%20and%20trailing%20spaces.png "Excel formula: Remove leading and trailing spaces from text")](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

### [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)

The TRIM function is fully automatic. It removes both leading and trailing spaces from text strings, and also "normalizes" multiple spaces between words to one space character only. All you need to do is supply a reference to a cell. TRIM with CLEAN If you also need to remove line breaks from cells...

[![Excel formula: Normalize text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/normalize%20text.png "Excel formula: Normalize text")](https://exceljet.net/formulas/normalize-text)

### [Normalize text](https://exceljet.net/formulas/normalize-text)

The formula shown in this example uses a series of nested SUBSTITUTE functions to strip out parentheses, hyphens, colons, semi-colons, exclamation marks, commas, and periods. The process runs from the inside out, with each SUBSTITUTE replacing one character with a single space, then handing off to...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20date%20ddmmyy%20to%20mmddyy.png "Excel formula: Convert text date dd/mm/yy to mm/dd/yy")](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

### [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

The core of this formula is the DATE function, which is used to assemble a proper Excel date value. The DATE function requires valid year, month, and day values, so these are parsed out of the original text string as follows: 1. The year value is extracted with the RIGHT function: RIGHT(B5,2)+2000...

[![Excel formula: Join cells with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join%20cells%20with%20comma_0.png "Excel formula: Join cells with comma")](https://exceljet.net/formulas/join-cells-with-comma)

### [Join cells with comma](https://exceljet.net/formulas/join-cells-with-comma)

Working from the inside out, the formula first joins the values the 5 cells to the left using the concatenation operator (...

TRIM function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20all%20in%20one%20formulas_Thumb.png)](https://exceljet.net/videos/how-to-build-all-in-one-formulas)

### [How to build all-in-one formulas](https://exceljet.net/videos/how-to-build-all-in-one-formulas)

In this video we're going to build a formula that counts the number of words in a cell. This cell has eight words in it, and we're going to build a formula step by step that gives us the number "8". We're going to use "helper" formulas to do that, and when we're finished, we'll take those helper...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20clean%20text%20with%20CLEAN%20and%20TRIM-thumb.png)](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

### [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

When you bring data into Excel you sometimes end up with extra spaces and other characters that cause problems. Excel contains two functions that can help you clean things up. Let's take a look. Here we have a list of movie titles that were copied in from some other system. You can see that there's...

Related functions
-----------------

[![Excel CLEAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20clean%20function.png "Excel CLEAN function")](https://exceljet.net/functions/clean-function)

### [CLEAN Function](https://exceljet.net/functions/clean-function)

The Excel CLEAN function takes a text string and returns text that has been "cleaned" of line breaks and other non-printable characters.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count total words in a cell](https://exceljet.net/formulas/count-total-words-in-a-cell)
    
*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    
*   [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)
    
*   [Get last line in cell](https://exceljet.net/formulas/get-last-line-in-cell)
    
*   [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)
    
*   [Join cells with comma](https://exceljet.net/formulas/join-cells-with-comma)
    
*   [LAMBDA count words](https://exceljet.net/formulas/lambda-count-words)
    
*   [Remove leading and trailing spaces from text](https://exceljet.net/formulas/remove-leading-and-trailing-spaces-from-text)
    
*   [Remove last word](https://exceljet.net/formulas/remove-last-word)
    
*   [Get last word](https://exceljet.net/formulas/get-last-word)
    

### Videos

*   [How to clean text with CLEAN and TRIM](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)
    
*   [How to build all-in-one formulas](https://exceljet.net/videos/how-to-build-all-in-one-formulas)
    

### Functions

*   [CLEAN Function](https://exceljet.net/functions/clean-function)
    

### Links

*   [Microsoft TRIM function documentation](https://support.office.com/en-us/article/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9)
    

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