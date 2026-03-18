# Cell contains one of many things - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cell-contains-one-of-many-things

---

[Skip to main content](https://exceljet.net/formulas/cell-contains-one-of-many-things#main-content)

[](https://exceljet.net/formulas/cell-contains-one-of-many-things#)

*   [Previous](https://exceljet.net/formulas/cell-contains-number)
    
*   [Next](https://exceljet.net/formulas/cell-contains-one-of-many-with-exclusions)
    

[Text](https://exceljet.net/formulas#Text)

Cell contains one of many things
================================

by Dave Bruns · Updated 8 Dec 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6484/download?token=lbbm1riF)
 (14.91 KB)

![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")

Summary
-------

To test if a cell contains one of many strings, you can use a formula based on the [SEARCH](https://exceljet.net/functions/search-function)
, [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 functions. The formula in C5, copied down, is:

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))>0
    

where **things** is the [named range](https://exceljet.net/articles/named-ranges)
 E5:E7.

Generic formula
---------------

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,A1)))>0

Explanation 
------------

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the [named range](https://exceljet.net/articles/named-ranges)
 **things** (E5:E7). These strings can appear _anywhere_ in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is:

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))>0
    

This formula is based on [another formula](https://exceljet.net/formulas/cell-contains-specific-text)
 that checks a cell for a single substring. If the cell contains the substring, the formula returns TRUE. If not, the formula returns FALSE:

    ISNUMBER(SEARCH(substring,B5)) // test for substring
    

When the [SEARCH function](https://exceljet.net/functions/search-function)
 finds a string, it returns the position of that string as a number. If SEARCH _doesn't_ find a string, it returns a #VALUE! error. This means ISNUMBER will return TRUE if there is a match and FALSE if not.

In this example, the goal is to check for more than one string, so we are giving the SEARCH function a _list of strings_ in the [named range](https://exceljet.net/glossary/named-range)
 **things**. Since there are 3 strings in **things** ("red", "green", and "blue"), SEARCH returns 3 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {#VALUE!;#VALUE!;23}
    

Because "red" and "blue" aren't found , the SEARCH returns a #VALUE! error. However, because "green" appears near the end of the text in cell B5, SEARCH returns 23 (i.e. "green" begins at the 23rd character).

This array is returned directly to the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, which converts the items in the array to either TRUE or FALSE:

    ISNUMBER({#VALUE!;#VALUE!;23}) // returns {FALSE;FALSE;TRUE}
    

Logically, if we have even one TRUE in the array, we know a cell contains at least one of the strings we're looking for. The easiest way to check for TRUE is to add all values together. We can do that with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, but first we need to coerce the TRUE / FALSE values to 1s and 0s with a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) like this:

    --{FALSE;FALSE;TRUE} // coerce to 1s and 0s
    

This yields a new array containing only 1s and 0s:

    {0;0;1}
    

which is delivered directly to SUMPRODUCT:

    =SUMPRODUCT({0;0;1}) // returns 1
    

With just one array to process, SUMPRODUCT sums the items in the array and returns a result. Any non-zero result means we have a "hit", so we add >0 to force a final result of TRUE or FALSE:

    =SUMPRODUCT({0;0;1})>0 // returns TRUE
    

Note that any combination of matches will return a number greater than zero and cause the formula to return TRUE.

### With a hard-coded list

It's not necessary to use a range for the list of strings to look for. You can also use an [array constant](https://exceljet.net/glossary/array-constant)
. For example, to check for "red", "blue", or "green", you can use a formula like this:

    =SUMPRODUCT(--ISNUMBER(SEARCH({"red","blue","green"},B5)))>0
    

### SUM function

Historically, [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 often appears in [array formulas](https://exceljet.net/glossary/array-formula)
, because it can handle arrays natively, _without control + shift + enter_. This makes the formula "more friendly" to most users. In [Excel 365](https://exceljet.net/glossary/excel-365)
, which handles arrays [natively](https://exceljet.net/videos/dynamic-arrays-are-native)
, the [SUM function](https://exceljet.net/functions/sum-function)
 can be used instead of SUMPRODUCT without control + shift + enter:

    =SUM(--ISNUMBER(SEARCH(things,A1)))>0
    

### Preventing false matches

One problem with this approach is you may get false matches from substrings that appear inside longer words. For example, if you try to match "dr" you may also find "Andrea", "drink", "dry", etc. since "dr" appears inside these words. This happens because SEARCH automatically does a "contains" match. For a quick hack, you can add space around the search words (i.e. " dr ", or "dr ") to avoid catching "dr" in another word. But this will fail if "dr" appears first or last in a cell, or appears with punctuation. If you need a more accurate solution, one option is to [normalize the text](https://exceljet.net/formulas/normalize-text)
 first in a [helper column](https://exceljet.net/glossary/helper-column)
, taking care to also add a leading and trailing space. Then you use the formula on this page on the resulting text.

_Note: in the latest version of Excel, the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 provides a better way to [search for specific words](https://exceljet.net/formulas/cell-contains-specific-words)
 without catching unrelated substrings._

Related formulas
----------------

[![Excel formula: Cell contains one of many with exclusions](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20with%20exclusions.png "Excel formula: Cell contains one of many with exclusions")](https://exceljet.net/formulas/cell-contains-one-of-many-with-exclusions)

### [Cell contains one of many with exclusions](https://exceljet.net/formulas/cell-contains-one-of-many-with-exclusions)

At the core, this formula uses the SEARCH function to look for multiple strings inside a cell. Inside the left SUMPRODUCT, SEARCH looks for all strings in the named range "include". In the right SUMPRODUCT, SEARCH looks for all strings in the named range "exclude". In both parts of the formula,...

[![Excel formula: Cell contains all of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_all_of_many_things.png "Excel formula: Cell contains all of many things")](https://exceljet.net/formulas/cell-contains-all-of-many-things)

### [Cell contains all of many things](https://exceljet.net/formulas/cell-contains-all-of-many-things)

In this example, the goal is to build a formula that will return TRUE if a given cell contains all values that appear in a given range. We could build a formula that uses nested IF statements to check for each value, but that won't scale well if we have a lot of values to test because each new...

[![Excel formula: Cell contains specific words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_words.png "Excel formula: Cell contains specific words")](https://exceljet.net/formulas/cell-contains-specific-words)

### [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)

In this example, the goal is to test the text in a cell and return TRUE if it contains one or more specific words, and FALSE if not. Notice the emphasis here is on words, not substrings. For example, if we are testing for the word "green" and the text contains the word "evergreen" but not the word...

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

[![Excel formula: Cell contains some words but not others](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20some%20words%20but%20not%20others.png "Excel formula: Cell contains some words but not others")](https://exceljet.net/formulas/cell-contains-some-words-but-not-others)

### [Cell contains some words but not others](https://exceljet.net/formulas/cell-contains-some-words-but-not-others)

This formula relies on the AND function to test two conditions at the same time: Count of words from named range inc is >0 Count of words from named range exc is =0 If both conditions are TRUE, the formula returns TRUE. If either condition is FALSE, the formula returns FALSE. The test for...

[![Excel formula: Categorize text with keywords](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/categorize_text_with_keywords.png "Excel formula: Categorize text with keywords")](https://exceljet.net/formulas/categorize-text-with-keywords)

### [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)

In this example, the goal is to categorize various expenses using the categories shown in column F and the keywords shown in column E. This is a case where it seems like we should perform a lookup operation of some kind, but the problem is that the keywords appear embedded in the text and the...

[![Excel formula: LAMBDA contains one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20contains%20one%20of%20many.png "Excel formula: LAMBDA contains one of many")](https://exceljet.net/formulas/lambda-contains-one-of-many)

### [LAMBDA contains one of many](https://exceljet.net/formulas/lambda-contains-one-of-many)

Excel does not provide a dedicated "contains" function, but you can create a custom function to test if a cell contains one or many strings with the LAMBDA function . LAMBDA functions do not require VBA, but are only available in Excel 365 . The first step in creating a custom LAMBDA function is to...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

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

*   [Cell contains one of many with exclusions](https://exceljet.net/formulas/cell-contains-one-of-many-with-exclusions)
    
*   [Cell contains all of many things](https://exceljet.net/formulas/cell-contains-all-of-many-things)
    
*   [Cell contains specific words](https://exceljet.net/formulas/cell-contains-specific-words)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [Cell contains some words but not others](https://exceljet.net/formulas/cell-contains-some-words-but-not-others)
    
*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
    
*   [LAMBDA contains one of many](https://exceljet.net/formulas/lambda-contains-one-of-many)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
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