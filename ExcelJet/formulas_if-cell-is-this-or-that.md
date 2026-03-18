# If cell is this OR that - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-is-this-or-that

---

[Skip to main content](https://exceljet.net/formulas/if-cell-is-this-or-that#main-content)

[](https://exceljet.net/formulas/if-cell-is-this-or-that#)

*   [Previous](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [Next](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)
    

[If](https://exceljet.net/formulas#If)

If cell is this OR that
=======================

by Dave Bruns · Updated 27 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[OR](https://exceljet.net/functions/or-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6280/download?token=boXcMvcE)
 (10.09 KB)

![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")

Summary
-------

To do something when a cell is this or that (i.e. a cell is equal to "x", "y", etc.) you can use the [IF function](https://exceljet.net/videos/the-if-function)
 together with the [OR function](https://exceljet.net/functions/or-function)
 to run a test. In cell D6, the formula is:

    =IF(OR(B6="red",B6="green"),"x","")
    

which returns "x" when B6 contains "red" or "green", and an [empty string](https://exceljet.net/glossary/empty-string)
 ("") if not. Notice the OR function is _not_ case-sensitive.

Generic formula
---------------

    =IF(OR(A1="this",A1="that"),"x","")

Explanation 
------------

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is:

    =IF(OR(B6="red",B6="green"),"x","")
    

This is an example of [nesting](https://exceljet.net/glossary/nesting)
 – the OR function is _nested_ inside the IF function. Working from the inside out, the logical test is created with the OR function:

    OR(B6="red",B6="green") // returns TRUE
    

OR will return TRUE if the value in B6 is either "red" OR "green", and FALSE if not. This result is returned directly to the IF function as the _logical\_test_ argument. The color in B6 is "red" so OR returns TRUE:

    =IF(TRUE,"x","") // returns "x"
    

With TRUE as the result of the logical test, the IF function returns a final result of "x".

When the color in column B is _not_ red or green, the OR function will return FALSE, and IF will return an [empty string](https://exceljet.net/glossary/empty-string)
 ("") which looks like a blank cell:

    =IF(FALSE,"x","") // returns ""
    

As the formula is copied down the column, the result is either "x" or "", depending on the colors in column B.

_Note: if an empty string ("") is not provided for value\_if\_false, the formula will return FALSE when the color is not red or green._

### Increase price if color is red or green

You can extend this formula to run another calculation, instead of simply returning "x". For example, let's say you want to increase the price of red and green items only by 15%. In that case, you can use the formula in column E to calculate a new price:

![IF function example - increase price if color is red or green](https://exceljet.net/sites/default/files/images/formulas/inline/If%20cell%20is%20this%20or%20that2.png "IF function example - increase price if color is red or green")

    =IF(OR(B6="red",B6="green"),C6*1.15,C6)
    

The logical test is the same as before. However, the _value\_if\_true_ argument is now a formula:

    C6*1.15 // increase price 15%
    

When the result of the test is TRUE, we multiply the original price in column C by 1.15, to increase by 15%. If the result of the test is FALSE, we simply return the original price. As the formula is copied down, the result is either the increased price or the original price, depending on the color.

### Notes

1.  The [IF function](https://exceljet.net/functions/if-function)
     and the [OR function](https://exceljet.net/functions/or-function)
     are _not_ case-sensitive.
2.  The IF function can be [nested inside itself](https://exceljet.net/articles/nested-ifs)
    .
3.  Text values like "red" are enclosed in double quotes (""). [More examples](https://exceljet.net/articles/how-to-use-formula-criteria)
    .

Related formulas
----------------

[![Excel formula: If cell equals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_0.png "Excel formula: If cell equals")](https://exceljet.net/formulas/if-cell-equals)

### [If cell equals](https://exceljet.net/formulas/if-cell-equals)

The goal is to do something if a cell equals a given value. The most common way to solve this problem is with the IF function. IF function The IF function runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this: =...

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: If NOT this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If_not_this_or_that.png "Excel formula: If NOT this or that")](https://exceljet.net/formulas/if-not-this-or-that)

### [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)

The goal is to "flag" records that are neither "Red" nor "Green". More specifically, we want to check the color in column B, and leave an "x" in rows where the color is NOT "Red" OR "Green". If the color is "Red" OR "Green", we want to display nothing. IF function logic The IF function is commonly...

[![Excel formula: Only calculate if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20not%20blank%20then%20calculate2.png "Excel formula: Only calculate if not blank")](https://exceljet.net/formulas/only-calculate-if-not-blank)

### [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)

The goal is to verify the input of all required values before calculating a result. In the worksheet shown, the SUM function is used as an example only. You can use the same approach with any formula to prevent calculation until all required values are available. The logic can be adjusted in many...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

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
    
*   [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)
    
*   [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    
*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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