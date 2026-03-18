# If cell is greater than - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-is-greater-than

---

[Skip to main content](https://exceljet.net/formulas/if-cell-is-greater-than#main-content)

[](https://exceljet.net/formulas/if-cell-is-greater-than#)

*   [Previous](https://exceljet.net/formulas/if-cell-is-blank)
    
*   [Next](https://exceljet.net/formulas/if-cell-is-not-blank)
    

[If](https://exceljet.net/formulas#If)

If cell is greater than
=======================

by Dave Bruns · Updated 6 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

![Excel formula: If cell is greater than](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_cell_is_greater_than.png "Excel formula: If cell is greater than")

Summary
-------

To test if a cell is greater than a given value, you can use the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in cell E5 is:

    =IF(C5>80,"x","")
    

The result in cell E5 is "x" since the score in cell C5 is greater than 80. The result returned by the IF function can be adjusted as needed.

Generic formula
---------------

    =IF(A1>80,"Yes","No")

Explanation 
------------

The aim is to mark records with an "x" if a score is greater than 80 and leave the cell blank if the score is less than 80. This can be achieved using the IF function in Excel.

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this:

    =IF(logical_test,if_true,if_false)

The IF function can return a value, a cell reference, or even another formula. In the worksheet shown, the goal is to identify rows where the score is greater than 80 by returning "x" as a marker. To accomplish this task, the formula in cell E5 is:

    =IF(C5>80,"x","")
    

In this formula, the logical test is this expression:

    C5>80

This expression returns TRUE if the value in C5 is greater than 80 and FALSE if not. In cell F5, the result is TRUE because C5 contains 85. The IF function then returns "x" as a final result:

    =IF(C5>80,"x","") // returns "x"

In cell F6, the expression returns FALSE because C6 contains 79. The IF function returns an empty string "" as a final result:

    =IF(C6>80,"x","") // returns ""

In Excel, an [empty string](https://exceljet.net/glossary/empty-string)
 ("") displays nothing. The result returned by the IF function can be customized as needed. For example, to return "Yes" if a score is greater than 80 and "No" if not, you can use this formula:

    =IF(C5>80,"Yes","No")

Note that if _no value_ is provided for the _value\_if\_false_ argument, the formula will return FALSE for scores not greater than 80.

### Conditional formatting

Another way to identify cells with a value greater than 80 is to use [conditional formatting](https://exceljet.net/articles/conditional-formatting-with-formulas)
, as seen below:

![Using conditional formatting to highlight scores greater than 80](https://exceljet.net/sites/default/files/images/formulas/inline/if_cell_is_greater_than_conditional_formatting.png "Using conditional formatting to highlight scores greater than 80")

This is an example of applying conditional formatting with a formula. The formula used to highlight scores greater than 80 is:

    =C5>80

The formatting is automatic. If a score is changed to a number greater than 80, the yellow highlighting will appear. You can find more conditional formatting examples [here](https://exceljet.net/conditional-formatting-formulas)
.

Related formulas
----------------

[![Excel formula: If cell equals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_0.png "Excel formula: If cell equals")](https://exceljet.net/formulas/if-cell-equals)

### [If cell equals](https://exceljet.net/formulas/if-cell-equals)

The goal is to do something if a cell equals a given value. The most common way to solve this problem is with the IF function. IF function The IF function runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this: =...

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If NOT this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If_not_this_or_that.png "Excel formula: If NOT this or that")](https://exceljet.net/formulas/if-not-this-or-that)

### [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)

The goal is to "flag" records that are neither "Red" nor "Green". More specifically, we want to check the color in column B, and leave an "x" in rows where the color is NOT "Red" OR "Green". If the color is "Red" OR "Green", we want to display nothing. IF function logic The IF function is commonly...

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: Nested IF function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nested_if_function_example.png "Excel formula: Nested IF function example")](https://exceljet.net/formulas/nested-if-function-example)

### [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)

The goal is to assign a grade to each score in column C according to the rules in the table in the range F4:G9. One way to do this in Excel is to use a series of nested IF functions. Generally, nested IFs formulas are used to test more than one condition and return a different result for each...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/If%20this%20OR%20that-thumb.png)](https://exceljet.net/videos/if-this-or-that)

### [If this OR that](https://exceljet.net/videos/if-this-or-that)

Sometimes, you might need to write a formula that uses the IF function to test for this OR that, or this AND that. There are two special functions, AND and OR, that make this easy to do. Let's take a look. In this first worksheet, we have a list of employees. Let's assume that you need to group...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If cell equals](https://exceljet.net/formulas/if-cell-equals)
    
*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    
*   [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
    
*   [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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