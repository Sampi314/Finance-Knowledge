# Count unique numeric values in a range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-numeric-values-in-a-range

---

[Skip to main content](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range#main-content)

[](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range#)

*   [Previous](https://exceljet.net/formulas/count-unique-dates)
    
*   [Next](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)
    

[Count](https://exceljet.net/formulas#Count)

Count unique numeric values in a range
======================================

by Dave Bruns · Updated 25 Oct 2023

Related functions 
------------------

[FREQUENCY](https://exceljet.net/functions/frequency-function)

[SUM](https://exceljet.net/functions/sum-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Count unique numeric values in a range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20unique%20numeric%20values.png "Excel formula: Count unique numeric values in a range")

Summary
-------

To count unique numeric values in a range, you can use a formula based on the [FREQUENCY](https://exceljet.net/functions/frequency-function)
 and [SUM](https://exceljet.net/videos/how-to-use-the-sum-function)
 functions. In the example shown, employee numbers appear in the range B5:B14. The formula in F5 is:

    =SUM(--(FREQUENCY(B5:B14,B5:B14)>0))
    

which returns 4, since there are 4 unique employee ids in the list.

> In [Excel 365](https://exceljet.net/glossary/excel-365)
> , you can use a [simpler and faster formula](https://exceljet.net/formulas/count-unique-values)
>  based on the [UNIQUE function](https://exceljet.net/functions/unique-function)
> .

Generic formula
---------------

    =SUM(--(FREQUENCY(data,data)>0))

Explanation 
------------

_Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a [more complicated formula](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
._

The Excel FREQUENCY function returns a frequency distribution, which is a summary table that shows the frequency of numeric values, organized in "bins". We use it here as a roundabout way to count unique numeric values.

Working from the inside-out, we supply the same set of numbers for both the data array and bins array to FREQUENCY:

    FREQUENCY(B5:B14,B5:B14)
    

FREQUENCY returns an [array](https://exceljet.net/glossary/array)
 with a count of each numeric value in the range:

    {4;0;0;0;2;0;1;3;0;0;0}
    

The result is a bit cryptic, but the meaning is 905 appears four times, 773 appears two times, 801 appears once, and 963 appears three times.

FREQUENCY has a special feature that automatically returns zero for any numbers that have already appeared in the data array, which is why values are zero once a number has been encountered.

Next, each of these values is tested to be greater than zero:

    {4;0;0;0;2;0;1;3;0;0;0}>0
    

The result is an array like this:

    {TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;FALSE;FALSE}
    

Each TRUE represents a unique number in the list. The SUM ignores logical values by default, so we coerce TRUE and FALSE values to 1s and 0s with a [double negative](https://exceljet.net/glossary/double-unary)
 (--), which yields:

    =SUM({1;0;0;0;1;0;1;1;0;0;0})
    

Finally, SUM adds these values up and returns the total, which in this case is 4.

_Note: you could also use SUMPRODUCT to sum the items in the array._

### Using COUNTIF instead of FREQUENCY to count unique values

Another way to count unique numeric values is to use [COUNTIF instead of FREQUENCY](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
. This is a simpler formula, but beware that using COUNTIF on larger data sets to count unique values can cause performance issues. The FREQUENCY formula, while more complicated, calculates much faster.

### UNIQUE function in Excel 365

> In Excel 2021 and later, you can use a [simpler and faster formula](https://exceljet.net/formulas/count-unique-values)
>  based on the [UNIQUE function](https://exceljet.net/functions/unique-function)
> .

Related formulas
----------------

[![Excel formula: Count unique numeric values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values%20with%20criteria.png "Excel formula: Count unique numeric values with criteria")](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)

### [Count unique numeric values with criteria](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

[![Excel formula: Count unique text values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20text%20values%20in%20a%20range.png "Excel formula: Count unique text values in a range")](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

### [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

This formula is more complicated than a similar formula that uses FREQUENCY to count unique numeric values because FREQUENCY doesn't normally work with non-numeric values. As a result, a large part of the formula simply transforms the non-numeric data into numeric data that FREQUENCY can handle...

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

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count unique numeric values with criteria](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)
    
*   [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    
*   [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
    
*   [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    

### Functions

*   [FREQUENCY Function](https://exceljet.net/functions/frequency-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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