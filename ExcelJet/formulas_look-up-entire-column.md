# Look up entire column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/look-up-entire-column

---

[Skip to main content](https://exceljet.net/formulas/look-up-entire-column#main-content)

[](https://exceljet.net/formulas/look-up-entire-column#)

*   [Previous](https://exceljet.net/formulas/look-up-and-return-to-single-cell)
    
*   [Next](https://exceljet.net/formulas/look-up-entire-row)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Look up entire column
=====================

by Dave Bruns · Updated 6 Dec 2022

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7235/download?token=AVKRWLnB)
 (14.88 KB)

![Excel formula: Look up entire column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/look%20up%20entire%20column.png "Excel formula: Look up entire column")

Summary
-------

To look up and retrieve an entire column, you can use a formula based on the XLOOKUP function. In the example shown, the formula in cell H5  is:

    =XLOOKUP(H4,quarter,data)
    

where **quarter** (C4:F4) and **data** (C5:F16) are [named ranges](https://exceljet.net/glossary/named-range)
. With a lookup value of "Q3" in cell H4, the result is all values associated with Q3, which [spill](https://exceljet.net/glossary/spill)
 into the range H5:H16.

_Note: this problem can also be solved with INDEX and MATCH and FILTER, as described below._

Generic formula
---------------

    =XLOOKUP(value,header,data)

Explanation 
------------

In this example, the goal is to look up and retrieve an entire column of values in a set of data. For example, when a value like "Q3" is entered into cell H4, all values in the range E5:E16 should be returned. For convenience and readability, **quarter** (C4:F4) and **data** (C5:F16) are [named ranges](https://exceljet.net/glossary/named-range)
.

Although this example shows off the simplicity of the XLOOKUP function, it can also be solved with a straightforward INDEX and MATCH formula, as described below.

### With XLOOKUP

With the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, the solution is straightforward. In the example shown, the formula in H5 is:

    =XLOOKUP(H4,quarter,data)
    

Here, _lookup\_value_ is H4 (which contains "Q3"), _lookup\_array_ is **quarter** (C4:F4), and _return\_array_ is **data** (C5:F16). With this configuration, XLOOKUP matches the 3rd value in C4:F4, and returns the third column in C5:F16. In the [dynamic array version of Excel,](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 the 12 values in E5:E16 [spill](https://exceljet.net/glossary/spill)
 into the range H5:H16. If the value in H4 is changed to a different quarter, the formula will immediately recalculate and return a new column of values.

### With FILTER

You might not think of using the [FILTER function](https://exceljet.net/functions/filter-function)
 to filter columns, but it works fine. In this case, the formula to solve this problem is:

    =FILTER(data,quarter=H4)
    

After the _include_ argument is evaluated, we have an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values:

    =FILTER(data,{FALSE,FALSE,TRUE,FALSE})
    

And FILTER returns the third column in **data**. For another example of using FILTER on horizontal data, [see this page](https://exceljet.net/formulas/filter-horizontal-data)
.

### With INDEX and MATCH

This problem can also be solved with an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 like this:

    =INDEX(data,0,MATCH(N4,quarter,0))
    

The gist of the solution is that the [MATCH function](https://exceljet.net/functions/match-function)
 is used to identify the column index, and the [INDEX function](https://exceljet.net/functions/index-function)
 will retrieve the entire column when _row\_num_ is set to zero(0). Working from the inside out, MATCH is used to get the column index like this:

    MATCH(H4,quarter,0) // returns 3
    

With "Q3" in H4, the MATCH function returns 3, since "Q3" is the third value in **quarter** (C4:F4). MATCH returns this result directly to the INDEX function as the _col\_num_ argument, with _array_ set to **data**, and _row\_num_ set to 0:

    =INDEX(data,0,3)
    

This causes INDEX to return all 12 values in the third column of **data** as a final result. In the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, these results will [spill](https://exceljet.net/glossary/spill)
 into the range H5:H16. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, you will need to enter this formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
.

### Processing with other functions

Often, the purpose of looking up and retrieving an entire column of values is to feed those values into another function like SUM, MAX, MIN, AVERAGE, LARGE, etc. This is simply a matter of [nesting](https://exceljet.net/glossary/nesting)
 the lookup formula into another function. For example,  you can get the sum, max, and average for Q3 like this:

    =SUM(XLOOKUP(H4,quarter,data)) // get sum
    =MAX(XLOOKUP(H4,quarter,data)) // get max
    =AVERAGE(XLOOKUP(H4,quarter,data)) // get average
    

In each formula, the XLOOKUP returns all 12 values in the Q3 column to the outer function, which returns a single result. The same approach can be used with the INDEX and MATCH and FILTER versions of the formula.

Related formulas
----------------

[![Excel formula: Look up entire row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20row.png "Excel formula: Look up entire row")](https://exceljet.net/formulas/look-up-entire-row)

### [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)

In this example, the goal is to look up and retrieve an entire row of values in a set of data. For example, when a value like "Neptune" is entered into cell H5, all values in the range C11:F11 should be returned. For convenience and readability, project (B5:B16) and data (C5:F16) are named ranges...

[![Excel formula: Sum entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20entire%20column.png "Excel formula: Sum entire column")](https://exceljet.net/formulas/sum-entire-column)

### [Sum entire column](https://exceljet.net/formulas/sum-entire-column)

In this example, the goal is to return the total for an entire column in an Excel worksheet. One way to do this is to use a full column reference. Full column references Excel supports " full column " like this: =SUM(A:A) // sum all of column A =SUM(C:C) // sum all of column C =SUM(A:C) // sum all...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

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

*   [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)
    
*   [Sum entire column](https://exceljet.net/formulas/sum-entire-column)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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