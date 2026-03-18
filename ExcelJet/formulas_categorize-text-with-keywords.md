# Categorize text with keywords - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/categorize-text-with-keywords

---

[Skip to main content](https://exceljet.net/formulas/categorize-text-with-keywords#main-content)

[](https://exceljet.net/formulas/categorize-text-with-keywords#)

*   [Previous](https://exceljet.net/formulas/return-blank-if)
    
*   [Next](https://exceljet.net/formulas/group-arbitrary-text-values)
    

[Grouping](https://exceljet.net/formulas#Grouping)

Categorize text with keywords
=============================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8205/download?token=s5EH_HRl)
 (15.75 KB)

![Excel formula: Categorize text with keywords](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/categorize_text_with_keywords.png "Excel formula: Categorize text with keywords")

Summary
-------

To categorize text using keywords, you can use a formula based on the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 and the [SEARCH function](https://exceljet.net/functions/search-function)
.  In the example shown, the formula in C5 is:

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(keyword,B5)),category)
    

where **keyword** (E5:E13) and **category** (F5:F13) are [named ranges](https://exceljet.net/glossary/named-range)
. As the formula is copied down, it searches the text in column B for a matching keyword in E5:E13  and returns the associated category from F5:F13. If no keyword is found, the formula returns a #N/A error. Notice the formula automatically performs a "contains" type match and is not case-sensitive.

Generic formula
---------------

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(keyword,A1)),category)

Explanation 
------------

In this example, the goal is to categorize various expenses using the categories shown in column F and the keywords shown in column E. This is a case where it seems like we should perform a lookup operation of some kind, but the problem is that the keywords appear embedded in the text and the structure is unpredictable. The article below explains two ways to solve this problem. The first approach, based on the XLOOKUP function is the simplest. The second approach, based on INDEX and MATCH is a more complicated array formula but will work in older versions of Excel without XLOOKUP. The keywords and categories are completely arbitrary and can be customized to suit the situation.

_Note: For convenience, **keyword** (E5:E13) and **category** (F5:F13) are named ranges, but you can use absolute references or an [Excel Table](https://exceljet.net/articles/excel-tables)
 instead if you prefer._

### Background study

This is a more advanced lookup formula. If you need a good introduction to XLOOKUP or INDEX and MATCH, these are good resources:

*   [XLOOKUP function overview](https://exceljet.net/functions/xlookup-function)
    
*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    
*   [XLOOKUP vs. INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

### XLOOKUP solution

In the worksheet shown above, the formula in cell C5, copied down, looks like this:

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(keyword,B5)),category)
    

Working from the inside out, we first use the SEARCH function to look for keywords in cell B5 like this:

    SEARCH(keyword,B5)
    

The [SEARCH function](https://exceljet.net/functions/search-function)
 returns the _position_ of one text string inside another, and a #VALUE! error if the text string is not found. In this case, because the named range **keyword** contains 9 values:

    SEARCH({"chevron";"netflix";"hbo";"costco";"kroger";"cvs";"urgent";"electric";"gas"},B5)

SEARCH returns an array that contains 9 results like this:

    {#VALUE!;#VALUE!;#VALUE!;1;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}

Notice all results are #VALUE! errors except for the fourth value, which is 1. This corresponds to the text "costco" appearing as the first word in the text in cell B5: "COSTCO West des Moines". Also, notice that SEARCH is not case-sensitive: it matches the lowercase "costco" in a text string that contains "COSTCO".

Next, the array above is returned to the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, which converts the results into TRUE and FALSE values:

    ISNUMBER({#VALUE!;#VALUE!;#VALUE!;1;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!})

ISNUMBER returns an array like this:

    {FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}

The result from ISNUMBER is delivered directly to the XLOOKUP function as the _lookup\_array_ argument, and we can now simplify the original formula as follows:

    =XLOOKUP(TRUE,{FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE},category)

We can now finally see how the formula works. XLOOKUP is configured with the _lookup\_value_ set to TRUE. XLOOKUP locates the TRUE in the fourth position of the array returned by ISNUMBER and SEARCH, and returns the fourth item in **category**, "Food", as a final result. As the formula is copied down, the same operation is performed for each expense listed in column B.

> For a more detailed explanation of the search method used in this formula [see this example](https://exceljet.net/formulas/cell-contains-specific-text)
> .

### INDEX and MATCH solution

In older versions of Excel without the XLOOKUP function, you can use an alternative formula based on [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. The equivalent formula in C5 looks like this:

    =INDEX(category,MATCH(TRUE,ISNUMBER(SEARCH(keyword,B5)),0))
    

where **keyword** (E5:E13) and **category** (F5:F13) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in Excel 2019 and older. In Excel 2021 and newer, [array formulas are native](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 so the formula will "just work" without special handling._

The operation of this formula is similar to the XLOOKUP formula above. Inside the MATCH function, we use the [SEARCH function](https://exceljet.net/functions/search-function)
 to search cells in column B for every listed keyword in the [named range](https://exceljet.net/articles/named-ranges)
 **keyword** (E5:E13):

    SEARCH(keyword,B5)
    

Because we are looking for multiple items (in the named range **keyword**), we'll get back multiple results like this:

    {#VALUE!;#VALUE!;#VALUE!;1;#VALUE!;#VALUE!;#VALUE!;#VALUE!;#VALUE!}
    

The #VALUE! error occurs when SEARCH can't find the text. When SEARCH does find a match, it returns a number that corresponds to the position of the text inside the cell. To change these results into a more usable format, we use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, which converts all values to TRUE/FALSE like so:

    {FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

This array goes into the MATCH function as the _lookup\_array_, with the _lookup\_value_ set to TRUE, and _match\_type_ set to 0 to force an exact match. MATCH returns the position of the first TRUE it finds in the array (4 in this case) which is provided to the [INDEX function](https://exceljet.net/functions/index-function)
 as the _row\_num_:

    =INDEX(category,4)
    

INDEX returns the 4th item in **category**, "Food", as a final result.

### Preventing false matches

One problem with this approach is you may get false matches from substrings that appear inside longer words. For example, if you try to match "dr" you may also find "Andrea", "drink", "dry", etc. since "dr" appears inside these words. This happens because SEARCH looks for a substring and has no concept of words. For a quick hack, you can add space around the search words (i.e. " dr ", or "dr ") to avoid catching "dr" in another word. But this will fail if "dr" appears first or last in a cell, or appears with punctuation, etc. If you need a more accurate solution, one option is to [normalize the text](https://exceljet.net/formulas/normalize-text)
 first in a [helper column](https://exceljet.net/glossary/helper-column)
, taking care to also add a leading and trailing space. Then you can search for whole words surrounded by spaces.

In the latest version of Excel, another option is to use the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 with the [XMATCH function](https://exceljet.net/functions/xmatch-function)
 like this:

    =XLOOKUP(TRUE,ISNUMBER(XMATCH(keyword,TEXTSPLIT(B5,{".",", "," "}))),category)

In this formula, we have replaced the SEARCH function with XMATCH and TEXTSPLIT. The result is that we are splitting the text in B5 into an array of actual words, and then checking the words for keywords with XMATCH. For a detailed explanation of how this works, [see this example](https://exceljet.net/formulas/cell-contains-specific-words)
.

Related formulas
----------------

[![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")](https://exceljet.net/formulas/get-first-match-cell-contains)

### [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in...

[![Excel formula: Get last match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_last_match_cell_contains.png "Excel formula: Get last match cell contains")](https://exceljet.net/formulas/get-last-match-cell-contains)

### [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)

The goal is to search through a cell for one of several specified values and return the last match found when one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in column C...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Get all matches cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_all_matches_cell_contains.png "Excel formula: Get all matches cell contains")](https://exceljet.net/formulas/get-all-matches-cell-contains)

### [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)

In this example the goal is to check a cell for several things at once, and return a comma separated list of the things that were found. In other words, we want check for the colors seen in column E and list the colors found in column C. The formula in C5, copied down, is: =TEXTJOIN(", ",1,FILTER(...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: Count keywords cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20keywords%20cell%20contains.png "Excel formula: Count keywords cell contains")](https://exceljet.net/formulas/count-keywords-cell-contains)

### [Count keywords cell contains](https://exceljet.net/formulas/count-keywords-cell-contains)

Note: if a keyword appears more than once in a given cell, it will only be counted once. In other words, the formula only counts instances of different keywords. The core of this formula is the ISNUMBER + SEARCH approach to finding text in a cell, which is explained in more detail here . In this...

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

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    
*   [Get last match cell contains](https://exceljet.net/formulas/get-last-match-cell-contains)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Count keywords cell contains](https://exceljet.net/formulas/count-keywords-cell-contains)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

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