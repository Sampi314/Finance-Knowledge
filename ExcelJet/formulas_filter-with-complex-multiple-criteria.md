# FILTER with complex multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-with-complex-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/filter-with-complex-multiple-criteria#main-content)

[](https://exceljet.net/formulas/filter-with-complex-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/filter-values-within-tolerance)
    
*   [Next](https://exceljet.net/formulas/filter-with-multiple-criteria)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER with complex multiple criteria
=====================================

by Dave Bruns · Updated 13 Feb 2023

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[LEFT](https://exceljet.net/functions/left-function)

[MONTH](https://exceljet.net/functions/month-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: FILTER with complex multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20with%20complex%20multiple%20criteria.png "Excel formula: FILTER with complex multiple criteria")

Summary
-------

To filter and extract data based on multiple complex criteria, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with a chain of expressions that use boolean logic. In the example shown, the formula in G5 is:

    =FILTER(B5:E16,(LEFT(B5:B16)="x")*(C5:C16="east")*NOT(MONTH(D5:D16)=4))
    

This formula returns data where:

_account begins with "x" AND region is "east", and month is NOT April._

Explanation 
------------

In this example, we need to construct logic that filters data to include:

_account begins with "x" AND region is "east", and month is NOT April._

The filtering logic of this formula (the _include_ argument) is created by chaining together three expressions that use [boolean logic](https://exceljet.net/glossary/boolean-logic)
 on arrays in the data. The first expression uses the [LEFT function](https://exceljet.net/functions/left-function)
 to test if Account begins with "x":

    LEFT(B5:B16)="x" // account begins with "x"
    

The result is an [array](https://exceljet.net/glossary/array)
 of TRUE FALSE values like this:

    {TRUE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE}
    

The second expression tests if Region is "east" with the equal to (=) [operator](https://exceljet.net/glossary/logical-operators)
:

    C5:C16="east" // region is east
    

The result is another array:

    {FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE}
    

The third expression uses the [MONTH function](https://exceljet.net/functions/month-function)
 with the [NOT function](https://exceljet.net/functions/not-function)
 to test if the month is _not_ April:

    NOT(MONTH(D5:D16)=4) // month is not april
    

which yields:

    {FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}
    

Note that the NOT function _reverses_ the result from the MONTH expression.

All three arrays are multiplied together. The math operation coerces the TRUE and FALSE values to 1s and 0s, so at this point we can visualize the _include_ argument like this:

    {1;0;1;1;1;0;0;0;1;1;0;1}*
    {0;0;1;1;1;0;1;0;0;1;0;1}*
    {0;0;0;1;1;1;1;1;1;1;1;1}
    

Boolean multiplication corresponds to the logical function AND, so the final result is a single array like this:

    {0;0;0;1;1;0;0;0;0;1;0;1}
    

The FILTER function uses this array to filter the data, and returns the four rows that correspond with the 1s in the array.

### Extending criteria

The expressions used to create the _include_ argument in filter can be extended as needed to handle even more complex filters. For example, to further filter data to include only rows where amount > 10000, you could use a formula like this:

    =FILTER(B5:E16,(LEFT(B5:B16)="x")*(C5:C16="east")*NOT(MONTH(D5:D16)=4)*(E5:E16>10000))
    

Related formulas
----------------

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: FILTER with multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20multiple%20or%20criteria.png "Excel formula: FILTER with multiple OR criteria")](https://exceljet.net/formulas/filter-with-multiple-or-criteria)

### [FILTER with multiple OR criteria](https://exceljet.net/formulas/filter-with-multiple-or-criteria)

In this example, criteria are entered in the range F5:H6. The logic of the formula is: item is (tshirt OR hoodie) AND color is (red OR blue) AND city is (denver OR seattle) The filtering logic of this formula (the include argument) is applied with the ISNUMBER and MATCH functions, together with...

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

*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [FILTER with multiple OR criteria](https://exceljet.net/formulas/filter-with-multiple-or-criteria)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

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