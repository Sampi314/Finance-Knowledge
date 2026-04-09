# Find lowest n values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/find-lowest-n-values

---

[Skip to main content](https://exceljet.net/formulas/find-lowest-n-values#main-content)

[](https://exceljet.net/formulas/find-lowest-n-values#)

*   [Previous](https://exceljet.net/formulas/cap-percentage-between-0-and-100)
    
*   [Next](https://exceljet.net/formulas/first-in-last-out-times)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Find lowest n values
====================

by Dave Bruns · Updated 30 Apr 2023

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Find lowest n values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Find%20lowest%20n%20values.png "Excel formula: Find lowest n values")

Summary
-------

To find the n lowest values in a set of data, you can use the [SMALL function](https://exceljet.net/functions/small-function)
. This can be combined with [INDEX](https://exceljet.net/functions/index-function)
 as shown below to retrieve associated values. In the example shown, the formula in F7 is:

    =SMALL(bid,E7)
    

_Note: this worksheet has two [named ranges](https://exceljet.net/glossary/named-range)
: **bid** (C5:C12), and **company** (B5:B12), used for convenience and readability only._

Generic formula
---------------

    =SMALL(range,n)

Explanation 
------------

The [SMALL function](https://exceljet.net/functions/small-function)
 retrieves the smallest values from data based on a given rank. For example:

    =SMALL(range,1) // smallest
    =SMALL(range,2) // 2nd smallest
    =SMALL(range,3) // 3rd smallest
    

In the worksheet shown, the rank (which is provided to SMALL as the _k_ argument) comes from numbers in column E.

### Retrieve associated values

To retrieve the _name_ of the company associated with the smallest bids, we can use an [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
. In the worksheet shown, the formula in G7 is:

    =INDEX(company,MATCH(F7,bid,0))
    

Here, the value in column F is used as the lookup value inside MATCH, with the [named range](https://exceljet.net/glossary/named-range)
 **bid** (C5:C12) for _lookup\_array_, and _match\_type_ set to zero to force an exact match. MATCH returns the location of the value to INDEX as the row number. INDEX then retrieves the corresponding value from the named range **company** (B5:B12). An all-in-one formula to get the company name in one step would look like this:

    =INDEX(company,MATCH(SMALL(bid,E7),bid,0))
    

_Note: if your values contain duplicates you may get ties when you try to rank. You can [use a formula like this](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)
 to break times._

### FILTER option

The [FILTER function](https://exceljet.net/functions/filter-function)
 provides a better way to retrieve the top or bottom n values from a set of data. [See this page](https://exceljet.net/formulas/filter-on-top-n-values)
 for an example.

Related formulas
----------------

[![Excel formula: nth smallest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value.png "Excel formula: nth smallest value")](https://exceljet.net/formulas/nth-smallest-value)

### [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)

In this example, the goal is to extract the 3 best race times for each name from the 5 race times that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the fastest time, the 2nd fastest time, and the 3rd fastest time. This problem can be solved with the SMALL...

[![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")](https://exceljet.net/formulas/nth-largest-value)

### [nth largest value](https://exceljet.net/formulas/nth-largest-value)

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function. Note...

[![Excel formula: Sum bottom n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values.png "Excel formula: Sum bottom n values")](https://exceljet.net/formulas/sum-bottom-n-values)

### [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)

In this example, the goal is to sum the smallest n values in a set of data, where n is a variable that can be easily changed. At a high level, the solution breaks down into two steps (1) extract the n smallest values from the data set and (2) sum the extracted values. This problem can be solved...

[![Excel formula: Break ties with helper column and COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/break%20ties%20with%20helper%20column%20and%20COUNTIF.png "Excel formula: Break ties with helper column and COUNTIF")](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)

### [Break ties with helper column and COUNTIF](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)

In this example, the goal is to retrieve information about the lowest three estimates in the data shown. The problem is that there are some duplicate values in the estimate column. This means we will have some trouble trying to display the names of the 2nd and 3rd lowest suppliers because the tie...

Related functions
-----------------

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

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

*   [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)
    
*   [nth largest value](https://exceljet.net/formulas/nth-largest-value)
    
*   [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)
    
*   [Break ties with helper column and COUNTIF](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif)
    

### Functions

*   [SMALL Function](https://exceljet.net/functions/small-function)
    
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