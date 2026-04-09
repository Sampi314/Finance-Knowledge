# Excel FREQUENCY function | Exceljet

**Source:** https://exceljet.net/functions/frequency-function

---

[Skip to main content](https://exceljet.net/functions/frequency-function#main-content)

[](https://exceljet.net/functions/frequency-function#)

*   [Previous](https://exceljet.net/functions/forecast.linear-function)
    
*   [Next](https://exceljet.net/functions/gamma-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

FREQUENCY Function
==================

by Dave Bruns · Updated 22 Sep 2021

Related functions 
------------------

[MODE](https://exceljet.net/functions/mode-function)

![Excel FREQUENCY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20frequency%20function.png "Excel FREQUENCY function")

Summary
-------

The Excel FREQUENCY function returns a frequency distribution, which is a list that shows the frequency of values at given intervals. FREQUENCY returns multiple values and must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control-shift-enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
.

Purpose 
--------

Get the frequency of values in a data set

Return value 
-------------

A vertical array of frequencies

Syntax
------

    =FREQUENCY(data_array,bins_array)

*   _data\_array_ - An array of values for which you want to get frequencies.
*   _bins\_array_ - An array of intervals ("bins") for grouping values.

Using the FREQUENCY function 
-----------------------------

The FREQUENCY function counts how often numeric values occur in a set of data and returns a _frequency distribution_ – a list that shows the frequency (count) of each value in a range at given intervals (bins).  FREQUENCY returns the distribution as a [vertical array](https://exceljet.net/glossary/array)
 of numbers that represent a "count per bin".

The FREQUENCY function always returns an array with _one more item_ than bins in the _bins\_array_. This is by design, to catch any values greater than the largest value in the _bins\_array_. The general pattern for FREQUENCY is:

    =FREQUENCY(data,bins)
    

where _data\_array_ and _bins\_array_ are typically [ranges](https://exceljet.net/glossary/range)
 on the worksheet.

### Instructions

To create a frequency distribution using FREQUENCY:

1.  Enter numbers that represent the bins you want to group values into
2.  Make a selection the same size as the range that contains bins, or one greater if want to include the extra item
3.  Enter the FREQUENCY function as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
     with control+shift+enter.

In [Excel 365](https://exceljet.net/glossary/excel-365)
, it is not necessary to enter FREQUENCY as an array formula. See notes below.

### Examples

In the example shown, the formula in G5:G8 is:

    {=FREQUENCY(C5:C14,F5:F8)}
    

Entered as a multi-cell array formula. 

_Note: the curly braces added by Excel automatically when entered with [control + shift + enter](https://exceljet.net/glossary/cse)
._

### Horizontal results

The FREQUENCY function always returns a vertical [array](https://exceljet.net/glossary/array)
 of results. To return horizontal results, wrap the FREQUENCY function in the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
:

    =TRANSPOSE(FREQUENCY(data,bins))
    

### Excel 365

In [Excel 365](https://exceljet.net/glossary/excel-365)
, which supports [dynamic arrays natively](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, it is not necessary to select multiple cells before entering the FREQUENCY function. In cell G5, you can simply enter the formula below:

    =FREQUENCY(C5:C14,L5:L8)
    

FREQUENCY will return an array of six counts, and these counts will [spill](https://exceljet.net/glossary/spill)
 automatically into the range G5:G9. The count in the last row (G9) is the overflow bin, the count of any values greater than the largest value in the _bins\_array_.

### Notes

*   FREQUENCY returns multiple values and _must be entered as an array formula, except in [Excel 365](https://exceljet.net/glossary/excel-365)
    ._
*   FREQUENCY always returns an array with _one more item_ than bins. This is by design, to catch any values greater than the largest interval in the bins\_array.
*   Each bin shows a count of values up to and including bin value, excluding values already accounted for.

FREQUENCY function examples
---------------------------

[![Excel formula: Histogram with FREQUENCY](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Histogram%20with%20FREQUENCY.png "Excel formula: Histogram with FREQUENCY")](https://exceljet.net/formulas/histogram-with-frequency)

### [Histogram with FREQUENCY](https://exceljet.net/formulas/histogram-with-frequency)

Note: later versions of Excel include a native histogram chart , which is easy to create , but not as flexible to format. The example on this page shows one way to create your own histogram data with the FREQUENCY function and use a regular column chart to plot the results. Because FREQUENCY is a...

[![Excel formula: Count consecutive monthly orders](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20consecutive%20monthly%20orders.png "Excel formula: Count consecutive monthly orders")](https://exceljet.net/formulas/count-consecutive-monthly-orders)

### [Count consecutive monthly orders](https://exceljet.net/formulas/count-consecutive-monthly-orders)

In this example, the goal is to count the maximum number of consecutive monthly orders. That is, we want to count consecutive monthly orders greater than zero. This is a tricky formula to understand, so buckle up! They key to the formula is knowing that the FREQUENCY function gathers numbers into "...

[![Excel formula: Count unique numeric values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values%20with%20criteria.png "Excel formula: Count unique numeric values with criteria")](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)

### [Count unique numeric values with criteria](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

[![Excel formula: Count unique text values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20text%20values%20in%20a%20range.png "Excel formula: Count unique text values in a range")](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

### [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

This formula is more complicated than a similar formula that uses FREQUENCY to count unique numeric values because FREQUENCY doesn't normally work with non-numeric values. As a result, a large part of the formula simply transforms the non-numeric data into numeric data that FREQUENCY can handle...

[![Excel formula: Count unique numeric values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values.png "Excel formula: Count unique numeric values in a range")](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

### [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

[![Excel formula: Count unique text values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20text%20values%20with%20criteria.png "Excel formula: Count unique text values with criteria")](https://exceljet.net/formulas/count-unique-text-values-with-criteria)

### [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)

This is a complex formula that uses FREQUENCY to count numeric values that are derived with the MATCH function. Working from the inside out, the MATCH function is used to get the position of each value that appears in the data: MATCH(B5:B11,B5:B11,0) The result from MATCH is an array like this: {1;...

[![Excel formula: Count numbers by range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20numbers%20by%20range.png "Excel formula: Count numbers by range")](https://exceljet.net/formulas/count-numbers-by-range)

### [Count numbers by range](https://exceljet.net/formulas/count-numbers-by-range)

In this example, the goal is to count ages in column C according to the brackets defined in columns E and F. All data is in an Excel Table named data defined in the range B5:C16. A simple way to solve this problem is with the COUNTIFS function. If you are using Excel 365 or Excel 2021, another easy...

[![Excel formula: Longest winning streak](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/longest_winning_streak.png "Excel formula: Longest winning streak")](https://exceljet.net/formulas/longest-winning-streak)

### [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)

In this example, the goal is to calculate a count for the longest winning streak in a set of data. In the worksheet shown, wins ("W") and losses ("L") are recorded in column C, so this means we want to count the longest consecutive series of W's. Although we are specifically counting the longest...

Related functions
-----------------

[![Excel MODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")](https://exceljet.net/functions/mode-function)

### [MODE Function](https://exceljet.net/functions/mode-function)

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

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
    
*   [Histogram with FREQUENCY](https://exceljet.net/formulas/histogram-with-frequency)
    
*   [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Count consecutive monthly orders](https://exceljet.net/formulas/count-consecutive-monthly-orders)
    
*   [Count numbers by range](https://exceljet.net/formulas/count-numbers-by-range)
    
*   [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)
    
*   [Count unique numeric values with criteria](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)
    
*   [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    

### Functions

*   [MODE Function](https://exceljet.net/functions/mode-function)
    

### Links

*   [Microsoft FREQUENCY function documentation](https://support.office.com/en-us/article/frequency-function-44e3be2b-eca0-42cd-a3f7-fd9ea898fdb9)
    

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