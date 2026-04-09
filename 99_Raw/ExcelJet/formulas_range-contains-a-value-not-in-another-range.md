# Range contains a value not in another range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/range-contains-a-value-not-in-another-range

---

[Skip to main content](https://exceljet.net/formulas/range-contains-a-value-not-in-another-range#main-content)

[](https://exceljet.net/formulas/range-contains-a-value-not-in-another-range#)

*   [Previous](https://exceljet.net/formulas/multiple-columns-are-equal)
    
*   [Next](https://exceljet.net/formulas/range-contains-numbers)
    

[Range](https://exceljet.net/formulas#Range)

Range contains a value not in another range
===========================================

by Dave Bruns · Updated 29 Jan 2016

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNA](https://exceljet.net/functions/isna-function)

![Excel formula: Range contains a value not in another range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/range%20contains%20a%20value%20not%20in%20another%20range.png "Excel formula: Range contains a value not in another range")

Summary
-------

To test if a range contains any values (i.e. at least one value) not in another range, you can use the SUMPRODUCT function with MATCH and ISNA.

In the example shown, the formula in F6 is:

    =SUMPRODUCT(--(ISNA(MATCH(lista,listb,0))))>0
    

Generic formula
---------------

    =SUMPRODUCT(--(ISNA(MATCH(rngA,rngB,0))))>0

Explanation 
------------

Normally, the MATCH function receives a single lookup value, and returns a single match if any. In this case, however, we are giving MATCH an array for lookup value, so it will return an array of results, one per element in the lookup array. MATCH is configured for "exact match". If a match isn't found, MATCH will return the #N/A error. After match runs, it returns have something like this:

    =SUMPRODUCT(--(ISNA({3;5;6;2;#N/A;4})))>0
    

We take advantage of this by using the ISNA function to test for any #N/A errors.

After ISNA, we have:

    =SUMPRODUCT(--({FALSE;FALSE;FALSE;FALSE;TRUE;FALSE}))>0
    

We use the double negative (double unary) operator to convert TRUE FALSE values to ones and zeros, which gives us this:

    =SUMPRODUCT({0;0;0;0;1;0})>0
    

SUMPRODUCT then sums the elements in the array, and the result is compared to zero for force a TRUE or FALSE result.

Related formulas
----------------

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Range contains one of many values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20values.png "Excel formula: Range contains one of many values")](https://exceljet.net/formulas/range-contains-one-of-many-values)

### [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)

Each item in rng is compared to each item in values and the result is an array of TRUE or FALSE values. The double negative will force the TRUE and FALSE values to 1 and 0 respectively. Since SUMPRODUCT receives just one array, it simply adds up the items in the array and returns the result...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Range contains one of many values](https://exceljet.net/formulas/range-contains-one-of-many-values)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    

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