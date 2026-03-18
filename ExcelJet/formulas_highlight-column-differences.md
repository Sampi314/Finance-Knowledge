# Highlight column differences - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-column-differences

---

[Skip to main content](https://exceljet.net/formulas/highlight-column-differences#main-content)

[](https://exceljet.net/formulas/highlight-column-differences#)

*   [Previous](https://exceljet.net/formulas/highlight-cells-that-equal)
    
*   [Next](https://exceljet.net/formulas/highlight-data-by-quartile)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight column differences
============================

by Dave Bruns · Updated 31 Oct 2023

Related functions 
------------------

[EXACT](https://exceljet.net/functions/exact-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: Highlight column differences](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20column%20differences.png "Excel formula: Highlight column differences")

Summary
-------

To highlight the differences between two columns of data with conditional formatting you can use a simple formula that uses the "not equal to" operator (e.g. <>) and mixed references. In the example shown, the formula used to highlight differences in the ranges B2:B11 and C2:C11 looks like this:

    =$B2<>$C2
    

_Note: with conditional formatting, it's important that the formula be entered relative to the "active cell" in the selection, which is assumed to be B2 in this case._

Generic formula
---------------

    =$A1<>$B1

Explanation 
------------

In this example, the goal is to highlight differences in two ranges, B2:B11 and C2:C11, using conditional formatting. To do this, we need to create a new conditional formatting rule, triggered by a formula, like this:

1.  Select the range B2:C11, starting at cell B2.
2.  Select Home > Conditional Formatting > New Rule
3.  Select "Use a formula to determine which cells to format"
4.  Enter the formula =$B2<>$C2 in the input area
5.  Set the desired format to highlight differences
6.  Save the rule

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 20 cells in the two columns of data.

The references to $B2 and $C2 are "[mixed references](https://exceljet.net/glossary/mixed-reference)
" - the column is locked, but the row is relative. This means only the row number will change as the formula is evaluated. Whenever two values in a row are not equal, the formula returns TRUE and the conditional formatting is applied.

### A case-sensitive option

Note that the "equals to" (=) and "not equals to" (<>) operators are not case-sensitive. If you need a case-sensitive comparison, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
 with NOT, like so:

    =NOT(EXACT($B2,$C2))
    

EXACT performs a case-sensitive comparison and returns TRUE when values match. The [NOT function](https://exceljet.net/functions/not-function)
 reverses this logic so that the formula returns TRUE only when the values don't match.

### Another approach

One problem with this approach is that if there is an extra or missing value in one column, or if the data is not sorted, many rows will be highlighted as different. Another approach is to count instances that appear in one range but do not appear in another. For details on this approach, see [highlight missing values](https://exceljet.net/formulas/highlight-missing-values)
.

Related formulas
----------------

[![Excel formula: Highlight missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20that%20don%27t%20exist.png "Excel formula: Highlight missing values")](https://exceljet.net/formulas/highlight-missing-values)

### [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)

This formula is evaluated for each of the 10 cells in A1:D10. A1 will change to the address of the cell being evaluated, while C1:C10 is entered as an absolute address, so it won't change at all. The key to this formula is the =0 at the end, which "flips" the logic of the formula. For each value in...

Related functions
-----------------

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

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

*   [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)
    

### Functions

*   [EXACT Function](https://exceljet.net/functions/exact-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    

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