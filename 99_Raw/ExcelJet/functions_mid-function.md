# Excel MID function | Exceljet

**Source:** https://exceljet.net/functions/mid-function

---

[Skip to main content](https://exceljet.net/functions/mid-function#main-content)

[](https://exceljet.net/functions/mid-function#)

*   [Previous](https://exceljet.net/functions/lower-function)
    
*   [Next](https://exceljet.net/functions/numbervalue-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

MID Function
============

by Dave Bruns · Updated 24 Feb 2024

Related functions 
------------------

[LEFT](https://exceljet.net/functions/left-function)

[RIGHT](https://exceljet.net/functions/right-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

![Excel MID function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_mid_function.png "Excel MID function")

Summary
-------

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

Purpose 
--------

Extract text from inside a string

Return value 
-------------

The characters extracted.

Syntax
------

    =MID(text,start_num,num_chars)

*   _text_ - The text to extract from.
*   _start\_num_ - The location of the first character to extract.
*   _num\_chars_ - The number of characters to extract.

Using the MID function 
-----------------------

The MID function extracts a given number of characters from the _middle_ of a supplied text string. MID takes three arguments, all of which are required. The first [argument](https://exceljet.net/glossary/function-argument)
, _text_, is the text string to start with. The second argument, _start\_num_, is the position of the first character to extract. The third argument, _num\_chars_, is the number of characters to extract. If _num\_chars_ is greater than the number of characters available, MID returns all remaining characters.

### MID function basics

To extract text with MID, just provide the text, the starting position, and the number of characters to extract. The formulas below show how to extract one, two, and three characters with MID:

    =MID("apple",1,1) // returns "a"
    =MID("apple",1,2) // returns "ap"
    =MID("apple",1,3) // returns "app"

The formula below returns 3 characters starting at the 5th character:

    =MID("The cat in the hat",5,3) // returns "cat"
    

This formula will extract 3 characters starting at character 16:

    =MID("The cat in the hat",16,3) // returns "hat"
    

If _num\_chars_ is greater than the remaining characters, MID will all remaining characters:

    =MID("apple",1,100) // returns "apple"
    

This can be useful as a way to simply certain formulas as explained below. MID can extract text from numbers, but the result is text:

    =MID(12348,3,4) // returns "348" as text
    

### Example 1 - extract date from serial number

In the example below, we use the MID function to extract a date in YYYYMM notation from a serial number with 14 characters. The formula in cell D5, copied down, is:

    =MID(B5,5,6)

![MID function example - extract date from serial number](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/mid_function_example_extract_date_from_serial_number.png "MID function example - extract date from serial number")

Note that the date is returned as text like "202105" which indicates the year and month but is not a valid date. If you want a valid date, you could use a formula like this:

    =DATE(MID(B5,5,4),MID(B5,9,2),1)

Here we use the MID function twice: once to get the year, and once to get the month. The day is hard-coded as 1, and all values are returned to the [DATE function](https://exceljet.net/functions/date-function)
, which returns a valid Excel date like 1-May-2021.

### Example 2 - extract name from email address

A common challenge with MID is how to provide a variable end point. This can be done by combining MID with the FIND function. For example, in the worksheet below, the goal is to return the name portion of each email address. To perform this task, MID should start at the first character and end at the character before the "@" symbol. The formula in cell D5 looks like this:

    =MID(B5,1,FIND("@",B5)-1)

![MID function example - extract name from email address](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/mid_function_example_extract_name_from_email_address.png "MID function example - extract name from email address")

As the formula is copied down, the FIND function returns the position of the "@" symbol as a number. We then subtract 1 and the result goes into the MID function as the _num\_chars_ argument. 

### Example 3 - extract domain from email address

A related challenge with MID is how to provide a _variable starting point_. This too can be accomplished by combining MID with the FIND function. In the worksheet below, the goal is to return the domain portion of each email address. To perform this task, MID should start at the character after the "@" symbol and continue to the end of the text string. The formula in cell D5 looks like this:

    =MID(B5,FIND("@",B5)+1,100)

![MID function example - extract domain from email address](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/mid_function_example_extract_domain_from_email_address.png "MID function example - extract domain from email address")

In this formula, the starting position (_start\_num_) is provided by FIND, which returns the location as a number of the "@" symbol. We then add 1 to the result from FIND to start at the _next_ character. For _num\_chars_, we hardcode 100. This is a simple hack. When _num\_chars_ exceeds the characters that remain in a text string, MID returns _all remaining characters_. We take advantage of this behavior by providing an arbitrarily large number that will work in all cases.

### Example 4 - MID with IF

You can easily combine the MID function with the [IF function](https://exceljet.net/functions/if-function)
 to create "if cell contains" logic. In the example below, a formula is used to flag serial numbers that contain "2021". The formula in cell D5 is:

    =IF(MID(B5,5,4)="2021","x","")

![MID function example - flag data that contains specific info](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/mid_function_example_flag_data_that_contains_specific_info.png "MID function example - flag data that contains specific info")

The MID function is configured to extract 4 characters beginning at character 5. The result is then compared to "2021" as the logical test inside the IF function. When the result is TRUE, IF returns "x". Otherwise, IF returns an empty string (""). The result is that serial numbers that contain "2021" are clearly identified.

### Example 5 - MID with SEQUENCE

The MID function can also be used together with the SEQUENCE function to split a text string into an array of characters. This pattern shows up in [more advanced formulas](https://exceljet.net/formulas/strip-non-numeric-characters)
 where it is necessary to iterate through a text string one character at a time. The generic version of the formula looks like this:

    =MID(A1,SEQUENCE(1,LEN(A1)),1)

In brief, SEQUENCE spins up a numeric array based on the length of the text string in A1 and this array is delivered to the MID function as the _start\_num_ argument, with _num\_chars_ hardcoded as 1. The results is an array that contains all characters in the text string. See [this page](https://exceljet.net/formulas/split-text-string-to-character-array)
 for a full explanation.

### Related functions

Use the [MID function](https://exceljet.net/functions/mid-function)
 to extract from the _middle_ of a text string. Use the [LEFT function](https://exceljet.net/functions/left-function)
 to extract text from the _left_ side of a text string and the [RIGHT function](https://exceljet.net/functions/right-function)
 to extract text starting from the _right_ side of a text string. The [LEN function](https://exceljet.net/functions/len-function)
 returns the length of text as a count of characters. Use [FIND](https://exceljet.net/functions/find-function)
 or [SEARCH](https://exceljet.net/functions/search-function)
 to locate an unknown starting or ending position.

> In the latest version of Excel, newer functions like [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
> , [TEXTAFTER](https://exceljet.net/functions/textafter-function)
> , and [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
>  greatly simplify certain text operations and make some traditional formulas obsolete. [Example here](https://exceljet.net/formulas/get-name-from-email-address)
> .

### Notes

*   All three arguments are required.
*   The output from MID is _always_ text.
*   MID can extract numbers as well, but the result is text.
*   MID ignores [number formatting](https://exceljet.net/glossary/number-format)
     when extracting characters.
*   When _num\_chars_ is greater than the remaining text, MID returns all remaining characters

MID function examples
---------------------

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

[![Excel formula: Count numbers in text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_numbers_in_text_string.png "Excel formula: Count numbers in text string")](https://exceljet.net/formulas/count-numbers-in-text-string)

### [Count numbers in text string](https://exceljet.net/formulas/count-numbers-in-text-string)

In this example, the goal is to count numbers that appear in column B. The COUNT function is designed to only count numeric values, but because all values in the range B5:B15 are text , COUNT will return zero. One approach is to split the characters in each text value into an array , then use the...

[![Excel formula: Extract word containing specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20containing%20specific%20text.png "Excel formula: Extract word containing specific text")](https://exceljet.net/formulas/extract-word-containing-specific-text)

### [Extract word containing specific text](https://exceljet.net/formulas/extract-word-containing-specific-text)

The gist: this formula "floods" the space between words in a text string with a large number of spaces, finds and extracts the substring of interest, and uses the TRIM function to clean up the mess. Working from the inside out, the original text in B5 is flooded with spaces using SUBSTITUTE:...

[![Excel formula: Remove protocol from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_protocol_from_url.png "Excel formula: Remove protocol from URL")](https://exceljet.net/formulas/remove-protocol-from-url)

### [Remove protocol from URL](https://exceljet.net/formulas/remove-protocol-from-url)

In this example, the goal is to remove the protocol from a list of URLs. To remove the protocol from a URL, we need to remove the first part of the URL. Protocols typically look like this: http:// https:// sftp:// Notice that all protocols end with a double slash ("//"). In the current version of...

[![Excel formula: Capitalize first letter in a text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/capitalize_first_letter.png "Excel formula: Capitalize first letter in a text string")](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)

### [Capitalize first letter in a text string](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)

One of the most important skills to learn with Excel formulas is the concept of nesting. Put simply, nesting just means putting one function inside another. Nesting is super useful, but it does take some practice. You have to learn to read a formula from the inside out. The formulas below are good...

[![Excel formula: Highlight numbers that include symbols](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Conditional%20formatting%20numbers%20with%20symbols%20arrows.png "Excel formula: Highlight numbers that include symbols")](https://exceljet.net/formulas/highlight-numbers-that-include-symbols)

### [Highlight numbers that include symbols](https://exceljet.net/formulas/highlight-numbers-that-include-symbols)

The formula first uses the ISNUMBER function to test if the value is a number, and applies a simple logical if so: =IF(ISNUMBER(B4) For any number less than the value in "input", the formula will return TRUE and the conditional formatting will be applied. However, if the value is not a number, the...

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

[![Excel formula: Convert date string to date time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20date%20string%20to%20date%20time.png "Excel formula: Convert date string to date time")](https://exceljet.net/formulas/convert-date-string-to-date-time)

### [Convert date string to date time](https://exceljet.net/formulas/convert-date-string-to-date-time)

When date information from other systems is pasted or imported to Excel, it may not be recognized as a proper date or time. Instead, Excel may interpret this information as a text or string value only. In this example, the goal is to extract valid date and time information from a text string and...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)

### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...

[![Excel formula: Extract last two words from cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Extract%20last%20two%20words%20from%20cell.png "Excel formula: Extract last two words from cell")](https://exceljet.net/formulas/extract-last-two-words-from-cell)

### [Extract last two words from cell](https://exceljet.net/formulas/extract-last-two-words-from-cell)

At the core, this formula uses the MID function to extract characters starting at the second to last space. The MID function takes 3 arguments: the text to work with, the starting position, and the number of characters to extract. The text comes from column B, and the number of characters can be...

[![Excel formula: Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20text%20date%20ddmmyy%20to%20mmddyy.png "Excel formula: Convert text date dd/mm/yy to mm/dd/yy")](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

### [Convert text date dd/mm/yy to mm/dd/yy](https://exceljet.net/formulas/convert-text-date-ddmmyy-to-mmddyy)

The core of this formula is the DATE function, which is used to assemble a proper Excel date value. The DATE function requires valid year, month, and day values, so these are parsed out of the original text string as follows: 1. The year value is extracted with the RIGHT function: RIGHT(B5,2)+2000...

[![Excel formula: Translate letters to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/translate%20letters%20to%20numbers.png "Excel formula: Translate letters to numbers")](https://exceljet.net/formulas/translate-letters-to-numbers)

### [Translate letters to numbers](https://exceljet.net/formulas/translate-letters-to-numbers)

At the core, this formula uses an array operation to generate an array of letters from the input text, translates each letter individually to a number, then joins all numbers together again and returns the output as a string. To parse the input string into an array or letters, we use MID, ROW, LEN...

[![Excel formula: List sheet names with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/List_sheet_names_with_formula_0.png "Excel formula: List sheet names with formula")](https://exceljet.net/formulas/list-sheet-names-with-formula)

### [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)

In this example, the goal is to generate a list of the sheet names in an Excel workbook with a formula. Unfortunately, there is no simple way to do this with a formula in Excel. However, it can be done with a two-step approach: Define a name called "sheetnames" with an old macro command and the...

[![Excel formula: Cell contains number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_number.png "Excel formula: Cell contains number")](https://exceljet.net/formulas/cell-contains-number)

### [Cell contains number](https://exceljet.net/formulas/cell-contains-number)

In this example, the goal is to test the passwords in column B to see if they contain a number. This is a surprisingly tricky problem because Excel doesn't have a function that will let you test for a number inside a text string directly. Note this is different from checking if a cell value is a...

Related functions
-----------------

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    
*   [Data validation specific characters only](https://exceljet.net/formulas/data-validation-specific-characters-only)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [Strip html from text or numbers](https://exceljet.net/formulas/strip-html-from-text-or-numbers)
    
*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    
*   [LAMBDA strip trailing characters recursive](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive)
    
*   [Extract text between parentheses](https://exceljet.net/formulas/extract-text-between-parentheses)
    
*   [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)
    
*   [Highlight numbers that include symbols](https://exceljet.net/formulas/highlight-numbers-that-include-symbols)
    

### Functions

*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    

### Links

*   [Microsoft MID function documentation](https://support.office.com/en-us/article/mid-midb-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028)
    

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