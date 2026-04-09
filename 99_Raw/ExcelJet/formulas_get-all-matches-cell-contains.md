# Get all matches cell contains - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-all-matches-cell-contains

---

[Skip to main content](https://exceljet.net/formulas/get-all-matches-cell-contains#main-content)

[](https://exceljet.net/formulas/get-all-matches-cell-contains#)

*   [Previous](https://exceljet.net/formulas/get-address-of-lookup-result)
    
*   [Next](https://exceljet.net/formulas/get-cell-content-at-given-row-and-column)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get all matches cell contains
=============================

by Dave Bruns · Updated 22 Apr 2025

Related functions 
------------------

[SEARCH](https://exceljet.net/functions/search-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[FILTER](https://exceljet.net/functions/filter-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

![Excel formula: Get all matches cell contains](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_all_matches_cell_contains.png "Excel formula: Get all matches cell contains")

Summary
-------

To check a cell for several things at once, and return a list of things found, you can use a formula based on the [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 and [FILTER](https://exceljet.net/functions/filter-function)
 functions, with help from [SEARCH](https://exceljet.net/functions/search-function)
 and [ISNUMBER](https://exceljet.net/functions/isnumber-function)
. In the example shown, the formula in C5, copied down, is:

    =TEXTJOIN(", ",1,FILTER(things,ISNUMBER(SEARCH(things,B5)),""))
    

where **things** is the [named range](https://exceljet.net/glossary/named-range)
 E5:E9.

Generic formula
---------------

    =TEXTJOIN(", ",1,FILTER(things,ISNUMBER(SEARCH(things,A1)),""))

Explanation 
------------

In this example the goal is to check a cell for several things at once, and return a comma separated list of the things that were found.  In other words, we want check for the colors seen in column E and list the colors found in column C. The formula in C5, copied down, is:

     =TEXTJOIN(", ",1,FILTER(things,ISNUMBER(SEARCH(things,B5)),""))
    

Working from the inside out, this formula is based on the [formula described here](https://exceljet.net/formulas/cell-contains-specific-text)
, which uses the [SEARCH function](https://exceljet.net/functions/search-function)
 together with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    ISNUMBER(SEARCH(things,B5))
    

In a nutshell, SEARCH returns a number if it finds the target string and an error if not, and ISNUMBER converts this result into a TRUE or FALSE. In this case, we are looking for several strings at once – the five colors in the [named range](https://exceljet.net/glossary/named-range)
 **things** (E5:E10), so the code above returns an [array](https://exceljet.net/glossary/array)
 with five TRUE FALSE values like this:

    {FALSE;FALSE;TRUE;FALSE;TRUE}
    

Notice the TRUE values correspond to white and green in the list of colors (positions 3 and 5), and FALSE values correspond to the colors not found. This array is returned directly to the [FILTER function](https://exceljet.net/functions/filter-function)
 as the _include_ argument, with the _array_ argument given as **things:**

    FILTER(things,{FALSE;FALSE;TRUE;FALSE;TRUE},"")
    

The FILTER function uses the TRUE and FALSE values to filter the list of colors and returns an array of the two colors found:

    {"white";"green"} // result from FILTER
    

The result from FILTER is delivered to the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
:

    =TEXTJOIN(", ",1,{"white";"green"})
    

TEXTJOIN is configured to join items in the array with a comma and space (", ") and to ignore empty strings (""). The number 1 is provided instead of TRUE for brevity. TEXTJOIN [concatenates](https://exceljet.net/glossary/concatenation)
 the found colors, separated by commas, and returns a final result.

Note FILTER's _not\_found_ argument is provided as an [empty string](https://exceljet.net/glossary/empty-string)
 (""). In the event no colors are found, FILTER returns an empty string to TEXTJOIN, which then also returns an empty string as the final result.

Related formulas
----------------

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")](https://exceljet.net/formulas/get-first-match-cell-contains)

### [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in...

[![Excel formula: Count cells that contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20specific%20text.png "Excel formula: Count cells that contain specific text")](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

### [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)

In this example, the goal is to count cells that contain a specific substring. This problem can be solved with the SUMPRODUCT function or the COUNTIF function. Both approaches are explained below. The SUMPRODUCT version can also perform a case-sensitive count. COUNTIF function The COUNTIF function...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Look up and return to single cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_and_return_to_single_cell.png "Excel formula: Look up and return to single cell")](https://exceljet.net/formulas/look-up-and-return-to-single-cell)

### [Look up and return to single cell](https://exceljet.net/formulas/look-up-and-return-to-single-cell)

In this example, the goal is to look up and retrieve all names for a given team and return them in a single cell as a comma‑separated list. At the core, this is a lookup problem, but the twist is that we want to return multiple matches for each team, not just one. That means traditional lookup...

Related functions
-----------------

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    
*   [Count cells that contain specific text](https://exceljet.net/formulas/count-cells-that-contain-specific-text)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Look up and return to single cell](https://exceljet.net/formulas/look-up-and-return-to-single-cell)
    

### Functions

*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    

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