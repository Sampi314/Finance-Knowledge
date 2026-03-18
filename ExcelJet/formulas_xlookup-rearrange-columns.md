# XLOOKUP rearrange columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-rearrange-columns

---

[Skip to main content](https://exceljet.net/formulas/xlookup-rearrange-columns#main-content)

[](https://exceljet.net/formulas/xlookup-rearrange-columns#)

*   [Previous](https://exceljet.net/formulas/xlookup-match-text-contains)
    
*   [Next](https://exceljet.net/formulas/xlookup-return-blank-if-blank)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP rearrange columns
=========================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

![Excel formula: XLOOKUP rearrange columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20rearrange%20columns.png "Excel formula: XLOOKUP rearrange columns")

Summary
-------

One way to reorder columns in Excel is to use a formula that nests one [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 inside another. In the example shown, The formula in G9 is:

    =XLOOKUP(G8:J8,B4:E4,XLOOKUP(G5,E5:E15,B5:E15))
    

The result is a match on the value in G5, with all 4 fields in the order specified in the range G8:J8.

Generic formula
---------------

    =XLOOKUP(neworder,oldorder,XLOOKUP(val,lookup,results))

Explanation 
------------

This formula uses XLOOKUP twice, by [nesting](https://exceljet.net/glossary/nesting)
 one XLOOKUP inside another. The first (inner) XLOOKUP is used to perform an exact match lookup on the value in G5:

    XLOOKUP(G5,E5:E15,B5:E15)
    

*   The _lookup\_value_ comes from cell G5
*   The _lookup\_array_ is E5:E15 (codes)
*   The _return\_array_ is B5:E15 (all fields)
*   The _match\_mode_ is not provided and defaults to 1 (exact match)
*   The _search\_mode_ is not provided and defaults to 1 (first to last)

The result is a match on "AX-160", returned as an array of all four fields in the original order:

    {160,130,60,"AX-160"}
    

This result is delivered directly to the second (outer) XLOOKUP as the return array argument. The lookup value is provided as a range representing the _new_ order of fields, and the lookup array is the range containing the _original_ field name order.

    =XLOOKUP(G8:J8,B4:E4,{160,130,60,"AX-160"})
    

*   The _lookup\_value_ is the range G8:J8 (new field order)
*   The _lookup\_array_ is the range B4:E4 (old field order)
*   The _return\_array_ is the result from the first XLOOKUP

This is the tricky bit. We are passing in multiple lookup values, so XLOOKUP internally will calculate multiple match positions. For each value in the _new field order range_, XLOOKUP will find a position inside the _old field order range_ and use this position to fetch a value from the return array (the values returned by the first XLOOKUP function). The result is the original lookup result with fields arranged in the new order.

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

[![Excel formula: XLOOKUP two-way exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20two-way%20exact%20match.png "Excel formula: XLOOKUP two-way exact match")](https://exceljet.net/formulas/xlookup-two-way-exact-match)

### [XLOOKUP two-way exact match](https://exceljet.net/formulas/xlookup-two-way-exact-match)

One of XLOOKUP's features is the ability to lookup and return an entire row or column. This feature can be used to nest one XLOOKUP inside another to perform a two-way lookup. The inner XLOOKUP returns a result to the outer XLOOKUP, which returns a final result. Note: XLOOKUP performs an exact...

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
    
*   [XLOOKUP two-way exact match](https://exceljet.net/formulas/xlookup-two-way-exact-match)
    

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