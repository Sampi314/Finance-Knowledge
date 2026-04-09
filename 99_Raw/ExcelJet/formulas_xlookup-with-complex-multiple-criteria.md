# XLOOKUP with complex multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria#main-content)

[](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)
    
*   [Next](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP with complex multiple criteria
======================================

by Dave Bruns · Updated 15 May 2024

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[LEFT](https://exceljet.net/functions/left-function)

[MONTH](https://exceljet.net/functions/month-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: XLOOKUP with complex multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/xlookup%20with%20complex%20multiple%20criteria.png "Excel formula: XLOOKUP with complex multiple criteria")

Summary
-------

To lookup data based on multiple complex criteria, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 with multiple expressions based on [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. In the example shown, the formula in G5 is:

    =XLOOKUP(1,(LEFT(B5:B16)="x")*(C5:C16="east")*NOT(MONTH(D5:D16)=4),B5:E16)
    

With XLOOKUP's default settings for _match\_mode_ (exact) and _search\_mode_ (first to last) the formula matches the first record where:

_account begins with "x" AND region is "east", and month is NOT April._

The first match is the fourth record (row 8) in the example shown.

Explanation 
------------

Normally, the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 is configured to look for a value in a lookup array that exists on the worksheet. However, when the criteria used to match a value becomes more complex, you can use Boolean logic to create a lookup array on the fly composed only of 1s and 0s, then look for the value 1. This is the approach used in this example:

    =XLOOKUP(1,boolean_array,result_array)
    

In this example, the required criteria is:

_account begins with "x" AND region is "east", and month is NOT April._

For each of the three separate criteria above, we use a separate logical expression. The first expression uses the [LEFT function](https://exceljet.net/functions/left-function)
 to test if the Account begins with "x":

    LEFT(B5:B16)="x" // account begins with "x"
    

Because we are checking 12 values, the result is an [array](https://exceljet.net/glossary/array)
 with 12 TRUE FALSE values like this:

    {TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

The second expression tests if Region is "east" using the equal to (=) [operator](https://exceljet.net/glossary/logical-operators)
:

    C5:C16="east" // region is east
    

As before, we get another array with twelve TRUE FALSE values:

    {FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE}
    

The third expression needs to exclude the month of April. The easiest way to do this is to test for the month of April directly with the [MONTH function](https://exceljet.net/functions/month-function)
:

    MONTH(D5:D16)=4 // month is April
    

Then use the [NOT function](https://exceljet.net/functions/not-function)
 to reverse the result:

    NOT(MONTH(D5:D16)=4) // month is not April
    

which creates an array correctly describing "not April":

    {FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}
    

Next, all three arrays are multiplied together, and the math operation coerces the TRUE and FALSE values to 1s and 0s:

    {1;0;1;1;1;0;0;0;1;1;0;1}*
    {0;0;1;1;1;0;1;0;0;1;0;1}*
    {0;0;0;1;1;1;1;1;1;1;1;1}
    

In Boolean arithmetic, [multiplication works like the logical function AND](https://exceljet.net/videos/boolean-algebra-in-excel)
, so the final result is a single array like this:

    {0;0;0;1;1;0;0;0;0;1;0;1}
    

The formula can now be rewritten like this:

    =XLOOKUP(1,{0;0;0;1;1;0;0;0;0;1;0;1},B5:E16)
    

With 1 as a lookup value, and default settings for _match\_mode_ (exact) and _search\_mode_ (first to last), XLOOKUP matches the first 1 (fourth position) and returns the corresponding row in the result array, which is B8:E8.

### Last match

By setting the optional search mode argument to -1, you can locate the "last match" with the same criteria like this:

    =XLOOKUP(1,(LEFT(B5:B16)="x")*(C5:C16="east")*NOT(MONTH(D5:D16)=4),B5:E16,,,-1)
    

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: XLOOKUP with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_with_multiple_criteria.png "Excel formula: XLOOKUP with multiple criteria")](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

### [XLOOKUP with multiple criteria](https://exceljet.net/formulas/xlookup-with-multiple-criteria)

In this example, the goal is to look up a price using XLOOKUP with multiple criteria. To be more specific, we want to look up a price based on Item, Size, and Color. At a glance, this seems like a difficult problem because XLOOKUP only has one value for lookup\_value and lookup\_array . How can we...

[![Excel formula: XLOOKUP basic exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20exact%20match_0.png "Excel formula: XLOOKUP basic exact match")](https://exceljet.net/formulas/xlookup-basic-exact-match)

### [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)

In the example shown, cell G4 contains the lookup value, "Berlin". XLOOKUP is configured to find this value in the table, and return the population. The formula in G5 is: =XLOOKUP(G4,B5:B18,D5:D18) // get population The lookup\_value comes from cell G4 The lookup\_array is the range B5:B18, which...

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: XLOOKUP latest by date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20latest%20by%20date.png "Excel formula: XLOOKUP latest by date")](https://exceljet.net/formulas/xlookup-latest-by-date)

### [XLOOKUP latest by date](https://exceljet.net/formulas/xlookup-latest-by-date)

XLOOKUP offers several features that make it exceptionally good for more complicated lookups. In this example, we want the latest price for an item by date . If data were sorted by date in ascending order, this would be very straightforward . However, in this case, data is unsorted . By default,...

[![Excel formula: FILTER with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20complex%20multiple%20criteria.png "Excel formula: FILTER with complex multiple criteria")](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

### [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

In this example, we need to construct logic that filters data to include: account begins with "x" AND region is "east", and month is NOT April. The filtering logic of this formula (the include argument) is created by chaining together three expressions that use boolean logic on arrays in the data...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

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
    
*   [XLOOKUP basic exact match](https://exceljet.net/formulas/xlookup-basic-exact-match)
    
*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [XLOOKUP latest by date](https://exceljet.net/formulas/xlookup-latest-by-date)
    
*   [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

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