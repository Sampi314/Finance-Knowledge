# Highlight cells that equal - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-cells-that-equal

---

[Skip to main content](https://exceljet.net/formulas/highlight-cells-that-equal#main-content)

[](https://exceljet.net/formulas/highlight-cells-that-equal#)

*   [Previous](https://exceljet.net/formulas/highlight-cells-that-end-with)
    
*   [Next](https://exceljet.net/formulas/highlight-column-differences)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight cells that equal
==========================

by Dave Bruns · Updated 22 Sep 2020

Related functions 
------------------

[EXACT](https://exceljet.net/functions/exact-function)

![Excel formula: Highlight cells that equal](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20cells%20that%20equal.png "Excel formula: Highlight cells that equal")

Summary
-------

To highlight cells equal to a specific value, you can use conditional formatting with a custom formula. In the example shown, the formula used to apply conditional formatting to the range C5:C11 is:

    =C5=$F$6
    

If the value in F6 is changed, the highlighting will update automatically.

Generic formula
---------------

    =A1="X"

Explanation 
------------

_Note: Excel contains many built-in "presets" for highlighting values with conditional formatting, including a preset to highlight cells that equal a specific value. However, for more flexibility, you can use your own formula, as explained in this article._

If you want to highlight cells that equal a specific value, you can use a simple formula that returns TRUE when the condition is met. For example, to highlight any cells in the range C5-C11 that contain the text "dog", you can use conditional formatting with this formula:

    =C5="Dog"
    

In the example shown we have placed the value we are looking for in cell F6, so it can be easily changed. The conditional formatting rule itself is using this formula:

    =C5=$F$6
    

This formula is just a simple comparison using the equal to [operator](https://exceljet.net/glossary/logical-operators)
 (=).

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 7 cells in C5:C11, and during evaluation C5 (entered as a [relative reference](https://exceljet.net/glossary/relative-reference)
) will change to the address of the cell being evaluated in the range where conditional formatting is applied.

The address of the cell that contains the search string (F6) is an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 ($F$6) so that it is "locked" and won't change as the formula is evaluated.

### Case sensitive option

By default a comparison is not case-sensitive. If you need to check case as well, you can use the [EXACT function](https://exceljet.net/functions/exact-function)
 like this:

    =EXACT(C5,$F$6)
    

Related formulas
----------------

[![Excel formula: Highlight cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20begin%20with.png "Excel formula: Highlight cells that begin with")](https://exceljet.net/formulas/highlight-cells-that-begin-with)

### [Highlight cells that begin with](https://exceljet.net/formulas/highlight-cells-that-begin-with)

In this example, the goal is to apply conditional formatting to cells that begin with specific text, which is entered in cell G2. The highlighting is done automatically with a conditional formatting rule applied to the range B4:G12. The rule type is "Use a formula to determine which cells to format...

[![Excel formula: Highlight cells that end with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20end%20with.png "Excel formula: Highlight cells that end with")](https://exceljet.net/formulas/highlight-cells-that-end-with)

### [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each cell in B4:G12, and the reference to B4 will change to the address of each cell being evaluated...

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: Highlight rows that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20rows%20that%20contain%20specific%20text.png "Excel formula: Highlight rows that contain")](https://exceljet.net/formulas/highlight-rows-that-contain)

### [Highlight rows that contain](https://exceljet.net/formulas/highlight-rows-that-contain)

The SEARCH function returns the position of the text you are looking for as a number (if it exists). Conditional formatting automatically treats any positive number as TRUE, so the rule is triggered whenever SEARCH returns a number. When SEARCH doesn't find the text you're looking for, it returns a...

Related functions
-----------------

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20based%20on%20a%20different%20cell-thumb.png)](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

### [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)

In this video, we'll look at how to apply conditional formatting to one cell based on values in another, using a formula. Let's take a look. The easiest way to apply conditional formatting is to apply rules directly to the cells you want to format. For example, if I want to highlight the average...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20with%20conditional%20formatting_thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

Using conditional formatting, It's easy to highlight cells that match a certain condition. However, it's a little trickier to highlight entire rows in a list that contains multiple columns. In this video, we'll show you how to use a formula with conditional formatting to highlight an entire row in...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Highlight cells that begin with](https://exceljet.net/formulas/highlight-cells-that-begin-with)
    
*   [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)
    
*   [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Highlight rows that contain](https://exceljet.net/formulas/highlight-rows-that-contain)
    

### Functions

*   [EXACT Function](https://exceljet.net/functions/exact-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    

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