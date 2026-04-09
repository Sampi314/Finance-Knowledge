# Excel SEARCH function | Exceljet

**Source:** https://exceljet.net/functions/search-function

---

[Skip to main content](https://exceljet.net/functions/search-function#main-content)

[](https://exceljet.net/functions/search-function#)

*   [Previous](https://exceljet.net/functions/right-function)
    
*   [Next](https://exceljet.net/functions/substitute-function)
    

Excel 2003

[Text](https://exceljet.net/functions#Text)

SEARCH Function
===============

by Dave Bruns · Updated 22 Nov 2024

Related functions 
------------------

[FIND](https://exceljet.net/functions/find-function)

[REPLACE](https://exceljet.net/functions/replace-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")

Summary
-------

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive.

Purpose 
--------

Get the location of substring in a string

Return value 
-------------

A number representing the location of substring

Syntax
------

    =SEARCH(find_text,within_text,[start_num])

*   _find\_text_ - The substring to find.
*   _within\_text_ - The text to search within.
*   _start\_num_ - \[optional\] Starting position. Optional, defaults to 1.

Using the SEARCH function 
--------------------------

The SEARCH function returns the position (as a number) of one [text string](https://exceljet.net/glossary/text-value)
 inside another. In the most basic case, you can use SEARCH to locate the position of a substring in a text string. You can also use SEARCH to check if a cell contains specific text. SEARCH is _not case-sensitive_, which means it does not distinguish between uppercase and lowercase letters. In addition, SEARCH supports the use of [wildcards](https://exceljet.net/glossary/wildcard)
 like \*?~, allowing more flexible search patterns. Here are a few key points to remember about the SEARCH function:

*   SEARCH returns the _position_ of one text string inside another as a _number_.
*   When SEARCH cannot locate the search string, it returns a #VALUE error.
*   If the search string appears more than once, SEARCH returns the _first position_.
*   SEARCH is _not case-sensitive_ and will treat "Apple" and "apple" as the same text strings.
*   SEARCH _does_ support wildcards like \*?~ when searching for text.
*   SEARCH will return 1 if the search string (_find\_text_) is empty, which can cause a false positive when _find\_text_ is an empty cell.

_Note: The SEARCH function is similar to the FIND function. Both functions return the position of one text string inside another. However, unlike FIND, SEARCH is not case-sensitive and_ does _support wildcards._

Video: [How to find text with a formula](https://exceljet.net/videos/how-to-find-text-with-a-formula)

### Basic syntax

The basic syntax of the SEARCH function looks like this

    SEARCH(find_text,within_text,[start_num])

*   _find\_text_: The text you want to find (the search string). This is a substring that Excel searches for within another text string. The text must be entered in double quotes if you are hardcoding the value into the formula. Otherwise, you can refer to a cell that contains the text.
*   _within\_text_: The text string that contains the text you want to find. Often, this is a cell reference that contains the text, but you can also hardcode a text string in double quotes.
*   _start\_num_ (optional): The character at which to begin searching as a numeric position. The first character in _within\_text_ is considered position 1. If omitted, the search starts at the beginning of the _within\_text_.

### Basic example

The [SEARCH function](https://exceljet.net/functions/search-function)
 is designed to look inside a text string for a specific substring. When SEARCH locates the substring, it returns the position of the substring in the text as a number. If the substring is not found, SEARCH returns a #VALUE error. For example:

    =SEARCH("p","apple") // returns 2
    =SEARCH("z","apple") // returns #VALUE!
    =SEARCH("apple","Pineapple") // returns 5

Note that text values entered directly into SEARCH must be enclosed in double quotes (""). Unlike the FIND function, the SEARCH function is _not_ case-sensitive:

    =SEARCH("a","Apple") // returns 1
    =SEARCH("A","Apple") // returns 1
    =SEARCH("Apple","Pineapple") // returns 5

The worksheet below shows the same examples translated into formulas based on cell references:

![SEARCH function - basic example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_search_function_basic_example.png "SEARCH function - basic example")

Again, notice that SEARCH is not case-sensitive, as seen in D8 and D10.

### Forcing a TRUE or FALSE result

By default, the SEARCH function returns a number when a search string is found and a #VALUE! error when not. This is inconvenient in cases where you simply want to know if the search string has been found or not. To force a TRUE or FALSE result, you can [nest](https://exceljet.net/glossary/nesting)
 the SEARCH function inside the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. ISNUMBER returns TRUE for numeric values and FALSE for anything else. If SEARCH locates the substring, it returns the position as a number, and ISNUMBER returns TRUE:

    =ISNUMBER(SEARCH("p","apple")) // returns TRUE
    =ISNUMBER(SEARCH("z","apple")) // returns FALSE

If SEARCH _doesn't_ locate the substring, it returns an error, and ISNUMBER returns FALSE. This approach allows for support for wildcards in the search. For a more detailed explanation of this approach, with many more examples, [see this example](https://exceljet.net/formulas/cell-contains-specific-text)
.

### If cell contains

Once you have a TRUE or FALSE result, you can combine the SEARCH function with the [IF function](https://exceljet.net/functions/if-function)
 to create "if cell contains" logic. The generic pattern for this formula looks like this:

    =IF(ISNUMBER(SEARCH(substring,A1)), "Yes", "No")
    

Instead of returning TRUE or FALSE, the formula above will return "Yes" if the _substring_ is found and "No" if not. You can use the same idea to mark or "flag" items of interest. For example, in the worksheet below, we are using SEARCH with IF to flag email addresses that contain "abc" with an "x".

![SEARCH function - using SEARCH with the IF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_search_function_with_the_if_function.png "SEARCH function - using SEARCH with the IF function")

The formula in C5, copied down, is:

    =IF(ISNUMBER(SEARCH("abc",B5)),"x","")

### Start number

The SEARCH function has an optional [argument](https://exceljet.net/glossary/function-argument)
 called _start\_num_ that controls where SEARCH should begin looking for a substring. To find the first match of "x" in upper or lowercase, you can omit _start\_num_, which defaults to 1:

    =SEARCH("x","20 x 30 x 50") // returns 4

SEARCH returns 4 since the first "x" appears at position 4. To find the second "x", enter 5 for _start\_num_:

    =SEARCH("x","20 x 30 x 50",5) // returns 9
    

In this case, SEARCH returns 9 since it starts searching after the first "x". You can effectively find the second "x" in cell A1 in a single formula by using the SEARCH function twice like this:

    =SEARCH("x",A1,SEARCH("x",A1)+1)

The _inner_ SEARCH returns the location of the first "x". We then add 1, and the result is used as the _start\_num_ in the _outer_ SEARCH. The result is the location of the second "x" in cell A1.

### Wildcards

Although SEARCH is _not_ case-sensitive, it does support [wildcards](https://exceljet.net/glossary/wildcard)
 (\*?~), which makes it a versatile tool for finding substrings in text. This allows for more complex searches, including basic pattern matching. For example, the question mark (?) wildcard matches any one character. The formula below looks for a 3-character substring beginning with "x" and ending in "y":

    =ISNUMBER(SEARCH("x?z","xyz")) // TRUE
    =ISNUMBER(SEARCH("x?z","xbz")) // TRUE
    =ISNUMBER(SEARCH("x?z","xyy")) // FALSE

The asterisk (\*) wildcard is not as useful in the SEARCH function because SEARCH _already looks for a substring_. For example, it might seem like the following formula will test for a value that ends with "z":

    =SEARCH("*z",text)

However, because SEARCH _automatically looks for a substring_, the following formulas all return 1 as a result, even though the text in the first formula is the only text that ends with "z":

    =SEARCH("*z","XYZ") // returns 1
    =SEARCH("*z","XYZXY") // returns 1
    =SEARCH("*z","XYZXY123") // returns 1
    =SEARCH("x*z","XYZXY123") // returns 1

However, it is possible to use the asterisk (\*) wildcard like this: 

    =SEARCH("x*2*b","AAAXYZ123ABCZZZ") // returns 4
    =SEARCH("x*2*b","NXYZ12563JKLB") // returns 2

Here we are looking for "x", "2", and "b" in that order, with any number of characters in between. Finally, use the tilde (~) as an escape character to indicate that the next character is a _literal_ like this:

    =SEARCH("~*","apple*") // returns 6
    =SEARCH("~?","apple?") // returns 6
    =SEARCH("~~","apple~") // returns 6

The above formulas use SEARCH to find a _literal_ asterisk (\*), question mark (?), and tilde (~) in that order.

### More advanced formulas

The SEARCH function shows up in many more advanced formulas that work with text. SEARCH is often used instead of FIND when wildcards are needed or when the goal is to perform a case-insensitive search. Here are a few examples:

*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
     - tests a cell for more than one text string simultaneously, using wildcards for flexible matching.
*   [Sum if cells contain either x or y](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)
     - sums numbers when associated cells contain one value or another, utilizing wildcard searches.
*   [Filter if text contains](https://exceljet.net/formulas/filter-text-contains)
     - extract values from a data set with "contains-type" logic, leveraging wildcards for comprehensive searching.
*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
     - return an appropriate category based on if a cell contains one of several text values, using wildcards to match patterns.
*   [Filter based on partial match](https://exceljet.net/formulas/filter-with-partial-match)
     - extract records from an Excel Table based on a partial match, using wildcards for pattern recognition.

### Notes

*   The SEARCH function returns the location of the first _find\_text_ in _within\_text_ as a number.
*   SEARCH returns #VALUE if _find\_text_ is not found.
*   _Start\_num_ is optional and defaults to 1.
*   SEARCH returns 1 when _find\_text_ is empty. This can cause a false positive when _find\_text_ is an empty cell.
*   SEARCH _is_ not case-sensitive but _does_ support wildcards.
*   Use the [FIND function](https://exceljet.net/functions/find-function)
     for a case-sensitive search.
*   SEARCH allows the wildcard characters question mark (?) and asterisk (\*), in _find\_text_.
    *   ? matches any single character
    *   \* matches any sequence of characters.
    *   To find a literal ? or \* or ~, use a tilde (~) before the character, i.e. ~\*, ~?,~~.

SEARCH function examples
------------------------

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: Lookup last file revision](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20last%20file%20revision.png "Excel formula: Lookup last file revision")](https://exceljet.net/formulas/lookup-last-file-revision)

### [Lookup last file revision](https://exceljet.net/formulas/lookup-last-file-revision)

Context In this example, we have a number of file versions listed in a table with a date and user name. Note that file names are repeated, except for the code appended at the end to represent version ("CA", "CB", "CC", "CD", etc.). For a given file, we want to locate the position (row number) for...

[![Excel formula: Get last match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match_cell_contains.png "Excel formula: Get last match cell contains")](https://exceljet.net/formulas/get-last-match-cell-contains)

### [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)

The goal is to search through a cell for one of several specified values and return the last match found when one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in column C...

[![Excel formula: XLOOKUP match text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20match%20text%20contains.png "Excel formula: XLOOKUP match text contains")](https://exceljet.net/formulas/xlookup-match-text-contains)

### [XLOOKUP match text contains](https://exceljet.net/formulas/xlookup-match-text-contains)

The XLOOKUP function contains built-in support for wildcards, but this feature must be enabled explicitly by setting match mode to the number 2. In the example shown, XLOOKUP is configured to match the value entered in cell E5, which may appear anywhere in the lookup values in B5:B15. The formula...

[![Excel formula: Data validation must not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data_validation_must_not_contain.png "Excel formula: Data validation must not contain")](https://exceljet.net/formulas/data-validation-must-not-contain)

### [Data validation must not contain](https://exceljet.net/formulas/data-validation-must-not-contain)

In this example, the goal is to construct a data validation rule that will prevent any one of a list of values from being entered. Data validation rules are triggered when a user adds or changes a cell value. One option is to use a formula to validate user input, which is the approach taken in the...

[![Excel formula: IF with wildcards](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/IF_with_wildcards.png "Excel formula: IF with wildcards")](https://exceljet.net/formulas/if-with-wildcards)

### [IF with wildcards](https://exceljet.net/formulas/if-with-wildcards)

The goal of this formula is to verify whether the values in column B follow the format xx-xxxx-xxx, where "x" represents any single character. The IF function doesn't support wildcards directly, so we can't use IF by itself. Instead, we can combine the IF function with the COUNTIF function, which...

[![Excel formula: Sum if cells contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_either_x_or_y.png "Excel formula: Sum if cells contain either x or y")](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)

### [Sum if cells contain either x or y](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)

In this example, the goal is to sum numbers in the range C5:C16 when text in the range B5:B16 contains the substring "red" OR the substring "blue". In other words, if the text in B5:B16 contains either of these two text values in any location, the corresponding number in C5:C16 should be included...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: Count keywords cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20keywords%20cell%20contains.png "Excel formula: Count keywords cell contains")](https://exceljet.net/formulas/count-keywords-cell-contains)

### [Count keywords cell contains](https://exceljet.net/formulas/count-keywords-cell-contains)

Note: if a keyword appears more than once in a given cell, it will only be counted once. In other words, the formula only counts instances of different keywords. The core of this formula is the ISNUMBER + SEARCH approach to finding text in a cell, which is explained in more detail here . In this...

[![Excel formula: Highlight cells that contain one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20one%20of%20many.png "Excel formula: Highlight cells that contain one of many")](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)

### [Highlight cells that contain one of many](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)

Working from the inside out, this part of the formula searches each cell in B4:B11 for all values in the named range "things": --ISNUMBER(SEARCH(things,B4) The SEARCH function returns the position of the value if found, and the #VALUE error if not found. For B4, the results come back in an array...

[![Excel formula: Match first occurrence does not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/match%20first%20occurrence%20does%20not%20contain.png "Excel formula: Match first occurrence does not contain")](https://exceljet.net/formulas/match-first-occurrence-does-not-contain)

### [Match first occurrence does not contain](https://exceljet.net/formulas/match-first-occurrence-does-not-contain)

This formula depends on a TRUE or FALSE result from a logical test, where FALSE represents the value you are looking for. In the example, the logical test is data="red", entered as the lookup\_array argument in the MATCH function: =MATCH(FALSE,data="red",0) Once the test is run, it returns an array...

[![Excel formula: FILTER case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20case%20sensitive.png "Excel formula: FILTER case-sensitive")](https://exceljet.net/formulas/filter-case-sensitive)

### [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)

This formula relies on the FILTER function to retrieve data based on a logical test . The array argument is provided as B5:D15, which contains all of the data without headers. The include argument is an expression based on the EXACT function: EXACT(B5:B15,"RED") The EXACT function compares two text...

[![Excel formula: Count cells that do not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain.png "Excel formula: Count cells that do not contain")](https://exceljet.net/formulas/count-cells-that-do-not-contain)

### [Count cells that do not contain](https://exceljet.net/formulas/count-cells-that-do-not-contain)

In this example, the goal is to count cells that do not contain a specific substring. This problem can be solved with the COUNTIF function or the SUMPRODUCT function . Both approaches are explained below. Although COUNTIF is not case-sensitive, the SUMPRODUCT version of the formula can be adapted...

[![Excel formula: FILTER with partial match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20partial%20match.png "Excel formula: FILTER with partial match")](https://exceljet.net/formulas/filter-with-partial-match)

### [FILTER with partial match](https://exceljet.net/formulas/filter-with-partial-match)

In this example, the goal is to extract a set of records that match a partial text string . To keep things simple, we are only matching one field in the data, the last name ("Last"). The core operation of this formula comes from the FILTER function (new in Excel 365 ) which extracts matching data...

SEARCH function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20find%20text%20with%20a%20formula-thumb.png)](https://exceljet.net/videos/how-to-find-text-with-a-formula)

### [How to find text with a formula](https://exceljet.net/videos/how-to-find-text-with-a-formula)

When you're working with text, you often need to pinpoint the location of some bit of text inside another. You can then use this position to extract or replace the text. In this video we'll look at how to locate the position of one text string inside another. Let's take a look. Excel contains two...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20extract%20a%20first%20name%20with%20a%20helper%20column-thumb.png)](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)

### [How to extract a first name with a helper column](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)

In this video we'll look at how to combine the FIND function with the LEFT function to extract the first name from a full name. Let's take a look. Excel's LEFT and RIGHT function s are easy to use when you know how many characters you want to extract. But what if you want to extract the first name...

Related functions
-----------------

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

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

*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [IF with wildcards](https://exceljet.net/formulas/if-with-wildcards)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [Cell contains some words but not others](https://exceljet.net/formulas/cell-contains-some-words-but-not-others)
    
*   [LAMBDA contains which things](https://exceljet.net/formulas/lambda-contains-which-things)
    
*   [Data validation must not contain](https://exceljet.net/formulas/data-validation-must-not-contain)
    
*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    

### Videos

*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to find text with a formula](https://exceljet.net/videos/how-to-find-text-with-a-formula)
    
*   [How to extract a first name with a helper column](https://exceljet.net/videos/how-to-extract-a-first-name-with-a-helper-column)
    

### Functions

*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

### Links

*   [Microsoft SEARCH function documentation](https://support.office.com/en-us/article/search-searchb-functions-9ab04538-0e55-4719-a72e-b6f54513b495)
    

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