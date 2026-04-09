# Filter and exclude columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-and-exclude-columns

---

[Skip to main content](https://exceljet.net/formulas/filter-and-exclude-columns#main-content)

[](https://exceljet.net/formulas/filter-and-exclude-columns#)

*   [Previous](https://exceljet.net/formulas/extract-numbers-from-text)
    
*   [Next](https://exceljet.net/formulas/filter-and-sort-without-errors)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Filter and exclude columns
==========================

by Dave Bruns · Updated 11 Jul 2024

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SORT](https://exceljet.net/functions/sort-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

[TAKE](https://exceljet.net/functions/take-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8423/download?token=efwjQnMD)
 (32.08 KB)

![Excel formula: Filter and exclude columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/filter_and_exclude_columns.png "Excel formula: Filter and exclude columns")

Summary
-------

The goal is to display high-value projects in a simple table. To filter data and remove unwanted columns in one step, you can use a formula based on the [FILTER](https://exceljet.net/functions/filter-function)
 and [CHOOSECOLS](https://exceljet.net/functions/choosecols-function)
 functions, with help from the [SORT function](https://exceljet.net/functions/sort-function)
 as needed. In the example shown, the formula in F4 is:

    =CHOOSECOLS(SORT(FILTER(B9:G20,E9:E20>90000),4,-1),1,4)
    

The result is a small list of projects with a value of over 90,000, with only two columns out of the original six. The SORT function is used to sort the projects in descending order by value. See below for another slightly simpler formula option based on the [TAKE function](https://exceljet.net/functions/take-function)
.

Generic formula
---------------

    =CHOOSECOLS(SORT(FILTER(data,criteria)),1,n)

Explanation 
------------

In this example, the goal is to use a single formula to extract high-value projects and list them in a simple table. We also want to remove unnecessary columns to create a clean, uncluttered view. The solutions explained below are based on a combination of several functions in Excel, including FILTER, SORT, TAKE, and CHOOSECOLS. This is a useful technique for creating a simple dashboard report with a dynamic set of data. The beauty of this approach is that the original data remains untouched and can be easily updated at any time. In addition, the source data can be located on a different worksheet. You can use this same idea in many ways, for example:

*   Create a summary of top-selling products for the current month.
*   Create a sales performance dashboard to highlight top-performing sales representatives.
*   Create a list of the largest outstanding invoices over 30 days due.
*   Create a leaderboard to display the most productive groups or employees.

The article below describes two methods to solve this challenge. The first method uses the FILTER function to extract data of interest. This is the best approach when the logic needed to select important data is more complex. The second approach uses the TAKE function to grab the most important records after sorting. This is an elegant way to build a summary of the "Top n projects", "Top 5 outstanding payments", etc.

### Method 1: FILTER, SORT, and CHOOSECOLS

The first method to filter and exclude columns is based on the FILTER, SORT, and CHOOSECOLS functions. This is the solution shown in the workbook above, where the formula in cell F4 is:

    =CHOOSECOLS(SORT(FILTER(B9:G20,E9:E20>90000),4,-1),1,4)

Working from the inside out, the [FILTER function](https://exceljet.net/functions/filter-function)
 is configured to extract projects with a value over 90,000 like this:

    =FILTER(B9:G20,E9:E20>90000)

*   _array_ - provided as all data in B9:G20.
*   _include_ - provided as the logical expression E9:E20>90000.
*   _if\_empty_ - Not provided.

The advantage of using FILTER is that we can configure the logic used to select data to apply even [complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
. This is a more powerful way to isolate important information compared to sorting only.

In the next step, FILTER returns a filtered array of data to the SORT function, which is configured to sort the data by value in descending order:

    SORT(FILTER(...),4,-1)

*   _array_ - delivered by FILTER.
*   _sort\_index_ - provided as 4 to sort by Value.
*   _sort\_order_ - provided as -1 to sort in descending order.

The last step is to remove any columns we don't want in the final output, which is done with the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
:

    =CHOOSECOLS(SORT(...),1,4)

*   _array_ - provided by SORT.
*   _col\_num1_ - provided as 1 to extract Project.
*   _col\_num2_ - provided as 4 to extract Value.

CHOOSECOLS is a simple function designed to select specific columns from a set of data by index number. In this case, we want to retain column 1 (Project) and column 4 (Value) so we provide 1 and 4.

_Note: We could sort the data before filtering with the same result. However, using FILTER first is more efficient since we are only sorting records that meet our criteria._

### Method 2: SORT, TAKE, and CHOOSECOLS

Another way to filter and exclude columns is to use the TAKE function instead of the FILTER function. This approach makes sense when sorting alone is enough to "surface" the most important data. Once we have data sorted in the preferred order, we use the TAKE function to collect the number of rows desired. For example, to list the top 3 projects by value, we can use a formula like this:

    =CHOOSECOLS(TAKE(SORT(B9:G20,4,-1),3),1,4)

You can see the result in the worksheet below:

![Solving the problem with SORT, TAKE, and CHOOSECOLS](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/filter_and_exclude_columns_with_sort_and_take.png "Solving the problem with SORT, TAKE, and CHOOSECOLS")

In the first step, the [SORT function](https://exceljet.net/functions/sort-function)
 is configured to sort all projects by value in descending order like this:

    SORT(B9:G20,4,-1)

*   _array_ - provided as B9:G20 (12 rows)
*   _sort\_index_ - provided as 4 to sort by Value.
*   _sort\_order_ - provided as -1 to sort in descending order.

In the next step, SORT returns a sorted array of data to the [TAKE function](https://exceljet.net/functions/take-function)
, which is configured to extract the first 3 rows:

    TAKE(SORT(...),3)

*   _array_ - delivered by SORT.
*   _rows_ - provided as 3.

The last step is to remove any columns we don't want in the final output, which is done with the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 as before. Because we want to retain column 1 (Project) and column 4 (Value), we provide 1 and 4:

    =CHOOSECOLS(TAKE(...),1,4)

*   _array_ - provided by TAKE.
*   _col\_num1_ - provided as 1 to extract Project.
*   _col\_num2_ - provided as 4 to extract Value.

### Conclusion

In this article, we looked at two ways to filter and exclude columns from a dataset in Excel using a combination of FILTER, SORT, TAKE, and CHOOSECOLS functions. These techniques are useful for creating simple, dynamic summaries that update automatically as the source data changes.

*   Use the FILTER method when you need to apply more complex logic to select data. FILTER is an excellent tool for identifying and isolating important information based on multiple criteria.
*   Use the TAKE method when sorting alone is enough to surface data of interest. This method is ideal for creating summaries like "Top 3 projects" or "Top 5 outstanding payments." TAKE is also a good choice when you want to limit the number of records displayed.

In the example shown, both methods work well. But note that if more rows were returned by FILTER, more rows would appear in the final result, so we would need to make room for this additional information.

### Wait, what about Pivot Tables?

Yes, you can definitely solve this challenge with a Pivot Table as well. In fact, the workbook attached to this article has a working Pivot Table on Sheet3. Until a couple of years ago, Pivot Tables were the _best_ way to solve this challenge. These days, the main reason to use a Pivot Table instead of a formula is that you are working in an older version of Excel without modern functions like FILTER, SORT, TAKE, and CHOOSECOLS. The main disadvantage of a Pivot Table is that it won't refresh automatically when data changes; you will need to refresh manually. In contrast, a formula-based table will recalculate when any data changes. For more information on Pivot Tables, see:

*   [Excel Pivot Tables](https://exceljet.net/articles/excel-pivot-tables)
     (overview)
*   [Why Pivot Tables](https://exceljet.net/videos/why-pivot-tables)
     (video)

_Note:_ _The video above is now somewhat dated because new functions have made it much easier to summarize data in Excel. In addition, two brand new functions, [GROUPBY](https://exceljet.net/functions/groupby-function)
 and [PIVOTBY](https://exceljet.net/functions/pivotby-function)
, directly mimic Pivot Table functionality__._

Related formulas
----------------

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

[![Excel formula: Filter by column, sort by row](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20by%20column%20sort%20by%20row.png "Excel formula: Filter by column, sort by row")](https://exceljet.net/formulas/filter-by-column-sort-by-row)

### [Filter by column, sort by row](https://exceljet.net/formulas/filter-by-column-sort-by-row)

Note: FILTER is a new dynamic array function in Excel 365 . In other versions of Excel, there are alternatives , but they are more complex. In this example, the goal is to filter the data shown in B5:G15 by year, then sort the results in descending order. In addition, the result should include the...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

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

*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)
    
*   [Filter by column, sort by row](https://exceljet.net/formulas/filter-by-column-sort-by-row)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

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