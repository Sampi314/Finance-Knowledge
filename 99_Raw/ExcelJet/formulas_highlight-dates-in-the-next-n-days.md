# Highlight dates in the next N days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-dates-in-the-next-n-days

---

[Skip to main content](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days#main-content)

[](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days#)

*   [Previous](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)
    
*   [Next](https://exceljet.net/formulas/highlight-dates-that-are-weekends)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight dates in the next N days
==================================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Highlight dates in the next N days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20dates%20in%20the%20next%20n%20days.png "Excel formula: Highlight dates in the next N days")

Summary
-------

If you want to highlight dates that occur in the next N days with conditional formatting, you can do so with a formula that uses the TODAY function with AND. This is a great way to visually flag things like expiration dates, deadlines, upcoming events, and dates relative to the current date.

For example, if you have dates in the range B4:G11, and want to highlight cells that occur in the next 30 days, select the range and create a new CF rule that uses this formula:

    =AND(B4>TODAY(),B4<=(TODAY()+30))
    

_Note: it's important that CF formulas be entered relative to the "active cell" in the selection, which is assumed to be B4 in this case._

Once you save the rule, you'll see the dates occurring in the next 30 days highlighted.

Generic formula
---------------

    =AND(A1>TODAY(),A1<=(TODAY()+days))

Explanation 
------------

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The TODAY function returns the current date. Dates in Excel are simply large serial numbers, so you can create a new relative date by adding or subtracting days. TODAY() + 30 creates a new date 30 days in the future, so when a days is greater than today and less than today + 30, both conditions are true, and the AND function returns true, triggering the rule.

### Variable days

Of course, you can adjust days to any value you like:

    =AND(B4>TODAY(),B4<=(TODAY()+7)) // next 7 days
    =AND(B4>TODAY(),B4<=(TODAY()+45)) // next 45 days
    

### Use other cells for input

You don't need to hard-code the dates into the rule. To make a more flexible rule, you can use other cells like variables in the formula. For example, you can name cell E2 "days" and rewrite the formula like so:

    =AND(B4>TODAY(),B4<=(TODAY()+days))
    

When you change either date, the conditional formatting rule will respond instantly. By using other cells for input, and naming them as named ranges, you make the conditional formatting interactive and the formula is simpler and easier to read.

Related formulas
----------------

[![Excel formula: Highlight dates greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20greater%20than.png "Excel formula: Highlight dates greater than")](https://exceljet.net/formulas/highlight-dates-greater-than)

### [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)

The DATE function creates a proper Excel date with given year, month, and day values. Then, it's simply a matter of comparing each date in the range with the date created with DATE. The reference B4 is fully relative, so will update as the rule is applied to each cell in the range, and any dates...

[![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")](https://exceljet.net/formulas/highlight-dates-between)

### [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and...

[![Excel formula: Conditional formatting date past due](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20date%20past%20due.png "Excel formula: Conditional formatting date past due")](https://exceljet.net/formulas/conditional-formatting-date-past-due)

### [Conditional formatting date past due](https://exceljet.net/formulas/conditional-formatting-date-past-due)

In this example, we want to apply three different colors, depending on how much the original date varies from the current date: Green if the variance is less than 3 days Yellow if the variance is between 3 and 10 days Red if the variance is greater than 10 days For each rule, we calculate a...

Related functions
-----------------

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20based%20on%20a%20different%20cell-thumb.png)](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

### [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

In this video, we'll look at how to apply conditional formatting to one cell based on values in another, using a formula. Let's take a look. The easiest way to apply conditional formatting is to apply rules directly to the cells you want to format. For example, if I want to highlight the average...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20with%20conditional%20formatting_thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

Using conditional formatting, It's easy to highlight cells that match a certain condition. However, it's a little trickier to highlight entire rows in a list that contains multiple columns. In this video, we'll show you how to use a formula with conditional formatting to highlight an entire row in...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)
    
*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    
*   [Conditional formatting date past due](https://exceljet.net/formulas/conditional-formatting-date-past-due)
    

### Functions

*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    

### Articles

*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    

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