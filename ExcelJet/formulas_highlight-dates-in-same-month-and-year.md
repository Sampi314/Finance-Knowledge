# Highlight dates in same month and year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-dates-in-same-month-and-year

---

[Skip to main content](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year#main-content)

[](https://exceljet.net/formulas/highlight-dates-in-same-month-and-year#)

*   [Previous](https://exceljet.net/formulas/highlight-dates-greater-than)
    
*   [Next](https://exceljet.net/formulas/highlight-dates-in-the-next-n-days)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight dates in same month and year
======================================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Highlight dates in same month and year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20dates%20in%20same%20month%20and%20year.png "Excel formula: Highlight dates in same month and year")

Summary
-------

If you want to use conditional formatting to highlight dates that are in the same month and year as another date, you can use a simple formula based on the TEXT function.

For example, if you have dates in the range B4:G11, and want to highlight dates that have the same month and year as the date June 1, 2015, select the range B4:G11 and create a new CF rule that uses this formula:

    =TEXT(B4,"myyyy")=TEXT(DATE(2015,6,1),"myyyy")
    

_Note: it's important that CF formulas be entered relative to the "active cell" in the selection, which is assumed to be B4 in this case._

Once you save the rule, you'll see all dates that occur in June 2015 highlighted.

Generic formula
---------------

    =TEXT(A1,"myyyy")=TEXT(date,"myyyy")

Explanation 
------------

This formula uses the TEXT function to concatenate the month and year of each date. Then, the two dates are tested for equality. TEXT is a useful function that allows you to convert a number to text in the text format of your choice. In this case the format is the custom date format "myyyy", which translates to: month number without leading zeros & 4-digit year. For example, if A1 contains the date 9-Jun-2015, TEXT(A1,"myyyy") will produce the text string "62016".

### Use other cells for input

You don't need to hard-code a date into the rule. To make a more flexible rule, you can use another cells like a variable. For example, if you name cell E2 "date", you can rewrite the formula like so:

    =TEXT(B4,"myyyy")=TEXT(date,"myyyy")
    

Then whenever you change the date in E2, the conditional formatting rule will update instantly. This simplifies the formula and makes it easier to read.

### Other formulas

There are several other formulas you could use to solve this problem. For a run-down of 5 different options, see: [5 formulas to highlight dates by month and year](https://exceljet.net/articles/5-formulas-to-highlight-dates-by-month-and-year)

Related formulas
----------------

[![Excel formula: Highlight dates greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20greater%20than.png "Excel formula: Highlight dates greater than")](https://exceljet.net/formulas/highlight-dates-greater-than)

### [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)

The DATE function creates a proper Excel date with given year, month, and day values. Then, it's simply a matter of comparing each date in the range with the date created with DATE. The reference B4 is fully relative, so will update as the rule is applied to each cell in the range, and any dates...

[![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")](https://exceljet.net/formulas/highlight-dates-between)

### [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and...

[![Excel formula: Count dates in given year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20dates%20in%20given%20year.png "Excel formula: Count dates in given year")](https://exceljet.net/formulas/count-dates-in-given-year)

### [Count dates in given year](https://exceljet.net/formulas/count-dates-in-given-year)

The YEAR function extracts the year from a valid Excel date . For example: =YEAR("15-Jun-2021") // returns 2021 In this case, we are giving YEAR and array of dates in the named range dates : YEAR(dates) Because dates contains 11 cells, we get back 11 results in an array like this: {2018;2017;2019;...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

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

*   [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)
    
*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    
*   [Count dates in given year](https://exceljet.net/formulas/count-dates-in-given-year)
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
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