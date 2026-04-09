# Highlight many matching values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-many-matching-values

---

[Skip to main content](https://exceljet.net/formulas/highlight-many-matching-values#main-content)

[](https://exceljet.net/formulas/highlight-many-matching-values#)

*   [Previous](https://exceljet.net/formulas/highlight-integers-only)
    
*   [Next](https://exceljet.net/formulas/highlight-missing-values)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight many matching values
==============================

by Dave Bruns · Updated 22 Jun 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6754/download?token=JxnuxEFg)
 (15.11 KB)

![Excel formula: Highlight many matching values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/highlight%20many%20matching%20values.png "Excel formula: Highlight many matching values")

Summary
-------

To highlight many matching values in a set of data with conditional formatting you can use a formula based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula for green cells is:

    =COUNTIF(values,B4)
    

where **values** is the [named range](https://exceljet.net/glossary/named-range)
 K4:M7 and the rule is applied to all data in B4:I15.

Generic formula
---------------

    =COUNTIF(values,A1)

Explanation 
------------

In this example, the goal is to highlight all values in K4:M7 (**values**) that appear in the range B4:I15 (**data**). The range K4:M7 is named "values" for readability and convenience only. If you don't want to use a named range, use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 instead.

Although this is a difficult problem for the human eye, it is exactly the kind of thing Excel does very well. The solution above shows matching **data** in green, and matching **values** in blue. The colors are applied automatically with conditional formatting and will update instantly if values change. This requires two separate conditional formatting rules, each with its own formula.

### Highlight matching data (green)

This formula is based on the [COUNTIF function](https://exceljet.net/functions/countif-function)
, which takes two arguments: _range_ and _criteria_ and returns a count of values that match criteria. Normally, _range_ represents the cells being checked. For example, to count cells in the range A1:A10 that are equal to 7, you would configure COUNTIF like this:

    =COUNTIF(A1:A10,7) // count values = 7
    

However, in this case, we want to check each cell in B4:I15 against the 12 separate values in K4:M7. One option is to use COUNTIF with **values** as _criteria_ and use SUM to add up results:

    =SUM(COUNTIF(B4,values)) // returns {0,0,0;0,0,1;0,0,0;0,0,0}
    

_Note: the rule is applied to all cells in B4:I15. The relative reference to B4 will change at each cell._

Because we are giving COUNTIF 12 separate numbers to evaluate as criteria, COUNTIF will return 12 counts in an [array](https://exceljet.net/glossary/array)
 for each cell in the data. To force a single result, we wrap COUNTIF in the [SUM function](https://exceljet.net/functions/sum-function)
. Any sum greater than zero means B4 contains a number in **values**, and [any non-zero result will evaluate as TRUE](https://exceljet.net/videos/introduction-to-booleans)
 and trigger the rule.

However, a simpler option is to reverse the COUNTIF configuration like this:

    =COUNTIF(values,B4) // returns 1
    

Here, _range_ is **values** , and B4 is _criteria_. This gives us a _single_ numeric result – the count of the cell value (B4) in **values**. As above, any non-zero result means that B4 is a number in K4:M7. And any non-zero result triggers the conditional formatting rule and colors the cell.

### Highlight matching values (blue)

The above rule highlights numbers in **data** that appear in **values**. We can easily make a rule to highlight cells in **values** that contain numbers in **data**. In the example shown, the blue highlighting is created with the following formula:

    =COUNTIF(data,K4) // blue highlighting
    

Notice the approach is the same as above. Each cell in **values** K4:M7 becomes the _criteria_ argument inside COUNTIF while the _range_ is **data** (B4:I15). As above, COUNTIF returns a single count for each cell in **values** and any non-zero result triggers the rule.

### Count all matching values

To count the total number of cells in **data** (B4:I15) that match a number in **values** (K4:M7) you can use a formula like this:

    =SUMPRODUCT(COUNTIF(values,data)) // returns 12
    

To count the total number of cells in **values** (K4:M7) that match a value in **data** (B4:I15), you can use a formula like this:

    =SUMPRODUCT(--(COUNTIF(data,values)>0)) // returns 6
    

Here, because the numbers in **values** often appear more than once in **data**, we need to force non-zero counts from COUNTIF to 1 before we add them up, to avoid over counting. We do this by checking if the counts are greater than zero and using a [double negative](https://exceljet.net/glossary/double-unary)
 (--) to force the TRUE FALSE results to 1s and 0s. 

_Note: you can also use the [SUM function](https://exceljet.net/functions/sum-function)
 in place of SUMPRODUCT above, but you will need to enter the formula as an [array formula](https://exceljet.net/glossary/array-formula)
 with control + shift + enter, unless you are using [Excel 365](https://exceljet.net/glossary/excel-365)
._

Related formulas
----------------

[![Excel formula: Highlight cells that contain one of many](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20contain%20one%20of%20many.png "Excel formula: Highlight cells that contain one of many")](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)

### [Highlight cells that contain one of many](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)

Working from the inside out, this part of the formula searches each cell in B4:B11 for all values in the named range "things": --ISNUMBER(SEARCH(things,B4) The SEARCH function returns the position of the value if found, and the #VALUE error if not found. For B4, the results come back in an array...

[![Excel formula: Highlight top values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20top%20values.png "Excel formula: Highlight top values")](https://exceljet.net/formulas/highlight-top-values)

### [Highlight top values](https://exceljet.net/formulas/highlight-top-values)

This formula uses two named ranges: data (B4:G11) and input (F2). These are for readability and convenience only. If you don't want to use named ranges, make sure you use absolute references for both of these ranges in the formula. This formula is based on the LARGE function , which returns the nth...

[![Excel formula: Highlight values greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/%20Highlight%20values%20greater%20than%20or%20less%20than.png "Excel formula: Highlight values greater than")](https://exceljet.net/formulas/highlight-values-greater-than)

### [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. So, in this case the formula =B4>100 is evaluated for each of the 40 cells in B4:G11. Because B4 is entered as a relative address, the...

[![Excel formula:  Highlight 3 smallest values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%203%20smallest%20values%20with%20criteria_0.png "Excel formula:  Highlight 3 smallest values with criteria")](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)

### [Highlight 3 smallest values with criteria](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)

Inside the AND function there are two logical criteria. The first is straightforward, and ensures that only cells that match the color in E5 are highlighted: $B3=$E$5 The second test is more complex: $C3<=SMALL(IF(color=$E$5,amount),3) Here, we filter amounts to make sure that only values...

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

*   [Highlight cells that contain one of many](https://exceljet.net/formulas/highlight-cells-that-contain-one-of-many)
    
*   [Highlight top values](https://exceljet.net/formulas/highlight-top-values)
    
*   [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)
    
*   [Highlight 3 smallest values with criteria](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria)
    

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