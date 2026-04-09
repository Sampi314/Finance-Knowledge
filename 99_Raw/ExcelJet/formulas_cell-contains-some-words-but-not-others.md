# Cell contains some words but not others - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cell-contains-some-words-but-not-others

---

[Skip to main content](https://exceljet.net/formulas/cell-contains-some-words-but-not-others#main-content)

[](https://exceljet.net/formulas/cell-contains-some-words-but-not-others#)

*   [Previous](https://exceljet.net/formulas/cell-contains-one-of-many-with-exclusions)
    
*   [Next](https://exceljet.net/formulas/cell-contains-specific-text)
    

[Text](https://exceljet.net/formulas#Text)

Cell contains some words but not others
=======================================

by Dave Bruns · Updated 8 Oct 2018

Related functions 
------------------

[COUNT](https://exceljet.net/functions/count-function)

[SEARCH](https://exceljet.net/functions/search-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Cell contains some words but not others](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cell%20contains%20some%20words%20but%20not%20others.png "Excel formula: Cell contains some words but not others")

Summary
-------

To test a cell to see if contains certain words but not others, you can use an array formula based on the COUNT and SEARCH functions, wrapped in the AND function.

In the example shown, the formula in C5 is:

    {=AND(COUNT(SEARCH(inc,B5))>0,COUNT(SEARCH(exc,B5))=0)}
    

This formula returns TRUE when B5 contains any of the words in the named range **inc** and none of the words in the named range **exc**.

_This is an array formula and must be entered with Control + Shift + Enter._

Generic formula
---------------

    {=AND(COUNT(SEARCH(inc,A1))>0,COUNT(SEARCH(exc,A1))=0)}

Explanation 
------------

This formula relies on the AND function to test two conditions at the same time:

1.  Count of words from named range **inc** is >0
2.  Count of words from named range **exc** is =0

If both conditions are TRUE, the formula returns TRUE. If either condition is FALSE, the formula returns FALSE.

The test for multiple words is done using the SEARCH function with help from COUNT.

When SEARCH receives more than one item to look for, it returns an array of results, one per item. When a match is found, SEARCH returns the position of the match. When no match is found, SEARCH returns the #VALUE error. The COUNT function gets a count of numbers in the array returned by SEARCH. COUNT ignores errors by default.

In the example shown, the formula is solved in steps like this

    =AND(COUNT({1;11;#VALUE!})>0,COUNT({#VALUE!;#VALUE!})=0)
    =AND(2>0,0=0)
    =AND(TRUE,TRUE)
    =TRUE
    

### With hard-coded values

There's no requirement that you use a range for your list of things. If you're only looking for a small number of things, you can use a list in array format, which is called an array constant. For example, to test for red, blue, or green, but exclude pink and orange, you can use:

    =AND(COUNT(SEARCH({"red","blue","green"},B5))>0,COUNT(SEARCH({"orange","pink"},B5))=0)
    

This version does not require the control + shift + enter array formula syntax.

Related formulas
----------------

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Cell contains all of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_all_of_many_things.png "Excel formula: Cell contains all of many things")](https://exceljet.net/formulas/cell-contains-all-of-many-things)

### [Cell contains all of many things](https://exceljet.net/formulas/cell-contains-all-of-many-things)

In this example, the goal is to build a formula that will return TRUE if a given cell contains all values that appear in a given range. We could build a formula that uses nested IF statements to check for each value, but that won't scale well if we have a lot of values to test because each new...

[![Excel formula: Get all matches cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_all_matches_cell_contains.png "Excel formula: Get all matches cell contains")](https://exceljet.net/formulas/get-all-matches-cell-contains)

### [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)

In this example the goal is to check a cell for several things at once, and return a comma separated list of the things that were found. In other words, we want check for the colors seen in column E and list the colors found in column C. The formula in C5, copied down, is: =TEXTJOIN(", ",1,FILTER(...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

Related functions
-----------------

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

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
    
*   [Cell contains all of many things](https://exceljet.net/formulas/cell-contains-all-of-many-things)
    
*   [Get all matches cell contains](https://exceljet.net/formulas/get-all-matches-cell-contains)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    

### Functions

*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

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