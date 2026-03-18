# XLOOKUP latest by date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-latest-by-date

---

[Skip to main content](https://exceljet.net/formulas/xlookup-latest-by-date#main-content)

[](https://exceljet.net/formulas/xlookup-latest-by-date#)

*   [Previous](https://exceljet.net/formulas/xlookup-last-match)
    
*   [Next](https://exceljet.net/formulas/xlookup-lookup-left)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP latest by date
======================

by Dave Bruns · Updated 24 Jan 2023

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[MAX](https://exceljet.net/functions/max-function)

![Excel formula: XLOOKUP latest by date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20latest%20by%20date.png "Excel formula: XLOOKUP latest by date")

Summary
-------

To get the latest match in a set of data _by date_, you can use XLOOKUP in approximate match mode by setting match\_mode to -1. In the example shown, the formula in G5, copied down, is:

    =XLOOKUP(MAX(date),(item=F5)*date,price,,-1)
    

where **date** (C5:C15), **item** (B5:B15) and **price** (D5:D15) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =XLOOKUP(max,dates,results,,-1) // latest match by date
    

Explanation 
------------

XLOOKUP offers several features that make it exceptionally good for more complicated lookups. In this example, we want the latest price for an item _by date_. If data were sorted by date in ascending order, this would be [very straightforward](https://exceljet.net/formulas/xlookup-last-match)
. However, in this case, _data is unsorted_.

By default, XLOOKUP will return the _first match_ in a data set. To get the _last match_, we can set the optional argument _search\_mode_, to -1 to cause XLOOKUP to search "last to first". However, we can't use this approach here because there is no guarantee that the latest price for an item appears last.

Instead, we can set the optional argument _match\_mode_ to -1 to force an approximate match of "exact or next smallest", and adjust the lookup value and lookup array as explained below. The formula in G5, copied down, is:

    =XLOOKUP(MAX(date),(item=F5)*date,price,,-1)
    

Working through arguments one by one, the _lookup\_value_ is the largest (latest) date in the data:

    MAX(date) // get max date value
    

The _lookup\_array_ is derived with a [boolean logic](https://exceljet.net/glossary/boolean-logic)
 expression:

    (item=F5)*date
    

By comparing each item to the value in F5, "Belt", we get an [array](https://exceljet.net/glossary/array)
 of TRUE/FALSE values:

    {TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;TRUE;FALSE;FALSE}
    

where TRUE values represent entries for "Belt". This array acts like a filter. When it is multiplied by the values in the named range **date**, the TRUE/FALSE values are evaluated to 1's and 0's:

    ={1;0;0;0;0;0;1;0;1;0;0}*date
    

The result is an array that contains only zeros and dates for belts:

    ={43484;0;0;0;0;0;43561;0;43671;0;0}
    

_Note: the serial numbers are valid [Excel dates](https://exceljet.net/glossary/excel-date)
._

*   This array is delivered directly to XLOOKUP as the _lookup\_array_ argument.
*   The _return\_array_ is the [named range](https://exceljet.net/glossary/named-range)
     **price** (D5:D15)
*   The optional argument _not\_found_ is not provided.
*   _Match\_mode_ is set to -1, for exact match, or next smallest item.

XLOOKUP looks through the lookup array for the maximum date value. Since the array has already been filtered to exclude dates not associated with "Belt", XLOOKUP simply finds the best match (either the exact date, or the next smallest date) which corresponds to the latest date. The final result is the price associated with the latest date. The formula will continue to work when the data sorted in any order.

Related formulas
----------------

[![Excel formula: XLOOKUP last match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20last%20match.png "Excel formula: XLOOKUP last match")](https://exceljet.net/formulas/xlookup-last-match)

### [XLOOKUP last match](https://exceljet.net/formulas/xlookup-last-match)

By default, XLOOKUP will return the first match in a data set. However, XLOOKUP offers an optional argument called search\_mode to control the order in which data is searched. Setting search mode to -1 causes XLOOKUP to search "last to first" or, in other words, search backwards through the data...

[![Excel formula: Nearest location with XMATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nearest%20location%20with%20XMATCH.png "Excel formula: Nearest location with XMATCH")](https://exceljet.net/formulas/nearest-location-with-xmatch)

### [Nearest location with XMATCH](https://exceljet.net/formulas/nearest-location-with-xmatch)

At the core, this formula is a basic INDEX and MATCH formula . However, instead of using the older MATCH function , we are using XMATCH function , which provides a more powerful match mode setting: =INDEX(location,XMATCH(0,distance,1)) Working from the inside out, we are using the XMATCH function...

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

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

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP last match](https://exceljet.net/formulas/xlookup-last-match)
    
*   [Nearest location with XMATCH](https://exceljet.net/formulas/nearest-location-with-xmatch)
    
*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)
    
*   [Lookup latest price](https://exceljet.net/formulas/lookup-latest-price)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    

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