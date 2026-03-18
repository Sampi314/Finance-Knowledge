# FILTER with partial match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-with-partial-match

---

[Skip to main content](https://exceljet.net/formulas/filter-with-partial-match#main-content)

[](https://exceljet.net/formulas/filter-with-partial-match#)

*   [Previous](https://exceljet.net/formulas/filter-with-multiple-or-criteria)
    
*   [Next](https://exceljet.net/formulas/generate-random-text-strings)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER with partial match
=========================

by Dave Bruns · Updated 5 Apr 2023

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEARCH](https://exceljet.net/functions/search-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6659/download?token=QYs1AJTK)
 (20.23 KB)

![Excel formula: FILTER with partial match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20with%20partial%20match.png "Excel formula: FILTER with partial match")

Summary
-------

To use select records from a set of data based on a partial match, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [SEARCH function](https://exceljet.net/functions/search-function)
. In the example shown, the formula in G7 is:

    =FILTER(Table1,ISNUMBER(SEARCH(H4,Table1[Last]))*(H4<>""),"No results")
    

where **Table1** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 that contains 100 rows of data in B5:E104.

Generic formula
---------------

    =FILTER(range,ISNUMBER(SEARCH(text,range)))

Explanation 
------------

In this example, the goal is to extract a set of records that match a partial [text string](https://exceljet.net/glossary/text-value)
. To keep things simple, we are only matching one field in the data, the last name ("Last"). The core operation of this formula comes from the [FILTER function](https://exceljet.net/functions/filter-function)
 (new in [Excel 365](https://exceljet.net/glossary/excel-365)
) which extracts matching data from a range based on a logical filter:

    =FILTER(data,logic)
    

The challenge in this example is to construct the logic needed to match records based on a partial match. The FILTER function does not support [wildcards](https://exceljet.net/glossary/wildcard)
, so we need to use a different approach. In this case, we are using the [SEARCH function](https://exceljet.net/functions/search-function)
 together with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 like this:

    ISNUMBER(SEARCH(H4,Table1[Last])) // partial match logic
    

Here, the SEARCH function is configured to look for text entered in cell H4, inside the "Last" column in the table. If SEARCH finds a result, it returns the position of that result in the text. For example:

    =SEARCH("cat","The cat in the hat") // returns 5
    

If SEARCH doesn't find anything, it returns the #VALUE! error:

    =SEARCH("dog","The cat in the hat") // returns #VALUE!
    

In other words, if SEARCH returns a number, we have a match. If not, we don't have a match. To convert this result into a simple TRUE/FALSE value, we wrap the SEARCH function inside the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. ISNUMBER will return TRUE only when SEARCH has returned a number:

    =ISNUMBER(SEARCH("cat","The cat in the hat")) // returns TRUE
    =ISNUMBER(SEARCH("dog","The cat in the hat")) // returns FALSE
    

Notice we are not using a wildcard like ("\*") to get a partial match, but the SEARCH + ISNUMBER combo behaves like a partial match nonetheless. If the search string is found anywhere in the text, SEARCH will return a number and ISNUMBER will return TRUE.

Getting back to the example shown, we are using SEARCH and ISNUMBER like this:

    ISNUMBER(SEARCH(H4,Table1[Last])) // partial match logic
    

Because the table contains 100 rows, the snippet above will generate 100 TRUE/FALSE results, one for each cell in the Last column. This is exactly what we need for the FILTER function – a TRUE or FALSE value for each row in the data. When the snippet above is embedded in FILTER as the include argument, FILTER returns the matching rows:

    =FILTER(Table1,ISNUMBER(SEARCH(H4,Table1[Last]))
    

We now have a working formula but need to tidy up a few things. First, if the FILTER function does not return any match, it will return a #CALC! error. To provide a more friendly message, we add a text message for the _if\_empty_ [argument](https://exceljet.net/glossary/function-argument)
:

    =FILTER(Table1,ISNUMBER(SEARCH(H4,Table1[Last])),"No results")
    

Now if the search text isn't found, FILTER will return "No results".

Finally, we need to handle the case of the search text in H4 being empty. Somewhat oddly, the SEARCH function will return the number 1 if the search text is an empty string:

    =ISNUMBER(SEARCH("","The cat in the hat")) // returns 1
    

This will cause FILTER to return all results if cell H4 is empty, since ISNUMBER will happily return TRUE for number 1. To prevent this behavior, we tack on a bit of logic to the original logical expression:

    ISNUMBER(SEARCH(H4,Table1[Last]))*(H4<>"")
    

The expression H4<>"" returns TRUE only when H4 is not empty, and FALSE when H4 is empty. When we multiply the results of this expression by the original SEARCH + ISNUMBER expression, it will "cancel out" all TRUE results when H4 is empty. This is a form of [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. The math operation of [multiplication (\*) works like AND logic in array formulas](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
.

### Partial match with INDEX and MATCH

The FILTER function is available only in Excel 365. In older versions of Excel, it is possible to set up a partial match formula to return more than one match, but it is more complicated. [This formula shows one approach based on INDEX and MATCH](https://exceljet.net/formulas/index-and-match-all-partial-matches)
.

Related formulas
----------------

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Partial match with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Partial%20match%20with%20VLOOKUP.png "Excel formula: Partial match with VLOOKUP")](https://exceljet.net/formulas/partial-match-with-vlookup)

### [Partial match with VLOOKUP](https://exceljet.net/formulas/partial-match-with-vlookup)

In this example, the goal is to retrieve employee information from a table using only a partial match on the last name. In other words, by typing "Aya" into cell H4, the formula should retrieve information about Michael Ayala. The VLOOKUP function supports wildcards , which makes it possible to...

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
    
*   [Partial match with VLOOKUP](https://exceljet.net/formulas/partial-match-with-vlookup)
    

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