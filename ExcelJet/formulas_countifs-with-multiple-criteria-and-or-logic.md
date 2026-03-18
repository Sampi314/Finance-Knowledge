# COUNTIFS with multiple criteria and OR logic - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic

---

[Skip to main content](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic#main-content)

[](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic#)

*   [Previous](https://exceljet.net/formulas/countif-with-non-contiguous-range)
    
*   [Next](https://exceljet.net/formulas/histogram-with-frequency)
    

[Count](https://exceljet.net/formulas#Count)

COUNTIFS with multiple criteria and OR logic
============================================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: COUNTIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/COUNTIFS%20with%20multiple%20criteria%20and%20OR%20logic.png "Excel formula: COUNTIFS with multiple criteria and OR logic")

Summary
-------

To use the COUNTIFS function with OR logic, you can use an [array constant](https://exceljet.net/glossary/array-constant)
 for criteria. In the example shown, the formula in H7 is:

    =SUM(COUNTIFS(D5:D16,{"complete","pending"}))
    

The result is 9 since there are 6 orders that are complete and 3 orders that are pending.

Generic formula
---------------

    =SUM(COUNTIFS(range,{"red","blue","green"}))

Explanation 
------------

In this example, the goal is to use the COUNTIFS function to count data with "OR logic". The challenge is the COUNTIFS function applies AND logic by default.

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 returns the count of cells that meet one or more criteria, and supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Conditions are supplied to COUNTIFS in the form of range/criteria pairs — each pair contains one range and the associated criteria for that range:

    =COUNTIFS(range1,criteria1)
    

_Count cells in range1 that meet criteria1._

By default, the COUNTIFS function applies AND logic. When you supply multiple conditions, ALL conditions must match in order to generate a count:

    =COUNTIFS(range1,criteria1,range1,criteria2)
    

_Count where range1 meets criteria1 AND range1 meets criteria2._

This means if we try to user COUNTIFS like this:

    =COUNTIFS(D5:D16,"complete",D5:D16,"pending") // returns 0
    

The result is zero, since the order status in column D can't be both "complete" and "pending" at the same time. One solution is to supply multiple criteria in an [_array constant_](https://exceljet.net/glossary/array-constant)
 like this:

    =COUNTIFS(D5:D16,{"complete","pending"})
    

This will cause COUNTIFS to return two results: a count for "complete" and a count for "pending" in [array](https://exceljet.net/glossary/array)
 like this:

    {6,3}
    

In the [current version of Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, these results will [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into two cells. To get a final total in one formula, we [nest](https://exceljet.net/glossary/nesting)
 the COUNTIFS formula inside the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(COUNTIFS(D5:D16,{"complete","pending"}))
    

COUNTIFS returns the counts directly to SUM:

    =SUM({6,3}) // returns 9
    

And the SUM function returns the sum of the array as a final result.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 but it doesn't require special handling in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
 when using an array constant as above. If you use a cell reference for criteria instead of an array constant, you will need to enter the formula with Control + Shift + Enter in Legacy Excel._

### Adding another OR criteria

You can add one additional criteria to this formula, but you'll need to use a _single column_ [array](https://exceljet.net/glossary/array)
 for criteria1 and a _single row array_ for criteria2. So, for example, to count orders that are "Complete" or "Pending", for "Andy Garcia" or "Bob Jones", you can use:

    =SUM(COUNTIFS(D4:D16,{"complete","pending"},C4:C16,{"Bob Jones";"Andy Garcia"}))
    

Note we use a comma in the first array constant for a [horizontal array](https://exceljet.net/glossary/array)
 and a semicolon for the second array constant for a vertical array. With this configuration, Excel "pairs" elements in the two array constants, and returns counts in a two dimensional array like this

|     | Bob Jones | Andy Garcia |
| --- | --- | --- |
| Complete | 1   | 1   |
| Pending | 1   | 0   |

The array result from COUNTIFS is returned directly to the SUM function:

    =SUM({1,1;1,0}) // returns 3
    

And SUM returns the final result, which is 3 in this case.

_Note: this technique will only handle two range/criteria pairs. If you have more than two criteria, [consider a SUMPRODUCT formula as described here](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
._

### Cell reference for criteria

As mentioned above, you can use a cell reference for criteria in an [array formula](https://exceljet.net/glossary/array-formula)
 like this:

    ={SUM(COUNTIFS(range,B1:B2))}
    

Where _range_ is the criteria range, and _B1:B2_ is an example cell reference that contains criteria. This formula "just works" in the current version of Excel, which supports [dynamic array formulas](https://exceljet.net/glossary/dynamic-array)
. However, in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, the formula must be entered with Control + Shift + Enter.

### Wildcards and double-counting

COUNTIF and COUNTIFS support [wildcards](https://exceljet.net/glossary/wildcard)
, but you need to be careful not to double-count when you have multiple "contains" conditions with OR logic. [See this example](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
 for more information

Related formulas
----------------

[![Excel formula: Count cells equal to this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20this%20or%20that.png "Excel formula: Count cells equal to this or that")](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

### [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

In this example, the goal is to count cells in the range D5:D15 that contain "red" or "blue". For convenience, the D5:D15 is named color . Counting cells equal to this OR that is more complicated than it first appears because there is no built-in function for counting with OR logic. The COUNTIFS...

[![Excel formula: Count cells not equal to x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20x%20or%20y_1.png "Excel formula: Count cells not equal to x or y")](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

### [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

In this example, the goal is to count the number of cells in data (B5:B15) that are not equal to "red" or "blue". This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. Not equal to The not equal to operator in Excel is <>. For example, with the...

[![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

### [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both text strings . When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't...

[![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

### [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using array constants to hold the values of interest, but the article also shows how to use cell references instead. In simple...

[![Excel formula: Count matching values in matching columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20matching%20values%20in%20matching%20columns.png "Excel formula: Count matching values in matching columns")](https://exceljet.net/formulas/count-matching-values-in-matching-columns)

### [Count matching values in matching columns](https://exceljet.net/formulas/count-matching-values-in-matching-columns)

In this example, the goal is to count "z" or "c" values in the named range data , but only when the column header is "A" or "B". The formula used to perform this calculation is based on the SUMPRODUCT function : =SUMPRODUCT(ISNUMBER(MATCH(headers,{"A","B"},0))\*ISNUMBER(MATCH(data,{"z","c"},0)))...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIFS%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countifs-function)

### [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

In this video, we'll look at how to use the COUNTIFS function to count cells that meet multiple criteria. Let's take a look. In this first set of tables, we have two named ranges , "number" and "color." In column G, I'll enter a formula that satisfies the conditions in column E. The COUNTIFS...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)
    
*   [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    
*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    
*   [Count matching values in matching columns](https://exceljet.net/formulas/count-matching-values-in-matching-columns)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Videos

*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    

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