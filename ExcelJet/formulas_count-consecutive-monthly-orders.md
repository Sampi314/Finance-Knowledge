# Count consecutive monthly orders - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-consecutive-monthly-orders

---

[Skip to main content](https://exceljet.net/formulas/count-consecutive-monthly-orders#main-content)

[](https://exceljet.net/formulas/count-consecutive-monthly-orders#)

*   [Previous](https://exceljet.net/formulas/cost-of-living-adjustment)
    
*   [Next](https://exceljet.net/formulas/count-values-out-of-tolerance)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Count consecutive monthly orders
================================

by Dave Bruns · Updated 22 Apr 2021

Related functions 
------------------

[FREQUENCY](https://exceljet.net/functions/frequency-function)

[MAX](https://exceljet.net/functions/max-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Count consecutive monthly orders](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20consecutive%20monthly%20orders.png "Excel formula: Count consecutive monthly orders")

Summary
-------

To count consecutive monthly orders, you can use a formula based on the [FREQUENCY function](https://exceljet.net/functions/frequency-function)
, with help from the [COLUMN](https://exceljet.net/functions/column-function)
 and [MAX](https://exceljet.net/functions/max-function)
 functions. In the example shown, the formula in I5 is:

    {=MAX(FREQUENCY(IF(C5:H5>0,COLUMN(C5:H5)),IF(C5:H5=0,COLUMN(C5:H5))))}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with Control + Shift + Enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Generic formula
---------------

    {=MAX(FREQUENCY(IF(rng>0,COLUMN(rng)),IF(rng=0,COLUMN(rng))))}

Explanation 
------------

In this example, the goal is to count the maximum number of consecutive monthly orders. That is, we want to count consecutive monthly orders greater than zero. This is a tricky formula to understand, so buckle up!

They key to the formula is knowing that the [FREQUENCY function](https://exceljet.net/functions/frequency-function)
 gathers numbers into "bins" in a particular way. Each bin represents an upper limit, and contains a count of all numbers in the data set that are less than or equal to the upper limit, and greater than the previous bin number. The trick then is to create the _data\_array_ argument using the condition you want to test for (order count greater than zero in this case), and the _bins\_array_ using the opposite condition.

To create the _data\_array_ bin we use the following code:

    IF(C5:H5>0,COLUMN(C5:H5))
    

Here, we use the [IF function](https://exceljet.net/functions/if-function)
 to test the order count in each month to see if it's greater than zero. If so, IF returns the column number using the [COLUMN function](https://exceljet.net/functions/column-function)
. The result from IF is an [array](https://exceljet.net/glossary/array)
 like this:

    {3,FALSE,FALSE,6,7,8}
    

Notice that only columns where order count > 0 make it into this array. Those columns where the count is zero become FALSE.

The _bins\_array_ is generated with this snippet:

    IF(C5:H5=0,COLUMN(C5:H5))
    

Here the IF function is used again to test the order count in each column, but this time the logic is reversed. Only column numbers where the count is zero make it into the array returned by IF, which looks like this:

    {FALSE,4,5,FALSE,FALSE,FALSE}
    

Per standard FREQUENCY behavior, the numbers in the _bins\_array_ become the functional bins that tally non-zero orders. Months where orders are greater than zero are translated to FALSE and don't collect any numbers from the data array, since FALSE values are ignored. The result is that the surviving bins count the number of consecutive non-zero orders up to that point, but excluding those previously counted. This all works because of the incrementing nature of rows and columns – you can be certain that the "next" number is always greater than the previous number.

With the data array and bin arrays as shown above, FREQUENCY returns a count per bin in an array like this:

    {1;0;3}
    

The FREQUENCY function always returns an array with _one more item_ than bins in the _bins\_array_. This is by design, to catch any values greater than the largest value in the _bins\_array_. This array is returned directly to the [MAX function](https://exceljet.net/functions/max-function)
,  with returns the largest number in the array:

    =MAX({1;0;3}) // returns 3
    

### Other consecutive values

To count consecutive occurrences of other values, just adjust the logic as needed following the same pattern: the first condition tests for the thing you want to count, the second condition tests for the opposite.

Related formulas
----------------

[![Excel formula: Longest winning streak](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/longest_winning_streak.png "Excel formula: Longest winning streak")](https://exceljet.net/formulas/longest-winning-streak)

### [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)

In this example, the goal is to calculate a count for the longest winning streak in a set of data. In the worksheet shown, wins ("W") and losses ("L") are recorded in column C, so this means we want to count the longest consecutive series of W's. Although we are specifically counting the longest...

Related functions
-----------------

[![Excel FREQUENCY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20frequency%20function.png "Excel FREQUENCY function")](https://exceljet.net/functions/frequency-function)

### [FREQUENCY Function](https://exceljet.net/functions/frequency-function)

The Excel FREQUENCY function returns a frequency distribution, which is a list that shows the frequency of values at given intervals. FREQUENCY returns multiple values and must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control-shift-enter, except in...

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)
    

### Functions

*   [FREQUENCY Function](https://exceljet.net/functions/frequency-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Links

*   [Count consecutive cells with specific text (MrExcel)](http://www.mrexcel.com/forum/excel-questions/620059-count-consecutive-cells-containing-specific-text.html)
    

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