# Highlight dates that are weekends - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-dates-that-are-weekends

---

[Skip to main content](https://exceljet.net/formulas/highlight-dates-that-are-weekends#main-content)

[](https://exceljet.net/formulas/highlight-dates-that-are-weekends#)

*   [Previous](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)
    
*   [Next](https://exceljet.net/formulas/highlight-duplicate-columns)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight dates that are weekends
=================================

by Dave Bruns · Updated 25 Jan 2023

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[OR](https://exceljet.net/functions/or-function)

![Excel formula: Highlight dates that are weekends](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight_dates_that_are_weekends.png "Excel formula: Highlight dates that are weekends")

Summary
-------

To highlight dates that land on weekends (i.e. Saturday or Sunday) with conditional formatting, you can use a simple formula based on the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
 and the [OR function](https://exceljet.net/functions/or-function)
. In the example shown, weekend dates are highlighted with the following formula:

    =OR(WEEKDAY(C5)=7,WEEKDAY(C5)=1)
    

Once you save the rule, you'll see all dates that are a Saturday or a Sunday highlighted by your rule. If the dates in the data are changed, the highlighting will update instantly.

Generic formula
---------------

    =OR(WEEKDAY(A1)=7,WEEKDAY(A1)=1)

Explanation 
------------

In this example, the goal is to highlight dates that occur on weekends. In other words, we want to highlight dates that land on either Saturday or Sunday. This problem can be easily solved by applying conditional formatting with a formula based on the WEEKDAY function together with the OR function.

### WEEKDAY function

The [WEEKDAY function](https://exceljet.net/functions/weekday-function)
 takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday. For example, with the date January 16, 2023 in cell A1, WEEKDAY will return 2, since the day of week is Monday:

    =WEEKDAY(A1) // returns 2

### OR function

The [OR function](https://exceljet.net/functions/or-function)
 returns TRUE if any given arguments evaluate to TRUE, and returns FALSE only if all supplied arguments evaluate to FALSE. For example, if cell A1 contains the text "apple", then:

    =OR(A1="pear",A1="apple") // returns TRUE
    =OR(A1="pear",A1="orange") // returns FALSE

We can combine the WEEKDAY function with the OR function to test for weekends as explained below.

### Test for weekends

To highlight weekends, we need a formula that will return TRUE if a date is either Saturday or Sunday. We can do that by combining the WEEKDAY function with the OR function like this:

    =OR(WEEKDAY(C5)=7,WEEKDAY(C5)=1)
    

Inside the OR function, WEEKDAY returns a number between 1 and 7. If WEEKDAY returns either 7 or 1, the OR function will return TRUE. In all other cases, OR will return FALSE. This is what we need to trigger a conditional formatting rule.

### Define the rule

The next step is to define the conditional formatting rule itself. With the range C5:C16 selected, navigate to Home > Conditional Formatting > New rule. Then select "Use a formula to determine which cells to format". Next, enter the formula above in the formula area and set the desired format. At this point, the conditional formatting rule should look like this:

![Conditional formatting rule to highlight weekends](https://exceljet.net/sites/default/files/images/formulas/inline/Highlight_dates_that_are_weekends_cf_rule_0.png "Conditional formatting rule to highlight weekends")

Video: [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### Highlighting the entire row

The rule above will highlight dates in C5:C16 only. To highlight the entire row when a date is a weekend, start by selecting all data in the range B5:D16. Then use a modified formula that locks the date column:

    =OR(WEEKDAY($C5)=7,WEEKDAY($C5)=1)
    

Note in this version of the formula, $C5 is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 with the column locked. We do this because we want to make sure that the test for weekend dates is always applied to the dates in column C.

Video: [How to use a formula with conditional formatting](https://exceljet.net/videos/how-to-use-a-formula-with-conditional-formatting)

Related formulas
----------------

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

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

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

*   [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)
    
*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    
*   [Highlight dates in same month and year](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

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