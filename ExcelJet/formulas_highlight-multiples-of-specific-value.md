# Highlight multiples of specific value - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-multiples-of-specific-value

---

[Skip to main content](https://exceljet.net/formulas/highlight-multiples-of-specific-value#main-content)

[](https://exceljet.net/formulas/highlight-multiples-of-specific-value#)

*   [Previous](https://exceljet.net/formulas/highlight-missing-values)
    
*   [Next](https://exceljet.net/formulas/highlight-numbers-that-include-symbols)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight multiples of specific value
=====================================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Highlight multiples of specific value](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20multiples%20of%20specific%20value.png "Excel formula: Highlight multiples of specific value")

Summary
-------

To highlight numbers that are multiples of a another number with conditional formatting, you can use a simple formula based on the MOD function.

In the example shown, the formula used to highlight multiples of 9 is:

    =MOD(B4,$E$2)=0
    

_Note: formula is entered relative to the "active cell" in the selection, cell B4 in this case._

Generic formula
---------------

    =MOD(A1,value)=0

Explanation 
------------

Conditional formatting is evaluated for each cell in the range, relative to the upper left cell in the selection. In this case, the formula uses the MOD function to check the remainder of dividing the value in each cell, with the value in cell E2, which is 9. When the remainder is zero, we know that the value is an even multiple of the number 9, so the formula checks the result of MOD against zero.

When MOD returns zero, the expression returns TRUE and the conditional formatting applies. When MOD returns any other result, the expression returns FALSE conditional formatting is not applied.

Note E2 is input as an [absolute address](https://exceljet.net/glossary/absolute-reference)
 ($E$2) to prevent the reference from changing as the conditional formatting rule is evaluated across the selection B4:G11.

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

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

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

*   [MOD Function](https://exceljet.net/functions/mod-function)
    

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