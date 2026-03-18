# If NOT this or that - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-not-this-or-that

---

[Skip to main content](https://exceljet.net/formulas/if-not-this-or-that#main-content)

[](https://exceljet.net/formulas/if-not-this-or-that#)

*   [Previous](https://exceljet.net/formulas/if-not-blank-multiple-cells)
    
*   [Next](https://exceljet.net/formulas/if-this-and-that)
    

[If](https://exceljet.net/formulas#If)

If NOT this or that
===================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[OR](https://exceljet.net/functions/or-function)

[NOT](https://exceljet.net/functions/not-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7860/download?token=7EdtjIKJ)
 (13.84 KB)

![Excel formula: If NOT this or that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/If_not_this_or_that.png "Excel formula: If NOT this or that")

Summary
-------

To do something when a cell is NOT this or that (i.e. a cell is NOT equal to "x", "y", etc.) you can use the [IF function](https://exceljet.net/videos/the-if-function)
 together with the [OR function](https://exceljet.net/functions/or-function)
 and the [NOT function](https://exceljet.net/functions/not-function)
. In cell D6, the formula is:

    =IF(NOT(OR(B6="red",B6="green")),"x","")
    

When copied down, it returns "x" when the color in column B contains any value _except_ "red" or "green". Otherwise, the formula returns an empty string ("") which looks like an empty cell in Excel. Notice that Excel is _not_ case-sensitive by default, B6="red", B6="Red", and B6="RED" will all return the same result.

Generic formula
---------------

    =IF(NOT(OR(A1="red",A1="green")),"x","")

Explanation 
------------

The goal is to "flag" records that are neither "Red" nor "Green". More specifically, we want to check the color in column B, and leave an "x" in rows where the color is NOT "Red" OR "Green". If the color _is_ "Red" OR "Green", we want to display nothing.

### IF function logic

The [IF function](https://exceljet.net/functions/if-function)
 is commonly used for simple tests. For example, to return "OK", when a value is over 100 and "Fail" if not, you can use the IF function in a formula like this:

    =IF(A1>100,"OK","Fail")

In this formula, A1>100 is the logical test. The behavior of the IF function can be easily extended by adding functions like [AND](https://exceljet.net/functions/and-function)
, [OR](https://exceljet.net/functions/or-function)
, and [NOT](https://exceljet.net/functions/not-function)
 to the logical test. For example, to _reverse_ the existing logic in the formula above, we can add NOT like this:

    =IF(NOT(A1>100),"OK","Fail")

Translation: _If the value in A1 is NOT greater than 100, then return "OK". Otherwise, return "Fail"._

In the worksheet shown, the goal is to mark records where the color is NOT "Red" OR "Green" with an "x". If the color _is_ "Red" or "Green" we don't want to do anything. The formula in cell D6 is:

    =IF(NOT(OR(B6="red",B6="green")),"x","")

In this formula, the logical test is this bit:

    NOT(OR(B6="red",B6="green"))
    

Working from the inside out, we first use the [OR function](https://exceljet.net/functions/or-function)
 to test for "red" or "green":

    OR(B6="red",B6="green")
    

OR will return TRUE if B6 is "Red" or "Green", and FALSE if B6  contains any other value. The [NOT function](https://exceljet.net/functions/not-function)
 simply reverses this result. Adding NOT means the test will return TRUE if B6 is NOT "Red" or "Green", and FALSE otherwise:

    NOT(OR(B6="red",B6="green"))
    

The rest of the formula is standard. Since we want to flag items that pass the test, we provide "x" for _value\_if\_true_. Since we don't want to display anything for other values, we provide an [empty string](https://exceljet.net/glossary/empty-string)
 ("") for _value\_if\_false_. This causes an "x" to appear in column D when the color in column B is NOT "Red" or "Green". You can extend the OR function to check additional conditions as needed.

Keep in mind that Excel is not case-sensitive by default, so the color names in the formula are all lowercase. The expressions B6="red", B6="Red", and B6="RED" will all return the same result. Also, notice that we need to provide an empty string ("") for the false result. This argument is _not_ required, but if we leave it empty, the formula will return FALSE when a color is "Red" or "Green".

### Increase price

You can use other formulas inside the IF function to run a different calculation instead of simply returning "x". For example, let's say you want to increase the price for all colors _except_ Red and Green by 15%. If the color is Red or Green, you want to leave the price alone. To perform this task, the formula in E6 below is:

    =IF(NOT(OR(B6="red",B6="green")),C6*1.15,C6)

![Increase price if color is NOT red or green](https://exceljet.net/sites/default/files/images/formulas/inline/If_not_this_or_that_increase_price.png "Increase price if color is NOT red or green")

Translation: _if the color is NOT "Red" or "Green", increase the price by 15%. Otherwise, return the original price._

Related formulas
----------------

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If cell equals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_0.png "Excel formula: If cell equals")](https://exceljet.net/formulas/if-cell-equals)

### [If cell equals](https://exceljet.net/formulas/if-cell-equals)

The goal is to do something if a cell equals a given value. The most common way to solve this problem is with the IF function. IF function The IF function runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this: =...

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

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

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
    
*   [If cell equals](https://exceljet.net/formulas/if-cell-equals)
    
*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    
*   [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

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