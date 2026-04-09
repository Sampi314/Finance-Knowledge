# Excel TEXTSPLIT function | Exceljet

**Source:** https://exceljet.net/functions/textsplit-function

---

[Skip to main content](https://exceljet.net/functions/textsplit-function#main-content)

[](https://exceljet.net/functions/textsplit-function#)

*   [Previous](https://exceljet.net/functions/textbefore-function)
    
*   [Next](https://exceljet.net/functions/tocol-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

TEXTSPLIT Function
==================

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[CONCAT](https://exceljet.net/functions/concat-function)

![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")

Summary
-------

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

Purpose 
--------

Split a text string with a delimiter

Return value 
-------------

An array of split values

Syntax
------

    =TEXTSPLIT(text,col_delimiter,[row_delimiter],[ignore_empty],[match_mode],[pad_with])

*   _text_ - The text string to split.
*   _col\_delimiter_ - The character(s) to delimit columns.
*   _row\_delimiter_ - \[optional\] The character(s) to delimit rows.
*   _ignore\_empty_ - \[optional\] Ignore empty values. TRUE = ignore, FALSE = preserve. Default is FALSE.
*   _match\_mode_ - \[optional\] Case-sensitivity. 0 = enabled, 1 = disabled. Default is 0.
*   _pad\_with_ - \[optional\] Value to pad missing values in 2d arrays.

Using the TEXTSPLIT function 
-----------------------------

The TEXTSPLIT function splits a text string with a given delimiter into multiple values. The output from TEXTSPLIT is an [array](https://exceljet.net/glossary/array)
 that will [spill](https://exceljet.net/glossary/spill)
 into multiple cells in the workbook.

Video: [Excel TEXTSPLIT function](https://exceljet.net/videos/excel-textsplit-function)

### Split text into columns or rows

TEXTSPLIT can split a text string into columns or rows. To use TEXTSPLIT, you will need to provide the text to split and a delimiter. You can either provide a column delimiter (_col\_delimiter_) to split text into columns, or a row delimiter (_row\_delimiter_) to split text into rows. For example, the formula below splits the text "red-blue-green" into separate values in columns:

    =TEXTSPLIT("red-blue-green","-") // returns {"red","blue","green"}

Note that the column delimiter is provided as a hyphen ("-). If we move the hyphen ("-") to the row delimiter position, the TEXTSPLIT function will return the same values split into rows:

    =TEXTSPLIT("red-blue-green",,"-") // returns {"red";"blue";"green"}

Note that both formulas above return an [array](https://exceljet.net/glossary/array)
 of three values and the only difference is the location of the delimiter. The values in this first array will spill into separate _columns_, and the values in the second formula will spill into _rows_. The example below shows how this looks on the worksheet:

![A basic example of the TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TEXTSPLIT_basic_example.png "A basic example of the TEXTSPLIT function")

The first formula in cell D3 separates the three values into separate columns:

    =TEXTSPLIT(B3,",") // returns {"Red","Blue","Green"}
    

The formula in cell D5 uses the same delimiter to split the text into separate _rows_:

    =TEXTSPLIT(B3,,",") // returns {"Red";"Blue";"Green"}
    

In the second formula, the _row\_delimiter_ is left empty, and the same delimiter (",") appears as _col\_delimiter_.

_To summarize: provide a column delimiter if you want the results to be in separate columns and a row delimiter if you want the results to appear in separate rows._

> TEXTSPLIT extracts _all text_ separated by delimiters. Use [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
>  to extract text _before_ a given delimiter, and [TEXTAFTER](https://exceljet.net/functions/textafter-function)
>  to extract text _after_ a given delimiter.

### Behavior if no delimiter is found

If the provided delimiter is not found, TEXTSPLIT will return the original text unchanged. For example, if we use TEXTSPLIT on the text string "apple orange" with a period configured as the delimiter, TEXTSPLIT will return the original text:

    =TEXTSPLIT("apple orange",".") // returns "apple orange"

The period (".") is not found, yet TEXTSPLIT behaves as if the delimiter _was found_ at the end of the text. Both the TEXTBEFORE and TEXTAFTER functions have a similar feature, but it must be enabled with the _match\_end_ argument. With TEXTSPLIT, this behavior is automatic and [useful](https://exceljet.net/formulas/count-total-words-in-a-cell)
.

### Ignoring empty values

By default, TEXTSPLIT will _include_ empty values in the text, where empty values are defined as two or more consecutive delimiters without a value in between. In practice, this means you will see empty cells in the worksheet when there is no value between delimiters, as you can see in the first formula below:

![TEXTSPLIT example with empty values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TEXTSPLIT%20ignore%20empty%20values.png?itok=-LXO2DOG "TEXTSPLIT example with empty values")

The formula in cell D3 does not include a value for _ignore\_empty_, so empty values will appear:

    =TEXTSPLIT(B3,",") // empty values will appear

To ignore (i.e., remove) empty values, set _ignore\_empty_ to TRUE, as in the second formula in cell D5:

    =TEXTSPLIT(B3,",",,TRUE) // ignore empty values
    

In this case, TEXTSPLIT behaves as if the missing value does not exist at all. Only "Red" and "Green" are returned.

_Note: you can use 1 and 0 in place of TRUE and FALSE for the ignore\_empty argument._

### Match mode

The fifth argument, _match\_mode_, determines case sensitivity when looking for a delimiter. By default, TEXTSPLIT _is_ case-sensitive and _match\_mode_ is zero (0). Supply 1 to _disable case sensitivity_. In the example below the delimiter is " x " and " X ". The formula in D5 sets match mode to 1 to make TEXTSPLIT ignore case. As a result, the formula works for both cases:

    =TEXTSPLIT(B5," x ",,,1)
    

![TEXTSPLIT and case sensitivity](https://exceljet.net/sites/default/files/images/functions/inline/TEXTSPLIT%20and%20case%20sensitivity.png "TEXTSPLIT and case sensitivity")

### Rows and columns

TEXTSPLIT can split text into rows and columns at the same time, as seen below:

![TEXTSPLIT rows and columns example](https://exceljet.net/sites/default/files/images/functions/inline/TEXTSPLIT%20example%20rows%20and%20columns.png "TEXTSPLIT rows and columns example")

In this case, an equal sign ("=") is provided as _col\_delimiter_ and a comma (",") is provided as _row\_delimiter:_

    =TEXTSPLIT(B3,"=",",")
    

The resulting [array](https://exceljet.net/glossary/array)
 from TEXTSPLIT contains 3 rows and 2 columns.

### Padding

The last argument in TEXTSPLIT is _pad\_with._ This argument is optional and will default to #N/A. Padding is used when the output contains rows and columns and a value is missing that would affect the structure of the array. In the worksheet below, "Blue" does not contain a quantity (there is no "=" delimiter). As a result, TEXTSPLIT returns #N/A where the quantity would go, to maintain the integrity of the array.

![TEXTSPLIT with custom padding](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TEXTSPLIT%20with%20padding.png?itok=V8bwJhOn "TEXTSPLIT with custom padding")

The formula in cell E3 contains does not specify a _pad\_with_ argument so the default value is returned:

    =TEXTSPLIT(B3,"=",",") // default padding is #N/A
    

In cell E7, "x" is supplied for _pad\_with_ so "x" appears in cell F8 instead of #N/A.

    =TEXTSPLIT(B3,"=",",",,"x")
    

### Multiple delimiters

Multiple delimiters can be supplied to TEXTSPLIT as an [array constant](https://exceljet.net/glossary/array-constant)
 like {"x","y"} where x and y represent delimiters:

![TEXTSPLIT with multiple delimiters](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TEXTSPLIT%20with%20multiple%20delimiters.png?itok=MYUp6LQw "TEXTSPLIT with multiple delimiters")

In the worksheet above, the text in B3 is delimited by both hyphens "-" and commas (","). The formula in cell F3 is:

    =TEXTSPLIT(B3,{"-",","})
    

Notice also that there is an extra space separating green and purple. The [TRIM function](https://exceljet.net/functions/trim-function)
 can be used to clean up extra space characters that appear in the output from TEXTSPLIT. The formula in F5 is:

    =TRIM(TEXTSPLIT(B3,{"-",","}))
    

Notice the extra space that appears before purple in cell I3 is gone in cell I5.

Video: [TEXTSPLIT with multiple delimiters](https://exceljet.net/videos/textsplit-with-multiple-delimiters)

### Array of arrays

When using TEXTSPLIT, you might run into a limitation of the Excel formula engine where the formula will not return "arrays of arrays". When TEXTSPLIT is used on a single cell, it returns the text in a single array, and values spill onto the worksheet into multiple cells. However, when TEXTSPLIT is used on a [range](https://exceljet.net/glossary/range)
 of cells, TEXTSPLIT returns an "array of arrays". The result may be a truncated version of the data or in some cases an error. [Example here](https://exceljet.net/glossary/array-of-arrays)
.

TEXTSPLIT function examples
---------------------------

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

[![Excel formula: Convert UTC timestamp to Excel datetime](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert-utc-timestamp-to-excel-datetime.png "Excel formula: Convert UTC timestamp to Excel datetime")](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime)

### [Convert UTC timestamp to Excel datetime](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime)

UTC timestamps like 2026-01-18T08:00:00Z are a common standard for representing dates and times, but Excel won't correctly recognize this format without some help. If you try to apply date formatting to a UTC timestamp, nothing happens. In this example, the goal is to convert UTC timestamps to...

[![Excel formula: Split full name into parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_full_name_into_parts.png "Excel formula: Split full name into parts")](https://exceljet.net/formulas/split-full-name-into-parts)

### [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)

In this example, the goal is to split the names in column B into three separate parts (First, Middle, and Last) with a single formula. In cases where there is no middle name, the Middle column should be blank. In cases where there are two middle names, the Middle column should contain both names...

[![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")](https://exceljet.net/formulas/abbreviate-names-or-words)

### [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")](https://exceljet.net/formulas/get-domain-from-email-address)

### [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND...

[![Excel formula: Get name from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_name_from_email_address_0.png "Excel formula: Get name from email address")](https://exceljet.net/formulas/get-name-from-email-address)

### [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)

In this example, the goal is to extract the name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTBEFORE function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the LEFT and FIND functions. All three...

[![Excel formula: Extract numbers from text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract_numbers_from_text.png "Excel formula: Extract numbers from text")](https://exceljet.net/formulas/extract-numbers-from-text)

### [Extract numbers from text](https://exceljet.net/formulas/extract-numbers-from-text)

In this example, the goal is to extract the numbers from a set of property listings which describe the number of bedrooms and bathrooms, the size of the house in sq. ft., and the size of the lot in acres. Traditionally, this kind of problem has been quite difficult in Excel because each number must...

[![Excel formula: Sum numbers in single cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_numbers_in_cell.png "Excel formula: Sum numbers in single cell")](https://exceljet.net/formulas/sum-numbers-in-single-cell)

### [Sum numbers in single cell](https://exceljet.net/formulas/sum-numbers-in-single-cell)

The goal is to sum numbers that appear inside a single cell as seen in column B. Technically, the numbers in each cell are a single text string, and the numbers are separated by commas, which is referred to as a "delimiter". In the current version of Excel, the easiest way to solve this problem is...

[![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")](https://exceljet.net/formulas/reverse-a-list-or-range)

### [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the SORT function...

[![Excel formula: TEXTSPLIT get numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/TEXTSPLIT_get_numbers.png "Excel formula: TEXTSPLIT get numeric values")](https://exceljet.net/formulas/textsplit-get-numeric-values)

### [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)

In this example, we have comma-separated text in column B. The goal is to split the text in column B into columns D through G while at the same time converting the numbers to true numeric values. The challenge is that TEXTSPLIT always returns text, so we need a way to convert the numbers while...

[![Excel formula: Sort comma separated values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort_comma_separated_values.png "Excel formula: Sort comma separated values")](https://exceljet.net/formulas/sort-comma-separated-values)

### [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)

In this example the goal is to sort the comma separated values in column B in alphabetical order. In the latest version of Excel, you can solve this problem with a formula based on TEXTSPLIT, SORT, and TEXTJOIN. In earlier versions of Excel the problem is more complicated. See below for a couple of...

[![Excel formula: Cell contains specific words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_words.png "Excel formula: Cell contains specific words")](https://exceljet.net/formulas/cell-contains-specific-words)

### [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)

In this example, the goal is to test the text in a cell and return TRUE if it contains one or more specific words, and FALSE if not. Notice the emphasis here is on words, not substrings. For example, if we are testing for the word "green" and the text contains the word "evergreen" but not the word...

[![Excel formula: Replace one delimiter with another](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/replace_one_delimiter_with_another.png "Excel formula: Replace one delimiter with another")](https://exceljet.net/formulas/replace-one-delimiter-with-another)

### [Replace one delimiter with another](https://exceljet.net/formulas/replace-one-delimiter-with-another)

In this example, the goal is to replace the comma-separated values in column B with the line break-separated values seen in column D. In a problem like this, the first step is to identify the delimiter , which is the character (or characters) that separate each value we want to process. In this...

[![Excel formula: Split dimensions into three parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_dimensions_into_three_parts.png "Excel formula: Split dimensions into three parts")](https://exceljet.net/formulas/split-dimensions-into-three-parts)

### [Split dimensions into three parts](https://exceljet.net/formulas/split-dimensions-into-three-parts)

In this example, the goal is to split the text strings in column B, which contain three dimensions in the form "L x W x H", into 3 separate dimensions. One problem with dimensions entered as text is that they can't be used for any kind of calculation. So, in addition, we want our final dimensions...

TEXTSPLIT function videos
-------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/TEXTSPLIT_with_multiple_delimiters_PLAY.png)](https://exceljet.net/videos/textsplit-with-multiple-delimiters)

### [TEXTSPLIT with multiple delimiters](https://exceljet.net/videos/textsplit-with-multiple-delimiters)

In this video, we'll look at how to use TEXTSPLIT with multiple delimiters. Sometimes, you'll want to configure TEXTSPLIT to use multiple delimiters. On this worksheet, we have some comma-separated text. If I configure TEXTSPLIT to split the text using a comma... It works fine for most of the data...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel_TEXTSPLIT_function_play.png)](https://exceljet.net/videos/excel-textsplit-function)

### [Excel TEXTSPLIT function](https://exceljet.net/videos/excel-textsplit-function)

In this video, we'll take a look at the TEXTSPLIT function. TEXTSPLIT is an Excel function designed to split text into separate cells using a given delimiter. In this worksheet, we have a list of email addresses. The goal is to split each email into a separate name and domain. As I start to enter...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/TEXTSPLIT_with_numbers_Play.png)](https://exceljet.net/videos/textsplit-with-numbers)

### [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)

In this video, we'll take a look at how to handle numbers with the TEXTSPLIT function. One result of using the TEXTSPLIT function is that all output is text, and this can cause problems if you need numeric values. Let me illustrate with an example. In this worksheet, we have some comma-separated...

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

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

*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Extract numbers from text](https://exceljet.net/formulas/extract-numbers-from-text)
    
*   [Sort comma separated values](https://exceljet.net/formulas/sort-comma-separated-values)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    
*   [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)
    
*   [Replace one delimiter with another](https://exceljet.net/formulas/replace-one-delimiter-with-another)
    
*   [Convert UTC timestamp to Excel datetime](https://exceljet.net/formulas/convert-utc-timestamp-to-excel-datetime)
    
*   [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)
    
*   [Encode Unicode sequence into text](https://exceljet.net/formulas/encode-unicode-sequence-into-text)
    
*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    

### Videos

*   [Excel TEXTSPLIT function](https://exceljet.net/videos/excel-textsplit-function)
    
*   [TEXTSPLIT with multiple delimiters](https://exceljet.net/videos/textsplit-with-multiple-delimiters)
    
*   [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)
    

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [CONCAT Function](https://exceljet.net/functions/concat-function)
    

### Links

*   [Microsoft TEXTSPLIT function documentation](https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7)
    

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