# Count unique text values with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-text-values-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/count-unique-text-values-with-criteria#main-content)

[](https://exceljet.net/formulas/count-unique-text-values-with-criteria#)

*   [Previous](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    
*   [Next](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
    

[Count](https://exceljet.net/formulas#Count)

Count unique text values with criteria
======================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[FREQUENCY](https://exceljet.net/functions/frequency-function)

[MATCH](https://exceljet.net/functions/match-function)

[ROW](https://exceljet.net/functions/row-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Count unique text values with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20unique%20text%20values%20with%20criteria.png "Excel formula: Count unique text values with criteria")

Summary
-------

To count unique text values in a range with criteria, you can use an array formula based on the [FREQUENCY](https://exceljet.net/functions/frequency-function)
 and [MATCH](https://exceljet.net/functions/match-function)
 functions. In the example shown, the formula in G6 is:

    {=SUM(--(FREQUENCY(IF(C5:C11=G5,MATCH(B5:B11,B5:B11,0)),ROW(B5:B11)-ROW(B5)+1)>0))}
    

The result is 3 since three different people worked on the Omega project.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in Excel 2019 and earlier._

> With [Excel 365](https://exceljet.net/glossary/excel-365)
> , you can use a [much simpler formula](https://exceljet.net/formulas/count-unique-values-with-criteria)
>  based on the [UNIQUE function](https://exceljet.net/functions/unique-function)
> .

Generic formula
---------------

    {=SUM(--(FREQUENCY(IF(criteria,MATCH(vals,vals,0)),ROW(vals)-ROW(vals.first)+1)>0))}
    

Explanation 
------------

This is a complex formula that uses FREQUENCY to count numeric values that are derived with the MATCH function. Working from the inside out, the MATCH function is used to get the position of each value that appears in the data:

    MATCH(B5:B11,B5:B11,0)
    

The result from MATCH is an array like this:

    {1;1;3;1;1;6;7}
    

Because MATCH always returns the position of the _first_ match, values that appear more than once in the data return the same position. For example, because "Jim" appears 4 times in the list, he shows up in this array 4 times as the number 1.

Outside of the MATCH function, the [IF function](https://exceljet.net/functions/if-function)
 is used to apply criteria, which in this case involves testing if the project is "omega" (from cell G5):

    IF(C5:C11=G5 // filter on "omega"
    

The IF function acts like a filter, only allowing the values from MATCH to pass through if they are associated with "omega". The result is an array like this:

    {FALSE;FALSE;FALSE;1;1;6;7} // after filtering
    

The filtered array is delivered directly to the FREQUENCY function as the **data\_array** argument. Next, the [ROW function](https://exceljet.net/functions/row-function)
 is used to build a [sequential list of numbers](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
 for each value in the data:

    ROW(B3:B12)-ROW(B3)+1
    

This creates an array like this:

    {1;2;3;4;5;6;7;8;9;10}
    

which becomes the **bins\_array** argument in FILTER. At this point, we have:

    FREQUENCY({FALSE;FALSE;FALSE;1;1;6;7},{1;2;3;4;5;6;7})
    

FREQUENCY returns an array of numbers that indicate a count for each value in the data array, organized by bin. When a number has already been counted, FREQUENCY will return zero. The result from FREQUENCY is an array like this:

    {2;0;0;0;0;1;1;0} // result from FREQUENCY
    

_Note: FREQUENCY always returns an array with one more item than the **bins\_array**._

At this point, we can rewrite the formula like this:

    =SUM(--({2;0;0;0;0;1;1;0}>0))
    

We check for values greater than zero, which converts the numbers to TRUE or FALSE:

    =SUM(--({TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;FALSE}))
    

Then we use a [double-negative](https://exceljet.net/glossary/double-unary)
 to coerce the logical values to 1s and 0s:

    =SUM({1;0;0;0;0;1;1;0})
    

Finally, the [SUM function](https://exceljet.net/functions/sum-function)
 returns 3 as the final result.

_Note: this is an array formula and must be entered using Control + Shift + Enter in Excel 2019 and earlier._

### Handling empty cells in the range

If any cells in the range are empty, you'll need to adjust the formula to prevent empty cells from being passed into the MATCH function, which will throw an error. You can do this by adding another nested IF function to check for blank cells:

    {=SUM(--(FREQUENCY(IF(B5:B11<>"",IF(C5:C11=G5,MATCH(B5:B11,B5:B11,0))),ROW(B5:B11)-ROW(B5)+1)>0))}
    

### With two criteria

If you have two criteria, you can extend the logic of the formula by adding another nested IF:

    {=SUM(--(FREQUENCY(IF(c1,IF(c2,MATCH(vals,vals,0))),ROW(vals)-ROW(vals.1st)+1)>0))}
    

Where **c1** = criteria1, **c2** = criteria2 and **vals** = the values range.

### With boolean logic

With [boolean logic](https://exceljet.net/glossary/boolean-logic)
, you can reduce [nested IFs](https://exceljet.net/articles/nested-ifs)
:

    {=SUM(--(FREQUENCY(IF((criteria1)*(criteria2),MATCH(vals,vals,0)),ROW(vals)-ROW(vals.1st)+1)>0))}
    

This makes it easier to add and manage additional criteria.

Note: I adapted the formulas above from [Mike Girvin's](https://www.youtube.com/user/excelisfun)
 excellent book on array formulas, _Control-Shift-Enter._

### UNIQUE function in Excel 365

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 provides a better, more elegant way to [list unique values](https://exceljet.net/formulas/unique-values)
 and [count unique values](https://exceljet.net/formulas/count-unique-values)
. These formulas can be adapted to [apply logical criteria](https://exceljet.net/formulas/unique-values-with-criteria)
.

Related formulas
----------------

[![Excel formula: Count unique numeric values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values%20with%20criteria.png "Excel formula: Count unique numeric values with criteria")](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)

### [Count unique numeric values with criteria](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

[![Excel formula: Count unique numeric values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20numeric%20values.png "Excel formula: Count unique numeric values in a range")](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

### [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)

Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a more complicated formula . The Excel FREQUENCY...

[![Excel formula: Count unique values in a range with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values%20with%20COUNTIF.png "Excel formula: Count unique values in a range with COUNTIF")](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)

### [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)

Working from the inside out, COUNTIF is configured to values in the range B5:B14, using all of these same values as criteria: COUNTIF(B5:B14,B5:B14) Because we provide 10 values for criteria, we get back an array with 10 results like this: {3;3;3;2;2;3;3;3;2;2} Each number represents a count – "Jim...

[![Excel formula: Count unique text values in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20unique%20text%20values%20in%20a%20range.png "Excel formula: Count unique text values in a range")](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

### [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)

This formula is more complicated than a similar formula that uses FREQUENCY to count unique numeric values because FREQUENCY doesn't normally work with non-numeric values. As a result, a large part of the formula simply transforms the non-numeric data into numeric data that FREQUENCY can handle...

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

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

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
    
*   [Count unique numeric values in a range](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
    
*   [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
    
*   [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    

### Functions

*   [FREQUENCY Function](https://exceljet.net/functions/frequency-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    

### Links

*   [Mike Girvin's book Control-Shift-Enter](https://www.youtube.com/@excelisfun)
    

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