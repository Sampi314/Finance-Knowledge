# Highlight cells that contain - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-cells-that-contain

---

[Skip to main content](https://exceljet.net/formulas/highlight-cells-that-contain#main-content)

[](https://exceljet.net/formulas/highlight-cells-that-contain#)

*   [Previous](https://exceljet.net/formulas/highlight-cells-that-begin-with)
    
*   [Next](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight cells that contain
============================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[SEARCH](https://exceljet.net/functions/search-function)

[FIND](https://exceljet.net/functions/find-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

![Excel formula: Highlight cells that contain](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20cells%20that%20contain%20specific%20text.png "Excel formula: Highlight cells that contain")

Summary
-------

_Note: Excel contains many built-in "presets" for highlighting values with conditional formatting, including a preset to highlight cells that contain specific text. However, if you want more flexibility, you can use your own formula, as explained in this article._

If you want to highlight cells that contain certain text, you can use a simple formula that returns TRUE when a cell contains the text (substring) that you specify.

For example, if you want to highlight any cells in the range B2:B11 that contain the text "dog", you can use:

    =ISNUMBER(SEARCH("dog",B2))
    

_Note: with conditional formatting, it's important that the formula be entered relative to the "active cell" in the selection, which is assumed to be B2 in this case._

Generic formula
---------------

    =ISNUMBER(SEARCH(substring,A1))

Explanation 
------------

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each of the 10 cells in B2:B11, and B2 will change to the address of the cell being evaluated each time, since B2 is relative.

The formula itself uses the SEARCH function to find the position of "dog" in the text. If "dog" exists, SEARCH will return a number that represents the position. If "dog" doesn't exist, SEARCH will return a #VALUE error. By wrapping ISNUMBER around SEARCH, we trap the error, so that the formula will only return TRUE when SEARCH returns a number. We don't care about the actual position, we only care if there is a position.

### Case sensitive option

SEARCH is not case-sensitive. If you need to check case as well, just replace SEARCH with FIND like so:

    =ISNUMBER(FIND("dog",A1))
    

### Looking for more than one thing?

If you want to highlight cells that contain one of many different strings, you can [use the formula described here](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)
.

Related formulas
----------------

[![Excel formula: Highlight cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20begin%20with.png "Excel formula: Highlight cells that begin with")](https://exceljet.net/formulas/highlight-cells-that-begin-with)

### [Highlight cells that begin with](https://exceljet.net/formulas/highlight-cells-that-begin-with)

In this example, the goal is to apply conditional formatting to cells that begin with specific text, which is entered in cell G2. The highlighting is done automatically with a conditional formatting rule applied to the range B4:G12. The rule type is "Use a formula to determine which cells to format...

[![Excel formula: Highlight cells that end with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20end%20with.png "Excel formula: Highlight cells that end with")](https://exceljet.net/formulas/highlight-cells-that-end-with)

### [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each cell in B4:G12, and the reference to B4 will change to the address of each cell being evaluated...

[![Excel formula: Cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cell%20contains%20one%20of%20many%20things_0.png "Excel formula: Cell contains one of many things")](https://exceljet.net/formulas/cell-contains-one-of-many-things)

### [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)

The goal of this example is to test each cell in B5:B14 to see if it contains any of the strings in the named range things (E5:E7). These strings can appear anywhere in the cell, so this is a literal "contains" problem. The formula in C5, copied down, is: =SUMPRODUCT(--ISNUMBER(SEARCH(things,B5)))...

[![Excel formula: Highlight cells that contain one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20one%20of%20many.png "Excel formula: Highlight cells that contain one of many")](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)

### [Highlight cells that contain one of many](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)

Working from the inside out, this part of the formula searches each cell in B4:B11 for all values in the named range "things": --ISNUMBER(SEARCH(things,B4) The SEARCH function returns the position of the value if found, and the #VALUE error if not found. For B4, the results come back in an array...

Related functions
-----------------

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

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

*   [Highlight cells that begin with](https://exceljet.net/formulas/highlight-cells-that-begin-with)
    
*   [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)
    
*   [Cell contains one of many things](https://exceljet.net/formulas/cell-contains-one-of-many-things)
    
*   [Highlight cells that contain one of many](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)
    

### Functions

*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
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