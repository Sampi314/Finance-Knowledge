# Highlight cells that begin with - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-cells-that-begin-with

---

[Skip to main content](https://exceljet.net/formulas/highlight-cells-that-begin-with#main-content)

[](https://exceljet.net/formulas/highlight-cells-that-begin-with#)

*   [Previous](https://exceljet.net/formulas/highlight-bottom-values)
    
*   [Next](https://exceljet.net/formulas/highlight-cells-that-contain)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight cells that begin with
===============================

by Dave Bruns · Updated 30 Jan 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Highlight cells that begin with](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20cells%20that%20begin%20with.png "Excel formula: Highlight cells that begin with")

Summary
-------

To highlight cells that begin with certain text, you can use a formula based on the SEARCH function to trigger a conditional formatting rule. In the example shown, the formula used to highlight values that begin with "mi" is:

    =SEARCH($G$2,B4)=1
    

Here, G2 contains the text to search for, and B4 is the cell being evaluated. When this formula returns TRUE, it triggers a conditional formatting rule that applies a bright fill color to cells that begin with "mi", as seen in the worksheet above. The value in cell G2 can be changed at any time.

_Note: Excel contains many built-in "presets" for highlighting values with conditional formatting, including a preset to highlight cells that begin with specific text. However, defining a rule based on your own formula provides more flexibility and power. For example, you can easily adapt the formula to perform a case-sensitive match, as explained below._

Generic formula
---------------

    =SEARCH("substring",A1)=1

Explanation 
------------

In this example, the goal is to apply conditional formatting to cells that begin with specific text, which is entered in cell G2. The highlighting is done automatically with a conditional formatting rule applied to the range B4:G12. The rule type is "Use a formula to determine which cells to format". The formula looks like this:

    =SEARCH($G$2,B4)=1
    

G2 contains the text to search for, and B4 is the cell being tested. The formula is evaluated relative to the active cell at the time the rule is created for each cell in the range, which is B4. Each cell in B4:G12 is evaluated separately. Since B4 is entered as a [relative reference](https://exceljet.net/glossary/relative-reference)
, it will change to the cell being evaluated. Since cell G2 is entered as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 ($G$2), it will not change.

The formula uses the [SEARCH function](https://exceljet.net/functions/search-function)
 to match cells that begin with "mi". SEARCH returns a number that indicates a position when the text is found, and a #VALUE! error if the text is not found. When SEARCH returns the number 1, we know that the cell value _begins_ with "mi" because the location of the text is 1. The formula returns TRUE when the position is 1 and FALSE for any other value. For example, in cell B4, the formula evaluates like this:

When this formula returns TRUE, it triggers a conditional formatting rule that applies a bright fill color to cells that begin with "mi", as seen in the worksheet above. The value in cell G2 can be changed at any time and the conditional formatting will instantly update.

### With a named input cell

You can simplify the formula a bit by using a [named range](https://exceljet.net/glossary/named-range)
 for cell G2. For example, if we name G2 "input" the formula can be revised as follows:

    =SEARCH(input,B4)=1
    

The named range automatically behaves like an absolute reference so there is no need to lock any references.

### Case-sensitive option

The SEARCH is not case-sensitive so the text "MI" and "mi" will be evaluated in the same way. If you need a case-sensitive version of the formula, you can use a formula based on the [FIND function](https://exceljet.net/functions/find-function)
 instead:

    =FIND(input,B4)=1
    

Like the SEARCH function, FIND returns the position of the text as a number. However, FIND is automatically case-sensitive.

Related formulas
----------------

[![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")](https://exceljet.net/formulas/highlight-cells-that-contain)

### [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each...

[![Excel formula: Highlight cells that end with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20end%20with.png "Excel formula: Highlight cells that end with")](https://exceljet.net/formulas/highlight-cells-that-end-with)

### [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each cell in B4:G12, and the reference to B4 will change to the address of each cell being evaluated...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

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

*   [Highlight cells that contain](https://exceljet.net/formulas/highlight-cells-that-contain)
    
*   [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

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