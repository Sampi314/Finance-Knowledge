# Conditional formatting date past due - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/conditional-formatting-date-past-due

---

[Skip to main content](https://exceljet.net/formulas/conditional-formatting-date-past-due#main-content)

[](https://exceljet.net/formulas/conditional-formatting-date-past-due#)

*   [Previous](https://exceljet.net/formulas/conditional-formatting-column-is-blank)
    
*   [Next](https://exceljet.net/formulas/conditional-formatting-dates-overlap)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Conditional formatting date past due
====================================

by Dave Bruns · Updated 26 Jun 2020

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6175/download?token=4iNEVJb1)
 (14.12 KB)

![Excel formula: Conditional formatting date past due](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/conditional%20formatting%20date%20past%20due.png "Excel formula: Conditional formatting date past due")

Summary
-------

To highlight dates that are "past due" you can use a conditional formatting rule that checks if the variance between two dates is greater than a certain number of days. In the example shown, three conditional formatting rules have been applied to the range D5:C12 with these formulas:

    =(D5-C5)<3 // rule 1 (green)
    =(D5-C5)<10 // rule 2 (yellow)
    =(D5-C5)>=10 // rule 3 (red)
    

_Note: conditional formatting rules are evaluated relative to the upper left cell in the selection at the time the rule is created, in this case D5._

### Calculating variance in days

The variances in column E are calculated by subtracting the original date from the current date with this formula:

    =D5-C5
    

The result is the difference in days between the original date and the current date. A positive difference represents a late date (i.e. a "slip" in the schedule). A negative difference indicates the current date is ahead of schedule. This works, because [Excel dates are serial numbers](https://exceljet.net/glossary/excel-date)
.

The variance shown in column E is for reference only in this example, and is not used by the conditional formatting rules. However, if you treat column E as a [helper column](https://exceljet.net/glossary/helper-column)
, you could write simpler conditional formatting rules that use the variance directly.

Generic formula
---------------

    =(date2-date1)>n

Explanation 
------------

In this example, we want to apply three different colors, depending on how much the original date varies from the current date:

1.  Green if the variance is less than 3 days
2.  Yellow if the variance is between 3 and 10 days
3.  Red if the variance is greater than 10 days

For each rule, we calculate a variance by subtracting the original date from the "current" date (as explained above). Then we check the result with a logical expression. When an expression returns TRUE, the conditional formatting is triggered.

Because we want three separate colors, each with a logical test, we'll need three separate conditional formatting rules. The screen below shows how the rules have been configured to apply the green, yellow, and red formatting. Note the first two rules have "stop if true" ticked:

![Rules for formatting dates past due](https://exceljet.net/sites/default/files/images/formulas/inline/conditional%20formatting%20date%20past%20due%20rules.png "Rules for formatting dates past due")

Rules are evaluated in the order shown. Rule 1 tests if the variance is less than 3 days. Rule 2 checks if the variance is less than 10 days. Rule 3 checks if the variance is greater than or equal to 10 days. Both rule 1 and rule 2 have "stop if true" enabled. When either rule returns TRUE, Excel will stop checking additional rules.

### Overdue by n days from today

You might want to compare a due date to today's date. To test if dates are overdue by at least n days from today, you can use a formula like this:

    =(TODAY()-date)>=n
    

This formula will return TRUE only when a date is at least n days in the past. When a date is in the future, the difference will be a negative number, so the rule will never fire.

For more information on building formula criteria, see [50+ formula criteria examples](https://exceljet.net/articles/how-to-use-formula-criteria)
.

Related formulas
----------------

[![Excel formula: Highlight dates in the next N days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20in%20the%20next%20n%20days.png "Excel formula: Highlight dates in the next N days")](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)

### [Highlight dates in the next N days](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The TODAY function returns the current date. Dates in Excel are simply large serial numbers, so you can create a new relative date by adding or subtracting days. TODAY() + 30 creates a new date 30 days...

Related functions
-----------------

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20with%20conditional%20formatting_thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

Using conditional formatting, It's easy to highlight cells that match a certain condition. However, it's a little trickier to highlight entire rows in a list that contains multiple columns. In this video, we'll show you how to use a formula with conditional formatting to highlight an entire row in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20based%20on%20a%20different%20cell-thumb.png)](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

### [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

In this video, we'll look at how to apply conditional formatting to one cell based on values in another, using a formula. Let's take a look. The easiest way to apply conditional formatting is to apply rules directly to the cells you want to format. For example, if I want to highlight the average...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight dates in the next N days](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)
    

### Functions

*   [TODAY Function](https://exceljet.net/functions/today-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    

### Articles

*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    
*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Conditional Formatting](https://exceljet.net/training/conditional-formatting)
    

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