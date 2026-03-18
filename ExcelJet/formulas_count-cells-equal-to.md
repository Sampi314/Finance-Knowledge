# Count cells equal to - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-equal-to

---

[Skip to main content](https://exceljet.net/formulas/count-cells-equal-to#main-content)

[](https://exceljet.net/formulas/count-cells-equal-to#)

*   [Previous](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Next](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    

[Count](https://exceljet.net/formulas#Count)

Count cells equal to
====================

by Dave Bruns · Updated 13 Dec 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count cells equal to](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20equal%20to.png "Excel formula: Count cells equal to")

Summary
-------

To count the number of cells equal to a specific value, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, H6 contains this formula:

    =COUNTIF(D5:D16,"red")
    

The result is 4, since there are four cells in the range D5:D16 that contain "red".

Generic formula
---------------

    =COUNTIF(range,value)

Explanation 
------------

In this example, the goal is to count cells equal to a specific value. In this case, we want to count cells that contain "red" in the [range](https://exceljet.net/glossary/range)
 D5:D16. This problem can be solved with the COUNTIF function and the SUMPRODUCT function, as explained below.

### COUNTIF function

One way to solve this problem is with the COUNTIF function, which is designed to count cells in a range that meet one specific condition. COUNTIF takes two [arguments](https://exceljet.net/glossary/function-argument)
: _range_ and _criteria_:

    =COUNTIF(range,criteria)
    

For this problem, _range_ is D5:D16 and _criteria_ is "red". We place double quotes ("red") because "red" is a [text value](https://exceljet.net/glossary/text-value)
. The formula in cell H6 is:

    =COUNTIF(D5:D16,"red") // returns 4
    

COUNTIF returns the count of values in D5:D16 that are equal to "red", which is 4.

_Note: when [text values](https://exceljet.net/glossary/text-value)
 are supplied directly as criteria in COUNTIF, they need to be enclosed double quotes (""). If you have a criteria in another cell, supply the cell address as criteria without quotes, as seen in [this example](https://exceljet.net/formulas/summary-count-with-countif)
._

### With SUMPRODUCT

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. To count cells in the range D5:D16 that are equal to "red", you can use a formula like this:

    =SUMPRODUCT(--(D5:D16="red")) // returns 4
    

Because the range D5:D16 contains 12 values, the logical expression D5:D16="red" returns an [array](https://exceljet.net/glossary/array)
 with 12 TRUE/FALSE results like this:

    {TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE}
    

Each TRUE corresponds to a cell in D5:D16 that contains "red". The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to convert the TRUE and FALSE values to 1s and 0s:

    =SUMPRODUCT({1;1;0;0;0;0;1;0;0;1;0;0})
    

SUMPRODUCT then sums the items in the array and returns 4 as a final result. Although in this example the COUNTIF function is an excellent solution, SUMPRODUCT provides a lot more flexibility in [more complex problems](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
.

Related formulas
----------------

[![Excel formula: Count cells that do not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain.png "Excel formula: Count cells that do not contain")](https://exceljet.net/formulas/count-cells-that-do-not-contain)

### [Count cells that do not contain](https://exceljet.net/formulas/count-cells-that-do-not-contain)

In this example, the goal is to count cells that do not contain a specific substring. This problem can be solved with the COUNTIF function or the SUMPRODUCT function . Both approaches are explained below. Although COUNTIF is not case-sensitive, the SUMPRODUCT version of the formula can be adapted...

[![Excel formula: Count cells that contain text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20text.png "Excel formula: Count cells that contain text")](https://exceljet.net/formulas/count-cells-that-contain-text)

### [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)

In this example, the goal is to count cells in a range that contain text values. This could be hard-coded text like "apple" or "red", numbers entered as text, or formulas that return text values. Empty cells and cells that contain numeric values or errors should not be included in the count. This...

[![Excel formula: Cell contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell_contains_specific_text.png "Excel formula: Cell contains specific text")](https://exceljet.net/formulas/cell-contains-specific-text)

### [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)

In this example, the goal is to test a value in a cell to see if it contains a specific substring . Excel contains two functions designed to check the occurrence of one text string inside another: the SEARCH function and the FIND function. The difference is that the SEARCH function supports...

[![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

### [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the named range value . The core of the solution explained below is the COUNTIF function , with help from the IF function to suppress a count for...

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

### [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both text strings . When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

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

*   [Count cells that do not contain](https://exceljet.net/formulas/count-cells-that-do-not-contain)
    
*   [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)
    
*   [Cell contains specific text](https://exceljet.net/formulas/cell-contains-specific-text)
    
*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Videos

*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    
*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

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