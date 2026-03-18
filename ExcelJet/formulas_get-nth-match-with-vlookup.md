# Get nth match with VLOOKUP - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-nth-match-with-vlookup

---

[Skip to main content](https://exceljet.net/formulas/get-nth-match-with-vlookup#main-content)

[](https://exceljet.net/formulas/get-nth-match-with-vlookup#)

*   [Previous](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Next](https://exceljet.net/formulas/get-value-of-last-non-empty-cell)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get nth match with VLOOKUP
==========================

by Dave Bruns · Updated 29 Apr 2025

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Get nth match with VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nth_match_with_VLOOKUP.png "Excel formula: Get nth match with VLOOKUP")

Summary
-------

To get the nth match in a set of data with the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
, you can use a helper column that contains a special calculated lookup value. In the worksheet shown, the formula in cell I7 looks like this:

    =VLOOKUP($I$4&"-"&$H7,data,4,0)
    

Where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:F16. When I4 contains "A", the formula will return the first 5 matches as it is copied down column I, using the numbers in column H for n. A similar formula can be used to return the amount associated with the nth match in cell J7. See below for details. 

> The purpose of this example is to explain how to get the nth match in Excel 2019 and older with VLOOKUP. It is also possible to use a [formula based on INDEX and MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
> . However, in the current version of Excel, the [FILTER function](https://exceljet.net/functions/filter-function)
>  is a much better way to get multiple matching records.

Generic formula
---------------

    =VLOOKUP(id_formula,table,n,0)

Explanation 
------------

The table contains basic order information, with columns for Date, Product, Name, and Amount. The Helper column is used to create a special lookup value, as explained below. The goal is to retrieve the nth matching record in a table for a specific product, which is entered in cell I4. For example, if the value in cell H4 is "A", the formula in I7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in I8 should return 'Juan', since this is the second name associated with product "A". If the product in H4 is changed, the formula should calculate a new result. All data exists in an Excel Table named **data**.

### Helper column

This formula depends on a [helper column](https://exceljet.net/glossary/helper-column)
, which is added as the first column to the source data table. The helper column uses a formula to create a unique ID to use as a lookup value using the product in column D and a counter created with the [COUNTIF function](https://exceljet.net/functions/countif-function)
. The lookup value is created by [concatenating](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the product in I4 to a running count of the product. The formula in B5 is:

    =D5&"-"&COUNTIF($D$5:D5,D5)

This formula picks up the value in D5 and uses the ampersand (&) to concatenate the product to a hyphen (-), and the result from COUNTIF. The COUNTIF function uses an [expanding range](https://exceljet.net/glossary/expanding-reference)
 ($D$5:D5) to generate a [running count](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
 of the product in the table. The values in column B show the results of this formula.

### VLOOKUP function

VLOOKUP is an Excel function to get data from a table organized _vertically_, with lookup values in the _first column_. The data to retrieve is specified by column number, and the generic syntax for VLOOKUP looks like this:

    =VLOOKUP(lookup_value,table_array,column_index_num,range_lookup)

In this example, we use the formulas below to look up the name and amount for each match in the table:

    =VLOOKUP($I$4&"-"&$H7,data,4,0) // name
    =VLOOKUP($I$4&"-"&$H7,data,5,0) // amount

The _lookup\_value_ is the value to search for, and this is the tricky part of this approach. To match the lookup values in column B, we need to create a lookup value in the same format as the IDs we created in the Helper column: a product code joined to a count, separated by a hyphen (i.e., "A-1", "A-2", etc.). To do this, we use the snippet below:

    $I$4&"-"&$H7

Notice the reference to $I$4 is [absolute](https://exceljet.net/glossary/absolute-reference)
 so that it will not change when the formula is copied, while the reference to $H7 is [mixed](https://exceljet.net/glossary/mixed-reference)
 so that the column is locked but the row can change. As the formula is copied down, the _lookup\_value_ increments at each row using the numbers in column H. This is how the formula can return the first match, the second match, and so on.

The _table\_array_ is the [Excel Table](https://exceljet.net/articles/excel-tables)
 named data. Next, we have the column number, which is a number that indicates the column from which we want to retrieve data, where the first column is column 1 and contains lookup values. To get the Name, we use 4 for _column\_index\_num,_ and to get the Amount, we use 5. Finally, we have the last argument, range\_lookup, for which we provide zero (0). Using zero (0) tells VLOOKUP to find an _exact match_ for the ID. If the exact ID isn't found, VLOOKUP will return the #N/A error.

As the VLOOKUP formulas are copied down, they return the first five matches for Product A as shown in the worksheet. In cells I7 and J7, the lookup values and results look like this:

    =VLOOKUP("A-1",data,4,0) // returns "John"
    =VLOOKUP("A-1",data,5,0) // returns 100

In cells I8 and J8, we have:

    =VLOOKUP("A-2",data,4,0) // returns "Juan"
    =VLOOKUP("A-2",data,5,0) // returns 120

And so on, as the formula is copied down.

For more information about VLOOKUP, see: [How to use the VLOOKUP function](https://exceljet.net/functions/vlookup-function)
.

Related formulas
----------------

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

### [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the named range value . The core of the solution explained below is the COUNTIF function , with help from the IF function to suppress a count for...

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)
    
*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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