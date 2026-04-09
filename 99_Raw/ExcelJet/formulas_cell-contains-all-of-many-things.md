# Cell contains all of many things - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cell-contains-all-of-many-things

---

[Skip to main content](https://exceljet.net/formulas/cell-contains-all-of-many-things#main-content)

[](https://exceljet.net/formulas/cell-contains-all-of-many-things#)

*   [Previous](https://exceljet.net/formulas/cell-begins-with)
    
*   [Next](https://exceljet.net/formulas/cell-contains-number)
    

[Text](https://exceljet.net/formulas#Text)

Cell contains all of many things
================================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

[COUNTA](https://exceljet.net/functions/counta-function)

[COUNT](https://exceljet.net/functions/count-function)

![Excel formula: Cell contains all of many things](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cell_contains_all_of_many_things.png "Excel formula: Cell contains all of many things")

Summary
-------

To test if a cell contains all of many values, you can use a formula based on the [SEARCH function](https://exceljet.net/functions/search-function)
, with help from [ISNUMBER](https://exceljet.net/functions/isnumber-function)
, [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
, and [COUNTA](https://exceljet.net/functions/counta-function)
. In the worksheet shown, the formula in cell D5 is:

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))=COUNTA(things)

where **things** is the [named range](https://exceljet.net/articles/named-ranges)
 F5:F7. As the formula is copied down, it returns TRUE if the text in column B contains "red", "blue", and "green" and FALSE if not. The values to search for can be customized as needed.

Generic formula
---------------

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,A1)))=COUNTA(things)

Explanation 
------------

In this example, the goal is to build a formula that will return TRUE if a given cell contains all values that appear in a given range. We could build a formula that uses [nested IF statements](https://exceljet.net/formulas/nested-if-function-example)
 to check for each value, but that won't scale well if we have a lot of values to test because each new value will require another nested IF. The article below explains a more scalable approach based on the SEARCH function. For convenience, the values we are testing for are in the [named range](https://exceljet.net/articles/named-ranges)
 "things" which is F5:F7. The formula in cell D5 looks like this:

    =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))=COUNTA(things)

At a high level, this formula counts the matches found in cell B5 for the three values in **things** (F5:F7). Then it compares the count of matches found with the count of values in **things**. If the counts match, the formula returns TRUE. Otherwise, the formula returns FALSE. Working from the inside out, the core of the formula is this snippet based on the [SEARCH function](https://exceljet.net/functions/search-function)
 and the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    ISNUMBER(SEARCH(things,B5)
    

This code is based on a fairly common pattern in Excel formulas ([explained in detail here](https://exceljet.net/formulas/cell-contains-specific-text)
) that are designed to test a cell for a specific text. The more generic version of the formula looks like this:

    ISNUMBER(SEARCH(substring,text)
    

In a nutshell, the SEARCH function searches _text_ for a _substring_. If the _substring_ is found, SEARCH returns the location of the match as a number. If the _substring_ is not found, SEARCH returns a #VALUE error. The ISNUMBER function is used to convert the result from SEARCH into TRUE or FALSE.

The twist in this formula is that we are not searching for a single substring. Instead, we are searching for 3 different substrings in the named range **things** (F5:F7). Because we are giving SEARCH three different substrings to look for, SEARCH will return three separate results in an [array](https://exceljet.net/glossary/array)
. In cell B5, the results from SEARCH look like this:

    {7;1;16}

These numbers represent the location of "red", "blue", and "green" in the text from cell B5. The text "red" begins at character 7, "blue" begins at character 1, and "green" begins at character 16. These locations are delivered to the ISNUMBER function, which converts the results to TRUE or FALSE values. Because all three results are numbers, ISNUMBER returns an array that contains three TRUE values:

    =ISNUMBER(SEARCH(things,B5))
    =ISNUMBER({7;1;16))
    ={TRUE;TRUE;TRUE}

Next, we convert the TRUE / FALSE values to 1s and 0s with a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) operation:

    --{TRUE;TRUE;TRUE}
    

The result is an array like this:

    {1;1;1}

We take this step because we want to work with TRUE and FALSE like the numbers 1 and 0. Next, we process this array with SUMPRODUCT, which will give us a total count of matches:

    =SUMPRODUCT({1;1;1}) // returns 3

The final step in the formula is to compare this result to the count of values in the named range **things** (F5:F7). To get a count of the values in things, we use the [COUNTA function](https://exceljet.net/functions/counta-function)
, which is designed to count both numbers and text:

    =COUNTA(things)
    =COUNTA({"red";"blue";"green"})
    =3
    

If the counts are equal, the formula will return TRUE:

    =SUMPRODUCT({1;1;1})=COUNTA(things)
    =3=3
    =TRUE

### With a hard-coded list

There's no requirement to use a range for your list of things. If you're only looking for a small number of things, you can use a list in array format, called an [array constant](https://exceljet.net/glossary/array-constant)
. For example, if you're just looking for the colors red, blue, and green, you can use {"red","blue","green"} and hardcode a count of values like this:

    =SUMPRODUCT(--ISNUMBER(SEARCH({"yellow","green","dog"},B5)))=3

### Simplifying the formula

There is a fair bit of complexity in computing a count of the substrings found, which involves ISNUMBER, a double negative (--) operation, and SUMPRODUCT. You might wonder why you can't just do this:

    =COUNT(SEARCH(things,B5))=COUNTA(things)

The COUNT function only counts numeric values, so it should work, right? The answer is that it will work fine in Excel 2021 or later. But keep in mind that if the formula is opened in an older version of Excel, Excel will convert it to an [array formula](https://exceljet.net/glossary/array-formula)
 automatically. Then, if a user edits the formula and enters it again, without using control + shift + enter, it will break. The SUMPRODUCT approach is a workaround that ensures the formula will run cleanly in all versions of Excel without special handling. You can read more about this topic here: [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)

Related formulas
----------------

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Get first match cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_match_cell_contains.png "Excel formula: Get first match cell contains")](https://exceljet.net/formulas/get-first-match-cell-contains)

### [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)

The general goal is to search through a cell for one of several specified values and return the first match found if one exists. The worksheet includes a list of colors in the range E5:E11 (which is named list ) and a series of short sentences in the range B5:B16. The task is to add a formula in...

[![Excel formula: Get all matches cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_all_matches_cell_contains.png "Excel formula: Get all matches cell contains")](https://exceljet.net/formulas/get-all-matches-cell-contains)

### [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)

In this example the goal is to check a cell for several things at once, and return a comma separated list of the things that were found. In other words, we want check for the colors seen in column E and list the colors found in column C. The formula in C5, copied down, is: =TEXTJOIN(", ",1,FILTER(...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

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

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

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
    
*   [Get first match cell contains](https://exceljet.net/formulas/get-first-match-cell-contains)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    

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