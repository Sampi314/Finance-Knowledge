# Filter by column, sort by row - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-by-column-sort-by-row

---

[Skip to main content](https://exceljet.net/formulas/filter-by-column-sort-by-row#main-content)

[](https://exceljet.net/formulas/filter-by-column-sort-by-row#)

*   [Previous](https://exceljet.net/formulas/filter-and-transpose-horizontal-to-vertical)
    
*   [Next](https://exceljet.net/formulas/filter-by-date)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter by column, sort by row
=============================

by Dave Bruns · Updated 27 Jun 2024

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SORT](https://exceljet.net/functions/sort-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6765/download?token=_hY2_vN9)
 (14.66 KB)

![Excel formula: Filter by column, sort by row](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter%20by%20column%20sort%20by%20row.png "Excel formula: Filter by column, sort by row")

Summary
-------

To filter a set of data by a column heading, then sort the result by row, you can use a formula based on the [FILTER](https://exceljet.net/functions/filter-function)
 and [SORT](https://exceljet.net/functions/sort-function)
 functions. In the example shown, the formula in I5 is:

    =SORT(FILTER(B5:G15,(B4:G4="group")+(B4:G4=J4)),2,-1)
    

This formula returns the "Group" column plus data for the year in J4, sorted in descending order by the values in that year. The year in J4 is a dropdown menu created with [data validation](https://exceljet.net/articles/excel-data-validation-guide)
.

Generic formula
---------------

    =SORT(FILTER(data,(heading="group")+(heading=year)),2,-1)

Explanation 
------------

_Note: FILTER is a new [dynamic array](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 function in [Excel 365](https://exceljet.net/glossary/excel-365)
. In other versions of Excel, there are [alternatives](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
, but they are more complex._

In this example, the goal is to filter the data shown in B5:G15 by year, then sort the results in descending order. In addition, the result should include the Group column, sorted in the same way. The problem breaks down into two main steps:

1.  Filter to select the Group and matching Year column
2.  Sort the result in descending order by year values

### Filter by column

To filter the data to select the Group column and data for the matching year, we use the [FILTER function](https://exceljet.net/functions/filter-function)
. Typically FILTER is used to filter data vertically, selecting rows that match provided conditions. However, FILTER can also select data horizontally. The key is to provide logic for the _include_ argument that will return a horizontal array with the same number of columns as the source data. For example, to return data for the year 2017, we can use a formula like this:

    =FILTER(B5:G15,B4:G4=2017)
    

The logical expression:

    =B4:G4=2017
    

returns a one-row [horizontal array](https://exceljet.net/glossary/array)
 with 5 columns:

    {FALSE,FALSE,TRUE,FALSE,FALSE,FALSE}
    

When provided to FILTER as the _include_ [argument](https://exceljet.net/glossary/function-argument)
, FILTER returns the values for 2017 only:

    FILTER(B5:G15,{FALSE,FALSE,TRUE,FALSE,FALSE,FALSE}) // 2017 only
    

To add in the Group column, we extend the logic using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
, a technique for working with TRUE and FALSE values as 1s and 0s. In Boolean algebra, [multiplication corresponds to AND logic, and addition corresponds to OR logic](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
. In this case, we want FILTER to return the Group column and the matching year column. This means we need OR logic - i.e. column = "group" OR column = \[year\].

Using addition for OR logic, we can construct an expression like this:

    =(B4:G4="group")+(B4:G4=2017)
    

This results in two arrays with TRUE and FALSE values, joined by addition:

    {TRUE,FALSE,FALSE,FALSE,FALSE,FALSE} +
    {FALSE,FALSE,TRUE,FALSE,FALSE,FALSE}
    

The math operation of addition coerces the TRUE and FALSE to numbers, and the result is a single array of 1s and 0s:

    {1,0,1,0,0,0}
    

Notice the first and third columns are 1, while the other columns are 0. When this array is provided to FILTER as the _include_ argument, FILTER returns columns 1 and 3 from the data.

### Sort by row

Because the FILTER function is [nested](https://exceljet.net/glossary/nesting)
 inside the [SORT function](https://exceljet.net/functions/sort-function)
. FILTER returns the two matching columns explained above directly to SORT:

    =SORT(filter_result,2,-1)
    

We want to sort these columns by values in the year column (2017) in _descending_ order, so _sort\_index_ is provided as 2, and _sort\_order_ is given as -1. With these inputs, the [SORT function](https://exceljet.net/functions/sort-function)
 returns the sorted as shown in the example. Notice that Group E appears first since 27% is the highest value in 2017.

When the year in J4 is changed, FILTER selects new columns, and the SORT function sorts the new data in the same way.

### Dropdown menu for year

To make the year dropdown menu, you can apply a simple data validation rule to cell J4. The allowed values are based on the existing years in C4:G4, with In-cell dropdown selected:

![Dropdown menu for year with data validation](https://exceljet.net/sites/default/files/images/formulas/inline/dropdown%20menu%20for%20year%20with%20data%20validation.png "Dropdown menu for year with data validation")

Once data validation is in place, a dropdown menu with the years 2016-2020 will appear. If you are new to data validation, see our [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
.

Related formulas
----------------

[![Excel formula: Filter horizontal data](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Filter%20horizontal%20data.png "Excel formula: Filter horizontal data")](https://exceljet.net/formulas/filter-horizontal-data)

### [Filter horizontal data](https://exceljet.net/formulas/filter-horizontal-data)

Note: FILTER is a new dynamic array function in Excel 365 . In other versions of Excel, there are alternatives , but they are more complex. There are ten columns of data in the range C4:L6. The goal is to filter this horizontal data and extract only columns (records) where the group is "fox". For...

[![Excel formula: FILTER to remove columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20to%20remove%20columns.png "Excel formula: FILTER to remove columns")](https://exceljet.net/formulas/filter-to-remove-columns)

### [FILTER to remove columns](https://exceljet.net/formulas/filter-to-remove-columns)

Although FILTER is more commonly used to filter rows, you can also filter columns, the trick is to supply an array with the same number of columns as the source data. In this example, we construct the array we need with boolean logic , also called Boolean algebra. In Boolean algebra, multiplication...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter exclude blank values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20exclude%20blank%20values.png "Excel formula: Filter exclude blank values")](https://exceljet.net/formulas/filter-exclude-blank-values)

### [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)

The FILTER function is designed to extract data that matches one or more criteria. In this case, we want to apply criteria that requires all three columns in the source data (Name, Group, and Room) to have data. In other words, if a row is missing any of these values, we want to exclude that row...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20SORT%20function%20example-Play.png)](https://exceljet.net/videos/basic-sort-function-example)

### [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)

In this video, we’ll look at a basic example of sorting with the SORT function . Sorting with formulas is one of those traditionally hard problems in Excel that new dynamic array formulas have made much easier. In this worksheet, we have a list of names, scores, and groups. Currently the data is...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Filter horizontal data](https://exceljet.net/formulas/filter-horizontal-data)
    
*   [FILTER to remove columns](https://exceljet.net/formulas/filter-to-remove-columns)
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)
    

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