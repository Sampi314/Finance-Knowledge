# Sort text by length - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-text-by-length

---

[Skip to main content](https://exceljet.net/formulas/sort-text-by-length#main-content)

[](https://exceljet.net/formulas/sort-text-by-length#)

*   [Previous](https://exceljet.net/formulas/sort-by-two-columns)
    
*   [Next](https://exceljet.net/formulas/sort-values-by-columns)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Sort text by length
===================

by Dave Bruns · Updated 18 Dec 2020

Related functions 
------------------

[SORTBY](https://exceljet.net/functions/sortby-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Sort text by length](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort%20text%20by%20length.png "Excel formula: Sort text by length")

Summary
-------

To sort text strings by length in ascending or descending order, you can use a formula based on the SORTBY and LEN functions. In the example shown, the formula in D5 is:

    =SORTBY(B5:B15,LEN(B5:B15),-1)
    

which sorts the text values in column B by string length, in descending order.

Generic formula
---------------

    =SORTBY(data,LEN(data),-1)

Explanation 
------------

The [SORTBY function](https://exceljet.net/functions/sortby-function)
 can sort values in a range with an [array](https://exceljet.net/glossary/array)
 that doesn't exist on the worksheet.

In this example, we want to sort the values in B5:B15 by the number of characters each string contains. Working from inside out, we use the LEN function to get the length of each value:

    LEN(B5:B15) // get length of all strings
    

Because we give LEN an array with 11 values, we get an array with 11 lengths:

    {5;7;14;6;5;13;9;4;8;6;11}
    

Each number represents the character length of a value in B5:B11.

This array is returned directly to the SORTBY function as the _by\_array1_ argument:

    =SORTBY(B5:B15,{5;7;14;6;5;13;9;4;8;6;11},-1)
    

The SORTBY function allows sorting based on one or more "sort by" arrays, as long as dimensions are compatible with the source data. In this case, there are 11 rows in the source data, and 11 rows in the array returned by LEN, so the requirement is met.

The SORTBY function uses the array of lengths returned by LEN to sort the values in B5:B15, and returns sorted results to D5 in a [dynamic array](https://exceljet.net/glossary/dynamic-array)
. Because the sort order is set to -1, the values are sorted in reverse (descending) order by length. Use a positive 1 to sort in ascending order.

> [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
>  are available in [Office 365](https://www.office.com/)
>  only.

Related formulas
----------------

[![Excel formula: Sort by one column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20one%20column_0.png "Excel formula: Sort by one column")](https://exceljet.net/formulas/sort-by-one-column)

### [Sort by one column](https://exceljet.net/formulas/sort-by-one-column)

The SORT function requires very little configuration. In the example shown, we want to sort data in B5:D14 by the third column, Group. For array , we provide entire range, B5:D14. For sort\_index , we provide 3: =SORT(B5:D14,3) With this formula in F5, the SORT function outputs the sorted array in...

[![Excel formula: Sort by two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20two%20columns.png "Excel formula: Sort by two columns")](https://exceljet.net/formulas/sort-by-two-columns)

### [Sort by two columns](https://exceljet.net/formulas/sort-by-two-columns)

In the example shown, we want to sort data in B5:D14 first by group in descending order. Here is the configuration needed: array = B5:D14 by\_array1 = D5:D14 sort\_order1 = 1 The formula below will sort data by group A-Z: =SORTBY(B5:D14,D5:D14,1) // sort by group only To extend the formula to sort...

[![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random_sort.png "Excel formula: Random sort")](https://exceljet.net/formulas/random-sort)

### [Random sort](https://exceljet.net/formulas/random-sort)

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the SORTBY function and the RANDARRAY function . SORTBY function The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort...

[![Excel formula: Sort by custom list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20custom%20list.png "Excel formula: Sort by custom list")](https://exceljet.net/formulas/sort-by-custom-list)

### [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)

In this example, we are sorting a table with 10 rows and 3 columns. In the range J5:J7 (the named range custom ), the colors "red", "blue", and "green" are listed in the desired sort order. The goal is to sort the table using values in the Group column in this same custom order. The SORTBY function...

Related functions
-----------------

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

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
    
*   [Sort by two columns](https://exceljet.net/formulas/sort-by-two-columns)
    
*   [Random sort](https://exceljet.net/formulas/random-sort)
    
*   [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)
    

### Functions

*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

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