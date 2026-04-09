# Highlight bottom values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-bottom-values

---

[Skip to main content](https://exceljet.net/formulas/highlight-bottom-values#main-content)

[](https://exceljet.net/formulas/highlight-bottom-values#)

*   [Previous](https://exceljet.net/formulas/highlight-blank-cells)
    
*   [Next](https://exceljet.net/formulas/highlight-cells-that-begin-with)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight bottom values
=======================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

![Excel formula: Highlight bottom values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20bottom%20values.png "Excel formula: Highlight bottom values")

Summary
-------

To highlight the smallest (bottom) values in a set of data with conditional formatting, you can use a formula based on the [SMALL function](https://exceljet.net/functions/small-function)
. In the example shown, the formula used for conditional formatting is:

    =B4<=SMALL(data,input)
    

where **data** (B4:G11) and **input** (F2) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: Excel contains a conditional formatting "preset" that highlights bottom values. However, using a formula provides more flexibility._

Generic formula
---------------

    =A1<=SMALL(data,N)

Explanation 
------------

In this example, the goal is to highlight the 5 bottom values in B4:G11 where the number 5 is a variable set in cell F2.

This formula uses two named ranges: data (B4:G11) and input (F2). These are for readability and convenience only. If you don't want to use named ranges, make sure you use absolute references for both of these ranges in the formula.

This formula is based on the [SMALL function](https://exceljet.net/functions/small-function)
, which returns the nth smallest value from a range or array of values. The range appears as the first argument in SMALL, and the value for "n" appears as the second:

    SMALL(data,input)
    

In the example, the input value (F2) is 5, so SMALL will return the 5th smallest value in the data, which is 9. The formula then compares each value in the data range with 9, using the less than or equal to operator:

    =B4<=SMALL(data,input)
    =B4<=9
    

Any cell with a value less than or equal to 9 triggers the rule, and the conditional formatting is applied.

Related formulas
----------------

[![Excel formula: Highlight top values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20top%20values.png "Excel formula: Highlight top values")](https://exceljet.net/formulas/highlight-top-values)

### [Highlight top values](https://exceljet.net/formulas/highlight-top-values)

This formula uses two named ranges: data (B4:G11) and input (F2). These are for readability and convenience only. If you don't want to use named ranges, make sure you use absolute references for both of these ranges in the formula. This formula is based on the LARGE function , which returns the nth...

[![Excel formula: Highlight values greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/%20Highlight%20values%20greater%20than%20or%20less%20than.png "Excel formula: Highlight values greater than")](https://exceljet.net/formulas/highlight-values-greater-than)

### [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. So, in this case the formula =B4>100 is evaluated for each of the 40 cells in B4:G11. Because B4 is entered as a relative address, the...

[![Excel formula:  Highlight 3 smallest values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%203%20smallest%20values%20with%20criteria_0.png "Excel formula:  Highlight 3 smallest values with criteria")](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)

### [Highlight 3 smallest values with criteria](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)

Inside the AND function there are two logical criteria. The first is straightforward, and ensures that only cells that match the color in E5 are highlighted: $B3=$E$5 The second test is more complex: $C3<=SMALL(IF(color=$E$5,amount),3) Here, we filter amounts to make sure that only values...

Related functions
-----------------

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

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

*   [Highlight top values](https://exceljet.net/formulas/highlight-top-values)
    
*   [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)
    
*   [Highlight 3 smallest values with criteria](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)
    

### Functions

*   [SMALL Function](https://exceljet.net/functions/small-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    

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