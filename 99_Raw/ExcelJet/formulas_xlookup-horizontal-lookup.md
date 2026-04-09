# XLOOKUP horizontal lookup - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-horizontal-lookup

---

[Skip to main content](https://exceljet.net/formulas/xlookup-horizontal-lookup#main-content)

[](https://exceljet.net/formulas/xlookup-horizontal-lookup#)

*   [Previous](https://exceljet.net/formulas/xlookup-date-of-max-value)
    
*   [Next](https://exceljet.net/formulas/xlookup-last-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP horizontal lookup
=========================

by Dave Bruns · Updated 11 Oct 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[HLOOKUP](https://exceljet.net/functions/hlookup-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8623/download?token=YbjlNJM9)
 (20.95 KB)

![Excel formula: XLOOKUP horizontal lookup](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP%20horizontal%20lookup.png "Excel formula: XLOOKUP horizontal lookup")

Summary
-------

To perform a horizontal lookup with the XLOOKUP function, supply a lookup value, a lookup array, and a result array. Provide a _match\_mode_ argument for an approximate match if needed. In the example shown, the formula in D5, copied down the table, is:

    =XLOOKUP(B5,quantity,discount,,-1)
    

where **quantity** (G6:L6) and **discount** (G7:L7) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =XLOOKUP(A1,range1,range2,,-1) // approximate match

Explanation 
------------

In this example, the goal is to perform a horizontal lookup to determine the correct quantity-based discount. The range G6:L7 contains quantity-based discounts. Column B contains random quantities used when testing the formula. This problem can be easily solved with the XLOOKUP function or the HLOOKUP function. Both methods are explained below.

### XLOOKUP formula

One of XLOOKUP's nice benefits is its ability to work with vertical or horizontal data. The syntax used for horizontal lookups is the same as for vertical lookups. In the worksheet shown, the formula in cell D5, copied down, is:

    =XLOOKUP(B5,quantity,discount,,-1)

Where **quantity** (G6:L6) and **discount** (G7:L7) are [named ranges](https://exceljet.net/glossary/named-range)
 used for convenience and readability only. The same formula _without named ranges_ looks like this:

    =XLOOKUP(B5,$G$6:$L$6,$G$7:$L$7,,-1)
    

Note that the _lookup\_array_ and _return\_array_ are both provided as absolute references to lock these ranges as these formulas are copied down. This is not required with named ranges because they automatically behave as absolute references.

XLOOKUP's arguments are configured as follows:

*   The _lookup\_value_ comes from cell B5
*   The _lookup\_array_ is the named range **quantity** (G6:L6)
*   The _return\_array_ is the named range **discount** (G7:L7)
*   The _not\_found_ argument is omitted
*   The _match\_mode_ is set to -1 (exact match or next smaller)
*   The _search\_mode_ is omitted and defaults to 1 (first to last)

At each row, XLOOKUP looks up the quantity in column B. If an exact match is found, the corresponding discount in row 7 is returned. When an exact match is _not found_, the discount associated with the _next smallest_ quantity is returned. 

> In this particular problem, we set _match\_mode_ to -1 to enable an approximate match. This is because the input quantities will not match the table values in G6:L6 exactly in most cases. In other problems that require an exact match, you will want to set _match\_mode_ to zero (0) to enable an exact match.

### HLOOKUP formula

Working with HLOOKUP is similar to working with the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
. Both functions require the _entire lookup table_ as the _table\_array_ argument and use an index number to specify return values. However, for VLOOKUP, the index number represents a _column number_, while for HLOOKUP, the index represents a _row number_. This problem can also be solved with the [HLOOKUP function](https://exceljet.net/functions/hlookup-function)
 like this:

    =HLOOKUP(B5,data,2,TRUE)
    

Where **data** is the named range G6:L7.

![HLOOKUP formula to solve the same problem](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/XLOOKUP_horizontal_lookup_HLOOKUP_formula.png "HLOOKUP formula to solve the same problem")

In the formula above, the arguments are configured like this:

*   The _lookup\_value_ comes from cell B5
*   The _table\_array_ is provided as **data** (G6:L7)
*   The _row\_index\_num_ is provided as 2 since discounts are in the second row.
*   The _range\_lookup_ argument is provided as TRUE to explicitly enable an approximate match.

Named ranges automatically behave like locked references when copied. Without named ranges, the same formula would need an absolute reference for the lookup table like this:

    =HLOOKUP(B5,$G$6:$L$7,2,TRUE)

The absolute reference prevents _table\_array_ from changing as the formula is copied down the table. 

> Because HLOOKUP will perform an approximate match by default, it is _not necessary_ to provide the TRUE value for _range\_lookup_. However, because this feature can cause a lot of confusion, I recommend you always provide a value as a reminder to yourself and others of the behavior you expect.

### XLOOKUP vs HLOOKUP

When we compare the XLOOKUP formula to the HLOOKUP formula, there are several differences worth noting:

*   HLOOKUP requires the full table array. XLOOKUP requires only the range that contains lookup values.
*   HLOOKUP requires a row index to specify a result column. XLOOKUP requires a range that contains result values.
*   HLOOKUP performs an approximate match _by default_. XLOOKUP performs an exact match by default, so we must set _match\_mode_ to -1 (exact match or next smaller).
*   HLOOKUP requires lookup data to be sorted by lookup value. XLOOKUP works with unsorted data.
*   HLOOKUP performs horizontal lookups only. XLOOKUP can perform both horizontal and vertical lookups.

### INDEX and MATCH

Naturally, you can also solve this problem with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, the Swiss Army Knife of lookup formulas :) With named ranges, the formula will look like this:

    =INDEX(discount,1,MATCH(B5,quantity,1))

I've included all three options on different sheets. Download the workbook and try it out yourself.

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

[![Excel HLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hlookup%20function.png "Excel HLOOKUP function")](https://exceljet.net/functions/hlookup-function)

### [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)

The Excel HLOOKUP function finds and retrieve a value from data in a horizontal table. The "H" in HLOOKUP stands for "horizontal", and lookup values must appear in the first row of the table, moving horizontally to the right. HLOOKUP supports approximate and exact matching, and...

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
    
*   [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)
    
*   [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [HLOOKUP Function](https://exceljet.net/functions/hlookup-function)
    

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