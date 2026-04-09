# FILTER on first or last n values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-on-first-or-last-n-values

---

[Skip to main content](https://exceljet.net/formulas/filter-on-first-or-last-n-values#main-content)

[](https://exceljet.net/formulas/filter-on-first-or-last-n-values#)

*   [Previous](https://exceljet.net/formulas/filter-last-n-valid-entries)
    
*   [Next](https://exceljet.net/formulas/filter-on-top-n-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER on first or last n values
================================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: FILTER on first or last n values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/FILTER%20on%20first%20or%20last%20n%20values.png "Excel formula: FILTER on first or last n values")

Summary
-------

To FILTER and extract the _first_ or _last_ **n** values, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with [INDEX](https://exceljet.net/functions/index-function)
 and [SEQUENCE](https://exceljet.net/functions/sequence-function)
. In the example shown, the formula in D5 is:

    =INDEX(FILTER(data,data<>""),SEQUENCE(3,1,1,1))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15 and **n** is 3.

Generic formula
---------------

    =INDEX(FILTER(data,data<>""),SEQUENCE(n,1,1,1))

Explanation 
------------

In this example, the goal is to extract the first 3 values or the last 3 values from the named range **data** (B5:B15). We also want to exclude any empty cells from our results. In the worksheet shown the formula in cell D5 is:

    =INDEX(FILTER(data,data<>""),SEQUENCE(3,1,1,1))
    

Working from the inside out, we use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 to construct a row number value for INDEX like this:

    SEQUENCE(3,1,1,1)
    

We are asking SEQUENCE for an array of 3 rows x 1 column, starting at 1, with a step value of 1. The result is an array like this:

    {1;2;3}
    

which is returned directly to the [INDEX function](https://exceljet.net/functions/index-function)
 as the _row\_num_ argument:

    =INDEX(FILTER(data,data<>""),{1;2;3})
    

To construct the array for INDEX, we use the [FILTER function](https://exceljet.net/functions/filter-function)
 to retrieve a list of non-blank entries from the named range **data** (B5:B15) like this:

    FILTER(data,data<>"")
    

The _array_ argument is data, and the _include_ argument is the expression data<>"". This can be translated literally as "return values from the named range **data** where values in **data** are not empty". The result is an [array](https://exceljet.net/glossary/array)
 with 9 values like this:

    {"Atlanta";"Chicago";"Dallas";"Denver";"Los Angeles";"Miami";"New York";"Seattle";"Minneapolis"}
    

Notice values associated with the two empty cells have been removed. This array is returned to the INDEX function as its _array_ argument.

Finally, INDEX returns the 1st, 2nd, and 3rd values from the array returned by FILTER:

    {"Atlanta";"Chicago";"Dallas"}
    

### Last n values

To get the last n values with FILTER, you use the same formula structure, with the inputs to SEQUENCE modified to construct a "last n" array of row numbers. For example, to get the last 3 non-blank values in the example shown, you can use a formula like this:

    =INDEX(FILTER(data,data<>""),SORT(SEQUENCE(3,1,SUM(--(data<>"")),-1)))
    

The main trick here is counting the non-blank entries in the named range **data** like this:

    SUM(--(data<>""))
    

We use a [double-negative](https://exceljet.net/glossary/double-unary)
 to force the TRUE FALSE values to 1s and 0s, then use the [SUM function](https://exceljet.net/functions/sum-function)
 to get the count. The result is returned as the _start_ argument inside SEQUENCE. We supply -1 for _step_ to step backwards from _start_.

We also wrap the [SORT function](https://exceljet.net/functions/sort-function)
 around SEQUENCE so the array returned is {7;8;9} and not {9;8;7}. This ensures that values are returned in the same order they appear in the source data.

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

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

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
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

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