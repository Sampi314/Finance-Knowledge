# Filter text contains - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-text-contains

---

[Skip to main content](https://exceljet.net/formulas/filter-text-contains#main-content)

[](https://exceljet.net/formulas/filter-text-contains#)

*   [Previous](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria)
    
*   [Next](https://exceljet.net/formulas/filter-this-or-that)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter text contains
====================

by Dave Bruns · Updated 13 Feb 2023

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEARCH](https://exceljet.net/functions/search-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")

Summary
-------

To filter data to include data based on a "contains specific text" logic, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with help from the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 and [SEARCH function](https://exceljet.net/functions/search-function)
. In the example shown, the formula in F5 is:

    =FILTER(B5:D14,ISNUMBER(SEARCH("rd",B5:B14)),"No results")
    

Which retrieves data where the street column contains "rd".

Generic formula
---------------

    =FILTER(rng1,ISNUMBER(SEARCH("txt",rng2)))

Explanation 
------------

This formula relies on the [FILTER function](https://exceljet.net/functions/filter-function)
 to retrieve data based on a logical test. The _array_ argument is provided as B5:D14, which contains the full set of data without headers. The _include_ argument is based on a [logical test](https://exceljet.net/formulas/cell-contains-specific-text)
 based on the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 and [SEARCH](https://exceljet.net/functions/search-function)
 functions:

    ISNUMBER(SEARCH("rd",B5:B14))
    

In brief, the [SEARCH function](https://exceljet.net/functions/search-function)
 is set up to look for the text "rd" inside the street data in B5:B14. Because this range includes 10 cells, 10 results are returned. Each result is either a number (text found) or a #VALUE error (text not found):

    {#VALUE!;11;#VALUE!;#VALUE!;13;#VALUE!;#VALUE!;18;17;#VALUE!}
    

This array is delivered to the ISNUMBER function, which converts the result from SEARCH into an array that contains only TRUE or FALSE:

    {FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;TRUE;FALSE}
    

The array from ISNUMBER is provided to the FILTER function as the _include_ argument, and FILTER uses this array to retrieve matching data. Only rows where the result is TRUE make it into the final output. The _if\_empty_ argument is set to "No results" in case no matching data is found.

### Wildcards

The SEARCH function supports [wildcards](https://exceljet.net/glossary/wildcard)
, so the filter logic can include these characters.

### Case-sensitive

For a partial match, case-sensitive filter, you can adjust the formula to use the [FIND function](https://exceljet.net/functions/find-function)
 instead of SEARCH like this:

    =FILTER(rng1,ISNUMBER(FIND("TXT",rng2)))
    

_Note: FIND is case-sensitive, but does not support wildcards._

Related formulas
----------------

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: FILTER with partial match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20partial%20match.png "Excel formula: FILTER with partial match")](https://exceljet.net/formulas/filter-with-partial-match)

### [FILTER with partial match](https://exceljet.net/formulas/filter-with-partial-match)

In this example, the goal is to extract a set of records that match a partial text string . To keep things simple, we are only matching one field in the data, the last name ("Last"). The core operation of this formula comes from the FILTER function (new in Excel 365 ) which extracts matching data...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

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
    
*   [FILTER with partial match](https://exceljet.net/formulas/filter-with-partial-match)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    

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