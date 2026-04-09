# Sum last n columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-last-n-columns

---

[Skip to main content](https://exceljet.net/formulas/sum-last-n-columns#main-content)

[](https://exceljet.net/formulas/sum-last-n-columns#)

*   [Previous](https://exceljet.net/formulas/sum-last-30-days)
    
*   [Next](https://exceljet.net/formulas/sum-last-n-rows)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum last n columns
==================

by Dave Bruns · Updated 18 Mar 2025

Related functions 
------------------

[TAKE](https://exceljet.net/functions/take-function)

[OFFSET](https://exceljet.net/functions/offset-function)

[COLUMNS](https://exceljet.net/functions/columns-function)

[INDEX](https://exceljet.net/functions/index-function)

[SUM](https://exceljet.net/functions/sum-function)

[TRIMRANGE](https://exceljet.net/functions/trimrange-function)

![Excel formula: Sum last n columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_last_n_columns.png "Excel formula: Sum last n columns")

Summary
-------

To sum the last **n** columns in a table of data, you can use a formula based on the [TAKE function](https://exceljet.net/functions/take-function)
. In the example shown, the formula in K5 is:

    =SUM(TAKE(data,,-J5))

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:H16. The result is 303, the sum of values in the range F5:H16.

_Note: The TAKE function is new in Excel. See below for options that will work in older versions._

Generic formula
---------------

    =SUM(TAKE(data,,-n))

Explanation 
------------

In this example, the goal is to sum the last **n** columns in a set of data, where **n** is a variable that can be changed at any time. In the latest version of Excel, the easiest way to solve this problem is with the [TAKE function](https://exceljet.net/functions/take-function)
. In older versions of Excel you can use the [OFFSET function](https://exceljet.net/functions/offset-function)
, as explained below.

### TAKE function

The TAKE function returns a subset of a given [array](https://exceljet.net/glossary/array)
 or [range](https://exceljet.net/glossary/range)
. The size of the array returned is determined by separate _rows_ and _columns_ [arguments](https://exceljet.net/glossary/function-argument)
. When positive numbers are provided for rows or columns, TAKE returns values from the start or top of the array. Negative numbers take values from the end or bottom of the array. For example:

    =TAKE(array,3) // get first 3 rows
    =TAKE(array,-3) // get last 3 rows
    =TAKE(array,,3) // get first 3 columns
    =TAKE(array,,-3) // get last 3 columns
    

In the worksheet shown, **data** is the named range C5:H16. We can retrieve the last 3 columns like this:

    =TAKE(data,,-3) // last 3 columns

To make the number of columns variable, we need to swap in the reference to J5:

    =TAKE(data,,-J5)

Finally, to sum the result from TAKE, we need to [nest](https://exceljet.net/glossary/nesting)
 the TAKE function inside the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM(TAKE(data,,-J5))

With 3 in cell J5, the result from TAKE is the last 3 columns in **data**. This result is handed off to the SUM function, which returns a final result of 303, the sum of values in the range F5:H16.

### Dynamic range option

One limitation of the formula above is that the named range **data** is static — it won't expand as new columns are added. A simple way to make the range dynamic is to add the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
 to the formula like this:

    =SUM(TAKE(TRIMRANGE(range,,-n)))

The TRIMRANGE function removes empty rows and columns from a range of data. The result is a "trimmed" range that only includes the used portion of the range. Because it is a formula, TRIMRANGE will update the range dynamically when data is added or removed from the original range. To make this work correctly, you will want to use a range that is largest enough to hold all possible data. For example, if the data begins in column A and might include up to 12 columns, you could use TRIMRANGE like this:

    =SUM(TAKE(TRIMRANGE(A:L),,-n))

If needed, you could also remove the header row with the [DROP function](https://exceljet.net/functions/drop-function)
:

    =SUM(TAKE(DROP(TRIMRANGE(A:L),1),,-3))

You can read more about the TRIMRANGE function [here](https://exceljet.net/functions/trimrange-function)
.

### OFFSET function

In older versions of Excel, another way to solve this problem is to use the [OFFSET function](https://exceljet.net/functions/offset-function)
. The OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. To sum the last 3 columns in the named range **data**, we can use the OFFSET function like this:

    =SUM(OFFSET(data,0,COLUMNS(data)-J5,,J5))

Inside the OFFSET function, we provide **data** for _reference_ and 0 for _rows_, since we don't want any row offset. Next, we subtract the value for **n** in cell J5 from the total columns in data (6) to get a value for _cols_ (3), the column offset. We leave _height_ empty, because OFFSET will automatically inherit the height of _reference_, and we supply J5 for _width_, since we want a 3-column range in the end. In this configuration, OFFSET returns a 3-column range starting at cell F5, and this range contains 12 rows because the named range **data** contains 12 rows.

_Note: the_ [_OFFSET function_](https://exceljet.net/functions/offset-function)
 _is a volatile function and can cause performance problems in larger or more complicated worksheets. If you run into this problem, see the INDEX solution below._

### INDEX function

Yet another way to solve this problem is to use the versatile [INDEX function](https://exceljet.net/functions/index-function)
 in a formula like this:

    =SUM(INDEX(data,0,COLUMNS(data)-(J5-1)):INDEX(data,0,COLUMNS(data)))

The key to understanding this formula is to realize that the INDEX function can return a _reference_ to [entire rows](https://exceljet.net/formulas/look-up-entire-row)
 and [entire columns](https://exceljet.net/formulas/look-up-entire-column)
. To generate a reference to the "last n columns" in a table, we build a reference in two parts: the left column and the right column, then use the range [operator](https://exceljet.net/glossary/math-operators)
 (:) to join the two parts together. To get a reference to the _left_ column, we use:

    INDEX(data,0,COLUMNS(data)-(J5-1))
    

Since **data** contains 6 columns, the COLUMNS function returns 6, and this simplifies to:

    INDEX(data,0,4) // column 4
    

INDEX returns a reference to column 4. For the _right_ column in the range, we use INDEX like this:

    INDEX(data,0,COLUMNS(data))
    

Since COLUMNS returns 6, this simplifies to:

    INDEX(data,0,6) // column 6
    

Together, the two INDEX functions return a reference to columns 4 through 6 in the **data** (i.e. F5:H16). The range [operator](https://exceljet.net/glossary/math-operators)
 (:) joins the two references together, and the SUM function returns a final result of 303.

Related formulas
----------------

[![Excel formula: Sum entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20entire%20column.png "Excel formula: Sum entire column")](https://exceljet.net/formulas/sum-entire-column)

### [Sum entire column](https://exceljet.net/formulas/sum-entire-column)

In this example, the goal is to return the total for an entire column in an Excel worksheet. One way to do this is to use a full column reference. Full column references Excel supports " full column " like this: =SUM(A:A) // sum all of column A =SUM(C:C) // sum all of column C =SUM(A:C) // sum all...

[![Excel formula: Look up entire column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20column.png "Excel formula: Look up entire column")](https://exceljet.net/formulas/look-up-entire-column)

### [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)

In this example, the goal is to look up and retrieve an entire column of values in a set of data. For example, when a value like "Q3" is entered into cell H4, all values in the range E5:E16 should be returned. For convenience and readability, quarter (C4:F4) and data (C5:F16) are named ranges ...

[![Excel formula: Look up entire row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/look%20up%20entire%20row.png "Excel formula: Look up entire row")](https://exceljet.net/formulas/look-up-entire-row)

### [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)

In this example, the goal is to look up and retrieve an entire row of values in a set of data. For example, when a value like "Neptune" is entered into cell H5, all values in the range C11:F11 should be returned. For convenience and readability, project (B5:B16) and data (C5:F16) are named ranges...

Related functions
-----------------

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

[![Excel COLUMNS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20columns%20function.png "Excel COLUMNS function")](https://exceljet.net/functions/columns-function)

### [COLUMNS Function](https://exceljet.net/functions/columns-function)

The Excel COLUMNS function returns the count of columns in a given reference. For example, COLUMNS(A1:C3) returns 3, since the range A1:C3 contains 3 columns.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel TRIMRANGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_trimrange_function.png "Excel TRIMRANGE function")](https://exceljet.net/functions/trimrange-function)

### [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)

The Excel TRIMRANGE function removes empty rows and columns from the outer edges of a range of data. The result is a "trimmed" range that only includes data from the used portion of the range. Because it is a formula, TRIMRANGE will update the range dynamically when data is added or removed...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum entire column](https://exceljet.net/formulas/sum-entire-column)
    
*   [Look up entire column](https://exceljet.net/formulas/look-up-entire-column)
    
*   [Look up entire row](https://exceljet.net/formulas/look-up-entire-row)
    

### Functions

*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [COLUMNS Function](https://exceljet.net/functions/columns-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    

### Links

*   [The Imposing INDEX (fantastic article by Daniel Ferry)](http://www.excelhero.com/blog/2011/03/the-imposing-index.html)
    

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