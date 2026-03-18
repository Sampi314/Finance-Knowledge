# Excel IF function | Exceljet

**Source:** https://exceljet.net/functions/if-function

---

[Skip to main content](https://exceljet.net/functions/if-function#main-content)

[](https://exceljet.net/functions/if-function#)

*   [Previous](https://exceljet.net/functions/false-function)
    
*   [Next](https://exceljet.net/functions/iferror-function)
    

Excel 2003

[Logical](https://exceljet.net/functions#Logical)

IF Function
===========

by Dave Bruns · Updated 9 Jun 2025

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[OR](https://exceljet.net/functions/or-function)

[NOT](https://exceljet.net/functions/not-function)

[IFS](https://exceljet.net/functions/ifs-function)

[SWITCH](https://exceljet.net/functions/switch-function)

![Excel IF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_If_function.png "Excel IF function")

Summary
-------

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF function can be combined with AND, OR, and NOT to create more advanced logical tests.

Purpose 
--------

Test for a specific condition

Return value 
-------------

The values you supply for TRUE or FALSE

Syntax
------

    =IF(logical_test,[value_if_true],[value_if_false])

*   _logical\_test_ - A value or logical expression that can be evaluated as TRUE or FALSE.
*   _value\_if\_true_ - \[optional\] The value to return when logical\_test evaluates to TRUE.
*   _value\_if\_false_ - \[optional\] The value to return when logical\_test evaluates to FALSE.

Using the IF function 
----------------------

The IF function is one of the most widely used functions in Excel. At the core, IF runs a test and returns one value when the result is TRUE, and another value when the result is FALSE. At first glance, this seems very basic — if this is true, do this; otherwise, do that. However, formulas that use IF can quickly become advanced as the requirements become more complex and more IFs are nested together. One of the tricks in using IF effectively is knowing how to combine IF with other functions like [AND](https://exceljet.net/functions/and-function)
 and [OR](https://exceljet.net/functions/or-function)
 to handle more complex logic gracefully. This article explains the basics carefully, then introduces more advanced formulas that use the IF function.

### Key features

*   Performs logical tests that return TRUE or FALSE
*   Returns different results based on whether the test is TRUE or FALSE
*   Works with all comparison operators (=, <>, >, <, >=, <=)
*   Both _value\_if\_true_ and _value\_if\_false_ are optional, but at least one must be provided
*   Can be combined with AND, OR, and NOT for complex logical tests
*   Supports nested IF statements for multiple conditions ("else if" logic)
*   Not case sensitive and does not support wildcards directly
*   Can be combined with SEARCH and ISNUMBER for simple pattern matching
*   Can be combined with REGEXTEST for advanced pattern matching
*   Can return empty strings ("") to make cells appear blank
*   Works in all versions of Excel

> The IF function can be deceptively simple. Many Excel users have gotten into the weeds debugging a complicated nested IF formula that doesn't even make sense for the problem at hand. If an IF formula seems too long and complicated, there is almost certainly a better way to do it in Excel. To avoid this fate, it pays to understand the basics well and know when to seek other solutions.

### Contents

*   [Basic IF function example](https://exceljet.net/functions/if-function#basic-example)
    
*   [Logical tests](https://exceljet.net/functions/if-function#logical-tests)
    
*   [Example - Pass or Fail](https://exceljet.net/functions/if-function#example-pass-or-fail)
    
*   [Example - IF this OR that](https://exceljet.net/functions/if-function#example-if-this-or-that)
    
*   [Example - IF this AND that](https://exceljet.net/functions/if-function#example-if-this-and-that)
    
*   [Example - IF this AND OR that](https://exceljet.net/functions/if-function#example-if-this-and-or-that)
    
*   [Example - Nested IF](https://exceljet.net/functions/if-function#example-nested-if)
    
*   [Example - Return another formula with IF](https://exceljet.net/functions/if-function#example-return-another-formula-with-if)
    
*   [Example - IF contains specific text](https://exceljet.net/functions/if-function#example-if-contains-specific-text)
    
*   [Example - IF with wildcards and regex](https://exceljet.net/functions/if-function#example-if-with-wildcards)
    
*   [When not to use IF](https://exceljet.net/functions/if-function#when-not-to-use-IF)
    

### Basic IF function example

To understand how the IF function works, let's start with a very basic example. In the worksheet below, the goal is to use the IF function to mark scores greater than 80 with an IF formula. The simplest IF we can write for this looks like this:

    =IF(B5>80,TRUE)

Translation: _If B5 is greater than 80, return TRUE_. You can see the result in the worksheet below.

![Basic example - simple formula to return TRUE or FALSE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_basic_example_1.png "Basic example - simple formula to return TRUE or FALSE")

Note we are not using quotes ("") anywhere in the formula because the formula contains no text. Also, we do not need to provide a value for value\_if\_false because IF will return FALSE by default. This formula works fine. But the output is rather busy and hard to read. Let's change the formula to return an "x" when the score is over 80:

    =IF(B5>80,"x")

Notice that the "x" appears in double quotes because it is a text value. Text values hardcoded into formulas must always be quoted. You can see the result below:

![Basic example - modified to return "x" for scores over 80](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_basic_example_2.png "Basic example - modified to return "x" for scores over 80")

Note that TRUE values have been replaced by "x", and the FALSE results remain FALSE since we have not provided a value for _value\_if\_false_. Finally, let's modify the formula to display nothing when a score is not over 80. We can do this by providing an empty string ("") for value\_if\_false like this:

    =IF(B5>80,"x","")

After updating the formulas in column E, the output is much easier to read. We now see an "x" for scores over 80. For scores that are not over 80, the cells appear to be empty:

![Basic example - final IF formula to mark scores over 80](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_basic_example_3.png "Basic example - final IF formula to mark scores over 80")

_Remember: text values like "x" must be enclosed in double-quotes. Numbers like 80 are not quoted._

### Logical tests

Before we move on, let's talk more about how logical tests work in the IF function. Usually, the _logical\_test_ in IF is an expression that will return TRUE or FALSE. The table below shows some common examples:

| Goal | Logical test |
| --- | --- |
| If A1 is greater than 75 | A1>75 |
| If A1 equals 100 | A1=100 |
| If A1 is less than or equal to 100 | A1<=100 |
| If A1 equals "Red" | A1="red" |
| If A1 is not equal to "Red" | A1<>"red" |
| If A1 is less than B1 | A1<B1 |
| If A1 is empty | A1="" |
| If A1 is not empty | A1<>"" |
| If A1 is less than the current date | A1<TODAY() |

Notice that text values that appear in a logical test must be enclosed in quotes (""). However, numbers and logical [operators](https://exceljet.net/glossary/logical-operators)
 like >,<,<>,=, etc., are _not quoted_. 

> Note: The IF function is _not_ case-sensitive. The text "red" will match "red", "Red", "RED", or "rEd".

### Example - Pass or Fail

In the worksheet below, we want to assign either a "Pass" or "Fail" based on a test score. A passing score is 70 or higher. The formula in E5, copied down, is:

    =IF(C5<70,"Fail","Pass")
    

![IF function example - Pass or Fail](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_pass_or_fail_example.png "IF function example - Pass or Fail")

Notice both "Pass" and "Fail" are in double quotes ("") because they are text values. Also, note that the logical flow of this formula can be reversed. Above, we test for failing scores. To test for passing scores, we can write a formula like this:

    =IF(C5>=70,"Pass","Fail")
    

Translation: _If the value in C5 is greater than or equal to 70, return "Pass". Otherwise, return "Fail"._ Both formulas will return the same result. Which option you choose is a personal preference.

### Example - IF this OR that

A common challenge with the IF function is how to handle a problem that requires "if this or that" logic. The logical test for IF takes just one value, so how do you test for more than one result? The trick is to combine the IF function with the OR function. For example, the goal in the worksheet below is to mark rows where the color is "Red" OR "Green". We can write a formula that does this by combining the IF function with the [OR function](https://exceljet.net/functions/or-function)
 like this:

    =IF(OR(B5="red",B5="green"),"x","")

Translation: _If the value in B5 is "red" or "green", return "x". Otherwise, return an empty string ("")_.

Notice that the OR function is embedded inside the IF function as the logical test. The OR function accepts multiple logical expressions. If _any_ expression returns TRUE, the OR function will return TRUE. Only if all logical expressions return FALSE will the OR function return FALSE.  You can see the result below:

![IF function example - IF this OR that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_if_this_OR_that_example.png "IF function example - IF this OR that")

> Video: [IF this OR that](https://exceljet.net/videos/if-this-or-that)

### Example - IF this AND that

Like the OR function, the [AND function](https://exceljet.net/functions/and-function)
 can be combined with the IF function to create "if this AND that logic". In the worksheet below, the goal is to mark people in group B with a score of at least 80. The formula in cell F5, copied down, is:

    =IF(AND(C5="B",D5>=80),"x","")

![IF function example - IF this AND that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_if_this_AND_that_example.png "IF function example - IF this AND that")

Notice the AND function is nested in the IF function as the logical test and contains two logical expressions: C5="B", and D5>=80. The "B" appears in quotes ("") because it is a text string. The 80 is not quoted because it is a number.

### Example - IF this AND OR that

You can combine the AND and OR functions inside IF to implement more advanced logic. In the example below, the goal is to mark people in groups A or B with a score of at least 80. The formula in cell F5, copied down, is:

    =IF(AND(OR(C5="A",C5="B"),D5>=80),"x","")

![IF function example - IF this AND OR that](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_if_this_AND_OR_that_example.png "IF function example - IF this AND OR that")

### Example - Nested IF

The IF function can be "[nested](https://exceljet.net/glossary/nesting)
". A "nested IF" refers to a formula where one IF function is nested inside another to test for more conditions and return more possible results. Each IF statement needs to be carefully "nested" inside another so that the logic is correct. The idea here is that we are chaining together multiple IF functions to create "else if" logic. In the example below, the goal is to assign a number to each color. If the color is Red, the result should be 100. If the color is Blue, the result should be 125. If the color is Green, the result should be 150. In the worksheet below, the formula in D5 is a "nested IF" like this:

    =IF(B5="red",100,IF(B5="blue",125,IF(B5="green",150)))
    

![IF function example - Nested IF formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_nested_IF_example.png "IF function example - Nested IF formula")

Translation: _If the color is Red, 100, else if the color is Blue, 125, else if the color is Green, 150_.

Video: [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)

Note that this formula will only handle three colors: Red, Blue, and Green". With any other color, the formula will return FALSE. As you might expect, you can add more IF functions to handle more values. [See this page](https://exceljet.net/formulas/nested-if-function-example)
 for a more advanced nested IF to assign grades. However, before you go down that road, be aware that Excel has other options to handle multiple tests. For example, the [IFS function](https://exceljet.net/functions/ifs-function)
 can handle multiple logical tests without nesting with a formula like this:

    =IFS(B5="red",100,B5="blue",125,B5="green",150)

You can also use the [SWITCH function](https://exceljet.net/functions/switch-function)
 with an even simpler formula like this:

    =SWITCH(B5,"red",100,"blue",125,"green",150)

Both formulas above will return the same result as the original nested IF formula.

_Note: For more complex scenarios with many values to test, consider other functions, like_ [_VLOOKUP_](https://exceljet.net/functions/vlookup-function)
 _or_ [_XLOOKUP_](https://exceljet.net/functions/xlookup-function)
_, because they can handle more conditions in a_ [_more streamlined fashion_](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
_._ 

### Example - Return another formula with IF

As seen above, the IF function can easily return another value when the result of a test is TRUE or FALSE. In addition, the IF function can also return a formula. For example, in the worksheet below, the goal is to increase the price of Red items only by 20%. The price of other colors should remain unchanged. The formula in cell F5 is:

    =IF(B5="red",D5*1.2,D5)
    

As the formula is copied down, it tests the color in column B. If the color is Red, it returns D5\*1.2, effectively increasing the price by 20%. If the color is _not_ Red, it simply returns D5. You can see the result below:

![IF function example - Return another formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_return_another_formula_example.png "IF function example - Return another formula")

Notice the results in column F. Most prices are the same, but prices for the color Red are now 20% higher. Although this is a simple formula, IF can return any normal Excel formula for both TRUE and FALSE results.

### Example - IF contains specific text

Because the IF function does not support wildcards directly, it is not obvious how to configure IF to check for a specific _substring_ in a cell. A common approach is to combine the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 and the [SEARCH function](https://exceljet.net/functions/search-function)
 to create a logical test like this:

    =ISNUMBER(SEARCH(substring,A1)) // returns TRUE or FALSE

For example, to check for the substring "xyz" in cell A1, you can use a formula like this:

    =IF(ISNUMBER(SEARCH("xyz",A1)),"Yes","No")

In the worksheet below, we want to test each sentence in column B for the word "apple". The formula in cell D5, copied down, is:

    =IF(ISNUMBER(SEARCH("apple",B5)),"x","")

![IF function example - If cell contains specific text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_if_cell_contains_specific_text_example.png "IF function example - If cell contains specific text")

> Because the SEARCH function supports basic Excel wildcards, you can include these in your IF formula. [Read a more detailed explanation here](https://exceljet.net/formulas/cell-contains-specific-text)
> .

### IF with wildcards and regex

The IF function does not support [wildcards](https://exceljet.net/glossary/wildcard)
 directly. However, you can combine IF with other Excel functions to overcome this limitation. For basic wildcard support, you can [combine IF with COUNTIF](https://exceljet.net/formulas/if-with-wildcards)
 or [combine IF with SEARCH](https://exceljet.net/formulas/cell-contains-specific-text)
 (as seen above). If you need more than basic wildcards, you can use the full power of Regular Expressions by combining IF with the [REGEXTEST function](https://exceljet.net/functions/regextest-function)
. REGEXTEST tests for a regex pattern and returns TRUE or FALSE, making it a perfect fit for the IF function. For example, in the worksheet below, the goal is to test the input in column B for four US states based on their two-letter abbreviations: MN, MT, ND, and SD. This can be done with the pattern ""\\b(MN|MT|ND|SD)\\b". The formula in D5, copied down, is:

    =IF(REGEXTEST(B5,"\b(MN|MT|ND|SD)\b"),"x","")

![IF function example - IF with regular expressions (regex)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/IF_function_regex_example.png "IF function example - IF with regular expressions (regex)")

> For more information on regex in Excel, see: [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
> .

### When not to use IF (related functions)

IF is a widely used function in Excel, and you'll find it in all kinds of worksheets in almost any industry. However, just because IF is common doesn't mean you should always use it. Excel has _many_ functions that can apply conditional logic. Here are some good options, depending on your specific use case:

*   [IFS function](https://exceljet.net/functions/ifs-function)
     - Handles multiple conditions without nesting
*   [SWITCH function](https://exceljet.net/functions/switch-function)
     - Match a single value against multiple options
*   [CHOOSE function](https://exceljet.net/functions/choose-function)
     - Return values based on position/index numbers
*   [XLOOKUP](https://exceljet.net/functions/xlookup-function)
     / [VLOOKUP](https://exceljet.net/functions/vlookup-function)
     - Better than nested IFs for matching values in tables
*   [COUNTIFS](https://exceljet.net/functions/countifs-function)
     / [SUMIFS](https://exceljet.net/functions/sumifs-function)
     - Apply conditional logic for counting/summing without IF
*   [FILTER function](https://exceljet.net/functions/filter-function)
     - Extract matching records based on matching criteria

Before you try to make IF do something it's not well suited for, make sure you have an idea of what Excel offers out of the box. See [101 Functions You Should Know](https://exceljet.net/articles/101-excel-functions)
, [Dynamic Array Formulas in Excel,](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 and [New Excel Functions](https://exceljet.net/new-excel-functions)
 for more information.

### Notes

*   The IF function is _not_ case-sensitive.
*   Inside IF, text values should be enclosed in double quotes ("").
*   Numbers and logical values like TRUE and FALSE should not be quoted.
*   IF does not support wildcards, but can be combined with other functions that do.
*   To extract records that meet specific criteria, see the [FILTER function](https://exceljet.net/functions/filter-function)
    .
*   To count values that meet specific criteria, use the [COUNTIF](https://exceljet.net/functions/countif-function)
     or the [COUNTIFS](https://exceljet.net/functions/countifs-function)
     functions.
*   To sum values that meet specific criteria, use the [SUMIF](https://exceljet.net/functions/sumif-function)
     or the [SUMIFS](https://exceljet.net/functions/sumifs-function)
     functions.

IF function examples
--------------------

[![Excel formula: If NOT this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If_not_this_or_that.png "Excel formula: If NOT this or that")](https://exceljet.net/formulas/if-not-this-or-that)

### [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)

The goal is to "flag" records that are neither "Red" nor "Green". More specifically, we want to check the color in column B, and leave an "x" in rows where the color is NOT "Red" OR "Green". If the color is "Red" OR "Green", we want to display nothing. IF function logic The IF function is commonly...

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

[![Excel formula: Assign points based on late time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/assign%20penalty%20points%20based%20on%20late%20time2.png "Excel formula: Assign points based on late time")](https://exceljet.net/formulas/assign-points-based-on-late-time)

### [Assign points based on late time](https://exceljet.net/formulas/assign-points-based-on-late-time)

This formula is a classic example of a nested IF formula that tests threshold values in ascending order. To match the schedule shown in G5:G11, the formula first checks the late by time in D5 to see if it's less than 5 minutes. If so, zero points are assigned: IF(D5<VALUE("0:05"),0, If the...

[![Excel formula: Get location of value in 2D array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_location_of_value_in_2D_array.png "Excel formula: Get location of value in 2D array")](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

### [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)

In this example, the goal is to return a list of the locations for a specific value in a 2D array of values (i.e., a table). The target value is entered in cell N5, and the table being tested is in the range C4:L16. The coordinates are supplied from row 4 and column B, as seen in the worksheet. In...

[![Excel formula: Maximum value if](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/maximum_value_if.png "Excel formula: Maximum value if")](https://exceljet.net/formulas/maximum-value-if)

### [Maximum value if](https://exceljet.net/formulas/maximum-value-if)

In this example, the goal is to get the maximum value for each group in the data as shown. The easiest way to solve this problem is with the MAXIFS function. However, there are actually several options. If you need more flexibility (i.e. you need to work with arrays and not ranges), you can use the...

[![Excel formula: If date is between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_date_is_between_two_dates.png "Excel formula: If date is between two dates")](https://exceljet.net/formulas/if-date-is-between-two-dates)

### [If date is between two dates](https://exceljet.net/formulas/if-date-is-between-two-dates)

The goal is to identify dates in column B that fall between a given start date and end date. The start and end dates are exposed as inputs on the worksheet that can be changed at any time, labeled "Start" and "End" in the example shown. Named ranges For convenience, both start (E5) and end (E8) are...

[![Excel formula: Minimum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/minimum_if_multiple_criteria.png "Excel formula: Minimum if multiple criteria")](https://exceljet.net/formulas/minimum-if-multiple-criteria)

### [Minimum if multiple criteria](https://exceljet.net/formulas/minimum-if-multiple-criteria)

In this example, the goal is to get the minimum value for a given group above a specific temperature. In other words, we want the min value after applying multiple criteria. The easiest way to solve this problem is with the MINIFS function. However, if you need more flexibility (for example, you...

[![Excel formula: IF with wildcards](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/IF_with_wildcards.png "Excel formula: IF with wildcards")](https://exceljet.net/formulas/if-with-wildcards)

### [IF with wildcards](https://exceljet.net/formulas/if-with-wildcards)

The goal of this formula is to verify whether the values in column B follow the format xx-xxxx-xxx, where "x" represents any single character. The IF function doesn't support wildcards directly, so we can't use IF by itself. Instead, we can combine the IF function with the COUNTIF function, which...

[![Excel formula: Create date range from two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20date%20range%20from%20two%20dates.png "Excel formula: Create date range from two dates")](https://exceljet.net/formulas/create-date-range-from-two-dates)

### [Create date range from two dates](https://exceljet.net/formulas/create-date-range-from-two-dates)

The TEXT function takes numeric values and converts them to text values using the format you specify. In this example, we are using the format "mmm d" for both TEXT functions in E5. The results are joined with a hyphen using simple concatenation. Note: the other examples in column E all use...

[![Excel formula: Get nth match with INDEX / MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_nth_match_with_INDEX_and_MATCH.png "Excel formula: Get nth match with INDEX / MATCH")](https://exceljet.net/formulas/get-nth-match-with-index-match)

### [Get nth match with INDEX / MATCH](https://exceljet.net/formulas/get-nth-match-with-index-match)

The goal is to retrieve the nth matching record in a table when targeting a specific product. For example, if the value in cell H4 is "A", the formula in H7 should return the name "John", since this is the first name in the table associated with product "A". In the same way, the formula in H8...

[![Excel formula: Transpose table without zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/transpose%20table%20without%20zeros.png "Excel formula: Transpose table without zeros")](https://exceljet.net/formulas/transpose-table-without-zeros)

### [Transpose table without zeros](https://exceljet.net/formulas/transpose-table-without-zeros)

The TRANSPOSE function automatically transposes values in a horizontal orientation to vertical orientation and vice versa. However, if a source cell is blank (empty) TRANSPOSE will output a zero. To fix that problem, this formula contains an IF function that checks first to see if a cell is blank...

[![Excel formula: Find missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_missing_values.png "Excel formula: Find missing values")](https://exceljet.net/formulas/find-missing-values)

### [Find missing values](https://exceljet.net/formulas/find-missing-values)

The goal is to identify invoice numbers in range D5:D11 that are missing in range B5:B16 (named list ). Two good ways to solve this problem in Excel are the COUNTIF function and the MATCH function . Both approaches are explained below. COUNTIF function COUNTIF counts cells in a range that meet a...

[![Excel formula: Time since start in day ranges](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/time%20since%20start%20in%20day%20ranges.png "Excel formula: Time since start in day ranges")](https://exceljet.net/formulas/time-since-start-in-day-ranges)

### [Time since start in day ranges](https://exceljet.net/formulas/time-since-start-in-day-ranges)

In this example, the goal is to calculate durations in "days" starting from the start date and time in cell G5 and ending at the dates and times shown in column B. The twist is that we want to classify the durations using the custom labels shown in column E, starting with "Day 0" for the first 24...

[![Excel formula: Two-way approximate match multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20approximate%20match%20multiple%20criteria%20v2.png "Excel formula: Two-way approximate match multiple criteria")](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)

### [Two-way approximate match multiple criteria](https://exceljet.net/formulas/two-way-approximate-match-multiple-criteria)

The goal is to lookup a feed rate based on material, hardness, and drill bit diameter. Feed rate values are in the named range data (D6:H16). This can be done with a two-way INDEX and MATCH formula. One MATCH function works out the row number (material and hardness), and the other MATCH function...

[![Excel formula: All dates in chronological order](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/all%20dates%20are%20in%20order.png "Excel formula: All dates in chronological order")](https://exceljet.net/formulas/all-dates-in-chronological-order)

### [All dates in chronological order](https://exceljet.net/formulas/all-dates-in-chronological-order)

This is a good example of how the SUMPRODUCT function can help in situations where the COUNTIF or COUNTIFS functions do not work. In this case, the goal is to check all dates in a given range and show a check mark (✓) only when dates are in chronological order. The logic itself is quite simple, but...

IF function videos
------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20group%20values%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-group-values-with-vlookup)

### [How to group values with VLOOKUP](https://exceljet.net/videos/how-to-group-values-with-vlookup)

In this video we'll look at how to use VLOOKUP to group data into specific categories. Let's take a look. Sometimes you need to group values into discreet categories that don't exist in your data. For example, in this case, we have a list of employees and each employee is in one department. What if...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20CHOOSE%20function-Thumb.png)](https://exceljet.net/videos/how-to-use-the-choose-function)

### [How to use the CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)

In this video we'll look at how you can use the CHOOSE function . Let's look at three examples. In this first example we have some items listed with a numeric color code. We want to bring these names into column D. Now, since I already have a table here, I could just use VLOOKUP and reference the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/3%20Basic%20Array%20Formulas-Play.png)](https://exceljet.net/videos/3-basic-array-formulas)

### [3 basic array formulas](https://exceljet.net/videos/3-basic-array-formulas)

In this video we'll look at three basic array formula examples. The latest version of Excel ships with new functions like UNIQUE , SORT, FILTER and so on that make certain array formulas easy. But you can still build traditional array formulas as well, and they can solve some tricky problems. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20join%20values%20with%20the%20ampersand-thumb_0.png)](https://exceljet.net/videos/how-to-join-values-with-the-ampersand)

### [How to join values with the ampersand](https://exceljet.net/videos/how-to-join-values-with-the-ampersand)

Often, you'll need to join together values in Excel. A good example is when you have first, last, and middle names in separate columns and you want to join these together into one name. This is referred to as "concatenation." In this example, we have first, middle, and last names shown separately...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20make%20a%20nested%20IF%20formula%20easier%20to%20read.png)](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

### [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

In this video we're going to look at how to make a nested IF formula more readable by adding line breaks. Here I have a worksheet that calculates sales commissions based on the commission structure shown in the table. For example, we can see that King sold $124,500 and gets a commission of 5%,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20dynamic%20chart_thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)

### [How to build a simple dynamic chart](https://exceljet.net/videos/how-to-build-a-simple-dynamic-chart)

In this video, we'll look at how to build a simple dynamic chart in Excel. First, let's look at the problem we're trying to solve. Here we have monthly sales data. At the moment, we only have 5 months, but we'll be adding more data over time. Now, if I insert a column chart, everything works fine...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20check%20and%20debug%20a%20formula%20with%20F9.png)](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

### [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

One thing you'll frequently do in Excel is check or debug formulas. In this video, we'll look at how to use the F9 key to quickly break a formula down into pieces that you can understand. Here we have a simple list of names. In addition to names, we have a column for birthdate, a column for age,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20search%20box%20with%20conditional%20formatting.png)](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

### [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)

In this video, we'll look at a way to create a search box that highlights rows in a table, by using conditional formatting, and a formula that checks several columns at once. This is a great alternative to filtering, because you can see the information you're looking for highlighted in context. Let...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Complex%20formula%20example%20401k%20Match-thumb.png)](https://exceljet.net/videos/complex-formula-example-401k-match)

### [Complex formula example 401k Match](https://exceljet.net/videos/complex-formula-example-401k-match)

In this video we'll look at how to build a formula that calculates a 401k match using several nested IF statements . In the US, many companies match an employee's retirement deferral up to a certain percent. In this example, the match has two tiers: In Tier 1, the company matches 100% up to 4% of...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel OR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_or_function.png "Excel OR function")](https://exceljet.net/functions/or-function)

### [OR Function](https://exceljet.net/functions/or-function)

The Excel OR function is a logical function used to test multiple conditions at the same time. OR returns TRUE _if any condition is TRUE_. If all conditions are FALSE, the OR function returns FALSE. The OR function is often used with the IF function and can be combined...

[![Excel NOT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_not_function.png "Excel NOT function")](https://exceljet.net/functions/not-function)

### [NOT Function](https://exceljet.net/functions/not-function)

The Excel NOT function returns the opposite of a given logical or Boolean value. When given TRUE, NOT returns FALSE. When given FALSE, NOT returns TRUE. Use the NOT function to reverse a logical value.

[![Excel IFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ifs.png "Excel IFS function")](https://exceljet.net/functions/ifs-function)

### [IFS Function](https://exceljet.net/functions/ifs-function)

The Excel IFS function can run multiple tests and return a value corresponding to the first TRUE result. Use the IFS function to evaluate multiple conditions without multiple nested IF statements. IFS allows shorter, easier to read formulas....

[![Excel SWITCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20switch.png "Excel SWITCH function")](https://exceljet.net/functions/switch-function)

### [SWITCH Function](https://exceljet.net/functions/switch-function)

The Excel SWITCH function compares one value against a list of values, and returns a result corresponding to the first match found. When no match is found, SWITCH can return an optional default value....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)
    
*   [Date is same month and year](https://exceljet.net/formulas/date-is-same-month-and-year)
    
*   [Value is within tolerance](https://exceljet.net/formulas/value-is-within-tolerance)
    
*   [Mark rows with logical tests](https://exceljet.net/formulas/mark-rows-with-logical-tests)
    
*   [Rank values by month](https://exceljet.net/formulas/rank-values-by-month)
    
*   [Cap percentage between 0 and 100](https://exceljet.net/formulas/cap-percentage-between-0-and-100)
    
*   [Get next scheduled event](https://exceljet.net/formulas/get-next-scheduled-event)
    
*   [Make words plural](https://exceljet.net/formulas/make-words-plural)
    
*   [Get location of value in 2D array](https://exceljet.net/formulas/get-location-of-value-in-2d-array)
    
*   [Student class enrollment with table](https://exceljet.net/formulas/student-class-enrollment-with-table)
    

### Videos

*   [How to build a search box with conditional formatting](https://exceljet.net/videos/how-to-build-a-search-box-with-conditional-formatting)
    
*   [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
    
*   [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)
    
*   [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
    
*   [How to trap errors in formulas](https://exceljet.net/videos/how-to-trap-errors-in-formulas)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
*   [How to group values with VLOOKUP](https://exceljet.net/videos/how-to-group-values-with-vlookup)
    
*   [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [OR Function](https://exceljet.net/functions/or-function)
    
*   [NOT Function](https://exceljet.net/functions/not-function)
    
*   [IFS Function](https://exceljet.net/functions/ifs-function)
    
*   [SWITCH Function](https://exceljet.net/functions/switch-function)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    
*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

### Links

*   [Microsoft IF function documentation](https://support.office.com/en-us/article/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)
    

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