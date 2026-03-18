# Highlight blank cells - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-blank-cells

---

[Skip to main content](https://exceljet.net/formulas/highlight-blank-cells#main-content)

[](https://exceljet.net/formulas/highlight-blank-cells#)

*   [Previous](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)
    
*   [Next](https://exceljet.net/formulas/highlight-bottom-values)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight blank cells
=====================

by Dave Bruns · Updated 8 Feb 2024

Related functions 
------------------

[ISBLANK](https://exceljet.net/functions/isblank-function)

[LEN](https://exceljet.net/functions/len-function)

![Excel formula: Highlight blank cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/highlight_blank_cells.png "Excel formula: Highlight blank cells")

Summary
-------

To highlight blank cells (i.e. empty cells) with conditional formatting, you can use a simple formula based on the [ISBLANK function](https://exceljet.net/functions/isblank-function)
. In the example shown, the formula used to highlight blank cells is:

    =ISBLANK(C5)

When this formula returns TRUE, it triggers a Conditional Formatting rule that applies a bright fill color to empty cells in the range C5:J16. This makes it easy to see at a glance which students are missing quiz scores. The formatting is dynamic — if the data changes, the highlighting will automatically update.

Generic formula
---------------

    =ISBLANK(A1)

Explanation 
------------

In this example, the goal is to highlight empty cells in the range C5:J16 with conditional formatting. This is a quick and easy way to locate missing values in a data set. To apply a conditional formatting rule to highlight empty cells, follow these steps:

1.  Select the range that contains empty cells you want to highlight (C5:J16 in this case).
2.  On the Home tab of the ribbon, click Conditional Formatting, then New Rule.
3.  In the list of options for rule type, select "Use a formula to determine which cells to format".
4.  In the input area, add the following formula: =ISBLANK(C5)
5.  Click the Format button and configure the desired formatting.

The result should be a Conditional Formatting rule like this:

![A conditional formatting rule to highlight blank cells](https://exceljet.net/sites/default/files/images/formulas/inline/highlight_blank_cells_conditional_formatting_rule.png "A conditional formatting rule to highlight blank cells")

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. So, in this case, the formula =ISBLANK(C5) is evaluated for each cell in C5:J16. Because C5 is entered as a relative address, the address will be updated each time the formula is applied, and ISBLANK() is run on each cell in the range. The TRUE or FALSE result for each cell is what triggers the rule.

### Empty vs. blank

The ISBLANK function only returns TRUE if a cell contains no value. If a cell contains a formula that returns an [empty string](https://exceljet.net/glossary/empty-string)
 (""), the result may _look like an empty cell_, but ISBLANK will return FALSE because the cell contains a formula. As a result, the cell won't be highlighted. If you want to highlight cells that contain an empty string ("") returned by a formula, you can use this formula instead:

    =LEN(C5)=0
    

The [LEN function](https://exceljet.net/functions/len-function)
 returns the length of a text string as a number. A cell that contains an empty string ("") will have a length of zero, so the formula will return TRUE for cells that are truly empty and cells that contain an empty string ("") returned by a formula.

### Not blank

To conditionally format cells that are not blank, you can use a formula like this:

    =NOT(ISBLANK(A1))
    

The [NOT function](https://exceljet.net/functions/not-function)
 reverses the logic.

Related functions
-----------------

[![Excel ISBLANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isblank%20function.png "Excel ISBLANK function")](https://exceljet.net/functions/isblank-function)

### [ISBLANK Function](https://exceljet.net/functions/isblank-function)

The Excel ISBLANK function returns TRUE when a cell is empty, and FALSE when a cell is not empty. For example, if A1 contains "apple", ISBLANK(A1) returns FALSE.

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

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

### Functions

*   [ISBLANK Function](https://exceljet.net/functions/isblank-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    

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