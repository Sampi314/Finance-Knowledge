# Conditional formatting dates overlap - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/conditional-formatting-dates-overlap

---

[Skip to main content](https://exceljet.net/formulas/conditional-formatting-dates-overlap#main-content)

[](https://exceljet.net/formulas/conditional-formatting-dates-overlap#)

*   [Previous](https://exceljet.net/formulas/conditional-formatting-date-past-due)
    
*   [Next](https://exceljet.net/formulas/conditional-formatting-highlight-target-percentage)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Conditional formatting dates overlap
====================================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Conditional formatting dates overlap](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Conditional%20formatting%20dates%20overlap.png "Excel formula: Conditional formatting dates overlap")

Summary
-------

To highlight cells where dates overlap you can use conditional formatting with a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown the formula in cell E6 is:

    =SUMPRODUCT(($C6<=$D$5:$D$9)*($D6>=$C$5:$C$9))>1
    

This is the same formula used to highlight entire rows in the table using a formula-based conditional formatting rule.

Generic formula
---------------

    =SUMPRODUCT((start_date<=end_dates)*(end_date>=start_dates))>1

Explanation 
------------

Consider for a moment how overlapping dates work. For a project to overlap the dates of other projects, two conditions must be true:

1.  The start date must be less than or equal (<=) to at least one other end date and the list.
2.  The end date for the project must be greater than or equal to (>=) at least one other start date in the list.

If both of these conditions are true, the project dates must overlap with another project in that list. The SUMPRODUCT function is perfect for this kind of test because it handles array comparisons elegantly. To check a project start date against all end dates, we use this expression:

    ($C6<=$D$5:$D$9)
    

To check a project end date against all end dates, we use this expression:

    ($D6>=$C$5:$C$9)
    

The resulting arrays of TRUE FALSE values are multiplied by each other inside SUMPRODUCT. This coerces the TRUE and FALSE results into 1s and 0s automatically, so the formula is solved like this:

    =SUMPRODUCT({0;1;1;1;1}*{1;1;1;0;0})>1
    =SUMPRODUCT({0;1;1;0;0})>1
    =TRUE
    

Related formulas
----------------

[![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")](https://exceljet.net/formulas/highlight-dates-between)

### [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

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

*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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