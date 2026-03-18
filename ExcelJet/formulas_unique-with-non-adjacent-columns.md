# UNIQUE with non-adjacent columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/unique-with-non-adjacent-columns

---

[Skip to main content](https://exceljet.net/formulas/unique-with-non-adjacent-columns#main-content)

[](https://exceljet.net/formulas/unique-with-non-adjacent-columns#)

*   [Previous](https://exceljet.net/formulas/unique-values-with-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/xlookup-match-any-column)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

UNIQUE with non-adjacent columns
================================

by Dave Bruns · Updated 26 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[SORT](https://exceljet.net/functions/sort-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6198/download?token=ONo7v4Dl)
 (14.53 KB)

![Excel formula: UNIQUE with non-adjacent columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/unique%20with%20non-adjacent%20columns.png "Excel formula: UNIQUE with non-adjacent columns")

Summary
-------

To extract unique values from non-adjacent columns in a set of data, you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
, with help from the [FILTER function](https://exceljet.net/functions/filter-function)
 to remove unwanted columns.  In the example shown, the formula in G5 is:

    =SORT(UNIQUE(FILTER(data,{1,0,1})))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:D15. The result is a list of unique pairs of color and region, sorted by color.

Generic formula
---------------

    =SORT(UNIQUE(FILTER(data,arrayconstant)))

Explanation 
------------

Although FILTER is commonly used to filter rows, you can also filter columns. The trick is to use an _include_ argument that operates on columns instead of rows. In this example, we use a hard-coded [array constant](https://exceljet.net/glossary/array-constant)
 to filter out unwanted columns, but [you can also use a logical expression](https://exceljet.net/formulas/filter-to-remove-columns)
 that returns the same kind of array in a dynamic way. Note: the [named range](https://exceljet.net/glossary/named-range)
 **data** is used for convenience only; a regular range reference will also work fine.

Working from the inside out, the [FILTER function](https://exceljet.net/functions/filter-function)
 is used to filter out the middle column, "Qty", like this:

    FILTER(data,{1,0,1}) // remove middle column
    

The array constant {1,0,1} is what does the actual filtering, and notice this is a horizontal [array](https://exceljet.net/glossary/array)
, separated by commas. The result from FILTER is a two-dimensional array with 2 columns and 11 rows like this:

    {"Red","East";
    "Blue","South";
    "Green","North";
    "Red","North";
    "Blue","East";
    "Green","North";
    "Red","North";
    "Blue","South";
    "Green","North";
    "Red","North";
    "Blue","East"}
    

Notice data in the "Qty" column has been removed. This array is delivered to the [UNIQUE function](https://exceljet.net/functions/unique-function)
, which can automatically extract unique values from data with adjacent columns. The UNIQUE function returns a smaller two-dimensional array with 2 columns and 5 rows like this:

    {"Red","East";
    "Blue","South";
    "Green","North";
    "Red","North";
    "Blue","East"}
    

Notice this array contains only the unique combinations of Color and Region. This smaller array is then handed off to the [SORT function](https://exceljet.net/functions/sort-function)
, which returns the same data, sorted by Color, as seen in the example. The SORT function is optional and can be removed.

This is a nice example of [nesting](https://exceljet.net/glossary/nesting)
 one function inside another. When you see a formula created this way, learn to read from the inside out. The inner functions deliver values to the outer functions. The outermost function returns the final result.

Related formulas
----------------

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

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [FILTER to remove columns](https://exceljet.net/formulas/filter-to-remove-columns)
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    

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