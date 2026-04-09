# FILTER with multiple OR criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-with-multiple-or-criteria

---

[Skip to main content](https://exceljet.net/formulas/filter-with-multiple-or-criteria#main-content)

[](https://exceljet.net/formulas/filter-with-multiple-or-criteria#)

*   [Previous](https://exceljet.net/formulas/filter-with-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/filter-with-partial-match)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER with multiple OR criteria
================================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: FILTER with multiple OR criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20with%20multiple%20or%20criteria.png "Excel formula: FILTER with multiple OR criteria")

Summary
-------

To extract data with multiple OR conditions, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with the [MATCH function](https://exceljet.net/functions/match-function)
. In the example shown, the formula in F9 is:

    =FILTER(B5:D16,
    ISNUMBER(MATCH(items,F5:F6,0))*
    ISNUMBER(MATCH(colors,G5:G6,0))*
    ISNUMBER(MATCH(cities,H5:H6,0)))
    

where **items** (B3:B16), **colors** (C3:C16), and **cities** (D3:D16) are [named ranges](https://exceljet.net/glossary/named-range)
.

This formula returns data where item is (tshirts OR hoodie) AND color is (red OR blue) AND city is (denver OR seattle).

Explanation 
------------

In this example, criteria are entered in the range F5:H6. The logic of the formula is:

_item is (tshirt OR hoodie) AND color is (red OR blue) AND city is (denver OR seattle)_

The filtering logic of this formula (the _include_ argument) is applied with the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and MATCH functions, together with [boolean logic](https://exceljet.net/glossary/boolean-logic)
 applied in an array operation.

MATCH is configured "backwards", with _lookup\_values_ coming from the data, and criteria used for the _lookup\_array_. For example, the first condition is that items must be either a Tshirt or Hoodie. To apply this condition, MATCH is set up like this:

    MATCH(items,F5:F6,0) // check for tshirt or hoodie
    

Because there are 12 values in the data, the result is an [array](https://exceljet.net/glossary/array)
 with 12 values like this:

    {1;#N/A;#N/A;2;#N/A;2;2;#N/A;1;#N/A;2;1}
    

This array contains either #N/A errors (no match) or numbers (match). Notice numbers correspond to items that are either Tshirt or Hoodie. To convert this array into TRUE and FALSE values, the MATCH function is wrapped in the ISNUMBER function:

    ISNUMBER(MATCH(items,F5:F6,0))
    

which yields an array like this:

    {TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;TRUE}
    

In this array, the TRUE values correspond to tshirt or hoodie.

The full formula contains three expressions like the above used for the _include_ argument of the FILTER function:

    ISNUMBER(MATCH(items,F5:F6,0))* // tshirt or hoodie
    ISNUMBER(MATCH(colors,G5:G6,0))* // red or blue
    ISNUMBER(MATCH(cities,H5:H6,0))) // denver or seattle
    

After MATCH and ISNUMBER are evaluated, we have three arrays containing TRUE and FALSE values. The math operation of multiplying these arrays together coerces the TRUE and FALSE values to 1s and 0s, so we can visualize the arrays at this point like this:

    {1;0;0;1;0;1;1;0;1;0;1;1}*
    {1;0;1;1;0;1;0;0;0;0;0;1}*
    {1;0;1;0;0;1;0;1;1;0;0;1}
    

The result, following the rules of boolean arithmetic, is a single array:

    {1;0;0;0;0;1;0;0;0;0;0;1}
    

which becomes the _include_ argument in the FILTER function:

    =FILTER(B5:D16,{1;0;0;0;0;1;0;0;0;0;0;1})
    

The final result is the three rows of data shown in F9:H11

### With hard-coded values

Although the formula in the example uses criteria entered directly on the worksheet, criteria can be hard-coded as [array constants](https://exceljet.net/glossary/array-constant)
 instead like this:

    =FILTER(B5:D16,
    ISNUMBER(MATCH(items,{"Tshirt";"Hoodie"},0))*
    ISNUMBER(MATCH(colors,{"Red";"Blue"},0))*
    ISNUMBER(MATCH(cities,{"Denver";"Seattle"},0)))
    

Related formulas
----------------

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

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

*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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