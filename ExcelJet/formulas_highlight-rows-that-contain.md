# Highlight rows that contain - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-rows-that-contain

---

[Skip to main content](https://exceljet.net/formulas/highlight-rows-that-contain#main-content)

[](https://exceljet.net/formulas/highlight-rows-that-contain#)

*   [Previous](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)
    
*   [Next](https://exceljet.net/formulas/highlight-rows-with-blank-cells)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight rows that contain
===========================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[SEARCH](https://exceljet.net/functions/search-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Highlight rows that contain](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20rows%20that%20contain%20specific%20text.png "Excel formula: Highlight rows that contain")

Summary
-------

To highlight rows in a table that contain specific text, you can use conditional formatting with a formula that returns TRUE when the text is found. The trick is to concatenate (glue together) the columns you want to search and to lock the column references so that only the rows can change.

For example, assume you have a simple table of data in B4:E11 and you want to highlight all rows that contain the text "dog". Just select all data in the table and create a new conditional formatting rule that uses this formula:

    =SEARCH("dog",$B4&$C4&$D4&$E4)
    

_Note: with conditional formatting, the formula must be entered relative to the "active cell" in the selection, which is assumed to be B4 in this case._

Generic formula
---------------

    =SEARCH(text,concatenated_text)

Explanation 
------------

The SEARCH function returns the position of the text you are looking for as a number (if it exists). Conditional formatting automatically treats any positive number as TRUE, so the rule is triggered whenever SEARCH returns a number. When SEARCH doesn't find the text you're looking for, it returns a #VALUE error, which conditional formatting treats as FALSE.

Using the ampersand (&) we are concatenating all values in each row together and then searching the result with SEARCH. All addresses are entered in "mixed" format, with the columns locked and the rows left relative. Effectively, this means that all 4 cells in each row are tested with exactly the same formula.

### Using other cells as inputs

Note that you don't have to hard-code any values that might change into the rule. Instead, you can use another cell as an "input" cell so you can easily change it later. For example, in this case, you could name cell E2 "input" and rewrite the formula like so:

    =SEARCH(input,$B4&$C4&$D4&$E4)
    

You can then put any text value in E2, and the conditional formatting rule will respond instantly, highlighting rows that contain that text. See the video link below for a more detailed description.

### Case sensitive option

If you need a case-sensitive option, you can use the FIND function instead of SEARCH like so:

    =FIND(input,$B4&$C4&$D4&$E4)
    

The FIND function works just like SEARCH but matches the case as well.

Related formulas
----------------

[![Excel formula: Highlight entire rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20entire%20rows.png "Excel formula: Highlight entire rows")](https://exceljet.net/formulas/highlight-entire-rows)

### [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the address of the active cell (B5) is used for the row (5) and entered as a mixed address , with column D locked and the row...

Related functions
-----------------

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20with%20conditional%20formatting_thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

### [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)

Using conditional formatting, It's easy to highlight cells that match a certain condition. However, it's a little trickier to highlight entire rows in a list that contains multiple columns. In this video, we'll show you how to use a formula with conditional formatting to highlight an entire row in...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

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

*   [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)
    

### Functions

*   [SEARCH Function](https://exceljet.net/functions/search-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

### Videos

*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
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