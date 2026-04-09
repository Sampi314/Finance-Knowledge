# Get first match cell contains - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-first-match-cell-contains

---

[Skip to main content](https://exceljet.net/formulas/get-first-match-cell-contains#main-content)

[](https://exceljet.net/formulas/get-first-match-cell-contains#)

*   [Previous](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [Next](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get first match cell contains
=============================

by Dave Bruns · Updated 10 Jun 2023

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")

Summary
-------

This article provides a method to search through a cell for one of several specified values, returning the first match found. The method uses the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 and the formula that appears in cell C5 of the worksheet is:

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(list,B5)),list,"na")
    

where **list** is the [named range](https://exceljet.net/glossary/named-range)
 E5:E11. As the formula is copied down, it returns the first match found in each cell. If no match is found, it returns "na". The value to return if no match is found can be customized as desired.

_Note: It is also possible to [list all matches a cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
 with a formula._

Generic formula
---------------

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(list,A1)),list)

Explanation 
------------

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named **list**) and a series of short sentences in the range B5:B16. The task is to add a formula in column C that will search through each sentence in B5:B16 and extract the first color in E5:E11 that is found in each sentence. If no matching colors are found, the formula should return the value "na". One way to solve this problem is with a formula that utilizes the ISNUMBER, SEARCH, and XLOOKUP functions. In older versions of Excel, you can use a formula based on INDEX and MATCH. Both methods are explained below.

### The functions

Let's first run through the functions used in the XLOOKUP formula:

1.  The [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
     checks if the given input or expression results in a number. It returns TRUE if the value is numeric, and FALSE if not.
    
2.  The [SEARCH function](https://exceljet.net/functions/search-function)
     is used to find the starting position of a specific substring within a string. The syntax is SEARCH(find\_text, within\_text, \[start\_num\]). If the substring (find\_text) is found, SEARCH returns the starting position as a number. If not, it results in an error.
    
3.  The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
     is a modern upgrade to the older VLOOKUP function. XLOOKUP allows you to search for a key value in a specified range or array, and return a corresponding value from another range or array. The syntax is XLOOKUP(lookup\_value, lookup\_array, return\_array, \[if\_not\_found\], \[match\_mode\], \[search\_mode\]).
    

### The formula

Now, let's look at the formula that appears in cell C5:

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(list,B5)),list,"na")
    

Here's how the formula works step by step, working from the inside out:

    SEARCH(list,B5)
    

The SEARCH function tries to find each color in the named range **list** (E5:E11) inside the sentence in cell B5. If a color is found, SEARCH returns the starting position as a number. If a color is not found, SEARCH returns an error. Because E5:E11 contains 7 colors, SEARCH returns 7 results in an array like this:

    {#VALUE!;30;#VALUE!;#VALUE!;#VALUE!;#VALUE!;5}

Notice the second value is 30 and the seventh value is 5. These numbers indicate the numeric positions of the colors "white" and "blue" in cell B5. The #VALUE! errors indicate colors in E5:E11 that were not found. We need to convert these values into something more useful and for that, we use the ISNUMBER function:

    ISNUMBER(SEARCH(list,B5))
    

This function is an error handler. Since the SEARCH function will return an error if the color is not found, ISNUMBER is used to turn the errors into FALSE (not a number) and the numbers (which indicate positions) into TRUE (is a number). The result from ISNUMBER is an array like this:

    {FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE}

Note we have TRUE in the second and seventh positions, indicating a match on the colors White and Blue. Next, we have the XLOOKUP function, which is the main part of the formula

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(list,B5)),list,"na")
    

After ISNUMBER and SEARCH are evaluated, the array from ISNUMBER is returned to XLOOKUP as the _lookup\_array_ argument:

    =XLOOKUP(TRUE,{FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE},list,"na")
    

XLOOKUP is configured to match the first TRUE in the array. When it finds a TRUE, it returns the corresponding color from the named range **list** (E5:E11). If no TRUE is found (i.e., no color from the list was found in the sentence), it returns "na". This value can be omitted or customized as desired. To recap, this formula extracts the first color found from the list (E5:E11) in each cell from B5 to B16. It does so by searching for each color in the sentence, checking whether the result is a number (indicating a match was found), and then returning the corresponding color.

### First match in sentence, or first match in list?

The language used in this example is ambiguous because it is not clear whether we are referring to the "first color found in the list of colors" or the "first color found in each sentence". These are two distinctly different operations. The formula above returns the first match found in the color list. If multiple colors from the list appear in a sentence, the formula will return the color that appears _first in the color list_, not the color that occurs _first in the sentence_. If instead, you want to find the first matched color in a sentence (ignoring the order of colors in the list) we need to use a different formula like this:

    =XLOOKUP(1,IFERROR(SEARCH(list,B5),0),list,"na",1)

