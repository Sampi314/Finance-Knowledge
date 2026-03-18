# Conditional formatting last n rows - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/conditional-formatting-last-n-rows

---

[Skip to main content](https://exceljet.net/formulas/conditional-formatting-last-n-rows#main-content)

[](https://exceljet.net/formulas/conditional-formatting-last-n-rows#)

*   [Previous](https://exceljet.net/formulas/conditional-formatting-highlight-target-percentage)
    
*   [Next](https://exceljet.net/formulas/find-duplicate-values-in-two-columns)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Conditional formatting last n rows
==================================

by Dave Bruns · Updated 12 Jun 2020

![Excel formula: Conditional formatting last n rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/conditional%20formatting%20last%20n%20rows.png "Excel formula: Conditional formatting last n rows")

Summary
-------

To highlight the last n rows of a range or a table, you can use a formula based on the [ROW](https://exceljet.net/functions/row-function)
 and [ROWS function](https://exceljet.net/functions/rows-function)
. In the example shown, the formula used to apply conditional formatting to the data in B5:D15 is:

    =ROW()-INDEX(ROW(data),1,1)+1>ROWS(data)-n
    

where **data** (B5:D15) and **n** (F5) are [named ranges](https://exceljet.net/glossary/named-range)
. This rule highlights the last n rows in the data. When n is changed, the highlighting is automatically updated.

Generic formula
---------------

    =ROW()-INDEX(ROW(data),1,1)+1>ROWS(data)-n

Explanation 
------------

This example is based on the [formula explained in detail here](https://exceljet.net/formulas/last-n-rows)
:

    =ROW()-INDEX(ROW(data),1,1)+1>ROWS(data)-n
    

The formula uses the greater than [operator](https://exceljet.net/glossary/logical-operators)
 (>) to check row in the data. On the left, the formula calculates a "current row", normalized to begin at the number 1:

    =ROW()-INDEX(ROW(data),1,1)+1 // calculate current row
    

On the right, the formula generates a threshold number:

    ROWS(data)-n // calculate threshold
    

When the current row is greater than the threshold, the formula returns TRUE, triggering the conditional formatting.

### Conditional formatting rule

The conditional formatting rule is set up to use a formula like this:

![Conditional formatting last n rows rule](https://exceljet.net/sites/default/files/images/formulas/inline/conditional%20formatting%20last%20n%20rows%20rule.png "Conditional formatting last n rows rule")

### With a table

[You can't use a table name in a CF formula at present](https://exceljet.net/videos/conditional-formatting-formula-in-a-table)
. However, you can select or enter the table data range when creating the formula in the CF window, and Excel will keep the reference up to date as the table expands or shrinks.

Related formulas
----------------

[![Excel formula: Conditional formatting based on another cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Conditional%20formatting%20based%20on%20another%20cell.png "Excel formula: Conditional formatting based on another cell")](https://exceljet.net/formulas/conditional-formatting-based-on-another-cell)

### [Conditional formatting based on another cell](https://exceljet.net/formulas/conditional-formatting-based-on-another-cell)

Excel contains many built-in "presets" for highlighting values with conditional formatting, including a preset to highlight cells greater than a specific value. However, by using your own formula, you have more flexibility and control. In this example, a conditional formatting rule is set up to...

[![Excel formula: Highlight values between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20between.png "Excel formula: Highlight values between")](https://exceljet.net/formulas/highlight-values-between)

### [Highlight values between](https://exceljet.net/formulas/highlight-values-between)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

[![Excel formula: Highlight values greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/%20Highlight%20values%20greater%20than%20or%20less%20than.png "Excel formula: Highlight values greater than")](https://exceljet.net/formulas/highlight-values-greater-than)

### [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. So, in this case the formula =B4>100 is evaluated for each of the 40 cells in B4:G11. Because B4 is entered as a relative address, the...

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: Highlight entire rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20entire%20rows.png "Excel formula: Highlight entire rows")](https://exceljet.net/formulas/highlight-entire-rows)

### [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the address of the active cell (B5) is used for the row (5) and entered as a mixed address , with column D locked and the row...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20based%20on%20a%20different%20cell-thumb.png)](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

### [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

In this video, we'll look at how to apply conditional formatting to one cell based on values in another, using a formula. Let's take a look. The easiest way to apply conditional formatting is to apply rules directly to the cells you want to format. For example, if I want to highlight the average...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20with%20conditional%20formatting_thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

Using conditional formatting, It's easy to highlight cells that match a certain condition. However, it's a little trickier to highlight entire rows in a list that contains multiple columns. In this video, we'll show you how to use a formula with conditional formatting to highlight an entire row in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20mixed%20reference-thumb.png)](https://exceljet.net/videos/how-to-create-a-mixed-reference)

### [How to create a mixed reference](https://exceljet.net/videos/how-to-create-a-mixed-reference)

So what's a mixed reference? A mixed reference is a reference that's part relative and part absolute. Let's take a look. So, we've looked at both relative and absolute references, and also at a situation where we needed to use both at the same time. These are sometimes called "mixed references." A...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Conditional formatting based on another cell](https://exceljet.net/formulas/conditional-formatting-based-on-another-cell)
    
*   [Highlight values between](https://exceljet.net/formulas/highlight-values-between)
    
*   [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)
    
*   [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to create a mixed reference](https://exceljet.net/videos/how-to-create-a-mixed-reference)
    

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