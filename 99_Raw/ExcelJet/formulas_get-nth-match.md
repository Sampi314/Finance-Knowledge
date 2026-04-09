# Get nth match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-nth-match

---

[Skip to main content](https://exceljet.net/formulas/get-nth-match#main-content)

[](https://exceljet.net/formulas/get-nth-match#)

*   [Previous](https://exceljet.net/formulas/get-location-of-value-in-2d-array)
    
*   [Next](https://exceljet.net/formulas/get-nth-match-with-index-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Get nth match
=============

by Dave Bruns · Updated 12 Jun 2023

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[INDEX](https://exceljet.net/functions/index-function)

[CHOOSEROWS](https://exceljet.net/functions/chooserows-function)

[SMALL](https://exceljet.net/functions/small-function)

[IF](https://exceljet.net/functions/if-function)

[MIN](https://exceljet.net/functions/min-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Get nth match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_nth_match.png "Excel formula: Get nth match")

Summary
-------

To get the nth matching record in a set of data, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 with the [INDEX function](https://exceljet.net/functions/index-function)
. In the example shown, the formula in cell G8 is:

    =INDEX(FILTER(data,data[Product]=H4),H5)

Where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:E16. When H4 contains "A" and H5 contains 3, the result will be the 3rd record in the table where the product is "A".

Generic formula
---------------

    =INDEX(FILTER(range,logical_test),n)

Explanation 
------------

The goal is to retrieve the nth matching record in a set of data, after filtering on a specific product. In the worksheet shown, the product in H4 and the value for **n** in H5 are inputs that can be changed at any time. For instance, if the product in H4 is "A" and the value in H5 is 3, the formula should return the 3rd record in the table where the product is "A", as shown in the screen above. This can be accomplished with the FILTER function and the INDEX function.

### FILTER function

The [FILTER function](https://exceljet.net/functions/filter-function)
 "filters" data based on a logical test and extracts matching records. The generic syntax for FILTER looks like this:

    =FILTER(array,include,[if_empty])

The _array_ is the data to filter, and the _include_ argument is the logical expression to use when filtering. The _if\_empty_ parameter specifies the value to return if no matches are found. Note that by itself, FILTER returns all matching data. For example, if we configure FILTER to match on product "A", it will extract all 5 matching records as seen below:

![Example of FILTER to extract all matching records](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/get_nth_match_filter_example_all_matches.png "Example of FILTER to extract all matching records")

To just return the nth record from this data, we need another function.

### INDEX function

    =INDEX(FILTER(data,data[Product]="A",n)

The [INDEX function](https://exceljet.net/functions/index-function)
 returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The generic syntax for INDEX looks like this:

    =INDEX(array,row_num,[col_num])

In this case, we only need to provide a row number to get back the nth match returned by FILTER. To get the 3rd match for product "A", we nest the FILTER function inside INDEX for _array_, then supply 3 for _row\_num_:

    =INDEX(FILTER(data,data[Product]="A"),3)

To complete the formula as shown, we need to replace the hard-coded reference for product and column number with H4 and H5:

    =INDEX(FILTER(data,data[Product]=H4),H5)

Now when a different product is entered in cell H4, or a different value for n is entered in cell H5, the formula will return a new result.

### CHOOSEROWS function

The [CHOOSEROWS function](https://exceljet.net/functions/chooserows-function)
, a more recent addition to Excel, is designed to return one or more rows from a range or array. As an alternative to INDEX, we can use the CHOOSEROWS function to solve this problem like this:

    =CHOOSEROWS(FILTER(data,data[Product]=H4),H5)

This formula returns the same result as the INDEX version above.

### Older versions of Excel

In older versions of Excel without the FILTER function, you can use a more complicated formula like this:

    =INDEX(data,SMALL(IF(data[Product]=H4,ROW(data)-MIN(ROW(data))+1),H5),0)

_This is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter in Excel 2019 and older._

The generic form of this formula looks like this:

    =INDEX(rng,SMALL(IF(rng=value,ROW(rng)-MIN(ROW(rng))+1),n)

The core of this formula is the [SMALL function](https://exceljet.net/functions/small-function)
, which returns the nth smallest value in an array of numeric values. In this case, the array provided to SMALL represents row numbers created with this part of the formula:

    IF(data[Product]=H4,ROW(data)-MIN(ROW(data))+1)

Essentially, IF applies a filter based on the product in cell H4, then returns the corresponding row number from an array of row numbers created with this code:

    ROW(list)-MIN(ROW(list))+1
    

Because the table contains 12 rows of data, the result is an array like this:

    {1;2;3;4;5;6;7;8;9;10;11;12}

See [this page](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
 for a full explanation of the code to create row numbers in Legacy Excel. Putting it all together, SMALL returns the 3rd smallest row number that corresponds with "A" products:

    SMALL(IF(data[Product]=H4,{1;2;3;4;5;6;7;8;9;10;11;12}),H5)

With "A" in cell H4, the result is 5. Simplifying, the original formula becomes:

    =INDEX(data,5,0)

And INDEX returns row 5 from the data. Note: (1) in older versions of Excel, the zero for _col\_num_ is required to [return an entire row](https://exceljet.net/formulas/look-up-entire-row)
 of data. (2) To display the entire row, enter the formula as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
 across all 4 cells simultaneously.

Related formulas
----------------

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel CHOOSEROWS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20chooserows%20function.png "Excel CHOOSEROWS function")](https://exceljet.net/functions/chooserows-function)

### [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)

The Excel CHOOSEROWS function returns specific rows from an array or range. The rows to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a row in the given array.

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20get%20nth%20values%20with%20SMALL%20and%20LARGE_thumb.png)](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

In this video we'll look at how to calculate the "nth" smallest or largest values in a range using the SMALL or LARGE function s. This would be, for example, the 1st, 2nd, and 3rd smallest or largest values. In this first sheet, we have a list of students with five test scores. I'll use the LARGE...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

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
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [CHOOSEROWS Function](https://exceljet.net/functions/chooserows-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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