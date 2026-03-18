# Excel COUNTIF function | Exceljet

**Source:** https://exceljet.net/functions/countif-function

---

[Skip to main content](https://exceljet.net/functions/countif-function#main-content)

[](https://exceljet.net/functions/countif-function#)

*   [Previous](https://exceljet.net/functions/countblank-function)
    
*   [Next](https://exceljet.net/functions/countifs-function)
    

Excel 2003

[Statistical](https://exceljet.net/functions#Statistical)

COUNTIF Function
================

by Dave Bruns · Updated 8 Jun 2025

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[MINIFS](https://exceljet.net/functions/minifs-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")

Summary
-------

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count cells that contain dates, numbers, and text. Criteria can include [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?).

Purpose 
--------

Count cells that match criteria

Return value 
-------------

A number representing cells counted.

Syntax
------

    =COUNTIF(range,criteria)

*   _range_ - The range of cells to count.
*   _criteria_ - The criteria that controls which cells should be counted.

Using the COUNTIF function 
---------------------------

The COUNTIF function counts cells in a range when they meet a specific condition. COUNTIF is one of Excel's most widely used functions, and you will find it in all kinds of spreadsheets that calculate conditional counts based on dates, text, or numbers. While powerful, COUNTIF has a unique syntax that splits logical conditions into two parts, making it different from many other Excel functions. This syntax takes a little getting used to. Remember that COUNTIF can only apply _one condition_. For multiple conditions, use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
.

### Key features

*   Counts cell values that meet a single condition (use [COUNTIFS](https://exceljet.net/functions/countifs-function)
     for multiple conditions)
*   Works with dates, text, and numbers
*   Supports comparison operators (>, <, <>, =) and wildcards (\*, ?)
*   Available in all Excel versions

> Unlike most other Excel functions, COUNTIF requires an actual range for the _range_ argument. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula. For details, [see the example below](https://exceljet.net/functions/countif-function#array_problem)
> .

### Table of Contents

*   [Basic Example](https://exceljet.net/functions/countif-function#basic_example)
    
*   [Applying Criteria](https://exceljet.net/functions/countif-function#applying_criteria)
    
*   [Criteria in another cell](https://exceljet.net/functions/countif-function#criteria_in_another_cell)
    
*   [Not equal to](https://exceljet.net/functions/countif-function#not_equal_to)
    
*   [Blank cells](https://exceljet.net/functions/countif-function#blank_cells)
    
*   [Dates](https://exceljet.net/functions/countif-function#dates)
    
*   [Wildcards](https://exceljet.net/functions/countif-function#wildcards)
    
*   [OR logic](https://exceljet.net/functions/countif-function#or_logic)
    
*   [Summary Table](https://exceljet.net/functions/countif-function#summary_table)
    
*   [Array Problem](https://exceljet.net/functions/countif-function#array_problem)
    
*   [Limitations](https://exceljet.net/functions/countif-function#sumif_limitations)
    
*   [Notes](https://exceljet.net/functions/countif-function#notes)
    

### Basic Example

The generic syntax for COUNTIF looks like this:

    =COUNTIF(range,criteria)

The _criteria_ is applied to cells in the _range_. When cells meet the criteria, they are added to the count. In the worksheet below, we have a small amount of sales data. We use COUNTIF in three formulas to perform these calculations: (1) count all sales over $100, (2) count all sales by Jim, and (3) count all sales in CA (California). The formulas in G5:G7 look like this:

    =COUNTIF(D5:D16,">100") // count sales over 100
    =COUNTIF(B5:B16,"jim") // count sales by Jim
    =COUNTIF(C5:C16,"CA") // count sales in CA

![COUNTIF function - basic example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_basic_example.png "COUNTIF function - basic example")

Note the following about the formulas above:

*   An equal sign (=) is not needed with "is equal to" _criteria (i.e., use "jim" not "=jim")._
*   COUNTIF is not case-sensitive, so "jim", "Jim", and "JIM" will return the same results.
*   Numbers must appear in quotes ("") when used with operators (i.e. ">100").

> Note that the syntax for the _criteria_ argument in COUNTIF is somewhat unusual in Excel. Instead of simply entering >100 as the criteria, you must enter ">100" in double quotes. If you don't quote values as required, Excel will not let you enter the formula. See below for more examples of this syntax.

### Applying Criteria

The COUNTIF function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. The tricky part about using the COUNTIF function is the syntax needed to apply criteria. This is because COUNTIF is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
 that split logical criteria into two parts: _range_ and _criteria_. Because of this design, operators must be enclosed in double quotes (""). The table below shows examples of the syntax needed for common criteria:

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
| Cells equal to A1 | A1  |
| Cells less than A1 | "<"&A1 |
| Cells less than today | "<"&TODAY() |

Notice the last two examples involve [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
 with the ampersand (&) character. Any time you use a value from another cell (or the result of a formula) with a logical operator like "<", you must concatenate. This is because Excel needs to evaluate cell references and formulas first before the value can used with an operator.

### Criteria in another cell

A great way to use COUNTIF is to put criteria in another cell and then refer to this cell inside your formula. This makes it easy to change criteria later without editing the original formula. For example, you can count cells in a range equal to the value in A1 like this:

    =COUNTIF(range,A1)

If you need to include an operator in the criteria, you must [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the cell reference to the operator. For example, to count cells that are greater than A1, use a formula like this:

    =COUNTIF(range,">"&A1)

Note we are joining the ">" operator to cell A1 with an ampersand (&) character. In the worksheet below, COUNTIF has been configured to return the count of all sales _over the value in F5_. Notice the greater than operator (>), which is text, must be enclosed in quotes. The formula in F5 is:

    =COUNTIF(D5:D16,">"&F5) // count if greater than G4
    

![COUNTIF function example - criteria in another cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_example_criteria_in_another_cell.png "COUNTIF function example - criteria in another cell")

> Don't enclose cell references in double quotes like "A1". Doing so will convert them to text.

### Not equal to

To express "not equal to" criteria, use the "<>" [operator](https://exceljet.net/glossary/logical-operators)
 surrounded by double quotes (""). For example, use "<>red" for "not red", and "<>blue" for "not blue", as seen in the worksheet below:

![COUNTIF function example - not equal to](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_example_not_equal_to.png "COUNTIF function example - not equal to")

    =COUNTIF(B5:B9,"<>red") // not equal to "red"
    =COUNTIF(B5:B9,"<>blue") // not equal to "blue"
    =COUNTIF(B5:B9,"<>"&E7) // not equal to E7
    

Note the following:

*   In the last formula, we use E7 directly, so we need to concatenate like "<>"&E7.
*   Do not use quotes around the cell reference.
*   COUNTIF is _not_ case-sensitive, so "red", "RED", and "Red" will return the same result.

### Blank cells

COUNTIF can count cells that are blank or not blank. Use an empty string ("") to target _blank cells_ and the "not equal to" operator ("<>") to target cells that are _not blank_. In the worksheet below, COUNTIF is used to count blank and not blank cells depending on whether column D contains "x" or is empty:

![COUNTIF function example - count blank and not blank cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_example_count_blank_and_not_blank.png "COUNTIF function example - count blank and not blank cells")

    =COUNTIF(D5:D9,"") // blank
    =COUNTIF(D5:D9,"<>") // not blank
    

The result is that there are 2 "not paid" (blank) invoices and 3 paid invoices. To be more precise, you can use a formula like this that counts cells only when column D contains an "x":

    =COUNTIF(D5:D9,"x") // equals "x"
    

### Dates

In Excel, [dates are large serial numbers](https://exceljet.net/glossary/excel-date)
, so you can use operators like <,>, <=, and >= with dates like any other number. The tricky part about using dates in COUNTIF criteria is entering the dates in a way that Excel will understand. The most reliable method is to refer to a date in another cell or use the [DATE function](https://exceljet.net/functions/date-function)
. The worksheet below shows both methods:

![COUNTIF function example - working with dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_example_working_with_dates.png "COUNTIF function example - working with dates")

    =COUNTIF(B5:B9,"<"&DATE(2024,3,1))
    =COUNTIF(B5:B9,">="&DATE(2024,4,1))
    =COUNTIF(B5:B9,">"&E9)
    

Note the following:

*   When using a function with an operator, you must concatenate like "<"&DATE(2014,3,1)
*   When using a cell reference with an operator, you must concatenate like ">"&E9.

> COUNTIF can apply only one condition. To count dates _between_ two dates, you'll want to switch to the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
> , which can count cells based on multiple conditions.

> Pro tip: Avoid hard-coding a date into a formula. Instead, put the date in a cell, then reference that cell in your formula. This makes the worksheet more useful since you can easily see the date being used and change the date when needed without editing the formula.

### Wildcards

COUNTIF supports three wildcards you can use in criteria for more flexible matching:

*   Asterisk (\*) - match zero or more characters
*   Question mark (?) - match any one character
*   Tilde (~) - an escape character to match a _literal wildcard_

The worksheet below shows how wildcards can be used with COUNTIF. The formulas in F5:F8 apply the criteria described in column E.

    =COUNTIF(B5:B11,"mi*") // begins with "mi"
    =COUNTIF(B5:B11,"*ota") // ends with "ota"
    =COUNTIF(B5:B11,"????") // contains 4 characters
    =COUNTIF(B5:B11,"*~?") // ends with "?"

![COUNTIF function example - working with wildcards](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_example_working_with_wildcards.png "COUNTIF function example - working with wildcards")

Note the last formula in F8 uses "\*~?" to match a question mark (?) that occurs at the end of "Michigan?" and "Montana?". The tilde (~) is an escape character that allows you to find a _literal_ wildcard. To match a question mark (?), use "~?"; to match an asterisk(\*), use "~\*"; and to match a tilde (~), use "~~". The table below shows more examples of how wildcards can be used:

| Pattern | Behavior | Will match |
| --- | --- | --- |
| ?   | Any one character | "A", "B", "c", "z", etc. |
| ??  | Any two characters | "AA", "AZ", "zz", etc. |
| ??? | Any three characters | "Jet", "AAA", "ccc", etc. |
| \*  | Any characters | "apple", "APPLE", "A100", etc. |
| \*th | Ends in "th" | "bath", "fourth", etc. |
| c\* | Starts with "c" | "Cat", "CAB", "cindy", "candy", etc. |
| ?\* | At least one character | "a", "b", "ab", "ABCD", etc. |
| ???-?? | Five characters with a hyphen | "ABC-99", "100-ZT", etc. |
| \*~? | Ends with a question mark | "Hello?", "Anybody home?", etc. |
| \*xyz\* | Contains "xyz" | "code is XYZ", "100-XYZ", "XyZ90", etc. |

> Note: Wildcards only work with _text_, not numbers.

### OR logic

The COUNTIF function is designed to apply just one condition, so there is no obvious way to count cells with "this OR that" logic. However, one workaround is to provide the _criteria_ as an [array constant](https://exceljet.net/glossary/array-constant)
 like {"red","blue}, and then nest the COUNTIF formula inside the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(COUNTIF(range,{"red","blue"})) // count red or blue
    

The formula above will count cells in _range_ that contain "red" or "blue". Essentially, COUNTIF returns two counts in an array (one for "red" and one for "blue"), and the SUM function returns the sum of the counts. [This example](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
 explains this idea in more detail.

### Summary Table

You can use COUNTIF to create a simple summary table of counts. In the worksheet below, we have a list of unique colors in F5:F9. The goal is to generate a count for each color. The formula in cell G5, copied down, is:

    =COUNTIF($C$5:$C$16,F5)

![COUNTIF function example - creating a simple summary table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_example_simple_summary_table.png "COUNTIF function example - creating a simple summary table")

Notice that the _range_ is locked as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to prevent changes as the formula is copied down the column. If you are using Excel 2021 or later, you can generate all totals at once with a [dynamic array formula](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 like this:

    =COUNTIF(C5:C16,F5:F9)

We don't need absolute references in this case because a single formula creates all results. You can go one step further by using the [UNIQUE function](https://exceljet.net/functions/unique-function)
 in cell F5 to get a list of unique colors, then referring to the [spill range](https://exceljet.net/glossary/spill-range)
 directly like this:

    =COUNTIF(C5:C16,F5#)

The advantage of using the spill range is that the counts will update if the list of unique colors changes.

> In Excel 365, you can also use the new [GROUPBY function](https://exceljet.net/functions/groupby-function)
>  to create a summary table.

### Array Problem

One tricky limitation of COUNTIF is that it won't allow an _array_ for the _range_ argument. This means you can't feed an array from another function into COUNTIF like a range. To understand the problem, consider the worksheet below, where we have 12 dates in column B and 12 amounts in column C. The goal is to create a formula to count the entries per year. If you have some experience with Excel formulas, you might think you can use COUNTIF and YEAR together in a clever formula like this:

    =COUNTIF(YEAR(B5:B16),E5)

The idea is to extract the year from the dates in column B with the [YEAR function](https://exceljet.net/functions/year-function)
 and then use 2024 in cell E5 for the criteria. This would be cool if it worked. However, Excel won't even let you enter this formula. If you try, you'll get a generic "There's a problem with your formula" error.

![COUNTIF function example - the "array problem"](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_example_of_array_problem.png "COUNTIF function example - the "array problem"")

The problem is that COUNTIF _requires_ a proper range for the _range_ argument, but YEAR(B5:B16) will return an _array_ like this:

    {2024;2024;2024;2024;2024;2025;2025;2025;2025;2025;2025;2025}

To be clear, using YEAR like this works fine in most other formulas. However, SUMIF is not programmed to handle arrays, so it won't work. How can we work around this problem? One nice solution is to switch to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and use a formula like this:

    =SUMPRODUCT(--(YEAR(range)=value))

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is a way to convert TRUE and FALSE values to 1s and 0s. If we adapt the pattern above to the workbook example, we get the following:

    =SUMPRODUCT(--(YEAR(B5:B16)=E5))

![COUNTIF function example - workaround for the array problem](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/countif_function_example_of_array_problem_workaround.png "COUNTIF function example - workaround for the array problem")

_Note: I would normally use absolute references for the two ranges so that the formula can be copied down without changes, but I have left the addresses relative here to make the formula easier to read._

Another option is to switch to the COUNTIFS function and use two conditions to capture all dates in a given year with a formula like this:

    =COUNTIFS(B5:B16,">="&DATE(E5,1,1),B5:B16,"<="&DATE(E5,12,31))

However, this is a more complicated formula, and I prefer the SUMPRODUCT option. In fact, this is a good example of how SUMPRODUCT can often solve a tricky problem in a clever and elegant formula.

> Remember: If you try to provide an array for a range, you won't be able to enter the formula because Excel will display a "There's a problem with your formula" error dialog. The "array problem" is not mentioned explicitly.

### Limitations

The COUNTIF function has several limitations you should be aware of:

*   COUNTIF only supports a single condition. To count cells that meet multiple conditions, use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
    .
*   COUNTIF is not case-sensitive. Use the [EXACT function](https://exceljet.net/functions/exact-function)
     for [case-sensitive counts](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    .
*   COUNTIF requires an actual [range](https://exceljet.net/glossary/range)
     for the range argument; you can't provide an array. This means you can't alter values in a range inside your formula before applying criteria. [Read more here](https://exceljet.net/functions/countif-function#array_problem)
    .
*   COUNTIF does not correctly count long numbers greater than 15 digits. [Example here](https://exceljet.net/formulas/count-long-numbers)
    .
*   If you reference a range in an _external workbook_, COUNTIF requires that the workbook be _open_ to calculate a result. If the external workbook is not open, you will see a #VALUE! error. As a workaround, you can switch to the SUMPRODUCT function, which does not have this limitation. The syntax will look like this: =SUMPRODUCT(--(criteria\_range=criteria)). See [this page](https://exceljet.net/functions/sumproduct-function)
     for details.
*   COUNTIF has other quirks [explained in this article](https://exceljet.net/articles/excels-racon-functions)
    .

The most common way to work around most of these limitations is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. However, the latest version of Excel offers powerful alternatives, including [BYROW](https://exceljet.net/functions/byrow-function)
, [BYCOL](https://exceljet.net/functions/bycol-function)
, and [GROUPBY](https://exceljet.net/functions/groupby-function)
.

### Notes

*   COUNTIF only supports one condition. Use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
     for multiple conditions.
*   Text strings in criteria must be enclosed in double quotes  ( i.e.,">32", "TX", "app\*", etc.)
*   Cell references in criteria are _not_ enclosed in quotes, i.e., "<"&A1
*   The wildcard characters ? and \* can be used in criteria. A question mark matches any one character, and an asterisk matches any sequence of characters (zero or more).
*   To match a literal question mark(?) or asterisk (\*), use a tilde (~) like (~?, ~\*).
*   COUNTIF _requires_ a range. You can't substitute an [array](https://exceljet.net/glossary/array)
    .
*   COUNTIF returns incorrect results when used to match strings longer than 255 characters.
*   COUNTIF will return a #VALUE error when referencing another workbook that is not open.

COUNTIF function examples
-------------------------

[![Excel formula: Count cells that begin with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20begin%20with.png "Excel formula: Count cells that begin with")](https://exceljet.net/formulas/count-cells-that-begin-with)

### [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)

In this example, the goal is to count cells in the range B5:B16 that begin with specific text, which is provided in column D. For convenience, the range B5:B16 is named data . COUNTIF function The simplest way to solve this problem is with the COUNTIF function and a wildcard. COUNTIF supports three...

[![Excel formula: IF with wildcards](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/IF_with_wildcards.png "Excel formula: IF with wildcards")](https://exceljet.net/formulas/if-with-wildcards)

### [IF with wildcards](https://exceljet.net/formulas/if-with-wildcards)

The goal of this formula is to verify whether the values in column B follow the format xx-xxxx-xxx, where "x" represents any single character. The IF function doesn't support wildcards directly, so we can't use IF by itself. Instead, we can combine the IF function with the COUNTIF function, which...

[![Excel formula: Validate input with check mark](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/validate_input_with_check_mark.png "Excel formula: Validate input with check mark")](https://exceljet.net/formulas/validate-input-with-check-mark)

### [Validate input with check mark](https://exceljet.net/formulas/validate-input-with-check-mark)

This formula is a good example of nesting one function inside another. At the core, this formula uses the IF function to return a check mark (✓) when a logical test returns TRUE: =IF(logical\_test,"✓","") If the test returns FALSE, the formula returns an empty string (""). For the logical test, we...

[![Excel formula: Count cells not equal to many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20many.png "Excel formula: Count cells not equal to many things")](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

### [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

First, a little context. Normally, if you have just a couple things you don't want to count, you can use COUNTIFS like this: =COUNTIFS(range,"<>apple",range,"<>orange") But this doesn't scale very well if you have a list of many things, because you'll have to add an additional range/...

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Highlight duplicate values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20duplicate%20values.png "Excel formula: Highlight duplicate values")](https://exceljet.net/formulas/highlight-duplicate-values)

### [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)

COUNTIF simply counts the number of times each value appears in the range. When the count is more than 1, the formula returns TRUE and triggers the rule. When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the...

[![Excel formula: Volunteer hours requirement calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/volunteer%20hours%20requirement%20calculation.png "Excel formula: Volunteer hours requirement calculation")](https://exceljet.net/formulas/volunteer-hours-requirement-calculation)

### [Volunteer hours requirement calculation](https://exceljet.net/formulas/volunteer-hours-requirement-calculation)

In this example, the goal create a formula that will return TRUE when a volunteer has successfully logged the required number of hours in each of the three categories. Two requirements must be satisfied: A volunteer should have at least 5 hours in each of the three categories. A volunteer needs to...

[![Excel formula: Find missing values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find_missing_values.png "Excel formula: Find missing values")](https://exceljet.net/formulas/find-missing-values)

### [Find missing values](https://exceljet.net/formulas/find-missing-values)

The goal is to identify invoice numbers in range D5:D11 that are missing in range B5:B16 (named list ). Two good ways to solve this problem in Excel are the COUNTIF function and the MATCH function . Both approaches are explained below. COUNTIF function COUNTIF counts cells in a range that meet a...

[![Excel formula: Highlight duplicate rows](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/highlight%20duplicate%20rows.png "Excel formula: Highlight duplicate rows")](https://exceljet.net/formulas/highlight-duplicate-rows)

### [Highlight duplicate rows](https://exceljet.net/formulas/highlight-duplicate-rows)

In the formula, COUNTIFS counts the number of times each value in a cell appears in its "parent" column. By definition, each value must appear at least once, so when the count > 1, the value must be a duplicate. The references are carefully locked so the formula will return true only when all 3...

[![Excel formula: Highlight cells that end with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20cells%20that%20end%20with.png "Excel formula: Highlight cells that end with")](https://exceljet.net/formulas/highlight-cells-that-end-with)

### [Highlight cells that end with](https://exceljet.net/formulas/highlight-cells-that-end-with)

When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the rule is created. In this case, the rule is evaluated for each cell in B4:G12, and the reference to B4 will change to the address of each cell being evaluated...

[![Excel formula: Count cells equal to this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20this%20or%20that.png "Excel formula: Count cells equal to this or that")](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

### [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

In this example, the goal is to count cells in the range D5:D15 that contain "red" or "blue". For convenience, the D5:D15 is named color . Counting cells equal to this OR that is more complicated than it first appears because there is no built-in function for counting with OR logic. The COUNTIFS...

[![Excel formula: Count numbers with leading zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20numbers%20with%20leading%20zeros.png "Excel formula: Count numbers with leading zeros")](https://exceljet.net/formulas/count-numbers-with-leading-zeros)

### [Count numbers with leading zeros](https://exceljet.net/formulas/count-numbers-with-leading-zeros)

In this example, the goal is to count numbers that contain leading zeros. In cell E5, we have the code "009875" and we want to count how many times this code appears in the range B5:B16. The challenge is that Excel can be finicky with leading zeros. Technically, the values in B5:B16 are text , as...

[![Excel formula: Unique values by count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20by%20count.png "Excel formula: Unique values by count")](https://exceljet.net/formulas/unique-values-by-count)

### [Unique values by count](https://exceljet.net/formulas/unique-values-by-count)

This example uses the UNIQUE function together with the FILTER function. You can see a more basic example here . The trick in this case is to apply criteria to the FILTER function to only allow values based on the count of occurrence. Working from the inside out, this is done with COUNTIF and the...

[![Excel formula: FILTER to show duplicate values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20to%20show%20duplicate%20values.png "Excel formula: FILTER to show duplicate values")](https://exceljet.net/formulas/filter-to-show-duplicate-values)

### [FILTER to show duplicate values](https://exceljet.net/formulas/filter-to-show-duplicate-values)

In this example, the goal is to list and count values that are duplicated in a set of data at least n times, where n is provided as a variable in cell D5. All data is in the named range data (B5:B16). In the worksheet shown, the formula used in cell F5 is: =UNIQUE(FILTER(data,COUNTIF(data,data)...

[![Excel formula: 10 most common text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/10%20most%20common%20text%20values.png "Excel formula: 10 most common text values")](https://exceljet.net/formulas/10-most-common-text-values)

### [10 most common text values](https://exceljet.net/formulas/10-most-common-text-values)

In this example, the goal is to list the 10 most frequently occurring text values in a range, in descending order by count, as seen in the range in E5:F14. This is an advanced formula that requires a number of nested functions. However, it is an excellent example of the power of dynamic array...

COUNTIF function videos
-----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/List%20duplicate%20values%20with%20FILTER-Play.png)](https://exceljet.net/videos/list-duplicate-values-with-filter)

### [List duplicate values with FILTER](https://exceljet.net/videos/list-duplicate-values-with-filter)

In this video, we'll look at how to list duplicate values. In other words, values that appear more than once in a set of data. In this worksheet, we have a list of the Wimbledon Men's Singles Champions since 1968, in a table called "data". How can we list names that appear more than once, along...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Formulas%20to%20query%20a%20table-Thumb.png)](https://exceljet.net/videos/formulas-to-query-a-table)

### [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)

In this video, we'll look at some formulas you can use to query a table. Because tables support structured references, you can learn a lot about a table with basic formulas. On this sheet, Table1 contains employee data. Let's run through some examples. To start off, you can use the ROWS function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20find%20missing%20values%20with%20COUNTIF-Thumb.png)](https://exceljet.net/videos/how-to-find-missing-values-with-countif)

### [How to find missing values with COUNTIF](https://exceljet.net/videos/how-to-find-missing-values-with-countif)

In this video we'll take a look at how to use the COUNTIF function to solve a common problem: how to find values in one list that appear in another list. Or, how to find values in a list that don't appear in another list. Let's take a look. In this worksheet, on the left, I have a list of 20 names...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20dynamic%20named%20range%20with%20a%20Table-thumb.png)](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)

### [How to create a dynamic named range with a Table](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)

In this video we'll look at how to create a dynamic named range with a Table. This is the simplest way to create a dynamic named range in Excel. This table contains data for ten properties. I can easily create a named range for this data. For example, I can create a range called "data." Then, using...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Compare%20two%20lists%20and%20highlight%20differences-Thumb.png)](https://exceljet.net/videos/how-to-compare-two-lists-and-highlight-differences)

### [How to compare two lists and highlight differences](https://exceljet.net/videos/how-to-compare-two-lists-and-highlight-differences)

In this video, we'll look at how to compare two lists using conditional formatting. This is a great way to visually highlight missing items in a list. Here we have two lists. Both lists contain the same number of items, but each list is slightly different. We can use conditional formatting with a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/survey%20data%20bar%20chart%20example_Thumb.png)](https://exceljet.net/videos/how-to-plot-survey-data-in-a-bar-chart)

### [How to plot survey data in a bar chart](https://exceljet.net/videos/how-to-plot-survey-data-in-a-bar-chart)

In this video, we'll look at how to plot results from a survey question in an Excel bar chart. Here we have data from a survey we ran recently. We've got around 3900 responses to the question "What version of Excel do you use most?". Let's plot the data in a chart. The first step is to build a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel AVERAGEIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageif.png "Excel AVERAGEIF function")](https://exceljet.net/functions/averageif-function)

### [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)

The Excel AVERAGEIF function calculates the average of numbers in a range that meet supplied criteria. AVERAGEIF criteria can include logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel MINIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_minifs.png "Excel MINIFS function")](https://exceljet.net/functions/minifs-function)

### [MINIFS Function](https://exceljet.net/functions/minifs-function)

The Excel MINIFS function returns the smallest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MINIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers,...

[![Excel MAXIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20maxifs%20function.png "Excel MAXIFS function")](https://exceljet.net/functions/maxifs-function)

### [MAXIFS Function](https://exceljet.net/functions/maxifs-function)

The Excel MAXIFS function returns the largest numeric value in cells that meet multiple conditions, referred to as criteria. To define criteria, MAXIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can apply conditions to cells that contain dates, numbers, and...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [IF with wildcards](https://exceljet.net/formulas/if-with-wildcards)
    
*   [Count cells that contain positive numbers](https://exceljet.net/formulas/count-cells-that-contain-positive-numbers)
    
*   [Data validation require unique number](https://exceljet.net/formulas/data-validation-require-unique-number)
    
*   [Text is greater than number](https://exceljet.net/formulas/text-is-greater-than-number)
    
*   [Minimum value if unique](https://exceljet.net/formulas/minimum-value-if-unique)
    
*   [Count cells not between two numbers](https://exceljet.net/formulas/count-cells-not-between-two-numbers)
    
*   [Data validation exists in list](https://exceljet.net/formulas/data-validation-exists-in-list)
    
*   [10 most common text values](https://exceljet.net/formulas/10-most-common-text-values)
    
*   [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    
*   [Highlight duplicate columns](https://exceljet.net/formulas/highlight-duplicate-columns)
    

### Videos

*   [How to create a dynamic named range with a Table](https://exceljet.net/videos/how-to-create-a-dynamic-named-range-with-a-table)
    
*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    
*   [How to compare two lists and highlight differences](https://exceljet.net/videos/how-to-compare-two-lists-and-highlight-differences)
    
*   [How to find missing values with COUNTIF](https://exceljet.net/videos/how-to-find-missing-values-with-countif)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [How to plot survey data in a bar chart](https://exceljet.net/videos/how-to-plot-survey-data-in-a-bar-chart)
    
*   [Formulas to query a table](https://exceljet.net/videos/formulas-to-query-a-table)
    
*   [List duplicate values with FILTER](https://exceljet.net/videos/list-duplicate-values-with-filter)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    
*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

### Links

*   [Microsoft COUNTIF function documentation](https://support.office.com/en-us/article/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34)
    

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