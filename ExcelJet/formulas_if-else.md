# If else - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-else

---

[Skip to main content](https://exceljet.net/formulas/if-else#main-content)

[](https://exceljet.net/formulas/if-else#)

*   [Previous](https://exceljet.net/formulas/if-date-is-between-two-dates)
    
*   [Next](https://exceljet.net/formulas/if-not-blank-multiple-cells)
    

[If](https://exceljet.net/formulas#If)

If else
=======

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[IFS](https://exceljet.net/functions/ifs-function)

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel formula: If else](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_else.png "Excel formula: If else")

Summary
-------

To test a condition, and take one action if the condition is TRUE, and another action if the condition is FALSE, you can use the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in cell E5 is:

    =IF(D5="S","Small","Large")
    

As the formula is copied down, it returns "Small" when the value in column D is "S" and "Large" when the value in column D is "L". Note that _text values_ within the formula must be enclosed in double quotes ("").

Generic formula
---------------

    =IF(test,true_result,false_result)
    

Explanation 
------------

The goal is to return "Small" when the value in column D is "S" and "Large" when the value in column D is "L". In other words, if the value in column D is "S" return "Small" else return "Large".

### If else in Excel

The concept of "If else" in Excel is handled with the [IF function](https://exceljet.net/functions/if-function)
. The IF function runs a test, then returns one value if the result is TRUE, and a different value if the result is FALSE. The generic syntax for IF looks like this:

    =IF(test,true_result,false_result)

For example, to check cell A1 and return "Yes" if the value is greater than 100 and "No" if not, you can use the IF function like this:

    =IF(A1>100,"Yes","No")

Note that the "else" concept is built into the IF function. The first argument is the logical test, and the second argument is the result (or calculation) to return when the test is TRUE. The third argument is the "else" — the value or calculation to return if the result of the logical test is FALSE.

### Example worksheet problem

In the worksheet shown, we have a list of T-shirts that includes color and size. The sizes in column D are abbreviated, with "S" for small and "L" for large. There are only these two sizes in the data. Let's say you want to write a formula to expand these abbreviations and show either the word "Small" or "Large" in column E. In other words:

1.  If a cell in column D contains "S", return "Small".
2.  If a cell in column D contains "L", return "Large".

This is a perfect application of the IF function. To check the abbreviated size in column D and return either "Small" or "Large", the formula in cell E5 is:

    =IF(D5="S","Small","Large")
    

Translated, this means: _IF cell D5 equals "S", return "Small", ELSE return "Large"._

Notice we are only testing for "S" — we don't need to test for "L". That's because we only have two possible values, and the ELSE part of the formula (the FALSE result) logically takes care of "L" for us: if the cell doesn't contain "S", it _must be_ "L".

> Text values inside the IF function must be enclosed in double quotes (""), but numbers should _not_ be quoted. See our [IF Function page](https://exceljet.net/functions/if-function)
>  for more details.

### Nesting IFs  (if elseif)

As seen above, handling a single condition with the IF statement is simple. But how do you implement the idea of "If elseif" in Excel? The formula above works fine if we only have two sizes, Small ("S") and Large ("L"), but what if we have another size, "M" for "Medium"? In that case, we can extend the formula with another IF statement. We do this by replacing the existing FALSE result with a second IF function. In the example below, we've extended the formula to handle a medium size. The formula in E5 is:

    =IF(D5="S","Small",IF(D5="M","Medium","Large"))
    

![Nested IF function example](https://exceljet.net/sites/default/files/images/formulas/inline/if_else_with_nested_if.png "Nested IF function example")

Roughly translated, the formula now means: _"If D5 is "S" return "Small", elseif D5 is "M" return "Medium", else return "Large"._ This technique is called "[nesting](https://exceljet.net/glossary/nesting)
" since we are placing one function _inside_ another. When more than one IF function is nested together in a formula, you will sometimes hear the formula called a "Nested IF formula" or "Nested IFs" for short. [This page has many examples](https://exceljet.net/articles/nested-ifs)
. 

### Other options

It is possible to nest many IF functions together in a single formula. However, the longer a formula like this gets, the harder it is to read and maintain. Before you create a long nested IF formula, you should consider other options:

1.  The [IFS function](https://exceljet.net/functions/ifs-function)
     is designed to handle multiple options without nesting.
2.  The [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
     can handle _many_ options with a [simple formula](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    .

Related formulas
----------------

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

[![Excel IFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ifs.png "Excel IFS function")](https://exceljet.net/functions/ifs-function)

### [IFS Function](https://exceljet.net/functions/ifs-function)

The Excel IFS function can run multiple tests and return a value corresponding to the first TRUE result. Use the IFS function to evaluate multiple conditions without multiple nested IF statements. IFS allows shorter, easier to read formulas....

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

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

*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    
*   [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
    
*   [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)
    
*   [If cell contains](https://exceljet.net/formulas/if-cell-contains)
    
*   [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [IFS Function](https://exceljet.net/functions/ifs-function)
    
*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    

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