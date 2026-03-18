# Average last n columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-last-n-columns

---

[Skip to main content](https://exceljet.net/formulas/average-last-n-columns#main-content)

[](https://exceljet.net/formulas/average-last-n-columns#)

*   [Previous](https://exceljet.net/formulas/average-last-3-numeric-values)
    
*   [Next](https://exceljet.net/formulas/average-last-n-rows)
    

[Average](https://exceljet.net/formulas#Average)

Average last n columns
======================

by Dave Bruns · Updated 4 Oct 2023

Related functions 
------------------

[TAKE](https://exceljet.net/functions/take-function)

[AVERAGE](https://exceljet.net/functions/average-function)

[OFFSET](https://exceljet.net/functions/offset-function)

[COUNT](https://exceljet.net/functions/count-function)

[INDEX](https://exceljet.net/functions/index-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

![Excel formula: Average last n columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_last_5_columns.png "Excel formula: Average last n columns")

Summary
-------

To average the last **n** columns in a set of data, you can use the [TAKE function](https://exceljet.net/functions/take-function)
 with the [AVERAGE function](https://exceljet.net/functions/average-function)
. In the example shown, the formula in K5 is:

    =AVERAGE(TAKE(data,,-J5))

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:H16 and **n** is entered in cell J5 as a variable. The result is 8.42, the average of values in the range F5:H16.

_Notes: (1) The TAKE function is new in Excel. See below for options that will work in older versions. (2) The example shows an average across 12 rows, but the formula will work fine with a single row of data._

Generic formula
---------------

    =AVERAGE(TAKE(data,,-n))

Explanation 
------------

In this example, the goal is to average the last **n** columns in a set of data, where **n** is a variable entered in cell K5 that can be changed at any time. Since more data may be added, a key requirement is to average amounts _by_ __position.__ For convenience, the values to average are in the [named range](https://exceljet.net/glossary/named-range)
 **data** (C5:H16). In the latest version of Excel, the best way to solve this problem is with the [TAKE function](https://exceljet.net/functions/take-function)
, a new [dynamic array function](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 in Excel. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, you can use the [OFFSET function](https://exceljet.net/functions/offset-function)
 or the [INDEX function](https://exceljet.net/functions/index-function)
. All three approaches are explained below.

### TAKE function

The TAKE function returns a subset of a given [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
. The size of the array returned is determined by separate _rows_ and _columns_ [arguments](https://exceljet.net/glossary/function-argument)
:

    =TAKE(array,rows,columns)
    

When positive numbers are provided for _rows_ or _columns_, TAKE returns values from the start of the array:

    =TAKE(array,3) // get first 3 rows
    =TAKE(array,,3) // get first 3 columns
    

When negative numbers are provided, TAKE returns values from the end of the array:

    =TAKE(array,-3) // get last 3 rows
    =TAKE(array,,-3) // get last 3 columns
    

In the worksheet shown, **data** is the named range C5:H16. We can retrieve the last 3 columns like this:

    =TAKE(data,,-3) // last 3 columns

Notice we simply omit _rows_ in this case because we want all rows in **data**_._ To make the number of columns variable, we simply swap in the reference to J5 and add a negative sign:

    =TAKE(data,,-J5)

Finally, to average the result from TAKE, we [nest](https://exceljet.net/glossary/nesting)
 the TAKE function inside the [AVERAGE function](https://exceljet.net/functions/average-function)
:

    =AVERAGE(TAKE(data,,-J5))

With 3 in cell J5, TAKE returns the last 3 columns in **data**. This result is handed off to the AVERAGE function, which returns a final result of 8.42, the average of values in the range F5:H16.

### OFFSET function

In older versions of Excel, another way to solve this problem is to use the [OFFSET function](https://exceljet.net/functions/offset-function)
. The OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. To average the last 3 columns in the named range **data**, we can use the OFFSET function like this:

    =AVERAGE(OFFSET(data,0,COLUMNS(data)-J5,,J5))

Inside the OFFSET function, we provide **data** for _reference_ and 0 for _rows_, since we don't want any row offset. Next, we count the number of columns in data with the [COLUMNS function](https://exceljet.net/functions/columns-function)
 and subtract the value for **n** in cell J5 to get a value for _cols_, the column offset. We leave _height_ empty, because OFFSET will automatically inherit the height of _reference_, and we supply J5 for _width_ since we want a 3-column range in the end. In this configuration, OFFSET returns a 3-column range starting at cell F5 in **data** containing all 12 rows.

_Note: the [OFFSET function](https://exceljet.net/functions/offset-function)
 is a volatile function and can cause performance problems in larger or more complicated worksheets. If you run into this problem, see the INDEX solution below._

### INDEX function

Another way to solve this problem is to use the versatile [INDEX function](https://exceljet.net/functions/index-function)
 in a formula like this:

    =AVERAGE(INDEX(data,0,COLUMNS(data)-(J5-1)):INDEX(data,0,COLUMNS(data)))

The key to understanding this formula is to realize that the INDEX function can return a _reference_ to [entire rows](https://exceljet.net/formulas/look-up-entire-row)
 and [entire columns](https://exceljet.net/formulas/look-up-entire-column)
. To generate a reference to the "last n columns" in a table, we build a reference in two parts: the left column and the right column, then use the range [operator](https://exceljet.net/glossary/math-operators)
 (:) to join the two parts together:

    =AVERAGE(left:right)

To get a reference to the _left_ column, we use:

    INDEX(data,0,COLUMNS(data)-(J5-1))

Since **data** contains 6 columns, the COLUMNS function returns 6, and this simplifies to:

    INDEX(data,0,4) // column 4
    

INDEX returns a reference to column 4, F5:F16. For the _right_ column in the range, we use INDEX like this:

    INDEX(data,0,COLUMNS(data))
    

Since COLUMNS returns 6, this simplifies to:

    INDEX(data,0,6) // column 6
    

INDEX returns a reference to column 6, H5:H16. Together, the two INDEX functions return a reference to columns 4 through 6 in the **data** (i.e. F5:H16). The range [operator](https://exceljet.net/glossary/math-operators)
 (:) joins the two references together, and the AVERAGE function returns a final result of 8.42.

Related formulas
----------------

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

[![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")](https://exceljet.net/formulas/average-last-3-numeric-values)

### [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the AVERAGE function , the FILTER function , and the TAKE...

Related functions
-----------------

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)
    
*   [Average last 3 numeric values](https://exceljet.net/formulas/average-last-3-numeric-values)
    

### Functions

*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    

### Articles

*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

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