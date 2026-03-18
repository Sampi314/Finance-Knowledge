# Match long text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/match-long-text

---

[Skip to main content](https://exceljet.net/formulas/match-long-text#main-content)

[](https://exceljet.net/formulas/match-long-text#)

*   [Previous](https://exceljet.net/formulas/match-first-occurrence-does-not-contain)
    
*   [Next](https://exceljet.net/formulas/match-next-highest-value)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Match long text
===============

by Dave Bruns · Updated 20 Mar 2021

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[LEFT](https://exceljet.net/functions/left-function)

[MID](https://exceljet.net/functions/mid-function)

[EXACT](https://exceljet.net/functions/exact-function)

![Excel formula: Match long text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/match%20long%20text.png "Excel formula: Match long text")

Summary
-------

To match text longer than 255 characters with the [MATCH function](https://exceljet.net/functions/match-function)
, you can use the [LEFT](https://exceljet.net/functions/left-function)
, [MID](https://exceljet.net/functions/mid-function)
, and [EXACT](https://exceljet.net/functions/exact-function)
 functions to parse and compare text, as explained below. In the example shown, the formula in G5 is:

    =MATCH(1,EXACT(LEFT(E5,255),LEFT(data,255))*EXACT(MID(E5,256,255),MID(data,256,255)),0)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

_Note: this formula performs a case-sensitive comparison. See notes below for other options._

Generic formula
---------------

    =MATCH(1,EXACT(LEFT(A1,255),LEFT(rng,255))*EXACT(MID(A1,256,255),MID(rng,256,255)),0)

Explanation 
------------

The MATCH function has a limit of 255 characters for the lookup value. If you try to use longer text, MATCH will return a #VALUE error. To workaround this limit you can use boolean logic and the LEFT, MID, and EXACT functions to parse and compare text.

_Note: this formula performs an exact match when both the lookup value and array values are greater than 255 characters. See below for other options._

The string we are testing with in cell E5 is 373 characters as follows:

_Lorem ipsum dolor amet put a bird on it listicle trust fund, unicorn vaporware bicycle rights you probably haven't heard of them mustache. Forage helvetica crusty semiotics actually heirloom. Tumblr poutine unicorn godard try-hard before they sold out narwhal meditation kitsch waistcoat fixie twee literally hoodie retro. Messenger bag hell of crusty green juice artisan._

At the core, this is just a MATCH formula, set up to look for 1 in exact match mode:

    =MATCH(1,array,0)
    

The array in the formula above contains only 1s and 0s, and 1s represent matching text. This array is constructed by the following expression:

    EXACT(LEFT(E5,255),LEFT(data,255))*EXACT(MID(E5,256,255),MID(data,256,255))
    

This expression itself has two parts. On the left we have:

    EXACT(LEFT(E5,255),LEFT(data,255)) // compare first 255 chars
    

Here, the LEFT function extracts the first 255 characters from E5, and from all cells in the named range data (B5:B15). Because data contains 11 text strings, LEFT will generate 11 results.

The EXACT function then compares the single string from E5 against all the 11 strings returned by LEFT. EXACT returns 11 results in an array like this:

    {FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE}
    

On the right, we have another expression:

    EXACT(MID(E5,256,255),MID(data,256,255) // compare next 255 chars
    

This is exact the same approach as used with LEFT, but here we use the MID function to extract the next 255 characters of text. The EXACT function again returns 11 results:

    {TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE}
    

When the two arrays above are multiplied by one another, the math operation coerces the TRUE FALSE values into 1s and 0s. Following the rules of boolean arithmetic, the result is an array like this:

    {0;0;0;0;0;0;0;0;0;1;0}
    

which is returned directly to MATCH as the lookup array. The formula can now be resolved to:

    =MATCH(1,{0;0;0;0;0;0;0;0;0;1;0},0)
    

The MATCH function performs an exact match, and returns a final result of 10, which represents the tenth text string in B5:B15.

_Note: the text length shown in the example is calculated with the [LEN function](https://exceljet.net/functions/len-function)
. It appears for reference only._

### Case-insensitive option

The EXACT function is case-sensitive, so the formula above will respect case.

To perform a case-insensitive match with long text, you use the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
 functions as follows:

    =MATCH(1,ISNUMBER(SEARCH(LEFT(E5,255),LEFT(data,255)))*ISNUMBER(SEARCH(MID(E5,256,255),MID(data,256,255))),0)
    

The overall structure of this formula is identical to the example above, but the SEARCH function is used instead of EXACT to compare text (explained in detail here).

Unlike EXACT, the SEARCH function also supports [wildcards](https://exceljet.net/glossary/wildcard)
.

### With XMATCH

The [XMATCH function](https://exceljet.net/functions/xmatch-function)
 does not have the same 255 character limit as MATCH. To perform an similar match on long text with XMATCH, you can use the much simpler formula below:

    =XMATCH(E5,data)
    

_Note: XMATCH supports wildcards, but is not case-sensitive._

### MATCH with SEARCH

The example above shows a worksheet where the lookup value and some of the entries in the lookup array are longer than 255 characters, and the match type is _exact_. If the lookup value is _less than_ 255 characters, but some values in the lookup array are _greater than_ 255 characters, you can use MATCH function with the [SEARCH function](https://exceljet.net/functions/search-function)
 like this:

    =MATCH(1,--ISNUMBER(SEARCH(E5,data)),0)
    

This formula works when text in E5 is less than 255 characters, but values in column B are greater than 255 characters. The behavior however is different. Instead of finding an _exact match_ (as in the example above) this formula performs a _contains match._ SEARCH will return a number if the text in E5 appears _anywhere_ in a cell that is part of the named range **data**. [Detailed explanation here](https://exceljet.net/formulas/cell-contains-specific-text)
. The equivalent formula using XMATCH with wildcards is:

    =XMATCH("*"&E5&"*",data,2)
    

A similar wildcard search with the MATCH function _won't work_ because of the 255 character limitation.

Related formulas
----------------

[![Excel formula: Count long numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20long%20numbers.png "Excel formula: Count long numbers")](https://exceljet.net/formulas/count-long-numbers)

### [Count long numbers](https://exceljet.net/formulas/count-long-numbers)

In this example the goal is to count numbers longer than 15 digits with a formula. The COUNTIF function may seem like this logical choice. However, if you try to count very long numbers (16+ digits) in a range with the COUNTIF function, you may see incorrect results, due to a bug in how RACON...

[![Excel formula: Find longest string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_longest_string.png "Excel formula: Find longest string")](https://exceljet.net/formulas/find-longest-string)

### [Find longest string](https://exceljet.net/formulas/find-longest-string)

The goal is to find the longest text string in the range B5:B16. At the core, this is a lookup problem that requires creating a value (the string length) that does not exist in the data as part of the formula. The easiest way to solve this problem is with the XLOOKUP function or the FILTER function...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count long numbers](https://exceljet.net/formulas/count-long-numbers)
    
*   [Find longest string](https://exceljet.net/formulas/find-longest-string)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

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