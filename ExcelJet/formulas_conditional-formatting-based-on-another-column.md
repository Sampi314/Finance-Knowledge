# Conditional formatting based on another column - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/conditional-formatting-based-on-another-column

---

[Skip to main content](https://exceljet.net/formulas/conditional-formatting-based-on-another-column#main-content)

[](https://exceljet.net/formulas/conditional-formatting-based-on-another-column#)

*   [Previous](https://exceljet.net/formulas/conditional-formatting-based-on-another-cell)
    
*   [Next](https://exceljet.net/formulas/conditional-formatting-column-is-blank)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Conditional formatting based on another column
==============================================

by Dave Bruns · Updated 12 Jun 2020

![Excel formula: Conditional formatting based on another column](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Conditional%20formatting%20based%20on%20another%20column.png "Excel formula: Conditional formatting based on another column")

Summary
-------

To apply conditional formatting based on a value in another column, you can create a rule based on a simple formula. In the example shown, the formula used to apply conditional formatting to the range D5:D14 is:

    =$D5>$C5
    

This highlights values in D5:D14 that are greater than C5:C14. Note that both [references are mixed](https://exceljet.net/glossary/mixed-reference)
 in order to lock the column but allow the row to change.

Generic formula
---------------

    =$B1>$A1

Explanation 
------------

In this example, a conditional formatting rule highlights cells in the range D5:D14 when the value is greater than corresponding values in C5:C14. The formula used to create the rule is:

    =$D5>$C5
    

The rule is applied to the entire range D5:G14. The formula uses the greater than [operator](https://exceljet.net/glossary/logical-operators)
 (>) to evaluate each cell in D5:D14 against the corresponding cell in C5:C14. When the formula returns TRUE, the rule is triggered and the highlighting is applied.

![Conditional formatting rule applied to D5:D14](https://exceljet.net/sites/default/files/images/formulas/inline/Conditional%20formatting%20based%20on%20another%20column%20rules.png "Conditional formatting rule applied to D5:D14")

### Mixed references

The [mixed references](https://exceljet.net/glossary/mixed-reference)
 used in this formula ($D5, $C5) make this rule portable. You could use the same formula to highlight cells in B5:B14 instead of D5:D14, or even to [highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)
 based on the same logic.

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