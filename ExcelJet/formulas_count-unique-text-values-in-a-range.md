# Count unique text values in a range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-text-values-in-a-range

---

[Skip to main content](https://exceljet.net/formulas/count-unique-text-values-in-a-range#main-content)

[](https://exceljet.net/formulas/count-unique-text-values-in-a-range#)

*   [Previous](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)
    
*   [Next](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    

[Count](https://exceljet.net/formulas#Count)

Count unique text values in a range
===================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[FREQUENCY](https://exceljet.net/functions/frequency-function)

[MATCH](https://exceljet.net/functions/match-function)

[ROW](https://exceljet.net/functions/row-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count unique text values in a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20unique%20text%20values%20in%20a%20range.png "Excel formula: Count unique text values in a range")

Summary
-------

To count unique text values in a range, you can use a formula based on several functions: [FREQUENCY](https://exceljet.net/functions/frequency-function)
, [MATCH](https://exceljet.net/functions/match-function)
, [ROW](https://exceljet.net/functions/row-function)
, and [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in F5 is:

    =SUMPRODUCT(--(FREQUENCY(MATCH(B5:B14,B5:B14,0),ROW(B5:B14)-ROW(B5)+1)>0))
    

which returns 4, since there are 4 unique names in B5:B14.

_Note: Another way to count unique values is to [use the COUNTIF function](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
. This is a much simpler formula, but it can run slowly on large data sets._ 

> In [Dynamic Excel](https://exceljet.net/glossary/dynamic-excel)
> , you can use a [simpler and faster formula](https://exceljet.net/formulas/count-unique-values)
>  based on [UNIQUE](https://exceljet.net/functions/unique-function)
> .

Generic formula
---------------

    =SUMPRODUCT(--(FREQUENCY(MATCH(data,data,0),ROW(data)-ROW(data.firstcell)+1)>0))
    

Explanation 
------------

This formula is more complicated than a similar formula that uses FREQUENCY to [count unique numeric values](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
 because FREQUENCY doesn't normally work with non-numeric values. As a result, a large part of the formula simply transforms the non-numeric data into numeric data that FREQUENCY can handle.

Working from the inside out, the MATCH function is used to get the position of each item that appears in the data:

    MATCH(B5:B14,B5:B14,0)
    

The result from MATCH is an [array](https://exceljet.net/glossary/array)
 like this:

    {1;1;1;4;4;6;6;6;9;9}
    

Because MATCH always returns the position of the _first_ match, values that appear more than once in the data return the same position. For example, because "Jim" appears 3 times in the list, he shows up in this array 3 times as the number 1.

This array is fed into FREQUENCY as the _data\_array_ argument. The _bins\_array_ argument is constructed from this part of the formula:

    ROW(B5:B14)-ROW(B5)+1)
    

which builds a [sequential list of numbers](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
 for each value in the data:

    {1;2;3;4;5;6;7;8;9;10}
    

At this point, FREQUENCY is configured like this:

    FREQUENCY({1;1;1;4;4;6;6;6;9;9},{1;2;3;4;5;6;7;8;9;10})
    

FREQUENCY returns an array of numbers that indicate a count for each number in the data array, organized by bin. When a number has already been counted, FREQUENCY will return zero. This is a key feature in the operation of this formula. The result from FREQUENCY is an array like this:

    {3;0;0;2;0;3;0;0;2;0;0} // output from FREQUENCY
    

_Note: FREQUENCY always returns an array with one more item than the bins\_array._

We can now rewrite the formula like this:

    =SUMPRODUCT(--({3;0;0;2;0;3;0;0;2;0;0}>0))
    

Next, we check for values greater than zero (>0), which converts the numbers to TRUE or FALSE, then use a double-negative (--) to convert the TRUE and FALSE values to 1s and 0s. Now we have:

    =SUMPRODUCT({1;0;0;1;0;1;0;0;1;0;0})
    

Finally, SUMPRODUCT simply adds the numbers up and returns the total, which in this case is 4.

### Handling blank cells

Empty cells in the range will cause the formula to return an #N/A error. To handle empty cells, you can use a more complicated array formula that uses the IF function to filter out blank values:

    {=SUM(IF(FREQUENCY(IF(data<>"", MATCH(data,data,0)),ROW(data)-ROW(data.firstcell)+1),1))}
    

_Note: adding IF makes this into an [array formula](https://exceljet.net/glossary/array-formula)
 that requires control-shift-enter._

For more information, [see this page](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
.

> From [Mike Girvin's](https://www.youtube.com/@excelisfun)
>  excellent book on array formulas, _Control-Shift-Enter._

### UNIQUE function in Excel 365

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 provides a better, more elegant way to [list unique values](https://exceljet.net/formulas/unique-values)
 and [count unique values](https://exceljet.net/formulas/count-unique-values)
. These formulas can be adapted to [apply logical criteria](https://exceljet.net/formulas/unique-values-with-criteria)
.

A pivot table is also an excellent way to [list and count unique values](https://exceljet.net/pivot-tables/pivot-table-list-unique-values)
.

Related formulas
----------------

[![Excel formula: Count unique numeric values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values.png "Excel formula: Count unique numeric values in a range")](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

### [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

[![Excel formula: Count unique values in a range with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values%20with%20COUNTIF.png "Excel formula: Count unique values in a range with COUNTIF")](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)

### [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)

Working from the inside out, COUNTIF is configured to values in the range B5:B14, using all of these same values as criteria: COUNTIF(B5:B14,B5:B14) Because we provide 10 values for criteria, we get back an array with 10 results like this: {3;3;3;2;2;3;3;3;2;2} Each number represents a count – "Jim...

[![Excel formula: Count unique text values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20text%20values%20with%20criteria.png "Excel formula: Count unique text values with criteria")](https://exceljet.net/formulas/count-unique-text-values-with-criteria)

### [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)

This is a complex formula that uses FREQUENCY to count numeric values that are derived with the MATCH function. Working from the inside out, the MATCH function is used to get the position of each value that appears in the data: MATCH(B5:B11,B5:B11,0) The result from MATCH is an array like this: {1;...

[![Excel formula: Extract unique items from a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20unique%20items%20from%20a%20list.png "Excel formula: Extract unique items from a list")](https://exceljet.net/formulas/extract-unique-items-from-a-list)

### [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)

The core of this formula is a basic lookup with INDEX: =INDEX(list,row) In other words, give INDEX the list and a row number, and INDEX will retrieve a value to add to the unique list. The hard work is figuring out the ROW number to give INDEX, so that we get unique values only. This is done with...

Related functions
-----------------

[![Excel FREQUENCY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20frequency%20function.png "Excel FREQUENCY function")](https://exceljet.net/functions/frequency-function)

### [FREQUENCY Function](https://exceljet.net/functions/frequency-function)

The Excel FREQUENCY function returns a frequency distribution, which is a list that shows the frequency of values at given intervals. FREQUENCY returns multiple values and must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control-shift-enter, except in...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
    
*   [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
    
*   [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    

### Functions

*   [FREQUENCY Function](https://exceljet.net/functions/frequency-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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