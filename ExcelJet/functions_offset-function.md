# Excel OFFSET function | Exceljet

**Source:** https://exceljet.net/functions/offset-function

---

[Skip to main content](https://exceljet.net/functions/offset-function#main-content)

[](https://exceljet.net/functions/offset-function#)

*   [Previous](https://exceljet.net/functions/match-function)
    
*   [Next](https://exceljet.net/functions/row-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

OFFSET Function
===============

by Dave Bruns · Updated 12 Feb 2023

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")

Summary
-------

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

Purpose 
--------

Create a reference offset from given starting point

Return value 
-------------

A cell reference.

Syntax
------

    =OFFSET(reference,rows,cols,[height],[width])

*   _reference_ - The starting point, supplied as a cell reference or range.
*   _rows_ - The number of rows to offset below the starting reference.
*   _cols_ - The number of columns to offset to the right of the starting reference.
*   _height_ - \[optional\] The height in rows of the returned reference.
*   _width_ - \[optional\] The width in columns of the returned reference.

Using the OFFSET function 
--------------------------

The Excel OFFSET function returns a dynamic range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns.

> OFFSET is a [volatile function](https://exceljet.net/glossary/volatile-function)
> , and can cause performance issues in large or complex worksheets.

The starting point (the _reference_ argument) can be one cell or a range of cells. The _rows_ and _cols_ arguments are the number of cells to "offset" from the starting point. The _height_ and _width_ arguments are optional and determine the size of the range that is created. When _height_ and _width_ are omitted, they default to the height and width of _reference_.

For example, to reference C5 starting at A1,  _reference_ is A1, _rows_ is 4 and _cols_ is 2:

    =OFFSET(A1,4,2) // returns reference to C5
    

To reference C1:C5 from A1, _reference_ is A1, _rows_ is 0, _cols_ is 2, _height_ is 5, and _width_ is 1:

    =OFFSET(A1,0,2,5,1) // returns reference to C1:C5
    

_Note: width could be omitted, since it will default to 1._

It is common to see OFFSET wrapped in another function that expects a range. For example, to SUM C1:C5, beginning at A1:

    =SUM(OFFSET(A1,0,2,5,1)) // SUM C1:C5
    

The main purpose of OFFSET is to allow formulas to dynamically adjust to available data or to user input. The OFFSET function can be used to build a [dynamic named range](https://exceljet.net/formulas/dynamic-named-range-with-offset)
 for charts or pivot tables, to ensure that source data is always up to date.

_Note: Excel documentation states height and width can't be negative, but negative values appear to have worked fine [since the early 1990's](https://answers.microsoft.com/en-us/msoffice/forum/all/offset-bug-negative-height-argument/dc24aca4-b77c-e011-9b4b-68b599b31bf5)
. The OFFSET function in Google Sheets won't allow a negative value for height or width arguments._

Examples
--------

The examples below show how OFFSET can be configured to return different kinds of ranges. These screens were taken with [Excel 365](https://exceljet.net/glossary/excel-365)
, so OFFSET returns a [dynamic array](https://exceljet.net/glossary/dynamic-array)
 when the result is more than one cell. In older versions of Excel, you can use the [F9 key](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
 to check results returned from OFFSET.

### Example #1

In the screen below, we use OFFSET to return the third value (March) in the second column (West). The formula in H4 is:

    =OFFSET(B3,3,2) // returns D6
    

![OFFSET Function Example 1](https://exceljet.net/sites/default/files/images/functions/inline/OFFSET%20function%20example%201.png "OFFSET Function Example 1")

### Example #2

In the screen below, we use OFFSET to return the last value (June) in the third column (North). The formula in H4 is:

    =OFFSET(B3,6,3) // returns E9
    

![OFFSET Function Example 2](https://exceljet.net/sites/default/files/images/functions/inline/OFFSET%20function%20example%202.png "OFFSET Function Example 2")

### Example #3

Below, we use OFFSET to return all values in the third column (North). The formula in H4 is:

    =OFFSET(B3,1,3,6) // returns E4:E9
    

![OFFSET Function Example 3](https://exceljet.net/sites/default/files/images/functions/inline/OFFSET%20function%20example%203.png "OFFSET Function Example 3")

### Example #4

Below, we use OFFSET to return all values for May (fifth row). The formula in H4 is:

    =OFFSET(B3,5,1,1,4) // returns C8:F8
    

![OFFSET Function Example 4](https://exceljet.net/sites/default/files/images/functions/inline/OFFSET%20function%20example%204.png "OFFSET Function Example 4")

### Example #5

Below, we use OFFSET to return April, May, and June values for the West region. The formula in H4 is:

    =OFFSET(B3,4,2,3,1) // returns D7:D9
    

![OFFSET Function Example 5](https://exceljet.net/sites/default/files/images/functions/inline/OFFSET%20function%20example%205.png "OFFSET Function Example 5")

### Example #6

Below, we use OFFSET to return April, May, and June values for West and North. The formula in H4 is:

    =OFFSET(B3,4,2,3,2) // returns D7:E9
    

![OFFSET Function Example 6](https://exceljet.net/sites/default/files/images/functions/inline/OFFSET%20function%20example%206.png "OFFSET Function Example 6")

### Notes

*   OFFSET only returns a reference, no cells are moved.
*   Both _rows_ and _cols_ can be supplied as negative numbers to reverse their normal offset direction - negative **cols** offset to the left, and negative _rows_ offset above.
*   OFFSET is a "[volatile function](https://exceljet.net/glossary/volatile-function)
    ". Volatile functions can make larger and more complex workbooks run slowly.
*   OFFSET will display the #REF! error value if the offset is outside the edge of the worksheet.
*   When _height_ or _width_ is omitted, the height and width of _reference_ is used.
*   OFFSET can be used with any other function that expects to receive a reference.
*   Excel documentation says _height_ and _width_ can't be negative, but negative values do work.

OFFSET function examples
------------------------

[![Excel formula: Copy value from every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20column.png "Excel formula: Copy value from every nth column")](https://exceljet.net/formulas/copy-value-from-every-nth-column)

### [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)

In Excel, you can't easily create formulas that skip columns following a certain pattern, because the references in the formula will automatically change to maintain the relationship between the original source cell and the new target cell. However, with a little work, it's possible to construct...

[![Excel formula: Define range based on cell value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Define%20range%20based%20on%20cell%20value.png "Excel formula: Define range based on cell value")](https://exceljet.net/formulas/define-range-based-on-cell-value)

### [Define range based on cell value](https://exceljet.net/formulas/define-range-based-on-cell-value)

This formula relies on a specific behavior of INDEX — although it seems that INDEX returns the value at a particular location, it actually returns a reference to the location. In most formulas, you wouldn't notice the difference – Excel simply evaluates the reference and returns the value. This...

[![Excel formula: Average last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_5_columns.png "Excel formula: Average last n columns")](https://exceljet.net/formulas/average-last-n-columns)

### [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)

In this example, the goal is to average the last n columns in a set of data, where n is a variable entered in cell K5 that can be changed at any time. Since more data may be added, a key requirement is to average amounts by position. For convenience, the values to average are in the named range...

[![Excel formula: Sum last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_n_columns.png "Excel formula: Sum last n columns")](https://exceljet.net/formulas/sum-last-n-columns)

### [Sum last n columns](https://exceljet.net/formulas/sum-last-n-columns)

In this example, the goal is to sum the last n columns in a set of data, where n is a variable that can be changed at any time. In the latest version of Excel, the easiest way to solve this problem is with the TAKE function . In older versions of Excel you can use the OFFSET function , as explained...

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

[![Excel formula: Count visible rows with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20visible%20rows%20with%20criteria.png "Excel formula: Count visible rows with criteria")](https://exceljet.net/formulas/count-visible-rows-with-criteria)

### [Count visible rows with criteria](https://exceljet.net/formulas/count-visible-rows-with-criteria)

In this example, the goal is to count visible rows where Region="West". Row 13 meets this criteria, but has been hidden. The SUBTOTAL function can easily generate sums and counts for visible rows. However, SUBTOTAL is not able to apply criteria like the COUNTIFS function without help. Conversely,...

[![Excel formula: Unwrap column into fields](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unwrap%20column%20into%20fields.png "Excel formula: Unwrap column into fields")](https://exceljet.net/formulas/unwrap-column-into-fields)

### [Unwrap column into fields](https://exceljet.net/formulas/unwrap-column-into-fields)

In this example the goal is to "unwrap" a column of values into separate fields. The values are spaced evenly apart, and the result should be all related values on one row, where each column corresponds to a field of information. The input data appears in column B. Each "record" in the data has...

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

[![Excel formula: Dynamic named range with OFFSET](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20offset.png "Excel formula: Dynamic named range with OFFSET")](https://exceljet.net/formulas/dynamic-named-range-with-offset)

### [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)

Dynamic ranges are also known as expanding ranges because they automatically expand and contract to accommodate new or deleted data. You can see a video demo of this approach here . This formula uses the OFFSET function to generate a range that expands and contracts by adjusting height and width...

[![Excel formula: Moving average formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/moving%20average%20formula.png "Excel formula: Moving average formula")](https://exceljet.net/formulas/moving-average-formula)

### [Moving average formula](https://exceljet.net/formulas/moving-average-formula)

The formulas shown in the example all use the AVERAGE function with a relative reference set up for each specific interval. The 3-day moving average in E7 is calculated by feeding AVERAGE a range that includes the current day and the two previous days like this: =AVERAGE(C5:C7) // 3-day average The...

[![Excel formula: Sum every 3 cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%203%20cells.png "Excel formula: Sum every 3 cells")](https://exceljet.net/formulas/sum-every-3-cells)

### [Sum every 3 cells](https://exceljet.net/formulas/sum-every-3-cells)

At the core, the OFFSET function delivers a range of 3 cells to SUM, which returns a summed result. The arguments for OFFSET are provided as follows: For reference we use the first cell in the data range, B5, entered as a mixed reference (column locked, row relative). For rows , we use 0, since we...

[![Excel formula: COUNTIFS with variable range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/countifs%20with%20a%20variable%20range.png "Excel formula: COUNTIFS with variable range")](https://exceljet.net/formulas/countifs-with-variable-range)

### [COUNTIFS with variable range](https://exceljet.net/formulas/countifs-with-variable-range)

In the example shown, the formula in B11 is: =COUNTIFS(OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1),"<>") Working from the inside out, the work of setting up a variable range is done by the OFFSET function here: OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1) // variable range OFFSET has five arguments and is...

[![Excel formula: Sum first n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_first_n_rows.png "Excel formula: Sum first n rows")](https://exceljet.net/formulas/sum-first-n-rows)

### [Sum first n rows](https://exceljet.net/formulas/sum-first-n-rows)

In the example shown, we have a list of amounts by month. The goal is to dynamically sum values through a given number of months using a variable n in cell E5. Since month names are just text, and months are listed in order, the key requirement is to sum amounts by position , starting with cell C5...

[![Excel formula: Sum every n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20every%20n%20rows.png "Excel formula: Sum every n rows")](https://exceljet.net/formulas/sum-every-n-rows)

### [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)

In this example, the goal is to calculate a weekly total using the data as shown. Notice each week corresponds to 5 rows of data (Monday-Friday) so we will need to sum values in every 5 rows. To build a range that corresponds to the correct 5 rows for each week, we use the OFFSET function. To sum...

[![Excel formula: Copy value from every nth row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/copy%20value%20every%20nth%20row_0.png "Excel formula: Copy value from every nth row")](https://exceljet.net/formulas/copy-value-from-every-nth-row)

### [Copy value from every nth row](https://exceljet.net/formulas/copy-value-from-every-nth-row)

In this example, the goal is to copy every nth value from column B, where n is a variable that can be changed as needed. In Excel, it's difficult to create formulas that skip rows following a certain pattern, because the references in the formula will automatically change as the formula is copied...

OFFSET function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20OFFSET-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)

### [How to create a dynamic named range with OFFSET](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)

In this video we're going to look at how to create a dynamic named range using the OFFSET function . To create a dynamic named range that refers to this data using the OFFSET function, first identify the first cell of the data in the upper left. In this case, that's cell B6. To create a named range...

Related functions
-----------------

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

*   [Count visible rows with criteria](https://exceljet.net/formulas/count-visible-rows-with-criteria)
    
*   [Unwrap column into fields](https://exceljet.net/formulas/unwrap-column-into-fields)
    
*   [Sum every 3 cells](https://exceljet.net/formulas/sum-every-3-cells)
    
*   [Copy value from every nth column](https://exceljet.net/formulas/copy-value-from-every-nth-column)
    
*   [COUNTIFS with variable range](https://exceljet.net/formulas/countifs-with-variable-range)
    
*   [Sum first n rows](https://exceljet.net/formulas/sum-first-n-rows)
    
*   [Dynamic named range with OFFSET](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    
*   [Sum last n rows](https://exceljet.net/formulas/sum-last-n-rows)
    
*   [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)
    
*   [Sum every n rows](https://exceljet.net/formulas/sum-every-n-rows)
    

### Videos

*   [How to create a dynamic named range with OFFSET](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-offset)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    

### Links

*   [Microsoft OFFSET function documentation](https://support.office.com/en-us/article/offset-function-c8de19ae-dd79-4b9b-a14e-b4d906d11b66)
    

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