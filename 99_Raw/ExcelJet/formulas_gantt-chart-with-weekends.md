# Gantt chart with weekends - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/gantt-chart-with-weekends

---

[Skip to main content](https://exceljet.net/formulas/gantt-chart-with-weekends#main-content)

[](https://exceljet.net/formulas/gantt-chart-with-weekends#)

*   [Previous](https://exceljet.net/formulas/gantt-chart-time-schedule)
    
*   [Next](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Gantt chart with weekends
=========================

by Dave Bruns · Updated 30 Oct 2023

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

![Excel formula: Gantt chart with weekends](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/conditional%20formatting%20gantt%20chart%20weekends.png "Excel formula: Gantt chart with weekends")

Summary
-------

To build a Gantt chart with weekends shaded, you can use Conditional Formatting with a formula based on the weekday function.In the example shown, the formula applied the calendar, starting at D4, is:

    =WEEKDAY(D$4,2)>5
    

_Note: this formula deals with weekend shading only. To see how to build the date bars with conditional formatting, see [this article](https://exceljet.net/formulas/gantt-chart)
._

Generic formula
---------------

    =WEEKDAY(date,2)>5

Explanation 
------------

The key to this approach is the calendar header (row 4), which is just a series of valid dates, formatted with the custom number format "d". With a hardcoded date in D4, you can use =D4+1 to populate the calendar. This allows you to set up a conditional formatting rule that compares the date in row 4 with the dates in columns B and C.

To shade days that are weekends, we are using a formula based on the [weekday function](https://exceljet.net/functions/weekday-function)
. By default, the weekday function returns a number between 1 and 7 that corresponds to days of the week, where Sunday is 1 and Saturday is 7. However, by adding the optional second argument called "return type" with a value of 2, the numbering scheme changes so that Monday is 1 and Saturday and Sunday are 6 and 7, respectively.

As a result, to return TRUE for dates that are either Saturday or Sunday, we only need to test for numbers greater than 5. The conditional formatting formula applied to the calendar area (starting with D4) looks like this:

    =WEEKDAY(D$4,2)>5
    

The reference to D4 is [mixed](https://exceljet.net/glossary/mixed-reference)
, with the row locked so that the formula continues to evaluate the dates in the header for all rows in the calendar grid.

Related formulas
----------------

[![Excel formula: Gantt chart](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20gantt%20chart.png "Excel formula: Gantt chart")](https://exceljet.net/formulas/gantt-chart)

### [Gantt chart](https://exceljet.net/formulas/gantt-chart)

The trick with this approach is the calendar header (row 4), which is just a series of valid dates, formatted with the custom number format "d". With a static date in D4, you can use =D4+1 to populate the calendar. This makes it easy to set up a conditional formatting rule that compares the date...

[![Excel formula: Gantt chart by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/gantt%20chart%20by%20week.png "Excel formula: Gantt chart by week")](https://exceljet.net/formulas/gantt-chart-by-week)

### [Gantt chart by week](https://exceljet.net/formulas/gantt-chart-by-week)

In the example shown, row 5 is a header row and which contains a series of valid dates, formatted with the custom number format "d". With a static date in D5, you can use this formula in E5 (copied across) to populate the calendar header in row 5: =D5+7 // header row This makes it easy to set up a...

[![Excel formula: Highlight dates that are weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight_dates_that_are_weekends.png "Excel formula: Highlight dates that are weekends")](https://exceljet.net/formulas/highlight-dates-that-are-weekends)

### [Highlight dates that are weekends](https://exceljet.net/formulas/highlight-dates-that-are-weekends)

In this example, the goal is to highlight dates that occur on weekends. In other words, we want to highlight dates that land on either Saturday or Sunday. This problem can be easily solved by applying conditional formatting with a formula based on the WEEKDAY function together with the OR function...

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

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
    
*   [Gantt chart by week](https://exceljet.net/formulas/gantt-chart-by-week)
    
*   [Highlight dates that are weekends](https://exceljet.net/formulas/highlight-dates-that-are-weekends)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    

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