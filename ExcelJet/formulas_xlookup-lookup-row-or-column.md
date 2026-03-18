# XLOOKUP lookup row or column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-lookup-row-or-column

---

[Skip to main content](https://exceljet.net/formulas/xlookup-lookup-row-or-column#main-content)

[](https://exceljet.net/formulas/xlookup-lookup-row-or-column#)

*   [Previous](https://exceljet.net/formulas/xlookup-lookup-left)
    
*   [Next](https://exceljet.net/formulas/xlookup-match-text-contains)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP lookup row or column
============================

by Dave Bruns · Updated 21 Feb 2020

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

![Excel formula: XLOOKUP lookup row or column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20lookup%20row%20or%20column.png "Excel formula: XLOOKUP lookup row or column")

Summary
-------

XLOOKUP can be used to lookup and retrieve rows or columns. In the example shown, the formula in H5 is:

    =XLOOKUP(H4,C4:F4,C5:F8)
    

Since all data in the C5:F8 is provided as the _return\_array_ XLOOKUP returns the range E5:E8 as a result, which [spills](https://exceljet.net/glossary/spill)
 into the range H5:H8.

Generic formula
---------------

    =XLOOKUP(value,headers,data) // lookup row

Explanation 
------------

One of the nice benefits of XLOOKUP is it can easily return entire rows or columns as a lookup result. This can be done also with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, but the syntax is more complex.

In the example shown, we want to retrieve all values associated with Q3. The formula in H5 is:

    =XLOOKUP(H4,C4:F4,C5:F8)
    

*   The _lookup\_value_ comes from cell H4, which contains "Q3"
*   The _lookup\_array_ is the range C4:F4, which quarters in a header
*   The _return\_array_ is C5:F8, which contains all data
*   The _match\_mode_ is not provided and defaults to 0 (exact match)
*   The _search\_mode_ is not provided and defaults to 1 (first to last)

XLOOKUP finds "Q3" as the second item in C4:F4 and returns the second column of the _return\_array_, the range E5:E8.

### Lookup row

In the example shown, XLOOKUP is also used to lookup a row. The formula in C10 is:

    =XLOOKUP(B10,B5:B8,C5:F8)
    

*   The _lookup\_value_ comes from cell B10, which contains "Central"
*   The _lookup\_array_ is the range B5:B8, which lists regions
*   The _return\_array_ is C5:F8, which contains all data
*   The _match\_mode_ is not provided and defaults to 0 (exact match)
*   The _search\_mode_ is not provided and defaults to 1 (first to last)

XLOOKUP finds "Central" as the third item in B5:B8 and returns the third row of the _return\_array_, the range C7:F7.

### Further processing with other functions

The results delivered by XLOOKUP can be handed off to other functions for further processing. For example, to add up all Q3 numbers, you can use the SUM function like this:

    =SUM(XLOOKUP("Q3",C4:F4,C5:F8)) // sum Q3
    

which returns a single result, 503,250.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: XLOOKUP lookup left](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20lookup%20left.png "Excel formula: XLOOKUP lookup left")](https://exceljet.net/formulas/xlookup-lookup-left)

### [XLOOKUP lookup left](https://exceljet.net/formulas/xlookup-lookup-left)

Whereas VLOOKUP is limited to lookups to the right of the lookup column, XLOOKUP can lookup values to the left natively. This means XLOOKUP can be used instead of INDEX and MATCH to find values to the left in a table or range. In the example shown, we are looking for the weight associated with...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Look up entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20column.png "Excel formula: Look up entire column")](https://exceljet.net/formulas/look-up-entire-column)

### [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)

In this example, the goal is to look up and retrieve an entire column of values in a set of data. For example, when a value like "Q3" is entered into cell H4, all values in the range E5:E16 should be returned. For convenience and readability, quarter (C4:F4) and data (C5:F16) are named ranges ...

Related functions
-----------------

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

*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [XLOOKUP lookup left](https://exceljet.net/formulas/xlookup-lookup-left)
    
*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

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