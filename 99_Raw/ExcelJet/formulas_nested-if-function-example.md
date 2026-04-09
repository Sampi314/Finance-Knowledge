# Nested IF function example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/nested-if-function-example

---

[Skip to main content](https://exceljet.net/formulas/nested-if-function-example#main-content)

[](https://exceljet.net/formulas/nested-if-function-example#)

*   [Previous](https://exceljet.net/formulas/invoice-age-and-status)
    
*   [Next](https://exceljet.net/formulas/nested-if-with-multiple-and)
    

[If](https://exceljet.net/formulas#If)

Nested IF function example
==========================

by Dave Bruns · Updated 30 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[IFS](https://exceljet.net/functions/ifs-function)

![Excel formula: Nested IF function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/nested_if_function_example.png "Excel formula: Nested IF function example")

Summary
-------

The [IF function](https://exceljet.net/videos/the-if-function)
 can be [nested](https://exceljet.net/glossary/nesting)
 inside of itself to handle multiple conditions. In the example shown, a nested IF formula is used to assign a grade to a score. The formula in D5 contains 4 separate IF functions:

    =IF(C5<64,"F",IF(C5<73,"D",IF(C5<85,"C",IF(C5<95,"B","A"))))
    

As the formula is copied down, it returns the correct grade for each score in column C.

_For another good example of a nested if formula, see: [Calculate sales commission with IF](https://exceljet.net/formulas/calculate-sales-commission-with-if)
._

Generic formula
---------------

    =IF(T1,R1,IF(T2,R2,IF(T3,R3,IF(T4,R4,R5))))

Explanation 
------------

The goal is to assign a grade to each score in column C according to the rules in the table in the range F4:G9. One way to do this in Excel is to use a series of nested IF functions. Generally, nested IFs formulas are used to test more than one condition and return a different result for each condition.

### Testing more than one condition

If you need to test for more than one condition, then take one of several actions, depending on the result of the tests, one option is to nest multiple IF statements together in one formula. You'll often hear this referred to as "nested IFs". The idea of nesting comes from embedding or "nesting" one IF function inside another. In the workbook shown, we are nesting IF functions to assign grades based on a score. The rules for assigning each grade can be seen in the table below:

| Score | Grade |
| --- | --- |
| 0-63 | F   |
| 64-72 | D   |
| 73-84 | C   |
| 85-94 | B   |
| 95-100 | A   |

To create a nested IF formula that reflects this logic, start we can start either at the bottom of the scale, or the top. In this example, we start at the bottom. The first condition to test is if the score is below 64:

    =IF(C5<64,"F"

If the result is TRUE, we return "F". If the result is FALSE, we move into the next IF function. This time, we test to see if the score is less than 73:

    =IF(C5<64,"F",IF(C5<73,"D"

If TRUE, we return "D". We don't need to worry about scores less than 64 anymore, because that case is already handled. If the result is FALSE, we move to the next condition, which checks if the score is less than 85:

    =IF(C5<64,"F",IF(C5<73,"D",IF(C5<85,"C"

 If TRUE, we return "C". If FALSE, we move to the next condition, which checks if the score is less than 95:

    =IF(C5<64,"F",IF(C5<73,"D",IF(C5<85,"C",IF(C5<95,"B"

If TRUE, we return "B". At this point, the only condition to check is if the score is between 95 and 100. However, by process of elimination, we know that if the score has not yet passed any tests, it must be between 95 and 100. So, we only need to provide "A" in the last IF for the _value\_if\_false_ argument, and close up the formula with 4 parentheses, one for each IF function. The final formula in D5 is:

    =IF(C5<64,"F",IF(C5<73,"D",IF(C5<85,"C",IF(C5<95,"B","A"))))
    

You can see that it's important in this case to move in one direction, either low to high, or high to low. This allows us to return a result whenever a test returns TRUE, because we _know_ that any previous tests already returned FALSE.

### Making nested IFs easier to read

By their nature, nested IF formulas can be hard to read. To make a nested IF easier to understand, you can add line breaks inside the formula to "line up" the tests and results line this:

    =
    IF(C5<64,"F",
    IF(C5<73,"D",
    IF(C5<85,"C",
    IF(C5<95,"B",
    "A"))))
    

The line breaks do not affect the formula. The Excel formula engine will ignore them.

Video: [How to add line breaks to a nested if](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

### IFS function

Another way to solve this problem is with the IFS function, which can handle multiple conditions without nesting. The equivalent formula with IFs is:

    =IFS(C5<64,"F",C5<73,"D",C5<85,"C",C5<95,"B",C5>95,"A")

The IFS function doesn't have a "default" value to return after all tests have run, so we need to use another logical test for the last category of scores, scores above 95. One workaround is to use TRUE as the last test, which you can see in the formula below.

    =IFS(C5<64,"F",C5<73,"D",C5<85,"C",C5<95,"B",TRUE,"A")

Read more: [How to use the IFS function](https://exceljet.net/functions/ifs-function)
.

### Notes

1.  [VLOOKUP](https://exceljet.net/functions/vlookup-function)
     can sometimes be used to [replace complicated nested ifs](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    .
2.  This article has [many more examples of nested ifs with alternatives](https://exceljet.net/articles/nested-ifs)
    .

Related formulas
----------------

[![Excel formula: Nested IF with multiple AND](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nested%20IF%20with%20multiple%20AND.png "Excel formula: Nested IF with multiple AND")](https://exceljet.net/formulas/nested-if-with-multiple-and)

### [Nested IF with multiple AND](https://exceljet.net/formulas/nested-if-with-multiple-and)

This formula relies on a technique called "nested IFs" to handle a series of options and results. With nested IFs, one IF function is nested inside another, a process that is explained in some detail here . The formula in this example is purposely more verbose than necessary to "show" all possible...

[![Excel formula: Invoice age and status](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/invoice_age_and_status.png "Excel formula: Invoice age and status")](https://exceljet.net/formulas/invoice-age-and-status)

### [Invoice age and status](https://exceljet.net/formulas/invoice-age-and-status)

The goal is to calculate the correct invoice status ("OK", "Paid", or "Overdue") using the following rules: If there is an "x" in the "Paid" column, return "Paid". If there is not an "x" in the "Paid" column, and if the age is less than 31 days, return "OK" If there is not an "x" in the "Paid"...

[![Excel formula: Calculate sales commission with if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_sales_commission_with_if.png "Excel formula: Calculate sales commission with if")](https://exceljet.net/formulas/calculate-sales-commission-with-if)

### [Calculate sales commission with if](https://exceljet.net/formulas/calculate-sales-commission-with-if)

Imagine a company that uses a tiered commission structure for its sales team. Each salesperson is assigned a commission rate based on the total sales they have made. The commission tiers are structured like this: For sales less than $10,000, the commission rate is 10%. For sales from $10,000 to $20...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel IFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ifs.png "Excel IFS function")](https://exceljet.net/functions/ifs-function)

### [IFS Function](https://exceljet.net/functions/ifs-function)

The Excel IFS function can run multiple tests and return a value corresponding to the first TRUE result. Use the IFS function to evaluate multiple conditions without multiple nested IF statements. IFS allows shorter, easier to read formulas....

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

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Nested IF with multiple AND](https://exceljet.net/formulas/nested-if-with-multiple-and)
    
*   [Invoice age and status](https://exceljet.net/formulas/invoice-age-and-status)
    
*   [Calculate sales commission with if](https://exceljet.net/formulas/calculate-sales-commission-with-if)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [IFS Function](https://exceljet.net/functions/ifs-function)
    

### Videos

*   [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)
    
*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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