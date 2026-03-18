# IF with wildcards - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-with-wildcards

---

[Skip to main content](https://exceljet.net/formulas/if-with-wildcards#main-content)

[](https://exceljet.net/formulas/if-with-wildcards#)

*   [Previous](https://exceljet.net/formulas/if-with-other-calculations)
    
*   [Next](https://exceljet.net/formulas/invoice-age-and-status)
    

[If](https://exceljet.net/formulas#If)

IF with wildcards
=================

by Dave Bruns · Updated 18 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[SEARCH](https://exceljet.net/functions/search-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: IF with wildcards](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/IF_with_wildcards.png "Excel formula: IF with wildcards")

Summary
-------

The [IF function](https://exceljet.net/functions/if-function)
 doesn't support [wildcards](https://exceljet.net/glossary/wildcard)
 directly, but you can combine IF with [COUNTIF](https://exceljet.net/functions/countif-function)
 or [COUNTIFS](https://exceljet.net/functions/countifs-function)
 to get basic wildcard functionality. In the example shown, the formula in D5 is:

    =IF(COUNTIF(B5,"??-????-???"),"ok","invalid")
    

As the formula is copied down, it returns "ok" if the value in column B matches the form xx-xxxx-xxx, and "invalid" if it does not.

Generic formula
---------------

    =IF(COUNTIF(A1,"??-????-???"),"","invalid")

Explanation 
------------

The goal of this formula is to verify whether the values in column B follow the format xx-xxxx-xxx, where "x" represents any single character. The IF function doesn't support wildcards directly, so we can't use IF by itself. Instead, we can combine the IF function with the COUNTIF function, which does support wildcards.

### Excel wildcards

Excel supports three wildcards that can be used in formulas:

*   Asterisk (\*) - zero or more characters
*   Question mark (?) - any one character
*   Tilde (~) - escape for literal character (~\*) a literal question mark (~?), or a literal tilde (~~).

### IF + COUNTIF

Unlike several other frequently used functions, the IF function does not support wildcards. However, you can use the COUNTIF or COUNTIFS functions inside the logical test of IF for basic [wildcard functionality](https://exceljet.net/glossary/wildcard)
. In the example shown, the formula in D5 is:

    =IF(COUNTIF(B5,"??-????-???"),"ok","invalid")
    

Working from the inside out, the logical test inside the IF function is based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
:

    COUNTIF(B5,"??-????-???") // returns 1 or 0
    

In this context, COUNTIF counts cells matching the pattern "??-????-???", with the question mark (?) representing any single character. Because the range provided to COUNTIF is just one cell, the result will always be 1 or zero. Inside the IF function, Excel will evaluate any non-zero number as TRUE and zero as FALSE.  When COUNTIF returns the number 1 (indicating that the value in B5 consists of 11 characters with two hyphens as described by the pattern), IIF interprets this as TRUE and returns "ok". When COUNTIF returns zero, IF will return "invalid". The values returned by IF can be customized as needed.

### IF + SEARCH

Another way to use wildcards with the IF function is to combine the [SEARCH](https://exceljet.net/functions/search-function)
 and [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 functions to create a logical test. This works because the SEARCH function supports wildcards:

    =IF(ISNUMBER(SEARCH("??-????-???",B5)),"ok","invalid")

The SEARCH function returns the _position_ of a match inside a text string. If SEARCH does not find a match, it returns a #VALUE! error. The ISNUMBER function is used to convert the result from SEARCH into TRUE or FALSE. Like COUNTIF, SEARCH supports wildcards, so we can use the same pattern to check for invalid codes. For more details on how SEARCH and ISNUMBER can be used together, see [this page.](https://exceljet.net/formulas/if-cell-contains)

_Note: The COUNTIF function has a limitation – the range argument [must be a range](https://exceljet.net/articles/excels-racon-functions)
. It's not possible to pass an [array](https://exceljet.net/glossary/array)
 from another function into COUNTIF. If you run into this problem, you can use SEARCH + ISNUMBER option above instead._

Related formulas
----------------

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    

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