# Sum first n rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-first-n-rows

---

[Skip to main content](https://exceljet.net/formulas/sum-first-n-rows#main-content)

[](https://exceljet.net/formulas/sum-first-n-rows#)

*   [Previous](https://exceljet.net/formulas/sum-first-n-matching-values)
    
*   [Next](https://exceljet.net/formulas/sum-formulas-only)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum first n rows
================

by Dave Bruns · Updated 2 Jan 2023

Related functions 
------------------

[TAKE](https://exceljet.net/functions/take-function)

[SUM](https://exceljet.net/functions/sum-function)

[OFFSET](https://exceljet.net/functions/offset-function)

![Excel formula: Sum first n rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_first_n_rows.png "Excel formula: Sum first n rows")

Summary
-------

To sum the first n rows of values in a range, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 with the [TAKE function](https://exceljet.net/functions/take-function)
. In the example shown, the formula in G6 is:

    =SUM(TAKE(C5:C16,E5))
    

The result is 5,775, the sum of the first six values in the range C5:C16.

_Note: The [TAKE function](https://exceljet.net/functions/take-function)
 is new in Excel. See below for a formula that will work in older versions of Excel._

Generic formula
---------------

    =SUM(TAKE(range,n))

Explanation 
------------

In the example shown, we have a list of amounts by month. The goal is to dynamically sum values through a given number of months using a variable **n** in cell E5. Since month names are just text, and months are listed in order, the key requirement is to sum amounts _by_ __position__, starting with cell C5. In other words, we want to sum the first **n** values starting at cell C5. In the latest version of Excel, the best way to solve this problem is with the [TAKE function](https://exceljet.net/functions/take-function)
, a new [dynamic array function](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 in Excel. In older versions of Excel, you can use the [OFFSET function](https://exceljet.net/functions/offset-function)
. Both approaches are explained below.

### TAKE function

The TAKE function returns a subset of a given [array](https://exceljet.net/glossary/array)
. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. For example, you can use TAKE to return the first 3 rows or columns of an array like this:

    =TAKE(array,3) // first 3 rows
    =TAKE(array,,3) // first 3 columns

In this problem, the values we want to sum are in the range C5:C16, and the number of rows to return is a variable entered in cell E5. To return the first n values from C5:C16, we use TAKE like this:

    =TAKE(C5:C16,E5)

In this configuration, TAKE will return an array with six values like this:

    {900;850;925;975;1050;1075}

To sum these values, we [nest](https://exceljet.net/glossary/nesting)
 the TAKE function inside the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(TAKE(C5:C16,E5))
    =SUM({900;850;925;975;1050;1075})
    =5775

The result is 5,775, the sum of the first six values in the range C5:C16.

### OFFSET function

In older versions of Excel that do not have the TAKE function, you can use the [OFFSET function](https://exceljet.net/functions/offset-function)
 to solve this problem. OFFSET is designed to create a reference to a range constructed using five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. To sum the first 6 values in C5:C16, we can use the OFFSET function with the SUM function like this:

    =SUM(OFFSET(C5,0,0,E5))

Inside OFFSET, we use C5 for _reference_, since we want to start at C5. Next, we provide 0 for _rows_ and 0 for _cols_ since we don't want a row offset or a column offset. Finally, we provide E5 for _height_, since this cell contains the number of rows to include in the sum. We don't need to provide a value for the optional _width_ argument, since width will be automatically inherited from _reference_. In this configuration, OFFSET will return a reference to C5:C10. The formula will evaluate like this:

    =SUM(OFFSET(C5,0,0,E5))
    =SUM(C5:C10)
    =SUM({900;850;925;975;1050;1075})
    =5775

The final result is 5,775, the sum of the first six values in the range C5:C16.

Related formulas
----------------

[![Excel formula: Sum last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_rows.png "Excel formula: Sum last n rows")](https://exceljet.net/formulas/sum-last-n-rows)

### [Sum last n rows](https://exceljet.net/formulas/sum-last-n-rows)

In the example shown, we have a list of amounts in column C. The goal is to dynamically sum the last n amounts using the number that appears in cell E5 for n . Since the list may grow over time, the key requirement is to sum amounts by position. For convenience only, the values to sum are in the...

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

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum last n rows](https://exceljet.net/formulas/sum-last-n-rows)
    
*   [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)
    
*   [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Sum top n values with criteria](https://exceljet.net/formulas/sum-top-n-values-with-criteria)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    

### Functions

*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    

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