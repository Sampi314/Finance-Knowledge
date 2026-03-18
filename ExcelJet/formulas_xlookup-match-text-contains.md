# XLOOKUP match text contains - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-match-text-contains

---

[Skip to main content](https://exceljet.net/formulas/xlookup-match-text-contains#main-content)

[](https://exceljet.net/formulas/xlookup-match-text-contains#)

*   [Previous](https://exceljet.net/formulas/xlookup-lookup-row-or-column)
    
*   [Next](https://exceljet.net/formulas/xlookup-rearrange-columns)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP match text contains
===========================

by Dave Bruns · Updated 23 Oct 2023

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[SEARCH](https://exceljet.net/functions/search-function)

[FIND](https://exceljet.net/functions/find-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: XLOOKUP match text contains](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20match%20text%20contains.png "Excel formula: XLOOKUP match text contains")

Summary
-------

To use XLOOKUP to match values that contain specific text, you can use [wildcards](https://exceljet.net/glossary/wildcard)
 and [concatenation](https://exceljet.net/glossary/concatenation)
. In the example shown, the formula in F5 is:

    =XLOOKUP("*"&E5&"*",code,quantity,"no match",2)
    

where **code** (B5:B15) and **quantity** (C5:C15) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =XLOOKUP("*"&value&"*",lookup,results,,2)

Explanation 
------------

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 contains built-in support for wildcards, but this feature must be enabled explicitly by setting match mode to the number 2.

In the example shown, XLOOKUP is configured to match the value entered in cell E5, which may appear anywhere in the lookup values in B5:B15. The formula in F5 is:

    =XLOOKUP("*"&E5&"*",code,quantity,"no match",2) // returns 50
    

*   _lookup\_value_ - E5, with asterisks (\*) concatenated front and back
*   _lookup\_array_ - the named range **code** (B5:B15)
*   _return\_array_ - the named range **quantity** (C5:C15)
*   _if\_not\_found_ - the string "no match"
*   _match\_mode_ - provided as 2 (wildcard match)
*   _search\_mode_ - not provided. Defaults to 1 (first to last)

To make a "contains" type match automatic, the wildcard asterisk (\*) is both prepended and appended to the value in cell E5 with [concatenation](https://exceljet.net/glossary/concatenation)
:

    "*"&E5&"*"
    

After concatenation, the formula becomes:

    =XLOOKUP("*BCC*",code,quantity,"no match",2)
    

XLOOKUP locates the first match that contains "BCC" (050-BCC-123 in row 10) and returns the corresponding value from the return array, 50.

Note that XLOOKUP is _not_ case-sensitive, entering "bcc" in E5 will return the same result:

    =XLOOKUP("*bcc*",code,quantity,"no match",2) // returns 50
    

See below for an option to configure XLOOKUP for a case-sensitive match.

### VLOOKUP option

The VLOOKUP formula also supports wildcards when set to exact match. The equivalent VLOOKUP formula for this example is:

    =VLOOKUP("*"&E5&"*",B5:C15,2,0)
    

Full [explanation here](https://exceljet.net/formulas/partial-match-with-vlookup)
.

### With SEARCH and FIND

It is also possible to use the [SEARCH](https://exceljet.net/functions/search-function)
 and [FIND](https://exceljet.net/functions/find-function)
 functions to perform a "contains" type match with XLOOKUP. For a case-insensitive match (like the example above), you can use SEARCH like this:

    =XLOOKUP(1,--ISNUMBER(SEARCH("BCC",code)),quantity,"no match",2)
    

For a case-sensitive match, you can use FIND instead:

    =XLOOKUP(1,--ISNUMBER(FIND("BCC",code)),quantity,"no match",2)
    

Both options above make it easier to extend criteria to [include other conditions](https://exceljet.net/formulas/vlookup-with-multiple-criteria)
 using [boolean logic](https://exceljet.net/glossary/boolean-logic)
.

The logic for ISNUMBER + SEARCH is [explained here](https://exceljet.net/formulas/cell-contains-specific-text)
.

### Multiple matches

If you need multiple matches, see the [FILTER function](https://exceljet.net/functions/filter-function)
.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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