This version of the formula has the same basic structure as the original formula. However, instead of using the ISNUMBER function as an error handler, it uses the [IFERROR function](https://exceljet.net/functions/iferror-function)
. IFERROR is set to catch errors from SEARCH and remap them to a zero (0) value. After IFERROR runs, the _lookup\_array_ inside XLOOKUP looks like this:

    =XLOOKUP(1,{0;34;0;0;0;0;5},list,"na",1)

XLOOKUP is configured to look for 1, and match\_mode is set to 1, which means "exact match or next larger value". In this case, XLOOKUP will match the last value (5), because it is the next larger value after 1, and return "white", since "white" appears before "blue" in the sentence.

> For more details on XLOOKUP, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
> .

### INDEX and MATCH

In older versions of Excel that do not provide XLOOKUP, you can solve this problem with a formula based on INDEX and MATCH:

    =INDEX(list,MATCH(TRUE,ISNUMBER(SEARCH(list,B5)),0))

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in Excel 2019 and older._

This formula works in much the same way as the XLOOKUP version above. Working from the inside out, we use [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
 to locate color matches in each sentence like this:

    ISNUMBER(SEARCH(list,B5)
    

As explained above, SEARCH will return the positions of any colors that appear in each sentence, and ISNUMBER will convert results from SEARCH into TRUE and FALSE values. The result is delivered to the MATCH function as the _lookup\_array_:

    =INDEX(list,MATCH(TRUE,{FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE},0))

Notice MATCH is configured to look for TRUE, and there are 2 TRUE values in the _lookup\_array_. The _match\_type_ argument is set to zero (0) to force an exact match. In this configuration, MATCH will match the first TRUE value and return 2 as a result directly to INDEX as the row\_num argument:

    =INDEX(list,2) // returns "blue"

INDEX will then return the second color in E5:E11 ("blue") as a final result.

### First match in sentence

As above, we need a different INDEX and MATCH formula to extract the first color that appears in a sentence, as opposed to the first color matched in **list** (E5:E11):

    =INDEX(list,MATCH(AGGREGATE(15,6,SEARCH(list,B5),1),SEARCH(list,B5),0))
    

The main trick in this formula is the _lookup\_value_ inside the MATCH function, which is calculated with the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
 like this:

    AGGREGATE(15,6,SEARCH(list,B5),1) // get min value
    

Here, we use AGGREGATE to get the minimum value in the results returned by SEARCH. We need AGGREGATE because the array will contain errors (returned by SEARCH when colors aren't found), and we need a function that will _ignore those errors_ and still give us the minimum numeric value. AGGREGATE works well here because it has an option to ignore errors. The result from AGGREGATE is 5, which is returned to MATCH as the _lookup\_value_. The _lookup\_array_ is created by the SEARCH function:

    {#VALUE!;34;#VALUE!;#VALUE!;#VALUE!;#VALUE!;5}

We don't use ISNUMBER in this case because we need to be able to find the number calculated by AGGREGATE. Back in the formula, we now have:

    =INDEX(list,MATCH(5,{#VALUE!;34;#VALUE!;#VALUE!;#VALUE!;#VALUE!;5},0))

The result from MATCH is 7, because 5 is the seventh value in the _lookup\_array_. MATCH returns this number to INDEX as the _row\_num_ argument:

    =INDEX(list,7) // returns "white"

The final result is "white", the first color found in the sentence.

> For more details on INDEX with MATCH, see [How to use the INDEX and MATCH](https://exceljet.net/articles/index-and-match)
> .

Related formulas
----------------

[![Excel formula: Categorize text with keywords](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/categorize_text_with_keywords.png "Excel formula: Categorize text with keywords")](https://exceljet.net/formulas/categorize-text-with-keywords)

### [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)

In this example, the goal is to categorize various expenses using the categories shown in column F and the keywords shown in column E. This is a case where it seems like we should perform a lookup operation of some kind, but the problem is that the keywords appear embedded in the text and the...

[![Excel formula: Get last match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match_cell_contains.png "Excel formula: Get last match cell contains")](https://exceljet.net/formulas/get-last-match-cell-contains)

### [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)

The goal is to search through a cell for one of several specified values and return the last match found when one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in column C...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Get all matches cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_all_matches_cell_contains.png "Excel formula: Get all matches cell contains")](https://exceljet.net/formulas/get-all-matches-cell-contains)

### [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)

In this example the goal is to check a cell for several things at once, and return a comma separated list of the things that were found. In other words, we want check for the colors seen in column E and list the colors found in column C. The formula in C5, copied down, is: =TEXTJOIN(", ",1,FILTER(...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: First match between two ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/first%20match%20between%20two%20ranges.png "Excel formula: First match between two ranges")](https://exceljet.net/formulas/first-match-between-two-ranges)

### [First match between two ranges](https://exceljet.net/formulas/first-match-between-two-ranges)

In this example the named range "range1" refers to cells B5:B8, and the named range "range2" refers to D5:D7. We are using named ranges for convenience and readability only; the formula works fine with regular cell references as well. The core of this formula is INDEX and MATCH. The INDEX function...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
    
*   [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [First match between two ranges](https://exceljet.net/formulas/first-match-between-two-ranges)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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