# Excel COUNTIFS function | Exceljet

**Source:** https://exceljet.net/functions/countifs-function

---

[Skip to main content](https://exceljet.net/functions/countifs-function#main-content)

[](https://exceljet.net/functions/countifs-function#)

*   [Previous](https://exceljet.net/functions/countif-function)
    
*   [Next](https://exceljet.net/functions/covar-function)
    

Excel 2007

[Statistical](https://exceljet.net/functions#Statistical)

COUNTIFS Function
=================

by Dave Bruns · Updated 8 Jun 2025

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[COUNT](https://exceljet.net/functions/count-function)

[COUNTA](https://exceljet.net/functions/counta-function)

![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")

Summary
-------

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells that contain dates, numbers, and text. Criteria can include [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?).

Purpose 
--------

Count cells that match multiple criteria

Return value 
-------------

The number of times criteria are met

Syntax
------

    =COUNTIFS(range1,criteria1,[range2],[criteria2],...)

*   _range1_ - The first range to evaluate.
*   _criteria1_ - The criteria to use on range1.
*   _range2_ - \[optional\] The second range to evaluate.
*   _criteria2_ - \[optional\] The criteria to use on range2.

Using the COUNTIFS function 
----------------------------

The COUNTIFS function counts cells in a range when they meet one or more specific conditions. COUNTIFS is one of Excel's most widely used functions, and you find it in all kinds of spreadsheets that perform conditional counts based on dates, text, or numbers. Although common, COUNTIFS has a unique design that splits logical conditions into two parts. As a result, the syntax to define conditions in COUNTIFS can be a little tricky and takes some getting used to. Remember that COUNTIFS uses "AND logic" — to be included in the final count, _all conditions_ must be TRUE.

### Key features

*   Counts values that meet one or more conditions
*   Each new condition requires a new _range_ and _criteria_
*   Works with dates, text, and numbers
*   Supports comparison operators (>, <, <>, =) and wildcards (\*, ?)
*   To be included in the final result, _all conditions must be TRUE_
*   Will return a #VALUE! error if ranges are not the same size
*   Available in all Excel versions since Excel 2007

> Unlike most other Excel functions, COUNTIFS requires an actual range for criteria ranges. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula. For details, [see the example below](https://exceljet.net/functions/countifs-function#array_problem)
> .

### Table of Contents

*   [Syntax](https://exceljet.net/functions/countifs-function#syntax)
    
*   [Basic Example](https://exceljet.net/functions/countifs-function#basic_example)
    
*   [Applying Criteria](https://exceljet.net/functions/countifs-function#applying_criteria)
    
*   [Criteria in another cell](https://exceljet.net/functions/countifs-function#criteria_in_another_cell)
    
*   [Not equal to](https://exceljet.net/functions/countifs-function#not_equal_to)
    
*   [Blank cells](https://exceljet.net/functions/countifs-function#blank_cells)
    
*   [Dates](https://exceljet.net/functions/countifs-function#dates)
    
*   [Wildcards](https://exceljet.net/functions/countifs-function#wildcards)
    
*   [OR logic](https://exceljet.net/functions/countifs-function#or_logic)
    
*   [Summary Table](https://exceljet.net/functions/countifs-function#summary_table)
    
*   [Array Problem](https://exceljet.net/functions/countifs-function#array_problem)
    
*   [Limitations](https://exceljet.net/functions/countifs-function#limitations)
    
*   [Notes](https://exceljet.net/functions/countifs-function#notes)
    

### Syntax

The COUNTIFS function counts the number of cells in a range that meet one or more conditions. The syntax depends on the number of conditions being evaluated. Each condition is provided as a pair of _range_/_criteria_ arguments:

    =COUNTIFS(range,criteria) // 1 condition
    =COUNTIFS(range,criteria,range,criteria) // 2 conditions

If there are two conditions, there will be two _range/criteria_ pairs. If there are three conditions, there will be three _range/criteria_ pairs, and so on. 

> All ranges must be the same size. If you provide different sizes, COUNTIFS will return #VALUE!

### Basic Example

The worksheet below simple contains order data, including Date, Color, State, Quantity, and Total. Using COUNTIFS, we can easily count orders in the data that meet the following conditions:

1.  Count orders where the color is Red.
2.  Count orders where the color is Red, and the state is TX.
3.  Count orders where the color is Red, and the total is over 20.
4.  Count orders where the color is Red, the total is over 20, and the state is TX.

The four formulas in I5:I8 look like this:

    =COUNTIFS(C5:C16,"red")
    =COUNTIFS(C5:C16,"red",D5:D16,"TX")
    =COUNTIFS(C5:C16,"red",F5:F16,">20")
    =COUNTIFS(C5:C16,"red",F5:F16,">20",D5:D16,"TX")

![COUNTIFS function example with multiple conditions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_with_multiple_criteria.png "COUNTIFS function example with multiple conditions")

The meaning of the formula in cell I8 is: _count rows where the color is "red" AND the quantity is >20 AND state is "TX"._ The result is 2 since there are two rows where the color is Red, the quantity is over 20, and the state is TX. Each condition requires a separate range/criteria pair, and there are three pairs in total. To summarize, here are a few things worth noting in the formulas above:

*   Each condition requires a separate _range_/_criteria_ pair.
*   All range arguments must be the same size.
*   The order in which conditions appear does not matter.
*   _Criteria_ can include logical operators (>,<,<>,<=,>=) as needed.
*   An equal sign (=) is not needed for "is equal to" _criteria (i.e. use "red" not "=red")._
*   COUNTIFS is not case-sensitive, so "red" and "Red" will return the same results.
*   Numbers must appear in quotes ("") when used with operators (i.e. ">20").
*   COUNTIFS uses "AND logic," and all conditions must be true.

> The syntax for the _criteria_ argument in COUNTIF is somewhat unusual in Excel. Instead of simply entering >20 as the criteria, you must enter ">20" in double quotes.  If you don't quote values as required, _Excel will not let you enter the formula_. See below for more examples of this syntax.

### Applying Criteria

The COUNTIFS function supports logical operators (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Because COUNTIFS is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
 that split logical criteria into two parts, the syntax is a bit tricky. Each condition requires a separate _range_ and _criteria_, and operators need to be enclosed in double quotes (""). The table below shows some common examples:

| Target | Criteria |
| --- | --- |
| Cells greater than 75 | ">75" |
| Cells equal to 100 | 100 or "100" |
| Cells less than or equal to 100 | "<=100" |
| Cells equal to "Red" | "red" |
| Cells not equal to "Red" | "<>red" |
| Cells that are blank "" | ""  |
| Cells that are _not_ blank | "<>" |
| Cells that begin with "X" | "x\*" |
| Cells less than A1 | "<"&A1 |
| Cells less than today | "<"&TODAY() |

Notice the last two examples use [concatenation](https://exceljet.net/glossary/concatenation)
 with the ampersand (&) character. When a _criteria_ argument includes a value from another cell, or the result of a formula, logical operators like "<" must be joined with concatenation. This is because Excel needs to evaluate cell references and formulas first to get a value before that value can be joined to an operator.

### Criteria in another cell

It is often convenient to put criteria in another cell and then refer to this cell inside your formula. This makes it easy to change criteria later without editing the original formula. For example, you can count cells in a range equal to the value in A1 like this:

    =COUNTIFS(range,A1)

When a condition requires an operator, you must [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the cell reference to the operator. For example, to count cells in a range greater than A1, use a formula like this:

    =COUNTIFS(range,">"&A1)

Note we are joining the ">" operator to cell A1 with an ampersand (&) character. In the worksheet below, COUNTIFS has been configured to return the count of all sales over the value in G4. Notice the greater than operator (>), which is text, must be enclosed in quotes. The formula in G5 is:

    =COUNTIFS(D5:D9,">"&G4) // count if greater than G4

![COUNTIFS function example - criteria in another cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_criteria_in_another_cell.png "COUNTIFS function example - criteria in another cell")

> Don't enclose cell references in double quotes like "A1". Doing so will convert them to text.

### Not equal to

To express "not equal to" criteria, use the "<>" operator surrounded by double quotes (""). For example, use "<>red" for "not red", and "<>blue" for "not blue", as seen in the worksheet below:

![COUNTIFS function example - count cells not equal to](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_not_equal_to.png "COUNTIFS function example - count cells not equal to")

    =COUNTIFS(B5:B9,"<>red") // not red
    =COUNTIFS(B5:B9,"<>blue") // not blue
    =COUNTIFS(B5:B9,"<>"&E7) // not E7
    

Note the following:

*   In the last formula, we use E7 directly, so we need to concatenate like "<>"&E7.
*   Do not use quotes around the cell reference.
*   COUNTIFS is _not_ case-sensitive, so "red", "RED", and "Red" will return the same result.

### Blank cells

COUNTIFS can count cells that are blank (empty) or not blank (not empty). Use an empty string ("") to target _blank cells_ and the "not equal to" operator ("<>") to target cells that are _not blank_. In the worksheet below, COUNTIFS is configured to count blank and not blank cells in column D:

![COUNTIFS function example - count blank and not blank cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_blank_and_not_blank.png "COUNTIFS function example - count blank and not blank cells")

    =COUNTIFS(D5:D9,"") // blank
    =COUNTIFS(D5:D9,"<>") // not blank
    

In the first format, we use an empty string ("") for the _criteria_, which will count _empty cells_. In the second formula, we use the "not equal to" operator ("<>"), which will count _non-empty cells_. Note that the second formula will count cells that contain _any value_. If you want to be more precise, you can adjust the criteria as follows:

    =COUNTIFS(D5:D9,"x")

This formula will count only cells that contain an "x".

### Double quotes ("") in criteria

In general, text values need to be enclosed in double quotes, and numbers do not. However, when a [logical operator](https://exceljet.net/glossary/logical-operators)
 is included with a number, the number _and_ operator must be enclosed in quotes as shown below:

    =COUNTIFS(range,100) // count equal to 100
    =COUNTIFS(range,">50") // count greater than 50
    =COUNTIFS(range,"jim") // count equal to "jim"
    

_Note: Additional conditions must follow the same rules._

### Dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
, so you can use operators like <,>, <=, >= with dates like any other number. The tricky part about using dates in COUNTIFS conditions is entering the dates in a way that Excel will understand. The easiest way to use COUNTIFS with dates is to refer to a valid date in another cell. For example, with a date in A1, you can count dates that are greater than A1 like this:

    =COUNTIFS(range,">"&A1) // count dates greater than A1
    

If you want to hardcode a date into the COUNTIFS function, the best way is to use the [DATE function](https://exceljet.net/functions/date-function)
. For example, to count dates greater than 1-Jan-2024, you can use COUNTIFS like this:

    =COUNTIFS(range,">"&DATE(2024,1,1) // count dates greater than 1-Jan-2024

The worksheet below uses both methods:

![COUNTIFS function example - working with dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_working_with_dates.png "COUNTIFS function example - working with dates")

The formulas in F5:F8 are as follows:

    =COUNTIFS(B5:B12,"<"&DATE(2024,3,1))
    =COUNTIFS(B5:B12,">="&DATE(2024,3,31))
    =COUNTIFS(B5:B12,">"&E10)
    =COUNTIFS(B5:B12,">="&DATE(2024,5,1),B5:B12,"<="&DATE(2024,5,31))

Note the following:

*   When using a cell reference, you must concatenate the reference to an operator like ">"&E10.
*   The DATE function guarantees Excel will interpret a date correctly.
*   Referring to a date in another cell makes it easy to change the date without editing the formula.

> Pro tip: Avoid hard-coding a date into a formula. Instead, put the date in a cell, then reference that cell in your formula. This makes the worksheet more useful since you can easily see the date being used and change the date when needed without editing the formula.

### Wildcards

The COUNTIFS function supports three [wildcards](https://exceljet.net/glossary/wildcard)
 you can use in criteria:

*   Asterisk (\*) - match zero or more characters
*   Question mark (?) - match any one character
*   Tilde (~) - an escape character to match a _literal_ wildcard

 For example, to count text strings that contain the text "apple", you can use a formula like this:

    =COUNTIFS(range,"*apple*") // cells that contain "apple"
    

To count cells that contain any 3 text characters, you can use:

    =COUNTIFS(range,"???") // cells that contain any 3 characters
    

Note that wildcards only work with text values. The formula above will not count a 3-digit number like 123 or 812. The worksheet below shows how wildcards can be used with the COUNTIFS function. The formulas in F5:F8 apply the criteria described in column E.

    =COUNTIFS(B5:B11,"mi*") // begins with "mi"
    =COUNTIFS(B5:B11,"*ota") // ends with "ota"
    =COUNTIFS(B5:B11,"????") // contains 4 characters
    =COUNTIFS(B5:B11,"*~?") // ends with "?"
    

![COUNTIFS function example - working with wildcards](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_working_with_wildcards.png "COUNTIFS function example - working with wildcards")

Note the last formula in F8 uses "\*~?" to match a question mark (?) that occurs at the end of "Montana?" and "Michigan?". The tilde (~) is an escape character that allows you to find a _literal_ wildcard. To match a question mark (?), use "~?"; to match an asterisk(\*), use "~\*"; and to match a tilde (~), use "~~". The table below shows more examples of how wildcards can be used:

| Pattern | Behavior | Will match |
| --- | --- | --- |
| ?   | Any one character | "A", "B", "c", "z", etc. |
| ??  | Any two characters | "AA", "AZ", "zz", etc. |
| ??? | Any three characters | "Jet", "AAA", "ccc", etc. |
| \*  | Any characters | "apple", "APPLE", "A100", etc. |
| \*th | Ends in "th" | "bath", "fourth", etc. |
| c\* | Starts with "c" | "Cat", "CAB", "cindy", "candy", etc. |
| ?\* | At least one character | "a", "b", "ab", "ABCD", etc. |
| ???-?? | Five characters with a hyphen | "ABC-99","100-ZT", etc. |
| \*~? | Ends with a question mark | "Hello?", "Anybody home?", etc. |
| \*xyz\* | Contains "xyz" | "code is XYZ", "100-XYZ", "XyZ90", etc. |

> Note: wildcards only work with _text_, not numbers.

### OR logic

The COUNTIFS function is designed to apply multiple conditions with "AND logic," so there is no obvious way to count cells with "OR logic". However, one workaround is to provide the _criteria_ as an [array constant](https://exceljet.net/glossary/array-constant)
 like {"red","blue}, and then nest the COUNTIFS formula inside the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(COUNTIFS(range,{"red","blue"})) // count red or blue
    

The formula above will count cells in _range_ when cells in _range_ contain "red" or "blue". Essentially, COUNTIFS returns _two_ sums, one for "red" and one for "blue", and SUM returns the sum of the counts. For more details, [see this example](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
.

### Summary Table

You can use COUNTIFS to create a simple summary table. In the worksheet below, we have a list of unique colors in F5:F9. The goal is to subtotal the amounts in column D by color. The formula in cell G5, copied down, is:

    =COUNTIFS($C$5:$C$16,F5)

![COUNTIFS function example - making a simple summary table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_simple_summary_table.png "COUNTIFS function example - making a simple summary table")

Notice that the _range_ is locked as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to prevent changes as the formula is copied down the column. If you are using Excel 2021 or later, you can generate all totals at once with a [dynamic array formula](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 like this:

    =COUNTIFS(C5:C16,F5:F9)

We don't need the absolute references in this case because a single formula creates all results. You can go one step further by using the [UNIQUE function](https://exceljet.net/functions/unique-function)
 in cell F5 to get a list of unique colors, then referring to the [spill range](https://exceljet.net/glossary/spill-range)
 directly like this:

    =COUNTIFS(C5:C16,F5#)

> In Excel 365, you can also use the new [GROUPBY function](https://exceljet.net/functions/groupby-function)
>  to create a summary table like this.

### Array Problem

_Note: For more advanced use cases, this is an important limitation in what COUNTIFS can do._

One of the more tricky limitations of COUNTIFS is that it won't allow an _array_ for a _range_ argument. To understand the problem, consider the worksheet below, where we have 12 dates in column B and 12 amounts in column C. The goal is to create a formula to count the amounts by year. We can do that with the following COUNTIFS formula:

    =COUNTIFS(B5:B16,">="&DATE(E5,1,1),B5:B16,"<="&DATE(E5,12,31))

_Note: I would normally use absolute references for the two ranges so that the formula can be copied down without changes, but I have left the addresses relative here so they are easier to read._

![COUNTIFS function example - array problem worksheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_of_array_problem1.png "COUNTIFS function example - array problem worksheet")

This formula works fine, but it's a little complicated. If you have some experience with Excel formulas, you might think you can use COUNTIFS and YEAR together in a clever formula like this:

    =COUNTIFS(YEAR(B5:B16),E5)

The idea is to extract the year from the dates in column B with the [YEAR function](https://exceljet.net/functions/year-function)
, and then use 2024 (in cell E5) for the criteria. This would be cool if it worked. However, Excel won't even let you enter this formula. If you try, you'll get a generic "There's a problem with your formula" error:

![COUNTIFS function example - array problem formula can't be entered](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countifs_function_example_of_array_problem2.png "COUNTIFS function example - array problem formula can't be entered")

The problem is that COUNTIFS _requires_ a proper range for the range argument, but YEAR(B5:B16) will return an array like this:

    {2024;2024;2024;2024;2024;2025;2025;2025;2025;2025;2025;2025}

To be clear, using YEAR like this works fine in most other formulas. However, COUNTIFS is not programmed to handle arrays, so it won't work. How can we work around this problem? One nice alternative is to switch to the SUMPRODUCT function and use a formula like this:

    =SUMPRODUCT(--(range=criteria))

If we modify the pattern above to fit the workbook example, we get the following:

    =SUMPRODUCT(--(YEAR(B5:B16)=E5))

This formula is quite a bit simpler than the COUNTIFS formula above. It's a good example of how SUMPRODUCT can often solve a tricky problem in a clever and elegant formula.

> Remember: If you try to provide an array for a range, you won't be able to enter the formula because Excel will display a "There's a problem with your formula" error dialog. The "array problem" is not mentioned explicitly.

### Limitations

The COUNTIFS function has several limitations you should be aware of:

*   COUNTIFS is not case-sensitive. Use the [EXACT function](https://exceljet.net/functions/exact-function)
     for [case-sensitive counts](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    .
*   Conditions in COUNTIFS are joined by AND logic. All conditions must be TRUE. For simple OR logic, see the [approach above](https://exceljet.net/functions/countifs-function#or_logic)
    , or the [more advanced formula here](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)
    .
*   COUNTIFS requires an actual [range](https://exceljet.net/glossary/range)
     for the range argument; you can't provide an array. This means you can't alter values in a range inside your formula before applying criteria. [Read more here](https://exceljet.net/functions/countifs-function#array_problem)
    .
*   COUNTIFS does not correctly count long numbers greater than 15 digits. [Example here](https://exceljet.net/formulas/count-long-numbers)
    .
*   If you reference a range in an _external workbook_, COUNTIFS requires that the workbook be _open_ to calculate a result. If the external workbook is not open, you will see a #VALUE! error. As a workaround, you can switch to the SUMPRODUCT function, which does not have this limitation. The syntax will look like this: =SUMPRODUCT(--(criteria\_range=criteria)). See [this page](https://exceljet.net/functions/sumproduct-function)
     for details.
*   COUNTIFS has some other quirks, which are [detailed in this article](https://exceljet.net/articles/excels-racon-functions)
    .

The most common way to work around most of these limitations is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. However, the latest version of Excel offers powerful alternatives, including [BYROW](https://exceljet.net/functions/byrow-function)
, [BYCOL](https://exceljet.net/functions/bycol-function)
, and [GROUPBY](https://exceljet.net/functions/groupby-function)
.

### Notes

*   All _ranges_ must be the same size or COUNTIFS will return a #VALUE! error.
*   Text strings in criteria must be enclosed in double quotes  ( i.e.,">32", "TX", "app\*", etc.)
*   Cell references in criteria are _not_ enclosed in quotes, i.e., "<"&A1
*   To match a literal question mark(?) or asterisk (\*), use a tilde (~) like (~?, ~\*).
*   COUNTIFS can handle up to 127 conditions.
*   COUNTIFS _requires_ a range. You can't substitute an [array](https://exceljet.net/glossary/array)
    .
*   COUNTIFS returns incorrect results when used to match strings longer than 255 characters.
*   COUNTIFS will return a #VALUE error when referencing another workbook that is not open.

COUNTIFS function examples
--------------------------

[![Excel formula: Highlight duplicate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20duplicate%20rows.png "Excel formula: Highlight duplicate rows")](https://exceljet.net/formulas/highlight-duplicate-rows)

### [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)

In the formula, COUNTIFS counts the number of times each value in a cell appears in its "parent" column. By definition, each value must appear at least once, so when the count > 1, the value must be a duplicate. The references are carefully locked so the formula will return true only when all 3...

[![Excel formula: Course completion status summary](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/course%20completion%20status%20summary.png "Excel formula: Course completion status summary")](https://exceljet.net/formulas/course-completion-status-summary)

### [Course completion status summary](https://exceljet.net/formulas/course-completion-status-summary)

The table in B3:D11 is a log that shows courses completed by various people. If a course has been completed by a person, there will be an entry in the table with name, course, and date. For the purpose of this example, if we find and entry for a given name/course, we can assume that course is...

[![Excel formula: Count not equal to multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20not%20equal%20to%20multiple%20criteria.png "Excel formula: Count not equal to multiple criteria")](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

### [Count not equal to multiple criteria](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)

In this example, the goal is to count rows in a set of data using multiple criteria and "not equals to" logic. Specifically, we want to count males that are not in group A or B. All data is in an Excel Table named data in the range B5:D15. This problem can be solved with the COUNTIFS function or...

[![Excel formula: COUNTIFS with variable range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/countifs%20with%20a%20variable%20range.png "Excel formula: COUNTIFS with variable range")](https://exceljet.net/formulas/countifs-with-variable-range)

### [COUNTIFS with variable range](https://exceljet.net/formulas/countifs-with-variable-range)

In the example shown, the formula in B11 is: =COUNTIFS(OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1),"<>") Working from the inside out, the work of setting up a variable range is done by the OFFSET function here: OFFSET(B$5,0,0,ROW()-ROW(B$5)-1,1) // variable range OFFSET has five arguments and is...

[![Excel formula: Course completion summary with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Course%20completion%20summary%20with%20criteria.png "Excel formula: Course completion summary with criteria")](https://exceljet.net/formulas/course-completion-summary-with-criteria)

### [Course completion summary with criteria](https://exceljet.net/formulas/course-completion-summary-with-criteria)

Note: there are many ways to summarize data with COUNTIFS, SUMIFS, etc. This example shows one specific and arbitrary way. Before you go the formula route, consider a pivot table first , since pivot tables are far simpler to set up and do most of the hard work for you. The table in B3:F11 is a log...

[![Excel formula: Count paired items in listed combinations](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20paired%20items%20in%20listed%20combinations.png "Excel formula: Count paired items in listed combinations")](https://exceljet.net/formulas/count-paired-items-in-listed-combinations)

### [Count paired items in listed combinations](https://exceljet.net/formulas/count-paired-items-in-listed-combinations)

We want to count how often items in columns B, C, and D appear together. For example, how often A appears with C, B appears with F, G appears with D, and so on. This would seem like a perfect use of COUNTIFS, but if we try to add criteria looking for 2 items across 3 columns, it isn't going to work...

[![Excel formula: Count cells between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20dates_0.png "Excel formula: Count cells between dates")](https://exceljet.net/formulas/count-cells-between-dates)

### [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)

In this example, the goal is to count the number of cells in column D that contain dates that are between two variable dates in G4 and G5. This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. For convenience, the worksheet contains two named ranges...

[![Excel formula: Count if two criteria match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20if%20two%20criteria%20match.png "Excel formula: Count if two criteria match")](https://exceljet.net/formulas/count-if-two-criteria-match)

### [Count if two criteria match](https://exceljet.net/formulas/count-if-two-criteria-match)

In this example, the goal is to count orders where the color is "blue" and the quantity is greater than 15. All data is in the range B5:B15. There are two primary ways to solve this problem, one with the COUNTIFS function, the other with the SUMPRODUCT function. Both approaches are explained below...

[![Excel formula: Count cells not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to.png "Excel formula: Count cells not equal to")](https://exceljet.net/formulas/count-cells-not-equal-to)

### [Count cells not equal to](https://exceljet.net/formulas/count-cells-not-equal-to)

In this example, the goal is to count the number of cells in column D that are not equal to a given color. The simplest way to do this is with the COUNTIF function , as explained below. Not equal to In Excel, the operator for not equal to is "<>". For example: =A1<>10 // A1 is not equal...

[![Excel formula: Count dates in current month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20dates%20in%20current%20month.png "Excel formula: Count dates in current month")](https://exceljet.net/formulas/count-dates-in-current-month)

### [Count dates in current month](https://exceljet.net/formulas/count-dates-in-current-month)

At the core, this formula uses the COUNTIFS function to count dates that are greater than or equal to the first day of the current month, and less than the first day of the next month. The EOMONTH function is used to create both dates based on the current date, which is supplied by the TODAY...

[![Excel formula: Count non-blank cells by category](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20non-blank%20cells%20by%20category.png "Excel formula: Count non-blank cells by category")](https://exceljet.net/formulas/count-non-blank-cells-by-category)

### [Count non-blank cells by category](https://exceljet.net/formulas/count-non-blank-cells-by-category)

In this example, the goal is to count non-blank dates in column D by group. All data is an Excel Table named data in the range B5:D16. This problem can be solved with the COUNTIFS function , as explained below. COUNTIFS function The Excel COUNTIFS function returns the count of cells that meet one...

[![Excel formula: Sum time over 30 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20over%2030%20minutes.png "Excel formula: Sum time over 30 minutes")](https://exceljet.net/formulas/sum-time-over-30-minutes)

### [Sum time over 30 minutes](https://exceljet.net/formulas/sum-time-over-30-minutes)

This formula uses the SUMPRODUCT function to sum the result of two expressions that yield arrays. The goal is to sum only time greater than 30 minutes, the "surplus" or "extra" time. The first expression subtracts 30 minutes from every time in the named range "times": times-TIME(0,30,0) This...

[![Excel formula: New customers per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/new%20customers%20per%20month.png "Excel formula: New customers per month")](https://exceljet.net/formulas/new-customers-per-month)

### [New customers per month](https://exceljet.net/formulas/new-customers-per-month)

This formula relies on a helper column, which is column E in the example shown. The formula in E5, copied down, is: =(COUNTIFS($B$5:B5,B5)=1)+0 This formula returns a 1 for new customers and a 0 for repeat customers, and is explained in detail here . Once this formula is in place, the COUNTIFS...

[![Excel formula: Count cells greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20greater%20than.png "Excel formula: Count cells greater than")](https://exceljet.net/formulas/count-cells-greater-than)

### [Count cells greater than](https://exceljet.net/formulas/count-cells-greater-than)

In this example, the goal is to count test scores in column C that are greater than 90. The simplest way to do this is with the COUNTIF function , which takes two arguments , range and criteria : =COUNTIF(range,criteria) All test scores are in the range C5:C16 and we want to count scores greater...

[![Excel formula: Count between dates by age range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20between%20dates%20by%20age%20range.png "Excel formula: Count between dates by age range")](https://exceljet.net/formulas/count-between-dates-by-age-range)

### [Count between dates by age range](https://exceljet.net/formulas/count-between-dates-by-age-range)

The goal of this example is to count rows in the data where the date joined falls between start and end dates (inclusive) and the age also falls into the age ranges seen in column G. The formula is complicated somewhat by the fact that the age range labels are actually text, so we need to extract a...

COUNTIFS function videos
------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIFS%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countifs-function)

### [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

In this video, we'll look at how to use the COUNTIFS function to count cells that meet multiple criteria. Let's take a look. In this first set of tables, we have two named ranges , "number" and "color." In column G, I'll enter a formula that satisfies the conditions in column E. The COUNTIFS...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Count paired items in listed combinations](https://exceljet.net/formulas/count-paired-items-in-listed-combinations)
    
*   [Customer is new](https://exceljet.net/formulas/customer-is-new)
    
*   [Count numbers by range](https://exceljet.net/formulas/count-numbers-by-range)
    
*   [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
    
*   [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)
    
*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [Count calls at specific times](https://exceljet.net/formulas/count-calls-at-specific-times)
    
*   [Course completion summary with criteria](https://exceljet.net/formulas/course-completion-summary-with-criteria)
    
*   [Flag first duplicate in a list](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)
    

### Videos

*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

### Links

*   [Microsoft COUNTIFS function documentation](https://support.office.com/en-us/article/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842)
    

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