# If cell is x or y and z - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-cell-is-x-or-y-and-z

---

[Skip to main content](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z#main-content)

[](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z#)

*   [Previous](https://exceljet.net/formulas/if-cell-is-this-or-that)
    
*   [Next](https://exceljet.net/formulas/if-complete-show-checkmark)
    

[If](https://exceljet.net/formulas#If)

If cell is x or y and z
=======================

by Dave Bruns · Updated 8 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[OR](https://exceljet.net/functions/or-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: If cell is x or y and z](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_cell_is_x_or_y_and_z.png "Excel formula: If cell is x or y and z")

Summary
-------

To take some action when a value is (x or y) and z, you can use the [IF function](https://exceljet.net/functions/if-function)
 in combination with the [AND function](https://exceljet.net/functions/and-function)
 and the [OR function](https://exceljet.net/functions/or-function)
. In the example shown, the formula in cell E5 is

    =IF(AND(OR(B5="red",B5="green"),C5>10),"x","")
    

This formula returns "x" if the color in column B is "Red" or "Green", _and_ the quantity in column C is greater than 10. Otherwise, the formula returns an [empty string](https://exceljet.net/glossary/empty-string)
 ("") which displays like an empty cell in Excel.

_Note: Excel is not case-sensitive by default, so B5="Red" and B5="red" will return the same result._

Generic formula
---------------

    =IF(AND(OR(A1="x",A1="y"),B1>z),"yes","no")

Explanation 
------------

The goal is to identify records where the color is "Red" or "Green" and the quantity is greater than 10. If a row meets all conditions, the formula should return "x". If any condition is not true, the formula should return an empty string (""). This problem can be solved with the IF function together with the OR function and the AND function.

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. For example, if cell A1 contains the text "Red", then:

    =IF(A1="red",TRUE) // returns TRUE
    =IF(A1="blue",TRUE) // returns FALSE

Notice the IF function is _not_ case-sensitive. Also, notice that IF automatically returns FALSE even though no value is provided for a false result.

### OR function

The [OR function](https://exceljet.net/functions/or-function)
 returns TRUE if any argument is TRUE. For example, if cell A1 contains "Red" then:

    =OR(A1="Red",A1="Green") // returns TRUE
    =OR(A1="Blue",A1="Green") // returns FALSE

### AND function

The [AND function](https://exceljet.net/functions/and-function)
 returns TRUE if all arguments are TRUE. For example, if cell A1 contains "Red" and B1 contains 10, then:

    =AND(A1="Red",B1=10) returns TRUE
    =AND(A1="Red",B1=12) returns FALSE
    =AND(A1="Blue",B1=10) returns FALSE
    

### Putting it all together

The goal is to identify records where the color is "Red" or "Green" and the quantity is greater than 10. The formula in cell E5 is:

    =IF(AND(OR(B5="red",B5="green"),C5>10),"x","")

Note that the [OR function](https://exceljet.net/functions/or-function)
 appears _inside_ the [AND function](https://exceljet.net/functions/and-function)
. This means the OR function must return TRUE in order for the AND function to return TRUE. In other words, the color must be "Red" or "Green" and the quantity must be greater than 10. In cell E5, the formula evaluates like this:

    =IF(AND(OR(B5="red",B5="green"),C5>10),"x","")
    =IF(AND(OR(TRUE,FALSE),C5>10),"x","")
    =IF(AND(TRUE,TRUE),"x","")
    =IF(TRUE,"x","")
    ="x"

Notice the OR function is evaluated first because it is [nested](https://exceljet.net/glossary/nesting)
 inside the AND function. In other words, the OR function must return a result before the AND function can return a result. In the same way, both the OR function and the AND function must return a result before the IF function can return a result. In the end, the IF function returns "x", because the AND function returns TRUE. In cell E6, the formula evaluates like this:

    =IF(AND(OR(B6="red",B6="green"),C6>10),"x","")
    =IF(AND(OR(FALSE,FALSE),C6>10),"x","")
    =IF(AND(FALSE,FALSE),"x","")
    =IF(FALSE,"x","")
    =""

The result is an [empty string](https://exceljet.net/glossary/empty-string)
 (""), because the color is not "Red" or "Green" and the quantity is not greater than 10. Even if the quantity were greater than 10, the result would be the same because the color would not be "Red" or "Green".  

_Note: if we didn't supply an empty string ("") for the value\_if\_false argument, the formula would return FALSE when the logical test returned FALSE._

Related formulas
----------------

[![Excel formula: If cell equals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_0.png "Excel formula: If cell equals")](https://exceljet.net/formulas/if-cell-equals)

### [If cell equals](https://exceljet.net/formulas/if-cell-equals)

The goal is to do something if a cell equals a given value. The most common way to solve this problem is with the IF function. IF function The IF function runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this: =...

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If cell begins with x, y, or z](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_begins_with_x_y_or_z_0.png "Excel formula: If cell begins with x, y, or z")](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)

### [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)

The goal is to take a specific action when a value begins with "x", "y", or "z". As is often the case in Excel, there are multiple ways to approach this problem. The simplest way is to use the OR function with the LEFT function to create the required logical test. Another option is to use the...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

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
    
*   [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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