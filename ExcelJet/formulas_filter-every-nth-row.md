# Filter every nth row - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-every-nth-row

---

[Skip to main content](https://exceljet.net/formulas/filter-every-nth-row#main-content)

[](https://exceljet.net/formulas/filter-every-nth-row#)

*   [Previous](https://exceljet.net/formulas/filter-data-between-dates)
    
*   [Next](https://exceljet.net/formulas/filter-exclude-blank-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter every nth row
====================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[MOD](https://exceljet.net/functions/mod-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Filter every nth row](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20every%20nth%20row.png "Excel formula: Filter every nth row")

Summary
-------

To filter and extract every nth row, you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
 together with [MOD](https://exceljet.net/functions/mod-function)
, [ROW](https://exceljet.net/functions/row-function)
, and [SEQUENCE](https://exceljet.net/functions/sequence-function)
. In the example shown, the formula in F5 is:

    =FILTER(data,MOD(SEQUENCE(ROWS(data)),3)=0)
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 D5:D16. With **n** hardcoded into the formula as 3, FILTER function returns every 3rd row in the data.

Generic formula
---------------

    =FILTER(rng,MOD(SEQUENCE(ROWS(rng)),n)=0)

Explanation 
------------

The [FILTER function](https://exceljet.net/functions/filter-function)
 is designed to filter and extract information based on logical criteria. In this example, the goal is to extract every 3rd record from the data shown, but there is no row number information in the data.

Working from the inside out, the first step is to generate a set of row numbers. This is done with the SEQUENCE function like this:

    SEQUENCE(ROWS(data))
    

The ROW function returns the count of rows in the [named range](https://exceljet.net/glossary/named-range)
 **data.** Using the count of rows, SEQUENCE returns an [array](https://exceljet.net/glossary/array)
 of 12 numbers in sequence:

    {1;2;3;4;5;6;7;8;9;10;11;12}
    

This array is returned directly to the [MOD function](https://exceljet.net/functions/mod-function)
 as the _number_ argument, with the number 3 hardcoded as the _divisor_. MOD is set up to test if row numbers are divisible by 3 with a remainder of zero

    MOD(SEQUENCE(ROWS(data)),3)=0 // divisible by 3?
    

The result from MOD is an array or TRUE and FALSE values like this:

    {FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE}
    

Note TRUE values correspond with every 3rd row in the data. This array is delivered directly to the FILTER function as the _include_ argument. FILTER returns every 3rd row in data as a final result.

Related formulas
----------------

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter exclude blank values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20exclude%20blank%20values.png "Excel formula: Filter exclude blank values")](https://exceljet.net/formulas/filter-exclude-blank-values)

### [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)

The FILTER function is designed to extract data that matches one or more criteria. In this case, we want to apply criteria that requires all three columns in the source data (Name, Group, and Room) to have data. In other words, if a row is missing any of these values, we want to exclude that row...

[![Excel formula: Name of nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value.png "Excel formula: Name of nth largest value")](https://exceljet.net/formulas/name-of-nth-largest-value)

### [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)

In a nutshell, this formula uses the LARGE function to find the nth largest value in a set of data. Once we have that value, we plug it into a standard INDEX and MATCH formula to retrieve the associated name. In other words, we use the nth largest value like a "key" to retrieve associated...

[![Excel formula: FILTER on top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values.png "Excel formula: FILTER on top n values")](https://exceljet.net/formulas/filter-on-top-n-values)

### [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE function. The LARGE function is a simple way to get the nth largest value in a range. Simply provide a range for the first argument ( array ), and a value for n as the second argument ( k ): =...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)
    
*   [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)
    
*   [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

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