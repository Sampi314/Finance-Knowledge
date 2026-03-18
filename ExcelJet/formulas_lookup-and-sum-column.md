# Lookup and sum column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/lookup-and-sum-column

---

[Skip to main content](https://exceljet.net/formulas/lookup-and-sum-column#main-content)

[](https://exceljet.net/formulas/lookup-and-sum-column#)

*   [Previous](https://exceljet.net/formulas/look-up-entire-row)
    
*   [Next](https://exceljet.net/formulas/lookup-first-negative-value)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Lookup and sum column
=====================

by Dave Bruns · Updated 10 Sep 2018

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Lookup and sum column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Lookup%20and%20sum%20column.png "Excel formula: Lookup and sum column")

Summary
-------

To lookup and return the sum of a column, you can use the a formula based on the INDEX, MATCH and SUM functions. In the example shown, the formula in I7 is:

    =SUM(INDEX(C5:F11,0,MATCH(I6,C4:F4,0)))
    

Generic formula
---------------

    =SUM(INDEX(data,0,MATCH(val,header,0)))
    

Explanation 
------------

The core of this formula uses the INDEX and MATCH function in a special way to return a full column instead of a single value. Working from the inside out, the MATCH function is used to find the correct column number for the fruit in I6:

    MATCH(I6,C4:F4,0)
    

MATCH return 2 inside the INDEX function as the column\_num argument, where the array is set to the range C5:F11, which includes data for all fruits.

The tricky part of the formula is the row\_num argument, which is set to zero. Setting row to zero causes INDEX to return all values in the matching column in an array like this:

    =SUM({6;12;4;10;0;9;6})
    

The SUM function then returns the sum of all items in the array, 47.

Related formulas
----------------

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Sum range with INDEX](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20range%20with%20INDEX.png "Excel formula: Sum range with INDEX")](https://exceljet.net/formulas/sum-range-with-index)

### [Sum range with INDEX](https://exceljet.net/formulas/sum-range-with-index)

The INDEX function looks up values by position. For example, this formula retrieves the value for Acme sales in Jan: =INDEX(data,1,1) The INDEX function has a special and non-obvious behavior: when the row number argument is supplied as zero or null, INDEX retrieves all values in the column...

[![Excel formula: Return array with INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/return%20array%20with%20INDEX%20function.png "Excel formula: Return array with INDEX function")](https://exceljet.net/formulas/return-array-with-index-function)

### [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)

It is surprisingly tricky to get INDEX to return more than one value to another function. To illustrate, the following formula can be used to return the first three items in the named range "data", when entered as a multi-cell array formula. {=INDEX(data,{1,2,3})} The results can be seen in the...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Sum range with INDEX](https://exceljet.net/formulas/sum-range-with-index)
    
*   [Return array with INDEX function](https://exceljet.net/formulas/return-array-with-index-function)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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