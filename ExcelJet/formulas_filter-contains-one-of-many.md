# Filter contains one of many - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-contains-one-of-many

---

[Skip to main content](https://exceljet.net/formulas/filter-contains-one-of-many#main-content)

[](https://exceljet.net/formulas/filter-contains-one-of-many#)

*   [Previous](https://exceljet.net/formulas/filter-case-sensitive)
    
*   [Next](https://exceljet.net/formulas/filter-data-between-dates)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter contains one of many
===========================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Filter contains one of many](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20contains%20one%20of%20many_0.png "Excel formula: Filter contains one of many")

Summary
-------

To filter data to include only records where a column is equal to one of many values, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 and [MATCH function](https://exceljet.net/functions/match-function)
. In the example shown, the formula in F5 is:

    =FILTER(data,ISNUMBER(MATCH(color,list,0)),"No data")
    

where **data** (B5:D15), **color** (C5:C15), and **list** (J5:J7) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =FILTER(data,ISNUMBER(MATCH(rng1,rng2,0)),"No data")

Explanation 
------------

The [FILTER function](https://exceljet.net/functions/filter-function)
 can filter data using a logical expression provided as the _include_ argument. In this example, this argument is created with an expression that uses the ISNUMBER and MATCH functions like this:

    =ISNUMBER(MATCH(color,list,0))
    

MATCH is configured to look for each color in C5:C15 inside the smaller range J5:J7. The MATCH function returns an array like this:

    {1;#N/A;#N/A;#N/A;2;3;2;#N/A;#N/A;#N/A;3}
    

Notice numbers correspond to the position of "found" colors (either "red", "blue", or "black"), and errors correspond to rows where a target color was not found. To force a result of TRUE or FALSE, this array goes into the ISNUMBER function, which returns:

    {TRUE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;TRUE}
    

The array above is delivered to the FILTER function as the _include_ argument, and FILTER returns only rows that correspond to a TRUE value.

### With hardcoded values

The example above is created with cell references, where target colors are entered in the range J5:J7. However, by using an [array constant](https://exceljet.net/glossary/array-constant)
, you can hardcode values into the formula like this with the same result:

    =FILTER(data,ISNUMBER(MATCH(color,{"red","blue","black"},0)),"No data")
    

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

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