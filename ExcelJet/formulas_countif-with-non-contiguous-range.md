# COUNTIF with non-contiguous range - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/countif-with-non-contiguous-range

---

[Skip to main content](https://exceljet.net/formulas/countif-with-non-contiguous-range#main-content)

[](https://exceljet.net/formulas/countif-with-non-contiguous-range#)

*   [Previous](https://exceljet.net/formulas/count-visible-rows-with-criteria)
    
*   [Next](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    

[Count](https://exceljet.net/formulas#Count)

COUNTIF with non-contiguous range
=================================

by Dave Bruns · Updated 15 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

![Excel formula: COUNTIF with non-contiguous range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/countif%20with%20non-contiguous%20range.png "Excel formula: COUNTIF with non-contiguous range")

Summary
-------

To count values in separate ranges with criteria, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 together with [INDIRECT](https://exceljet.net/functions/indirect-function)
 and [SUM](https://exceljet.net/functions/sum-function)
. In the example shown, cell I5 contains this formula:

    =SUM(COUNTIF(INDIRECT({"B5:B8","D7:D10","F6:F11"}),">50"))
    

The result is 9 since there are nine values greater than 50 in the three ranges shown.

_Note: In [Excel 365](https://exceljet.net/glossary/excel-365)
, the [VSTACK](https://exceljet.net/functions/vstack-function)
 and [HSTACK](https://exceljet.net/functions/hstack-function)
 functions offer a new approach to this problem. See below for an example._

Generic formula
---------------

    =SUM(COUNTIF(INDIRECT({"rng1","rng2","rng3"}),criteria))

Explanation 
------------

In this example, the goal is to count values in three non-contiguous ranges with criteria. To be included in the count, values must be greater than 50. The COUNTIF counts the number of cells in a range that meet the given criteria. However, COUNTIF does not perform counts across different ranges. If you try to use COUNTIF with multiple ranges separated by commas, or in an [array constant](https://exceljet.net/glossary/array-constant)
, you'll get an error. There are several ways to approach this problem, as explained below.

### INDIRECT and COUNTIF

The [INDIRECT function](https://exceljet.net/functions/indirect-function)
 converts a given [text string](https://exceljet.net/glossary/text-value)
 into a proper Excel reference:

    =INDIRECT("A1") // returns A1
    

One approach is to provide the ranges as text in an [array constant](https://exceljet.net/glossary/array-constant)
 to INDIRECT like this:

    INDIRECT({"B5:B8","D7:D10","F6:F11"})
    

Then pass the result from INDIRECT into the [COUNTIF function](https://exceljet.net/functions/countif-function)
 like this:

    =COUNTIF(INDIRECT({"B5:B8","D7:D10","F6:F11"}),">50")
    

INDIRECT will evaluate the text values and pass the references into COUNTIF as the _range_ argument. For reasons mysterious, COUNTIF will accept the result from INDIRECT without complaint. Because COUNTIF receives more than one range, it will return more than one result in an [array](https://exceljet.net/glossary/array)
 like this:

    ={4,2,3}
    

The three numbers in this array are the counts of numbers greater than 50 in each of the three ranges. To "catch" these results and return a total, we use the SUM function:

    =SUM({4,2,3}) // returns 9
    

The SUM function then returns the sum of all values, 9. Although this is an array formula, it does not require [CSE](https://exceljet.net/glossary/cse)
, since we are using an array constant.

_Note: INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can impact workbook performance._

### More than one COUNTIF

Another way to solve this problem is to use more than one COUNTIF:

    =COUNTIF(B5:B8,">50")+COUNTIF(D7:D10,">50")+COUNTIF(F6:F11,">50")
    

With a limited number of ranges, this approach may be easier to implement. It avoids possible performance impacts of INDIRECT and allows a normal formula syntax for ranges, so ranges will update automatically with worksheet changes. The INDIRECT example above relies on text strings that need to be updated manually.

### VSTACK function

In current versions of Excel, a better approach is to first combine the ranges, and then perform the conditional count. To combine all three ranges vertically, you can use the [VSTACK function](https://exceljet.net/functions/vstack-function)
:

    =VSTACK(B5:B8,D7:D10,F6:F11)
    

The result from VSTACK is a single array with 14 values. Unfortunately, we can't pass this result into the COUNTIF function, because COUNTIF is in a [group of functions that require actual ranges](https://exceljet.net/articles/excels-racon-functions)
. However, we can use the SUM function and [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
 to perform the conditional count. The complete formula looks like this:

    =SUM(--(VSTACK(B5:B8,D7:D10,F6:F11)>50))
    

After VSTACK runs, and all values are checked with >50, we have an array of 14 TRUE and FALSE values like this:

    {TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;FALSE}
    

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to convert the TRUE and FALSE values to 1s and 0s, and the resulting array is returned directly to the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM({1;1;1;1;1;1;0;0;1;0;1;1;0;0}) // returns 9
    

The SUM function sums the array and returns 9 as a final result. 

Video: [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

Related formulas
----------------

[![Excel formula: Count cells less than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20less%20than.png "Excel formula: Count cells less than")](https://exceljet.net/formulas/count-cells-less-than)

### [Count cells less than](https://exceljet.net/formulas/count-cells-less-than)

In this example, the goal is to count test scores in column C that are less than 75. The simplest way to do this is with the COUNTIF function , which takes two arguments , range and criteria : =COUNTIF(range,criteria) The test scores in the range C5:C16 and we want to count scores less than 75 , so...

[![Excel formula: Count cells that do not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain.png "Excel formula: Count cells that do not contain")](https://exceljet.net/formulas/count-cells-that-do-not-contain)

### [Count cells that do not contain](https://exceljet.net/formulas/count-cells-that-do-not-contain)

In this example, the goal is to count cells that do not contain a specific substring. This problem can be solved with the COUNTIF function or the SUMPRODUCT function . Both approaches are explained below. Although COUNTIF is not case-sensitive, the SUMPRODUCT version of the formula can be adapted...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells less than](https://exceljet.net/formulas/count-cells-less-than)
    
*   [Count cells that do not contain](https://exceljet.net/formulas/count-cells-that-do-not-contain)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    

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