# Random sort - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/random-sort

---

[Skip to main content](https://exceljet.net/formulas/random-sort#main-content)

[](https://exceljet.net/formulas/random-sort#)

*   [Previous](https://exceljet.net/formulas/random-numbers-without-duplicates)
    
*   [Next](https://exceljet.net/formulas/remove-blank-rows)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Random sort
===========

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[SORTBY](https://exceljet.net/functions/sortby-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[ROWS](https://exceljet.net/functions/rows-function)

![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/random_sort.png "Excel formula: Random sort")

Summary
-------

To sort a list or table in a random order, you can use the [SORTBY function](https://exceljet.net/functions/sortby-function)
 with the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
. In the example shown, the formula in D5 is:

    =SORTBY(data,RANDARRAY(ROWS(data)))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16. The result is a new random sort order whenever the worksheet is recalculated.

_Note: this example uses two newer functions in Excel: SORTBY and RANDARRAY. If you are using an older version of Excel, [see this example](https://exceljet.net/formulas/random-sort-formula)
._

Generic formula
---------------

    =SORTBY(range,RANDARRAY(ROWS(range)))

Explanation 
------------

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the [SORTBY function](https://exceljet.net/functions/sortby-function)
 and the [RANDARRAY function](https://exceljet.net/functions/randarray-function)
.

### SORTBY function

The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort data in a completely custom manner. The main requirement of the sort by array(s) is that they have dimensions that are compatible with the data being sorted. In this example, the named range **data** (B5:B16) holds the first 12 letters of the alphabet. That means we need a sort by array that contains 12 values. For example, we can sort the values in **data** in reverse order with a hardcoded [array constant](https://exceljet.net/glossary/array-constant)
 like this:

    =SORTBY(data,{12;11;10;9;8;7;6;5;4;3;2;1})

The semicolons in the array used for sorting indicate a vertical [array](https://exceljet.net/glossary/array)
 in rows, the same as the source data. To generate a random array of numbers to sort with, we need another function.

Video: [Sort by custom list with SORTBY](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

### RANDARRAY function

The RANDARRAY function generates an array of random numbers between two values. The size or the array is determined by _rows_ and _columns_ arguments. To generate 12 random numbers to sort with, we can use the RANDARRAY function together with the [ROWS function](https://exceljet.net/functions/rows-function)
 like this:

    RANDARRAY(ROWS(data))
    

ROWS returns the number of rows in **data**, which in this case is 12. This number goes into the RANDARRAY function as the _rows_ argument, and RANDARRAY returns an array of 12 decimal values like this:

    {0.489071793902109;0.380639786424253;0.12859884623431;0.520000510523814;0.638866975537127;0.105109233209619;0.219291392470457;0.938867459800217;0.782387454565537;0.915924172473614;0.73975376365456;0.50617850806796}
    

_Note: The array above is only an example. Because RANDARRAY generates a new set of random values with every worksheet change, it is difficult to capture the exact values used to sort the array._

### Final formula

Bringing the pieces explained above together, the final formula used in D5 is:

    =SORTBY(data,RANDARRAY(ROWS(data)))

ROWS provides a count of rows to RANDARRAY, which generates a random array of 12 decimal numbers. This array is returned directly to the SORTBY function as the _by\_array1_ argument. SORTBY uses the random values to sort the data, and returns the 12 letters into a [spill range](https://exceljet.net/glossary/spill-range)
 starting in D5.

Video: [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

_Note: RANDARRAY is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and will recalculate every time the worksheet is changed, causing values to be resorted. To stop values from sorting automatically, you can copy the formulas, then use Paste Special > Values to convert formulas to static values._

Related formulas
----------------

[![Excel formula: Sort by one column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20one%20column_0.png "Excel formula: Sort by one column")](https://exceljet.net/formulas/sort-by-one-column)

### [Sort by one column](https://exceljet.net/formulas/sort-by-one-column)

The SORT function requires very little configuration. In the example shown, we want to sort data in B5:D14 by the third column, Group. For array , we provide entire range, B5:D14. For sort\_index , we provide 3: =SORT(B5:D14,3) With this formula in F5, the SORT function outputs the sorted array in...

[![Excel formula: Sort by two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20two%20columns.png "Excel formula: Sort by two columns")](https://exceljet.net/formulas/sort-by-two-columns)

### [Sort by two columns](https://exceljet.net/formulas/sort-by-two-columns)

In the example shown, we want to sort data in B5:D14 first by group in descending order. Here is the configuration needed: array = B5:D14 by\_array1 = D5:D14 sort\_order1 = 1 The formula below will sort data by group A-Z: =SORTBY(B5:D14,D5:D14,1) // sort by group only To extend the formula to sort...

[![Excel formula: Sort by custom list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20custom%20list.png "Excel formula: Sort by custom list")](https://exceljet.net/formulas/sort-by-custom-list)

### [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)

In this example, we are sorting a table with 10 rows and 3 columns. In the range J5:J7 (the named range custom ), the colors "red", "blue", and "green" are listed in the desired sort order. The goal is to sort the table using values in the Group column in this same custom order. The SORTBY function...

Related functions
-----------------

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

[![Excel ROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rows%20function.png "Excel ROWS function")](https://exceljet.net/functions/rows-function)

### [ROWS Function](https://exceljet.net/functions/rows-function)

The Excel ROWS function returns the count of rows in a given reference. For example, ROWS(A1:A3) returns 3, since the range A1:A3 contains 3 rows.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/New%20dynamic%20array%20functions%20in%20Excel-Play.png)](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

### [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

In this video, we'll quickly review new Dynamic Array functions in Excel. With the introduction of dynamic array formulas, Excel includes 6 brand new functions that directly leverage dynamic array behavior. Each of these functions is covered in more detail later in the course, so this is just a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Sort%20by%20custom%20list%20with%20SORTBY-Play.png)](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

### [Sort by custom list with SORTBY](https://exceljet.net/videos/sort-by-custom-list-with-sortby)

In this video, we'll look at how to sort with SORTBY function using a custom list. One challenge that comes up frequently when sorting is a need to sort in a custom order. For example, in this worksheet, we have a list of opportunities, and we want to sort the list in the order that stages appear...

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
    
*   [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)
    

### Functions

*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [ROWS Function](https://exceljet.net/functions/rows-function)
    

### Videos

*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
    
*   [Sort by custom list with SORTBY](https://exceljet.net/videos/sort-by-custom-list-with-sortby)
    

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