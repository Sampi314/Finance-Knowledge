# Excel OR function | Exceljet

**Source:** https://exceljet.net/functions/or-function

---

[Skip to main content](https://exceljet.net/functions/or-function#main-content)

[](https://exceljet.net/functions/or-function#)

*   [Previous](https://exceljet.net/functions/not-function)
    
*   [Next](https://exceljet.net/functions/switch-function)
    

Excel 2003

[Logical](https://exceljet.net/functions#Logical)

OR Function
===========

by Dave Bruns · Updated 22 May 2024

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[IF](https://exceljet.net/functions/if-function)

[XOR](https://exceljet.net/functions/xor-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel OR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_or_function.png "Excel OR function")

Summary
-------

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined with NOT and AND to create complex logical tests.

Purpose 
--------

Test multiple conditions at the same time

Return value 
-------------

TRUE or FALSE

Syntax
------

    =OR(logical1,[logical2],...)

*   _logical1_ - The first condition or logical value to evaluate.
*   _logical2_ - \[optional\] The second condition or logical value to evaluate.

Using the OR function 
----------------------

The OR function is one of Excel's logical functions. It is designed to test multiple conditions simultaneously and return TRUE if _any_ condition is TRUE. If _all_ conditions are FALSE, the OR function returns FALSE. The OR function is often combined with other functions like AND, NOT, and IF to construct more complex logical tests. It commonly appears in the logical test of the IF function and in formulas for conditional formatting and data validation. The OR function is a good way to simplify complicated formulas use many [nested IFs](https://exceljet.net/articles/nested-ifs)
.

### OR function basics

The purpose of the OR function is to evaluate more than one [logical test](https://exceljet.net/glossary/logical-test)
 at the same time and return TRUE _if any result is TRUE_. Excel's OR function can handle up to 255 separate conditions, which are entered as arguments with names like "logical1", "logical2", and "logical3", etc. Each "logical" is a condition that can be evaluated as TRUE or FALSE. The arguments provided to the OR function can be constants, cell references, or logical expressions. OR will return TRUE _if any condition is TRUE:_

    =OR(FALSE,FALSE,TRUE) // returns TRUE

If all conditions are FALSE, OR will return FALSE:

    =OR(FALSE,FALSE,FALSE) // returns FALSE

Typically, logical arguments are provided to OR as logical expressions, for example:

    =OR(A1>0,A1<5)
    =OR(A1>0,B1>0)
    =OR(A1="red",B1="small")

All expressions in the formulas above will be evaluated as TRUE or FALSE. Notice that text values used in comparisons must be enclosed in double quotes (""). Be aware that OR will also evaluate numbers as TRUE or FALSE, and treat [any number except zero (0) as TRUE](https://exceljet.net/videos/introduction-to-booleans)
. You can see this behavior in the formulas below:

    =OR(0,0,3) // returns TRUE
    =OR(0,0,0) // returns FALSE

Let's look at some practical ways to use the OR function.

### Example - value is x or y or z

You can use OR to test for one of several values. For example, in the worksheet below, we are using the OR function to test if the codes in column B are 115, 120, or 125. The formula in cell D5 is:

    =OR(B5=115,B5=120,B5=125)

![Using the OR function to test for one of several values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/or_function_test_for_one_of_several_values.png "Using the OR function to test for one of several values")

Notice that we are testing for numeric values so the numbers appear in their raw form _without_ quotes ("").

### Example - OR with the IF function

The OR function is often embedded inside the [IF function](https://exceljet.net/functions/if-function)
 as the logical test to simplify what would otherwise be a more complex formula. For example, in the worksheet below, the goal is to test scores in columns B and C. If either score is below 750, the result should be "Deny". If both scores are 750 or above, the result should be "Approve". The formula in cell E5 is:

    =IF(OR(B5<750,C5<750),"Deny","Approve")
    

![Using the OR function with the IF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/or_function_with_the_if_function.png "Using the OR function with the IF function")

As the formula is copied down, it returns "Approve" or "Deny" for each row in the data.

### Example - IF this OR that

The worksheet below is a variation of the example above. This time, the goal is to flag rows where the color is "red" and the size is "small". The formula in cell D5 is:

    =IF(OR(B5="red",B5="green"),"x","")

![Using the OR function to flag specific rows](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/or_function_if_this_or_that.png "Using the OR function to flag specific rows")

You are free to replace "x" with any other value. Notice that the OR function is _not case-sensitive_. The lowercase "red" and "small" text strings equal the "Red" and "Small" text on the worksheet.

### Example - OR with AND

You can combine the OR function with the [AND function](https://exceljet.net/functions/and-function)
 to build more advanced conditions. In the worksheet below, the goal is to identify records where the color is "red" or "green" and the quantity is over 100. The logical test inside the IF function is created with AND and OR:

    AND(OR(B5="red",B5="green"),C5>100)

The complete formula in E5 is:

    =IF(AND(OR(B5="red",B5="green"),C5>100),"x","")

![Using OR and AND together inside IF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/or_function_with_the_and_function.png "Using OR and AND together inside IF")

Notice that the text values "red" and "green" _are_ enclosed in double quotes ("") but the number 100 _is not_.

### Example - OR with conditional formatting

The OR function is often used in the rules that trigger conditional formatting. In the worksheet below, we have adapted the formula in the example above to apply conditional formatting to rows where the color is "red" or "green" and the quantity is over 100. The conditional formatting is applied to the range B5:C15, and the formula to trigger the rule looks like this:

    =AND(OR($B5="red",$B5="green"),$C5>100)

Notice $B5 and $C5 are [mixed references](https://exceljet.net/glossary/mixed-reference)
 with the column fixed in order to highlight entire rows.

![Using the OR function to apply conditional formatting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/or_function_with_conditional_formatting.png "Using the OR function to apply conditional formatting")

### Example - OR with a range

It is possible to use OR with a range of values. In the worksheet below, the formula in cell J5 is:

    =IF(OR(C5:H5<65),"Fail","Pass")

![Using the OR function with a range of values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/or_function_with_a_range_of_values.png "Using the OR function with a range of values")

_Note: this is an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 and must be entered with Control + Shift + Enter in Excel 2019 and earlier. In Excel 2021 or later, the formula "just works" without special handling._

In the example above, the AND function is used inside the IF function as the logical test. This formula will return "Pass" only if the score for all six subjects is greater than 65. Otherwise, the result is "Fail". See also [Must pass 4 out of 6 subjects](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects)
.

> Pro-tip - as seen above, the OR function will aggregate _multiple_ results into a _single_ result. This means OR can't be used in array operations that must create an array of results. To work around this limitation, you can use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
> . For more information, see [Array formulas with AND and OR logic](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
> .

### Notes

*   Each logical condition must evaluate to TRUE or FALSE.
*   Text values or empty cells supplied as arguments are ignored.
*   The OR function will return #VALUE if no logical values are found
*   The OR function can handle up to 255 conditions in Excel.
*   If any condition is TRUE, OR returns TRUE
*   If all conditions are FALSE, OR returns FALSE
*   The OR function is not case-sensitive.
*   The OR function does not support [wildcards](https://exceljet.net/glossary/wildcard)
    .

OR function examples
--------------------

[![Excel formula: If cell contains this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_contains_this_or_that.png "Excel formula: If cell contains this or that")](https://exceljet.net/formulas/if-cell-contains-this-or-that)

### [If cell contains this or that](https://exceljet.net/formulas/if-cell-contains-this-or-that)

The goal is to do something if a cell contains one substring or another. Most users will think first of the IF function. However, one problem with IF is that it does not support wildcards like "?" and "\*". This means we can't use IF by itself to test for a substring like "abc" or "xyz" that might...

[![Excel formula: Sequence of leap years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_leap_years.png "Excel formula: Sequence of leap years")](https://exceljet.net/formulas/sequence-of-leap-years)

### [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)

In this example, the goal is to generate a list of leap years between a given start year and end year. The worksheet is set up so that the start year is an input in cell B5 and the end year is an input in cell B8. If either value changes, the formula should generate a new list of leap years. In the...

[![Excel formula: Conditional formatting column is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Conditional%20formatting%20column%20is%20blank.png "Excel formula: Conditional formatting column is blank")](https://exceljet.net/formulas/conditional-formatting-column-is-blank)

### [Conditional formatting column is blank](https://exceljet.net/formulas/conditional-formatting-column-is-blank)

When conditional formatting is applied with a formula, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the active cell when the rule is created is assumed to be cell E5, with the range E5:E14 selected. As the formula is evaluated...

[![Excel formula: If cell begins with x, y, or z](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_begins_with_x_y_or_z_0.png "Excel formula: If cell begins with x, y, or z")](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)

### [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)

The goal is to take a specific action when a value begins with "x", "y", or "z". As is often the case in Excel, there are multiple ways to approach this problem. The simplest way is to use the OR function with the LEFT function to create the required logical test. Another option is to use the...

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: Range contains duplicates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/range%20contains%20duplicates.png "Excel formula: Range contains duplicates")](https://exceljet.net/formulas/range-contains-duplicates)

### [Range contains duplicates](https://exceljet.net/formulas/range-contains-duplicates)

In this example, the goal is to test if a given range contains duplicate values and return TRUE if duplicates exist and FALSE if not. This is essentially a counting problem and the solution is based on the COUNTIF function , which counts values in a range that meet supplied criteria. The formula...

[![Excel formula: Year is a leap year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/year_is_leap_year.png "Excel formula: Year is a leap year")](https://exceljet.net/formulas/year-is-a-leap-year)

### [Year is a leap year](https://exceljet.net/formulas/year-is-a-leap-year)

In this example, the goal is to write a formula that will return TRUE if a year is a leap year and FALSE if not. This is a surprisingly challenging problem in Excel for two reasons: (1) Excel thinks 1900 is a leap year due to a long-standing bug inherited from Lotus 1-2-3 and (2) The logic for...

[![Excel formula: Gantt chart time schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/gantt%20chart%20time%20schedule.png "Excel formula: Gantt chart time schedule")](https://exceljet.net/formulas/gantt-chart-time-schedule)

### [Gantt chart time schedule](https://exceljet.net/formulas/gantt-chart-time-schedule)

Note: this is a great example of a formula that is hard to understand because the cell references are hard to interpret. The gist of the logic used is this: if the time in row 4 is between the start and end times, the formula should return TRUE and trigger the blue fill via conditional formatting...

[![Excel formula: If this AND that OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that_or_that.png "Excel formula: If this AND that OR that")](https://exceljet.net/formulas/if-this-and-that-or-that)

### [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)

The goal is to mark rows where the color is "Red" AND the size is "Small" or "Medium". To perform this task, you can use the IF function in combination with the AND function and the OR function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different...

[![Excel formula: Highlight dates that are weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight_dates_that_are_weekends.png "Excel formula: Highlight dates that are weekends")](https://exceljet.net/formulas/highlight-dates-that-are-weekends)

### [Highlight dates that are weekends](https://exceljet.net/formulas/highlight-dates-that-are-weekends)

In this example, the goal is to highlight dates that occur on weekends. In other words, we want to highlight dates that land on either Saturday or Sunday. This problem can be easily solved by applying conditional formatting with a formula based on the WEEKDAY function together with the OR function...

[![Excel formula: Only calculate if not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20not%20blank%20then%20calculate2.png "Excel formula: Only calculate if not blank")](https://exceljet.net/formulas/only-calculate-if-not-blank)

### [Only calculate if not blank](https://exceljet.net/formulas/only-calculate-if-not-blank)

The goal is to verify the input of all required values before calculating a result. In the worksheet shown, the SUM function is used as an example only. You can use the same approach with any formula to prevent calculation until all required values are available. The logic can be adjusted in many...

[![Excel formula: Highlight row and column intersection exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20row%20and%20column%20intersection%20exact%20match.png "Excel formula: Highlight row and column intersection exact match")](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)

### [Highlight row and column intersection exact match](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)

Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, cell B3 in this case. To highlight matching rows, we use this logical expression: $B4=$K$5 The reference to B4 is mixed , with the column locked and row unlocked, so that...

[![Excel formula: Nested IF with multiple AND](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nested%20IF%20with%20multiple%20AND.png "Excel formula: Nested IF with multiple AND")](https://exceljet.net/formulas/nested-if-with-multiple-and)

### [Nested IF with multiple AND](https://exceljet.net/formulas/nested-if-with-multiple-and)

This formula relies on a technique called "nested IFs" to handle a series of options and results. With nested IFs, one IF function is nested inside another, a process that is explained in some detail here . The formula in this example is purposely more verbose than necessary to "show" all possible...

[![Excel formula: Highlight approximate match lookup conditional formatting](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20approximate%20match%20lookups.png "Excel formula: Highlight approximate match lookup conditional formatting")](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)

### [Highlight approximate match lookup conditional formatting](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)

This formula uses 4 named ranges, defined as follows: width=K6 height=K7 widths=B6:B11 heights=C5:H5 Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, which is cell B5 in this case. To highlight the matching row, we use this...

[![Excel formula: If cell is x or y and z](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_x_or_y_and_z.png "Excel formula: If cell is x or y and z")](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)

### [If cell is x or y and z](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)

The goal is to identify records where the color is "Red" or "Green" and the quantity is greater than 10. If a row meets all conditions, the formula should return "x". If any condition is not true, the formula should return an empty string (""). This problem can be solved with the IF function...

OR function videos
------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20approximate%20match%20lookups-Thumb.png)](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

### [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

In this video, we'll look at how to highlight approximate match lookups with conditional formatting. Here we have a simple lookup table that shows material costs for various heights and widths. The formula in K8 uses the INDEX and MATCH functions to retrieve the correct cost based on width and...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20using%20multiple%20criteria-thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)

### [How to highlight rows using multiple criteria](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)

In this video, we'll look at how to use conditional formatting to highlight entire rows using multiple criteria. Here we have an example we looked at previously. With one conditional formatting rule that uses a formula, we're able to highlight rows based on the task owner. This works well. But what...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/If%20this%20OR%20that-thumb.png)](https://exceljet.net/videos/if-this-or-that)

### [If this OR that](https://exceljet.net/videos/if-this-or-that)

Sometimes, you might need to write a formula that uses the IF function to test for this OR that, or this AND that. There are two special functions, AND and OR, that make this easy to do. Let's take a look. In this first worksheet, we have a list of employees. Let's assume that you need to group...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20with%20two%20variable%20input-thumb.png)](https://exceljet.net/videos/conditional-formatting-with-two-variable-inputs)

### [Conditional formatting with two variable inputs](https://exceljet.net/videos/conditional-formatting-with-two-variable-inputs)

In this video, we'll look at how to extend a conditional formatting formula so that so that it checks more than just one condition. Let's take a look. Here we have the example we looked at previously. We have a single conditional formatting rule that uses a formula to highlight cells that have a...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel XOR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20xor.png "Excel XOR function")](https://exceljet.net/functions/xor-function)

### [XOR Function](https://exceljet.net/functions/xor-function)

The XOR function performs what is called "exclusive OR". With two logical statements, XOR returns TRUE if either statement is TRUE, but returns FALSE if both statements are TRUE. If neither is TRUE, XOR also returns FALSE.

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Year is a leap year](https://exceljet.net/formulas/year-is-a-leap-year)
    
*   [Gantt chart time schedule](https://exceljet.net/formulas/gantt-chart-time-schedule)
    
*   [Highlight row and column intersection exact match](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)
    
*   [If cell contains this or that](https://exceljet.net/formulas/if-cell-contains-this-or-that)
    
*   [Nested IF with multiple AND](https://exceljet.net/formulas/nested-if-with-multiple-and)
    
*   [Highlight approximate match lookup conditional formatting](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)
    
*   [Sequence of leap years](https://exceljet.net/formulas/sequence-of-leap-years)
    
*   [Highlight dates that are weekends](https://exceljet.net/formulas/highlight-dates-that-are-weekends)
    
*   [MAP with AND and OR logic](https://exceljet.net/formulas/map-with-and-and-or-logic)
    
*   [If cell begins with x, y, or z](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)
    

### Videos

*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    
*   [How to highlight rows using multiple criteria](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)
    
*   [Conditional formatting with two variable inputs](https://exceljet.net/videos/conditional-formatting-with-two-variable-inputs)
    
*   [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [XOR Function](https://exceljet.net/functions/xor-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

### Links

*   [Microsoft OR function documentation](https://support.office.com/en-us/article/or-function-7d17ad14-8700-4281-b308-00b131e22af0)
    

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