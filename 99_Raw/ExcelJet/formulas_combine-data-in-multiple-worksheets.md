# Combine data in multiple worksheets - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/combine-data-in-multiple-worksheets

---

[Skip to main content](https://exceljet.net/formulas/combine-data-in-multiple-worksheets#main-content)

[](https://exceljet.net/formulas/combine-data-in-multiple-worksheets#)

*   [Previous](https://exceljet.net/formulas/biggest-gainers-and-losers)
    
*   [Next](https://exceljet.net/formulas/combine-ranges)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Combine data in multiple worksheets
===================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[VSTACK](https://exceljet.net/functions/vstack-function)

[FILTER](https://exceljet.net/functions/filter-function)

[LET](https://exceljet.net/functions/let-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8239/download?token=JzhGdH6u)
 (17.78 KB)

![Excel formula: Combine data in multiple worksheets](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/combine_data_in_multiple_worksheets.png "Excel formula: Combine data in multiple worksheets")

Summary
-------

To combine data in multiple worksheets, you can use a formula based on the [VSTACK function](https://exceljet.net/functions/vstack-function)
 and the [FILTER function](https://exceljet.net/functions/filter-function)
. In the example shown, we are combining data on three separate worksheets. The formula in cell B5 is:

    =LET(data,VSTACK(Sheet1:Sheet3!B5:E16),FILTER(data,CHOOSECOLS(data,1)<>""))

The result is a single set of data extracted from Sheet1, Sheet2, and Sheet3. The FILTER function is used to remove empty rows.

Generic formula
---------------

    =LET(data,VSTACK(Sheet1:Sheet3!range),FILTER(data,CHOOSECOLS(data,1)<>""))

Explanation 
------------

The goal is to combine data from different worksheets with a formula. Note that we are not restructuring the data in any way, we are simply combining data in different worksheets that already have the same structure. At a high level, the formula we are using combines data from multiple sheets with the VSTACK function and removes empty rows with FILTER. The data in the workbook comes from 3 separate worksheets (Sheet1, Sheet2, and Sheet3) and is combined in another worksheet named Summary. The Diagram below provides an overview:

![Data from Sheet1, Sheet2, and Sheet3 is combined on a Summary sheet](https://exceljet.net/sites/default/files/images/formulas/inline/combine_data_in_multiple_worksheets_overview.jpg "Data from Sheet1, Sheet2, and Sheet3 is combined on a Summary sheet")

Notice that the range in the formula below is fixed as B5:B16 and some of the rows in this range are empty on each worksheet. This means the solution should also provide a way to remove empty rows in the final result.  In the worksheet example above, the formula used to solve this problem in cell B5 looks like this:

    =LET(data,VSTACK(Sheet1:Sheet3!B5:E16),FILTER(data,CHOOSECOLS(data,1)<>""))

Let's look at how this formula works step-by-step. The first step is to combine the data, which is done with the VSTACK function.

_Note: in this example, we are working with a tiny amount of data in a small number of worksheets so that the problem is easy to understand. However, the same approach will work with larger sets of data in many more worksheets._

### Combining data with VSTACK and a 3D reference

The first step in this formula is to combine the data in three separate ranges on three separate sheets. When you have data in  "normal" ranges (i.e. data not in a named range or an Excel Table) at a predictable location on multiple worksheets, a nice approach is to use the [VSTACK function](https://exceljet.net/functions/vstack-function)
 with a [3D reference](https://exceljet.net/videos/how-to-create-3d-references)
 like this:

    =VSTACK(Sheet1:Sheet3!B5:E16)

The reference "Sheet1:Sheet3!B5:E16" is called a "3D reference". It points to the range B5:E16 on Sheet1 _through_ Sheet3 which, in this case, is Sheet1, Sheet2, and Sheet3. VSTACK retrieves data from the range B5:E16 on each sheet and stacks each range on top of another vertically. This is the core of the formula — the part that does the actual data consolidation.

> _Note: If you are new to the idea of a 3D reference, [this video provides an overview](https://exceljet.net/videos/how-to-create-3d-references)
> ._

This works well, as you can see in the screen below. However, one problem when using a fixed range like this is that the output may contain empty rows, which also appear in the output:

![Output from VSTACK may contain empty rows ](https://exceljet.net/sites/default/files/images/formulas/inline/combine_data_in_multiple_worksheets_empty_rows.png "Output from VSTACK may contain empty rows ")

To remove the extra rows, we can use the FILTER function. However, before we do that, it makes sense to store the output from VSTACK in a variable with the LET function. The reason we do this is because we are going to use the same data _twice_ in FILTER. By using a variable, we only need to run the VSTACK operation one time.

### LET function

The [LET function](https://exceljet.net/functions/let-function)
 allows you to name variables inside a formula. This makes more complex formulas easier to read and write. It also improves performance since certain operations only need to run one time. In this case, we use LET to name the output from VSTACK "data" like this:

    =LET(data,VSTACK(Sheet1:Sheet3!B5:E16),

VSTACK runs as explained above and the result (the combined ranges) is stored in the variable "data". The next step is to remove the empty rows. For that, we'll use the FILTER function.

### Removing empty rows with FILTER

As seen in the screen above, the result from VSTACK (now stored in the variable _data_) contains empty rows. To remove these empty rows from the final result, we use the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 together like this:

    FILTER(data,CHOOSECOLS(data,1)<>"") // remove empty rows

Here, the _array_ in FILTER is provided as _data_, which was created by LET in the previous step. The logic to remove empty rows is based on the CHOOSECOLS function:

    CHOOSECOLS(data,1)<>"" // test column 1

CHOOSECOLS is designed to retrieve one or more specific columns from a larger set of data. In this case, we are asking CHOOSECOLS for the first column in _data_. Then we use a [logical expression](https://exceljet.net/glossary/logical-operators)
 to test for "not empty" cells in the column. The result is an array of TRUE and FALSE values, one per row. This array is returned to FILTER as the _include_ argument. When FILTER applies this array of TRUE and FALSE values to data, only the rows associated with TRUE values are returned. The rows associated with FALSE values are discarded. The final result on the summary sheet looks like this:

![Final result on Summary sheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/combine_data_in_multiple_worksheets_summary.png "Final result on Summary sheet")

_Note: we are only testing the first column (Date) for empty rows. If you need a more robust test for empty rows, [see this example](https://exceljet.net/formulas/remove-blank-rows)
._

### Without the LET function

It isn't necessary to use the LET function for this formula, it's just more efficient. Here is the same formula without LET:

    =FILTER(VSTACK(Sheet1:Sheet3!B5:E16),CHOOSECOLS(VSTACK(Sheet1:Sheet3!B5:E16),1)<>"")

The overall structure is the same, but notice that we need to run the VSTACK operation twice inside FILTER. With larger amounts of data, this will slow the formula down.

### Without a 3D reference

The 3D reference is useful in this problem because the ranges on each sheet are at the same location. As long as this remains true, you can easily expand the 3D reference to include additional sheets. However, there is no requirement that you use a 3D reference. You could refer to each range separately inside VSTACK like this:

    =VSTACK(Sheet1!B5:E16,Sheet2!B5:E16,Sheet3!B5:E16)

This works fine, but the approach won't scale well as you add a larger number of sheets.

### Using the combined data

Once you have combined the data with the formula above, you can use it normally in other functions. For example, to sum the Total for all rows with a color of "Red", you can use a formula like this:

    =SUMIFS(E5:E16,C5:C16,"red")

You can also refer to the [spill range](https://exceljet.net/glossary/spill-range)
 B5# to refer to the combined data. For example, to return all rows that have a color of "Red" you can use FILTER like this:

    =FILTER(B5#,C5:C16="red")

### With Excel Tables

If you are combining data that exists in [Excel Tables](https://exceljet.net/articles/excel-tables)
, this problem is much easier.  For example, with the data in this example in three tables (Table1, Table2, and Table3) we can combine the data with a simple VSTACK formula like this:

    =VSTACK(Table1,Table2,Table3)

There is usually no need to remove empty rows because Excel Tables automatically expand and contract to fit the data they contain. This means we don't need to use any fancy tricks to figure out how many rows to retrieve, or how many empty rows to remove — we can simply combine data in the tables with VSTACK.

### Data in external workbooks

It is possible to combine data in separate external workbooks with VSTACK like this:

    VSTACK(Sheet1.xlsx!B5:E16,Sheet2.xlsx!B5:E16,Sheet3.xlsx!B5:E16)

Or, with a 3D reference to a single workbook, like this:

    VSTACK([workbook.xlsx]Sheet1:Sheet3!B5:E16)

_Note: I have only tested the external links on a single local drive, so results may vary in different environments._

Related formulas
----------------

[![Excel formula: Combine ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/combine_ranges.png "Excel formula: Combine ranges")](https://exceljet.net/formulas/combine-ranges)

### [Combine ranges](https://exceljet.net/formulas/combine-ranges)

In this example, the goal is to combine ranges. With the introduction of the VSTACK function and the HSTACK function, this is quite a simple task. To combine ranges vertically, stacking one range on top of another, you can use the VSTACK function like this: =VSTACK(range1,range2) To combine ranges...

[![Excel formula: Unique values from multiple ranges ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20from%20multiple%20ranges.png "Excel formula: Unique values from multiple ranges ")](https://exceljet.net/formulas/unique-values-from-multiple-ranges)

### [Unique values from multiple ranges](https://exceljet.net/formulas/unique-values-from-multiple-ranges)

In this example, the goal is to extract unique values from three separate ranges at the same time: range1 (C5:C16), range2 (D5:D15), and range3 (F5:F13). At one time, this was a difficult problem, since UNIQUE is programmed to accept only one array and there is no obvious way to provide another...

[![Excel formula: Remove blank rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_blank_rows.png "Excel formula: Remove blank rows")](https://exceljet.net/formulas/remove-blank-rows)

### [Remove blank rows](https://exceljet.net/formulas/remove-blank-rows)

In this example, the goal is to remove empty rows from a range with a formula. One approach is to use the BYROW function to identify all non-empty rows in the range and pass this result into the FILTER function as the include argument. This is the approach used in the worksheet shown, where the...

Related functions
-----------------

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

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

*   [Combine ranges](https://exceljet.net/formulas/combine-ranges)
    
*   [Unique values from multiple ranges](https://exceljet.net/formulas/unique-values-from-multiple-ranges)
    
*   [Remove blank rows](https://exceljet.net/formulas/remove-blank-rows)
    

### Functions

*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

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