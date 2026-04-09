# Cell contains specific text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cell-contains-specific-text

---

[Skip to main content](https://exceljet.net/formulas/cell-contains-specific-text#main-content)

[](https://exceljet.net/formulas/cell-contains-specific-text#)

*   [Previous](https://exceljet.net/formulas/cell-contains-some-words-but-not-others)
    
*   [Next](https://exceljet.net/formulas/cell-contains-specific-words)
    

[Text](https://exceljet.net/formulas#Text)

Cell contains specific text
===========================

by Dave Bruns · Updated 12 Feb 2025

Related functions 
------------------

[SEARCH](https://exceljet.net/functions/search-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[FIND](https://exceljet.net/functions/find-function)

[REGEXTEST](https://exceljet.net/functions/regextest-function)

![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")

Summary
-------

To check if a cell contains specific text (i.e. a substring), you can use the [SEARCH function](https://exceljet.net/functions/search-function)
 together with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. In the example shown, the formula in D5 is:

    =ISNUMBER(SEARCH(C5,B5))
    

This formula returns TRUE if the substring in cell C5 is found in the text from cell B5. Otherwise, it returns FALSE. Note the SEARCH function is _not_ case-sensitive. See below for a case-sensitive formula.

Generic formula
---------------

    =ISNUMBER(SEARCH(substring,A1))

Explanation 
------------

In this example, the goal is to test a value in a cell to see if it contains a specific _substring_. Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports [wildcards](https://exceljet.net/glossary/wildcard)
 but is _not_ case-sensitive, while the FIND function _is_ case-sensitive but _does not_ support wildcards. Both functions return the _position_ of the substring in the text as a number when it is found and a #VALUE! error when the substring is not found. However, it is not obvious how to get a TRUE or FALSE result when the goal is simply to test for the existence of the substring. The standard approach is to wrap these functions in the ISNUMBER function to force a TRUE or FALSE result. ISNUMBER will return TRUE for a numeric result (a match) and FALSE when the result is #VALUE! (no-match).

> Excel 365 now [supports regular expressions](https://exceljet.net/articles/regular-expressions-in-excel)
>  (regex), a powerful tool for pattern-matching. The [REGEXTEST function](https://exceljet.net/functions/regextest-function)
>  offers a direct way to test for specific text with a TRUE or FALSE result. Because REGEXTEST uses regex, it can be configured to use precise patterns for advanced use cases. See below for basic examples.

### SEARCH function (not case-sensitive)

The [SEARCH function](https://exceljet.net/functions/search-function)
 is designed to look inside a text string for a specific substring. If SEARCH finds the substring, it returns the _position_ of the substring in the text as a number. If the substring is not found, SEARCH returns a #VALUE error. For example:

    =SEARCH("p","apple") // returns 2
    =SEARCH("z","apple") // returns #VALUE!

To force a TRUE or FALSE result, we use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. ISNUMBER returns TRUE for numeric values and FALSE for anything else. So, if SEARCH finds the substring, it returns the position as a number, and ISNUMBER returns TRUE:

    =ISNUMBER(SEARCH("p","apple")) // returns TRUE
    =ISNUMBER(SEARCH("z","apple")) // returns FALSE

If SEARCH _doesn't_ find the substring, it returns an error, which causes the ISNUMBER to return FALSE.

### Wildcards

Although SEARCH is _not_ case-sensitive, it does support [wildcards](https://exceljet.net/glossary/wildcard)
 (\*?~). For example, the question mark (?) wildcard matches _any one character_. The formula below looks for a 3-character substring beginning with "x" and ending in "y":

    =ISNUMBER(SEARCH("x?z","xyz")) // TRUE
    =ISNUMBER(SEARCH("x?z","xbz")) // TRUE
    =ISNUMBER(SEARCH("x?z","xyy")) // FALSE

The asterisk (\*) wildcard matches zero or more characters. This wildcard is not as useful in the SEARCH function because SEARCH _already looks for a substring_. For example, it might seem like the following formula will test for a value that ends with "z":

    =ISNUMBER(SEARCH("*z",text))

However, because SEARCH _automatically looks for a substring_, the following formulas all return 1 as a result, even though the text in the first formula is the only text that ends with "z":

    =SEARCH("*z","XYZ") // returns 1
    =SEARCH("*z","XYZXY") // returns 1
    =SEARCH("*z","XYZXY123") // returns 1
    =SEARCH("x*z","XYZXY123") // returns 1

This means the asterisk (\*) is not a reliable way to test for "ends with". However, you can use the asterisk (\*) wildcard like this: 

    =SEARCH("x*2*b","AAAXYZ123ABCZZZ") // returns 4
    =SEARCH("x*2*b","NXYZ12563JKLB") // returns 2

Here we are looking for "x", "2", and "b" in that order, with any number of characters in between. Finally, you can use the tilde (~) as an escape character to indicate that the next character is a _literal_ like this:

    =SEARCH("~*","apple*") // returns 6
    =SEARCH("~?","apple?") // returns 6
    =SEARCH("~~","apple~") // returns 6

The above formulas use SEARCH to find a _literal_ asterisk (\*), question mark (?), and tilde (~) in that order.

### FIND function (case-sensitive)

Like the SEARCH function, the [FIND function](https://exceljet.net/functions/find-function)
 returns the _position_ of a substring in text as a number, and an error if the substring is not found. However, _unlike_ the SEARCH function, the FIND function respects case:

    =FIND("A","Apple") // returns 1
    =FIND("A","apple") // returns #VALUE!

To make a case-sensitive version of the formula, just replace the SEARCH function with the FIND function in the formula above:

    =ISNUMBER(FIND(substring,A1))
    

The result is a case-sensitive search:

    =ISNUMBER(FIND("A","Apple")) // returns TRUE
    =ISNUMBER(FIND("A","apple")) // returns FALSE

### REGEXTEST function (very powerful)

The [REGEXTEST function](https://exceljet.net/functions/regextest-function)
 tests for text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable pattern. The generic syntax for REGEXTEST looks like this:

    =REGEXTEST(text,pattern)

The _text_ is the text to search within, and the _pattern_ is the text to search for, which can be a hardcoded text string or a combination of special characters used to define regex patterns. The result from REGEXTEST is TRUE or FALSE, so there is no need for ISNUMBER:

    =REGEXTEST("apple","a") // returns TRUE
    =REGEXTEST("apple","z") // returns FALSE
    

Note that REGEXTEST is case-sensitive by default:

    =REGEXTEST("apple","A") // returns FALSE

The power of REGEXTEST comes from its ability to use regex patterns. Here are a few simple examples that check text in cell A1 for various things:

    =REGEXTEST(A1,"[0-9]") // test for a number
    =REGEXTEST(A1,"[A-Z]") // test for an uppercase character
    =REGEXTEST(A1,"\d{3}") // test for a 3-digit number
    =REGEXTEST(A1,"[A-Z]{3}") // test for 3 uppercase characters together

Here are the examples above applied to a text string:

    =REGEXTEST("apple9","[0-9]") // returns TRUE
    =REGEXTEST("appLe","[A-Z]") // returns TRUE
    =REGEXTEST("apple123","\d{3}") // returns TRUE
    =REGEXTEST("appleABC","[A-Z]{3}") // // returns TRUE

For an overview of regex in Excel, see [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
. 

### If cell contains

To return a custom result when a cell contains specific text, you can wrap the formulas above inside the [IF function](https://exceljet.net/functions/if-function)
 like this:

    =IF(ISNUMBER(SEARCH(substring,A1)),"Yes","No")
    =IF(ISNUMBER(FIND(substring,A1)),"Yes","No")
    =IF(REGEXTEST(A1,substring),"Yes","No")
    

Instead of returning TRUE or FALSE, the formulas above will return "Yes" if the _substring_ is found and "No" if not. You are free to customize the values returned by IF as you like.

### Test for more than one search string

To test a cell for more than one thing (i.e. for one of many substrings), [see this example formula](https://exceljet.net/formulas/cell-contains-one-of-many-things)
.

Related formulas
----------------

[![Excel formula: Cell contains specific words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_words.png "Excel formula: Cell contains specific words")](https://exceljet.net/formulas/cell-contains-specific-words)

### [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)

In this example, the goal is to test the text in a cell and return TRUE if it contains one or more specific words, and FALSE if not. Notice the emphasis here is on words, not substrings. For example, if we are testing for the word "green" and the text contains the word "evergreen" but not the word...

[![Excel formula: Cell begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_begins_with.png "Excel formula: Cell begins with")](https://exceljet.net/formulas/cell-begins-with)

### [Cell begins with](https://exceljet.net/formulas/cell-begins-with)

In this example, the goal is to test values in column B to see if they begin with a specific text string, which is "xyz" in the worksheet shown. This problem can be solved with the LEFT function, as explained below. LEFT function The LEFT function extracts a given number of characters from the left...

[![Excel formula: Cell ends with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_ends_with.png "Excel formula: Cell ends with")](https://exceljet.net/formulas/cell-ends-with)

### [Cell ends with](https://exceljet.net/formulas/cell-ends-with)

In this example, the goal is to test values in column B to see if they end with a specific text string, which is "jwb" in the worksheet shown. This problem can be solved with the RIGHT function, as explained below. RIGHT function The RIGHT function extracts a given number of characters from the...

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Categorize text with keywords](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/categorize_text_with_keywords.png "Excel formula: Categorize text with keywords")](https://exceljet.net/formulas/categorize-text-with-keywords)

### [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)

In this example, the goal is to categorize various expenses using the categories shown in column F and the keywords shown in column E. This is a case where it seems like we should perform a lookup operation of some kind, but the problem is that the keywords appear embedded in the text and the...

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

### [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both text strings . When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't...

Related functions
-----------------

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel REGEXTEST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regextest_function.png "Excel REGEXTEST function")](https://exceljet.net/functions/regextest-function)

### [REGEXTEST Function](https://exceljet.net/functions/regextest-function)

The Excel REGEXTEST function tests for the existence of text defined by a given pattern. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable pattern. The result from REGEXTEST is TRUE or FALSE....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)
    
*   [Cell begins with](https://exceljet.net/formulas/cell-begins-with)
    
*   [Cell ends with](https://exceljet.net/formulas/cell-ends-with)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
    
*   [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    

### Functions

*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [REGEXTEST Function](https://exceljet.net/functions/regextest-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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