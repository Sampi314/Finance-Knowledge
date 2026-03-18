# Filter this or that - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-this-or-that

---

[Skip to main content](https://exceljet.net/formulas/filter-this-or-that#main-content)

[](https://exceljet.net/formulas/filter-this-or-that#)

*   [Previous](https://exceljet.net/formulas/filter-text-contains)
    
*   [Next](https://exceljet.net/formulas/filter-to-extract-matching-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter this or that
===================

by Dave Bruns · Updated 13 Feb 2023

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")

Summary
-------

To filter data to include only records where a value is this or that, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 and simple [boolean logic](https://exceljet.net/glossary/boolean-logic)
 expressions. In the example shown, the formula in F5 is:

    =FILTER(B5:D14,(D5:D14="red")+(D5:D14="blue"),"No results")
    

The result returned by FILTER includes only rows where group is "red" or "blue".

Generic formula
---------------

    =FILTER(rng1,(rng2="red")+(rng2="blue"),"No results")

Explanation 
------------

This formula relies on the [FILTER function](https://exceljet.net/functions/filter-function)
 to retrieve data based on a logical test built with simple expressions and [boolean logic](https://exceljet.net/glossary/boolean-logic)
:

    (D5:D14="red")+(D5:D14="blue")
    

After each expression is evaluated, we have the following two [arrays](https://exceljet.net/glossary/array)
:

    ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE})+
    ({FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE})
    

The math operation (addition) coerces TRUE and FALSE values to 1s and 0s:

    =({1;0;0;0;0;0;1;0;0;0})+({0;1;0;0;1;0;0;1;0;0})
    

The result is a single array like this:

    ={1;1;0;0;1;0;1;1;0;0}
    

This final array is delivered to the FILTER function as the _include_ argument, and FILTER returns only rows that correspond to a 1. Or, to put it another way, FILTER removes rows that are zero.

### Not mutually exclusive

In the example above, we are testing for two possible values in a _single_ column of data. This means that the two tests are mutually exclusive — both tests can't return TRUE at the same time. However, if you are testing _multiple_ columns/fields for values, there is the possibility that more than one logical test will return TRUE. In that case, the final array may contain numbers larger than 1 (i.e. TRUE + TRUE = 2). [This makes a difference in some formulas](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)
. However, in this case, it doesn't matter, because FILTER will treat any non-zero value as TRUE when evaluating the _include_ argument.

Video: [Boolean algebra in Excel formulas](https://exceljet.net/videos/boolean-algebra-in-excel)

Related formulas
----------------

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: XLOOKUP with Boolean OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20boolean%20OR%20logic.png "Excel formula: XLOOKUP with Boolean OR logic")](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)

### [XLOOKUP with Boolean OR logic](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)

In this example, the goal is to use XLOOKUP to find the first "red" or "pink" record in the data as shown. All data is in an Excel Table named data in the range B5:E14. This means the formulas below use structured references . As a result, the formulas will automatically include new data added to...

[![Excel formula: FILTER with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20complex%20multiple%20criteria.png "Excel formula: FILTER with complex multiple criteria")](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

### [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

In this example, we need to construct logic that filters data to include: account begins with "x" AND region is "east", and month is NOT April. The filtering logic of this formula (the include argument) is created by chaining together three expressions that use boolean logic on arrays in the data...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

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
    
*   [XLOOKUP with Boolean OR logic](https://exceljet.net/formulas/xlookup-with-boolean-or-logic)
    
*   [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    

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