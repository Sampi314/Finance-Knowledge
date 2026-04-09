# Excel VSTACK function | Exceljet

**Source:** https://exceljet.net/functions/vstack-function

---

[Skip to main content](https://exceljet.net/functions/vstack-function#main-content)

[](https://exceljet.net/functions/vstack-function#)

*   [Previous](https://exceljet.net/functions/valuetotext-function)
    
*   [Next](https://exceljet.net/functions/wrapcols-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

VSTACK Function
===============

by Dave Bruns · Updated 9 Apr 2025

Related functions 
------------------

[HSTACK](https://exceljet.net/functions/hstack-function)

[TRIMRANGE](https://exceljet.net/functions/trimrange-function)

![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")

Summary
-------

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array.

Purpose 
--------

Combine ranges or arrays vertically

Return value 
-------------

A single combined range or array

Syntax
------

    =VSTACK(array1,[array2],...)

*   _array1_ - The first array or range to combine.
*   _array2_ - \[optional\] The second array or range to combine.

Using the VSTACK function 
--------------------------

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array. The result from VSTACK is a _single_ array that [spills](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells.

VSTACK works equally well for [ranges](https://exceljet.net/glossary/range)
 on a worksheet or in-memory [arrays](https://exceljet.net/glossary/array)
 created by a formula. The output from VSTACK is fully dynamic. If data in the given arrays changes, the result from VSTACK will immediately update. VSTACK works well with [Excel Tables](https://exceljet.net/articles/excel-tables)
, as seen in the worksheet above, since [Excel Tables automatically expand](https://exceljet.net/videos/how-excel-table-ranges-work)
 when new data is added.

Use VSTACK to combine ranges _vertically_ and [HSTACK](https://exceljet.net/functions/hstack-function)
 to combine ranges _horizontally._

### Basic usage

VSTACK stacks ranges or arrays vertically. In the example below, the range B3:B5 is combined with the range B8:B9. Each subsequent range/array is appended to the bottom of the previous range/array. The formula in D3 is:

    =VSTACK(B3:B5,B8:B9) 
    

![VSTACK basic example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/VSTACK%20basic%20example.png?itok=iIQOwbnE "VSTACK basic example")

### Range with array

VSTACK can work interchangeably with both arrays and ranges. In the worksheet below, we combine the [array constant](https://exceljet.net/glossary/array-constant)
 {"Color","Qty"} with the range B3:C7. The formula in E3 is:

    =VSTACK({"Color","Qty"},B3:C7)
    

![VSTACK array with range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/VSTACK%20array%20with%20range.png?itok=O2RqlDQv "VSTACK array with range")

### Arrays of different size

When VSTACK is used with arrays of different size, the smaller array will be expanded to match the size of the larger array. In other words, the smaller array is "padded" to match the size of the larger array, as seen in the example below. The formula in cell E5 is:

    =VSTACK(B5:C8,B11:B13)
    

![VSTACK with IFERROR](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/VSTACK%20with%20IFERROR.png?itok=RqFG3646 "VSTACK with IFERROR")

By default, the cells used for padding will display the #N/A error. One option for trapping these errors is to use the [IFERROR function](https://exceljet.net/functions/iferror-function)
. The formula in H5 is:

    =IFERROR(VSTACK(B5:C8,B11:B13),"")
    

In this formula IFERROR is configured to replace errors with an [empty string](https://exceljet.net/glossary/empty-string)
 (""), which displays as an empty cell.

VSTACK function examples
------------------------

[![Excel formula: Sum by week number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week%20number.png "Excel formula: Sum by week number")](https://exceljet.net/formulas/sum-by-week-number)

### [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)

In this example, the goal is to sum the amounts in column D by week number, using the dates in column C to determine the week number. The week numbers in column G are manually entered. The final results should appear in column H. All data is in an Excel Table named data in the range B5:E16. This...

[![Excel formula: Tiered discounts based on quantity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tiered_discounts_based_on_quantity.png "Excel formula: Tiered discounts based on quantity")](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)

### [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)

This example shows a workbook designed to apply discounts based on seven pricing tiers. The total quantity of items is entered as a variable in cell C4. The discount is applied via the unit costs in E7:E13, which decrease as the quantity increases. The first 200 items have an undiscounted price of...

[![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")](https://exceljet.net/formulas/dynamic-two-way-count)

### [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps: Create an Excel Table called data List unique colors with UNIQUE function List unique sizes with UNIQUE...

[![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")](https://exceljet.net/formulas/sum-by-week)

### [Sum by week](https://exceljet.net/formulas/sum-by-week)

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named data in the range B5:C16. This problem can be solved in a straightforward way with the SUMIFS function . In the current version of...

[![Excel formula: Longest winning streak](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/longest_winning_streak.png "Excel formula: Longest winning streak")](https://exceljet.net/formulas/longest-winning-streak)

### [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)

In this example, the goal is to calculate a count for the longest winning streak in a set of data. In the worksheet shown, wins ("W") and losses ("L") are recorded in column C, so this means we want to count the longest consecutive series of W's. Although we are specifically counting the longest...

[![Excel formula: Sum if with multiple ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum_if_with_multiple_ranges.png "Excel formula: Sum if with multiple ranges")](https://exceljet.net/formulas/sum-if-with-multiple-ranges)

### [Sum if with multiple ranges](https://exceljet.net/formulas/sum-if-with-multiple-ranges)

In this example, the goal is to calculate a total quantity for each color across the two ranges shown in the worksheet. The two ranges are "non-contiguous", which means they are not connected or touching. Both ranges contain a list of colors in the first column and quantities in the second column...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Combine data in multiple worksheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/combine_data_in_multiple_worksheets.png "Excel formula: Combine data in multiple worksheets")](https://exceljet.net/formulas/combine-data-in-multiple-worksheets)

### [Combine data in multiple worksheets](https://exceljet.net/formulas/combine-data-in-multiple-worksheets)

The goal is to combine data from different worksheets with a formula. Note that we are not restructuring the data in any way, we are simply combining data in different worksheets that already have the same structure. At a high level, the formula we are using combines data from multiple sheets with...

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: Unique values case-sensitive](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique_values_case_sensitive.png "Excel formula: Unique values case-sensitive")](https://exceljet.net/formulas/unique-values-case-sensitive)

### [Unique values case-sensitive](https://exceljet.net/formulas/unique-values-case-sensitive)

In this example, the goal is to create a formula that will extract unique values from a range of data in a case-sensitive way. Normally, we would use the UNIQUE function to extract unique values. However, UNIQUE is not case-sensitive so it won't work in this situation. One way to solve this problem...

[![Excel formula: COUNTIF with non-contiguous range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/countif%20with%20non-contiguous%20range.png "Excel formula: COUNTIF with non-contiguous range")](https://exceljet.net/formulas/countif-with-non-contiguous-range)

### [COUNTIF with non-contiguous range](https://exceljet.net/formulas/countif-with-non-contiguous-range)

In this example, the goal is to count values in three non-contiguous ranges with criteria. To be included in the count, values must be greater than 50. The COUNTIF counts the number of cells in a range that meet the given criteria. However, COUNTIF does not perform counts across different ranges...

[![Excel formula: Unique values from multiple ranges ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20from%20multiple%20ranges.png "Excel formula: Unique values from multiple ranges ")](https://exceljet.net/formulas/unique-values-from-multiple-ranges)

### [Unique values from multiple ranges](https://exceljet.net/formulas/unique-values-from-multiple-ranges)

In this example, the goal is to extract unique values from three separate ranges at the same time: range1 (C5:C16), range2 (D5:D15), and range3 (F5:F13). At one time, this was a difficult problem, since UNIQUE is programmed to accept only one array and there is no obvious way to provide another...

[![Excel formula: Maximum change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_change.png "Excel formula: Maximum change")](https://exceljet.net/formulas/maximum-change)

### [Maximum change](https://exceljet.net/formulas/maximum-change)

In the example shown, the goal is to calculate the maximum difference between the "High" values in column C and the "Low" values in column D. Because the difference between High and Low is not part of the data, the calculation must occur in the formula itself. This is a classic example of an array...

Related functions
-----------------

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel TRIMRANGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_trimrange_function.png "Excel TRIMRANGE function")](https://exceljet.net/functions/trimrange-function)

### [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)

The Excel TRIMRANGE function removes empty rows and columns from the outer edges of a range of data. The result is a "trimmed" range that only includes data from the used portion of the range. Because it is a formula, TRIMRANGE will update the range dynamically when data is added or removed...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Combine data in multiple worksheets](https://exceljet.net/formulas/combine-data-in-multiple-worksheets)
    
*   [COUNTIF with non-contiguous range](https://exceljet.net/formulas/countif-with-non-contiguous-range)
    
*   [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)
    
*   [Unique values from multiple ranges](https://exceljet.net/formulas/unique-values-from-multiple-ranges)
    
*   [Maximum change](https://exceljet.net/formulas/maximum-change)
    
*   [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)
    
*   [Sum by week](https://exceljet.net/formulas/sum-by-week)
    

### Functions

*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)
    

### Links

*   [Microsoft VSTACK documentation](https://support.microsoft.com/en-us/office/vstack-function-a4b86897-be0f-48fc-adca-fcc10d795a9c)
    

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