# Excel HSTACK function | Exceljet

**Source:** https://exceljet.net/functions/hstack-function

---

[Skip to main content](https://exceljet.net/functions/hstack-function#main-content)

[](https://exceljet.net/functions/hstack-function#)

*   [Previous](https://exceljet.net/functions/groupby-function)
    
*   [Next](https://exceljet.net/functions/image-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

HSTACK Function
===============

by Dave Bruns · Updated 9 Apr 2025

Related functions 
------------------

[VSTACK](https://exceljet.net/functions/vstack-function)

[TRIMRANGE](https://exceljet.net/functions/trimrange-function)

![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")

Summary
-------

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array.

Purpose 
--------

Combine ranges or arrays horizontally

Return value 
-------------

A single combined range or array

Syntax
------

    =HSTACK(array1,[array2],...)

*   _array1_ - The first array or range to combine.
*   _array2_ - \[optional\] The second array or range to combine.

Using the HSTACK function 
--------------------------

The HSTACK function combines arrays horizontally into a single [array](https://exceljet.net/glossary/array)
. Each subsequent array is appended to the right of the previous array. The result from HSTACK is a _single_ array that [spills](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells.

HSTACK works equally well for [ranges](https://exceljet.net/glossary/range)
 on a worksheet or in-memory [arrays](https://exceljet.net/glossary/array)
 created by a formula. The output from HSTACK is fully dynamic. If data in any given array changes, the result from HSTACK will update immediately. 

Use HSTACK to combine ranges _horizontally_ and [VSTACK](https://exceljet.net/functions/vstack-function)
 to combine ranges _vertically_.

### Basic usage

HSTACK stacks ranges or arrays _horizontally_. In the example below, the range B3:D3 is combined with the range B6:C6. Each subsequent range/array is appended to the right of the previous range/array. The formula in F3 is:

    =HSTACK(B3:D3,B6:C6)
    

![HSTACK basic example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/HSTACK%20basic%20example.png?itok=UCJ0Ilnz "HSTACK basic example")

Ranges may include multiple rows, as seen below. The formula in F3 is:

    =HSTACK(B3:B5,D3:D5)
    

![HSTACK basic example 2](https://exceljet.net/sites/default/files/images/functions/inline/HSTACK%20basic%20example2.png "HSTACK basic example 2")

### Range with array

HSTACK can work interchangeably with both arrays and ranges. In the worksheet below, we combine the [array constant](https://exceljet.net/glossary/array-constant)
 {"Red";"Blue";"Green"} with the range B2:B4. The formula in F3 is:

    =HSTACK({"Red";"Blue";"Green"},B2:B4)
    

![HSTACK arrays with ranges](https://exceljet.net/sites/default/files/images/functions/inline/HSTACK%20arrays%20with%20ranges.png "HSTACK arrays with ranges")

### Arrays of different sizes

When HSTACK is used with arrays of different sizes, the smaller array will be expanded to match the size of the larger array. In other words, the smaller array is "padded" to match the size of the larger array, as seen in the example below. The formula in cell F5 is:

    =HSTACK(B5:B8,D5:D6)
    

![HSTACK with IFERROR](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/HSTACK%20with%20IFERROR.png?itok=7_WxKDjk "HSTACK with IFERROR")

By default, the cells used for padding will display the #N/A error. One option for trapping these errors is to use the [IFERROR function](https://exceljet.net/functions/iferror-function)
. The formula in I5 is:

    =IFERROR(HSTACK(B5:B8,D5:D6),"")
    

In this formula, IFERROR is configured to replace errors with an [empty string](https://exceljet.net/glossary/empty-string)
 (""), which displays as an empty cell.

HSTACK function examples
------------------------

[![Excel formula: Maximum change](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_change.png "Excel formula: Maximum change")](https://exceljet.net/formulas/maximum-change)

### [Maximum change](https://exceljet.net/formulas/maximum-change)

In the example shown, the goal is to calculate the maximum difference between the "High" values in column C and the "Low" values in column D. Because the difference between High and Low is not part of the data, the calculation must occur in the formula itself. This is a classic example of an array...

[![Excel formula: Split full name into parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_full_name_into_parts.png "Excel formula: Split full name into parts")](https://exceljet.net/formulas/split-full-name-into-parts)

### [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)

In this example, the goal is to split the names in column B into three separate parts (First, Middle, and Last) with a single formula. In cases where there is no middle name, the Middle column should be blank. In cases where there are two middle names, the Middle column should contain both names...

[![Excel formula: Sum by week number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week%20number.png "Excel formula: Sum by week number")](https://exceljet.net/formulas/sum-by-week-number)

### [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)

In this example, the goal is to sum the amounts in column D by week number, using the dates in column C to determine the week number. The week numbers in column G are manually entered. The final results should appear in column H. All data is in an Excel Table named data in the range B5:E16. This...

[![Excel formula: Two-way summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20summary%20count.png "Excel formula: Two-way summary count")](https://exceljet.net/formulas/two-way-summary-count)

### [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)

In this example, the goal is to count the people shown in the table by both Department (Dept) and Group as shown in the worksheet. A simple way to do this is with the COUNTIFS function. COUNTIFS function The COUNTIFS function is designed to count things based on more than one condition. Conditions...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Mortgage payment schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/mortgage_schedule_with_extra_payment.png "Excel formula: Mortgage payment schedule")](https://exceljet.net/formulas/mortgage-payment-schedule)

### [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)

The goal of this example is to show how to create a mortgage payment schedule using Excel formulas. A mortgage payment schedule is a detailed breakdown of every payment over the life of a loan. Each payment represents one period , typically a month. For each period, the schedule shows how much of...

[![Excel formula: Minimum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_value_if_0.png "Excel formula: Minimum value if")](https://exceljet.net/formulas/minimum-value-if)

### [Minimum value if](https://exceljet.net/formulas/minimum-value-if)

In this example, the goal is to get the minimum value for each group in the data as shown. The easiest way to solve this problem is with the MINIFS function. However, there are actually several options. If you need more flexibility (you need to work with arrays instead of ranges), you can use the...

[![Excel formula: GROUPBY with monthly totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/groupby_with_monthly_totals.png "Excel formula: GROUPBY with monthly totals")](https://exceljet.net/formulas/groupby-with-monthly-totals)

### [GROUPBY with monthly totals](https://exceljet.net/formulas/groupby-with-monthly-totals)

In this example, the goal is to generate monthly totals using the GROUPBY function. This is a tricky problem in Excel because typically, source data contains a regular date field and not a separate field with month names. In addition, the GROUPBY function will, by default, sort everything in...

[![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")](https://exceljet.net/formulas/dynamic-two-way-count)

### [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps: Create an Excel Table called data List unique colors with UNIQUE function List unique sizes with UNIQUE...

[![Excel formula: GROUPBY with survey results](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/groupby_with_survey_results.png "Excel formula: GROUPBY with survey results")](https://exceljet.net/formulas/groupby-with-survey-results)

### [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)

In May 2025, I ran a survey asking Exceljet newsletter subscribers what version of Excel they use most. This is an important question for Excel learning because the new dynamic array engine has completely changed how many formulas are written. These changes started rolling out after Excel 2019, so...

[![Excel formula: 10 most common text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/10%20most%20common%20text%20values.png "Excel formula: 10 most common text values")](https://exceljet.net/formulas/10-most-common-text-values)

### [10 most common text values](https://exceljet.net/formulas/10-most-common-text-values)

In this example, the goal is to list the 10 most frequently occurring text values in a range, in descending order by count, as seen in the range in E5:F14. This is an advanced formula that requires a number of nested functions. However, it is an excellent example of the power of dynamic array...

[![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")](https://exceljet.net/formulas/sum-by-week)

### [Sum by week](https://exceljet.net/formulas/sum-by-week)

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named data in the range B5:C16. This problem can be solved in a straightforward way with the SUMIFS function . In the current version of...

[![Excel formula: Cash denomination calculator](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cash_denomination_calculator.png "Excel formula: Cash denomination calculator")](https://exceljet.net/formulas/cash-denomination-calculator)

### [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)

In this example, the goal is to build a "cash denomination calculator." A cash denomination calculator is a tool for counting and verifying cash amounts. It can calculate the denominations needed to achieve a certain cash value. It can also perform the reverse calculation and determine the cash...

Related functions
-----------------

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

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
    
*   [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)
    
*   [Maximum change](https://exceljet.net/formulas/maximum-change)
    
*   [GROUPBY with survey results](https://exceljet.net/formulas/groupby-with-survey-results)
    
*   [10 most common text values](https://exceljet.net/formulas/10-most-common-text-values)
    
*   [Minimum value if](https://exceljet.net/formulas/minimum-value-if)
    
*   [Sum by week number](https://exceljet.net/formulas/sum-by-week-number)
    
*   [Sum by week](https://exceljet.net/formulas/sum-by-week)
    
*   [GROUPBY with monthly totals](https://exceljet.net/formulas/groupby-with-monthly-totals)
    
*   [Split full name into parts](https://exceljet.net/formulas/split-full-name-into-parts)
    

### Functions

*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [TRIMRANGE Function](https://exceljet.net/functions/trimrange-function)
    

### Links

*   [Microsoft TRIMRANGE documentation](https://support.microsoft.com/en-us/office/hstack-function-98c4ab76-10fe-4b4f-8d5f-af1c125fe8c2)
    

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