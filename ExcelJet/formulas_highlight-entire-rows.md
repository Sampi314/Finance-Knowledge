# Highlight entire rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-entire-rows

---

[Skip to main content](https://exceljet.net/formulas/highlight-entire-rows#main-content)

[](https://exceljet.net/formulas/highlight-entire-rows#)

*   [Previous](https://exceljet.net/formulas/highlight-duplicate-values)
    
*   [Next](https://exceljet.net/formulas/highlight-every-other-row)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight entire rows
=====================

by Dave Bruns · Updated 16 May 2024

![Excel formula: Highlight entire rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20entire%20rows.png "Excel formula: Highlight entire rows")

Summary
-------

To highlight entire rows with conditional formatting when a value meets specific criteria, use a formula with a [mixed reference](https://exceljet.net/glossary/mixed-reference)
 that locks the column. In the example shown, all rows where the owner is "bob" are highlighted with the following formula applied to B5:E12:

     =$D5="Bob"
    

_Note: CF formulas are entered relative to the "active cell" in the selection, B5 in this case._

Generic formula
---------------

    =($A1=criteria)

Explanation 
------------

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the address of the active cell (B5) is used for the row (5) and entered as a [mixed address](https://exceljet.net/glossary/mixed-reference)
, with column D locked and the row left relative. When the rule is evaluated for each of the 40 cells in B5:E12, the row will change, but the column will not.

Effectively, this causes the rule to ignore values in columns B, C, and E and only test values in column D. When the value in column D for in a given row is "Bob", the rule will return TRUE for all cells in that row and formatting will be applied to the entire row.

### Using other cells as inputs

Note that you don't have to hard-code any values that might change into the rule. Instead you can use another cell as an "input" cell to hold the value so that you can easily change it later. For example, in this case, you could put "Bob" into cell D2 and then rewrite the formula like so:

    =$D5=$D$2
    

You can then change D2 to any priority you like, and the conditional formatting rule will respond instantly. Just make sure you use an absolute address to keep the input cell address from changing.

### Named ranges for a cleaner syntax

Another way to lock references is to use [named ranges](https://exceljet.net/articles/named-ranges)
, since named ranges are automatically absolute. For example, if you name D2 "owner", you can rewrite the formula with a cleaner syntax as follows:

    =$D5=owner
    

This makes the formula easier to read and understand.

Related formulas
----------------

[![Excel formula: Highlight duplicate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20duplicate%20rows.png "Excel formula: Highlight duplicate rows")](https://exceljet.net/formulas/highlight-duplicate-rows)

### [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)

In the formula, COUNTIFS counts the number of times each value in a cell appears in its "parent" column. By definition, each value must appear at least once, so when the count > 1, the value must be a duplicate. The references are carefully locked so the formula will return true only when all 3...

[![Excel formula: Highlight row and column intersection exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20row%20and%20column%20intersection%20exact%20match.png "Excel formula: Highlight row and column intersection exact match")](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)

### [Highlight row and column intersection exact match](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)

Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, cell B3 in this case. To highlight matching rows, we use this logical expression: $B4=$K$5 The reference to B4 is mixed , with the column locked and row unlocked, so that...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20with%20conditional%20formatting_thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

Using conditional formatting, It's easy to highlight cells that match a certain condition. However, it's a little trickier to highlight entire rows in a list that contains multiple columns. In this video, we'll show you how to use a formula with conditional formatting to highlight an entire row in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

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

*   [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)
    
*   [Highlight row and column intersection exact match](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
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