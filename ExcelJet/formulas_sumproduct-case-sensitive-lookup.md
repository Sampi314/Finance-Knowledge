# SUMPRODUCT case-sensitive lookup - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sumproduct-case-sensitive-lookup

---

[Skip to main content](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup#main-content)

[](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup#)

*   [Previous](https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table)
    
*   [Next](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)
    

[Lookup](https://exceljet.net/formulas#Lookup)

SUMPRODUCT case-sensitive lookup
================================

by Dave Bruns · Updated 3 Nov 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[EXACT](https://exceljet.net/functions/exact-function)

![Excel formula: SUMPRODUCT case-sensitive lookup](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/SUMPRODUCT_case_sensitive_lookup.png "Excel formula: SUMPRODUCT case-sensitive lookup")

Summary
-------

To perform a case-sensitive lookup with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
. In the example, the formula in G5, copied down, is:

    =SUMPRODUCT(--EXACT(F5,data[Color]),data[Qty])
    

Where "data" is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D15. The result is the quantity associated with "Red" (5), excluding "RED". In cell G6, the same formula copied down returns 9, matching "RED". Note that if there is more than one match (i.e. exact match duplicate colors), SUMPRODUCT will _sum_ matching results.

_Note: While this is an [array formula](https://exceljet.net/glossary/array-formula)
, it does not need to be entered with Control + Shift + Enter in older versions of Excel, since [SUMPRODUCT handles arrays natively](https://exceljet.net/articles/why-sumproduct)
. In modern versions of Excel that support [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, there is no advantage to using SUMPRODUCT to solve a problem like this. Instead, switch to [XLOOKUP](https://exceljet.net/formulas/xlookup-case-sensitive)
 or [INDEX and MATCH](https://exceljet.net/formulas/index-and-match-case-sensitive)
._

Generic formula
---------------

    =SUMPRODUCT(--(EXACT(val,lookup_col)),result_col)

Explanation 
------------

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 multiplies [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. If only one array is supplied, SUMPRODUCT will simply sum the items in the array. For example, if we give SUMPRODUCT one array in the form of the data\[Qty\] column:

    =SUMPRODUCT(data[Qty]) // returns 54
    

SUMPRODUCT returns 54, the total of all numbers in the Qty column, like this:

    =SUMPRODUCT(data[Qty])
    =SUMPRODUCT({9;6;4;8;5;1;7;5;4;2;3})
    =54
    

What we need now is a way to "filter" these values to include only the value associated with "Red", respecting case. In other words, we need to test the values in the Color column and only allow those associated with "Red" to make it through. We can do this with the [EXACT function](https://exceljet.net/functions/exact-function)
, which is designed to perform a case-sensitive comparison of text strings. We use EXACT like this:

    --EXACT(F5,data[Color])
    

Because we are comparing the in value in F5 ("Red") with the eleven values in the Color column, the EXACT function returns 11 results in an array like this:

    {FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Next, we use a [double negative](https://exceljet.net/glossary/double-unary)
 (--) in front of EXACT to convert the TRUE and FALSE values to 1s and 0s. The resulting array looks like this:

    {0;0;0;0;1;0;0;0;0;0;0}
    

Notice the 1 in the 5th position corresponds to the "Red" in row 5. Every other value is now a zero. This will work perfectly as a filter. Turning back to the formula in G5, we can see how this works. The formula is evaluated like this:

    =SUMPRODUCT(--EXACT(F5,data[Color]),data[Qty])
    =SUMPRODUCT({0;0;0;0;1;0;0;0;0;0;0},{9;6;4;8;5;1;7;5;4;2;3})
    =SUMPRODUCT({0;0;0;0;5;0;0;0;0;0;0})
    =5
    

Each array is evaluated, the two arrays are multiplied together, and SUMPRODUCT returns the sum of the products. The FALSE values created with the EXACT function become zeros, and the zeros effectively cancel out the other values when the two arrays are multiplied together. The only values that survive are those associated with TRUE, and the final result is 5.

_Remember, this formula only works for numeric values, because SUMPRODUCT doesn't handle text._

### Case-sensitive sum

Note that because we are using SUMPRODUCT, this formula comes with a unique twist: if there are _multiple_ matches, SUMPRODUCT will return the _sum_ of those matches. For example, the value in cell F6 is "RED", which appears twice in the Color column. The formula in G6 returns 9 like this:

    =SUMPRODUCT(--EXACT(F6,data[Color]),data[Qty])
    =SUMPRODUCT({0;0;1;0;0;0;0;1;0;0;0}*{9;6;4;8;5;1;7;5;4;2;3})
    =SUMPRODUCT({0;0;4;0;0;0;0;5;0;0;0}) // returns 9
    

The value "RED" appears in row 3 and row 8 of the table, and the final sum is 9.

### Compact syntax

In more advanced SUMPRODUCT formulas, you will often see an abbreviated syntax like this:

    =SUMPRODUCT(EXACT(F6,data[Color])*data[Qty])
    

Notice we are now providing just one array to SUMPRODUCT, which is a result of multiplying the two arrays together directly. The advantage of this approach is that we no longer need to use the double negative. The math operation of multiplying the arrays together automatically coerces the TRUE and FALSE values in the first array into 1s and 0s.

Related formulas
----------------

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: VLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20case%20sensitive.png "Excel formula: VLOOKUP case-sensitive ")](https://exceljet.net/formulas/vlookup-case-sensitive)

### [VLOOKUP case-sensitive](https://exceljet.net/formulas/vlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on Color with VLOOKUP. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". This presents several challenges. First, Excel is not case-sensitive by default, and there is no built-in...

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

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
    
*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

### Training

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