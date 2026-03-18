#  Highlight 3 smallest values with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria#main-content)

[](https://exceljet.net/formulas/highlight-3-smallest-values-with-criteria#)

*   [Previous](https://exceljet.net/formulas/running-count-group-by-n-size)
    
*   [Next](https://exceljet.net/formulas/conditional-formatting-based-on-another-cell)
    

[Conditional formatting](https://exceljet.net/formulas#Conditional-formatting)

Highlight 3 smallest values with criteria
=========================================

by Dave Bruns · Updated 12 Jun 2020

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula:  Highlight 3 smallest values with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Highlight%203%20smallest%20values%20with%20criteria_0.png "Excel formula:  Highlight 3 smallest values with criteria")

Summary
-------

To highlight the 3 smallest values that meet specific criteria, you can use an array formula based on the AND and SMALL functions. In the example shown, the formula used for conditional formatting is:

    =AND($B5=$E$5,$C5<=SMALL(IF(color=$E$5,amount),3))
    

Where "color" is the [named range](https://exceljet.net/glossary/named-range)
 B5:B12 and "amount" is the named range C5:C12.

Generic formula
---------------

    =AND(A1=criteria,B1<=SMALL(IF(criteria,values),3))

Explanation 
------------

Inside the [AND function](https://exceljet.net/functions/and-function)
 there are two logical criteria. The first is straightforward, and ensures that only cells that match the color in E5 are highlighted:

    $B3=$E$5
    

The second test is more complex:

    $C3<=SMALL(IF(color=$E$5,amount),3)
    

Here, we filter amounts to make sure that only values associated with the color in E5 (blue) are retained. The filtering is done with the IF function like this:

    IF(color=$E$5,amount)
    

The resulting array looks like this:

    {FALSE;100;FALSE;200;FALSE;300;FALSE;400;FALSE;500}
    

Notice the value from the amount column only survives if the color is "blue". Other amounts are now FALSE.

Next, this array goes into the [SMALL function](https://exceljet.net/functions/small-function)
 with a k value of 3, and SMALL returns the "3rd smallest" value, 300. The logic for the second logical test reduces to:

    $C3<=300
    

When both logical conditions are return TRUE, the conditional formatting is triggered and cells are highlighted.

_Note: this is an array formula, but does not require control + shift + enter._

Related formulas
----------------

[![Excel formula: Highlight bottom values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20bottom%20values.png "Excel formula: Highlight bottom values")](https://exceljet.net/formulas/highlight-bottom-values)

### [Highlight bottom values](https://exceljet.net/formulas/highlight-bottom-values)

In this example, the goal is to highlight the 5 bottom values in B4:G11 where the number 5 is a variable set in cell F2. This formula uses two named ranges: data (B4:G11) and input (F2). These are for readability and convenience only. If you don't want to use named ranges, make sure you use...

[![Excel formula: Highlight values greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/%20Highlight%20values%20greater%20than%20or%20less%20than.png "Excel formula: Highlight values greater than")](https://exceljet.net/formulas/highlight-values-greater-than)

### [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. So, in this case the formula =B4>100 is evaluated for each of the 40 cells in B4:G11. Because B4 is entered as a relative address, the...

[![Excel formula: nth smallest value with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value_with_criteria.png "Excel formula: nth smallest value with criteria")](https://exceljet.net/formulas/nth-smallest-value-with-criteria)

### [nth smallest value with criteria](https://exceljet.net/formulas/nth-smallest-value-with-criteria)

In this example, the goal is to retrieve the lowest 3 scores in column D that appear in a given group, entered as a variable in cell F5. If the group is changed, the formulas should calculate new results. The core of the solution is the SMALL function, which can be used to retrieve the "nth"...

Related functions
-----------------

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

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

*   [Highlight bottom values](https://exceljet.net/formulas/highlight-bottom-values)
    
*   [Highlight values greater than](https://exceljet.net/formulas/highlight-values-greater-than)
    
*   [nth smallest value with criteria](https://exceljet.net/formulas/nth-smallest-value-with-criteria)
    

### Functions

*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [How to apply conditional formatting with a formula](https://exceljet.net/videos/how-to-apply-conditional-formatting-with-a-formula)
    
*   [Conditional formatting based on a different cell](https://exceljet.net/videos/conditional-formatting-based-on-a-different-cell)
    
*   [How to highlight rows with conditional formatting](https://exceljet.net/videos/how-to-highlight-rows-with-conditional-formatting)
    
*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    

### Articles

*   [Conditional formatting with formulas](https://exceljet.net/articles/conditional-formatting-with-formulas)
    
*   [Cool things you can do with conditional formatting](https://exceljet.net/articles/cool-things-you-can-do-with-conditional-formatting)
    
*   [Test conditional formatting with dummy formulas](https://exceljet.net/articles/test-conditional-formatting-with-dummy-formulas)
    

### Links

*   [Array formulas in conditional formatting (Bill Jelen)](http://sfmagazine.com/post-entry/june-2016-excel-array-formulas-in-conditional-formatting/)
    

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