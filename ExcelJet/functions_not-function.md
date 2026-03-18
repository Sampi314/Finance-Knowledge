# Excel NOT function | Exceljet

**Source:** https://exceljet.net/functions/not-function

---

[Skip to main content](https://exceljet.net/functions/not-function#main-content)

[](https://exceljet.net/functions/not-function#)

*   [Previous](https://exceljet.net/functions/ifs-function)
    
*   [Next](https://exceljet.net/functions/or-function)
    

Excel 2003

[Logical](https://exceljet.net/functions#Logical)

NOT Function
============

by Dave Bruns · Updated 24 May 2024

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[OR](https://exceljet.net/functions/or-function)

![Excel NOT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_not_function.png "Excel NOT function")

Summary
-------

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

Purpose 
--------

Reverse arguments or results

Return value 
-------------

A reversed logical value

Syntax
------

    =NOT(logical)

*   _logical_ - A value or logical expression that can be evaluated as TRUE or FALSE.

Using the NOT function 
-----------------------

The NOT function returns the opposite of a given logical or Boolean value. Use the NOT function to reverse a Boolean value or the result of a [logical expression](https://exceljet.net/glossary/logical-test)
. When given FALSE, NOT returns TRUE. When given TRUE, NOT returns FALSE. The NOT function is commonly used with other functions like IF, AND, and OR to create complex logical tests.

### NOT function basics

The purpose of the NOT function is to reverse a Boolean value, for example:

    =NOT(TRUE) // returns FALSE
    =NOT(FALSE) // returns TRUE

NOT is often used to reverse the result from another function. For example, if cell A1 contains "purple", the formula below will return FALSE since A1 is neither "green" nor "red":

    =OR(A1="green",A1="red") // returns FALSE
    

If we want to reverse this logic, we can wrap the OR function inside the NOT function:

    =NOT(OR(A1="green",A1="red")) // returns TRUE
    

The OR function returns FALSE (as before), and the NOT function returns TRUE. 

### Example - NOT this OR that

In the worksheet below, the goal is to test each color in column B and return TRUE if the color is not "green" or "red". The formula in C5, copied down, is:

    =NOT(OR(B5="green",B5="red"))
    

![The NOT function with OR - not "red" or "green"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/not_function_not_this_or_that.png "The NOT function with OR - not "red" or "green"")

The literal translation of this formula is "NOT green or red". At each row, the formula returns TRUE if the color in column B is _not_ green or red, and FALSE if the color _is_ green or red.

### Example - IF + NOT

The NOT function is often used inside the IF function as a logical test. For example, in the worksheet below, the goal is to "flag" colors that are not "red" or "green" with an "x". The formula in cell C5 looks like this:

    =IF(NOT(OR(B5="red",B5="green")),"x","")

![The NOT function with IF - if not "red" or "green"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/not_function_if_not_this_or_that.png "The NOT function with IF - if not "red" or "green"")

As the formula is copied down, it returns an "x" if the color in column B is NOT "green" or "red". Otherwise, the formula returns an empty string ("").

### Example - Not blank

A common use case for the NOT function is to reverse the behavior of another function. For example, If cell A1 is blank (empty), the [ISBLANK function](https://exceljet.net/functions/isblank-function)
 will return TRUE:

    =ISBLANK(A1)  // TRUE if A1 is empty
    

To reverse this behavior, wrap the NOT function around the ISBLANK function:

    =NOT(ISBLANK(A1))  // TRUE if A1 is NOT empty
    

By adding NOT the output from ISBLANK is reversed. This formula will return TRUE when A1 is not empty and FALSE when A1 is empty. You might use this kind of test to only run a calculation if there is a value in A1:

    =IF(NOT(ISBLANK(A1)),B1/A1,"")
    

Translation: if A1 is not blank, divide B1 by A1, otherwise return an empty string (""). This is an example of [nesting](https://exceljet.net/glossary/nesting)
 one function inside another.

NOT function examples
---------------------

[![Excel formula: If cell is not blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_cell_is_not_blank_0.png "Excel formula: If cell is not blank")](https://exceljet.net/formulas/if-cell-is-not-blank)

### [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)

The goal is to create a formula that returns "Done" in column E when a cell in column D is not blank (i.e., contains a value). In the worksheet shown, column D records the date a task is completed. If column D contains a date (i.e. is not empty), we can assume the task is complete. This problem can...

[![Excel formula: Count cells that contain formulas](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_cells_that_contain_formulas.png "Excel formula: Count cells that contain formulas")](https://exceljet.net/formulas/count-cells-that-contain-formulas)

### [Count cells that contain formulas](https://exceljet.net/formulas/count-cells-that-contain-formulas)

In this example, the goal is to count the number of cells in a range that contain formulas. This problem can be solved with a formula based on the SUMPRODUCT and ISFORMULA functions, as explained below. Forecast values The values in the range C13:C16 are forecasts created with a formula based on...

[![Excel formula: List missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_missing_values.png "Excel formula: List missing values")](https://exceljet.net/formulas/list-missing-values)

### [List missing values](https://exceljet.net/formulas/list-missing-values)

In this example, the goal is to generate a list of people who were invited but did not attend an unspecified event. More specifically, we need to compare the names in B5:B16 against the names in D5:D12 and return the missing names. For convenience, list1 (B5:B16) and list2 (D5:D12) are named ranges...

[![Excel formula: If NOT this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If_not_this_or_that.png "Excel formula: If NOT this or that")](https://exceljet.net/formulas/if-not-this-or-that)

### [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)

The goal is to "flag" records that are neither "Red" nor "Green". More specifically, we want to check the color in column B, and leave an "x" in rows where the color is NOT "Red" OR "Green". If the color is "Red" OR "Green", we want to display nothing. IF function logic The IF function is commonly...

[![Excel formula: Highlight values not between X and Y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20NOT%20between.png "Excel formula: Highlight values not between X and Y")](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)

### [Highlight values not between X and Y](https://exceljet.net/formulas/highlight-values-not-between-x-and-y)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

[![Excel formula: Count cells that do not contain errors](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain%20errors.png "Excel formula: Count cells that do not contain errors")](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)

### [Count cells that do not contain errors](https://exceljet.net/formulas/count-cells-that-do-not-contain-errors)

In this example, the goal is to count the number of cells in a range that do not contain errors. The best way to solve this problem is to use the SUMPRODUCT function together with the ISERROR function. You can also use the COUNTIF function or COUNTIFS function to exclude specific errors. Both...

[![Excel formula: Count cells that do not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain.png "Excel formula: Count cells that do not contain")](https://exceljet.net/formulas/count-cells-that-do-not-contain)

### [Count cells that do not contain](https://exceljet.net/formulas/count-cells-that-do-not-contain)

In this example, the goal is to count cells that do not contain a specific substring. This problem can be solved with the COUNTIF function or the SUMPRODUCT function . Both approaches are explained below. Although COUNTIF is not case-sensitive, the SUMPRODUCT version of the formula can be adapted...

[![Excel formula: FILTER with complex multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20with%20complex%20multiple%20criteria.png "Excel formula: FILTER with complex multiple criteria")](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

### [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)

In this example, we need to construct logic that filters data to include: account begins with "x" AND region is "east", and month is NOT April. The filtering logic of this formula (the include argument) is created by chaining together three expressions that use boolean logic on arrays in the data...

[![Excel formula: Sum formulas only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20formulas%20only.png "Excel formula: Sum formulas only")](https://exceljet.net/formulas/sum-formulas-only)

### [Sum formulas only](https://exceljet.net/formulas/sum-formulas-only)

In this example, the goal is to calculate a sum of the values in a range that are generated with a formula. In other words, we want to sum values in a range while ignoring the values that have been entered manually. In the context of this example, the hardcoded values in C5:C12 represent actual...

[![Excel formula: Count cells that contain text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20text.png "Excel formula: Count cells that contain text")](https://exceljet.net/formulas/count-cells-that-contain-text)

### [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)

In this example, the goal is to count cells in a range that contain text values. This could be hard-coded text like "apple" or "red", numbers entered as text, or formulas that return text values. Empty cells and cells that contain numeric values or errors should not be included in the count. This...

[![Excel formula: If not blank multiple cells](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_not_blank_multiple_cells.png "Excel formula: If not blank multiple cells")](https://exceljet.net/formulas/if-not-blank-multiple-cells)

### [If not blank multiple cells](https://exceljet.net/formulas/if-not-blank-multiple-cells)

The goal is to return the first non-blank value in each row from columns B:E, moving left to right. One way to solve this problem is with a series of nested IF statements. Since all cells are contiguous (connected) another way to get the first value is with the XLOOKUP function. Both approaches are...

[![Excel formula: All values in a range are at least](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/All%20values%20in%20a%20range%20are%20at%20least.png "Excel formula: All values in a range are at least")](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)

### [All values in a range are at least](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)

At the core, this formula uses the COUNTIF function to count any cells that fall below a given value, which is hardcoded as 65 in the formula: COUNTIF(B5:F5,"<65") In this part of the formula, COUNTIF will return a positive number if any cell in the range is less than 65, and zero if not. In the...

[![Excel formula: Celsius to Fahrenheit conversion](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/celsius%20to%20fahrenheit%20conversion.png "Excel formula: Celsius to Fahrenheit conversion")](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

### [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)

In this example, the goal is to convert the Celsius temperatures shown in column B to Fahrenheit temperatures in column C. The solution shown in the worksheet above relies on the CONVERT function, which can convert a number in one measurement system to another. CONVERT is fully automatic and based...

[![Excel formula: Conditional formatting column is blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Conditional%20formatting%20column%20is%20blank.png "Excel formula: Conditional formatting column is blank")](https://exceljet.net/formulas/conditional-formatting-column-is-blank)

### [Conditional formatting column is blank](https://exceljet.net/formulas/conditional-formatting-column-is-blank)

When conditional formatting is applied with a formula, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the active cell when the rule is created is assumed to be cell E5, with the range E5:E14 selected. As the formula is evaluated...

[![Excel formula: Get first non-blank value in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_non-blank_value_in_a_list.png "Excel formula: Get first non-blank value in a list")](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

### [Get first non-blank value in a list](https://exceljet.net/formulas/get-first-non-blank-value-in-a-list)

The gist of this problem is that we want to get the first non-blank cell, but we don't have a direct way to do that in Excel. The easiest way to solve this problem is with the XLOOKUP function. XLOOKUP function The XLOOKUP function is a modern upgrade to the VLOOKUP function. XLOOKUP is very...

NOT function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20highlight%20rows%20using%20multiple%20criteria-thumb.png)](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)

### [How to highlight rows using multiple criteria](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)

In this video, we'll look at how to use conditional formatting to highlight entire rows using multiple criteria. Here we have an example we looked at previously. With one conditional formatting rule that uses a formula, we're able to highlight rows based on the task owner. This works well. But what...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells that do not contain](https://exceljet.net/formulas/count-cells-that-do-not-contain)
    
*   [FILTER with complex multiple criteria](https://exceljet.net/formulas/filter-with-complex-multiple-criteria)
    
*   [All values in a range are at least](https://exceljet.net/formulas/all-values-in-a-range-are-at-least)
    
*   [If cell is not blank](https://exceljet.net/formulas/if-cell-is-not-blank)
    
*   [Celsius to Fahrenheit conversion](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)
    
*   [Conditional formatting column is blank](https://exceljet.net/formulas/conditional-formatting-column-is-blank)
    
*   [Count cells that contain formulas](https://exceljet.net/formulas/count-cells-that-contain-formulas)
    
*   [Count cells that contain text](https://exceljet.net/formulas/count-cells-that-contain-text)
    
*   [XLOOKUP with complex multiple criteria](https://exceljet.net/formulas/xlookup-with-complex-multiple-criteria)
    
*   [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)
    

### Videos

*   [How to highlight rows using multiple criteria](https://exceljet.net/videos/how-to-highlight-rows-using-multiple-criteria)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    

### Links

*   [Microsoft NOT function documentation](https://support.office.com/en-us/article/not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77)
    

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