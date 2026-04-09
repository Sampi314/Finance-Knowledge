# Look up entire row - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/look-up-entire-row

---

[Skip to main content](https://exceljet.net/formulas/look-up-entire-row#main-content)

[](https://exceljet.net/formulas/look-up-entire-row#)

*   [Previous](https://exceljet.net/formulas/look-up-entire-column)
    
*   [Next](https://exceljet.net/formulas/lookup-and-sum-column)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Look up entire row
==================

by Dave Bruns · Updated 29 Apr 2022

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Look up entire row](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/look%20up%20entire%20row.png "Excel formula: Look up entire row")

Summary
-------

To look up and retrieve an entire row, you can use a formula based on the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. In the example shown, the formula in cell I5  is:

    =XLOOKUP(H5,project,data)
    

where **project** (B5:B16) and **data** (C5:F16) are [named ranges](https://exceljet.net/glossary/named-range)
. With a lookup value of "Neptune" in cell H5, the result is all four quarterly values for the Neptune project, which [spill](https://exceljet.net/glossary/spill)
 into the range I5:L5.

_Note: this problem can also be solved with INDEX and MATCH, as described below._

Generic formula
---------------

    =XLOOKUP(value,column,data)

Explanation 
------------

In this example, the goal is to look up and retrieve an entire row of values in a set of data. For example, when a value like "Neptune" is entered into cell H5, all values in the range C11:F11 should be returned. For convenience and readability, **project** (B5:B16) and **data** (C5:F16) are [named ranges](https://exceljet.net/glossary/named-range)
.

Although this example shows off the simplicity of the XLOOKUP function, it can also be solved with a straightforward INDEX and MATCH formula, as described below. It can also be solved with the FILTER function.

### With XLOOKUP

With the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, the solution is simple. In the example shown, the formula in I5 is:

    =XLOOKUP(H5,project,data)
    

Here, _lookup\_value_ is H5 (which contains "Neptune"), _lookup\_array_ is **project** (B5:B16), and  _return\_array_ is **data** (C5:F16). In this configuration, XLOOKUP matches the 7th value in B5:B16, and returns the 7th column in C5:F16. In the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the 4 values in C11:F11 [spill](https://exceljet.net/glossary/spill)
 into the range I5:L5. If the value in H5 is changed to a different project, the formula will immediately recalculate and return a new column of values.

### With FILTER

The [FILTER function](https://exceljet.net/functions/filter-function)
 is designed to return multiple matching rows from a set of data, but it will work fine in this case as well. The syntax looks like this:

    =FILTER(data,project=H5)
    

The result is the same as with the XLOOKUP formula, since there is only one project named "Neptune". However, if there were multiple rows with Neptune as the project, FILTER would return data for all of these rows. See [this page](https://exceljet.net/functions/filter-function)
 for more details and examples.

### With INDEX and MATCH

This problem can also be solved with an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
 like this:

    =INDEX(data,MATCH(P5,project,0),0)
    

The gist of the solution is that the [MATCH function](https://exceljet.net/functions/match-function)
 is used to identify the correct row number in **project**, and the [INDEX function](https://exceljet.net/functions/index-function)
 retrieves the entire row in **data** when  _column\_num_ is set to zero(0). Working from the inside out, MATCH is used to get the row index like this:

    MATCH(P5,project,0) // returns 7
    

With "Neptune" in H5, the MATCH function returns 7, since "Neptune" is the seventh value in **project** (B5:B16). MATCH returns this result directly to the INDEX function as the _row\_num_ argument, with _array_ given as **data**, and _column\_num_ set to 0:

    =INDEX(data,7,0)
    

This causes INDEX to return all 4 values in the seventh column of **data** as a final result. In the [dynamic array version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, these results will [spill](https://exceljet.net/glossary/spill)
 into the range I5:L5. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, the values won't spill automatically and you will need to enter this formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
.

### Processing with other functions

Often, the purpose of looking up and retrieving an entire row of values is to feed those values into another function like SUM, MAX, MIN, AVERAGE, etc. To do this, simply [nest](https://exceljet.net/glossary/nesting)
 the formula above inside the other function. For example,  you can get the sum, max, and average for Project Neptune like this:

    =SUM(XLOOKUP(H5,project,data)) // get sum
    =MAX(XLOOKUP(H5,project,data)) // get max
    =AVERAGE(XLOOKUP(H5,project,data)) // get average
    

In each formula, the XLOOKUP returns all 4 values in the row to the outer function, which returns a single result. If the project in H5 is changed, the formula recalculates, and a new result is returned. The INDEX and MATCH and FILTER versions of the formula can be nested in the same way.

Related formulas
----------------

[![Excel formula: Look up entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20column.png "Excel formula: Look up entire column")](https://exceljet.net/formulas/look-up-entire-column)

### [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)

In this example, the goal is to look up and retrieve an entire column of values in a set of data. For example, when a value like "Q3" is entered into cell H4, all values in the range E5:E16 should be returned. For convenience and readability, quarter (C4:F4) and data (C5:F16) are named ranges ...

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

*   [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)
    
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