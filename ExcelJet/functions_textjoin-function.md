# Excel TEXTJOIN function | Exceljet

**Source:** https://exceljet.net/functions/textjoin-function

---

[Skip to main content](https://exceljet.net/functions/textjoin-function#main-content)

[](https://exceljet.net/functions/textjoin-function#)

*   [Previous](https://exceljet.net/functions/text-function)
    
*   [Next](https://exceljet.net/functions/trim-function)
    

Excel 2019

[Text](https://exceljet.net/functions#Text)

TEXTJOIN Function
=================

by Dave Bruns · Updated 3 Dec 2022

Related functions 
------------------

[CONCATENATE](https://exceljet.net/functions/concatenate-function)

[CONCAT](https://exceljet.net/functions/concat-function)

![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")

Summary
-------

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells

Purpose 
--------

Join text values with a delimiter

Return value 
-------------

Concatenated text

Syntax
------

    =TEXTJOIN(delimiter,ignore_empty,text1,[text2],...)

*   _delimiter_ - Separator between each text.
*   _ignore\_empty_ - Whether to ignore empty cells or not.
*   _text1_ - First text value or range.
*   _text2_ - \[optional\] Second text value or range.

Using the TEXTJOIN function 
----------------------------

The TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells.

The TEXTJOIN function takes three required [arguments](https://exceljet.net/glossary/function-argument)
: _delimiter_, _ignore\_empty_, and _text1_. _Delimiter_ is the text to use between values that are concatenated together and should be enclosed in double-quotes (""), for example, a space (" ") or a comma with a space (", "). To use no delimiter, supply an empty string ("").  _Ignore\_empty_ is a Boolean (TRUE/FALSE) value that controls whether empty values should be ignored or added to the result. This is often set to TRUE to avoid delimiters with no content in the result from TEXTJOIN. _Text1_ is the first value to join together. This can be a cell reference, a range, or a hard-coded text value. Subsequent optional arguments, _text2_, _text3_, _text4_, etc. can be provided up to 252 values total.

Values are concatenated in the order they appear. With "Hello" in A1 and "World" in A2, the following formula returns "Hello World":

    =TEXTJOIN(" ",TRUE,A1,A2) // returns "Hello World"
    

Changing the delimiter to a comma (", ") and reversing A1 and A2, we get "World, Hello":

    =TEXTJOIN(", ",TRUE,A2,A1) // returns "World, Hello"
    

### Concatenating a range

To join cells in the range A1:A3 with a comma and space, you can use TEXTJOIN like this:

    =TEXTJOIN(", ",TRUE,A1:A3)
    

![ TEXTJOIN basic example](https://exceljet.net/sites/default/files/images/functions/inline/textjoin%20basic%20example.png " TEXTJOIN basic example")

The second argument, _ignore\_empty,_ controls behavior for empty cells and text values. If set TRUE, empty values are skipped so that the delimiter is not repeated in the final result. If set to FALSE, TEXTJOIN will include empty values in the output.

### Name with title

In the example below, TEXTJOIN is set up to concatenate names. Notice the cell reference for Title is provided first, followed by a range for First, Middle, and Last. Ignore empty is set to 1 (TRUE) to avoid adding extra space to names without Middle or Title values. The formula in F3 is:

    =TEXTJOIN(" ",1,E3,B3:D3)
    

![ TEXTJOIN example with names](https://exceljet.net/sites/default/files/images/functions/inline/textjoin%20example%20with%20names.png " TEXTJOIN example with names")

### Number formatting

When concatenating numbers, [number formatting](https://exceljet.net/glossary/number-format)
 is lost. For example, with the date 1-Jul-2021 in cell A1, and 2-Jul-2021 in A2, the dates revert to [serial numbers](https://exceljet.net/glossary/excel-date)
:

    =TEXTJOIN("-",1,A1,A2) // returns "44378-44379"
    

Use the [TEXT function](https://exceljet.net/functions/text-function)
 to apply formatting during concatenation:

    =TEXTJOIN("-",1,TEXT(A1,"mmm d"),TEXT(A2,"mmm d")) // "Jul 1-Jul 2"
    

The formula above returns the text "Jul 1-Jul 2".  Adjust the [number formatting](https://exceljet.net/articles/custom-number-formats)
 as desired.

### TEXTJOIN versus CONCAT

TEXTJOIN and [CONCAT](https://exceljet.net/functions/concat-function)
 are both newer functions in Excel that replace the older [CONCATENATE](https://exceljet.net/functions/concatenate-function)
 function. Like the CONCAT function, TEXTJOIN will accept a _range_ of cells to concatenate. The main difference is that TEXTJOIN also accepts a _delimiter_ to use when joining values together.

### Notes

*   To concatenate manually, use the [concatenation operator](https://exceljet.net/glossary/concatenation)
     (&)
*   The [CONCAT function](https://exceljet.net/functions/concat-function)
     also provides basic concatenation, but provides no options for delimiters or empty values.
*   Numbers provided to TEXTJOIN will be converted to text values during concatenation.
*   TEXTJOIN is a new function, available in Office 365 and Excel 2019.

TEXTJOIN function examples
--------------------------

[![Excel formula: Multiple matches in comma separated list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/multiple%20matches%20in%20comma%20separated%20result2.png "Excel formula: Multiple matches in comma separated list")](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list)

### [Multiple matches in comma separated list](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list)

The core of this formula is the IF function, which "filters" the names in the table by color like this: IF(group=E5,name,"")) The logical test checks each cell in the named range "group" for the color value in E5 (red in this case). The result is an array like this: {FALSE;FALSE;TRUE;TRUE;FALSE;...

[![Excel formula: Split full name into parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_full_name_into_parts.png "Excel formula: Split full name into parts")](https://exceljet.net/formulas/split-full-name-into-parts)

### [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)

In this example, the goal is to split the names in column B into three separate parts (First, Middle, and Last) with a single formula. In cases where there is no middle name, the Middle column should be blank. In cases where there are two middle names, the Middle column should contain both names...

[![Excel formula: Get Unicode Sequence from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_unicode_sequence_of_text_main_0.png "Excel formula: Get Unicode Sequence from text")](https://exceljet.net/formulas/get-unicode-sequence-from-text)

### [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)

In this example, the goal is to convert each character in a text string into its corresponding Unicode code point and display the results as a space-separated sequence. This problem can be solved using several Excel functions working together to extract, convert, and format the Unicode values. The...

[![Excel formula: Reverse text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse%20text%20string.png "Excel formula: Reverse text string")](https://exceljet.net/formulas/reverse-text-string)

### [Reverse text string](https://exceljet.net/formulas/reverse-text-string)

At the core, this formula uses the MID function to extract each character of a text string in reverse order. The starting character is given as a list of numbers in descending order hard-coded as array constant: MID(B5,{10,9,8,7,6,5,4,3,2,1},1) The text argument comes B5, and 1 is specified for the...

[![Excel formula: List holidays between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20holidays%20between%20two%20dates.png "Excel formula: List holidays between two dates")](https://exceljet.net/formulas/list-holidays-between-two-dates)

### [List holidays between two dates](https://exceljet.net/formulas/list-holidays-between-two-dates)

At a high level, this formula uses a nested IF function to return an array of holidays between two dates. This array is then processed by the TEXTJOIN function, which converts the array to text using a comma as the delimiter. Working from the inside out, we generate the array of matching holidays...

[![Excel formula: Clean and reformat telephone numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/clean_and_reformat_telephone_numbers.png "Excel formula: Clean and reformat telephone numbers")](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

### [Clean and reformat telephone numbers](https://exceljet.net/formulas/clean-and-reformat-telephone-numbers)

In this example, the goal is to clean up telephone numbers with inconsistent formatting and then reformat the numbers in the same way. In practice, this means we need to start by removing the extra non-numeric characters, including spaces, dashes, periods, and parentheses. Once these characters are...

[![Excel formula: Look up and return to single cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_and_return_to_single_cell.png "Excel formula: Look up and return to single cell")](https://exceljet.net/formulas/look-up-and-return-to-single-cell)

### [Look up and return to single cell](https://exceljet.net/formulas/look-up-and-return-to-single-cell)

In this example, the goal is to look up and retrieve all names for a given team and return them in a single cell as a comma‑separated list. At the core, this is a lookup problem, but the twist is that we want to return multiple matches for each team, not just one. That means traditional lookup...

[![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")](https://exceljet.net/formulas/reverse-a-list-or-range)

### [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the SORT function...

[![Excel formula: Join first and last name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/join_first_and_last_names.png "Excel formula: Join first and last name")](https://exceljet.net/formulas/join-first-and-last-name)

### [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)

In this example, the goal is to join different parts of a name (first, middle, last) into a full name. This is an example of concatenation . To concatenate means to join one text value to another with a formula, or in a more general programming language. In a current version of Excel, the simplest...

[![Excel formula: Create email with display name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20email%20with%20display%20name.png "Excel formula: Create email with display name")](https://exceljet.net/formulas/create-email-with-display-name)

### [Create email with display name](https://exceljet.net/formulas/create-email-with-display-name)

Some applications show email addresses together with a "display name", where the name appears first, followed by the email address enclosed in angle brackets (<>). The goal in this example is to create a format like this based on an existing name and email address. In the worksheet shown,...

[![Excel formula: Translate letters to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/translate%20letters%20to%20numbers.png "Excel formula: Translate letters to numbers")](https://exceljet.net/formulas/translate-letters-to-numbers)

### [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)

At the core, this formula uses an array operation to generate an array of letters from the input text, translates each letter individually to a number, then joins all numbers together again and returns the output as a string. To parse the input string into an array or letters, we use MID, ROW, LEN...

[![Excel formula: Get all matches cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_all_matches_cell_contains.png "Excel formula: Get all matches cell contains")](https://exceljet.net/formulas/get-all-matches-cell-contains)

### [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)

In this example the goal is to check a cell for several things at once, and return a comma separated list of the things that were found. In other words, we want check for the colors seen in column E and list the colors found in column C. The formula in C5, copied down, is: =TEXTJOIN(", ",1,FILTER(...

[![Excel formula: Sort comma separated values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort_comma_separated_values.png "Excel formula: Sort comma separated values")](https://exceljet.net/formulas/sort-comma-separated-values)

### [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)

In this example the goal is to sort the comma separated values in column B in alphabetical order. In the latest version of Excel, you can solve this problem with a formula based on TEXTSPLIT, SORT, and TEXTJOIN. In earlier versions of Excel the problem is more complicated. See below for a couple of...

[![Excel formula: Strip numeric characters from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip%20numeric%20characters%20from%20cell_0.png "Excel formula: Strip numeric characters from cell")](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

### [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)

Excel doesn't have a way to cast the letters in a text string to an array directly in a formula. As a workaround, this formula uses the MID function, with help from the ROW and INDIRECT functions to achieve the same result. The formula in C5, copied down, is: =TEXTJOIN("",TRUE,IF(ISERR(MID(B5,ROW(...

[![Excel formula: MAC address format](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/MAC%20address%20format.png "Excel formula: MAC address format")](https://exceljet.net/formulas/mac-address-format)

### [MAC address format](https://exceljet.net/formulas/mac-address-format)

A MAC (Media Access Control) address is a unique identifier assigned to most network adapters. Two common IEEE 802 standards display a MAC address in 6 groups of 2 hexadecimal digits separated by a colon (:) or hyphen (-) like this: "01-23-45-67-89-ab" "01:23:45:67:89:ab" To format a text string...

Related functions
-----------------

[![Excel CONCATENATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20concatenate%20function.png "Excel CONCATENATE function")](https://exceljet.net/functions/concatenate-function)

### [CONCATENATE Function](https://exceljet.net/functions/concatenate-function)

The Excel CONCATENATE function concatenates (joins) join up to 30 values together and returns the result as text. In Excel 2019 and later, the [CONCAT](https://exceljet.net/functions/concat-function)
 and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 functions are better, more flexible alternatives...

[![Excel CONCAT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20concat%20function.png "Excel CONCAT function")](https://exceljet.net/functions/concat-function)

### [CONCAT Function](https://exceljet.net/functions/concat-function)

The Excel CONCAT function concatenates (joins) values supplied as references or constants. Unlike the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
 (which CONCAT replaces), CONCAT will accept a [range](https://exceljet.net/glossary/range)
 of cells to join, in addition to individual...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Join first and last name](https://exceljet.net/formulas/join-first-and-last-name)
    
*   [Create email with display name](https://exceljet.net/formulas/create-email-with-display-name)
    
*   [Strip numeric characters from cell](https://exceljet.net/formulas/strip-numeric-characters-from-cell)
    
*   [Multiple matches in comma separated list](https://exceljet.net/formulas/multiple-matches-in-comma-separated-list)
    
*   [MAC address format](https://exceljet.net/formulas/mac-address-format)
    
*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    
*   [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)
    
*   [Get Unicode Sequence from text](https://exceljet.net/formulas/get-unicode-sequence-from-text)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [Replace one delimiter with another](https://exceljet.net/formulas/replace-one-delimiter-with-another)
    

### Functions

*   [CONCATENATE Function](https://exceljet.net/functions/concatenate-function)
    
*   [CONCAT Function](https://exceljet.net/functions/concat-function)
    

### Articles

*   [How to concatenate in Excel](https://exceljet.net/articles/how-to-concatenate-in-excel)
    

### Links

*   [Microsoft TEXTJOIN function documentation](https://support.office.com/en-us/article/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c)
    

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