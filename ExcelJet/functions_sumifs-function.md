# Excel SUMIFS function | Exceljet

**Source:** https://exceljet.net/functions/sumifs-function

---

[Skip to main content](https://exceljet.net/functions/sumifs-function#main-content)

[](https://exceljet.net/functions/sumifs-function#)

*   [Previous](https://exceljet.net/functions/sumif-function)
    
*   [Next](https://exceljet.net/functions/sumproduct-function)
    

Excel 2007

[Math](https://exceljet.net/functions#Math)

SUMIFS Function
===============

by Dave Bruns · Updated 7 Jun 2025

Related functions 
------------------

[SUMIF](https://exceljet.net/functions/sumif-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[MINIFS](https://exceljet.net/functions/minifs-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")

Summary
-------

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Purpose 
--------

Sum cells in a range that meet criteria

Return value 
-------------

The sum of cells that meet all criteria

Syntax
------

    =SUMIFS(sum_range,range1,criteria1,[range2],[criteria2],...)

*   _sum\_range_ - The range to be summed.
*   _range1_ - The first range to evaluate.
*   _criteria1_ - The criteria to use on range1.
*   _range2_ - \[optional\] The second range to evaluate.
*   _criteria2_ - \[optional\] The criteria to use on range2.

Using the SUMIFS function 
--------------------------

The SUMIFS function sums numbers in Excel when they meet one or more specific conditions. SUMIFS is one of Excel's most widely used functions, and you will see it in all kinds of spreadsheets that calculate conditional sums based on dates, text, or numbers. Although a common function, SUMIFS has a unique syntax that splits logical conditions into two parts, making it different from many other Excel functions. As a result, the task of defining criteria in SUMIFS can be a bit tricky. Also note that SUMIFS uses "AND logic". To be included in the final result, all conditions must be TRUE.

### Key features

*   Sums values that meet one or more conditions
*   Each new condition requires a separate _range_ and _criteria_.
*   Works with dates, text, and numbers
*   Supports comparison operators (>, <, <>, =) and wildcards (\*, ?)
*   To be included in the final result, _all conditions must be TRUE_.
*   All _ranges_ must be the same size, or SUMIFS will return a #VALUE! error.
*   Available in all Excel versions since Excel 2007

> Unlike most other Excel functions, SUMIFS requires an actual range for sum/criteria ranges. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula. For details, [see the example below](https://exceljet.net/functions/sumifs-function#array_problem)
> .

### Table of Contents

*   [Syntax](https://exceljet.net/functions/sumifs-function#syntax)
    
*   [Basic Example](https://exceljet.net/functions/sumifs-function#basic_example)
    
*   [Applying Criteria](https://exceljet.net/functions/sumifs-function#applying_criteria)
    
*   [Criteria in another cell](https://exceljet.net/functions/sumifs-function#criteria_in_another_cell)
    
*   [Not equal to](https://exceljet.net/functions/sumifs-function#not_equal_to)
    
*   [Blank cells](https://exceljet.net/functions/sumifs-function#blank_cells)
    
*   [Dates](https://exceljet.net/functions/sumifs-function#dates)
    
*   [Wildcards](https://exceljet.net/functions/sumifs-function#wildcards)
    
*   [OR logic](https://exceljet.net/functions/sumifs-function#or_logic)
    
*   [Summary Table](https://exceljet.net/functions/sumifs-function#summary_table)
    
*   [Array Problem](https://exceljet.net/functions/sumifs-function#array_problem)
    
*   [Limitations](https://exceljet.net/functions/sumifs-function#sumif_limitations)
    
*   [Notes](https://exceljet.net/functions/sumifs-function#notes)
    

### Syntax

The syntax for the SUMIFS function depends on the criteria being evaluated. Each condition is provided with a separate _range_ and _criteria_. The generic syntax for SUMIFS looks like this:

    =SUMIFS(sum_range,range1,criteria1) // 1 condition
    =SUMIFS(sum_range,range1,criteria1,range2,criteria2) // 2 conditions

Note that the _sum\_range_ always comes first. This is the range of cells to sum. Each condition is provided as a pair of range/criteria arguments. The first formula above defines one condition and the second defines two. Additional conditions are defined by additional _range/criteria_ pairs. 

### Basic Example

The worksheet below contains simple order data. We use SUMIFS to perform three calculations:

1.  Sum values where the color is Red.
2.  Sum values where the color is Red and the state is TX.
3.  Sum values where the color is Red, the state is TX, and the total is >20.

The three formulas in I5:I7 look like this:

    =SUMIFS(F5:F16,C5:C16,"red") // Red
    =SUMIFS(F5:F16,C5:C16,"red",D5:D16,"TX") // Red and TX
    =SUMIFS(F5:F16,C5:C16,"red",D5:D16,"TX",F5:F16,">20") // Red and TX and >20
    

![SUMIFS function basic example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumifs_function_basic_example.png "SUMIFS function basic example")

There are a few things worth noting in the formulas above:

*   An equal sign (=) is not needed with "is equal to" _criteria (i.e. use "red" not "=red")._
*   SUMIFS is not case-sensitive, so "red" and "Red" will return the same results.
*   Numbers must appear in quotes ("") when used with operators (i.e. ">20").
*   SUMIFS always uses "AND logic". All conditions must be true.

> Note that the syntax for the _criteria_ argument in SUMIFS is somewhat unusual in Excel. Instead of simply entering >20 as the criteria, you must enter ">20" in double quotes.  If you don't quote values as required, _Excel will not let you enter the formula_. See below for more examples of this syntax.

### Applying Criteria

The SUMIFS function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. The tricky part is the syntax needed to apply the criteria. This is because SUMIFS is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
 that split logical criteria into two parts: _range_ and _criteria_. Because of this design, operators must be enclosed in double quotes (""). The table below shows the syntax required for a variety of criteria:

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
 with the ampersand (&) character. Any time you use a value from another cell or the result of a formula with a logical operator like "<", you must concatenate. This is because Excel needs to evaluate cell references and formulas first before the value can used with an operator.

### Criteria in another cell

It is often convenient to put criteria in another cell and then refer to this cell inside your formula. This makes it easy to change criteria later without editing the original formula. For example, you can sum cells in a range equal to the value in A1 like this:

    =SUMIFS(sum_range,range,A1)

When a condition requires an operator, you must [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the cell reference to the operator. For example, to sum cells in a range greater than A1, use a formula like this:

    =SUMIFS(sum_range,range,">"&A1)

Note we are joining the ">" operator to cell A1 with an ampersand (&) character. In the worksheet below, SUMIFS has been configured to return the sum of all sales over the value in G4. Notice the greater than operator (>), which is text, must be enclosed in quotes. The formula in G5 is:

    =SUMIFS(D5:D9,D5:D9,">"&G4) // sum if greater than G4

![SUMIFS function example of criteria in another cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumifs_function_criteria_in_another_cell_example.png "SUMIFS function example of criteria in another cell")

> Don't enclose cell references in double quotes like "A1". Doing so will convert them to text.

### Not equal to

To express "not equal to" criteria, use the "<>" operator surrounded by double quotes (""). For example, use "<>red" for "not red", and "<>blue" for "not blue", as seen in the worksheet below:

![SUMIFS function not equal to example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumifs_function_not_equal_to_example.png "SUMIFS function not equal to example")

    =SUMIFS(C5:C9,B5:B9,"<>red") // not red
    =SUMIFS(C5:C9,B5:B9,"<>blue") // not blue
    =SUMIFS(C5:C9,B5:B9,"<>"&E7) // not E7
    

Note the following:

*   In the last formula, we use E7 directly, so we need to concatenate like "<>"&E7.
*   Do not use quotes around the cell reference.
*   SUMIFS is _not_ case-sensitive, so "red", "RED", and "Red" will return the same result.

### Blank cells

SUMIFS can calculate sums based on whether cells are blank or not blank. Use an empty string ("") to target _blank cells_ and the "not equal to" operator ("<>") to target cells that are _not blank_. In the worksheet below, SUMIFS is used to sum the amounts in column C depending on whether column D contains "x" or is empty:

![SUMIFS function with blank and not blank cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumifs_function_blank_and_not_blank_example.png "SUMIFS function with blank and not blank cells")

    =SUMIFS(C5:C9,D5:D9,"") // blank
    =SUMIFS(C5:C9,D5:D9,"<>") // not blank
    

In the second formula, any value in a cell will cause SUMIFS to sum the amount. To be more precise, you can use a formula like this that sums values only when column D contains an "x":

    =SUMIFS(C5:C9,D5:D9,"x")

### Dates

In Excel, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
, so you can use operators like <,>, <=, >= with dates like any other number. The tricky part about using dates in SUMIFS conditions is entering the dates in a way that Excel will understand. The most reliable way to do this is to refer to a valid date in another cell or use the [DATE function](https://exceljet.net/functions/date-function)
. The example below shows both methods:

![SUMIFS function date example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumifs_function_date_example.png "SUMIFS function date example")

The formulas in F5:F8 are as follows:

    =SUMIFS(C5:C12,B5:B12,"<"&DATE(2024,3,1))
    =SUMIFS(C5:C12,B5:B12,">="&DATE(2024,3,31))
    =SUMIFS(C5:C12,B5:B12,">"&E10)
    =SUMIFS(C5:C12,B5:B12,">="&DATE(2024,5,1),B5:B12,"<="&DATE(2024,5,31))

Note the following:

*   When using a cell reference, you must concatenate the reference to an operator like ">"&E10.
*   In general, it's best to avoid hardcoding a date into a formula and refer to a date in another cell instead.
*   Referring to a date in another cell makes it easy to change the date without editing the formula.

> Pro tip: Avoid hard-coding a date into a formula. Instead, put the date in a cell, then reference that cell in your formula. This makes the worksheet more useful since you can easily see the date being used and change the date when needed without editing the formula.

### Wildcards

The SUMIFS function supports three [wildcards](https://exceljet.net/glossary/wildcard)
 you can use in criteria:

*   Asterisk (\*) - match zero or more characters
*   Question mark (?) - match any one character
*   Tilde (~) - an escape character to match a _literal_ wildcard

The worksheet below shows how wildcards can be used with the SUMIFS function. The formulas in F5:F8 apply the criteria described in column E.

    =SUMIFS(C5:C11,B5:B11,"mi*") // begins with "mi"
    =SUMIFS(C5:C11,B5:B11,"*ota") // ends with "ota"
    =SUMIFS(C5:C11,B5:B11,"????") // contains 4 characters
    =SUMIFS(C5:C11,B5:B11,"*~?") // ends with "?"
    

![SUMIFS function wildcard example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumif_function_wildcard_example_0.png "SUMIFS function wildcard example")

Note the last formula in F8 uses "\*~?" to match a question mark (?) that occurs at the end of "Montana?" in cell C10. The tilde (~) is an escape character that allows you to find a _literal_ wildcard. To match a question mark (?), use "~?"; to match an asterisk(\*), use "~\*"; and to match a tilde (~), use "~~". The table below shows more examples of how wildcards can be used:

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

The SUMIFS function is designed to apply multiple conditions with "AND logic," so there is no obvious way to sum cells with "OR logic". However, one workaround is to provide the _criteria_ as an [array constant](https://exceljet.net/glossary/array-constant)
 like {"red","blue}, and then nest the SUMIFS formula inside the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(SUMIFS(sum_range,range,{"red","blue"})) // red or blue
    

The formula above will sum cells in _sum\_range_ when cells in _range_ contain "red" or "blue". Essentially, SUMIFS returns _two_ sums, one for "red" and one for "blue", and the SUM function returns the sum of the sums. For more details, [see this example](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)
.

### Summary Table

You can use SUMIFS to create a simple summary table. In the worksheet below, we have a list of unique colors in F5:F9. The goal is to subtotal the amounts in column D by color. The formula in cell G5, copied down, is:

    =SUMIFS($D$5:$D$16,$C$5:$C$16,F5)

![SUMIFS function summary table example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumif_function_summary_table_example_0.png "SUMIFS function summary table example")

Notice that the _range_ and the _sum\_range_ are locked as [absolute references](https://exceljet.net/glossary/absolute-reference)
 to prevent changes as the formula is copied down the column. If you are using Excel 2021 or later, you can generate all totals at once with a [dynamic array formula](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 like this:

    =SUMIFS(D5:D16,C5:C16,F5:F9)

We don't need the absolute references in this case because a single formula creates all results. You can go one step further by using the [UNIQUE function](https://exceljet.net/functions/unique-function)
 in cell F5 to get a list of unique colors, then referring to the [spill range](https://exceljet.net/glossary/spill-range)
 directly like this:

    =SUMIFS(D5:D16,C5:C16,F5#)

> In Excel 365, you can also use the new [GROUPBY function](https://exceljet.net/functions/groupby-function)
>  to create a summary table.

### Array Problem

_Note: For more advanced use cases, this is an important limitation in what SUMIFS can do._

One of the more tricky limitations of SUMIFS is that it won't allow an _array_ for a _range_ argument. To understand the problem, consider the worksheet below, where we have 12 dates in column B and 12 amounts in column C. The goal is to create a formula to sum the amounts by year. We can do that with the following SUMIFS formula:

    =SUMIFS(C5:C16,B5:B16,">="&DATE(E5,1,1),B5:B16,"<="&DATE(E5,12,31))

_Note: I would normally use absolute references for the two ranges so that the formula can be copied down without changes, but I have left the addresses relative here so they are easier to read._

![SUMIFS function array problem example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumifs_function_array_problem_example.png "SUMIFS function array problem example")

This formula works fine, but it's a little complicated. If you have some experience with Excel formulas, you might think you can use SUMIFS and YEAR together in a clever formula like this:

    =SUMIFS(C5:C16,YEAR(B5:B16),E5)

The idea is to extract the year from the dates in column B with the [YEAR function](https://exceljet.net/functions/year-function)
, and then use 2024 (in cell E5) for the criteria. This would be cool if it worked. However, Excel won't even let you enter this formula. If you try, you'll get a generic "There's a problem with your formula" error:

![SUMIFS function array problem example 2](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumifs_function_array_problem_example2.png "SUMIFS function array problem example 2")

The problem is that SUMIFS _requires_ a proper range for the range argument, but YEAR(B5:B16) will return an array like this:

    {2024;2024;2024;2024;2024;2025;2025;2025;2025;2025;2025;2025}

To be clear, using YEAR like this works fine in most other formulas. However, SUMIFS is not programmed to handle arrays, so it won't work. How can we work around this problem? One nice alternative is to switch to the SUMPRODUCT function and use a formula like this:

    =SUMPRODUCT(sum_range,--(range=criteria))

If we modify the pattern above to fit the workbook example, we get the following:

    =SUMPRODUCT(C5:C16,--(YEAR(B5:B16)=E5))

This formula is quite a bit simpler than the SUMIFS formula above. It's a good example of how SUMPRODUCT can often solve a tricky problem in a clever and elegant formula.

> Remember: If you try to provide an array for a range, you won't be able to enter the formula because Excel will display a "There's a problem with your formula" error dialog. The "array problem" is not mentioned explicitly.

### Limitations

The SUMIFS function has several limitations you should be aware of:

*   Conditions in SUMIFS are joined by AND logic. In other words, all conditions must be TRUE in order for a cell to be included in a sum. To sum cells with OR logic, you can use [a workaround](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)
     in simple cases.
*   All ranges must be the same size. If you supply ranges that don't match, you'll get a #VALUE error. [See example here](https://exceljet.net/formulas/sum-if-multiple-columns)
    .
*   The SUMIFS function requires actual _ranges_ for all range arguments; you can't use an [array](https://exceljet.net/glossary/array)
    . This means you can't do things like [extract the year from dates](https://exceljet.net/formulas/sum-by-year)
     inside the SUMIFS function. To alter values that appear in a _range_ argument before applying criteria, the SUMPRODUCT function is a flexible solution.
*   SUMIFS is not case-sensitive. To sum values based on a case-sensitive condition, you can use a formula based on the SUMPRODUCT function with the [EXACT function](https://exceljet.net/functions/exact-function)
    .
*   If you reference a range in an external workbook, SUMIFS requires that the workbook be open to calculate a result. If the external workbook is not open, you will see a #VALUE! error. As a workaround, you can switch to the SUMPRODUCT function, which does not have this limitation. The syntax will look like this: =SUMPRODUCT(--(criteria\_range1=criteria1), --(criteria\_range2=criteria2) ... , sum\_range). See [this page](https://exceljet.net/functions/sumproduct-function)
     for details.
*   SUMIFS has some other quirks, which are [detailed in this article](https://exceljet.net/articles/excels-racon-functions)
    .

The most common way to work around most of these limitations is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
.

### Notes

*   Multiple conditions are applied using AND logic, i.e., condition 1 _AND_ condition 2, etc.
*   All ranges must be the same size. If you supply ranges that don't match, you'll get a #VALUE error.
*   Non-numeric criteria must be enclosed in double quotes (i.e., "<100",  ">32", "TX").
*   Cell references in criteria are _not_ enclosed in quotes, i.e., "<"&A1
*   The wildcard characters "?" and "\*" can be used in criteria. A question mark (?) matches any one character, and an asterisk (\*) matches any sequence of characters (zero or more).
*   To match a literal question mark(?) or asterisk (\*), use a tilde (~) like (~?, ~\*).
*   SUMIFS requires a [range](https://exceljet.net/glossary/range)
    ; you can't substitute an [array](https://exceljet.net/glossary/array)
    .

SUMIFS function examples
------------------------

[![Excel formula: Sum if date is between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_date_is_between.png "Excel formula: Sum if date is between")](https://exceljet.net/formulas/sum-if-date-is-between)

### [Sum if date is between](https://exceljet.net/formulas/sum-if-date-is-between)

In this example, the goal is to sum amounts in column C when the date in column B is between two given dates. The start date is provided in cell E5, and the end date is provided in cell F5. The date range should be inclusive - both the start date and end date should be included in the final result...

[![Excel formula: Sum by group](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20group.png "Excel formula: Sum by group")](https://exceljet.net/formulas/sum-by-group)

### [Sum by group](https://exceljet.net/formulas/sum-by-group)

In this example, the goal is to sum by group, where each group is represented by a different color: Blue, Red, Green, and Purple. The worksheet shown contains two different approaches. In the range F5:G8, we have created a summary table to summarize counts by color. In column D, we are using a...

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: SUMIFS with horizontal range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20with%20horizontal%20range.png "Excel formula: SUMIFS with horizontal range")](https://exceljet.net/formulas/sumifs-with-horizontal-range)

### [SUMIFS with horizontal range](https://exceljet.net/formulas/sumifs-with-horizontal-range)

Normally, SUMIFS is used with data in a vertical arrangement, but it can also be used in cases where data is arranged horizontally. The trick is to make sure the sum\_range and criteria\_range are the same dimensions. In the example shown, the formula in cell I5, copied down the column is: =SUMIFS(B5...

[![Excel formula: Sum if one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_one_of_many_things.png "Excel formula: Sum if one of many things")](https://exceljet.net/formulas/sum-if-one-of-many-things)

### [Sum if one of many things](https://exceljet.net/formulas/sum-if-one-of-many-things)

In this example, the goal is to sum the numbers in column E when the item in column B appears in the range G5:G7. The named range things is not required. It is used only for convenience and can be expanded as needed to include additional criteria. The article below explains several ways to solve...

[![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")](https://exceljet.net/formulas/sum-by-week)

### [Sum by week](https://exceljet.net/formulas/sum-by-week)

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named data in the range B5:C16. This problem can be solved in a straightforward way with the SUMIFS function . In the current version of...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum if date is greater than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_date_is_greater_than.png "Excel formula: Sum if date is greater than")](https://exceljet.net/formulas/sum-if-date-is-greater-than)

### [Sum if date is greater than](https://exceljet.net/formulas/sum-if-date-is-greater-than)

In this example, the goal is to sum amounts C5:C16 when the date in B5:B16 is greater than the date provided in cell E5. A good way to solve this problem is with the SUMIFS function . Note: for SUMIFS to work correctly, the worksheet must use valid Excel dates . All dates in Excel have a numeric...

[![Excel formula: Sum if cells are not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_not_equal_to.png "Excel formula: Sum if cells are not equal to")](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

### [Sum if cells are not equal to](https://exceljet.net/formulas/sum-if-cells-are-not-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when corresponding cells in the range C5:C15 are not equal to "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only one criteria...

[![Excel formula: Sum last 30 days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_last_30_days.png "Excel formula: Sum last 30 days")](https://exceljet.net/formulas/sum-last-30-days)

### [Sum last 30 days](https://exceljet.net/formulas/sum-last-30-days)

In this example, the goal is to calculate total amounts in column C that occur in the last 30 days, based on a current date of December 30, 2022. There are three basic approaches to solving this problem: (1) a traditional approach based on the SUMIFS function , (2) a more flexible approach that...

[![Excel formula: Sum if cells contain both x and y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_both_x_and_y.png "Excel formula: Sum if cells contain both x and y")](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y)

### [Sum if cells contain both x and y](https://exceljet.net/formulas/sum-if-cells-contain-both-x-and-y)

In this example, the goal is to sum the numbers in column C when the text in column B contains specific pairs of colors. For example, the formula should sum a number when the text contains both "red" and "blue". Order is not important; the two colors can appear anywhere in the cell. However, both...

[![Excel formula: SUMIFS with Excel Table](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMIFS%20with%20Excel%20Table.png "Excel formula: SUMIFS with Excel Table")](https://exceljet.net/formulas/sumifs-with-excel-table)

### [SUMIFS with Excel Table](https://exceljet.net/formulas/sumifs-with-excel-table)

This formula uses structured references to feed table ranges into the SUMIFS function. The sum range is provided as Table1\[Total\] , the criteria range is provided as Table1\[Item\] , and criteria comes from values in column I. The formula in I5 is: =SUMIFS(Table1\[Total\],Table1\[Item\],H5) which...

[![Excel formula: Sum time over 30 minutes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20over%2030%20minutes.png "Excel formula: Sum time over 30 minutes")](https://exceljet.net/formulas/sum-time-over-30-minutes)

### [Sum time over 30 minutes](https://exceljet.net/formulas/sum-time-over-30-minutes)

This formula uses the SUMPRODUCT function to sum the result of two expressions that yield arrays. The goal is to sum only time greater than 30 minutes, the "surplus" or "extra" time. The first expression subtracts 30 minutes from every time in the named range "times": times-TIME(0,30,0) This...

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

[![Excel formula: Sum time with SUMIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20with%20SUMIFS%20v2.png "Excel formula: Sum time with SUMIFS")](https://exceljet.net/formulas/sum-time-with-sumifs)

### [Sum time with SUMIFS](https://exceljet.net/formulas/sum-time-with-sumifs)

Excel times are numbers and can be summed like other numeric values. In this example, F4:G7 is a summary table, showing the total time logged in each of three states: Standby, Run, and Offline. These values are hardcoded in the range F5:F7. To sum time conditionally by each state, we are using the...

SUMIFS function videos
----------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20SUMIFS%20with%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

### [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)

In this video, we'll look at how to use the SUMIFS function with an Excel Table. On this worksheet, I have two identical sets of order data. I'm going to walk through the process of constructing a summary of sales by item for both sets of data. With the data on the left, I'll use standard formulas...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20a%20pivot%20chart-thumb.png)](https://exceljet.net/videos/what-is-a-pivot-chart)

### [What is a pivot chart](https://exceljet.net/videos/what-is-a-pivot-chart)

In this video, we'll introduce Pivot Charts. Pivot charts let you rapidly analyze large amounts of unsummarized data in different ways. Unlike normal charts, Pivot charts can be used to plot data with hundreds or thousands of rows. For example, on this worksheet, I have order data from a wholesale...

Related functions
-----------------

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

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

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)
    
*   [Sum by week](https://exceljet.net/formulas/sum-by-week)
    
*   [SUMIFS multiple criteria lookup in table](https://exceljet.net/formulas/sumifs-multiple-criteria-lookup-in-table)
    
*   [Sum if cells contain an asterisk](https://exceljet.net/formulas/sum-if-cells-contain-an-asterisk)
    
*   [Sum if greater than](https://exceljet.net/formulas/sum-if-greater-than)
    
*   [Sum if date is between](https://exceljet.net/formulas/sum-if-date-is-between)
    
*   [Sum if ends with](https://exceljet.net/formulas/sum-if-ends-with)
    
*   [Forecast vs actual variance](https://exceljet.net/formulas/forecast-vs-actual-variance)
    
*   [Sum if one of many things](https://exceljet.net/formulas/sum-if-one-of-many-things)
    
*   [Sum if less than](https://exceljet.net/formulas/sum-if-less-than)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [What is a pivot chart](https://exceljet.net/videos/what-is-a-pivot-chart)
    
*   [How to use SUMIFS with an Excel Table](https://exceljet.net/videos/how-to-use-sumifs-with-an-excel-table)
    

### Functions

*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [AVERAGEIF Function](https://exceljet.net/functions/averageif-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    
*   [MINIFS Function](https://exceljet.net/functions/minifs-function)
    
*   [MAXIFS Function](https://exceljet.net/functions/maxifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

### Links

*   [Microsoft SUMIFS function documentation](https://support.office.com/en-us/article/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b)
    

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