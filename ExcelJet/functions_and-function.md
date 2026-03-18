# Excel AND function | Exceljet

**Source:** https://exceljet.net/functions/and-function

---

[Skip to main content](https://exceljet.net/functions/and-function#main-content)

[](https://exceljet.net/functions/and-function#)

*   Previous
*   [Next](https://exceljet.net/functions/false-function)
    

Excel 2003

[Logical](https://exceljet.net/functions#Logical)

AND Function
============

by Dave Bruns · Updated 22 May 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[OR](https://exceljet.net/functions/or-function)

[XOR](https://exceljet.net/functions/xor-function)

[NOT](https://exceljet.net/functions/not-function)

![Excel AND function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_and_0.png "Excel AND function")

Summary
-------

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other functions like IF, NOT, and OR to create complex logical tests.

Purpose 
--------

Test multiple conditions at the same time

Return value 
-------------

TRUE if all conditions are met, otherwise FALSE

Syntax
------

    =AND(logical1,[logical2],...)

*   _logical1_ - The first condition or logical value to evaluate.
*   _logical2_ - \[optional\] The second condition or logical value to evaluate.

Using the AND function 
-----------------------

The AND function is one of Excel's logical functions. It is designed to test multiple conditions simultaneously and return TRUE only if all the conditions are met. If any condition is not met AND will return FALSE. You can use the AND function to check if a series of values all meet certain criteria before performing a calculation or action. The AND function is often combined with other functions like IF, NOT, and OR to construct more complex logical tests. It commonly appears in the logical test of the IF function and in the rules used for conditional formatting and data validation. The AND function is a good way to avoid complicated formulas that involve many [nested IFs](https://exceljet.net/articles/nested-ifs)
.

### AND function basics

The purpose of the AND function is to evaluate multiple conditions and only return TRUE if all conditions are TRUE. Excel's AND function can handle up to 255 separate conditions, which are entered as arguments with names like "logical1", "logical2", and "logical3", etc. Each "logical" is a condition that must be TRUE. The arguments provided to the AND function can be constants, cell references, or logical expressions. AND will return TRUE _only if all results are TRUE:_

    =AND(TRUE,TRUE,TRUE) // returns TRUE

If any argument is FALSE, AND will immediately return FALSE:

    =AND(TRUE,TRUE,FALSE) // returns FALSE

Typically, logical arguments are provided to AND as logical expressions, for example:

    =AND(A1>0,A1<5)
    =AND(A1>0,B1>0)
    =AND(A1="red",B1="small")

All expressions in the formulas above will be evaluated as TRUE or FALSE. Notice that text values used in comparisons must be enclosed in double quotes (""). Be aware that AND will also evaluate numbers as TRUE or FALSE, treating [any number except zero (0) as TRUE](https://exceljet.net/videos/introduction-to-booleans)
. You can see this behavior in the formulas below:

    =AND(1,2,3) // returns TRUE
    =AND(1,2,0) // returns FALSE

Let's look at some practical ways to use the AND function.

### Example - number is between

You can use AND to check if a number in a cell is between two numbers. For example, to test if a number is between 10 and 20 we can use AND as seen in the workbook below, where the formula in cell D5 is:

    =AND(B5>10,B5<20)

![Using AND to test if a value is between two numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/and_function_number_is_between.png "Using AND to test if a value is between two numbers")

To include the numbers 10 and 20 in the allowed range of values, we can adjust the logic to use greater than or equal to (>=) or less than or equal to (<=) like this:

    =AND(B5>=10,B5<=20)

_Note: [Excel dates are serial numbers](https://exceljet.net/glossary/excel-date)
 so you can use the idea to [test if a date is between two dates](https://exceljet.net/formulas/if-date-is-between-two-dates)
._

### Example - AND with IF

The AND function is often embedded inside the [IF function](https://exceljet.net/functions/if-function)
 as the logical test to simplify what would otherwise be a more complex formula. For example, in the worksheet below, the goal is to test scores in columns B and C. If both scores are over 750, the result should be "Approve". Otherwise, the result should be "Deny". The formula in cell E5 is:

    =IF(AND(B5>750,C5>750),"Approve","Deny")
    

![The AND function with the IF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/and_function_with_if_function.png "The AND function with the IF function")

As the formula is copied down, it returns "Approve" or "Deny" for each row in the data.

### IF this AND that

The worksheet below shows a variation of the example above. This time, we want to identify and flag rows where the color is "red" and the size is "small". The formula in cell D5 is:

    =IF(AND(B5="red",C5="small"),"x","")

![AND function example - If this AND that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/and_function_if_this_and_that.png "AND function example - If this AND that")

Notice that the AND function is _not case-sensitive_. The lowercase "red" and "small" work fine even though these values are capitalized in the worksheet.

### AND with OR

You can combine the AND function with the [OR function](https://exceljet.net/functions/or-function)
 to build more advanced conditions. In the worksheet below, the goal is to identify records where the Color is Red or Green and the Quantity is over 100. The logical test inside the IF function is:

    AND(OR(B5="red",B5="green"),C5>100)

Like AND, the OR function returns TRUE or FALSE, so AND evaluates the result like any other value.

![The AND function with the OR function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/and_function_with_or_function.png "The AND function with the OR function")

The full formula in cell E5, copied down, looks like this:

    =IF(AND(OR(B5="red",B5="green"),C5>100),"x","")
    

Notice that text values _are_ enclosed in double quotes ("") but numbers _are not_.

### Example - AND with conditional formatting

The AND function is often used in the rules that trigger [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
. In the worksheet below, we use conditional formatting to highlight rows in the data where the Color is Red or Green and the Quantity is over 100. The conditional formatting is applied to the range B5:C15, and the formula to trigger the rule looks like this:

    =AND(OR($B5="red",$B5="green"),$C5>100)

![The AND function with conditional formatting](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/and_function_with_conditional_formatting.png "The AND function with conditional formatting")

Notice the IF function is not required. Because AND returns TRUE or FALSE, it is a perfect fit for conditional formatting.

### Example - AND with a range

It is possible to use AND with a range of values. In the worksheet below, the formula in cell J5 is:

    =IF(AND(C5:H5>65),"Pass","Fail")

![Using the AND function with a range of cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/and_function_with_range.png "Using the AND function with a range of cells")

_Note: this is an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 and must be entered with Control + Shift + Enter in Excel 2019 and earlier. In Excel 2021 or later, the formula will "just work" without special handling._

In the example above, the AND function is used inside the IF function as the logical test. This formula will return "Pass" only if the score for all six subjects is greater than 65. Otherwise, the result is "Fail". See also [Must pass 4 out of 6 subjects](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects)
.

> Pro-tip - as seen above, the AND function will _aggregate_ results into a _single_ result. This means it can't be used in array operations that must deliver an array of results. To work around this limitation, you can use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
> . For more information, see [Array formulas with AND and OR logic](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
> .

### Notes

*   The AND function can handle up to 255 conditions in Excel.
*   If any condition is FALSE, the AND function immediately returns FALSE.
*   The AND function is not case-sensitive.
*   The AND function does not support [wildcards](https://exceljet.net/glossary/wildcard)
    .
*   Text values or empty cells supplied as arguments are ignored.
*   The AND function will return #VALUE if no logical values are found or created during evaluation.

AND function examples
---------------------

[![Excel formula: Highlight rows with dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20rows%20with%20dates%20between.png "Excel formula: Highlight rows with dates between")](https://exceljet.net/formulas/highlight-rows-with-dates-between)

### [Highlight rows with dates between](https://exceljet.net/formulas/highlight-rows-with-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. Dates are just serial numbers in Excel, so earlier dates are always less than later dates. In the above formula, any dates that are greater than or equal to the start date AND less than or equal to the...

[![Excel formula: MAP with AND and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20with%20and%20and%20or%20logic.png "Excel formula: MAP with AND and OR logic")](https://exceljet.net/formulas/map-with-and-and-or-logic)

### [MAP with AND and OR logic](https://exceljet.net/formulas/map-with-and-and-or-logic)

In this example, the goal is to apply AND and OR logic to an array using the AND function and the OR function . The challenge is that the AND function and the OR function both aggregate values to a single result. This means you can't use them in an array operation where the goal is to return more...

[![Excel formula: Data validation require unique number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20require%20unique%20number.png "Excel formula: Data validation require unique number")](https://exceljet.net/formulas/data-validation-require-unique-number)

### [Data validation require unique number](https://exceljet.net/formulas/data-validation-require-unique-number)

Data validation rules are triggered when a user adds or changes a cell value. The AND function takes multiple arguments (logical expressions) and returns TRUE only when all arguments return TRUE. In this case, we need two conditions: Logical 1 tests if the input is a number using the ISNUMBER...

[![Excel formula: Data validation allow uppercase only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20uppercase%20only.png "Excel formula: Data validation allow uppercase only")](https://exceljet.net/formulas/data-validation-allow-uppercase-only)

### [Data validation allow uppercase only](https://exceljet.net/formulas/data-validation-allow-uppercase-only)

Data validation rules are triggered when a user adds or changes a cell value. The UPPER function changes text values to uppercase, and the EXACT function performs a case-sensitive comparison. The AND function takes multiple arguments (logical conditions) and returns TRUE only when all arguments...

[![Excel formula: Conditional message with REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20message%20with%20REPT.png "Excel formula: Conditional message with REPT function")](https://exceljet.net/formulas/conditional-message-with-rept-function)

### [Conditional message with REPT function](https://exceljet.net/formulas/conditional-message-with-rept-function)

This formula uses boolean logic to output a conditional message. If the value in column C is less than 100, the formula returns "low". If not, the formula returns an empty string (""). Boolean logic is a technique of handling TRUE and FALSE values like 1 and 0. In cell C5, the formula is evaluated...

[![Excel formula: Multiple cells have same value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all%20cells%20have%20same%20value.png "Excel formula: Multiple cells have same value")](https://exceljet.net/formulas/multiple-cells-have-same-value)

### [Multiple cells have same value](https://exceljet.net/formulas/multiple-cells-have-same-value)

This formula relies on the standard behavior of the COUNTIF function. The range is C5:C8, the criteria is provided as not equals OK: =COUNTIF(C5:C8,"<>ok") The COUNTIF then returns a count of any cells that do not contain "OK" which is compared to zero. If the count is zero, the formula...

[![Excel formula: Highlight row and column intersection exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20row%20and%20column%20intersection%20exact%20match.png "Excel formula: Highlight row and column intersection exact match")](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)

### [Highlight row and column intersection exact match](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)

Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, cell B3 in this case. To highlight matching rows, we use this logical expression: $B4=$K$5 The reference to B4 is mixed , with the column locked and row unlocked, so that...

[![Excel formula: Check register balance](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/check%20register%20balance.png "Excel formula: Check register balance")](https://exceljet.net/formulas/check-register-balance)

### [Check register balance](https://exceljet.net/formulas/check-register-balance)

The value in G5 is hard-coded. The formula picks up the value in G5, then subtracts the value (if any) in E6 and adds the value (if any) in F6. When the credit or debit values are empty, they behave like zero and have no effect on the result. When this formula is copied down column G, it will...

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: Highlight values not between X and Y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20NOT%20between.png "Excel formula: Highlight values not between X and Y")](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)

### [Highlight values not between X and Y](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

[![Excel formula: Highlight approximate match lookup conditional formatting](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20approximate%20match%20lookups.png "Excel formula: Highlight approximate match lookup conditional formatting")](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)

### [Highlight approximate match lookup conditional formatting](https://exceljet.net/formulas/highlight-approximate-match-lookup-conditional-formatting)

This formula uses 4 named ranges, defined as follows: width=K6 height=K7 widths=B6:B11 heights=C5:H5 Conditional formatting is evaluated relative to every cell it is applied to, starting with the active cell in the selection, which is cell B5 in this case. To highlight the matching row, we use this...

[![Excel formula: Data validation date in next 30 days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Data%20validation%20date%20in%20next%2030%20days.png "Excel formula: Data validation date in next 30 days")](https://exceljet.net/formulas/data-validation-date-in-next-30-days)

### [Data validation date in next 30 days](https://exceljet.net/formulas/data-validation-date-in-next-30-days)

Data validation rules are triggered when a user adds or changes a cell value. The TODAY function returns today's date (recalculated an on on-going basis). The AND function takes multiple logical expressions and returns TRUE only when all expressions return TRUE. In this case, we need to test two...

[![Excel formula: Data validation whole percentage only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20whole%20percentage%20only3.png "Excel formula: Data validation whole percentage only")](https://exceljet.net/formulas/data-validation-whole-percentage-only)

### [Data validation whole percentage only](https://exceljet.net/formulas/data-validation-whole-percentage-only)

The Excel TRUNC function does no rounding, it just returns a truncated number. It has an optional second argument (num\_digits) to specify precision. When num\_digits is not provided, it defaults to zero. In this formula for data validation, we use TRUNC to get the non-decimal part of a percentage,...

[![Excel formula: Conditional formatting column is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Conditional%20formatting%20column%20is%20blank.png "Excel formula: Conditional formatting column is blank")](https://exceljet.net/formulas/conditional-formatting-column-is-blank)

### [Conditional formatting column is blank](https://exceljet.net/formulas/conditional-formatting-column-is-blank)

When conditional formatting is applied with a formula, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the active cell when the rule is created is assumed to be cell E5, with the range E5:E14 selected. As the formula is evaluated...

[![Excel formula: Year is a leap year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/year_is_leap_year.png "Excel formula: Year is a leap year")](https://exceljet.net/formulas/year-is-a-leap-year)

### [Year is a leap year](https://exceljet.net/formulas/year-is-a-leap-year)

In this example, the goal is to write a formula that will return TRUE if a year is a leap year and FALSE if not. This is a surprisingly challenging problem in Excel for two reasons: (1) Excel thinks 1900 is a leap year due to a long-standing bug inherited from Lotus 1-2-3 and (2) The logic for...

AND function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Conditional%20formatting%20with%20two%20variable%20input-thumb.png)](https://exceljet.net/videos/conditional-formatting-with-two-variable-inputs)

### [Conditional formatting with two variable inputs](https://exceljet.net/videos/conditional-formatting-with-two-variable-inputs)

In this video, we'll look at how to extend a conditional formatting formula so that so that it checks more than just one condition. Let's take a look. Here we have the example we looked at previously. We have a single conditional formatting rule that uses a formula to highlight cells that have a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/If%20this%20OR%20that-thumb.png)](https://exceljet.net/videos/if-this-or-that)

### [If this OR that](https://exceljet.net/videos/if-this-or-that)

Sometimes, you might need to write a formula that uses the IF function to test for this OR that, or this AND that. There are two special functions, AND and OR, that make this easy to do. Let's take a look. In this first worksheet, we have a list of employees. Let's assume that you need to group...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_a_formula_with_conditional_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-a-formula-with-conditional-formatting)

### [How to use a formula with conditional formatting](https://exceljet.net/videos/how-to-use-a-formula-with-conditional-formatting)

The most powerful and flexible way to apply Conditional Formatting is with a formula. Using a formula allows you to check more conditions, and check more than one condition at the same time. Let's take a look. Here we have the table of random numbers. Let's build a conditional format that uses a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20using%20multiple%20criteria-thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)

### [How to highlight rows using multiple criteria](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)

In this video, we'll look at how to use conditional formatting to highlight entire rows using multiple criteria. Here we have an example we looked at previously. With one conditional formatting rule that uses a formula, we're able to highlight rows based on the task owner. This works well. But what...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20approximate%20match%20lookups-Thumb.png)](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

### [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)

In this video, we'll look at how to highlight approximate match lookups with conditional formatting. Here we have a simple lookup table that shows material costs for various heights and widths. The formula in K8 uses the INDEX and MATCH functions to retrieve the correct cost based on width and...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

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

*   [Date is same month and year](https://exceljet.net/formulas/date-is-same-month-and-year)
    
*   [Highlight row and column intersection exact match](https://exceljet.net/formulas/highlight-row-and-column-intersection-exact-match)
    
*   [Multiple cells are equal](https://exceljet.net/formulas/multiple-cells-are-equal)
    
*   [Value is between two numbers](https://exceljet.net/formulas/value-is-between-two-numbers)
    
*   [If cell is x or y and z](https://exceljet.net/formulas/if-cell-is-x-or-y-and-z)
    
*   [Highlight rows with dates between](https://exceljet.net/formulas/highlight-rows-with-dates-between)
    
*   [Filter on dates expiring soon](https://exceljet.net/formulas/filter-on-dates-expiring-soon)
    
*   [INDEX and MATCH all matches](https://exceljet.net/formulas/index-and-match-all-matches)
    
*   [Gantt chart by week](https://exceljet.net/formulas/gantt-chart-by-week)
    
*   [Multiple cells have same value](https://exceljet.net/formulas/multiple-cells-have-same-value)
    

### Videos

*   [How to use a formula with conditional formatting](https://exceljet.net/videos/how-to-use-a-formula-with-conditional-formatting)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    
*   [How to highlight rows using multiple criteria](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)
    
*   [Conditional formatting with two variable inputs](https://exceljet.net/videos/conditional-formatting-with-two-variable-inputs)
    
*   [How to highlight approximate match lookups](https://exceljet.net/videos/how-to-highlight-approximate-match-lookups)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [XOR Function](https://exceljet.net/functions/xor-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

### Links

*   [Microsoft AND function documentation](https://support.office.com/en-us/article/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9)
    

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