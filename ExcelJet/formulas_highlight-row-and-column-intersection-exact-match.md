# Highlight row and column intersection exact match - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match

---

[Skip to main content](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match#main-content)

[](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match#)

*   [Previous](https://exceljet.net/formulas/highlight-numbers-that-include-symbols)
    
*   [Next](https://exceljet.net/formulas/highlight-rows-that-contain)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight row and column intersection exact match
=================================================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[OR](https://exceljet.net/functions/or-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Highlight row and column intersection exact match](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20row%20and%20column%20intersection%20exact%20match.png "Excel formula: Highlight row and column intersection exact match")

Summary
-------

To highlight intersecting row(s) and column(s) with conditional formatting based on exact matching, you can use a simple formula based on mixed references and the OR function.

In the example shown, the formula used to apply conditional formatting is:

    =OR($B4=$K$5,B$4=$K$6)
    

Generic formula
---------------

    =OR($A1=row_val,A$1=col_val)

Explanation 
------------

Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, cell B3 in this case.

To highlight matching rows, we use this logical expression:

    $B4=$K$5
    

The reference to B4 is [mixed](https://exceljet.net/glossary/mixed-reference)
, with the column locked and row unlocked, so that only values in column B are compared to the country in cell K5. The reference to K5 is [absolute](https://exceljet.net/glossary/absolute-reference)
, to prevent changes when the conditional formatting is applied to every cell in the range B4:H9. In the example shown, this logical expression will return TRUE for every cell in a row where country is "Korea".

To highlight matching columns, we use this logical expression:

    B$4=$K$6
    

The reference to B4 is again mixed. This time, the row is locked and the column is relative, so that only values in row 4 are compared to the month value in cell K6. The reference to K6 is absolute, so that it won't change when the conditional formatting is applied to every cell B4:H9. In the example shown, this logical expression will return TRUE for every cell in a column where row 3 is "Apr".

Because we are triggering the same conditional formatting (light yellow fill) for both rows and columns, we wrap the logical expressions above in the OR function. When either (or both) logicals return TRUE, the rule is triggered and the formatting is applied.

### Highlight intersection only

To highlight the intersection only, just replace the OR function with the AND function:

    =AND($B4=$K$5,B$4=$K$6)
    

Related formulas
----------------

[![Excel formula: Highlight duplicate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20duplicate%20rows.png "Excel formula: Highlight duplicate rows")](https://exceljet.net/formulas/highlight-duplicate-rows)

### [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)

In the formula, COUNTIFS counts the number of times each value in a cell appears in its "parent" column. By definition, each value must appear at least once, so when the count > 1, the value must be a duplicate. The references are carefully locked so the formula will return true only when all 3...

[![Excel formula: Highlight entire rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20entire%20rows.png "Excel formula: Highlight entire rows")](https://exceljet.net/formulas/highlight-entire-rows)

### [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the address of the active cell (B5) is used for the row (5) and entered as a mixed address , with column D locked and the row...

[![Excel formula: Highlight rows that contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20rows%20that%20contain%20specific%20text.png "Excel formula: Highlight rows that contain")](https://exceljet.net/formulas/highlight-rows-that-contain)

### [Highlight rows that contain](https://exceljet.net/formulas/highlight-rows-that-contain)

The SEARCH function returns the position of the text you are looking for as a number (if it exists). Conditional formatting automatically treats any positive number as TRUE, so the rule is triggered whenever SEARCH returns a number. When SEARCH doesn't find the text you're looking for, it returns a...

Related functions
-----------------

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20exact%20match%20lookups%20worked-Thumb.png)](https://exceljet.net/videos/how-to-highlight-exact-match-lookups)

### [How to highlight exact match lookups](https://exceljet.net/videos/how-to-highlight-exact-match-lookups)

In this video, we'll look at how to use conditional formatting to highlight rows and columns associated with exact match lookups. Whenever you have a lookup table visible to users, a nice touch is to highlight the rows and columns that match the current lookup. This makes it easy for users to see...

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
    
*   [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)
    
*   [Highlight rows that contain](https://exceljet.net/formulas/highlight-rows-that-contain)
    

### Functions

*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight exact match lookups](https://exceljet.net/videos/how-to-highlight-exact-match-lookups)
    

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