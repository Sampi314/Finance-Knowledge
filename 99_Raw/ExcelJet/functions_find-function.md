# Excel FIND function | Exceljet

**Source:** https://exceljet.net/functions/find-function

---

[Skip to main content](https://exceljet.net/functions/find-function#main-content)

[](https://exceljet.net/functions/find-function#)

*   [Previous](https://exceljet.net/functions/exact-function)
    
*   [Next](https://exceljet.net/functions/fixed-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

FIND Function
=============

by Dave Bruns · Updated 5 Feb 2024

Related functions 
------------------

[SEARCH](https://exceljet.net/functions/search-function)

[REPLACE](https://exceljet.net/functions/replace-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

![Excel FIND function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20find.png "Excel FIND function")

Summary
-------

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

Purpose 
--------

Get the position of one text string inside another

Return value 
-------------

A number representing the location of substring

Syntax
------

    =FIND(find_text,within_text,[start_num])

*   _find\_text_ - The substring to find.
*   _within\_text_ - The text to search within.
*   _start\_num_ - \[optional\] The starting position in the text to search. Optional, defaults to 1.

Using the FIND function 
------------------------

The FIND function returns the position (as a number) of one [text string](https://exceljet.net/glossary/text-value)
 inside another. In the most basic case, you can use FIND to locate the position of a substring in a text string. You can also use FIND to check if a cell contains specific text. FIND is case-sensitive, which means it distinguishes between uppercase and lowercase letters. This behavior is automatic and cannot be disabled. Here are a few key points to remember about the FIND function:

*   FIND returns the _position_ of one text string inside another as a _number_.
*   When FIND cannot locate the search string, it returns a #VALUE error.
*   If the search string appears more than once, FIND returns the _first position_.
*   FIND is _case-sensitive_ and will evaluate "Apple" and "apple" as different text strings.
*   FIND _does not_ support [wildcards](https://exceljet.net/glossary/wildcard)
     like \*?~ when searching for text.
*   FIND will return 1 if the search string (_find\_text_) is empty.

_Note: The [SEARCH function](https://exceljet.net/functions/search-function)
 is similar to the FIND function. Both functions return the position of one text string inside another. However, unlike FIND, SEARCH is not case-sensitive and_ does _support wildcards._

Video: [How to find text with a formula](https://exceljet.net/videos/how-to-find-text-with-a-formula)

### Basic syntax

The basic syntax of the FIND function looks like this

    FIND(find_text,within_text,[start_num])

*   _find\_text_: The text you want to find (the search string). This is a substring that Excel searches for within another text string. The text must be entered in double quotes if you are hardcoding the value into the formula. Otherwise, you can refer to a cell that contains the text.
*   _within\_text_: The text string that contains the text you want to find. Often this is a cell reference that contains the text, but you can also hardcode a text string in double quotes.
*   _start\_num_ (optional): The character at which to begin searching, as a numeric position. The first character in _within\_text_ is considered position 1. If omitted, the search starts at the beginning of the _within\_text_.

### Basic example

The [FIND function](https://exceljet.net/functions/find-function)
 is designed to look inside a text string for a specific substring. When FIND locates the substring, it returns the position of the substring in the text as a number. If the substring is not found, FIND returns a #VALUE error. For example:

    =FIND("p","apple") // returns 2
    =FIND("z","apple") // returns #VALUE!
    =FIND("apple","Pineapple") // returns 5

Note that text values entered directly into FIND must be enclosed in double quotes (""). As mentioned above, the FIND function is _always_ case-sensitive:

    =FIND("a","Apple") // returns #VALUE!
    =FIND("A","Apple") // returns 1
    =FIND("Apple","Pineapple") // returns #VALUE!

The worksheet below shows the same examples translated into formulas based on cell references:

![Excel FIND function - basic example](https://exceljet.net/sites/default/files/images/functions/inline/exceljet_find_function_basic_example.png "Excel FIND function - basic example")

### Forcing a TRUE or FALSE result

By default, the FIND function returns a number when a search string is found and a #VALUE! error when not. This is inconvenient in cases where you simply want to know if the search string has been found or not. To force a TRUE or FALSE result, you can [nest](https://exceljet.net/glossary/nesting)
 the FIND function inside the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. ISNUMBER returns TRUE for numeric values and FALSE for anything else. If FIND locates the substring, it returns the position as a number, and ISNUMBER returns TRUE:

    =ISNUMBER(FIND("p","apple")) // returns TRUE
    =ISNUMBER(FIND("z","apple")) // returns FALSE

If FIND _doesn't_ locate the substring, it returns an error, and ISNUMBER returns FALSE. You can replace the FIND function above with the SEARCH function if you need support for wildcards. For a more detailed explanation of this approach, with many more examples, [see this example](https://exceljet.net/formulas/cell-contains-specific-text)
.

### If cell contains

Once you have a TRUE or FALSE result, you can combine the FIND function with the [IF function](https://exceljet.net/functions/if-function)
 to create "if cell contains" logic. The generic pattern for this formula looks like this:

    =IF(ISNUMBER(FIND(substring,A1)), "Yes", "No")
    

Instead of returning TRUE or FALSE, the formula above will return "Yes" if the _substring_ is found and "No" if not. You can use the same idea to mark or "flag" items of interest. For example, in the worksheet below, we are using a FIND with IF to flag email addresses that contain "abc" with an "x".

![Using the FIND function with the IF function to flag records](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_find_function_if_cell_contains_example.png "Using the FIND function with the IF function to flag records")

The formula in C5, copied down, is:

    =IF(ISNUMBER(FIND("abc",B5)),"x","")

### Start number

The FIND function has an optional [argument](https://exceljet.net/glossary/function-argument)
 called _start\_num_, that controls where FIND should begin looking for a substring. To find the first match of "the" in any combination of upper or lowercase, you can omit _start\_num_, which defaults to 1:

    =FIND("x","20 x 30 x 50") // returns 4

FIND returns 4 since the first "x" appears at position 4. To find the second "x", enter 5 for _start\_num_:

    =FIND("x","20 x 30 x 50",5) // returns 9
    

 In this case, FIND returns 9 since it starts searching after the first "x". You can effectively find the second "x" in cell A1 in a single formula by using FIND twice like this:

    =FIND(A1,FIND("x",A1)+1)

The inner FIND returns the location of the first "x". We then add 1 and the result is used as the _start\_num_ in the outer FIND. The result is the location of the second "x" in cell A1.

### Wildcards

The FIND function does not support wildcards. See the [SEARCH function](https://exceljet.net/functions/search-function)
.

### More advanced formulas

The FIND function shows up in many more advanced formulas that work with text. FIND is interchangeable with SEARCH, so you will often see SEARCH substituted for FIND (and vice versa) depending on the need for case sensitivity and wildcard support. Here are a few examples:

*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
     - tests a cell for more than one text string simultaneously.
*   [Sum if cells contain either x or y](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)
     - sum numbers when associated cells contain one value or another value
*   [Filter if text contains](https://exceljet.net/formulas/filter-text-contains)
     - extract values from a set of data with "contains-type" logic
*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
     - return an appropriate category based on if a cell contains one of several text values.
*   [Filter based on partial match](https://exceljet.net/formulas/filter-with-partial-match)
     - extract records from an Excel Table based on a partial match.

### Notes

*   The FIND function returns the location of the first _find\_text_ in _within\_text_.
*   The location is returned as the number of characters from the start.
*   _Start\_num_ is optional and defaults to 1.
*   FIND returns 1 when _find\_text_ is empty.
*   FIND returns #VALUE if _find\_text_ is not found.
*   FIND _is_ case-sensitive but _does not_ support wildcards.
*   Use the [SEARCH function](https://exceljet.net/functions/search-function)
     to find a substring with wildcards.

FIND function examples
----------------------

[![Excel formula: Get name from email address](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_name_from_email_address_0.png "Excel formula: Get name from email address")](https://exceljet.net/formulas/get-name-from-email-address)

### [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)

In this example, the goal is to extract the name from a list of email addresses. In the current version of Excel, the easiest way to do this is with the TEXTBEFORE function or the TEXTSPLIT function. In older versions of Excel, you can use a formula based on the LEFT and FIND functions. All three...

[![Excel formula: Trim text to n words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/trim%20text%20to%20n%20words.png "Excel formula: Trim text to n words")](https://exceljet.net/formulas/trim-text-to-n-words)

### [Trim text to n words](https://exceljet.net/formulas/trim-text-to-n-words)

We need a way to split text at a certain marker that corresponds to a certain number of words. Excel doesn't have a built-in function to parse text by word, so are using the SUBSTITUTE function's "instance" argument to replace an "nth space" character with the pound sign (#), then using FIND and...

[![Excel formula: Remove last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20last%20word.png "Excel formula: Remove last word")](https://exceljet.net/formulas/remove-last-word)

### [Remove last word](https://exceljet.net/formulas/remove-last-word)

In this example, the goal is to remove the last word from the text strings in column B. This article explains two approaches: A modern formula based on the TEXTBEFORE function. A more traditional formula for older versions in Excel. The first option is much simpler, and you should use it if you...

[![Excel formula: Get middle name from full name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_middle_name_from_name_0.png "Excel formula: Get middle name from full name")](https://exceljet.net/formulas/get-middle-name-from-full-name)

### [Get middle name from full name](https://exceljet.net/formulas/get-middle-name-from-full-name)

In this example, the goal is to return the middle name from a full name in "First Middle Last" format. In the current version of Excel this is a fairly simple problem using the TEXTAFTER and TEXTBEFORE functions. In older versions of Excel, a similar formula is significantly more complicated, based...

[![Excel formula: Highlight cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20begin%20with.png "Excel formula: Highlight cells that begin with")](https://exceljet.net/formulas/highlight-cells-that-begin-with)

### [Highlight cells that begin with](https://exceljet.net/formulas/highlight-cells-that-begin-with)

In this example, the goal is to apply conditional formatting to cells that begin with specific text, which is entered in cell G2. The highlighting is done automatically with a conditional formatting rule applied to the range B4:G12. The rule type is "Use a formula to determine which cells to format...

[![Excel formula: Extract word that begins with specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20word%20that%20begins%20with.png "Excel formula: Extract word that begins with specific character")](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

### [Extract word that begins with specific character](https://exceljet.net/formulas/extract-word-that-begins-with-specific-character)

Starting from the inside out, the MID function is used to extract all text after "@": MID(B5,FIND("@",B5),LEN(B5)) The FIND function provides the starting point, and for total characters to extract, we just use LEN on the original text. This is a bit sloppy, but it avoids having to calculate the...

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Cell contains number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_number.png "Excel formula: Cell contains number")](https://exceljet.net/formulas/cell-contains-number)

### [Cell contains number](https://exceljet.net/formulas/cell-contains-number)

In this example, the goal is to test the passwords in column B to see if they contain a number. This is a surprisingly tricky problem because Excel doesn't have a function that will let you test for a number inside a text string directly. Note this is different from checking if a cell value is a...

[![Excel formula: Get last name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_name_from_name_with_comma.png "Excel formula: Get last name from name with comma")](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

### [Get last name from name with comma](https://exceljet.net/formulas/get-last-name-from-name-with-comma)

In this example, the goal is to extract the last name from a list of names in "Last, First" format as seen in column B. In the current version of Excel, the easiest solution is to use the TEXTBEFORE function. In older versions of Excel, it can be solved with a more complex formula based on the LEFT...

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: Count cells that contain case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20case%20sensitive.png "Excel formula: Count cells that contain case sensitive")](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

### [Count cells that contain case sensitive](https://exceljet.net/formulas/count-cells-that-contain-case-sensitive)

In this example, the goal is to count codes that appear as substrings in a case-sensitive way. The functions COUNTIF and COUNTIFS are both good options for counting text values, but these functions are not case-sensitive, so they can't be used to solve this problem. The solution is to use the FIND...

[![Excel formula: Sum if cells contain an asterisk](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_an_asterisk.png "Excel formula: Sum if cells contain an asterisk")](https://exceljet.net/formulas/sum-if-cells-contain-an-asterisk)

### [Sum if cells contain an asterisk](https://exceljet.net/formulas/sum-if-cells-contain-an-asterisk)

The goal in this example is to sum Prices in column C when the Items in column B contain an asterisk (\*). The challenge is that the asterisk (\*) is reserved as a wildcard in functions like the SUMIFS function, so you can't match a literal occurrence of this character without using a special syntax...

FIND function videos
--------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20find%20text%20with%20a%20formula-thumb.png)](https://exceljet.net/videos/how-to-find-text-with-a-formula)

### [How to find text with a formula](https://exceljet.net/videos/how-to-find-text-with-a-formula)

When you're working with text, you often need to pinpoint the location of some bit of text inside another. You can then use this position to extract or replace the text. In this video we'll look at how to locate the position of one text string inside another. Let's take a look. Excel contains two...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20complex%20formula%20step%20by%20step-thumb.png)](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

### [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)

When you look at a complex formula in Excel you may be completely baffled at first glance, but all complex formulas are just small steps added together. Let me show you an example. Here we have a list of names. We want to pull out the first name from the full name. There's an Excel function called...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20extract%20a%20first%20name%20with%20a%20helper%20column-thumb.png)](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)

### [How to extract a first name with a helper column](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)

In this video we'll look at how to combine the FIND function with the LEFT function to extract the first name from a full name. Let's take a look. Excel's LEFT and RIGHT function s are easy to use when you know how many characters you want to extract. But what if you want to extract the first name...

Related functions
-----------------

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel REPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20replace%20function.png "Excel REPLACE function")](https://exceljet.net/functions/replace-function)

### [REPLACE Function](https://exceljet.net/functions/replace-function)

The Excel REPLACE function replaces characters at a specified position in a given text string with another text string. REPLACE a good solution when the text to replace can't easily be matched, but the location is predictable.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

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
    
*   [Remove last word](https://exceljet.net/formulas/remove-last-word)
    
*   [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    
*   [Remove text by variable position](https://exceljet.net/formulas/remove-text-by-variable-position)
    
*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)
    
*   [Get domain from email address](https://exceljet.net/formulas/get-domain-from-email-address)
    
*   [Get name from email address](https://exceljet.net/formulas/get-name-from-email-address)
    
*   [Basic outline numbering](https://exceljet.net/formulas/basic-outline-numbering)
    
*   [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)
    
*   [Highlight cells that contain one of many](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)
    

### Videos

*   [How to create a complex formula step by step](https://exceljet.net/videos/how-to-create-a-complex-formula-step-by-step)
    
*   [How to find text with a formula](https://exceljet.net/videos/how-to-find-text-with-a-formula)
    
*   [How to extract a first name with a helper column](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)
    

### Functions

*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

### Links

*   [Microsoft FIND function documentation](https://support.office.com/en-us/article/find-findb-functions-c7912941-af2a-4bdf-a553-d0d89b0a0628)
    

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