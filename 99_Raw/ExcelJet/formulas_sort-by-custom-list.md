# Sort by custom list - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-by-custom-list

---

[Skip to main content](https://exceljet.net/formulas/sort-by-custom-list#main-content)

[](https://exceljet.net/formulas/sort-by-custom-list#)

*   [Previous](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)
    
*   [Next](https://exceljet.net/formulas/sort-by-one-column)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Sort by custom list
===================

by Dave Bruns · Updated 26 Aug 2022

Related functions 
------------------

[SORTBY](https://exceljet.net/functions/sortby-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Sort by custom list](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort%20by%20custom%20list.png "Excel formula: Sort by custom list")

Summary
-------

To sort a list in a custom order, you can combine the [SORTBY function](https://exceljet.net/functions/sortby-function)
 with the [MATCH function](https://exceljet.net/functions/match-function)
. In the example shown, The table is being sorted by the "group" column using in the order shown in cells J5:J7. The formula in D5 is:

    =SORTBY(B5:D14,MATCH(D5:D14,custom,0))
    

where **custom** is the [named range](https://exceljet.net/glossary/named-range)
 J5:J7 that defines desired sort order.

Generic formula
---------------

    =SORTBY(rng,MATCH(rng,custom,0))

Explanation 
------------

In this example, we are sorting a table with 10 rows and 3 columns. In the range J5:J7 (the [named range](https://exceljet.net/glossary/named-range)
 **custom**), the colors "red", "blue", and "green" are listed in the desired sort order. The goal is to sort the table using values in the Group column in this same custom order.

The SORTBY function allows sorting based on one or more "sort by" arrays, as long as dimensions are compatible with the source data. In this case, we can't use the named range **custom** directly in SORTBY, because it only contains 3 rows while the table contains 10 rows.

However, to create an array with 10 rows that can be used as a "sort by" array, we can use the MATCH function like this:

    MATCH(D5:D14,custom,0)
    

Notice we are passing in the Group values in D5:D14 as lookup values, and using **custom** as the lookup table. The result is an [array](https://exceljet.net/glossary/array)
 like this:

    {2;1;3;3;2;3;1;2;3;1}
    

Each value in the array represents the numeric position of given group value in **custom**, so there are 10 rows represented. This array is passed into the SORTBY function as the _by\_array1_ argument. SORTBY sorts the table in the "red", "blue", "green" order and returns the result as a [spill range](https://exceljet.net/glossary/spill-range)
 starting in cell D5.

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

[![Excel formula: Sort text by length](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20text%20by%20length.png "Excel formula: Sort text by length")](https://exceljet.net/formulas/sort-text-by-length)

### [Sort text by length](https://exceljet.net/formulas/sort-text-by-length)

The SORTBY function can sort values in a range with an array that doesn't exist on the worksheet. In this example, we want to sort the values in B5:B15 by the number of characters each string contains. Working from inside out, we use the LEN function to get the length of each value: LEN(B5:B15) //...

Related functions
-----------------

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

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
    
*   [Sort text by length](https://exceljet.net/formulas/sort-text-by-length)
    

### Functions

*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

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