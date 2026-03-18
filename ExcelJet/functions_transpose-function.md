# Excel TRANSPOSE function | Exceljet

**Source:** https://exceljet.net/functions/transpose-function

---

[Skip to main content](https://exceljet.net/functions/transpose-function#main-content)

[](https://exceljet.net/functions/transpose-function#)

*   [Previous](https://exceljet.net/functions/rows-function)
    
*   [Next](https://exceljet.net/functions/vlookup-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

TRANSPOSE Function
==================

by Dave Bruns · Updated 16 May 2024

![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")

Summary
-------

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

Purpose 
--------

Flip the orientation of a range of cells

Return value 
-------------

An array in a new orientation.

Syntax
------

    =TRANSPOSE(array)

*   _array_ - The array or range of cells to transpose.

Using the TRANSPOSE function 
-----------------------------

The TRANSPOSE function converts a vertical range of cells to a horizontal range of cells or a horizontal range of cells to a vertical range of cells. In other words, TRANSPOSE "flips" the orientation of a given range or array:

1.  When given a vertical range, TRANSPOSE converts it to a horizontal range
2.  When given a horizontal range, TRANSPOSE converts it to a vertical range

When a range or array is transposed, the first row becomes the first column of the new array, the second row becomes the second column of the new array, the third row becomes the third column of the new array, and so on.

TRANSPOSE can be used with both [ranges](https://exceljet.net/glossary/range)
 and [arrays](https://exceljet.net/glossary/array)
. Transposed ranges are dynamic. If data in the source range changes, TRANSPOSE will immediately update data in the target range.

### Examples

When given a vertical array, TRANSPOSE returns a [horizontal array](https://exceljet.net/glossary/array)
:

    =TRANSPOSE({"a";"b";"c"}) // returns {"a","b","c"}
    

To transpose the vertical range A1:A5 into a horizontal array:

    =TRANSPOSE(A1:A5) // vertical to horizontal
    

To transpose the horizontal range A1:E1 to a vertical array:

    =TRANSPOSE(A1:E1) // vertical to horizontal
    

In the example shown above, the formulas in I5 and F12 are:

    =TRANSPOSE(B5:F6) // formula in I5
    =TRANSPOSE(B12:C16) // formula in F12
    

_Note: TRANSPOSE does not carry over formatting. In the example shown, the target ranges have been formatted in a separate step._

### TRANSPOSE with other functions

TRANSPOSE can "catch" and transpose the output from another function. The formula below changes the result from XLOOKUP from a horizontal orientation to a vertical orientation:

    =TRANSPOSE((XLOOKUP(value,lookup_range,return_range))
    

Read more: [XLOOKUP wildcard example](https://exceljet.net/formulas/xlookup-wildcard-match-example)
.

### Older versions of Excel

In Excel 2021 or later, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, no special syntax is required, TRANSPOSE simply works and results [spill](https://exceljet.net/glossary/spill)
 into destination cells automatically. However, in older versions of Excel, TRANSPOSE must be entered as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 with control + shift + enter:

1.  First select the target range, which should have the same number of rows as the source range has columns, and the same number of columns as the source range has rows.
2.  Enter the TRANSPOSE function, and select the source range as the _array_ argument.
3.  Confirm the formula as an [array formula](https://exceljet.net/glossary/array-formula)
     with control + shift + enter.

### Paste special

The TRANSPOSE function makes sense when you need a dynamic solution that will continue to update when source data changes. However, for a one-time conversion, you can use Paste Special with the Transpose option. [This video covers the basics of Paste Special](https://exceljet.net/videos/shortcuts-for-paste-special)
.

TRANSPOSE function examples
---------------------------

[![Excel formula: Count rows with at least n matching values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20at%20least%20n%20matching%20values3.png "Excel formula: Count rows with at least n matching values")](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)

### [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)

Working from the inside out, the logical criteria used in this formula is: (data)<70 where data is the named range C5:I14. This generates a TRUE / FALSE result for every value in data , and the double negative coerces the TRUE FALSE values to 1 and 0 to yield an array like this: {0,0,0,1,0,1,0;0...

[![Excel formula: Get row totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20row%20totals.png "Excel formula: Get row totals")](https://exceljet.net/formulas/get-row-totals)

### [Get row totals](https://exceljet.net/formulas/get-row-totals)

In this example, the goal is to return an array with nine subtotals, one for each of the colors named in column B. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We can'...

[![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")](https://exceljet.net/formulas/dynamic-two-way-count)

### [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps: Create an Excel Table called data List unique colors with UNIQUE function List unique sizes with UNIQUE...

[![Excel formula: Dynamic two-way sum](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20sum.png "Excel formula: Dynamic two-way sum")](https://exceljet.net/formulas/dynamic-two-way-sum)

### [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)

In this example, the goal is to create a formula that performs a dynamic two-way sum of all City and Size combinations in the range B5:D17 . The solution shown requires four basic steps: Create an Excel Table called data List unique cities with the UNIQUE function List unique sizes with the UNIQUE...

[![Excel formula: Count columns that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20columns%20that%20contain%20specific%20values.png "Excel formula: Count columns that contain specific values")](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

### [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)

In this example, the goal is to count the number of columns in the data that contain 19 (the value in cell I4). The main challenge in this problem is that the value might appear in any row, and more than once in the same column. If we wanted to simply count the total number of times a value...

[![Excel formula: Count cells that do not contain many strings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain%20many%20strings.png "Excel formula: Count cells that do not contain many strings")](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

### [Count cells that do not contain many strings](https://exceljet.net/formulas/count-cells-that-do-not-contain-many-strings)

The goal in this example is to count cells in a range that do not contain a given number of strings. The cells to evaluate are in the named range data (B5:B14) and the strings to exclude are listed in the named range exclude (D5:D7). If your needs are simple, you can use the COUNTIFS function to...

[![Excel formula: Count rows that contain specific values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20that%20contain%20specific%20values.png "Excel formula: Count rows that contain specific values")](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

### [Count rows that contain specific values](https://exceljet.net/formulas/count-rows-that-contain-specific-values)

In this example, the goal is to count the number of rows in the data that contain the value in cell G4, which is 19. The main challenge in this problem is that the value might appear in any column, and might appear more than once in the same row. If we wanted to simply count the total number of...

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Get column totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20column%20totals.png "Excel formula: Get column totals")](https://exceljet.net/formulas/get-column-totals)

### [Get column totals](https://exceljet.net/formulas/get-column-totals)

In this example, the goal is to return an array with 7 subtotals, one for each day of the week, as seen in columns C:I. The numbers to sum are contained in data which is the named range C5:I13. This is an example of a problem where the goal is to create an array of sums rather than a single sum. We...

[![Excel formula: Transpose table without zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/transpose%20table%20without%20zeros.png "Excel formula: Transpose table without zeros")](https://exceljet.net/formulas/transpose-table-without-zeros)

### [Transpose table without zeros](https://exceljet.net/formulas/transpose-table-without-zeros)

The TRANSPOSE function automatically transposes values in a horizontal orientation to vertical orientation and vice versa. However, if a source cell is blank (empty) TRANSPOSE will output a zero. To fix that problem, this formula contains an IF function that checks first to see if a cell is blank...

[![Excel formula: Weighted average](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/weighted_average.png "Excel formula: Weighted average")](https://exceljet.net/formulas/weighted-average)

### [Weighted average](https://exceljet.net/formulas/weighted-average)

In this example, the goal is to calculate a weighted average of scores for each name in the table using the weights that appear in the named range weights (I5:K5) and the scores in columns C through E. A weighted average (also called a weighted mean ) is an average where some values are more...

[![Excel formula: Filter horizontal data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Filter%20horizontal%20data.png "Excel formula: Filter horizontal data")](https://exceljet.net/formulas/filter-horizontal-data)

### [Filter horizontal data](https://exceljet.net/formulas/filter-horizontal-data)

Note: FILTER is a new dynamic array function in Excel 365 . In other versions of Excel, there are alternatives , but they are more complex. There are ten columns of data in the range C4:L6. The goal is to filter this horizontal data and extract only columns (records) where the group is "fox". For...

[![Excel formula: List sheet names with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/List_sheet_names_with_formula_0.png "Excel formula: List sheet names with formula")](https://exceljet.net/formulas/list-sheet-names-with-formula)

### [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)

In this example, the goal is to generate a list of the sheet names in an Excel workbook with a formula. Unfortunately, there is no simple way to do this with a formula in Excel. However, it can be done with a two-step approach: Define a name called "sheetnames" with an old macro command and the...

[![Excel formula: Flip table rows to columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/flip%20table%20rows%20to%20columns.png "Excel formula: Flip table rows to columns")](https://exceljet.net/formulas/flip-table-rows-to-columns)

### [Flip table rows to columns](https://exceljet.net/formulas/flip-table-rows-to-columns)

The TRANSPOSE function is fully automatic and can transpose cells vertical to horizontal, and vice versa. The only requirement is that there be a one to one relationship between source and target cells. In the example shown, we are transposing a table that is 2 columns by 7 rows (14 cells), to a...

[![Excel formula: Filter and transpose horizontal to vertical](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20and%20transpose%20horizontal%20to%20vertical.png "Excel formula: Filter and transpose horizontal to vertical")](https://exceljet.net/formulas/filter-and-transpose-horizontal-to-vertical)

### [Filter and transpose horizontal to vertical](https://exceljet.net/formulas/filter-and-transpose-horizontal-to-vertical)

The goal is to filter the horizontal data in the range C4:L6 to extract members of the group "fox" and display results with data transposed to a vertical format. For convenience and readability, we have two named ranges to work with: data (C4:L6) and group (C5:L5). The FILTER function can be used...

TRANSPOSE function videos
-------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Two-way%20summary%20with%20dynamic%20arrays-PLAY.png)](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)

### [Two-way summary with dynamic arrays](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)

In this video, we'll look at how to create a two-way summary table with dynamic array formulas that works like a pivot table. This worksheet contains several hundred rows of sample order data in an Excel Table called "data". I'll first build a pivot table to summarize this data by Color and Region...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Weighted average](https://exceljet.net/formulas/weighted-average)
    
*   [Count columns that contain specific values](https://exceljet.net/formulas/count-columns-that-contain-specific-values)
    
*   [Filter horizontal data](https://exceljet.net/formulas/filter-horizontal-data)
    
*   [Index and match on multiple columns](https://exceljet.net/formulas/index-and-match-on-multiple-columns)
    
*   [Count rows with at least n matching values](https://exceljet.net/formulas/count-rows-with-at-least-n-matching-values)
    
*   [XLOOKUP wildcard match example](https://exceljet.net/formulas/xlookup-wildcard-match-example)
    
*   [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)
    
*   [Sort and extract unique values](https://exceljet.net/formulas/sort-and-extract-unique-values)
    
*   [Get row totals](https://exceljet.net/formulas/get-row-totals)
    
*   [Unwrap column into fields](https://exceljet.net/formulas/unwrap-column-into-fields)
    

### Videos

*   [Two-way summary with dynamic arrays](https://exceljet.net/videos/two-way-summary-with-dynamic-arrays)
    

### Links

*   [Microsoft TRANSPOSE function documentation](https://support.office.com/en-us/article/transpose-function-ed039415-ed8a-4a81-93e9-4b6dfac76027)
    

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