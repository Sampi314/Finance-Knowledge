# XLOOKUP two-way exact match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-two-way-exact-match

---

[Skip to main content](https://exceljet.net/formulas/xlookup-two-way-exact-match#main-content)

[](https://exceljet.net/formulas/xlookup-two-way-exact-match#)

*   [Previous](https://exceljet.net/formulas/xlookup-return-blank-if-blank)
    
*   [Next](https://exceljet.net/formulas/xlookup-wildcard-contains-substring)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP two-way exact match
===========================

by Dave Bruns · Updated 21 Feb 2020

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: XLOOKUP two-way exact match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20two-way%20exact%20match.png "Excel formula: XLOOKUP two-way exact match")

Summary
-------

To perform a two-lookup with the XLOOKUP function (a double XLOOKUP), you can nest one XLOOKUP inside another. In the example shown, the formula in H6 is:

    =XLOOKUP(H5,months,XLOOKUP(H4,names,data))
    

where **months** (C4:E4) and **names** (B5:B13), and **data** (C5:E13) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =XLOOKUP(A1,months,XLOOKUP(A2,names,data))

Explanation 
------------

One of XLOOKUP's features is the ability to lookup and return an entire row or column. This feature can be used to [nest](https://exceljet.net/glossary/nesting)
 one XLOOKUP inside another to perform a two-way lookup. The inner XLOOKUP returns a result to the outer XLOOKUP, which returns a final result.

_Note: XLOOKUP performs an exact match by default, so match mode is not set._

Working from the inside out, the _inner_ XLOOKUP is used to retrieve all data for "Frantz":

    XLOOKUP(H4,names,data)
    

XLOOKUP finds "Frantz" in the [named range](https://exceljet.net/glossary/named-range)
 **names** (B5:B13). Frantz appears in the fifth row, so XLOOKUP returns the fifth row of **data** (C5:E13). The result is an [array](https://exceljet.net/glossary/array)
 representing a single row of data for Frantz, containing 3 months of sales:

    {10699,5194,10525} // data for Frantz
    

This array is returned directly to the _outer_ XLOOKUP as the return\_array:

    =XLOOKUP(H5,months,{10699,5194,10525})
    

The outer XLOOKUP finds the value in H5 ("Mar") inside the named range **months** (C4:E4). The value "Mar" appears as the third item, so XLOOKUP returns the third item from the sales data, the value 10525.

### Without named ranges

The named ranges used in this example are for readability only. Without named ranges, the formula is:

    =XLOOKUP(H5,C4:E4,XLOOKUP(H4,B5:B13,C5:E13))
    

### INDEX and MATCH

This example can be solved with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 like this:

    =INDEX(C5:E13,MATCH(H4,B5:B13,0),MATCH(H5,C4:E4,0))
    

INDEX and MATCH is a good solution to this problem, and probably easier to understand for most people. However, the XLOOKUP version shows off the power and flexibility of XLOOKUP.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: XLOOKUP basic exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20exact%20match_0.png "Excel formula: XLOOKUP basic exact match")](https://exceljet.net/formulas/xlookup-basic-exact-match)

### [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)

In the example shown, cell G4 contains the lookup value, "Berlin". XLOOKUP is configured to find this value in the table, and return the population. The formula in G5 is: =XLOOKUP(G4,B5:B18,D5:D18) // get population The lookup\_value comes from cell G4 The lookup\_array is the range B5:B18, which...

[![Excel formula: XLOOKUP basic approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20approximate%20match.png "Excel formula: XLOOKUP basic approximate match")](https://exceljet.net/formulas/xlookup-basic-approximate-match)

### [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)

In the example shown, the table in B4:C13 contains quantity-based discounts. As the quantity increases, the discount also increases. The table in E4:F10 shows the discount returned by XLOOKUP for several random quantities. XLOOKUP is configured to use the quantity in column E to find the...

Related functions
-----------------

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)
    
*   [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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