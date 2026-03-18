# Conditional message with REPT function - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/conditional-message-with-rept-function

---

[Skip to main content](https://exceljet.net/formulas/conditional-message-with-rept-function#main-content)

[](https://exceljet.net/formulas/conditional-message-with-rept-function#)

*   [Previous](https://exceljet.net/formulas/compare-two-strings)
    
*   [Next](https://exceljet.net/formulas/convert-numbers-to-text)
    

[Text](https://exceljet.net/formulas#Text)

Conditional message with REPT function
======================================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[REPT](https://exceljet.net/functions/rept-function)

[IF](https://exceljet.net/functions/if-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Conditional message with REPT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/conditional%20message%20with%20REPT.png "Excel formula: Conditional message with REPT function")

Summary
-------

To display a conditional message, without the IF function, you can use [boolean logic](https://exceljet.net/glossary/boolean-logic)
 and the [REPT function](https://exceljet.net/functions/rept-function)
. In the example shown, the formula in D5 (copied down) is:

    =REPT("low",C5<100)
    

If the value in column C is less than 100, the formula returns "low". If not, the formula returns an [empty string](https://exceljet.net/glossary/empty-string)
 (""), which looks like a blank cell.

Generic formula
---------------

    =REPT("message",logical test)

Explanation 
------------

This formula uses [boolean logic](https://exceljet.net/glossary/boolean-logic)
 to output a conditional message. If the value in column C is less than 100, the formula returns "low". If not, the formula returns an empty string ("").

Boolean logic is a technique of handling TRUE and FALSE values like 1 and 0. In cell C5, the formula is evaluated like this:

    =REPT("low",C5<100)
    =REPT("low",TRUE)
    =REPT("low",1)
    ="low"
    

In other words, if C5 < 100, output "low" 1 time. In cell C6, the formula is evaluated like this:

    =REPT("low",C6<100)
    =REPT("low",FALSE)
    =REPT("low",0)
    =""
    

In other words, if C6 < 100 is FALSE, output "low" zero times.

### IF function alternative

Conditional messages like this are more commonly handled with the IF function. With IF, the equivalent formula is:

    =IF(C5<100,"low","")
    

Both formulas return exactly the same result, but the REPT version is a bit simpler.

### Extending the logic

Boolean logic can be extended with simple math operations to handle more complex scenarios. Briefly, AND logic can be expressed with multiplication (\*) OR logic can be expressed with addition (+). For example, to return "low" only when (count < 100) AND (day = Monday) we can use boolean logic like this:

    =REPT("low",(C5<100)*(B5="Monday"))
    

The equivalent IF formula is:

    =IF(C5<100,IF(B5="Monday","low",""),"")
    

or, simplifying a bit with AND:

    =IF(AND(C5<100,B5="Monday"),"low","")
    

### Coercing TRUE and FALSE to 1 and zero

When using boolean logic, you'll sometimes need to force Excel to coerce TRUE and FALSE to 1 and zero. A simple way to do this is to use a [double-negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--).

Related formulas
----------------

[![Excel formula: IF with boolean logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_with_boolean_logic.png "Excel formula: IF with boolean logic")](https://exceljet.net/formulas/if-with-boolean-logic)

### [IF with boolean logic](https://exceljet.net/formulas/if-with-boolean-logic)

The goal is to sum the quantity for rows where the color is "Red", the region is "East", and the quantity is greater than 7. Although there are a number of ways to solve this problem in Excel purpose of this example is to demonstrate how to replace a nested IF with a single IF using Boolean logic...

[![Excel formula: If NOT this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If_not_this_or_that.png "Excel formula: If NOT this or that")](https://exceljet.net/formulas/if-not-this-or-that)

### [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)

The goal is to "flag" records that are neither "Red" nor "Green". More specifically, we want to check the color in column B, and leave an "x" in rows where the color is NOT "Red" OR "Green". If the color is "Red" OR "Green", we want to display nothing. IF function logic The IF function is commonly...

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: If cell is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_blank.png "Excel formula: If cell is blank")](https://exceljet.net/formulas/if-cell-is-blank)

### [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)

In the example worksheet, column D contains a date when a task is completed. If the task is not yet complete, the cell in column D will be empty (blank). In column E, the goal is to display the word "Open" when there is no date in column D. If there is a date in column D, the formula in column E...

Related functions
-----------------

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/intro%20to%20boolean%20logic-thumb.png)](https://exceljet.net/videos/intro-to-boolean-logic)

### [Intro to Boolean Logic](https://exceljet.net/videos/intro-to-boolean-logic)

In this video, I'm going to show you the basics of Boolean logic. Boolean logic is a great tool for simplifying formulas, especially those with many IF statements. So, to start off, what's a Boolean? A Boolean is a data type with only two possible values, TRUE or FALSE. You'll often see Boolean...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [IF with boolean logic](https://exceljet.net/formulas/if-with-boolean-logic)
    
*   [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)
    
*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    
*   [If cell is blank](https://exceljet.net/formulas/if-cell-is-blank)
    

### Functions

*   [REPT Function](https://exceljet.net/functions/rept-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [Intro to Boolean Logic](https://exceljet.net/videos/intro-to-boolean-logic)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    
*   [The double negative in Excel formulas](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
    

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