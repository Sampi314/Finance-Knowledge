# Conditional formatting column is blank - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/conditional-formatting-column-is-blank

---

[Skip to main content](https://exceljet.net/formulas/conditional-formatting-column-is-blank#main-content)

[](https://exceljet.net/formulas/conditional-formatting-column-is-blank#)

*   [Previous](https://exceljet.net/formulas/conditional-formatting-based-on-another-column)
    
*   [Next](https://exceljet.net/formulas/conditional-formatting-date-past-due)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Conditional formatting column is blank
======================================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[OR](https://exceljet.net/functions/or-function)

[AND](https://exceljet.net/functions/and-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel formula: Conditional formatting column is blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Conditional%20formatting%20column%20is%20blank.png "Excel formula: Conditional formatting column is blank")

Summary
-------

To highlight values in one column when values in one or more other columns are blank, you can use the OR function and a basic logical expression to test for blank or empty values. In the example shown, conditional formatting has been applied to the range E5:E14 with this formula:

    =OR(B5="",C5="", D5="")
    

If B5 or C5 or D5 is blank, the formula returns TRUE and triggers the rule.

_Note: conditional formatting formulas should be entered relative to the "active cell" in the selection, which is assumed to be E5 in this case._

Generic formula
---------------

    =OR(A1="",B1="", C1="")

Explanation 
------------

When conditional formatting is applied with a formula, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the active cell when the rule is created is assumed to be cell E5, with the range E5:E14 selected.

As the formula is evaluated, formula references change so that the rule is testing for blank values in the correct row for each of the 10 cells in the range:

    =OR(B5="",C5="", D5="") // E5
    =OR(B6="",C6="", D6="") // E6
    =OR(B7="",C7="", D7="") // E7
    etc.
    

If any cell in a corresponding row in column B, C, or D is blank, OR function returns TRUE and the rule is triggered and the green fill is applied. When all tests return FALSE, the OR function returns FALSE and no conditional formatting is applied.

### With ISBLANK

of testing for an [empty string](https://exceljet.net/glossary/empty-string)
 (="") directly you can use the ISBLANK function in an equivalent formula like this:

    =OR(ISBLANK(B5),ISBLANK(C5),ISBLANK(D5))
    

### AND, OR, NOT

Other logical tests can be constructed using combinations of AND, OR, and NOT. For example, to test for a blank cell in column B and column D, you could use a formula like this:

    =AND(B5="",D5="")
    

This will trigger conditional formatting only when the column B and D are blank.

For more information on building formula criteria, see [50+ formula criteria examples](https://exceljet.net/articles/how-to-use-formula-criteria)
.

Related formulas
----------------

[![Excel formula: Highlight missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20that%20don%27t%20exist.png "Excel formula: Highlight missing values")](https://exceljet.net/formulas/highlight-missing-values)

### [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)

This formula is evaluated for each of the 10 cells in A1:D10. A1 will change to the address of the cell being evaluated, while C1:C10 is entered as an absolute address, so it won't change at all. The key to this formula is the =0 at the end, which "flips" the logic of the formula. For each value in...

[![Excel formula: Highlight column differences](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20column%20differences.png "Excel formula: Highlight column differences")](https://exceljet.net/formulas/highlight-column-differences)

### [Highlight column differences](https://exceljet.net/formulas/highlight-column-differences)

In this example, the goal is to highlight differences in two ranges, B2:B11 and C2:C11, using conditional formatting. To do this, we need to create a new conditional formatting rule, triggered by a formula, like this: Select the range B2:C11, starting at cell B2. Select Home > Conditional...

[![Excel formula: Highlight rows with blank cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20rows%20with%20blank%20cells.png "Excel formula: Highlight rows with blank cells")](https://exceljet.net/formulas/highlight-rows-with-blank-cells)

### [Highlight rows with blank cells](https://exceljet.net/formulas/highlight-rows-with-blank-cells)

Conditional formatting is applied to all cells in the active selection at the time a rule is created. In this case, the column references are locked to prevent columns from changing as the formula is evaluated, but the row references are relative so that row numbers are free to change. The result...

Related functions
-----------------

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20apply%20conditional%20formatting%20with%20a%20formula_thumb.png)](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

### [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)

In this video, we'll look at how to use a formula to apply conditional formatting. Formulas allow you to make powerful and flexible conditional formatting rules that highlight just the data you want. Let's take a look. Excel provides a large number of conditional formatting presets, but there are...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20zebra%20stripes%20with%20conditional%20formatting-thumb.png)](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

### [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)

In this video, we'll look at how to use conditional formatting to shade every other row in a table. This is sometimes called "zebra striping". In this spreadsheet, we have a table of employees with a small amount of formatting. To get shading on every other row, we could just convert this table to...

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

*   [Highlight missing values](https://exceljet.net/formulas/highlight-missing-values)
    
*   [Highlight column differences](https://exceljet.net/formulas/highlight-column-differences)
    
*   [Highlight rows with blank cells](https://exceljet.net/formulas/highlight-rows-with-blank-cells)
    

### Functions

*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [How to create zebra stripes with conditional formatting](https://exceljet.net/videos/how-to-create-zebra-stripes-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    

### Articles

*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    
*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    
*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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