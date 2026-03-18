# Highlight approximate match lookup conditional formatting - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting

---

[Skip to main content](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting#main-content)

[](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting#)

*   [Previous](https://exceljet.net/formulas/gantt-chart-with-weekends)
    
*   [Next](https://exceljet.net/formulas/highlight-blank-cells)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight approximate match lookup conditional formatting
=========================================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[LOOKUP](https://exceljet.net/functions/lookup-function)

[OR](https://exceljet.net/functions/or-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Highlight approximate match lookup conditional formatting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/highlight%20approximate%20match%20lookups.png "Excel formula: Highlight approximate match lookup conditional formatting")

Summary
-------

To highlight rows and columns associated with an approximate match, you can use conditional formatting with a formula based on the [LOOKUP function](https://exceljet.net/functions/lookup-function)
 together with a logical function like OR or AND. In the example shown, the formula used to apply conditional formatting is:

    =OR($B5=LOOKUP(width,widths),B$5=LOOKUP(height,heights))
    

Generic formula
---------------

    =OR($B5=LOOKUP(width,widths),B$5=LOOKUP(height,heights))

Explanation 
------------

This formula uses 4 named ranges, defined as follows:

    width=K6
    height=K7
    widths=B6:B11
    heights=C5:H5
    

Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, which is cell B5 in this case. To highlight the matching row, we use this logical expression:

    $B5=LOOKUP(width,widths)
    

The reference to B5 is [mixed](https://exceljet.net/glossary/mixed-reference)
, with the column locked and row unlocked, so that only values in column B (widths) are compared to the value in K6 (width). In the example shown, this logical expression will return TRUE for every cell in a row where the width is 200, based on an approximate match of the value in K6 (width, 275) against all values in K6:B11 (widths). This is done with the LOOKUP function:

    LOOKUP(width,widths)
    

Like the MATCH function, LOOKUP will run through sorted values until a greater value is found, then "step back" to the previous value, which is 200 in this case.

To highlight the matching column, we use this logical expression:

    B$5=LOOKUP(height,heights)
    

The reference to B5 is mixed, with the column relative and row [absolute](https://exceljet.net/glossary/absolute-reference)
, so that only values in row 5 (heights) are compared to the value in K7 (height). In the example shown, this logical expression will return TRUE for every cell in a row where the height is 300, based on an approximate match of the value in K7 (height, 325) against all values in C5:H5 (heights). This is done with the LOOKUP function:

    LOOKUP(height,heights)
    

As above, LOOKUP will run through sorted values until a greater value is found, then "step back" to the previous value, which is 300 in this case.

### Highlight intersection only

To highlight the intersection only, just replace the OR function with the AND function:

    =AND($B5=LOOKUP(width,widths),B$5=LOOKUP(height,heights))
    

Related formulas
----------------

[![Excel formula: Highlight row and column intersection exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20row%20and%20column%20intersection%20exact%20match.png "Excel formula: Highlight row and column intersection exact match")](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)

### [Highlight row and column intersection exact match](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)

Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, cell B3 in this case. To highlight matching rows, we use this logical expression: $B4=$K$5 The reference to B4 is mixed , with the column locked and row unlocked, so that...

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

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

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

*   [Highlight row and column intersection exact match](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)
    
*   [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)
    
*   [Highlight entire rows](https://exceljet.net/formulas/highlight-entire-rows)
    
*   [Highlight rows that contain](https://exceljet.net/formulas/highlight-rows-that-contain)
    

### Functions

*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
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