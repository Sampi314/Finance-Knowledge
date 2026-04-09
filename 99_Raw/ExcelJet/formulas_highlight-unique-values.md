# Highlight unique values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-unique-values

---

[Skip to main content](https://exceljet.net/formulas/highlight-unique-values#main-content)

[](https://exceljet.net/formulas/highlight-unique-values#)

*   [Previous](https://exceljet.net/formulas/highlight-top-values)
    
*   [Next](https://exceljet.net/formulas/highlight-unprotected-cells)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight unique values
=======================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Highlight unique values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20unique%20values.png "Excel formula: Highlight unique values")

Summary
-------

_Excel contains many built-in "presets" for highlighting values with conditional formatting, including a preset to highlight unique values. However, if you want more flexibility, you can highlight unique values with your own formula, as explained in this article._

To highlight cells that contain unique values in a set of data, you can use a formula that returns TRUE when a value appears just once. For example, if you have values in the cells A1:D10, and want to highlight cells with duplicate values, you can use this formula:

    =COUNTIF($A$1:$D$10,A1)=1
    

_Note: with conditional formatting, the formula must be entered relative to the "active cell" in the selection, which is assumed to be A1 in this case._

Generic formula
---------------

    =COUNTIF(data,A1)=1

Explanation 
------------

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts the number of times each value appears in the data range. By definition, each value must appear at least once, so when the count equals 1, the value is unique. When the count is 1, the formula returns TRUE and triggers the rule.

Conditional formatting is evaluated for each cell that is applied to. When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the range we are using in COUNTIF is locked with an absolute address, but A1 is fully relative. So, the rule is evaluated for each of the 40 cells in A1:D10, and A1 will be updated to a new address 40 times (once per cell) while $A$1:$D$10 remains unchanged.

### Named ranges for a cleaner syntax

Another way to lock references is to a [named range](https://exceljet.net/articles/named-ranges)
 since named ranges are automatically absolute. For example, if you name the range A1:D10 "data", you can rewrite the rule with a cleaner syntax like so:

    =COUNTIF(data,A1)=1
    

Related formulas
----------------

[![Excel formula: Highlight duplicate values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20duplicate%20values.png "Excel formula: Highlight duplicate values")](https://exceljet.net/formulas/highlight-duplicate-values)

### [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)

COUNTIF simply counts the number of times each value appears in the range. When the count is more than 1, the formula returns TRUE and triggers the rule. When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

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

*   [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    

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