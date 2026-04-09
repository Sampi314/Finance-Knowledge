# Unique rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/unique-rows

---

[Skip to main content](https://exceljet.net/formulas/unique-rows#main-content)

[](https://exceljet.net/formulas/unique-rows#)

*   [Previous](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)
    
*   [Next](https://exceljet.net/formulas/unique-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Unique rows
===========

by Dave Bruns · Updated 30 Jul 2021

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[SORT](https://exceljet.net/functions/sort-function)

![Excel formula: Unique rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/unique%20rows.png "Excel formula: Unique rows")

Summary
-------

To extract a list of unique rows from a set of data, you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 together with the [SORT function](https://exceljet.net/functions/sort-function)
. In the example shown, the formula in E5 is:

    =SORT(UNIQUE(B5:C15))
    

which return the 6 unique rows in the range B5:C15, sorted by group.

Generic formula
---------------

    =SORT(UNIQUE(range))

Explanation 
------------

In this example, the goal is to extract a list of unique rows from the range B5:C15. The easiest way to do this is to use the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
.

By default, UNIQUE will extract unique values in rows, so there is no special configuration needed. Working from the inside out, we give UNIQUE the full range of data, including the Group and Color columns:

    UNIQUE(B5:C15)
    

The UNIQUE function evaluates all 11 rows and returns the 6 unique rows in an unsorted [two-dimensional array](https://exceljet.net/glossary/array)
 that looks like this:

    {"a","red";"c","blue";"a","blue";"b","red";"d","red";"b","blue"}
    

This array is returned directly to the [SORT function](https://exceljet.net/functions/sort-function)
:

    =SORT({"a","red";"c","blue";"a","blue";"b","red";"d","red";"b","blue"})
    

By default, SORT will sort based on the first column in the data. The result is the same array, sorted by Group:

    {"a","red";"a","blue";"b","red";"b","blue";"c","blue";"d","red"}
    

UNIQUE is a [dynamic function](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. If any data in B5:C15 changes, the output from UNIQUE will update immediately.

### Dynamic source range

UNIQUE won't automatically adjust the _source range_ if data is added or deleted. To give UNIQUE a range that will automatically resize as needed, use an [Excel Table](https://exceljet.net/articles/excel-tables)
 or create a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
 with a formula.

Related formulas
----------------

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

[![Excel formula: Distinct values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/distinct%20values.png "Excel formula: Distinct values")](https://exceljet.net/formulas/distinct-values)

### [Distinct values](https://exceljet.net/formulas/distinct-values)

This example uses the UNIQUE function . With default settings, UNIQUE will output a list of unique values, i.e. values that appear one or more times in the source data. However, UNIQUE has an optional third argument, called occurs\_once that, when set to TRUE, will cause UNIQUE to return only values...

[![Excel formula: Count unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values.png "Excel formula: Count unique values")](https://exceljet.net/formulas/count-unique-values)

### [Count unique values](https://exceljet.net/formulas/count-unique-values)

This example uses the UNIQUE function to extract unique values. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. These are returned directly to the COUNTA function as an array like this: =COUNTA({"red";"amber";"green";"blue";"...

[![Excel formula: Unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values.png "Excel formula: Unique values")](https://exceljet.net/formulas/unique-values)

### [Unique values](https://exceljet.net/formulas/unique-values)

This example uses the UNIQUE function, which is fully automatic. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. UNIQUE is a dynamic function. If any data in B5:B16 changes, the output from UNIQUE will update immediately...

Related functions
-----------------

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

*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    
*   [Distinct values](https://exceljet.net/formulas/distinct-values)
    
*   [Count unique values](https://exceljet.net/formulas/count-unique-values)
    
*   [Unique values](https://exceljet.net/formulas/unique-values)
    

### Functions

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