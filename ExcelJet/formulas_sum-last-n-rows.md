# Sum last n rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-last-n-rows

---

[Skip to main content](https://exceljet.net/formulas/sum-last-n-rows#main-content)

[](https://exceljet.net/formulas/sum-last-n-rows#)

*   [Previous](https://exceljet.net/formulas/sum-last-n-columns)
    
*   [Next](https://exceljet.net/formulas/sum-matching-columns)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum last n rows
===============

by Dave Bruns · Updated 17 Mar 2025

Related functions 
------------------

[TAKE](https://exceljet.net/functions/take-function)

[SUM](https://exceljet.net/functions/sum-function)

[TRIMRANGE](https://exceljet.net/functions/trimrange-function)

[OFFSET](https://exceljet.net/functions/offset-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Sum last n rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_last_n_rows.png "Excel formula: Sum last n rows")

Summary
-------

To sum the last **n** rows of values in a range, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 with the [TAKE function](https://exceljet.net/functions/take-function)
. In the example shown, the formula in F5 is:

    =SUM(TAKE(data,-E5))
    

Where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C16. The result is 7,300, the sum of the last 6 values.

> The [TAKE function](https://exceljet.net/functions/take-function)
>  is new in Excel. See below for a formula that will work in older versions.

Generic formula
---------------

    =SUM(TAKE(range,-n))

Explanation 
------------

In the example shown, we have a list of amounts in column C. The goal is to dynamically sum the last **n** amounts using the number that appears in cell E5 for **n**. Since the list may grow over time, the key requirement is to sum amounts _by position._ For convenience only, the values to sum are in the [named range](https://exceljet.net/glossary/named-range)
 **data** (C5:C16). In the latest version of Excel, the best way to solve this problem is with the [TAKE function](https://exceljet.net/functions/take-function)
, a new [dynamic array function](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 in Excel. In older versions of Excel, you can use the [OFFSET function](https://exceljet.net/functions/offset-function)
. Both approaches are explained below.

### TAKE function

The TAKE function returns a subset of a given [array](https://exceljet.net/glossary/array)
. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. For example, you can use TAKE to return the _first_ 3 rows or columns of an array like this:

    =TAKE(array,3) // first 3 rows
    =TAKE(array,,3) // first 3 columns

A great feature of TAKE is that you can supply a negative value to retrieve _last_ rows or columns:

    =TAKE(array,-3) // last 3 rows
    =TAKE(array,,-3) // last 3 columns

In this problem, we want to sum the last **n** values that appear in **data**, where the number of rows to return is a variable entered in cell E5. To retrieve these values, we can use TAKE like this:

    TAKE(data,-E5)

With the number 6 in cell E5, TAKE will return an array with six values like this:

    {1050;1150;1250;1175;1350;1325}

To sum these values, we simply need to [nest](https://exceljet.net/glossary/nesting)
 the TAKE function inside the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM(TAKE(data,-E5))
    =SUM({1050;1150;1250;1175;1350;1325})
    =7300

The result is 7,300, the sum of the last six values in the range C5:C16. As new values are added to **data**, TAKE will continue to return the last **n** values to SUM.

### Making the range dynamic

One limitation of the formula explained above is that it assumes that the range going into the TAKE function contains all data. What should you do if new data is being added on an ongoing basis? One easy solution is to use the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
 to create a simple dynamic range like this:

    =SUM(TRIMRANGE(TAKE(range,-n)))

The TRIMRANGE function removes empty rows and columns from a range of data. The result is a "trimmed" range that only includes data from the used portion of the range. Because it is a formula, TRIMRANGE will update the range dynamically when data is added or removed from the original range. To make this work correctly, you will want to use a range that is largest enough to hold all possible data. For example, if the data is in column A, you can use a full-column reference like this:

    =SUM(TRIMRANGE(TAKE(A:A,-n)))

With TRIMRANGE in the formula, TAKE will always get the latest data. You can read more about the TRIMRANGE function [here](https://exceljet.net/functions/trimrange-function)
.

### OFFSET function

In older versions of Excel that do not have the TAKE function, you can use the [OFFSET function](https://exceljet.net/functions/offset-function)
 to solve this problem. OFFSET is designed to create a reference for a range using five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. To sum the last 6 values in **data** (C5:C16), we can use the OFFSET function with the SUM function like this:

    =SUM(OFFSET(C5,COUNT(data)-E5,0,E5))

Inside OFFSET, we use C5 for _reference_, since we want to start at C5. For _rows_, _we_ use this snippet:

    COUNT(data)-E5 // rows offset

Our goal is to create a range that starts at the cell in **data** that is **n** cells before last cell. The COUNT function returns the number of numeric values in data. We subtract E5 to "back up" to the correct cell. For _cols_, we provide 0 since we don't want a column offset. We provide E5 for _height_, since we want our final range to be **n** cells tall. We don't need to provide a value for the optional _width_ argument, since _width_ will inherit from _reference_. In this configuration, OFFSET will return a reference to C11:C16, which contains the last 6 values in **data**. The formula will evaluate like this:

    =SUM(OFFSET(C5,COUNT(data)-E5,0,E5))
    =SUM(OFFSET(C5,12-6,0,6))
    =SUM(C11:C16)
    =SUM({1050;1150;1250;1175;1350;1325})
    =7300

The final result is 7300, the sum of the last six values in the range C5:C16.

### INDEX function

One thing you might notice about the OFFSET formula above is that we are providing a reference to both **data** and cell C5, the first cell in **data**. This makes the formula more error-prone since **data** and C5 are disconnected. You can make the formula more robust and portable by using the [INDEX function](https://exceljet.net/functions/index-function)
 to return the first cell in **data** like this:

    =SUM(OFFSET(INDEX(data,1),COUNT(data)-E5,0,E5))

This works because the INDEX function returns C5 as a _reference_, not a _value_. Now, as long as the reference to **data** is correct, the formula will work properly.

### Making the range dynamic

One limitation of the formulas above is that they won't automatically include new data added to the range. In an older version of Excel, one way to make the range expand to include new data is to create a dynamic named range with a formula. You can create a dynamic named range [with the OFFSET function](https://exceljet.net/formulas/dynamic-named-range-with-offset)
 or [with the INDEX function](https://exceljet.net/formulas/dynamic-named-range-with-index)
. Another (simpler) option is to [use an Excel Table](https://exceljet.net/articles/excel-tables)
 to create the range.

Related formulas
----------------

[![Excel formula: Sum first n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_first_n_rows.png "Excel formula: Sum first n rows")](https://exceljet.net/formulas/sum-first-n-rows)

### [Sum first n rows](https://exceljet.net/formulas/sum-first-n-rows)

In the example shown, we have a list of amounts by month. The goal is to dynamically sum values through a given number of months using a variable n in cell E5. Since month names are just text, and months are listed in order, the key requirement is to sum amounts by position , starting with cell C5...

[![Excel formula: Sum last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_columns.png "Excel formula: Sum last n columns")](https://exceljet.net/formulas/sum-last-n-columns)

### [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)

In this example, the goal is to sum the last n columns in a set of data, where n is a variable that can be changed at any time. In the latest version of Excel, the easiest way to solve this problem is with the TAKE function . In older versions of Excel you can use the OFFSET function , as explained...

[![Excel formula: Average last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_5_columns.png "Excel formula: Average last n columns")](https://exceljet.net/formulas/average-last-n-columns)

### [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)

In this example, the goal is to average the last n columns in a set of data, where n is a variable entered in cell K5 that can be changed at any time. Since more data may be added, a key requirement is to average amounts by position. For convenience, the values to average are in the named range...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Sum top n values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20top%20n%20values%20with%20criteria.png "Excel formula: Sum top n values with criteria")](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

### [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)

In this example, the goal is to sum the largest n values in a set of data after applying specific criteria. In the worksheet shown, we want to sum the three largest values, so n is equal to 3. At a high level, this problem breaks down into three separate steps: Apply criteria to select specific...

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

Related functions
-----------------

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel TRIMRANGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_trimrange_function.png "Excel TRIMRANGE function")](https://exceljet.net/functions/trimrange-function)

### [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)

The Excel TRIMRANGE function removes empty rows and columns from the outer edges of a range of data. The result is a "trimmed" range that only includes data from the used portion of the range. Because it is a formula, TRIMRANGE will update the range dynamically when data is added or removed...

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

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

*   [Sum first n rows](https://exceljet.net/formulas/sum-first-n-rows)
    
*   [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)
    
*   [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    

### Functions

*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)
    
*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

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