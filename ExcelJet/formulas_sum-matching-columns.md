# Sum matching columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-matching-columns

---

[Skip to main content](https://exceljet.net/formulas/sum-matching-columns#main-content)

[](https://exceljet.net/formulas/sum-matching-columns#)

*   [Previous](https://exceljet.net/formulas/sum-last-n-rows)
    
*   [Next](https://exceljet.net/formulas/sum-matching-columns-and-rows)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum matching columns
====================

by Dave Bruns · Updated 18 Jan 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[LEFT](https://exceljet.net/functions/left-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Sum matching columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20matching%20columns.png "Excel formula: Sum matching columns")

Summary
-------

To sum values in columns by matching column headers, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in J5 is:

    =SUMPRODUCT(data*(LEFT(headers)=J4))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:G14, and **headers** is the named range B4:G4. The formula sums columns where headers begin with "A" and returns 201.

_Note: In the current version of Excel you can also use the [FILTER function](https://exceljet.net/functions/filter-function)
, as explained below._

Generic formula
---------------

    =SUMPRODUCT(data*(headers=A1))

Explanation 
------------

At the core, this formula relies on the SUMPRODUCT function to sum values in matching columns in the named range **data** C5:G14. If all data were provided to SUMPRODUCT in a single range, the result would be the sum of all values in the range:

    =SUMPRODUCT(data) // all data, returns 387
    

To apply a filter by matching column headers – columns with headers that begin with "A" – we use the LEFT function like this:

    LEFT(headers)=J4) // must begin with "a"
    

This expression returns TRUE if a column header begins with "a", and FALSE if not. The result is an array:

    {TRUE,TRUE,FALSE,FALSE,TRUE,FALSE}
    

You can see that values 1,2, and 5 correspond to columns that begin with "a".

Inside SUMPRODUCT, this array is multiplied by "data". Due to [broadcasting](https://exceljet.net/glossary/broadcasting)
, the result is a two-dimensional array like this:

    {8,10,0,0,7,0;9,10,0,0,10,0;8,6,0,0,6,0;7,6,0,0,6,0;8,6,0,0,6,0;10,11,0,0,7,0;7,8,0,0,8,0;2,3,0,0,3,0;3,4,0,0,4,0;7,7,0,0,4,0}
    

If we visualize this array in a table, it's easy to see that only values in columns that begin with "a" have survived the operation, all other columns are zero. In other words, the filter keeps values of interest and "cancels out" the rest:

| A001 | A002 | B001 | B002 | A003 | B003 |
| --- | --- | --- | --- | --- | --- |
| 8   | 10  | 0   | 0   | 7   | 0   |
| 9   | 10  | 0   | 0   | 10  | 0   |
| 8   | 6   | 0   | 0   | 6   | 0   |
| 7   | 6   | 0   | 0   | 6   | 0   |
| 8   | 6   | 0   | 0   | 6   | 0   |
| 10  | 11  | 0   | 0   | 7   | 0   |
| 7   | 8   | 0   | 0   | 8   | 0   |
| 2   | 3   | 0   | 0   | 3   | 0   |
| 3   | 4   | 0   | 0   | 4   | 0   |
| 7   | 7   | 0   | 0   | 4   | 0   |

With only a single array to process, SUMPRODUCT returns the sum of all values, 201.

### Sum by exact match

The example above shows how to sum columns that begin with one or more specific characters. To sum column based on an _exact match_, you can use a simpler formula like this:

    =SUMPRODUCT(data*(headers=J4))
    

### FILTER function

In the latest version of Excel, you can solve this problem more directly with the FILTER function like this:

    =SUM(FILTER(data,LEFT(headers)=J4,0))

In this formula, we use the same logic we used in the SUMPRODUCT function to select only data in columns that begin with the letter "A":

    LEFT(headers)=J4 // columns that begin with "A"

The expression above returns an array of TRUE and FALSE values like this:

    {TRUE,TRUE,FALSE,FALSE,TRUE,FALSE}

Notice that the TRUE values correspond to column headers that begin with "A". The FILTER function uses this array to select columns in the named range **data**. Because this [array is horizontal](https://exceljet.net/glossary/array)
, FILTER [automatically filters on columns](https://exceljet.net/formulas/filter-horizontal-data)
. The FILTER function returns the 3 columns in **data** with headers that begin with "A" to the SUM function, which returns a final result of 201.

Video: [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

Related formulas
----------------

[![Excel formula: Sum matching columns and rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_matching_columns_and_rows.png "Excel formula: Sum matching columns and rows")](https://exceljet.net/formulas/sum-matching-columns-and-rows)

### [Sum matching columns and rows](https://exceljet.net/formulas/sum-matching-columns-and-rows)

In this example, the goal is to sum values in matching columns and rows. Specifically, we want to sum values in data (C5:G14) where the column code is "A" and the day is "Wed". One way to solve this problem is with the SUMPRODUCT function , which can handle array operations natively, without...

[![Excel formula: Sum every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20nth%20column.png "Excel formula: Sum every nth column")](https://exceljet.net/formulas/sum-every-nth-column)

### [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)

In this example, the goal is to sum every nth value by column in a range of data, as seen in the worksheet above. For example, if n =2, we want to sum every second value by column, if n =3, we want to sum every third value by column, and so on. All data is in the range B5:J16 and n is entered into...

[![Excel formula: Get relative column numbers in range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20relative%20column%20numbers%20in%20range.png "Excel formula: Get relative column numbers in range")](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

### [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)

The first COLUMN function generates an array of 7 numbers like this: {2,3,4,5,6,7,8} The second COLUMN function generates an array with just one item like this: {2} which is then subtracted from the first array to yield: {0,1,2,3,4,5,6} Finally, 1 is added to get: {1,2,3,4,5,6,7} With a named range...

[![Excel formula: Sum columns based on adjacent criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20columns%20based%20on%20adjacent%20criteria.png "Excel formula: Sum columns based on adjacent criteria")](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)

### [Sum columns based on adjacent criteria](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)

In this example, the goal is to sum the values in columns C, E, G, and I conditionally using the text values in columns B, D, F, and H for criteria. This problem can be solved with the SUMPRODUCT function , which is designed to multiply ranges or arrays together and return the sum of products. The...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum matching columns and rows](https://exceljet.net/formulas/sum-matching-columns-and-rows)
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Get relative column numbers in range](https://exceljet.net/formulas/get-relative-column-numbers-in-range)
    
*   [Sum columns based on adjacent criteria](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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