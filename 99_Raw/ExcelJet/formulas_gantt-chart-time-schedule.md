# Gantt chart time schedule - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/gantt-chart-time-schedule

---

[Skip to main content](https://exceljet.net/formulas/gantt-chart-time-schedule#main-content)

[](https://exceljet.net/formulas/gantt-chart-time-schedule#)

*   [Previous](https://exceljet.net/formulas/gantt-chart-by-week)
    
*   [Next](https://exceljet.net/formulas/gantt-chart-with-weekends)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Gantt chart time schedule
=========================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[OR](https://exceljet.net/functions/or-function)

![Excel formula: Gantt chart time schedule](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/gantt%20chart%20time%20schedule.png "Excel formula: Gantt chart time schedule")

Summary
-------

To build a Gantt chart to show a time schedule, you can use [Conditional Formatting](https://exceljet.net/conditional-formatting-formulas)
 with a formula based on AND and OR functions. In the example shown, the formula applied to D5 is:

    =IF($B5<$C5,AND(D$4>=$B5,D$4<=$C5),OR(D$4>=$B5,D$4<$C5))
    

Note [references are mixed](https://exceljet.net/glossary/mixed-reference)
 to lock rows and columns as needed in order to test each cell in the grid correctly.

Generic formula
---------------

    =IF(start<end,AND(A$1>=start,time<=end),OR(A$1>=start,A$1<end))

Explanation 
------------

_Note: this is a great example of a formula that is hard to understand because the cell references are hard to interpret. The gist of the logic used is this: if the time in row 4 is between the start and end times, the formula should return TRUE and trigger the blue fill via conditional formatting. The actual implementation is a little more complicated because the formula below also takes into account the possibility that the start and end times cross midnight. If this is relevant to your situation, you can use just the AND expression explained below._

The calendar header (row 4) is a series of [valid Excel times](https://exceljet.net/glossary/excel-time)
, formatted with the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "hh". This makes it possible to set up a conditional formatting rule that compares the time associated with each column in row 4 with the times entered in columns B and C.

Each time in row 4 needs to be checked to see if it falls within the start and end times in columns B and C, for each row of data in the schedule. The logic used to apply conditional formatting depends on the start and end times. When the start time is less than the end time (normal case) the AND function is used to trigger conditional formatting. When the start time is greater than the end time (times cross midnight) the OR function is used instead.

To handle this distinction at a high level, the IF function is used first to check each pair of times:

    =IF($B5<$C5
    

When the start time is earlier than the end time, the test above returns TRUE, and IF returns the AND part of the formula:

    AND(D$4>=$B5,D$4<=$C5)
    

The [AND function](https://exceljet.net/functions/and-function)
 is configured with two conditions. The first condition checks to see if the column time is greater than or equal to the start time:

    D$4>=$B5
    

The second condition checks that the column time is less than or equal to the end time:

    D$4<=$C5
    

When both conditions return TRUE, the formula returns TRUE, and triggers the blue fill for the cells in the calendar grid.

When the start time is _greater_ than the end time (times cross midnight), IF returns an expression constructed with OR:

    OR(D$4>=$B5,D$4<$C5)
    

Here, the [OR function](https://exceljet.net/functions/or-function)
 is configured with two conditions. The first condition is the same as that used in AND above – it checks to see if the column time is greater than or equal to the start time:

    D$4>=$B5
    

The second condition is altered slightly to check if the column time is less than the end time:

    D$4<$C5
    

When _either_ condition returns TRUE, OR returns TRUE, and triggers the conditional formatting.

_Note: both conditions use [mixed references](https://exceljet.net/glossary/mixed-reference)
 to ensure that the references update correctly as conditional formatting is applied to the grid._

Related formulas
----------------

[![Excel formula: Gantt chart](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20gantt%20chart.png "Excel formula: Gantt chart")](https://exceljet.net/formulas/gantt-chart)

### [Gantt chart](https://exceljet.net/formulas/gantt-chart)

The trick with this approach is the calendar header (row 4), which is just a series of valid dates, formatted with the custom number format "d". With a static date in D4, you can use =D4+1 to populate the calendar. This makes it easy to set up a conditional formatting rule that compares the date...

[![Excel formula: Gantt chart with weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20gantt%20chart%20weekends.png "Excel formula: Gantt chart with weekends")](https://exceljet.net/formulas/gantt-chart-with-weekends)

### [Gantt chart with weekends](https://exceljet.net/formulas/gantt-chart-with-weekends)

The key to this approach is the calendar header (row 4), which is just a series of valid dates, formatted with the custom number format "d". With a hardcoded date in D4, you can use =D4+1 to populate the calendar. This allows you to set up a conditional formatting rule that compares the date in row...

[![Excel formula: Gantt chart by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/gantt%20chart%20by%20week.png "Excel formula: Gantt chart by week")](https://exceljet.net/formulas/gantt-chart-by-week)

### [Gantt chart by week](https://exceljet.net/formulas/gantt-chart-by-week)

In the example shown, row 5 is a header row and which contains a series of valid dates, formatted with the custom number format "d". With a static date in D5, you can use this formula in E5 (copied across) to populate the calendar header in row 5: =D5+7 // header row This makes it easy to set up a...

[![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")](https://exceljet.net/formulas/highlight-dates-between)

### [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and...

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20based%20on%20a%20different%20cell-thumb.png)](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

### [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

In this video, we'll look at how to apply conditional formatting to one cell based on values in another, using a formula. Let's take a look. The easiest way to apply conditional formatting is to apply rules directly to the cells you want to format. For example, if I want to highlight the average...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20with%20conditional%20formatting_thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

Using conditional formatting, It's easy to highlight cells that match a certain condition. However, it's a little trickier to highlight entire rows in a list that contains multiple columns. In this video, we'll show you how to use a formula with conditional formatting to highlight an entire row in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Gantt chart](https://exceljet.net/formulas/gantt-chart)
    
*   [Gantt chart with weekends](https://exceljet.net/formulas/gantt-chart-with-weekends)
    
*   [Gantt chart by week](https://exceljet.net/formulas/gantt-chart-by-week)
    
*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    

### Articles

*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    

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