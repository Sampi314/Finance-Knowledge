# Highlight integers only - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-integers-only

---

[Skip to main content](https://exceljet.net/formulas/highlight-integers-only#main-content)

[](https://exceljet.net/formulas/highlight-integers-only#)

*   [Previous](https://exceljet.net/formulas/highlight-every-other-row)
    
*   [Next](https://exceljet.net/formulas/highlight-many-matching-values)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight integers only
=======================

by Dave Bruns · Updated 6 Jul 2021

Related functions 
------------------

[MOD](https://exceljet.net/functions/mod-function)

![Excel formula: Highlight integers only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20integers%20only.png "Excel formula: Highlight integers only")

Summary
-------

To highlight numbers that are integers, you can use a simple formula based on the MOD function. In the example shown, conditional formatting has been applied to the range B4:G11 using this formula:

    =MOD(B4,1)=0
    

_Note: it's important that CF formulas be entered relative to the "active cell" in the selection, which is assumed to be B4 in this case._

Once you save the rule, you'll see only values that are integers (whole numbers) highlighted.

Generic formula
---------------

    =MOD(A1,1)=0

Explanation 
------------

The MOD function returns the remainder after division. With a divisor of 1, MOD will return zero for any whole number.

We use this fact to construct a simple formula that tests the result of MOD. When the result is zero (i.e. when the number is an integer) the formula returns TRUE, triggering the conditional formatting.

When the result is not zero (i.e. the number has a decimal component, and dividing by 1 leaves remainder) the formula returns FALSE.

Related formulas
----------------

[![Excel formula: Highlight unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20unique%20values.png "Excel formula: Highlight unique values")](https://exceljet.net/formulas/highlight-unique-values)

### [Highlight unique values](https://exceljet.net/formulas/highlight-unique-values)

The COUNTIF function counts the number of times each value appears in the data range. By definition, each value must appear at least once, so when the count equals 1, the value is unique. When the count is 1, the formula returns TRUE and triggers the rule. Conditional formatting is evaluated for...

[![Excel formula: Get integer part of a number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20integer%20part%20of%20a%20number.png "Excel formula: Get integer part of a number")](https://exceljet.net/formulas/get-integer-part-of-a-number)

### [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)

With TRUNC, no rounding takes place. The TRUNC function simply slices off the decimal part of the number with default settings. TRUNC actually takes an optional second argument to specify the precision of truncation, but when you don't supply this optional argument, it is assumed to be zero, and...

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

*   [Highlight unique values](https://exceljet.net/formulas/highlight-unique-values)
    
*   [Get integer part of a number](https://exceljet.net/formulas/get-integer-part-of-a-number)
    

### Functions

*   [MOD Function](https://exceljet.net/functions/mod-function)
    

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