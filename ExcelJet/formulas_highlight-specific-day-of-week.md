# Highlight specific day of week - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-specific-day-of-week

---

[Skip to main content](https://exceljet.net/formulas/highlight-specific-day-of-week#main-content)

[](https://exceljet.net/formulas/highlight-specific-day-of-week#)

*   [Previous](https://exceljet.net/formulas/highlight-rows-with-dates-between)
    
*   [Next](https://exceljet.net/formulas/highlight-top-values)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight specific day of week
==============================

by Dave Bruns · Updated 26 Jan 2023

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7693/download?token=-OvLvSly)
 (16.25 KB)

![Excel formula: Highlight specific day of week](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/highlight_specific_day_of_week.png "Excel formula: Highlight specific day of week")

Summary
-------

To highlight dates that land on a specific day of week (i.e. Mondays, Tuesdays, Wednesdays, etc.) with conditional formatting, you can use a formula based on the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, rows that contain Mondays are highlighted with the following formula:

    =TEXT($B5,"ddd")=$F$5
    

When a different day is selected with the dropdown menu in cell F5, the highlighting will instantly update.

Generic formula
---------------

    =TEXT(A1,"ddd")=day

Explanation 
------------

In this example, the goal is to highlight rows in the data shown when the date is a specific day of week. The target day of week is a variable selected with a dropdown menu in cell F5, which contains abbreviated day names. This problem can be easily solved by applying conditional formatting with a formula based on the TEXT function. The dropdown menu is implemented with [data validation](https://exceljet.net/glossary/data-validation)
.

### TEXT function

The [TEXT function](https://exceljet.net/functions/text-function)
 returns a number formatted as text, using the [number format](https://exceljet.net/glossary/number-format)
 provided. You can use the TEXT function to convert a valid Excel date into a text value with any standard date formatting. For example, with the date December 1, 2022 in cell A1, the TEXT function will return the following results:

    =TEXT(A1,"mmmm") // returns "December"
    =TEXT(A1,"dd") // returns "01"
    =TEXT(A1,"yyyy") // returns "2022"
    =TEXT(A1,"dddd") // returns "Thursday"
    =TEXT(A1,"ddd") // returns "Thu"

It is the last example above that we care about in this problem. We can use the abbreviated day name for each date to match against the target date in F5.

### Test for day of week

To highlight a specific day of week, we need a formula that will return TRUE when a date lands on the day selected in cell F5. We can do this with the TEXT function like this:

    =TEXT(B5,"ddd")=$F$5
    

The TEXT function extracts an abbreviated day name from the date in B5. When the value returned by TEXT is equal to the target day in cell F5 (which is also abbreviated) the formula will return TRUE. When the result from TEXT is different, the formula will return FALSE. This is what we need to trigger a conditional formatting rule.

### Define the rule

The next step is to define the conditional formatting rule itself. Because we want to highlight entire rows and not just dates, we will apply the rule to all data. With the range B5:C16 selected, navigate to Home > Conditional Formatting > New rule. Then select "Use a formula to determine which cells to format". Next, enter this formula in the formula area:

    =TEXT($B5,"ddd")=$F$5

Then set the desired format, which in this example is a light orange fill. At this point, the conditional formatting rule should look like this:

![Conditional formatting rule to highlight specific day of week](https://exceljet.net/sites/default/files/images/formulas/inline/highlight_specific_day_of_week_cf_rule.png "Conditional formatting rule to highlight specific day of week")

Note in this version of the formula, $B5 is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 with the column locked. We do this because we want to make sure that we are always testing just the date value in column B, even as the conditional formatting rule is applied to column C. The row is relative, because it needs to change as the rule is applied to data in different rows. We use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 for $F$5 because we need that value to remain fixed as the rule is applied to all cells in the data.

Video: [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

Related formulas
----------------

[![Excel formula: Highlight dates that are weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight_dates_that_are_weekends.png "Excel formula: Highlight dates that are weekends")](https://exceljet.net/formulas/highlight-dates-that-are-weekends)

### [Highlight dates that are weekends](https://exceljet.net/formulas/highlight-dates-that-are-weekends)

In this example, the goal is to highlight dates that occur on weekends. In other words, we want to highlight dates that land on either Saturday or Sunday. This problem can be easily solved by applying conditional formatting with a formula based on the WEEKDAY function together with the OR function...

[![Excel formula: Highlight dates greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20greater%20than.png "Excel formula: Highlight dates greater than")](https://exceljet.net/formulas/highlight-dates-greater-than)

### [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)

The DATE function creates a proper Excel date with given year, month, and day values. Then, it's simply a matter of comparing each date in the range with the date created with DATE. The reference B4 is fully relative, so will update as the rule is applied to each cell in the range, and any dates...

[![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")](https://exceljet.net/formulas/highlight-dates-between)

### [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and...

[![Excel formula: Highlight dates in same month and year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20in%20same%20month%20and%20year.png "Excel formula: Highlight dates in same month and year")](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)

### [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)

This formula uses the TEXT function to concatenate the month and year of each date. Then, the two dates are tested for equality. TEXT is a useful function that allows you to convert a number to text in the text format of your choice. In this case the format is the custom date format "myyyy", which...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

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

*   [Highlight dates that are weekends](https://exceljet.net/formulas/highlight-dates-that-are-weekends)
    
*   [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)
    
*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    
*   [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    

### Articles

*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    
*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    

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