# Biggest gainers and losers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/biggest-gainers-and-losers

---

[Skip to main content](https://exceljet.net/formulas/biggest-gainers-and-losers#main-content)

[](https://exceljet.net/formulas/biggest-gainers-and-losers#)

*   [Previous](https://exceljet.net/formulas/basic-filter-example)
    
*   [Next](https://exceljet.net/formulas/combine-data-in-multiple-worksheets)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Biggest gainers and losers
==========================

by Dave Bruns · Updated 11 Jul 2024

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[LARGE](https://exceljet.net/functions/large-function)

[SMALL](https://exceljet.net/functions/small-function)

[SORT](https://exceljet.net/functions/sort-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6996/download?token=S3KxF0pv)
 (16.47 KB)

![Excel formula: Biggest gainers and losers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/biggest%20gainers%20and%20losers.png "Excel formula: Biggest gainers and losers")

Summary
-------

To list the top 3 gainers or losers from a set of data that contains a start and end value, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with the [LARGE](https://exceljet.net/functions/large-function)
 and [SMALL](https://exceljet.net/functions/small-function)
 functions. In the example shown, the formula in G5 is:

    =SORT(FILTER(data,data[Change]>=LARGE(data[Change],3)),4,-1)
    

where **data** is the [Excel Table](https://exceljet.net/glossary/excel-table)
 in B5:E16. A similar formula in G12 returns the 3 biggest losers. These results are dynamic and will immediately update if data changes. Read below for a detailed explanation of both formulas.

_Note: [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 are only available in [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2021._ 

Explanation 
------------

In this example, the goal is to display the biggest 3 gainers and losers in a set of data where Start and End columns contain values at two points in time, and Change contains the percentage change in the values. The data in B5:E16 is defined as an [Excel Table](https://exceljet.net/articles/excel-tables)
 with the name **data**. Two formulas are required, one to return the top 3 gainers in the table, and one to return the top 3 losers. The primary component of the solution is the FILTER function, which is used to extract data that meets specific [logical conditions](https://exceljet.net/glossary/logical-test)
 from the table.

If you are new to FILTER, see this video: [Basic FILTER function example](https://exceljet.net/formulas/basic-filter-example)

### Top 3 gainers

In the example shown, the formula to return the top 3 gainers in cell G5 is:

    =SORT(FILTER(data,data[Change]>=LARGE(data[Change],3)),4,-1)
    

Working from the inside out, the first task is to extract the three rows from the data that have the largest change values. To do this, we use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with the [LARGE function](https://exceljet.net/functions/large-function)
 like this:

    FILTER(data,data[Change]>=LARGE(data[Change],3))
    

Inside FILTER, the _array_ [argument](https://exceljet.net/glossary/function-argument)
 is the entire table, since we want to return all four columns. The _include_ argument is a logical test based on the LARGE function:

    data[Change]>=LARGE(data[Change],3)
    

The LARGE function is configured to return the third largest value in the Change column:

    LARGE(data[Change],3) // get 3rd largest value
    

With 3 given for _k_, LARGE returns the 3rd largest value .02699 (2.699%). We can then simplify the FILTER function to the following:

    FILTER(data,data[Change]>=0.0269)
    

Essentially, we are asking FILTER for rows in the table where change is greater than or equal to 0.0269. FILTER returns the 3 matching rows in an array like this:

    {"JOF",111.63,117.546,0.053;
    "HHB",8.104,8.323,0.0269;
    "XXO",43.124,47.048,0.091}
    

_Note: values have been rounded for readability._

At this point, we have the data we want, but it is not sorted. Since the goal is to show the biggest gainers first, we need to sort the array in _descending_ order by Change. To do this, we use the [SORT function](https://exceljet.net/functions/sort-function)
 directly on the array returned by FILTER:

    =SORT(filtered_array,4,-1)
    

This is an example of nesting - the result from FILTER is delivered as an array inside the SORT function. Since the change column is the last column, _sort\_index_ is given as 4, and _sort\_index_ is provided as -1  to sort in _descending_ order. Finally, the SORT function returns the final sorted array to cell G5, which [spills](https://exceljet.net/glossary/spill)
 into the range G5:J7.

Video: [Basic SORT function example](https://exceljet.net/videos/basic-sort-function-example)

### Top 3 losers

Next, we need to list the biggest 3 losers. In the worksheet shown, the formula in G12 is:

    =SORT(FILTER(data,data[Change]<=SMALL(data[Change],3)),4,1)
    

The first task is to extract the three rows from the data that have the smallest change values. To do this, we use the  FILTER function together with the SMALL function like this:

    FILTER(data,data[Change]<=SMALL(data[Change],3))
    

The array argument in FILTER is given as the table name **data**, since we want to return all four columns. The _include_ argument is supplied as a [logical expression](https://exceljet.net/glossary/logical-test)
 that targets the three smallest values in Change:

    data[Change]<=SMALL(data[Change]
    

The [SMALL function](https://exceljet.net/functions/small-function)
 returns the third largest change in the table:

    SMALL(data[Change],3) // get 3rd smallest value
    

With 3 as _k_, SMALL returns -0.0671 (-6.7%). We can now simplify the FILTER function to this:

    FILTER(data,data[Change]<=-0.0671)
    

We are asking FILTER for rows in data where Change is less than or equal to -0.0671. FILTER returns the 3 matching rows in an array like this:

    {"EYN",7.673,7.158,-0.067;
    "YOL",17.492,16.058,-0.082;
    "DPP",4.067,3.790,-0.068}
    

_Note: values have been rounded for readability._

We have the data we want, but it is unsorted. The goal is to show the biggest losers first, so we want to sort the array in ascending order by change. To do this, the FILTER function is nested inside the [SORT function](https://exceljet.net/functions/sort-function)
, and the result from FILTER is delivered as array:

    =SORT(filtered_array,4,1)
    

_Sort\_index_ is given as 4, since change is the fourth column, and _sort\_index_ is provided as 1 because we want to sort _ascending_ order, starting with the largest negative change. Finally, the SORT function returns the final sorted array to cell G12, which [spills](https://exceljet.net/glossary/spill)
 into the range G12:J14.

_Note: this formula will always return the three rows in the data with the smallest change values, whether these values are negative or not. The label "losers" may not make sense in a small set of data with no negative change values._

Related formulas
----------------

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: FILTER on top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values.png "Excel formula: FILTER on top n values")](https://exceljet.net/formulas/filter-on-top-n-values)

### [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE function. The LARGE function is a simple way to get the nth largest value in a range. Simply provide a range for the first argument ( array ), and a value for n as the second argument ( k ): =...

[![Excel formula: Name of nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value.png "Excel formula: Name of nth largest value")](https://exceljet.net/formulas/name-of-nth-largest-value)

### [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)

In a nutshell, this formula uses the LARGE function to find the nth largest value in a set of data. Once we have that value, we plug it into a standard INDEX and MATCH formula to retrieve the associated name. In other words, we use the nth largest value like a "key" to retrieve associated...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20show%20top%20or%20bottom%20results-Play.png)](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)

### [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)

In this video, we'll use the FILTER function to show the top or bottom results in a set of data. Here we have some test scores for a group of students. In column F, I want to set up a formula to display the top students by score. Now, I'm going to use the FILTER function, but we'll need a way to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)
    
*   [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)
    

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