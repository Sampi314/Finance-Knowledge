# If this AND that - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-this-and-that

---

[Skip to main content](https://exceljet.net/formulas/if-this-and-that#main-content)

[](https://exceljet.net/formulas/if-this-and-that#)

*   [Previous](https://exceljet.net/formulas/if-not-this-or-that)
    
*   [Next](https://exceljet.net/formulas/if-this-and-that-or-that)
    

[If](https://exceljet.net/formulas#If)

If this AND that
================

by Dave Bruns · Updated 12 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")

Summary
-------

To perform an action when two conditions are TRUE (i.e. this AND that)  that you can use the [IF function](https://exceljet.net/videos/the-if-function)
 together with the [AND function](https://exceljet.net/functions/and-function)
. In cell D6, the formula is:

    =IF(AND(B6="red",C6="small"),"x","")
    

As the formula is copied down, it returns "x" when column B is "Red" AND column C is "Small". Otherwise, it returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("") which looks like an empty cell in Excel. 

Generic formula
---------------

    =IF(AND(A1="this",B1="that"),"x","")

Explanation 
------------

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the [IF function](https://exceljet.net/videos/the-if-function)
 in combination with the [AND function](https://exceljet.net/functions/and-function)
.

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 runs a test, then returns one value if the result is TRUE, and a different value if the result is FALSE. The generic syntax for IF looks like this:

    =IF(logical_test,value_if_true,value_if_false)

For example, if cell A1 contains the value 75, then you could use IF to return "Pass" or "Fail" like this:

    =IF(A1>70,"Pass","Fail") // returns "Pass"

If the value in A1 is 65, then IF returns "Fail":

    =IF(A1>70,"Pass","Fail") // returns "Fail"

Notice that the text values inside IF must be enclosed in double quotes ("").

### AND function

The [AND function](https://exceljet.net/functions/and-function)
 returns TRUE if all arguments are TRUE. For example, if cell A1 contains "Red" and B1 contains 10, then:

    =AND(A1="Red",B1>5) returns TRUE
    =AND(A1="Red",B1>12) returns FALSE
    =AND(A1="Blue",B1>5) returns FALSE
    

Because the AND function returns TRUE or FALSE, it often appears inside the IF function as a logical test.

### IF + AND

In the example shown, we want to identify records where the color is Red and the size is Small. This means we need to test the value in column B for "Red" and test the value in column C for "Small". We can do that with the AND function like this:

    AND(B6="red",C6="small")
    

_Note: Excel formulas are not case-sensitive by default, so B6="red", B6="Red", and B6="RED" will all return the same result. For that reason, the text values in the logical test are left in lowercase._

The formula above will return TRUE only if the value in B6 is "Red" AND the value in C6 is "Small". If either condition isn't true, the AND function will return FALSE. To process the result from AND and mark a row with an "x" when both conditions are TRUE, we embed the AND formula inside the IF function as the logical test. In D6, the formula is:

    =IF(AND(B6="red",C6="small"),"x","")
    

If the test is FALSE,  we don't want to display anything, so we simply return an empty string (""), which looks like an empty cell in Excel. As the formula is copied down, IF returns an "x" in column D only when the color is Red and the size is Small.

_Note: You might wonder if we need to supply an empty string ("") for the false result. Technically, this [argument](https://exceljet.net/glossary/function-argument)
 is optional. However, if we don't provide a value, the IF function will return and display FALSE in all rows that aren't Red and Small._

### Multiple conditions in the same cell

In some scenarios, you may need to evaluate multiple conditions within a single cell. For instance, if you need to verify that a cell value falls within a specific range (e.g., between 100 and 200), you can use the AND function as follows:

    =AND(A1>=100,A1<200)
    

To mark values that meet these conditions, you could use the IF function as before:

    =IF(AND(A1>=100,A1<200),"x","")
    

Related formulas
----------------

[![Excel formula: If cell equals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_0.png "Excel formula: If cell equals")](https://exceljet.net/formulas/if-cell-equals)

### [If cell equals](https://exceljet.net/formulas/if-cell-equals)

The goal is to do something if a cell equals a given value. The most common way to solve this problem is with the IF function. IF function The IF function runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this: =...

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If this AND that OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that_or_that.png "Excel formula: If this AND that OR that")](https://exceljet.net/formulas/if-this-and-that-or-that)

### [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)

The goal is to mark rows where the color is "Red" AND the size is "Small" or "Medium". To perform this task, you can use the IF function in combination with the AND function and the OR function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

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
    
*   [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
    
*   [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

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