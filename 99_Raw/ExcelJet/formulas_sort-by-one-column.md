# Sort by one column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-by-one-column

---

[Skip to main content](https://exceljet.net/formulas/sort-by-one-column#main-content)

[](https://exceljet.net/formulas/sort-by-one-column#)

*   [Previous](https://exceljet.net/formulas/sort-by-custom-list)
    
*   [Next](https://exceljet.net/formulas/sort-by-substring)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Sort by one column
==================

by Dave Bruns · Updated 27 Aug 2022

Related functions 
------------------

[SORT](https://exceljet.net/functions/sort-function)

![Excel formula: Sort by one column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort%20by%20one%20column_0.png "Excel formula: Sort by one column")

Summary
-------

To sort by one column, you can use the [SORT function](https://exceljet.net/functions/sort-function)
 or [SORTBY function](https://exceljet.net/functions/sortby-function)
. In the example shown, data is sorted by the Group column. The formula in F5 is:

    =SORT(B5:D14,3)
    

Notice data is sorted in ascending order (A-Z) by default.

Generic formula
---------------

    =SORT(data,index,order)

Explanation 
------------

The SORT function requires very little configuration. In the example shown, we want to sort data in B5:D14 by the third column, Group. For _array_, we provide entire range, B5:D14. For _sort\_index_, we provide 3:

    =SORT(B5:D14,3)
    

With this formula in F5, the SORT function outputs the sorted array in F5:H14.

### Ascending vs. Descending

Data is sorted in ascending order (A-Z) by default. This behavior is controlled by an optional third argument, _sort\_order_. The default value for _sort\_order_ is 1, so both formulas below return the same result as shown in the example above:

    =SORT(B5:D14,3)
    =SORT(B5:D14,3,1)
    

To sort in descending (Z-A) order, set sort\_order to -1. In the example below, we are sorting data in _descending order_ by score, which is the second column:

    =SORT(B5:D14,2,-1)
    

![Example - sort by one column in descending order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sort%20by%20one%20column%20descending%20order_0.png?itok=pxqWC-oA "Example - sort by one column in descending order")

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related functions
-----------------

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

### Functions

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