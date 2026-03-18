# Get last match cell contains - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-last-match-cell-contains

---

[Skip to main content](https://exceljet.net/formulas/get-last-match-cell-contains#main-content)

[](https://exceljet.net/formulas/get-last-match-cell-contains#)

*   [Previous](https://exceljet.net/formulas/get-last-match)
    
*   [Next](https://exceljet.net/formulas/get-location-of-value-in-2d-array)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get last match cell contains
============================

by Dave Bruns · Updated 10 Jun 2023

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[SEARCH](https://exceljet.net/functions/search-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[AGGREGATE](https://exceljet.net/functions/aggregate-function)

![Excel formula: Get last match cell contains](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_last_match_cell_contains.png "Excel formula: Get last match cell contains")

Summary
-------

To search through a cell for one of several values and return the _last_ match found, you can use the  [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. In the example shown, the formula in cell C5 of the worksheet is:

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(list,B5)),list,,,-1)

where **list** is the [named range](https://exceljet.net/glossary/named-range)
 E5:E11, which contains the values to search for. As the formula is copied down, it returns the last match found in each cell. If no match is found, the formula will return #N/A by default. To override this error, provide a value for the _if\_not\_found_ argument.

_Note: It is also possible to [get all matches a cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
 with a formula._

Generic formula
---------------

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(list,A1)),list,,,-1)

Explanation 
------------

The goal is to search through a cell for one of several specified values and return the last match found when one exists. The worksheet includes a list of colors in the range E5:E11 (which is named **list**) and a series of short sentences in the range B5:B16. The task is to add a formula in column C that will search through each sentence in B5:B16 and extract the last color **list** (E5:E11) that appears in each sentence. One way to solve this problem is with a formula that utilizes the ISNUMBER, SEARCH, and XLOOKUP functions. In older versions of Excel, you can use an alternative formula, as explained below.

### Key functions

Here are the functions used in the XLOOKUP formula seen in the worksheet:

1.  The [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
     checks if a given input or expression results in a number. It returns TRUE if the value is numeric, and FALSE if not.
    
2.  The [SEARCH function](https://exceljet.net/functions/search-function)
     is used to find the starting position of a specific substring within a string. The syntax is SEARCH(find\_text, within\_text, \[start\_num\]). If the substring (find\_text) is found, SEARCH returns the starting position as a number. If not, it results in an error.
    
3.  The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
     is a modern upgrade to the older VLOOKUP function. XLOOKUP allows you to search for a key value in a specified range or array, and return a corresponding value from another range or array. The syntax is XLOOKUP(lookup\_value, lookup\_array, return\_array, \[if\_not\_found\], \[match\_mode\], \[search\_mode\]).
    

### How the formula works

The formula in cell C5 is as follows:

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(list,B5)),list,,,-1)
    

Working from the inside out, the SEARCH function looks for each color in the named range **list** (E5:E11) in cell B5:

    SEARCH(list,B5)
    

If a color is found, SEARCH returns its starting position as a number. If a color is not found, SEARCH returns an #VALUE! error. Because E5:E11 contains 7 colors, SEARCH returns 7 results in an array like this:

    {#VALUE!;34;#VALUE!;#VALUE!;#VALUE!;#VALUE!;5}

Notice the second value is 34 and the seventh value is 5. These numbers indicate the _numeric positions_ of the colors "white" (5) and "blue" (34) in cell B5. The #VALUE! errors indicate colors in E5:E11 that were not found. To convert these values into something more useful, we use the ISNUMBER function:

    ISNUMBER(SEARCH(list,B5))
    

This function is an error handler. Valid numbers become TRUE, and errors become FALSE. The result from ISNUMBER is an array with 7 values like this:

    {FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE}

Note we have a TRUE value in the 2nd position ("blue") and the 7th position ("white"). All other colors in the list were not found. Next, we have the XLOOKUP function, which is the main driver of the formula:

    =XLOOKUP(TRUE,ISNUMBER(SEARCH(list,B5)),list,"na")
    

Notice the _lookup\_value_ is set to TRUE. After SEARCH and ISNUMBER are evaluated, we have the following:

    =XLOOKUP(TRUE,{FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE},list,,,-1)
    

The _return\_array_ is provided as **list** (E5:E11), and _search\_mode_ is set to -1 to search _last to first_. _If\_not\_found_ and _match\_mode_ are left empty. XLOOKUP scans the array starting at the end. When a match is found, XLOOKUP returns the _corresponding_ color from **list** (E5:E11). Since the last value is TRUE, XLOOKUP returns the seventh color in E5:E11, which is "white". If no match is found, XLOOKUP returns an #N/A error. To customize this result, provide a value for _if\_not\_found._

### Last match in the sentence

The language used in this example is somewhat ambiguous because it is not clear whether we are referring to the "last color found in the list of colors" or the "last color found in each sentence". These are two distinctly different operations and therefore need two different formulas. The formula above returns the last match found in **list** (E5:E11). To find the last matched color in a sentence (ignoring the order of colors E5:E11) you can use a different formula like this:

    =XLOOKUP(LEN(B5),SEARCH(list,B5),list,,-1)

Here, we use the LEN function to create the _lookup\_value_. This is the total number of characters in B5, which is a number that XLOOKUP will never find. The SEARCH function is used exactly the same way as before. The _return\_array_ is **list** (B5:B11), _if\_not\_found_ is omitted, and _match\_mode_ is set to -1 for "exact match or _next smallest_" behavior.

After LEN and SEARCH are evaluated, we have:

    =XLOOKUP(42,{#VALUE!;34;#VALUE!;#VALUE!;#VALUE!;#VALUE!;5},list,,-1)

The value of 42 is deliberately larger than any number returned by SEARCH. XLOOKUP then matches the next smallest number (34) and returns the 2nd color ("blue") as a final result.

For more details on XLOOKUP, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
.

Legacy Excel
------------

In Excel 2019 and older, the XLOOKUP function is not available, but you can use a formula based on the [LOOKUP function](https://exceljet.net/functions/lookup-function)
 to get the last match found in **list** (E5:E11). LOOKUP can work well in "last match" scenarios, because it can handle array operations in older versions of Excel natively, without special handling. We can use LOOKUP like this:

    =LOOKUP(2,1/ISNUMBER(SEARCH(list,B5)),list)

This formula finds the last color matched in **list** (E5:E11), which is "white". Working from the inside out, we use SEARCH + ISNUMBER as explained earlier:

    ISNUMBER(SEARCH(list,B5))
    

The SEARCH function tries to find each of the 7 colors in **list** (E5:E11). Because E5:E11 contains 7 colors, SEARCH returns 7 results in an array like this:

    ISNUMBER({#VALUE!;34;#VALUE!;#VALUE!;#VALUE!;#VALUE!;5})

Notice the 2nd value is 34 and the 7th value is 5. These numbers indicate the numeric positions of the colors "white" (5) and "blue" (34) in cell B5. The #VALUE! errors indicate other colors not found. SEARCH returns these results to ISNUMBER, and ISNUMBER returns an array of TRUE and FALSE values:

    {FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE}

Next, we divide the number 1 by this array. During division, the math operation coerces TRUE to 1 and FALSE to zero, so you should visualize the operation like this:

    1/{0;1;0;0;0;0;1}
    

When the actual division takes place, 1 divided by 1 is 1, and 1 divided by 0 creates a #DIV/0 error:

    {#DIV/0!;#DIV/0!;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!}

This array is the _lookup\_vector_ inside LOOKUP, so at this point, we have:

    =LOOKUP(2,{#DIV/0!;1;#DIV/0!;#DIV/0!;#DIV/0!;#DIV/0!;1},list)

Notice that the lookup value is 2. This may seem odd, but it is intentional. We use 2 as a lookup value to force LOOKUP to scan to the _end of the data_. LOOKUP will automatically ignore errors, so the only thing left to match are the 1s. It will scan through the 1s looking for a 2 that can never be found. When it reaches the end of the array, it will "step back" to the last valid value (the last 1), and return the corresponding color from **list** (E5:E11), which is "white".

### Last match in the sentence

To get the last match found in the sentence in Legacy Excel, you can use a formula based on INDEX and MATCH:

    =INDEX(list,MATCH(AGGREGATE(14,6,SEARCH(list,B5),1),SEARCH(list,B5),0))

_Note this is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with control + shift + enter in Excel 2019 and earlier._

The main trick is the _lookup\_value_ in MATCH, which is calculated with the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
 like this:

    AGGREGATE(14,SEARCH(list,B5),1) // get max value
    

Here, we use AGGREGATE to get the _maximum value_ in the results returned by SEARCH. The number 14 indicates that AGGREGATE should apply the behavior of the [LARGE function](https://exceljet.net/functions/large-function)
, which is designed to extract nth largest values. We use AGGREGATE because the array will contain errors (returned by SEARCH when colors aren't found), and we need to _ignore these errors_ and still get the maximum numeric value. AGGREGATE works well here because it has the option to _ignore errors_. The result from AGGREGATE is 34, which is returned to MATCH as the _lookup\_value_. The _lookup\_array_ is created by the SEARCH function:

    {#VALUE!;34;#VALUE!;#VALUE!;#VALUE!;#VALUE!;5}

We don't use ISNUMBER in this case because we need to be able to find the number calculated by AGGREGATE. Back in the formula, we now have:

    =INDEX(list,MATCH(34,{#VALUE!;34;#VALUE!;#VALUE!;#VALUE!;#VALUE!;5},0))

The result from MATCH is 2, because 34 is the 2nd value in the _lookup\_array_. MATCH returns this number to INDEX as the _row\_num_ argument:

    =INDEX(list,7) // returns "white"

The final result is "blue", the last color found in the sentence.

For more details on INDEX with MATCH, see [How to use the INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

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

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")](https://exceljet.net/formulas/get-first-match-cell-contains)

### [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

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

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel AGGREGATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20aggregate%20function.png "Excel AGGREGATE function")](https://exceljet.net/functions/aggregate-function)

### [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)

The Excel AGGREGATE function returns an aggregate calculation like AVERAGE, COUNT, MAX, etc., optionally ignoring hidden rows and errors. A total of 19 operations are available, specified by function number in the first argument (see table for options).

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

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
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [AGGREGATE Function](https://exceljet.net/functions/aggregate-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

### Articles

*   [How to lookup first and last match](https://exceljet.net/articles/how-to-lookup-first-and-last-match)
    

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