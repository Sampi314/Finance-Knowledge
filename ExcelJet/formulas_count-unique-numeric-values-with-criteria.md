# Count unique numeric values with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-unique-numeric-values-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria#main-content)

[](https://exceljet.net/formulas/count-unique-numeric-values-with-criteria#)

*   [Previous](https://exceljet.net/formulas/count-unique-numeric-values-in-a-range)
    
*   [Next](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    

[Count](https://exceljet.net/formulas#Count)

Count unique numeric values with criteria
=========================================

by Dave Bruns · Updated 12 Oct 2023

Related functions 
------------------

[FREQUENCY](https://exceljet.net/functions/frequency-function)

[SUM](https://exceljet.net/functions/sum-function)

![Excel formula: Count unique numeric values with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20unique%20numeric%20values%20with%20criteria.png "Excel formula: Count unique numeric values with criteria")

Summary
-------

To count unique numeric values in a range, you can use a formula based on the [FREQUENCY](https://exceljet.net/functions/frequency-function)
, [SUM](https://exceljet.net/functions/sum-function)
, and [IF](https://exceljet.net/functions/if-function)
 functions. In the example shown, employee numbers appear in the range B5:B14. The formula in G6 is:

    =SUM(--(FREQUENCY(IF(C5:C14="A",B5:B14),B5:B14)>0))
    

which returns 2, since there are 2 unique employee ids in building A.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
._

> With [Excel 365](https://exceljet.net/glossary/excel-365)
> , you can use a [simpler and faster formula](https://exceljet.net/formulas/count-unique-values-with-criteria)
>  based on [UNIQUE](https://exceljet.net/functions/unique-function)
> .

Generic formula
---------------

    {=SUM(--(FREQUENCY(IF(criteria,values),values)>0))}

Explanation 
------------

_Note: Prior to Excel 365, Excel did not have a dedicated function to count unique values. This formula shows one way to count unique values, as long as they are numeric. If you have text values, or a mix of text and numbers, you'll need to use a [more complicated formula](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
._

The Excel FREQUENCY function returns a frequency distribution, which is a summary table that contains the frequency of numeric values, organized in "bins". We use it here as a roundabout way to count unique numeric values. To apply criteria, we use the IF function.

Working from the inside-out, we first filter values with the IF function:

    IF(C5:C14="A",B5:B14) // filter on building A
    

The result of this operation is an array like this:

    {905;905;905;905;773;773;FALSE;FALSE;FALSE;FALSE}
    

Notice all ids in building B are now FALSE. This array is delivered directly to the FREQUENCY function as the _data\_array._ For the _bins\_array_, we supply the ids themselves:

    FREQUENCY({905;905;905;905;773;773;FALSE;FALSE;FALSE;FALSE},{905;905;905;905;773;773;801;963;963;963})
    

With this configuration, FREQUENCY returns the array below:

    {4;0;0;0;2;0;0;0;0;0;0}
    

The result is a bit cryptic, but the meaning is 905 appears four times, and 773 appears two times. The FALSE values are automatically ignored.

FREQUENCY has a special feature that automatically returns zero for any numbers that have already appeared in the data array, which is why values are zero once a number has been encountered. This is the feature that allows this approach to work.

Next, each of these values is tested to be greater than zero:

    {4;0;0;0;2;0;0;0;0;0;0}>0
    

The result is an array like this:

    {TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}
    

Each TRUE in the list represents a unique number in the list, and we just need to add up the TRUE values with SUM. However, SUM won't add up logical values in an array, so we need to first coerce the values into 1 or zero. This is done with the [double-negative](https://exceljet.net/glossary/double-unary)
 (--). The result is an array of only 1's or 0's:

    {1;0;0;0;1;0;0;0;0;0;0}
    

Finally, SUM adds these values up and returns the total, which in this case is 2.

### Multiple criteria

You can extend the formula to handle multiple criteria like this:

    {=SUM(--(FREQUENCY(IF((criteria1)*(criteria2),values),values)>0))}
    

### UNIQUE function in Excel 365

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [UNIQUE function](https://exceljet.net/functions/unique-function)
 provides a better, more elegant way to [list unique values](https://exceljet.net/formulas/unique-values)
 and [count unique values](https://exceljet.net/formulas/count-unique-values)
. These formulas can be adapted to [apply logical criteria](https://exceljet.net/formulas/unique-values-with-criteria)
.

Related formulas
----------------

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count unique text values in a range](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
    
*   [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)
    
*   [Count unique text values with criteria](https://exceljet.net/formulas/count-unique-text-values-with-criteria)
    
*   [Extract unique items from a list](https://exceljet.net/formulas/extract-unique-items-from-a-list)
    

### Functions

*   [FREQUENCY Function](https://exceljet.net/functions/frequency-function)
    
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