# Excel TEXTAFTER function | Exceljet

**Source:** https://exceljet.net/functions/textafter-function

---

[Skip to main content](https://exceljet.net/functions/textafter-function#main-content)

[](https://exceljet.net/functions/textafter-function#)

*   [Previous](https://exceljet.net/functions/take-function)
    
*   [Next](https://exceljet.net/functions/textbefore-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

TEXTAFTER Function
==================

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[CONCAT](https://exceljet.net/functions/concat-function)

![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")

Summary
-------

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter.

Purpose 
--------

Extract text after a delimiter

Return value 
-------------

Extracted text string

Syntax
------

    =TEXTAFTER(text,delimiter,[instance_num],[match_mode],[match_end],[if_not_found])

*   _text_ - The text string to extract from.
*   _delimiter_ - The character(s) that delimit the text.
*   _instance\_num_ - \[optional\] The instance of the delimiter in text. Default is 1.
*   _match\_mode_ - \[optional\] Case-sensitivity. 0 = enabled, 1 = disabled. Default is 0.
*   _match\_end_ - \[optional\] Treat end of text as delimiter. 0 = disabled, 1 = enabled. Default is 0.
*   _if\_not\_found_ - \[optional\] Value to return when no match is found. #N/A is default.

Using the TEXTAFTER function 
-----------------------------

The Excel TEXTAFTER function extracts text that occurs after a given delimiter. When multiple delimiters appear in the text, TEXTAFTER can return text that occurs after the nth instance of the delimiter. TEXTAFTER can also extract text after a specific delimiter when counting from the _end of a text string_ (i.e., get text after the second to the last delimiter).

*   The output from TEXTAFTER is a single text string that occurs after a matched delimiter.
*   TEXTAFTER takes six arguments, but only the first two are required: _text_ provides the text to process, and _delimiter_ is the substring used to split the text.
*   The _instance\_num_ argument indicates which instance of the delimiter to use. For example, to extract the text after the _second instance_ of a delimiter, use 2 for _instance\_num_. If not supplied, _instance\_num_ defaults to 1. 
*   By default, TEXTAFTER is case-sensitive (_match\_mode_ = 0) and will match case when looking for a delimiter. _S_et _match\_mode_ to 1 to ignore case when matching delimiters.
*   By default, TEXTAFTER will not treat the end of a text string like a delimiter (_match\_end_ = 0). To enable this behavior, set _match\_end_ to 1.
*   By default, TEXTAFTER will return #N/A when it cannot find the specified delimiter. To return something other than #N/A, provide a value for _if\_not\_found_. Note that if _match\_end_ is enabled, it will override the value provided for _if\_not\_found._

Video demo: [Excel TEXTAFTER function](https://exceljet.net/videos/excel-textafter-function)

Note that Excel has three related functions that split text:

*   Use [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
     to extract _all text_ separated by a given delimiter.
*   Use [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
     to extract the text _before_ a given delimiter.
*   Use [TEXTAFTER](https://exceljet.net/functions/textafter-function)
     to extract the text _after_ a given delimiter.

### Basic usage

To extract the text that occurs after a specific character or substring, provide the _text_ and the character(s) to use as _delimiter_ in double quotes (""). For example, to extract the first name from "Jones, Bob", provide a comma in double quotes (",") as _delimiter_:

    =TEXTAFTER("Jones,Bob",",") // returns "Bob"
    

You can use more than one character for _delimiter_. For example to extract the second dimension in the text string "12 ft x 20 ft", use " x "for _delimiter:_

    =TEXTAFTER("12 ft x 20 ft"," x ") // returns "20 ft"
    

Note we include a space before and after x, since all three characters function as a delimiter.

### Text after delimiter with positive instance number

By default _instance\_num_ is positive, and TEXTAFTER will count instances of the delimiter starting from the left, as illustrated in the image below. To get all text before "quick", use 1 for instance number. To get all text before "brown", use 2 for instance number. To extract all text before the last word in the sentence ("dog"), provide 8 for _instance\_num:_

![TEXTAFTER with a positive instance number](https://exceljet.net/sites/default/files/images/functions/inline/TEXTAFTER_with_positive_instance_number.png "TEXTAFTER with a positive instance number")

The formulas below extract text after the first and second occurrence of the hyphen character ("-"):

    =TEXTAFTER("ABX-112-Red-Y","-",1) // returns "112-Red-Y"
    =TEXTAFTER("ABX-112-Red-Y","-",2 // returns "Red-Y"
    

TEXTAFTER will return #N/A if the specified instance is not found.

### Text after delimiter with negative instance number

One of TEXTAFTER's special tricks is that it also supports _negative_ instance numbers, which makes it possible to work backward from the _last_ delimiter_._ When _instance\_num_ is negative, TEXTAFTER will count from the _right_, as illustrated below. To extract the last word in the sentence ("dog"), you would use -1 for instance number:

![TEXTAFTER with a negative instance number](https://exceljet.net/sites/default/files/images/functions/inline/TEXTAFTER_with_negative_instance_number.png "TEXTAFTER with a negative instance number")

This is very handy because you don't need to know how many words are in the sentence to begin with. The formulas below extract text after the _last_ and _second-to-last_ hyphen ("-"):

    =TEXTAFTER("ABX-112-Red-Y","-",-1) // returns "Y"
    =TEXTAFTER("ABX-112-Red-Y","-",-2) // returns "Red-Y"
    

If _instance\_num_ is out-of-range, TEXTAFTER returns an #N/A error.

### Match end of text

Normally, TEXTAFTER does not treat the end of a text string as a delimiter. For example, the formula below asks for the text after delimiter 3, counting from the end (note the negative 3):

    =TEXTAFTER("ABX-123-Red-XYZ","-",-3) // returns "123-Red-XYZ"
    

And this formula returns #N/A because there is no fourth delimiter from the end:

    =TEXTAFTER("ABX-123-Red-XYZ","-",-4) // returns #N/A
    

If we enable _match\_end_ by providing 1, the formula behaves as if a delimiter exists before "ABX", which is the "end" of the string when counting backward.

    =TEXTAFTER("ABX-123-Red-XYZ","-",-4,,1) // returns entire string
    

Take care in situations where a delimiter cannot be found and _match\_end_ is enabled. If _match\_end_ is enabled and _instance\_num_ is 1, TEXTAFTER will return an empty string ("") if _delimiter_ is not found. If _match\_end_ is enabled and _instance\_num_ is -1, TEXTAFTER will return the entire string if _delimiter_ is not found. When the target delimiter is found, _match\_end_ has no effect. The video below demonstrates how the _match\_end_ argument can be used:

Video: [Excel TEXTAFTER and TEXTBEFORE advanced options](https://exceljet.net/videos/textafter-and-textbefore-advanced-options)

### Multiple delimiters

To provide multiple delimiters at the same time to TEXTAFTER, you can use an [array constant](https://exceljet.net/glossary/array-constant)
 like {"x","y"} where x and y represent different delimiters. One use of this feature is to handle inconsistent delimiters in the source text. For example, in the worksheet below, the delimiter appears as a comma with a space (", ") and a comma without space (","). By providing the array constant {", ",","} for the delimiter, both variations are handled correctly:

    =TEXTAFTER(B4,{", ",","})
    

![TEXTAFTER with more than one delimiter](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TEXTAFTER%20with%20more%20than%20one%20delimiter.png?itok=HVZUCkzX "TEXTAFTER with more than one delimiter")

### Case-sensitivity

By default, TEXTAFTER _is case-sensitive_ when searching for _delimiter_. This behavior is controlled by the _match\_mode_ argument_,_ a boolean value that enables and disables case-sensitivity. By default, _match\_mode_ is FALSE. In the example below, the delimiter appears as both " x " and " X " (upper and lower case "x"). The formula in D4 sets _match\_mode_ to TRUE, which _disables case-sensitivity_ and allows TEXTAFTER to match both versions of the delimiter:

    =TEXTAFTER(B4," x ",,TRUE) // disable case-sensitivity
    

![TEXTAFTER case sensitive example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/TEXTAFTER%20case%20sensitive%20example.png?itok=c0JO9KUL "TEXTAFTER case sensitive example")

_Note: you can use 1 and 0 in place of TRUE and FALSE for the match\_mode argument._

### Notes

*   TEXTAFTER is case-sensitive by default.
*   TEXTAFTER will return a #N/A! error if _delimiter_ is not found.
*   TEXTAFTER will return a #VALUE! error if _text_ is empty
*   TEXTAFTER will return #N/A if _instance\_num_ is out-of-range.

TEXTAFTER function examples
---------------------------

[![Excel formula: Get top level domain (TLD)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_top_level_domain_TLD.png "Excel formula: Get top level domain (TLD)")](https://exceljet.net/formulas/get-top-level-domain-tld)

### [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)

In this example, the goal is to extract the top-level domain (TLD) from a list of domains. A top-level domain is the last segment of text in a domain name, for example, ".com", ".net", or ".net". In the current version of Excel, the TEXTAFTER function is a simple way to solve this problem. In an...

[![Excel formula: List sheet names with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/List_sheet_names_with_formula_0.png "Excel formula: List sheet names with formula")](https://exceljet.net/formulas/list-sheet-names-with-formula)

### [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)

In this example, the goal is to generate a list of the sheet names in an Excel workbook with a formula. Unfortunately, there is no simple way to do this with a formula in Excel. However, it can be done with a two-step approach: Define a name called "sheetnames" with an old macro command and the...

[![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")](https://exceljet.net/formulas/get-middle-name-from-full-name)

### [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based...

[![Excel formula: Get domain name from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_name_from_url_0.png "Excel formula: Get domain name from URL")](https://exceljet.net/formulas/get-domain-name-from-url)

### [Get domain name from URL](https://exceljet.net/formulas/get-domain-name-from-url)

In this example, the goal is to extract the domain name from a list of URLs. In the current version of Excel, the easiest way to do this is to use a formula based on the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, you can use a more complicated formula based on the LEFT and FIND...

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

[![Excel formula: Get last name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_0.png "Excel formula: Get last name from name")](https://exceljet.net/formulas/get-last-name-from-name)

### [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)

In this example, the goal is to extract the last name from names that appear in <first> <middle> <last> format, where the middle name is not always present. The easiest way to do this is with the newer TEXTAFTER function. In older versions of Excel, you can use a significantly...

[![Excel formula: Get page from URL](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_page_from_url.png "Excel formula: Get page from URL")](https://exceljet.net/formulas/get-page-from-url)

### [Get page from URL](https://exceljet.net/formulas/get-page-from-url)

In this example, we have a list of URLs. The goal is to get the portion of each URL that appears after the domain name. In the current version of Excel, the easiest way to do this is to use the TEXTAFTER function. In an older version of Excel, you can use a formula based on the MID, FIND, and LEN...

[![Excel formula: Get domain from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_domain_from_email_address_0.png "Excel formula: Get domain from email address")](https://exceljet.net/formulas/get-domain-from-email-address)

### [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)

In this example, the goal is to extract just the domain name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTAFTER function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the RIGHT, LEN, and FIND...

[![Excel formula: Sort by substring](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort_by_substring.png "Excel formula: Sort by substring")](https://exceljet.net/formulas/sort-by-substring)

### [Sort by substring](https://exceljet.net/formulas/sort-by-substring)

We have a list of 12 codes in Column B. Each code consists of a prefix (two letters), a color (variable), and a 4-digit number, all separated by hyphens (e.g., AX-Red-6387). The goal is to sort this list based on the color substring so that all codes with the same color are grouped together in the...

[![Excel formula: Put names into proper case](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/put_names_into_proper_case.png "Excel formula: Put names into proper case")](https://exceljet.net/formulas/put-names-into-proper-case)

### [Put names into proper case](https://exceljet.net/formulas/put-names-into-proper-case)

The goal in this example is to reformat names that appear in mixed upper and lower case letters into "proper case", defined as each word in the name beginning with a capital letter. This can easily be done in Excel with the PROPER function. PROPER function The PROPER function automatically...

[![Excel formula: Sum numbers with text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20numbers%20with%20text.png "Excel formula: Sum numbers with text")](https://exceljet.net/formulas/sum-numbers-with-text)

### [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)

In this example, one goal is to sum the numbers that appear in the range B5:B16. A second more challenging goal is to create the table of results seen in E7:F12. For convenience, data is the named range B5:B16. Total sum To sum all the numbers that appear in B5:B16, ignoring text, the formula in E5...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)

### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...

[![Excel formula: Get workbook name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_workbook_name_only.png "Excel formula: Get workbook name only")](https://exceljet.net/formulas/get-workbook-name-only)

### [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)

In this example, the goal is to return the name of the current workbook with a formula. This is a fairly simple problem in the latest version of Excel, which provides the TEXTAFTER function and the TEXTBEFORE function . In older versions of Excel, you can use a more complicated formula based on the...

TEXTAFTER function videos
-------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/TEXTAFTER_and_TEXTBEFORE_advanced_Play.png)](https://exceljet.net/videos/textafter-and-textbefore-advanced-options)

### [TEXTAFTER and TEXTBEFORE advanced options](https://exceljet.net/videos/textafter-and-textbefore-advanced-options)

In this video, we'll look at some advanced options for the TEXTBEFORE and TEXTAFTER functions. In this first example, let's look at how to configure TEXTBEFORE and TEXTAFTER to handle situations when a delimiter is not found. In column B, we have a list of projects with status. The delimiter...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The_TEXTBEFORE_function_Play.png)](https://exceljet.net/videos/excel-textbefore-function)

### [Excel TEXTBEFORE function](https://exceljet.net/videos/excel-textbefore-function)

In this video, we'll take a look at the TEXTBEFORE function. Like the name suggests, TEXTBEFORE is designed to extract text that occurs before a specific marker, called a "delimiter". A delimiter can be one or more characters. Let's look at an example. In this worksheet, we have a list of email...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The_TEXTAFTER_function_play.png)](https://exceljet.net/videos/excel-textafter-function)

### [Excel TEXTAFTER function](https://exceljet.net/videos/excel-textafter-function)

In this video, we'll take a look at the TEXTAFTER function. TEXTAFTER is designed to extract text that occurs after a specific "delimiter", which can be one or more characters. Let's look at an example. In this worksheet, we have a list of email addresses. The goal is to extract the domain portion...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The_TEXTAFTER_with_TEXTBEFORE-Play.png)](https://exceljet.net/videos/textafter-with-textbefore)

### [TEXTAFTER with TEXTBEFORE](https://exceljet.net/videos/textafter-with-textbefore)

In this video, we'll look at some examples where we need to use the TEXTAFTER function together with the TEXTBEFORE function. When splitting text with a formula in Excel you'll often find that you need to use more than one function. In this first example, we have a list of codes in column B and the...

Related functions
-----------------

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

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

*   [Get last name from name](https://exceljet.net/formulas/get-last-name-from-name)
    
*   [Put names into proper case](https://exceljet.net/formulas/put-names-into-proper-case)
    
*   [Get top level domain (TLD)](https://exceljet.net/formulas/get-top-level-domain-tld)
    
*   [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    
*   [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)
    
*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)
    
*   [Sort by substring](https://exceljet.net/formulas/sort-by-substring)
    
*   [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)
    

### Videos

*   [Excel TEXTAFTER function](https://exceljet.net/videos/excel-textafter-function)
    
*   [Excel TEXTBEFORE function](https://exceljet.net/videos/excel-textbefore-function)
    
*   [TEXTAFTER with TEXTBEFORE](https://exceljet.net/videos/textafter-with-textbefore)
    
*   [TEXTAFTER and TEXTBEFORE advanced options](https://exceljet.net/videos/textafter-and-textbefore-advanced-options)
    

### Functions

*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [CONCAT Function](https://exceljet.net/functions/concat-function)
    

### Links

*   [Microsoft TEXTAFTER function documentation](https://support.microsoft.com/en-us/office/textafter-function-c8db2546-5b51-416a-9690-c7e6722e90b4)
    

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