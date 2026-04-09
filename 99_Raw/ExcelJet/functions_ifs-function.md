# Excel IFS function | Exceljet

**Source:** https://exceljet.net/functions/ifs-function

---

[Skip to main content](https://exceljet.net/functions/ifs-function#main-content)

[](https://exceljet.net/functions/ifs-function#)

*   [Previous](https://exceljet.net/functions/ifna-function)
    
*   [Next](https://exceljet.net/functions/not-function)
    

Excel 2019

[Logical](https://exceljet.net/functions#Logical)

IFS Function
============

by Dave Bruns · Updated 1 Nov 2025

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[CHOOSE](https://exceljet.net/functions/choose-function)

[SWITCH](https://exceljet.net/functions/switch-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel IFS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20ifs.png "Excel IFS function")

Summary
-------

The Excel IFS function can run multiple tests and return a value corresponding to the first TRUE result. Use the IFS function to evaluate multiple conditions without multiple nested IF statements. IFS allows shorter, easier to read formulas.

Purpose 
--------

Test multiple conditions, return first true

Return value 
-------------

Value corresponding with first TRUE result

Syntax
------

    =IFS(test1,value1,[test2, value2],...)

*   _test1_ - First logical test.
*   _value1_ - Result when test1 is TRUE.
*   _test2, value2_ - \[optional\] Second test/value pair.

Using the IFS function 
-----------------------

The IFs function evaluates multiple expressions and returns a result that corresponds to the first TRUE result. You can use the IFS function when you want a self-contained formula to test multiple conditions at the same time without [nesting](https://exceljet.net/glossary/nesting)
 multiple IF statements. Formulas based on IFS are shorter and easier to read and write.

Conditions are provided to the IFS function as test/value pairs, and IFS can handle up to 127 conditions. Each test represents a [logical test](https://exceljet.net/glossary/logical-test)
 that returns TRUE or FALSE, and the value that follows will be returned when the test returns TRUE. In the event that more than one condition returns TRUE, the value corresponding to the first TRUE result is returned. For this reason, it is important to consider the order in which conditions appear.

### Structure

An IFS formula with 3 tests can be visualized like this:

    =IFS(
    test1,value1 // pair 1
    test2,value2 // pair 2
    test3,value3 // pair 3
    )
    

A value is returned by IFS only when the previous test returns TRUE, and the first test to return TRUE "wins".  For better readability, you can [add line breaks](https://exceljet.net/shortcuts/insert-line-break-in-cell)
 to an IFS formula as shown above.

_Note: the IFS function does not provide an argument for a default value. See Example #3 below for a workaround._

### Example #1 - grades, lowest to highest

In the example shown below, the IFS function is used to assign a grade based on a score. The formula in E5, copied down, is:

    =IFS(C5<60,"F",C5<70,"D",C5<80,"C",C5<90,"B",C5>=90,"A")
    

Notice the conditions are entered "in order" to test lower scores first. The grade associated with the first test to return TRUE is returned.

### Example #2 - rating, highest to lowest

In a simple rating system, a score of 3 or greater is "Good", a score between 2 and 3 is "Average", and anything below 2 is "Poor".  To assign these values with IFS, three conditions are used:

    =IFS(A1>=3,"Good",A1>=2,"Average",A1<2,"Poor")
    

Notice in this case, conditions are arranged to test higher values first.

### Example #3 - default value

The IFS function does not have a built-in default value to use when all conditions are FALSE. However, to provide a default value, you can enter TRUE as a final test, followed by a value to use as a default.

In the example below, a status code of 100 is "OK", a code of 200 is "Warning", and a code of 300 is "Error". Any other code value is invalid, so TRUE is provided as the final test, and "Invalid" is provided as a "default" value.

    =IFS(A1=100,"OK",A1=200,"Warning",A1=300,"Error",TRUE,"Invalid")
    

When the value in A1 is 100, 200, or 300, IFS will return the messages shown above. When A1 contains any other value (including when A1 is empty) IFS will return "Invalid". Without this final condition, IFS will return #N/A when a code is not recognized.

### IFS and performance

You might expect the IFS function to "short-circuit" and stop evaluating once it finds a logical test that returns TRUE, but this is not the case. IFS evaluates [all conditions and expressions](https://fastexcel.wordpress.com/2023/01/03/short-circuiting-excel-formulas-if-choose-ifs-and-switch/)
, even when the first logical test is TRUE. This behavior can degrade performance when an IFS formula includes complex or time-consuming calculations, since those calculations may still run even when their conditions are FALSE. It can also cause problems in recursive LAMBDA functions, because the “else” branch is evaluated even when it should be bypassed, potentially triggering unintended recursion and a #NUM! error.

To avoid these issues, consider rewriting the formula with nested [IF functions](https://exceljet.net/functions/if-function)
 or using the simpler [CHOOSE function](https://exceljet.net/functions/choose-function)
. Both IF and CHOOSE perform true short-circuit evaluation, skipping unnecessary calculations once a valid result is found.

### IFS versus SWITCH

Like the [SWITCH function](https://exceljet.net/functions/switch-function)
, the IFS function allows you to test more than one condition in a single self-contained formula. Both functions make it easier to write (and read) a formula with many conditions. One advantage of SWITCH over IFS is that the expression appears just once in the function and does not need to be repeated. In addition, SWITCH can accept a default value. However, SWITCH is limited to exact matching. It is not possible to use operators like greater than (>) or less than (<) with the standard syntax. In contrast, the IFS function _requires_ expressions for each condition, so you can use [logical operators](https://exceljet.net/glossary/logical-operators)
 as needed.

### Notes

*   The IFS function does not have a built-in default value to use when all conditions are FALSE.
*   To provide a default value, enter TRUE as a final test, and a value to return when no other conditions are met.
*   All logical tests must return TRUE or FALSE. Any other result will cause IFS to return a #VALUE! error.
*   If no logical tests return TRUE, IFS will return the #N/A error.
*   IFS does not have short-circuit behavior; all expressions are evaluated

IFS function examples
---------------------

[![Excel formula: Calculate sales commission with if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_sales_commission_with_if.png "Excel formula: Calculate sales commission with if")](https://exceljet.net/formulas/calculate-sales-commission-with-if)

### [Calculate sales commission with if](https://exceljet.net/formulas/calculate-sales-commission-with-if)

Imagine a company that uses a tiered commission structure for its sales team. Each salesperson is assigned a commission rate based on the total sales they have made. The commission tiers are structured like this: For sales less than $10,000, the commission rate is 10%. For sales from $10,000 to $20...

[![Excel formula: If else](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_else.png "Excel formula: If else")](https://exceljet.net/formulas/if-else)

### [If else](https://exceljet.net/formulas/if-else)

The goal is to return "Small" when the value in column D is "S" and "Large" when the value in column D is "L". In other words, if the value in column D is "S" return "Small" else return "Large". If else in Excel The concept of "If else" in Excel is handled with the IF function . The IF function...

[![Excel formula: Nested IF function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nested_if_function_example.png "Excel formula: Nested IF function example")](https://exceljet.net/formulas/nested-if-function-example)

### [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)

The goal is to assign a grade to each score in column C according to the rules in the table in the range F4:G9. One way to do this in Excel is to use a series of nested IF functions. Generally, nested IFs formulas are used to test more than one condition and return a different result for each...

[![Excel formula: Time since start in day ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time%20since%20start%20in%20day%20ranges.png "Excel formula: Time since start in day ranges")](https://exceljet.net/formulas/time-since-start-in-day-ranges)

### [Time since start in day ranges](https://exceljet.net/formulas/time-since-start-in-day-ranges)

In this example, the goal is to calculate durations in "days" starting from the start date and time in cell G5 and ending at the dates and times shown in column B. The twist is that we want to classify the durations using the custom labels shown in column E, starting with "Day 0" for the first 24...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel CHOOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choose%20function.png "Excel CHOOSE function")](https://exceljet.net/functions/choose-function)

### [CHOOSE Function](https://exceljet.net/functions/choose-function)

The Excel CHOOSE function returns a value from a list using a given position or index. For example, =CHOOSE(2,"red","blue","green") returns "blue", since blue is the 2nd value listed after the index number. The values provided to CHOOSE can include references.

[![Excel SWITCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20switch.png "Excel SWITCH function")](https://exceljet.net/functions/switch-function)

### [SWITCH Function](https://exceljet.net/functions/switch-function)

The Excel SWITCH function compares one value against a list of values, and returns a result corresponding to the first match found. When no match is found, SWITCH can return an optional default value....

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

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
    
*   [Time since start in day ranges](https://exceljet.net/formulas/time-since-start-in-day-ranges)
    
*   [Calculate sales commission with if](https://exceljet.net/formulas/calculate-sales-commission-with-if)
    
*   [If else](https://exceljet.net/formulas/if-else)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [CHOOSE Function](https://exceljet.net/functions/choose-function)
    
*   [SWITCH Function](https://exceljet.net/functions/switch-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Links

*   [Microsoft IFS function documentation](https://support.office.com/en-us/article/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45)
    
*   [Short-circuiting Excel Formulas - FastExcel (Charles Williams)](https://fastexcel.wordpress.com/2023/01/03/short-circuiting-excel-formulas-if-choose-ifs-and-switch/)
    
*   [Excel IFS short circuit evaluation (learn.microsoft.com)](https://learn.microsoft.com/en-us/answers/questions/5198974/excel-ifs-short-circuit-evaluation)
    

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