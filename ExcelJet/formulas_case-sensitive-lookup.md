# Case sensitive lookup - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/case-sensitive-lookup

---

[Skip to main content](https://exceljet.net/formulas/case-sensitive-lookup#main-content)

[](https://exceljet.net/formulas/case-sensitive-lookup#)

*   [Previous](https://exceljet.net/formulas/smaller-of-two-values)
    
*   [Next](https://exceljet.net/formulas/find-closest-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Case sensitive lookup
=====================

by Dave Bruns · Updated 23 May 2023

Related functions 
------------------

[EXACT](https://exceljet.net/functions/exact-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

![Excel formula: Case sensitive lookup](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/case%20sensitive%20lookup.png "Excel formula: Case sensitive lookup")

Summary
-------

To perform a case-sensitive lookup, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
 with [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. In the example shown, the formula in F5 is:

    =INDEX(C5:C14,MATCH(TRUE,EXACT(E5,B5:B14),0))
    

This formula returns 39, the age of "JILL SMITH" in uppercase. Notice that the first "Jill Smith" in the list has a different case and is ignored.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
._

Generic formula
---------------

    =INDEX(range1,MATCH(TRUE,EXACT(A1,range2),0))

Explanation 
------------

In this example, the goal is to perform a case-sensitive lookup on the name in column B, based on a lookup value entered in cell E5. By default, Excel is _not_ case-sensitive. This means that standard lookup functions like [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, [XLOOKUP](https://exceljet.net/functions/xlookup-function)
, and [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 are also not case-sensitive. These formulas will simply return the _first_ match, ignoring upper and lower case. The classic way to work around this limitation is to build a lookup formula that incorporates the EXACT function, which performs a case-sensitive comparison. In a nutshell, we use the EXACT function to generate an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values, then alter the lookup formula to look for the first TRUE value. The article below explains how to use this approach with INDEX and MATCH, and XLOOKUP.

### EXACT function

The [EXACT function](https://exceljet.net/functions/exact-function)
 compares two text strings in a case-sensitive fashion. If the two strings are exactly the same, taking into account upper and lower case characters, EXACT returns TRUE. Otherwise, EXACT returns FALSE. For example:

    =EXACT("apple","apple") // returns TRUE
    =EXACT("Apple","apple") // returns FALSE
    

If we use the EXACT function on a _range_ of values, we will get back multiple results. For example, if we use EXACT to compare the value in cell E5 with the range B5:B14:

    EXACT(E5,B5:B14)

We get back an [array](https://exceljet.net/glossary/array-formula)
 that contains 10 TRUE and FALSE values like this:

    {FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}

This is because we are checking the name in E5 ("JILL SMITH") against _all 10 names_ in the range B5:B14. Notice the only TRUE value is in the 5th position. This corresponds to cell B9, which contains "JILL SMITH".

### INDEX and MATCH solution

In the worksheet shown, the formula in cell F5 is:

    =INDEX(C5:C14,MATCH(TRUE,EXACT(E5,B5:B14),0))

Working from the inside-out, EXACT is configured to compare the value in E5 against all names in the range B5:B14:

    EXACT(E5,B5:B14) // returns 10 results
    

The EXACT function performs a case-sensitive comparison and returns TRUE or FALSE as a result. Because we are checking the name in E5 ("JILL SMITH") against _all 10 names_ in the range B5:B14, we get back an [array](https://exceljet.net/glossary/array-formula)
 of 10 TRUE and FALSE values like this:

    {FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

This array is returned directly to the MATCH function as the _lookup\_array_:

    MATCH(TRUE,{FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE},0)
    

Notice the _lookup\_value_ given to MATCH is TRUE, and _match\_type_ is set to zero (0) to force an exact match. The _lookup\_array_ is created by the EXACT function. MATCH then returns 5, since the only TRUE in the array is at the fifth position. This result is returned directly to the INDEX function as the row number, so we can simplify the formula to:

    =INDEX(C5:C14,5) // returns 39
    

With a row number of 5, INDEX returns the age in the fifth row (39) as a final result.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in [older versions of Excel](https://exceljet.net/glossary/legacy-excel)
._

### XLOOKUP solution

The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 can be configured to perform a case-sensitive lookup using EXACT in the same way as INDEX and MATCH, but in a more compact formula:

    =XLOOKUP(TRUE,EXACT(J5,B5:B14),C5:C14)
    

Notice the _lookup\_value_ and _lookup\_array_ are configured like the MATCH function above. After EXACT runs, we have the same array of 10 TRUE and FALSE values explained previously:

    =XLOOKUP(TRUE,{FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE},C5:C14)

XLOOKUP returns the 5th item from the range C5:C14 (39) as a final result.

_Note: For a more detailed example of a case-sensitive XLOOKUP formula, [see this page](https://exceljet.net/formulas/xlookup-case-sensitive)
._

Related formulas
----------------

[![Excel formula: Count cells equal to case sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20case%20sensitive.png "Excel formula: Count cells equal to case sensitive")](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

### [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)

In this example, the goal is to count codes in a case-sensitive way. The COUNTIF function and the COUNTIFS function are both good options for counting text values, but neither is case-sensitive, so they can't be used to solve this problem. The solution is to use the EXACT function to compare codes...

[![Excel formula: Compare two strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/compare%20two%20strings.png "Excel formula: Compare two strings")](https://exceljet.net/formulas/compare-two-strings)

### [Compare two strings](https://exceljet.net/formulas/compare-two-strings)

By default, Excel is not case-sensitive. For example, with "APPLE" in A1, and "apple" in A2, the following formula will return TRUE: =A1=A2 // returns TRUE To compare text strings in a case-sensitive way, you can use the EXACT function . The Excel EXACT function compares two text strings, taking...

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

[![Excel formula: FILTER case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20case%20sensitive.png "Excel formula: FILTER case-sensitive")](https://exceljet.net/formulas/filter-case-sensitive)

### [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)

This formula relies on the FILTER function to retrieve data based on a logical test . The array argument is provided as B5:D15, which contains all of the data without headers. The include argument is an expression based on the EXACT function: EXACT(B5:B15,"RED") The EXACT function compares two text...

[![Excel formula: INDEX and MATCH case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/case-sensitive%20INDEX%20and%20MATCH.png "Excel formula: INDEX and MATCH case-sensitive ")](https://exceljet.net/formulas/index-and-match-case-sensitive)

### [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the first name in column B, based on a lookup value in cell F6. By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP , XLOOKUP , and INDEX and MATCH . These formulas will simply return...

[![Excel formula: SUMPRODUCT case-sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT_case_sensitive_lookup.png "Excel formula: SUMPRODUCT case-sensitive lookup")](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

### [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

The SUMPRODUCT function multiplies arrays together and returns the sum of products. If only one array is supplied, SUMPRODUCT will simply sum the items in the array. For example, if we give SUMPRODUCT one array in the form of the data\[Qty\] column: =SUMPRODUCT(data\[Qty\]) // returns 54 SUMPRODUCT...

Related functions
-----------------

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

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

*   [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    
*   [Compare two strings](https://exceljet.net/formulas/compare-two-strings)
    
*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    
*   [FILTER case-sensitive](https://exceljet.net/formulas/filter-case-sensitive)
    
*   [INDEX and MATCH case-sensitive](https://exceljet.net/formulas/index-and-match-case-sensitive)
    
*   [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)
    

### Functions

*   [EXACT Function](https://exceljet.net/functions/exact-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    

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