# Nested IF with multiple AND - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nested-if-with-multiple-and

---

[Skip to main content](https://exceljet.net/formulas/nested-if-with-multiple-and#main-content)

[](https://exceljet.net/formulas/nested-if-with-multiple-and#)

*   [Previous](https://exceljet.net/formulas/nested-if-function-example)
    
*   [Next](https://exceljet.net/formulas/only-calculate-if-not-blank)
    

[If](https://exceljet.net/formulas#If)

Nested IF with multiple AND
===========================

by Dave Bruns · Updated 17 May 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[AND](https://exceljet.net/functions/and-function)

[OR](https://exceljet.net/functions/or-function)

![Excel formula: Nested IF with multiple AND](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nested%20IF%20with%20multiple%20AND.png "Excel formula: Nested IF with multiple AND")

Summary
-------

To evaluate several options with a nested IF statement, one approach is a separate IF function per line to show the result of each set of logical tests. By adding line breaks after each IF function, the formula becomes self-documenting. In the example shown, the formula in D5 is:

    =
    IF(AND(B5="red",C5>=100),1.5,
    IF(AND(B5="red",C5<100),1.4,
    IF(AND(B5="blue",C5>=100),1.3,
    IF(AND(B5="blue",C5<100),1.2,
    1.1))))
    

Generic formula
---------------

    =
    IF(AND(A1="x",B1>=100),1.5,
    IF(AND(A1="y",B1< 100),1.4,
    IF(AND(A1="x",B1>=100),1.3,
    IF(AND(A1="y",B1< 100),1.2,
    1.1))))

Explanation 
------------

This formula relies on a technique called "nested IFs" to handle a series of options and results. With nested IFs, one IF function is nested inside another, a process that is [explained in some detail here](https://exceljet.net/articles/nested-ifs)
.

The formula in this example is purposely more verbose than necessary to "show" all possible options and results in a way that is easier to understand and maintain. The trick is to structure the formula with [line breaks](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 to show each IF on a separate line along with the "true result" for that IF. The "false result" is the following IF statement. Notice the final false result will "catch" any case that fails all previous tests.

Essentially, we are using line breaks to build a "table" that the human eye can easily read. In addition, we are using the AND function to run more than one logical test at a time to limit the number of IF functions. The AND function inside each [IF function](https://exceljet.net/functions/if-function)
 tests both color and value.

Note you can use [Alt + Enter](https://exceljet.net/keyboard-shortcuts/start-a-new-line-in-the-same-cell)
 to enter new lines in the formula bar. You'll need to [expand the formula bar vertically](https://exceljet.net/shortcuts/expand-or-collapse-the-formula-bar)
 to see more than one line at a time.

### More conditions

This formula approach can be expanded to evaluate more options. The AND function can handle more logical tests, and you can combine the AND function with the [OR function](https://exceljet.net/functions/or-function)
 if needed. You could also replace AND and OR with [boolean logic](https://exceljet.net/glossary/boolean-logic)
. Finally, you can also use the [IFS function](https://exceljet.net/functions/ifs-function)
 in later versions of Excel to reduce nesting.

### Result as calculation

Although the example above shows a numeric result for each set of options, the formula can be customized to run a calculation instead by replacing hardcoded values with any standard formula expression.

Related formulas
----------------

[![Excel formula: Nested IF function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nested_if_function_example.png "Excel formula: Nested IF function example")](https://exceljet.net/formulas/nested-if-function-example)

### [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)

The goal is to assign a grade to each score in column C according to the rules in the table in the range F4:G9. One way to do this in Excel is to use a series of nested IF functions. Generally, nested IFs formulas are used to test more than one condition and return a different result for each...

[![Excel formula: IF with boolean logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_with_boolean_logic.png "Excel formula: IF with boolean logic")](https://exceljet.net/formulas/if-with-boolean-logic)

### [IF with boolean logic](https://exceljet.net/formulas/if-with-boolean-logic)

The goal is to sum the quantity for rows where the color is "Red", the region is "East", and the quantity is greater than 7. Although there are a number of ways to solve this problem in Excel purpose of this example is to demonstrate how to replace a nested IF with a single IF using Boolean logic...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20formula%20with%20nested%20IFs-thumb.png)](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)

### [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)

In this video I'll show you how to create a formula that uses multiple, nested IF statements. This is a common technique to handle multiple conditions. Let's take a look. This worksheet shows a class of students with five test scores in columns D through H, and an average in column I. In column J...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20make%20a%20nested%20IF%20formula%20easier%20to%20read.png)](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

### [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

In this video we're going to look at how to make a nested IF formula more readable by adding line breaks. Here I have a worksheet that calculates sales commissions based on the commission structure shown in the table. For example, we can see that King sold $124,500 and gets a commission of 5%,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)
    
*   [IF with boolean logic](https://exceljet.net/formulas/if-with-boolean-logic)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

### Videos

*   [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)
    
*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    
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