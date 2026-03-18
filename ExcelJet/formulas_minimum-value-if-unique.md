# Minimum value if unique - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/minimum-value-if-unique

---

[Skip to main content](https://exceljet.net/formulas/minimum-value-if-unique#main-content)

[](https://exceljet.net/formulas/minimum-value-if-unique#)

*   [Previous](https://exceljet.net/formulas/map-with-and-and-or-logic)
    
*   [Next](https://exceljet.net/formulas/random-list-of-names)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Minimum value if unique
=======================

by Dave Bruns · Updated 26 Aug 2022

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[MIN](https://exceljet.net/functions/min-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[IF](https://exceljet.net/functions/if-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6203/download?token=LOUwjHON)
 (14.01 KB)

![Excel formula: Minimum value if unique](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/minimum%20value%20if%20unique.png "Excel formula: Minimum value if unique")

Summary
-------

To find the minimum unique value in a set of data, you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 together with the [MIN function](https://exceljet.net/functions/min-function)
. In the example below, the formula in E5 is:

    =MIN(UNIQUE(data,0,1))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B14.

In older versions of Excel, you can use an [array formula](https://exceljet.net/glossary/array-formula)
 based on the MIN, IF, and COUNTIF functions as explained below.

Generic formula
---------------

    =MIN(UNIQUE(range,0,1))

Explanation 
------------

The goal in this example is to return the minimum value that is unique, i.e. the minimum value that occurs only once in the data.

The UNIQUE function, new in [Excel 365](https://exceljet.net/glossary/excel-365)
, will return a unique list of values from a set of data. By default, this is a list of any value that occurs one or more times in the data.

UNIQUE has an optional third argument called _exactly\_once_ that will limit results to values that occur once only in the source data. To enable this feature, the argument needs to be set to TRUE or 1.

Working from the inside out, the UNIQUE function is configured like this:

    UNIQUE(data,0,1)
    

For _array_, we provide the named range **data**. For the _by\_col_ argument, we use zero (0), since we want unique values by rows, not columns. Finally, for _exactly\_once_, we provide 1, since we want only values that occur just once in the source data.

Configured this way, UNIQUE returns the 4 values that appear only once:

    {700;600;500;300} // result from unique
    

This array is returned directly to the MIN function, which returns the minimum value, 300, as the final result:

    =MIN({700;600;500;300}) // returns 300
    

### Array formula with COUNTIF

If you are using a version of Excel without the UNIQUE function, you can find the minimum unique value with an array formula based on the COUNTIF, MIN, and IF functions.

    {=MIN(IF(COUNTIF(data,data)=1,data))}
    

_This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Working from the inside out, the [COUNTIF function](https://exceljet.net/functions/countif-function)
 is used to generate a count of each value in the data like this:

    COUNTIF(data,data) // count all values
    

Because there are 10 values in the named range **data**, COUNTIF returns an array of 10 results:

    {2;1;1;2;1;2;2;2;1;2}
    

This array holds the count of each value. Next we test the array for values equal to 1:

    {2;1;1;2;1;2;2;2;1;2}=1
    

Again, we get an array with 10 results:

    {FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE}
    

Each TRUE value corresponds to a value in the source data that occurs just once. This array is delivered directly to the [IF function](https://exceljet.net/functions/if-function)
, which uses it like a filter. Only values in data associated with TRUE make it into the array returned by IF, all other values are FALSE.

    {FALSE;700;600;FALSE;500;FALSE;FALSE;FALSE;300;FALSE}
    

This array is returned directly to the [MIN function](https://exceljet.net/functions/min-function)
 which automatically ignores logical values and returns the minimum of remaining values, 300, as a final result.

Related formulas
----------------

[![Excel formula: Unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values.png "Excel formula: Unique values")](https://exceljet.net/formulas/unique-values)

### [Unique values](https://exceljet.net/formulas/unique-values)

This example uses the UNIQUE function, which is fully automatic. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. UNIQUE is a dynamic function. If any data in B5:B16 changes, the output from UNIQUE will update immediately...

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Distinct values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/distinct%20values.png "Excel formula: Distinct values")](https://exceljet.net/formulas/distinct-values)

### [Distinct values](https://exceljet.net/formulas/distinct-values)

This example uses the UNIQUE function . With default settings, UNIQUE will output a list of unique values, i.e. values that appear one or more times in the source data. However, UNIQUE has an optional third argument, called occurs\_once that, when set to TRUE, will cause UNIQUE to return only values...

[![Excel formula: Count unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values.png "Excel formula: Count unique values")](https://exceljet.net/formulas/count-unique-values)

### [Count unique values](https://exceljet.net/formulas/count-unique-values)

This example uses the UNIQUE function to extract unique values. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. These are returned directly to the COUNTA function as an array like this: =COUNTA({"red";"amber";"green";"blue";"...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Unique values](https://exceljet.net/formulas/unique-values)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Distinct values](https://exceljet.net/formulas/distinct-values)
    
*   [Count unique values](https://exceljet.net/formulas/count-unique-values)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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