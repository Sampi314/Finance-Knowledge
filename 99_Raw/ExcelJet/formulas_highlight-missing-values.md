# Highlight missing values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-missing-values

---

[Skip to main content](https://exceljet.net/formulas/highlight-missing-values#main-content)

[](https://exceljet.net/formulas/highlight-missing-values#)

*   [Previous](https://exceljet.net/formulas/highlight-many-matching-values)
    
*   [Next](https://exceljet.net/formulas/highlight-multiples-of-specific-value)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight missing values
========================

by Dave Bruns · Updated 30 Apr 2023

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Highlight missing values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%20values%20that%20don%27t%20exist.png "Excel formula: Highlight missing values")

Summary
-------

To compare lists and highlight values that exist in one but not the other, you can apply conditional formatting with a formula based on the COUNTIF function. For example, to highlight values A1:A10 that don't exist C1:C10, select A1:A10 and create a conditional formatting rule based on this formula:

    =COUNTIF($C$1:$C$10,A1)=0
    

_Note: with conditional formatting, it's important to enter the formula relative to the "active cell" in the selection, which is assumed to be A1 in this case._

Generic formula
---------------

    =COUNTIF(list,A1)=0

Explanation 
------------

This formula is evaluated for each of the 10 cells in A1:D10. A1 will change to the address of the cell being evaluated, while C1:C10 is entered as an absolute address, so it won't change at all.

The key to this formula is the =0 at the end, which "flips" the logic of the formula. For each value in A1:A10, COUNTIF returns the number of times the value appears in C1:C10. As long as the value appears at least once in C1:C10, COUNTIF will return a non-zero number and the formula will return FALSE.

But when a value is _not found_ in C1:C10, the COUNTIF returns zero and, since 0 = 0, the formula will return TRUE and the conditional formatting will be applied.

### Named ranges for simple syntax

If you name the list you are searching (C1:C10 in this case) with a named range, the formula is simpler to read and understand:

    =COUNTIF(list,A1)=0
    

This works because named ranges are automatically absolute.

### Case-sensitive version

If you need a case sensitive count, you can use a formula like this:

    =SUMPRODUCT((--EXACT(A1,list)))=0
    

The EXACT function performs a case-sensitive evaluation and SUMPRODUCT tallies the result. As with the COUNTIF, this formula will return when the result is zero. Because the test is case-sensitive, "apple" will show as missing even if "Apple" or "APPLE" appears in the second list. See [this page](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
 for a more detailed explanation.

Related formulas
----------------

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Find missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_missing_values.png "Excel formula: Find missing values")](https://exceljet.net/formulas/find-missing-values)

### [Find missing values](https://exceljet.net/formulas/find-missing-values)

The goal is to identify invoice numbers in range D5:D11 that are missing in range B5:B16 (named list ). Two good ways to solve this problem in Excel are the COUNTIF function and the MATCH function . Both approaches are explained below. COUNTIF function COUNTIF counts cells in a range that meet a...

[![Excel formula: List missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_missing_values.png "Excel formula: List missing values")](https://exceljet.net/formulas/list-missing-values)

### [List missing values](https://exceljet.net/formulas/list-missing-values)

In this example, the goal is to generate a list of people who were invited but did not attend an unspecified event. More specifically, we need to compare the names in B5:B16 against the names in D5:D12 and return the missing names. For convenience, list1 (B5:B16) and list2 (D5:D12) are named ranges...

[![Excel formula: Count missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_missing_values.png "Excel formula: Count missing values")](https://exceljet.net/formulas/count-missing-values)

### [Count missing values](https://exceljet.net/formulas/count-missing-values)

In this example, the goal is to count the number of names in the range B5:B16 (Invited) that are missing from the range D5:D12 (Attended). This problem can be solved with the COUNTIF function or the MATCH function, as explained below. Both approaches work well. The advantage of the MATCH approach...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

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

*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Find missing values](https://exceljet.net/formulas/find-missing-values)
    
*   [List missing values](https://exceljet.net/formulas/list-missing-values)
    
*   [Count missing values](https://exceljet.net/formulas/count-missing-values)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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