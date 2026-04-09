# Highlight values between - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-values-between

---

[Skip to main content](https://exceljet.net/formulas/highlight-values-between#main-content)

[](https://exceljet.net/formulas/highlight-values-between#)

*   [Previous](https://exceljet.net/formulas/highlight-unprotected-cells)
    
*   [Next](https://exceljet.net/formulas/highlight-values-greater-than)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight values between
========================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Highlight values between](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20values%20between.png "Excel formula: Highlight values between")

Summary
-------

_Note: Excel contains many built-in "presets" for highlighting values above / below / between / equal to certain values, but if you want more flexibility you can apply conditional formatting using your own formula as explained in this article._

If you want to use conditional formatting to highlight cells that are "greater than X and less than Y", you can use a simple formula that returns TRUE when a value meets those conditions. For example, if you have numbers in the range B4:G11, and want to highlight cells with a numeric value over 60 and less than 90, select B4:G11 and create a conditional formatting rule that uses this formula:

    =AND(B4>=60,B4<=90)
    

It's important that the formula be entered relative to the "active cell" in the selection, which is assumed to be B4 in this case.

Also note that we are using greater than or equal to, and less than or equal to in order to include both the lower and upper values.

Generic formula
---------------

    =AND(A1>=lower,A1<=upper)

Explanation 
------------

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of the 40 cells in B4:G11 because B4 is entered as a fully relative address. Because we are using AND with two conditions, the formula returns TRUE only when both conditions return TRUE, triggering the conditional formatting.

### Using other cells as inputs

You don't have to hard-code the numbers into the rule and, if the numbers will change, it's better if you don't.

To make a more flexible, interactive conditional formatting rule, use other cells like variables in the formula. For example, if you want to use cell E2 for the lower limit, and cell G2 for the upper limit, you can use this formula:

    =AND(B4>=$E$2,A1<=$G$2)
    

You can then change the values in cells E2 and G2 to anything you like and the conditional formatting rule will respond instantly. You must use an absolute address for E2 and G2 to prevent these addresses from changing.

### With named ranges

A better way to lock these references is to use a named ranges, since named ranges are automatically absolute. If you name cell E2 "lower" and the cell G2 "upper", then you can write the conditional formatting formula like so:

    =AND(B4>=lower,B4<=upper)
    

Named ranges allow you to use a cleaner, more intuitive syntax.

Related formulas
----------------

[![Excel formula: Highlight values greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/%20Highlight%20values%20greater%20than%20or%20less%20than.png "Excel formula: Highlight values greater than")](https://exceljet.net/formulas/highlight-values-greater-than)

### [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. So, in this case the formula =B4>100 is evaluated for each of the 40 cells in B4:G11. Because B4 is entered as a relative address, the...

[![Excel formula: Highlight values not between X and Y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20NOT%20between.png "Excel formula: Highlight values not between X and Y")](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)

### [Highlight values not between X and Y](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

Related functions
-----------------

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

*   [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)
    
*   [Highlight values not between X and Y](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)
    

### Functions

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