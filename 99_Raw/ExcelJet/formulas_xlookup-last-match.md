# XLOOKUP last match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-last-match

---

[Skip to main content](https://exceljet.net/formulas/xlookup-last-match#main-content)

[](https://exceljet.net/formulas/xlookup-last-match#)

*   [Previous](https://exceljet.net/formulas/xlookup-horizontal-lookup)
    
*   [Next](https://exceljet.net/formulas/xlookup-latest-by-date)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP last match
==================

by Dave Bruns · Updated 21 May 2020

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

![Excel formula: XLOOKUP last match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20last%20match.png "Excel formula: XLOOKUP last match")

Summary
-------

To retrieve the last match in a data set with XLOOKUP, set the fifth argument to -1. In the example shown, the formula in G5, copied down, is:

    =XLOOKUP(F5,item,price,0,-1)
    

where **item** (B5:B15) and **price** (D5:D15) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =XLOOKUP(value,rng1,rng2,"no match",0,-1) // last exact match
    

Explanation 
------------

By default, XLOOKUP will return the first match in a data set. However, XLOOKUP offers an optional argument called search\_mode to control the order in which data is searched. Setting search mode to -1 causes XLOOKUP to search "last to first" or, in other words, search _backwards_ through the data. You can see this option used in the example shown. The formula in G5, copied down, is:

    =XLOOKUP(F5,item,price,"no match",0,-1)
    

The same formula without named ranges is:

    =XLOOKUP(F5,$B$5:$B$15,$D$5:$D$15,"no match",0,-1)
    

XLOOKUP's arguments are configured as follows:

*   The _lookup\_value_ comes from cell F5
*   The _lookup\_array_ is the named range **item** (B5:B15)
*   The _return\_array_ is the named range **price** (D5:D15)
*   The _not\_found_ argument is provided as "no match"
*   The _match\_mode_ is set to 0 (exact match)
*   The _search\_mode_ is set to -1 (last to first)

At each row, XLOOKUP looks for the item name in column F in B5:B15, starting at the _bottom_. When an exact match is found, the corresponding price in column D is returned. If no match is found, XLOOKUP will return #N/A.

_Note: this example depends on data being sorted by date in ascending order. If data is unsorted, [see this example](https://exceljet.net/formulas/xlookup-latest-by-date)
._

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: XLOOKUP latest by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20latest%20by%20date.png "Excel formula: XLOOKUP latest by date")](https://exceljet.net/formulas/xlookup-latest-by-date)

### [XLOOKUP latest by date](https://exceljet.net/formulas/xlookup-latest-by-date)

XLOOKUP offers several features that make it exceptionally good for more complicated lookups. In this example, we want the latest price for an item by date . If data were sorted by date in ascending order, this would be very straightforward . However, in this case, data is unsorted . By default,...

[![Excel formula: XLOOKUP basic exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20exact%20match_0.png "Excel formula: XLOOKUP basic exact match")](https://exceljet.net/formulas/xlookup-basic-exact-match)

### [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)

In the example shown, cell G4 contains the lookup value, "Berlin". XLOOKUP is configured to find this value in the table, and return the population. The formula in G5 is: =XLOOKUP(G4,B5:B18,D5:D18) // get population The lookup\_value comes from cell G4 The lookup\_array is the range B5:B18, which...

[![Excel formula: XLOOKUP basic approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20approximate%20match.png "Excel formula: XLOOKUP basic approximate match")](https://exceljet.net/formulas/xlookup-basic-approximate-match)

### [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)

In the example shown, the table in B4:C13 contains quantity-based discounts. As the quantity increases, the discount also increases. The table in E4:F10 shows the discount returned by XLOOKUP for several random quantities. XLOOKUP is configured to use the quantity in column E to find the...

[![Excel formula: Lookup latest price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Lookup%20latest%20price.png "Excel formula: Lookup latest price")](https://exceljet.net/formulas/lookup-latest-price)

### [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)

The LOOKUP function assumes data is sorted, and always does an approximate match. If the lookup value is greater than all values in the lookup array, default behavior is to "fall back" to the previous value. This formula exploits this behavior by creating an array that contains only 1s and errors,...

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

*   [XLOOKUP latest by date](https://exceljet.net/formulas/xlookup-latest-by-date)
    
*   [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)
    
*   [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    

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