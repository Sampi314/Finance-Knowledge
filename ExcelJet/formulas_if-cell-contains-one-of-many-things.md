# If cell contains one of many things - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-contains-one-of-many-things

---

[Skip to main content](https://exceljet.net/formulas/if-cell-contains-one-of-many-things#main-content)

[](https://exceljet.net/formulas/if-cell-contains-one-of-many-things#)

*   [Previous](https://exceljet.net/formulas/group-times-into-unequal-buckets)
    
*   [Next](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)
    

[Grouping](https://exceljet.net/formulas#Grouping)

If cell contains one of many things
===================================

by Dave Bruns · Updated 9 Nov 2021

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")

Summary
-------

To test a cell for one of several strings, and return a custom result for the first match found, you can use an [INDEX / MATCH formula](https://exceljet.net/articles/index-and-match)
 based on the [SEARCH function](https://exceljet.net/functions/match-function)
. In the example shown, the formula in C5 is:

    {=INDEX(results,MATCH(TRUE,ISNUMBER(SEARCH(things,B5)),0))}
    

where **things** (E5:E8 ) and **results** (F5:F8) are [named ranges](https://exceljet.net/glossary/named-range)
. This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter.

_Note: this formula is designed to return a different result for each value that may be found. If you only want to test for one of many values and return a single result when found, [see this formula](https://exceljet.net/formulas/cell-contains-one-of-many-things)
._

Generic formula
---------------

    {=INDEX(results,MATCH(TRUE,ISNUMBER(SEARCH(things,A1)),0))}

Explanation 
------------

This formula uses two [named ranges](https://exceljet.net/glossary/named-range)
: **things**, and **results**. If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use [absolute references](https://exceljet.net/glossary/absolute-reference)
 instead.

The core of this formula is this snippet:

    ISNUMBER(SEARCH(things,B5)
    

This is based on another formula ([explained in detail here](https://exceljet.net/formulas/cell-contains-specific-text)
) that checks a cell for a single substring. If the cell contains the substring, the formula returns TRUE. If not, the formula returns FALSE.

Because we are giving the [SEARCH function](https://exceljet.net/functions/search-function)
 more than one thing to look for, in the named range **things**, it will give us more the one result, in an array that looks like this:

    {#VALUE!;9;#VALUE!;#VALUE!}
    

Numbers represent matches in **things**, errors represent items that were not found.

To simplify the array, we use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 to convert all items in the array to either TRUE or FALSE. Any valid number becomes TRUE, and any error (i.e. a thing not found) becomes FALSE. The result is an array like this:

    {FALSE;TRUE;FALSE;FALSE}
    

which goes into the MATCH function as the _lookup\_array_ argument, with a _lookup\_value_ of TRUE:

    MATCH(TRUE,{FALSE;TRUE;FALSE;FALSE},0) // returns 2
    

MATCH then returns the position of first TRUE found, 2 in this case.

Finally, we use the [INDEX function](https://exceljet.net/functions/index-function)
 to retrieve a result from the named range **results** at that same position:

    =INDEX(results,2) // returns "found red"
    

You can customize the **results** range with whatever values make sense in your use case.

### Preventing false matches

One problem with this approach with the ISNUMBER + SEARCH approach is you may get false matches from partial matches inside longer words. For example, if you try to match "dr" you may also find "Andrea", "drank", "drip", etc. since "dr" appears inside these words. This happens because SEARCH automatically does a "contains-type" match.

For a quick fix, you can wrap search words in space characters (i.e. " dr ", or "dr ") to avoid finding "dr" in another word. But this will fail if "dr" appears first or last in a cell.

If you need a more robust solution, one option is to [normalize the text](https://exceljet.net/formulas/normalize-text)
 first in a [helper column](https://exceljet.net/glossary/helper-column)
, and add a leading and trailing space. Then use the formula on this page on the text in the helper column, instead of the original text.

Related formulas
----------------

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

[![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")](https://exceljet.net/formulas/get-first-match-cell-contains)

### [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in...

[![Excel formula: Categorize text with keywords](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/categorize_text_with_keywords.png "Excel formula: Categorize text with keywords")](https://exceljet.net/formulas/categorize-text-with-keywords)

### [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)

In this example, the goal is to categorize various expenses using the categories shown in column F and the keywords shown in column E. This is a case where it seems like we should perform a lookup operation of some kind, but the problem is that the keywords appear embedded in the text and the...

[![Excel formula: Highlight cells that contain one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20one%20of%20many.png "Excel formula: Highlight cells that contain one of many")](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)

### [Highlight cells that contain one of many](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)

Working from the inside out, this part of the formula searches each cell in B4:B11 for all values in the named range "things": --ISNUMBER(SEARCH(things,B4) The SEARCH function returns the position of the value if found, and the #VALUE error if not found. For B4, the results come back in an array...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    
*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
    
*   [Highlight cells that contain one of many](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

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