# XLOOKUP case-sensitive  - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/xlookup-case-sensitive#main-content)

[](https://exceljet.net/formulas/xlookup-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/xlookup-binary-search)
    
*   [Next](https://exceljet.net/formulas/xlookup-date-of-max-value)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP case-sensitive
======================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[EXACT](https://exceljet.net/functions/exact-function)

![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")

Summary
-------

To create a case-sensitive lookup with the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
. In the example shown, the formula in G5 is:

    =XLOOKUP(TRUE,EXACT(data[Color],F5),data[Qty])
    

where "data" is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:D16. The result is that XLOOKUP matches the text "RED" in row 5 of the table and returns 10 from the Qty column in the same row.

Generic formula
---------------

    =XLOOKUP(TRUE,EXACT(range1,A1),range2)

Explanation 
------------

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is _not_ case-sensitive and this applies to standard lookup formulas like [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, and [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. These formulas will simply return the _first_ match, ignoring case. For example, if we use a standard XLOOKUP formula like this:

    =XLOOKUP("RED",data[Color],data[Qty]) // returns 17
    

XLOOKUP will match "Red" in row 3 of the table and return 17, even though the lookup value is "RED" in uppercase.

We need a way to get Excel to compare case. The [EXACT function](https://exceljet.net/functions/exact-function)
 is perfect for this job, but the way we use it is a little different. Instead of comparing one [text value](https://exceljet.net/glossary/text-value)
 to another, we compare one text value to _many_ values. In a nutshell, we use the EXACT function to generate an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values, then use the XLOOKUP function to locate the first TRUE in the array.

Like many advanced formulas in Excel, this approach requires you to _imagine_ what the formula is doing, even though the process is largely invisible. There is no shortcut to mastering these ideas, you just have to practice :)

### Background reading

This article assumes you are familiar with the XLOOKUP function and Excel Tables. If not, see:

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     - introduction and overview
*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
     - 3-minute video

### EXACT function

Working from the inside out, to give XLOOKUP the ability to match case, we use the [EXACT function](https://exceljet.net/functions/exact-function)
 like this:

    EXACT(data[Color],F5)
    

Since there are 12 values in the Color column, the EXACT function will return an [array](https://exceljet.net/glossary/array)
 with 12 TRUE and FALSE results like this:

    {FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE}
    

Notice the position of the first TRUE (5) corresponds to row 5 in the table, where Color is "RED". EXACT returns TRUE again for "RED" in row 9 of the table. Every other result is FALSE, including "Red" in row 3.

### XLOOKUP with EXACT

As explained above, the EXACT function creates an array of TRUE and FALSE values, one for each value in the Color column. This array is returned directly to the XLOOKUP function as the _lookup\_array_ argument. Now we need to give XLOOKUP an appropriate _lookup\_value_. Instead of looking for "RED" (the original lookup value), we provide the value TRUE. This may seem a bit strange, but remember that when the EXACT function runs, it returns an array of TRUE/FALSE values. The original values are gone and thus we need to look for TRUE and not "RED".

Finally, we need to provide a _return\_array_. This is the column that contains the values we want as a result. In this example, _return\_array_ is the last column in the table, data\[Qty\]. The final formula in cell G5 looks like this:

    =XLOOKUP(TRUE,EXACT(data[Color],F5),data[Qty]) // returns 10
    

In summary, the EXACT function compares the value in F5 with every value in data\[Color\], generating an array of TRUE and FALSE values. This array is returned to XLOOKUP as the _lookup\_array_. XLOOKUP locates the TRUE at position 5 in the array and returns the value at row 5 in the Qty column, 10 as a final result. 

Notice that XLOOKUP matches on the first TRUE and not the second and last TRUE. This is standard behavior for Excel's lookup functions when there is more than one match. 

### Alternate syntax

You may sometimes see an alternate syntax like this:

    =XLOOKUP(1,--EXACT(data[Color],F5),data[Qty]) // returns 10
    

The behavior of this formula is the same. However, in this version, we convert the TRUE and FALSE values returned by EXACT to 1s and 0s with the [double negative](https://exceljet.net/glossary/double-unary)
:

    --EXACT(data[Color],F5) // convert to 1s and 0s
    

This yields an array like this:

    {0;0;0;0;1;0;0;0;1;0;0;0}
    

The positions of the 1s in this array correspond to the rows where the color is "RED". This array is returned directly to the XLOOKUP function as the lookup array argument. We can now rewrite the formula like this:

    =XLOOKUP(1,{0;0;0;0;1;0;0;0;1;0;0;0},data[Qty])
    

With a lookup value of 1, XLOOKUP finds the 1 in the 5th position and again returns the value at row 5 in the Quantity column: 10.

This use of 1s and 0s is common in formulas that use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 because Excel automatically coerces TRUE and FALSE values to 1s and 0s during any math operation. See below for an example.

### Extending the logic

The structure of the logic can be easily extended. For example, to narrow the match to "RED" in May, you can use a formula like this:

    =XLOOKUP(1,EXACT(data[Color],F5)*(MONTH(data[Date])=5),data[Qty])
    

Here, because each of the two expressions returns an array of TRUE FALSE values, and because these arrays are multiplied together, the math operation coerces the TRUE and FALSE values to 1s and 0s. It is not necessary to use the double-negative. The lookup value remains 1, as in the formula above. Once this operation is complete, the formula looks like this:

    =XLOOKUP(1,{0;0;0;0;0;0;0;0;1;0;0;0},data[Qty])
    

XLOOKUP locates the 1 in the 9th position and returns 14 as a final result

### First and last match

If there is more than one match in _lookup\_array_, XLOOKUP will return the _first_ match by default. To force XLOOKUP to return the _last_ match, set the [search mode argument for XLOOKUP](https://exceljet.net/functions/xlookup-function)
 to -1:

    =XLOOKUP(1,--EXACT(data[Color],F5),data[Qty],,,-1) // last match
    

This version of the formula will return 14 as a final result.

If you need to return _multiple_ results for _multiple_ matches, see the [FILTER function](https://exceljet.net/functions/filter-function)
.

Related formulas
----------------

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: VLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20case%20sensitive.png "Excel formula: VLOOKUP case-sensitive ")](https://exceljet.net/formulas/vlookup-case-sensitive)

### [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on Color with VLOOKUP. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". This presents several challenges. First, Excel is not case-sensitive by default, and there is no built-in...

[![Excel formula: FILTER case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20case%20sensitive.png "Excel formula: FILTER case-sensitive")](https://exceljet.net/formulas/filter-case-sensitive)

### [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)

This formula relies on the FILTER function to retrieve data based on a logical test . The array argument is provided as B5:D15, which contains all of the data without headers. The include argument is an expression based on the EXACT function: EXACT(B5:B15,"RED") The EXACT function compares two text...

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: XLOOKUP match text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20match%20text%20contains.png "Excel formula: XLOOKUP match text contains")](https://exceljet.net/formulas/xlookup-match-text-contains)

### [XLOOKUP match text contains](https://exceljet.net/formulas/xlookup-match-text-contains)

The XLOOKUP function contains built-in support for wildcards, but this feature must be enabled explicitly by setting match mode to the number 2. In the example shown, XLOOKUP is configured to match the value entered in cell E5, which may appear anywhere in the lookup values in B5:B15. The formula...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

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
    
*   [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)
    
*   [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)
    
*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
    
*   [XLOOKUP match text contains](https://exceljet.net/formulas/xlookup-match-text-contains)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

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