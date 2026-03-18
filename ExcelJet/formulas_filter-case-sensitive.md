# FILTER case-sensitive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/filter-case-sensitive#main-content)

[](https://exceljet.net/formulas/filter-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/filter-by-date)
    
*   [Next](https://exceljet.net/formulas/filter-contains-one-of-many)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER case-sensitive
=====================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEARCH](https://exceljet.net/functions/search-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: FILTER case-sensitive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20case%20sensitive.png "Excel formula: FILTER case-sensitive")

Summary
-------

To filter data in case-sensitive way, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with help from the [EXACT function](https://exceljet.net/functions/exact-function)
. In the example shown, the formula in F5 is:

    =FILTER(B5:D15,EXACT(B5:B15,"RED"))
    

Which extracts data where color is "RED", respecting upper and lower case.

Generic formula
---------------

    =FILTER(data,EXACT(range,A1))

Explanation 
------------

This formula relies on the FILTER function to retrieve data based on a [logical test](https://exceljet.net/glossary/logical-test)
. The _array_ [argument](https://exceljet.net/glossary/function-argument)
 is provided as B5:D15, which contains all of the data without headers. The _include_ argument is an expression based on the EXACT function:

    EXACT(B5:B15,"RED")
    

The EXACT function compares two text strings in a case-sensitive manner. If the two strings are exactly the same, EXACT returns TRUE. If the two strings are not exactly the same, EXACT returns FALSE. Since we are giving EXACT a range with 11 values as the first argument, and the string "RED" as the second, EXACT returns an [array](https://exceljet.net/glossary/array)
 with 11 results like this:

    {FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE}
    

Notice the position of TRUE values in this array corresponds to the rows where the color is "RED".

This array returned directly to the FILTER function as the _include_ argument. FILTER uses the array to filter the range B5:D15, and returns the three rows where the color is "RED". Rows where the color is "Red" are not included.

### Partial match

To run an exact match with FILTER based on a partial match, see [the example explained here](https://exceljet.net/formulas/filter-text-contains)
.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: XLOOKUP case-sensitive ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/xlookup%20case%20sensitive.png "Excel formula: XLOOKUP case-sensitive ")](https://exceljet.net/formulas/xlookup-case-sensitive)

### [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)

In this example, the goal is to perform a case-sensitive lookup on the color in the "Color" column. In other words, a lookup value of "RED" must return a different result from a lookup value of "Red". By default, Excel is not case-sensitive and this applies to standard lookup formulas like VLOOKUP...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [XLOOKUP case-sensitive](https://exceljet.net/formulas/xlookup-case-sensitive)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

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