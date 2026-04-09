# Max value with variable column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/max-value-with-variable-column

---

[Skip to main content](https://exceljet.net/formulas/max-value-with-variable-column#main-content)

[](https://exceljet.net/formulas/max-value-with-variable-column#)

*   [Previous](https://exceljet.net/formulas/max-value-on-given-weekday)
    
*   [Next](https://exceljet.net/formulas/maximum-change)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Max value with variable column
==============================

by Dave Bruns · Updated 2 Aug 2022

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[MAX](https://exceljet.net/functions/max-function)

[FILTER](https://exceljet.net/functions/filter-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/5755/download?token=zib07HpT)
 (10.78 KB)

![Excel formula: Max value with variable column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/max%20value%20with%20variable%20column.png "Excel formula: Max value with variable column")

Summary
-------

To retrieve the max value in a set of data, where the column is _variable_, you can use [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 together with the [MAX function](https://exceljet.net/functions/max-function)
. In the example shown the formula in J5 is:

    =MAX(INDEX(data,0,MATCH(J4,header,0)))
    

where **data** (B5:F15) and **header** (B4:F4) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =MAX(INDEX(data,0,MATCH(column,header,0)))

Explanation 
------------

Note: If you are new to INDEX and MATCH, see: [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)

In a standard configuration, the INDEX function retrieves a value at a given row and column. For example, to get the value at row 2 and column 3 in a given range:

    =INDEX(range,2,3) // get value at row 2, column 3
    

However, [INDEX](https://exceljet.net/functions/index-function)
 has a special trick – the ability to retrieve _entire_ columns and rows. The syntax involves supplying zero for the "other" argument. If you want an entire column, you supply _row_ as zero. If you want an entire row, you supply _column_ as zero:

    =INDEX(data,0,n) // retrieve column n
    =INDEX(data,n,0) // retrieve row n
    

In the example shown, we want to find the maximum value in a given column. The twist is that the column needs to be variable so it can be easily changed. In F5, the formula is:

    =MAX(INDEX(data,0,MATCH(J4,header,0)))
    

Working from the inside out, we first use the [MATCH function](https://exceljet.net/functions/match-function)
 to get the "index" of the column requested in cell J4:

    MATCH(J4,header,0) // get column index
    

With "Green" in J4, the MATCH function returns 3, since Green is the third value in the [named range](https://exceljet.net/glossary/named-range)
 **header**. After MATCH returns a result, the formula can be simplified to this:

    =MAX(INDEX(data,0,3))
    

With zero provided as the _row\_number_, INDEX returns all values in column 3 of the named range **data.** The result is returned to the [MAX function](https://exceljet.net/functions/max-function)
 in an [array](https://exceljet.net/glossary/array)
 like this:

    =MAX({83;54;35;17;85;16;70;72;65;93;91})
    

And MAX returns the final result, 93.

### Minimum value

To get the _minimum_ value with a variable column, you can simply replace the MAX function with the MIN function. The formula in J6 is:

    =MIN(INDEX(data,0,MATCH(J4,header,0)))
    

### With FILTER

The new [FILTER function](https://exceljet.net/functions/filter-function)
 can also be used to solve this problem, since FILTER can filter data by row or by column. The trick is to construct a logical filter that will exclude other columns. [COUNTIF](https://exceljet.net/functions/countif-function)
 works well in this case, but it must be configured "backwards", with J4 as the _range_, and **header** for _criteria_:

    =MAX(FILTER(data,COUNTIF(J4,header)))
    

After COUNTIF runs, we have:

    =MAX(FILTER(data,{0,0,1,0,0}))
    

And FILTER delivers the 3rd column to MAX, same as the INDEX function above.

As an alternative to COUNTIF, you can use ISNUMBER + MATCH instead:

    =MAX(FILTER(data,ISNUMBER(MATCH(header,J4,0))))
    

The MATCH function is again set up "backwards", so that we get an array with 5 values that will serve as the logical filter. After ISNUMBER and MATCH run, we have:

    =MAX(FILTER(data,{FALSE,FALSE,TRUE,FALSE,FALSE}))
    

And FILTER again delivers the 3rd column to MAX.

Related formulas
----------------

[![Excel formula: Look up entire row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20row.png "Excel formula: Look up entire row")](https://exceljet.net/formulas/look-up-entire-row)

### [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)

In this example, the goal is to look up and retrieve an entire row of values in a set of data. For example, when a value like "Neptune" is entered into cell H5, all values in the range C11:F11 should be returned. For convenience and readability, project (B5:B16) and data (C5:F16) are named ranges...

[![Excel formula: Sum entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20entire%20column.png "Excel formula: Sum entire column")](https://exceljet.net/formulas/sum-entire-column)

### [Sum entire column](https://exceljet.net/formulas/sum-entire-column)

In this example, the goal is to return the total for an entire column in an Excel worksheet. One way to do this is to use a full column reference. Full column references Excel supports " full column " like this: =SUM(A:A) // sum all of column A =SUM(C:C) // sum all of column C =SUM(A:C) // sum all...

[![Excel formula: Look up entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20column.png "Excel formula: Look up entire column")](https://exceljet.net/formulas/look-up-entire-column)

### [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)

In this example, the goal is to look up and retrieve an entire column of values in a set of data. For example, when a value like "Q3" is entered into cell H4, all values in the range E5:E16 should be returned. For convenience and readability, quarter (C4:F4) and data (C5:F16) are named ranges ...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

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
    
*   [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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