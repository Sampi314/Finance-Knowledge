# Sum by group - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-by-group

---

[Skip to main content](https://exceljet.net/formulas/sum-by-group#main-content)

[](https://exceljet.net/formulas/sum-by-group#)

*   [Previous](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)
    
*   [Next](https://exceljet.net/formulas/sum-by-month)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum by group
============

by Dave Bruns · Updated 11 Nov 2022

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Sum by group](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20by%20group.png "Excel formula: Sum by group")

Summary
-------

To sum data by group you can use the [SUMIF function](https://exceljet.net/functions/sumif-function)
 or the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
. In the example shown, the formula in G5 is:

    =SUMIF(B:B,F5,C:C)
    

With "Blue" in cell F5, the result is 38. As the formula is copied down, it returns a count of each color listed in column F. See below for an explanation of the formula in column D.

Generic formula
---------------

    SUMIF(A:A,A1,B:B)

Explanation 
------------

In this example, the goal is to sum by group, where each group is represented by a different color: Blue, Red, Green, and Purple. The worksheet shown contains two different approaches. In the range F5:G8, we have created a summary table to summarize counts by color. In column D, we are using a modified formula that reports a total per group the first time the group appears in the data. The article below explains both approaches.

_Note: both formulas below use [full column references](https://exceljet.net/glossary/full-column-reference)
 (e.g. B:B, C:C). Full column references are a compact way to express a formula, and they automatically pick up new data in a column. However, they can also cause performance problems in some formulas, and they can return incorrect results when they intersect data elsewhere in a worksheet . In general, an [Excel Table](https://exceljet.net/glossary/excel-table)
 or a [dynamic named range](https://exceljet.net/glossary/dynamic-named-range)
 is a safer way to refer to data that may shrink or grow. All that said, you will run into full column references in worksheets developed by others, so it is important to understand how they work._

### Summary table

One approach to solving this problem is to create a summary table to summarize results by group, as seen in the range F5:G8. The solution relies on the [SUMIF function](https://exceljet.net/functions/sumif-function)
.  The formula in G5, copied down, is:

    =SUMIF(B:B,F5,C:C)
    

In this formula, B:B is the _range_, F5 is the _criteria_, and C:C is the _sum\_range_. As the formula is copied down the column, the reference to F5 changes at each new row while the full column references do not change. The result is a subtotal by group of the amounts in column C.

_Note: in the latest version of Excel, [new functions](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 make it possible to create summary tables that automatically update to include new groups. See [this example](https://exceljet.net/formulas/dynamic-summary-count)
 for details._

### Inline totals

Another way to approach this problem is to perform the calculations directly in the data in column D as seen in the worksheet. The formula in cell D5, copied down, is:

    =IF(B5=B4,"",SUMIF(B:B,B5,C:C))
    

In this formula, we use the [IF function](https://exceljet.net/videos/the-if-function)
 to test each value in column B to see if its the same as the previous value (i.e. the cell above). If the two values match, we return an [empty string](https://exceljet.net/glossary/empty-string)
 (""). If the values do not match, the IF function returns this SUMIF formula:

    SUMIF(B:B,B5,C:C)
    

This formula works the same way as the formula used in the summary table. As the formula is copied down the column, the reference to B5 changes at each new row while the full column references do not change. Because the IF function is suppressing the SUMIF formula when the values in column B match, the sums only appear in column D the _first time_ a new color is encountered. 

_Note: this formula depends on data being sorted by group in order to get sensible results. One advantage of the summary table approach is that the sort order doesn't matter._

### Performance

As mentioned earlier, full column references can cause performance problems in some cases, because worksheets in Excel contain more than 1 million rows. Excel does try to limit calculations to the "used range" of a worksheet, in order to reduce the number of calculations being performed. However, be aware that full column references can cause severe performance problems in specific circumstances. Charles Williams over at Fast Excel has a good article on this topic, with a full set of timing results.

### Why about Pivot Tables?

[Pivot tables](https://exceljet.net/articles/excel-pivot-tables)
 remain an excellent way to [group and summarize data](https://exceljet.net/pivot-tables/pivot-table-basic-sum)
.

Related formulas
----------------

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

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

*   [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Links

*   [Excel Full Column References and Used Range: Good Idea or Bad Idea?](https://fastexcel.wordpress.com/2015/12/12/excel-full-column-references-and-used-range-good-idea-or-bad-idea/)
    

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