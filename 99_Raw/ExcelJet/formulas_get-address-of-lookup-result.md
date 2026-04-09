# Get address of lookup result - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-address-of-lookup-result

---

[Skip to main content](https://exceljet.net/formulas/get-address-of-lookup-result#main-content)

[](https://exceljet.net/formulas/get-address-of-lookup-result#)

*   [Previous](https://exceljet.net/formulas/find-missing-values)
    
*   [Next](https://exceljet.net/formulas/get-all-matches-cell-contains)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get address of lookup result
============================

by Dave Bruns · Updated 1 May 2023

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Get address of lookup result](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_address_of_lookup_result.png "Excel formula: Get address of lookup result")

Summary
-------

To get the address of the result returned by the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 or the [INDEX function](https://exceljet.net/functions/index-function)
, you can use the [CELL function](https://exceljet.net/functions/cell-function)
. In the example shown, the formula in cell F6 is:

    =CELL("address",XLOOKUP(F4,B5:B17,C5:C17))
    

The result is $C$10, the _address_ of the cell returned by XLOOKUP. See below for an [INDEX and MATCH example](https://exceljet.net/articles/index-and-match)
.

_Note: the CELL function is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems in large or complex worksheets. It is used in this example to show how to troubleshoot or confirm a lookup result._

Generic formula
---------------

    =CELL("address",XLOOKUP(value,range,range))

Explanation 
------------

There are certain functions in Excel that return a cell reference as a result rather than a value. Two of these functions are [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 and [INDEX](https://exceljet.net/functions/index-function)
. The presence of the cell reference in the result is not obvious, because Excel immediately resolves the reference to the value in that cell. You can check the reference returned by XLOOKUP or INDEX with the [CELL function](https://exceljet.net/functions/cell-function)
. This can be useful when debugging a lookup formula to confirm the result being returned.

### XLOOKUP function

XLOOKUP is a function in Excel that returns a cell reference as a result instead of a value. You can inspect the reference returned by XLOOKUP by wrapping the formula in the CELL function with "address" as _info\_type_. In the example shown, the formula in cell F6 is:

    =CELL("address",XLOOKUP(F4,B5:B17,C5:C17))
    

Working from the inside out, the formula is an ordinary XLOOKUP formula:

    =XLOOKUP(F4,B5:B17,C5:C17)
    

With a lookup value of "Sat" in cell F4, XLOOKUP returns 325, the Sales amount on the _first_ entry for Saturday. However, underneath the surface, XLOOKUP is actually returning a _reference_ to cell C10. We can check that result by [nesting](https://exceljet.net/glossary/nesting)
 the XLOOKUP function inside the CELL function, and providing "address" for the _info\_type_ argument:

    =CELL("address",XLOOKUP(F4,B5:B17,C5:C17)) // returns $C$10
    

The CELL function returns $C$10, the _address_ of the cell returned by XLOOKUP.  Note that if we configure XLOOKUP to perform a reverse search, by providing -1 for the _search\_mode_ argument, the result is $C$17:

    =CELL("address",XLOOKUP(F4,B5:B17,C5:C17,,,-1)) // returns $C$17

This is the address of the second (and last) entry for Saturday in the data.

### INDEX and MATCH

Like the XLOOKUP function, the [INDEX function](https://exceljet.net/functions/index-function)
 is another function that returns an address. The equivalent [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula that retrieves the Sales amount for "Sat" in F4 is:

    =INDEX(C5:C17,MATCH(F4,B5:B17,0))

By wrapping the formula in the [CELL function](https://exceljet.net/functions/cell-function)
, we can get Excel to show us the address to the cell returned by INDEX:

    =CELL("address",INDEX(C5:C17,MATCH(F4,B5:B17,0))) // returns $C$10

The CELL function returns $C$10, the _address_ of the cell returned by INDEX.

Related formulas
----------------

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: XLOOKUP basic exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20exact%20match_0.png "Excel formula: XLOOKUP basic exact match")](https://exceljet.net/formulas/xlookup-basic-exact-match)

### [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)

In the example shown, cell G4 contains the lookup value, "Berlin". XLOOKUP is configured to find this value in the table, and return the population. The formula in G5 is: =XLOOKUP(G4,B5:B18,D5:D18) // get population The lookup\_value comes from cell G4 The lookup\_array is the range B5:B18, which...

Related functions
-----------------

[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)

### [CELL Function](https://exceljet.net/functions/cell-function)

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)
    

### Functions

*   [CELL Function](https://exceljet.net/functions/cell-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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