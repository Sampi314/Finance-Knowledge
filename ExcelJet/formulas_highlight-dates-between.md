# Highlight dates between - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-dates-between

---

[Skip to main content](https://exceljet.net/formulas/highlight-dates-between#main-content)

[](https://exceljet.net/formulas/highlight-dates-between#)

*   [Previous](https://exceljet.net/formulas/highlight-data-by-quartile)
    
*   [Next](https://exceljet.net/formulas/highlight-dates-greater-than)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight dates between
=======================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[DATE](https://exceljet.net/functions/date-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")

Summary
-------

If you want to highlight dates between two dates with conditional formatting, you can use a simple formula that uses the AND and DATE functions together. For example, if you have dates in the range B4:G11, and want to highlight cells that contain a date greater than August 1st, 2015, and less than November 1, 2015, select the range and create a new CF rule that uses this formula:

    =AND(B4>=DATE(2015,8,1),B4<=DATE(2015,11,1))
    

_Note: it's important that CF formulas be entered relative to the "active cell" in the selection, which is assumed to be B4 in this case._

Once you save the rule, you'll see the dates between 8/1/2015 and 11/1/2015 are highlighted. Note we are including the start and end dates by using greater than or equal to (>=) and less than or equal to (<=)

Generic formula
---------------

    =AND(A1>=date1,A1<=date2)

Explanation 
------------

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and any dates that are both greater than 8/1/2015 _and_ less than 11/1/2015 will be highlighted.

### Use other cells for input

You don't need to hard-code the dates into the rule. To make a more flexible rule, you can use other cells like variables in the formula. For example, you can name cell E2 "start" and cell G2 "end", then rewrite the formula like so:

    =AND(B4>=start,B4<=end)
    

When you change either date, the conditional formatting rule will respond instantly. By using other cells for input, and naming them as named ranges, you make the conditional formatting interactive and the formula is simpler and easier to read.

Related formulas
----------------

[![Excel formula: Highlight dates greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20greater%20than.png "Excel formula: Highlight dates greater than")](https://exceljet.net/formulas/highlight-dates-greater-than)

### [Highlight dates greater than](https://exceljet.net/formulas/highlight-dates-greater-than)

The DATE function creates a proper Excel date with given year, month, and day values. Then, it's simply a matter of comparing each date in the range with the date created with DATE. The reference B4 is fully relative, so will update as the rule is applied to each cell in the range, and any dates...

Related functions
-----------------

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

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
    

### Functions

*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

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