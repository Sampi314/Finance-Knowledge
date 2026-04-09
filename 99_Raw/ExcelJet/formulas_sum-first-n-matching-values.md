# Sum first n matching values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-first-n-matching-values

---

[Skip to main content](https://exceljet.net/formulas/sum-first-n-matching-values#main-content)

[](https://exceljet.net/formulas/sum-first-n-matching-values#)

*   [Previous](https://exceljet.net/formulas/sum-every-nth-row)
    
*   [Next](https://exceljet.net/formulas/sum-first-n-rows)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum first n matching values
===========================

by Dave Bruns · Updated 18 Sep 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[TAKE](https://exceljet.net/functions/take-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Sum first n matching values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20first%20n%20matching%20values_0.png "Excel formula: Sum first n matching values")

Summary
-------

To sum the first n matching values in a set of data, you can use a formula based on the [FILTER](https://exceljet.net/functions/filter-function)
 and [TAKE](https://exceljet.net/functions/take-function)
 functions. In the example shown, the formula in cell G5, copied down, is:

    =SUM(TAKE(FILTER(data[Qty],data[Color]=F5),3))
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:C16 and **n** is 3. The result is the sum of quantity for the first 3 Red values.

Generic formula
---------------

    =SUM(TAKE(FILTER(data,logic),n))

Explanation 
------------

In this example, the goal is to sum the first **n** matching values in a set of data. Specifically, we want to sum the first 3 values for both Red and Blue, based on the order they appear in the table. There are 12 values total; 6 entries each for Red and Blue. All data is in [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range B5:C16.

### Example formula

In the example shown, the formula in cell G5, copied down, is:

    =SUM(TAKE(FILTER(data[Qty],data[Color]=F5),3))
    

Notice the value for **n** is hardcoded as 3. This formula is a good example of [nesting](https://exceljet.net/glossary/nesting)
 one function inside another.

### Extracting matching data

Working from the inside out, the first task is to extract a list of quantities by color. This is done with the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    FILTER(data[Qty],data[Color]=F5)
    

With "Red" in cell F5, the result is an [array](https://exceljet.net/glossary/array)
 that contains quantities associated with "Red":

    {6;5;6;9;6;8}
    

Notice there are 6 numbers in this array, one for each entry where the color is Red.

### Extract first 3 values

The next task is to extract just the first 3 values from the array returned by FILTER. This is done with the [TAKE function](https://exceljet.net/functions/take-function)
. FILTER returns the array directly to the TAKE function as the _array_ argument, with the _rows_ argument hardcoded as 3:

    TAKE({6;5;6;9;6;8},3) // returns {6;5;6}
    

The TAKE function then returns the first 3 values in the array:

    {6;5;6}
    

### Sum results

The last step in the problem is to sum the results from FILTER and TAKE. This is done with the [SUM function](https://exceljet.net/functions/sum-function)
. TAKE returns the first 3 values to SUM:

    =SUM({6;5;6}) // returns 17
    

And SUM returns 17 as a final result. This is the sum of the first 3 quantities for "Red". When the formula is copied down to cell G6, we get a sum of the first 3 "Blue" quantities.

### Sum last n matching values

To sum the _last_ **n** matching values, simply change **n** to a negative number like this:

    =SUM(TAKE(FILTER(data[Qty],data[Color]=F5),-3))
    

The TAKE function is explained in more detail [here](https://exceljet.net/functions/take-function)
.

Related formulas
----------------

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Sum last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_columns.png "Excel formula: Sum last n columns")](https://exceljet.net/formulas/sum-last-n-columns)

### [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)

In this example, the goal is to sum the last n columns in a set of data, where n is a variable that can be changed at any time. In the latest version of Excel, the easiest way to solve this problem is with the TAKE function . In older versions of Excel you can use the OFFSET function , as explained...

[![Excel formula: FILTER on first or last n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20first%20or%20last%20n%20values.png "Excel formula: FILTER on first or last n values")](https://exceljet.net/formulas/filter-on-first-or-last-n-values)

### [FILTER on first or last n values](https://exceljet.net/formulas/filter-on-first-or-last-n-values)

In this example, the goal is to extract the first 3 values or the last 3 values from the named range data (B5:B15). We also want to exclude any empty cells from our results. In the worksheet shown the formula in cell D5 is: =INDEX(FILTER(data,data<>""),SEQUENCE(3,1,1,1)) Working from the...

[![Excel formula: Lookup first negative value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup%20first%20negative%20value.png "Excel formula: Lookup first negative value")](https://exceljet.net/formulas/lookup-first-negative-value)

### [Lookup first negative value](https://exceljet.net/formulas/lookup-first-negative-value)

In this example, the goal is to lookup the first negative value in a set of data. In addition, we also want to get the corresponding date. All data is in an Excel Table called data, in the range B5:C16. This information represents the low temperature in Fahrenheit (F) for the dates as shown. There...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

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

*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)
    
*   [FILTER on first or last n values](https://exceljet.net/formulas/filter-on-first-or-last-n-values)
    
*   [Lookup first negative value](https://exceljet.net/formulas/lookup-first-negative-value)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

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