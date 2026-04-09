# If cell equals - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-equals

---

[Skip to main content](https://exceljet.net/formulas/if-cell-equals#main-content)

[](https://exceljet.net/formulas/if-cell-equals#)

*   [Previous](https://exceljet.net/formulas/if-cell-contains-this-or-that)
    
*   [Next](https://exceljet.net/formulas/if-cell-is-blank)
    

[If](https://exceljet.net/formulas#If)

If cell equals
==============

by Dave Bruns · Updated 6 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

![Excel formula: If cell equals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_cell_contains_0.png "Excel formula: If cell equals")

Summary
-------

To test if a cell is equal to a given value, you can use the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in cell F5 is:

    =IF(C5="red","x","")
    

The result in cell F5 is "x" since the color in cell C5 is equal to "Red". The result from IF can be adjusted as needed. See below for a formula to increase the price of "Red" items by 10%.

Generic formula
---------------

    =IF(A1="red","x","")

Explanation 
------------

The goal is to do something if a cell equals a given value. The most common way to solve this problem is with the IF function.

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this:

    =IF(logical_test,if_true,if_false)

The result from IF can be a value, a cell reference, or even another formula. In the worksheet shown, the goal is to identify rows where the color is "Red" by returning "x" as a marker. To accomplish this task, the formula in cell F5 is:

    =IF(C5="red","x","")
    

In this formula, the logical test is this expression:

    C5="red"

This expression returns TRUE if the value in C5 is "red" and FALSE if not. In cell F5, the result will be TRUE because C5 equals "red" but in cell F6 the result will be FALSE because C6 equals "Blue":

    C5="red" // returns TRUE
    C6="red" // returns FALSE

The formula at this point looks like this:

    IF(C5="red",

Next, we need to add a value when the result is TRUE and a value when the result is FALSE. Since we want to mark items when the color is "Red", we provide "x" for the value to return if TRUE:

    IF(C5="red","x",

Since we don't want to display anything when the color is not "Red", we provide an [empty string](https://exceljet.net/glossary/empty-string)
 (""), for the value to return if FALSE. The final formula in cell F5 looks like this:

    =IF(C5="red","x","")

The result returned by IF can be customized as needed. If an empty string ("") is not provided for _value\_if\_false_, the IF function will return FALSE when the color is not "Red". Note that Excel is not case-sensitive by default. The expressions below will all return TRUE:

    C5="Red" // returns TRUE
    C5="RED" // returns TRUE
    C5="red" // returns TRUE

If you need a case-sensitive formula, see the [EXACT function](https://exceljet.net/functions/exact-function)
.

### Increase price if color is red

The result from IF does not need to be a hard-coded value. It can be a cell reference or another formula. For example, let's say you want to increase the price of Red items only by 10%. In that case, you can use a formula like this:

    =IF(C5="red",D5*1.1,"")
    

![IF function example - increase price 10% if color is Red](https://exceljet.net/sites/default/files/images/formulas/inline/if_cell_contains_custom_result.png "IF function example - increase price 10% if color is Red")

The test is the same as before (B6="red"). If the result is TRUE, we multiply the original price by 1.1 (i.e. increase the price by 10%). If the result is FALSE, we return an empty string ("").

Related formulas
----------------

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If cell contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains.png "Excel formula: If cell contains")](https://exceljet.net/formulas/if-cell-contains)

### [If cell contains](https://exceljet.net/formulas/if-cell-contains)

The goal is to do something if a cell contains a given substring. For example, in the worksheet above, a formula returns "x" when a cell contains "abc". If you are familiar with Excel, you will probably think first of the IF function. However, one limitation of IF is that it does not support...

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: If this AND that OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that_or_that.png "Excel formula: If this AND that OR that")](https://exceljet.net/formulas/if-this-and-that-or-that)

### [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)

The goal is to mark rows where the color is "Red" AND the size is "Small" or "Medium". To perform this task, you can use the IF function in combination with the AND function and the OR function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different...

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

*   [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    
*   [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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