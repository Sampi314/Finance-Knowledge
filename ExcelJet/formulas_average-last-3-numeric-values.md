# Average last 3 numeric values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-last-3-numeric-values

---

[Skip to main content](https://exceljet.net/formulas/average-last-3-numeric-values#main-content)

[](https://exceljet.net/formulas/average-last-3-numeric-values#)

*   [Previous](https://exceljet.net/formulas/average-if-with-filter)
    
*   [Next](https://exceljet.net/formulas/average-last-n-columns)
    

[Average](https://exceljet.net/formulas#Average)

Average last 3 numeric values
=============================

by Dave Bruns · Updated 28 Feb 2023

Related functions 
------------------

[AVERAGE](https://exceljet.net/functions/average-function)

[FILTER](https://exceljet.net/functions/filter-function)

[TAKE](https://exceljet.net/functions/take-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[LARGE](https://exceljet.net/functions/large-function)

[ROW](https://exceljet.net/functions/row-function)

![Excel formula: Average last 3 numeric values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_last_3_numeric_values.png "Excel formula: Average last 3 numeric values")

Summary
-------

To average the top 3 scores in a set of data, you can use a formula based on the [AVERAGE function](https://exceljet.net/functions/average-function)
, the [FILTER function](https://exceljet.net/functions/filter-function)
, and the [TAKE function](https://exceljet.net/functions/take-function)
. In the example shown, the formula in D5 is:

    =AVERAGE(TAKE(FILTER(data,ISNUMBER(data)),-3))

where **data** is the named range B5:B16. The result is 100, the average of 99, 100, and 101. These are the last 3 numeric values in the range B5:B16.

_Note: FILTER and TAKE are newer functions in Excel. See below for a formula that will work in older versions of Excel._

Generic formula
---------------

    =AVERAGE(TAKE(FILTER(data,ISNUMBER(data)),-n))

Explanation 
------------

In this example, the goal is to average the last 3 numeric values in a set of data. The best solution depends on the version of Excel you have available. In the current version of Excel, this can be nicely solved with a formula based on the [AVERAGE function](https://exceljet.net/functions/average-function)
, the [FILTER function](https://exceljet.net/functions/filter-function)
, and the [TAKE function](https://exceljet.net/functions/take-function)
. In older versions of Excel, you can use an alternative formula based on the [LOOKUP function](https://exceljet.net/functions/lookup-function)
, the [LARGE function](https://exceljet.net/functions/large-function)
, and the [ROW function](https://exceljet.net/functions/row-function)
. Both approaches are explained below.

_Note: the difference in complexity between the modern formula and the legacy formula below is a great example of how new functions in Excel are making hard problems much easier to solve._

### Modern formula

In the current version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can solve this problem with a formula like this:

    =AVERAGE(TAKE(FILTER(data,ISNUMBER(data)),-3))

Working from the inside out, the [FILTER function](https://exceljet.net/functions/filter-function)
 is configured to extract only numeric values from the named range **data** (B5:B16) like this:

    FILTER(data,ISNUMBER(data))

The [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 creates the filtering logic. ISNUMBER returns TRUE for numeric values and FALSE for anything else. Because we are giving ISNUMBER a range that contains 12 values, ISNUMBER returns an [array](https://exceljet.net/glossary/array)
 with 12 TRUE or FALSE values like this:

    {TRUE;TRUE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE}

This array is returned to the FILTER function as the _include_ argument, and FILTER returns only the 8 numeric values in **data** in an array like this:

    {95;94;97;96;98;99;100;101}

This array above is handed off to the [TAKE function](https://exceljet.net/functions/take-function)
, which is configured to return only the last 3 values:

    TAKE({95;94;97;96;98;99;100;101},-3)

TAKE then returns 99, 100, and 101 to the [AVERAGE function](https://exceljet.net/functions/average-function)
:

    =AVERAGE({99;100;101})

AVERAGE calculates an average of the 3 values and returns 100 as a final result.

### Variable n

The generic form of this formula where **n** is a variable is shown below. To change the number of numeric values being averaged, just change **n** to a different number.

    =AVERAGE(TAKE(FILTER(data,ISNUMBER(data)),-n))

One nice thing about the TAKE function is that it will automatically handle the case where the number of requested values is greater than the number of values in the array returned by FILTER. For example, if you ask TAKE for 5 values, and there are only 3 values available, TAKE will return 3 values without an error.

### Last n columns

Although the example shown has data in rows, the formula can be adjusted to work with data in columns like this:

    =AVERAGE(TAKE(FILTER(data,ISNUMBER(data)),1,-n))

This formula assumes that values appear in columns. The only difference is that the 2nd argument in TAKE (_rows_) is now 1, and a 3rd argument (_columns_) has been added and set to -3. In other words, we are asking TAKE for the last **n** columns instead of the last **n** rows.

### Legacy Excel

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
 we need to take a different approach because we don't have the FILTER function or the TAKE function to use. One option is to use a formula like this:

    =AVERAGE(LOOKUP(LARGE(IF(ISNUMBER(data),ROW(data)),{1,2,3}),ROW(data),data))

Notice the [AVERAGE function](https://exceljet.net/functions/average-function)
 is the outermost function in the formula. AVERAGE will calculate an average of numbers presented in an array, so almost all the work in this formula is to generate an array of the last 3 numeric values in a range. Working from the inside out, the IF function is used to "filter" numeric values:

    IF(ISNUMBER(data),ROW(data))
    

The [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 returns TRUE for numeric values, and FALSE for other values (including blanks), and the [ROW function](https://exceljet.net/functions/row-function)
 returns row numbers, so the result of this operation is an array of row numbers that correspond to numeric entries:

    {5;6;FALSE;FALSE;9;10;11;12;13;FALSE;FALSE;16}
    

This array goes into the LARGE function with the [array constant](https://exceljet.net/glossary/array-constant)
 {1,2,3} for _k_:

    LARGE({5;6;FALSE;FALSE;9;10;11;12;13;FALSE;FALSE;16},{1,2,3})

LARGE automatically ignores the FALSE values and returns an array with the largest 3 numbers, which correspond to the last 3 rows with numeric values:

    {16,13,12}

This array goes into the [LOOKUP function](https://exceljet.net/functions/lookup-function)
 as the lookup value. The lookup array is provided by the ROW function, and the result array is the named range data (B5:B16):

    LOOKUP({16,13,12},ROW(data),data)

After ROW runs, we have:

    LOOKUP({16,13,12}, {5;6;7;8;9;10;11;12;13;14;15;16}, data)

LOOKUP locates the 3 row numbers in the array of row numbers returned by ROW, and returns the 3 corresponding values from data directly to the AVERAGE function:

    =AVERAGE({101,100,99})
    

AVERAGE calculates an average of the 3 values and returns 100 as a final result.

_Note: I ran into this clever approach over on chandoo.org, [in a reply by Sajan](http://chandoo.org/wp/2013/10/03/formula-forensics-no-035-average-the-last-3-values-greater-than-0/)
 to a similar question._

### Making n variable

To make **n** variable so that it can be easily changed, you can replace the hardcoded array constant {1,2,3} with a dynamic array created with the [INDIRECT function](https://exceljet.net/functions/indirect-function)
 like this:

    =AVERAGE(LOOKUP(LARGE(IF(ISNUMBER(data),ROW(data)),ROW(INDIRECT("1:"&n))), ROW(data), data))
    

Note that if the number of numeric values in data drops below **n**, this formula will return the #NUM error since LARGE won't be able to return 3 values as requested. To guard against this problem, you can use the [MIN function](https://exceljet.net/functions/min-function)
 like this:

    ROW(INDIRECT("1:"&MIN(3,COUNT(data))))
    

Here, [MIN](https://exceljet.net/functions/min-function)
 is used to set the size of the requested array to **n** or the actual count of numeric values, whichever is smaller.

Related formulas
----------------

[![Excel formula: Average last n columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_5_columns.png "Excel formula: Average last n columns")](https://exceljet.net/formulas/average-last-n-columns)

### [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)

In this example, the goal is to average the last n columns in a set of data, where n is a variable entered in cell K5 that can be changed at any time. Since more data may be added, a key requirement is to average amounts by position. For convenience, the values to average are in the named range...

[![Excel formula: Average top 3 scores](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_top_3_scores.png "Excel formula: Average top 3 scores")](https://exceljet.net/formulas/average-top-3-scores)

### [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)

In this example, the goal is to calculate an average of the top 3 quiz scores for each name listed in column B. For reference, column H has a formula that calculates an average of all 4 scores. This is a slightly tricky problem, because it's not obvious how to limit the scores included in the...

[![Excel formula: Average last n rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_last_n_rows.png "Excel formula: Average last n rows")](https://exceljet.net/formulas/average-last-n-rows)

### [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)

In the worksheet shown, we have a list of values in column C. The goal is to dynamically average the last n values using the numbers in cell E5 for n . Since the list may grow over time, the key requirement is to average amounts by position. For convenience only, the values to average are in the...

Related functions
-----------------

[![Excel AVERAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_average.png "Excel AVERAGE function")](https://exceljet.net/functions/average-function)

### [AVERAGE Function](https://exceljet.net/functions/average-function)

The Excel AVERAGE function calculates the average (arithmetic mean) of supplied numbers. AVERAGE can handle up to 255 individual arguments, which can include numbers, cell references, ranges, arrays, and constants.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average last n columns](https://exceljet.net/formulas/average-last-n-columns)
    
*   [Average top 3 scores](https://exceljet.net/formulas/average-top-3-scores)
    
*   [Average last n rows](https://exceljet.net/formulas/average-last-n-rows)
    

### Functions

*   [AVERAGE Function](https://exceljet.net/functions/average-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

### Videos

*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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