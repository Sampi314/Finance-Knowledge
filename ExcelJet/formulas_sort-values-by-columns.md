# Sort values by columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-values-by-columns

---

[Skip to main content](https://exceljet.net/formulas/sort-values-by-columns#main-content)

[](https://exceljet.net/formulas/sort-values-by-columns#)

*   [Previous](https://exceljet.net/formulas/sort-text-by-length)
    
*   [Next](https://exceljet.net/formulas/sum-numbers-with-text)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Sort values by columns
======================

by Dave Bruns · Updated 18 Dec 2020

Related functions 
------------------

[SORT](https://exceljet.net/functions/sort-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

![Excel formula: Sort values by columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort%20values%20by%20columns.png "Excel formula: Sort values by columns")

Summary
-------

To sort values by columns, you can use the [SORT function](https://exceljet.net/functions/sort-function)
. In the example shown, data is sorted by the Group column. The formula in C8 is:

    =SORT(C4:L5,2,-1,TRUE)
    

The result is the range C4:L5 sorted by score in descending order.

Generic formula
---------------

    =SORT(data,index,order,TRUE)

Explanation 
------------

The SORT function sorts a range using a given index, called _sort\_index_. Normally, this index represents a column in the source data.

However, the SORT function has an optional argument called "_by\_col_" which allows sorting values organized in columns. To sort by column, this argument must be set to TRUE, which tells the SORT function that _sort\_index_ represents a row.

In this case, we want to sort the data by Score, which appears in the second row, so we use a sort\_index of 2. The SORT function that appears in C8 is configured like this:

    =SORT(C4:L5,2,-1,TRUE)
    

*   _array_ is the data in the range C4:L5
*   _sort\_index_ is 2, since score is in the second row
*   _sort\_order_ is -1, since we want to sort in descending order
*   _by\_col_ is TRUE, since data is organized in columns

The SORT function returns the sorted array into the range C8:L9. This result is dynamic; if any scores in the source data change, the results will automatically update.

### With SORTBY

The [SORTBY function](https://exceljet.net/functions/sortby-function)
 can also be used to solve this problem. With SORTBY, the equivalent formula is:

    =SORTBY(C4:L5,C5:L5,-1)
    

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Sort by one column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20one%20column_0.png "Excel formula: Sort by one column")](https://exceljet.net/formulas/sort-by-one-column)

### [Sort by one column](https://exceljet.net/formulas/sort-by-one-column)

The SORT function requires very little configuration. In the example shown, we want to sort data in B5:D14 by the third column, Group. For array , we provide entire range, B5:D14. For sort\_index , we provide 3: =SORT(B5:D14,3) With this formula in F5, the SORT function outputs the sorted array in...

Related functions
-----------------

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sort by one column](https://exceljet.net/formulas/sort-by-one-column)
    

### Functions

*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    

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