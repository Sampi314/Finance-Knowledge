# XMATCH with multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xmatch-with-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/xmatch-with-multiple-criteria#main-content)

[](https://exceljet.net/formulas/xmatch-with-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/xmatch-reverse-search)
    
*   [Next](https://exceljet.net/formulas/zodiac-sign-lookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XMATCH with multiple criteria
=============================

by Dave Bruns · Updated 2 May 2025

Related functions 
------------------

[XMATCH](https://exceljet.net/functions/xmatch-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: XMATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XMATCH_with_multiple_criteria.png "Excel formula: XMATCH with multiple criteria")

Summary
-------

The best way to use [XMATCH](https://exceljet.net/functions/xmatch-function)
 with multiple criteria is to use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to apply conditions. In the example shown, the formula in H8 is:

    =XMATCH(1,(B5:B15=H5)*(C5:C15=H6)*(D5:D15=H7))
    

The result is 6, since the sixth row in the data contains a Medium Blue Hoodie. Note the _lookup\_value_ in XMATCH is 1. This is because the _lookup\_array_ is an [array](https://exceljet.net/glossary/array)
 that contains only 1s and 0s. Read below for details.

Generic formula
---------------

    =XMATCH(1,(criteria1)*(criteria2)*(criteria3))

Explanation 
------------

The goal is to match a row in a set of data based on a given Item, Size, and Color. At a glance, this seems like a difficult problem because XMATCH only has one value for _lookup\_value_ and _lookup\_array_. How can we configure XMATCH to consider values from _multiple_ columns? The trick is to _generate_ the lookup array we need using Boolean logic, then configure XMATCH to look for the number 1. This approach is explained below.

### The XMATCH function

The XMATCH function is an upgraded replacement for the older [MATCH function](https://exceljet.net/functions/match-function)
. At the core, XMATCH performs a lookup and returns the numeric position of the lookup value in a range or array as the result. XMATCH performs an exact match by default and in its simplest form, requires just two [arguments](https://exceljet.net/glossary/function-argument)
, a lookup value and a lookup array:

    =XMATCH(lookup_value,lookup_array)

Looking at the generic syntax above, you can see there is no obvious way to provide multiple criteria.

### Boolean Logic

This formula works around this limitation by using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to create a temporary [array](https://exceljet.net/glossary/array)
 of ones and zeros to represent rows matching all 3 criteria, then asking XMATCH to find the first 1 in the array. The temporary array of ones and zeros is generated like this:

    (B5:B15=H5)*(C5:C15=H6)*(D5:D15=H7)
    

This code compares the Item entered in H5 with all items, the Size in H6 with all sizes, and the Color in H7 with all colors. Each expression generates an array of TRUE and FALSE values as seen below:

    {FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE}*{FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;FALSE}*{FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

> Tip: [use F9 to see these results](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
> . Just select an expression in the formula bar, and press F9.

Next, the math operation (multiplication) automatically converts the TRUE and FALSE values to 1s and 0s:

    {0;0;0;0;1;1;1;0;0;0;0}*{0;1;0;0;0;1;0;1;1;0;0}*{0;1;0;1;0;1;0;0;0;0;0}
    

This behavior is a basic feature of [how Excel works with Boolean values](https://exceljet.net/videos/introduction-to-booleans)
. After the arrays are multiplied together, we have just a single array of 1s and 0s like this:

    {0;0;0;0;0;1;0;0;0;0;0}
    

Notice the 6th value in the array is 1. This represents the one row in the data that meets all three conditions, since this row contains a Medium Blue Hoodie. This is the array used inside XMATCH as the _lookup\_array_. Because the _lookup\_array_ contains only 1s and 0s, we provide 1 as the _lookup\_value_. At this point, we can rewrite the formula like this:

    =XMATCH(1,{0;0;0;0;0;1;0;0;0;0;0}) // returns 6

XMATCH matches the 1 in the sixth row of the array and returns 6 as a final result.

### Visualizing arrays

The [arrays](https://exceljet.net/glossary/array)
 explained above can be challenging to understand since they aren't visible when the formula calculates. The screen below shows how the arrays can be visualized with simple formulas in a worksheet. Columns B, C, and D correspond to the data in the example when the logical expressions for "Hoodie", "Medium", and "Blue" are being evaluated." Column F is the result of multiplying the ranges together:

![XLOOKUP with multiple criteria - visualizing Boolean arrays](https://exceljet.net/sites/default/files/images/formulas/inline/XMATCH_with_multiple_criteria_array_visualization.png "XLOOKUP with multiple criteria - visualizing Boolean arrays")

The result in F5:F15 represents the array delivered to XMATCH as the _lookup\_array_.

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### INDEX and XMATCH

Typically, the XMATCH function is used in an [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula to return a value instead of a position. In the original worksheet above, the formula in cell H9 uses INDEX with XMATCH to retrieve the correct price for a Medium Blue Hoodie:

    =INDEX(E5:E15,XMATCH(1,(B5:B15=H5)*(C5:C15=H6)*(D5:D15=H7)))

### Notes

1.  The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
     can also be configured to use multiple criteria in the same way.
2.  This approach can be adapted to apply [more complex criteria](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
    .

Related formulas
----------------

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: XLOOKUP with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20with%20complex%20multiple%20criteria.png "Excel formula: XLOOKUP with complex multiple criteria")](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)

### [XLOOKUP with complex multiple criteria](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)

Normally, the XLOOKUP function is configured to look for a value in a lookup array that exists on the worksheet. However, when the criteria used to match a value becomes more complex, you can use Boolean logic to create a lookup array on the fly composed only of 1s and 0s, then look for the value 1...

Related functions
-----------------

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/XLOOKUP%20with%20boolean%20logic-Play.png)](https://exceljet.net/videos/xlookup-with-boolean-logic)

### [XLOOKUP with boolean logic](https://exceljet.net/videos/xlookup-with-boolean-logic)

In this video we'll look at how to use the XLOOKUP function with Boolean logic. Boolean logic is an elegant way to apply multiple criteria. In this worksheet we have sample order data in a table called "data". Let's use the XLOOKUP function to find the first order in March where the color is red...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

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
    
*   [XLOOKUP with complex multiple criteria](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
    

### Functions

*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [XLOOKUP with boolean logic](https://exceljet.net/videos/xlookup-with-boolean-logic)
    
*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    

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