# Sort by two columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-by-two-columns

---

[Skip to main content](https://exceljet.net/formulas/sort-by-two-columns#main-content)

[](https://exceljet.net/formulas/sort-by-two-columns#)

*   [Previous](https://exceljet.net/formulas/sort-by-substring)
    
*   [Next](https://exceljet.net/formulas/sort-text-by-length)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Sort by two columns
===================

by Dave Bruns · Updated 26 Aug 2022

Related functions 
------------------

[SORTBY](https://exceljet.net/functions/sortby-function)

![Excel formula: Sort by two columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort%20by%20two%20columns.png "Excel formula: Sort by two columns")

Summary
-------

To sort by two columns, you can use the [SORTBY function](https://exceljet.net/functions/sortby-function)
. In the example shown, data is sorted first by the Group column in ascending order, then by the Score column in descending order. The formula in F5 is:

    =SORTBY(B5:D14,D5:D14,1,C5:C14,-1)
    

The result is data sorted by group, then by score, with highest scores appearing first.

Generic formula
---------------

    =SORTBY(data,col1,order,col2,order)

Explanation 
------------

In the example shown, we want to sort data in B5:D14 first by group in descending order. Here is the configuration needed:

*   _array_ = B5:D14
*   _by\_array1_ = D5:D14
*   _sort\_order1_ = 1

The formula below will sort data by group A-Z:

    =SORTBY(B5:D14,D5:D14,1) // sort by group only
    

To extend the formula to sort next by score, in descending order, we need to add:

*   _by\_array2_ = C5:C14
*   _sort\_order2_ = -1

With these arguments added, the complete formula is:

    =SORTBY(B5:D14,D5:D14,1,C5:C14,-1)
    

### Ascending vs. Descending

Data is sorted in ascending order (A-Z) by default. This behavior is controlled by the _sort\_order_ arguments. _Sort\_order_ can be set to 1 (ascending) or -1 (descending). The formula below is the same as above except that it sorts scores in ascending order:

    =SORTBY(B5:D14,D5:D14,1,C5:C14,1)
    

![Example - sort by two columns in ascending order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sort%20by%20two%20columns%20acending%20order.png?itok=j2xs-xt8 "Example - sort by two columns in ascending order")

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