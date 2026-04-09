# Excel SUMIF function | Exceljet

**Source:** https://exceljet.net/functions/sumif-function

---

[Skip to main content](https://exceljet.net/functions/sumif-function#main-content)

[](https://exceljet.net/functions/sumif-function#)

*   [Previous](https://exceljet.net/functions/sum-function)
    
*   [Next](https://exceljet.net/functions/sumifs-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SUMIF Function
==============

by Dave Bruns · Updated 2 Jun 2025

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[AVERAGEIF](https://exceljet.net/functions/averageif-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

[MINIFS](https://exceljet.net/functions/minifs-function)

[MAXIFS](https://exceljet.net/functions/maxifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")

Summary
-------

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching.

Purpose 
--------

Sum cells in a range that meet criteria

Return value 
-------------

The sum of matching cells

Syntax
------

    =SUMIF(range,criteria,[sum_range])

*   _range_ - Range to apply criteria to.
*   _criteria_ - Criteria to apply.
*   _sum\_range_ - \[optional\] Range to sum. If omitted, cells in range are summed.

Using the SUMIF function 
-------------------------

The SUMIF function adds up numbers in Excel when they meet a specific condition. It's one of Excel's most widely used functions, and you will find it in all kinds of spreadsheets that calculate conditional sums based on dates, text, or numbers. While powerful, SUMIF has a unique syntax that splits logical conditions into two parts, making it different from many other Excel functions. This syntax takes a little getting used to. SUMIF can only apply _one condition_. For multiple conditions, use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
.

### Key features

*   Sums values that meet a single condition
*   Works with dates, text, and numbers
*   Supports comparison operators (>, <, <>, =) and wildcards (\*, ?)
*   Available in all Excel versions

> Unlike most other Excel functions, SUMIF requires an actual range for the _range_ argument. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula. For details, [see the example below](https://exceljet.net/functions/sumif-function#array_problem)
> .

### Table of Contents

*   [Basic Example](https://exceljet.net/functions/sumif-function#basic_example)
    
*   [Applying Criteria](https://exceljet.net/functions/sumif-function#applying_criteria)
    
*   [Criteria in another cell](https://exceljet.net/functions/sumif-function#criteria_in_another_cell)
    
*   [Not equal to](https://exceljet.net/functions/sumif-function#not_equal_to)
    
*   [Blank cells](https://exceljet.net/functions/sumif-function#blank_cells)
    
*   [Dates](https://exceljet.net/functions/sumif-function#dates)
    
*   [Wildcards](https://exceljet.net/functions/sumif-function#wildcards)
    
*   [OR logic](https://exceljet.net/functions/sumif-function#or_logic)
    
*   [Summary Table](https://exceljet.net/functions/sumif-function#summary_table)
    
*   [Array Problem](https://exceljet.net/functions/sumif-function#array_problem)
    
*   [Limitations](https://exceljet.net/functions/sumif-function#sumif_limitations)
    
*   [Notes](https://exceljet.net/functions/sumif-function#notes)
    

### Basic Example

The generic syntax for SUMIF looks like this:

    =SUMIF(range,criteria,[sum_range])

The _criteria_ is applied to cells in the _range_. When cells meet the criteria, corresponding cells in the _sum\_range_ are summed. The _sum\_range_ is optional. If _sum\_range_ is omitted, the cells in _range_ are summed instead. In the worksheet below, we have a small amount of sales data. We use SUMIF to perform three calculations: (1) sum all sales by Jim, (2) sum all sales in CA (California), and (3) sum all sales over $100. The formulas in G5:G7 look like this:

    =SUMIF(B5:B14,"jim",D5:D14) // sum sales by Jim
    =SUMIF(C5:C14,"ca",D5:D14) // sum sales in CA
    =SUMIF(D5:D14,">100") // sum sales over 100

![SUMIF function basic example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumif_function_basic_example.png "SUMIF function basic example")

Note the following about the formulas above:

*   An equal sign (=) is not needed with "is equal to" _criteria (i.e. use "jim" not "=jim")._
*   SUMIF is not case-sensitive, so "jim" and "Jim" will return the same results.
*   The last formula in G7 does not provide a _sum\_range_, so _range_ is summed instead.
*   Numbers must appear in quotes ("") when used with operators (i.e. ">100").

> Note that the syntax for the _criteria_ argument in SUMIF is somewhat unusual in Excel. Instead of simply entering >100 as the criteria, you must enter ">100" in double quotes.  If you don't quote values as required, Excel will not let you enter the formula. See below for more examples of this syntax.

### Applying Criteria

The SUMIF function supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. The tricky part about using the SUMIF function is the syntax needed to apply criteria. This is because SUMIF is in a group of [eight functions](https://exceljet.net/articles/excels-racon-functions)
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
 with the ampersand (&) character. Any time you use a value from another cell or the result of a formula with a logical operator like "<", you must concatenate. This is because Excel needs to evaluate cell references and formulas first before the value can be used with an operator.

### Criteria in another cell

A great way to use SUMIF is to put criteria in another cell and then refer to this cell inside your formula. This makes it easy to change criteria later without editing the original formula. For example, you can sum cells in a range equal to the value in A1 like this:

    =SUMIF(range,A1)

If you want to include an operator in the criteria, you will need to [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the cell reference to the operator. For example, to sum cells in a range that are greater than A1, use a formula like this:

    =SUMIF(range,">"&A1)

Note we are joining the ">" operator to cell A1 with an ampersand (&) character. In the worksheet below, SUMIF has been configured to return the sum of all sales over the value in G4. Notice the greater than operator (>), which is text, must be enclosed in quotes. The formula in G5 is:

    =SUMIF(D5:D9,">"&G4) // sum if greater than G4
    

![SUMIF with variable criteria](https://exceljet.net/sites/default/files/images/functions/inline/sumif%20with%20variable%20criteria.png "SUMIF with variable criteria")

> Don't enclose cell references in double quotes like "A1". Doing so will convert them to text.

### Not equal to

To express "not equal to" criteria, use the "<>" [operator](https://exceljet.net/glossary/logical-operators)
 surrounded by double quotes (""). For example, use "<>red" for "not red", and "<>blue" for "not blue", as seen in the worksheet below:

![SUMIF not equal to criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumif%20not%20equal%20to.png?itok=9Lx94s7w "SUMIF not equal to criteria")

    =SUMIF(B5:B9,"<>red",C5:C9) // not equal to "red"
    =SUMIF(B5:B9,"<>blue",C5:C9) // not equal to "blue"
    =SUMIF(B5:B9,"<>"&E7,C5:C9) // not equal to E7
    

Note the following:

*   In the last formula, we use E7 directly, so we need to concatenate like "<>"&E7.
*   Do not use quotes around the cell reference.
*   SUMIF is _not_ case-sensitive, so "red", "RED", and "Red" will return the same result.

### Blank cells

SUMIF can calculate sums based on whether cells are blank or not blank. Use an empty string ("") to target _blank cells_ and the "not equal to" operator ("<>") to target cells that are _not blank_. In the worksheet below, SUMIF is used to sum the amounts in column C depending on whether column D contains "x" or is empty:

![SUMIF blank and not blank](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/SUMIF%20blank%20and%20not%20blank.png?itok=p6zqi3pn "SUMIF blank and not blank")

    =SUMIF(D5:D9,"",C5:C9) // blank
    =SUMIF(D5:D9,"<>",C5:C9) // not blank
    

To be more precise, you can use a formula like this that sums values only when column D contains an "x":

    =SUMIF(D5:D9,"x",C5:C9) // contains "x"
    

### Dates

In Excel, [dates are large serial numbers](https://exceljet.net/glossary/excel-date)
, so you can use operators like <,>, <=, >= with dates like any other number. The tricky part about using dates in SUMIF conditions is entering the dates in a way that Excel will understand. The most reliable way to do this is to refer to a [valid date](https://exceljet.net/glossary/excel-date)
 in another cell or use the [DATE function](https://exceljet.net/functions/date-function)
. The example below shows both methods:

![SUMIF with dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/SUMIF%20with%20dates.png?itok=e8LuqYEn "SUMIF with dates")

    =SUMIF(B5:B9,"<"&DATE(2019,3,1),C5:C9)
    =SUMIF(B5:B9,">="&DATE(2019,4,1),C5:C9)
    =SUMIF(B5:B9,">"&E9,C5:C9)
    

Note the following:

*   When using a function with an operator, you must concatenate like "<"&DATE(2019,3,1)
*   When using a cell reference with an operator, you must concatenate like ">"&E9.

> SUMIF can apply only one condition. To target dates _between_ two dates, you'll want to switch to the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
> , which can sum cells based on multiple conditions.

> Pro tip: Avoid hard-coding a date into a formula. Instead, put the date in a cell, then reference that cell in your formula. This makes the worksheet more useful since you can easily see the date being used and change the date when needed without editing the formula.

### Wildcards

The SUMIF function supports three wildcards you can use in criteria for more flexible matching:

*   Asterisk (\*) - match zero or more characters
*   Question mark (?) - match any one character
*   Tilde (~) - an escape character to match a _literal wildcard_

The worksheet below shows how wildcards can be used with the SUMIF function. The formulas in F5:F8 apply the criteria described in column E.

    =SUMIF(B5:B11,"mi*",C5:C11) // begins with "mi"
    =SUMIF(B5:B11,"*ota",C5:C11) // ends with "ota"
    =SUMIF(B5:B11,"????",C5:C11) // contains 4 characters
    =SUMIF(B5:B11,"*~?",C5:C11) // ends with "?"
    

![SUMIF function wildcard example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumif_function_wildcard_example.png "SUMIF function wildcard example")

Note the last formula in F8 uses "\*~?" to match a question mark (?) that occurs at the end of "Montana?" in cell C10. The tilde (~) is an escape character that allows you to find a _literal_ wildcard. To match a question mark (?), use "~?"; to match an asterisk (\*), use "~\*"; and to match a tilde (~), use "~~". The table below shows more examples of how wildcards can be used:

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

> Note: wildcards only work with _text_, not numbers.

### OR logic

The SUMIF function is designed to apply just one condition, so there is no obvious way to sum cells with "this OR that" logic. However, one workaround is to provide the _criteria_ as an [array constant](https://exceljet.net/glossary/array-constant)
 like {"red","blue"}, and then nest the SUMIF formula inside the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(SUMIF(range,{"red","blue"},sum_range)) // red or blue
    

The formula above will sum cells in _sum\_range_ when cells in _range_ contain "red" or "blue". Essentially, SUMIF returns two sums in an array (one for "red" and one for "blue"), and the SUM function returns the sum of the sums. For more details, [see this example](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
.

### Summary Table

You can use SUMIF to create a simple summary table. In the worksheet below, we have a list of unique colors in F5:F9. The goal is to subtotal the amounts in column D by color. The formula in cell G5, copied down, is:

    =SUMIF($C$5:$C$16,F5,$D$5:$D$16)

![SUMIF function summary table example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumif_function_summary_table_example.png "SUMIF function summary table example")

Notice that the _range_ and the _sum\_range_ are locked as [absolute references](https://exceljet.net/glossary/absolute-reference)
 to prevent changes as the formula is copied down the column. If you are using Excel 2021 or later, you can generate all totals at once with a [dynamic array formula](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 like this:

    =SUMIF(C5:C16,F5:F9,D5:D16)

We don't need the absolute references in this case because a single formula creates all results. You can go one step further by using the [UNIQUE function](https://exceljet.net/functions/unique-function)
 in cell F5 to get a list of unique colors, then referring to the [spill range](https://exceljet.net/glossary/spill-range)
 directly like this:

    =SUMIF(C5:C16,F5#,D5:D16)

The advantage of using the spill range is that the sums will update if the list of unique colors changes.

> In Excel 365, you can also use the new [GROUPBY function](https://exceljet.net/functions/groupby-function)
>  to create a summary table.

### Array Problem

_Note: This is an advanced topic, and you don't need to understand it if you are just learning about Excel formulas. For more advanced users, this is an important limitation in how SUMIF works and what it can do._

One of the trickier limitations of SUMIF is that it won't allow an _array_ for a _range_ argument. To understand the problem, consider the worksheet below, where we have 12 dates in column B and 12 amounts in column C. The goal is to create a formula to sum the amounts by year. If you have some experience with Excel formulas, you might think you can use SUMIF and YEAR together in a clever formula like this:

    =SUMIF(YEAR(B5:B16),E5,C5:C16)

The idea is to extract the year from the dates in column B with the [YEAR function](https://exceljet.net/functions/year-function)
 and then use 2024 in cell E5 for the criteria. This would be cool if it worked. However, Excel won't even let you enter this formula. If you try, you'll get a generic "There's a problem with your formula" error.

![SUMIF function array problem error example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumif_array_problem_error_example.png "SUMIF function array problem error example")

The problem is that SUMIF _requires_ a proper range for the range argument, but YEAR(B5:B16) will return an array like this:

    {2024;2024;2024;2024;2024;2025;2025;2025;2025;2025;2025;2025}

To be clear, using YEAR like this works fine in most other formulas. However, SUMIF is not programmed to handle arrays, so it won't work. How can we work around this problem? One nice solution is to switch to the SUMPRODUCT function and use a formula like this:

    =SUMPRODUCT(sum_range,--(range=criteria))

If we adapt the pattern above to the workbook example, we get the following:

    =SUMPRODUCT(C5:C16,--(YEAR(B5:B16)=E5))

![SUMIF function array problem example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumif_array_problem_example.png "SUMIF function array problem example")

_Note: I would normally use absolute references for the two ranges so that the formula can be copied down without changes, but I have left the addresses relative here to make the formula easier to read._

Another option is to switch to the SUMIFS function and use two conditions to capture all dates in a given year with a formula like this:

    =SUMIFS(C5:C16,B5:B16,">="&DATE(E5,1,1),B5:B16,"<="&DATE(E5,12,31))

However, this is undeniably a more complicated formula, and I prefer the SUMPRODUCT option. In fact, this is a good example of how SUMPRODUCT can often solve a tricky problem in a clever and elegant formula.

> Remember: If you try to provide an array for a range, you won't be able to enter the formula because Excel will display a "There's a problem with your formula" error dialog. The "array problem" is not mentioned explicitly.

### Limitations

The SUMIF function has several limitations you should be aware of:

*   SUMIF only supports a single condition. To count cells that meet multiple conditions, use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
    .
*   SUMIF is not case-sensitive. Use the [EXACT function](https://exceljet.net/functions/exact-function)
     with SUMPRODUCT to create a [case-sensitive sum](https://exceljet.net/formulas/sum-if-case-sensitive)
    .
*   SUMIF requires an actual [range](https://exceljet.net/glossary/range)
     for the range argument; you can't provide an array. This means you can't alter values in a range inside your formula before applying criteria. [Read more here](https://exceljet.net/functions/sumif-function#array_problem)
    .
*   If you reference a range in an _external workbook_ with SUMIF, the workbook must be _open,_ or SUMIF will return a #VALUE! error. To workaround this problem, you can switch to the SUMPRODUCT function, which does not have this limitation. The syntax will look like this: =SUMPRODUCT(--(criteria\_range=criteria),sum\_range). See [this page](https://exceljet.net/functions/sumproduct-function)
     for details.
*   SUMIF assumes the _sum\_range_ is the same size as the _range_ and will silently resize the _sum\_range_ when necessary to match the _range_ argument, using the upper left cell in the range as an origin. This can create incorrect results that look "normal". For an example of this problem, [see this article](https://exceljet.net/formulas/sum-if-multiple-columns)
    .
*   SUMIF has other quirks, which are [explained in this article](https://exceljet.net/articles/excels-racon-functions)
    .

The most common way to work around most of these limitations is to use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. However, the latest version of Excel offers powerful alternatives, including [BYROW](https://exceljet.net/functions/byrow-function)
, [BYCOL](https://exceljet.net/functions/bycol-function)
, and [GROUPBY](https://exceljet.net/functions/groupby-function)
.

### Notes

*   SUMIF only supports one condition. Use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
     for multiple criteria.
*   When _sum\_range_ is omitted, the cells in _range_ will be summed.
*   Non-numeric criteria must be enclosed in double quotes (i.e. "<100", ">32", "TX")
*   Cell references in criteria are _not_ enclosed in quotes, i.e. "<"&A1
*   The wildcard characters ? and \* can be used in criteria. A question mark matches any one character and an asterisk matches any sequence of characters (zero or more).
*   To match a literal question mark(?) or asterisk (\*), use a tilde (~) like (~?, ~\*, ~~).
*   SUMIF _requires_ a range; you can't substitute an [array](https://exceljet.net/glossary/array)
    .

SUMIF function examples
-----------------------

[![Excel formula: Sum if cells contain specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_specific_text.png "Excel formula: Sum if cells contain specific text")](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

### [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)

In this example, the goal is to sum the quantities in column C when the text in column B contains "hoodie". The challenge is that the item names ("Hoodie", "Vest", "Hat") are embedded in a text string that also contains size and color. This means we need to apply criteria that looks for a substring...

[![Excel formula: Subtotal by invoice number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/subtotal%20by%20invoice.png "Excel formula: Subtotal by invoice number")](https://exceljet.net/formulas/subtotal-by-invoice-number)

### [Subtotal by invoice number](https://exceljet.net/formulas/subtotal-by-invoice-number)

This formula uses COUNTIF with an expanding range to first check if the current row is the first occurrence of a given invoice number: COUNTIF($B$5:B5,B5)=1 This expression only returns TRUE when this is the first occurrence of a given invoice number. If so, a SUMIF calculation is run: SUMIF($B:$B,...

[![Excel formula: Sum by fiscal year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20fiscal%20year.png "Excel formula: Sum by fiscal year")](https://exceljet.net/formulas/sum-by-fiscal-year)

### [Sum by fiscal year](https://exceljet.net/formulas/sum-by-fiscal-year)

The goal of this example is to sum amounts by fiscal year, when the fiscal year begins in July. The first approach is a self-contained formula based on the SUMPRODUCT function. The second method uses SUMIF with column D as a helper column. Either approach will work correctly, and the best option...

[![Excel formula: Count numbers with leading zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20numbers%20with%20leading%20zeros.png "Excel formula: Count numbers with leading zeros")](https://exceljet.net/formulas/count-numbers-with-leading-zeros)

### [Count numbers with leading zeros](https://exceljet.net/formulas/count-numbers-with-leading-zeros)

In this example, the goal is to count numbers that contain leading zeros. In cell E5, we have the code "009875" and we want to count how many times this code appears in the range B5:B16. The challenge is that Excel can be finicky with leading zeros. Technically, the values in B5:B16 are text , as...

[![Excel formula: Sum if ends with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_end_with.png "Excel formula: Sum if ends with")](https://exceljet.net/formulas/sum-if-ends-with)

### [Sum if ends with](https://exceljet.net/formulas/sum-if-ends-with)

In this example, the goal is to sum the Quantity in C5:C16 when the Item in B5:B16 ends with "small". To solve this problem, you can use either the SUMIFS function or the SUMIF function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIFS and SUMIF...

[![Excel formula: Sum if begins with](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_begins_with.png "Excel formula: Sum if begins with")](https://exceljet.net/formulas/sum-if-begins-with)

### [Sum if begins with](https://exceljet.net/formulas/sum-if-begins-with)

In this example, the goal is to sum the Price in column C when the Product in column B begins with "sha". To solve this problem, you can use either the SUMIF function or the SUMIFS function with the asterisk (\*) wildcard, as explained below. Wildcards Certain Excel functions like SUMIF and SUMIFS...

[![Excel formula: Sum if cells are equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_are_equal_to.png "Excel formula: Sum if cells are equal to")](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

### [Sum if cells are equal to](https://exceljet.net/formulas/sum-if-cells-are-equal-to)

In this example the goal is to sum the numbers in the range F5:F16 when cells in the range C5:C15 contain "Red". To solve this problem, you can use either the SUMIFS function or the SUMIF function . The SUMIF function is an older function that supports only a single condition. SUMIFS on the other...

[![Excel formula: Dropdown sum with all option](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dropdown%20sum%20with%20all%20option.png "Excel formula: Dropdown sum with all option")](https://exceljet.net/formulas/dropdown-sum-with-all-option)

### [Dropdown sum with all option](https://exceljet.net/formulas/dropdown-sum-with-all-option)

The dropdown is set up with a simple data validation rule based on a "list": Red,Blue,Green,All The named ranges "color" (C5:C15) and "qty" (D5:D15) are for convenience only. The formula in G5 performs a conditional sum based on the current dropdown selection in F5. The outermost function is an IF...

[![Excel formula: Subtotal by color](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/subtotal%20by%20color_0.png "Excel formula: Subtotal by color")](https://exceljet.net/formulas/subtotal-by-color)

### [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)

In this example, the goal is to subtotal (count and sum) values based on cell color. This is a tricky problem, because there is no Excel function that will let you count cells by color directly. There are several different approaches, as explained below. Standard formula logic If color is being...

[![Excel formula: Sum across multiple worksheets with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20across%20multiple%20worksheets%20with%20criteria.png "Excel formula: Sum across multiple worksheets with criteria")](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)

### [Sum across multiple worksheets with criteria](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)

In this example, the goal is to sum hours per project across three different worksheets: Sheet1, Sheet2, and Sheet3. The data on each of the three sheets has the same structure as Sheet1, as seen below: 3D reference won't work Before we look at a solution, let's look at something that doesn't work...

[![Excel formula: Sum by group](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20group.png "Excel formula: Sum by group")](https://exceljet.net/formulas/sum-by-group)

### [Sum by group](https://exceljet.net/formulas/sum-by-group)

In this example, the goal is to sum by group, where each group is represented by a different color: Blue, Red, Green, and Purple. The worksheet shown contains two different approaches. In the range F5:G8, we have created a summary table to summarize counts by color. In column D, we are using a...

[![Excel formula: Sum if less than](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_less_than.png "Excel formula: Sum if less than")](https://exceljet.net/formulas/sum-if-less-than)

### [Sum if less than](https://exceljet.net/formulas/sum-if-less-than)

In this example, the goal is to sum values in the range D5:D16 when they are less than the value entered in cell F5. This problem can be easily solved with the SUMIF function or the SUMIFS function. The main challenge in this problem is the syntax needed for cell F5 in the criteria, which involves...

[![Excel formula: Subtotal invoices by age](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Subtotal%20invoices%20by%20age.png "Excel formula: Subtotal invoices by age")](https://exceljet.net/formulas/subtotal-invoices-by-age)

### [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)

In this example, the goal is to subtotal invoices by age, where age represents the number of days since the invoice was issued. This problem can be solved with the SUMIFS function and the COUNTIFS function, as explained below. For convenience, age (E5:E16) and amount (D5:D16) are named ranges ...

[![Excel formula: Sum if cell contains text in another cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_cells_contain_text_in_another_cell.png "Excel formula: Sum if cell contains text in another cell")](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell)

### [Sum if cell contains text in another cell](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell)

In this example, the goal is to sum Amounts in column C by state using the two-letter codes in column E. Note the states are abbreviated, "CA" is California, "FL" is Florida, "TX" is Texas, and "WA" is Washington. The challenge in this case is that the state abbreviations are embedded in a text...

[![Excel formula: Sum time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20time%20with%20a%20formula.png "Excel formula: Sum time")](https://exceljet.net/formulas/sum-time)

### [Sum time](https://exceljet.net/formulas/sum-time)

Dates and times are just numbers in Excel, so you can use them in any normal math operation. However, by default, Excel will only display hours and minutes up to 24 hours. This means you might seem to "lose time" if you are adding up time that is more than 1 day. In this example, the goal is to sum...

SUMIF function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumif-function)

### [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

In this video we'll look at how to use the SUMIF function to sum cells that meet a single criteria. Let's take a look. The SUMIF function sums cells that satisfy a single condition that you supply. It takes three arguments: range, criteria, and sum range. Note that sum range is optional. If you don...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20add%20a%20totals%20row%20to%20a%20Table-Thumb.png)](https://exceljet.net/videos/how-to-add-a-totals-row-to-a-table)

### [How to add a totals row to a Table](https://exceljet.net/videos/how-to-add-a-totals-row-to-a-table)

In this video, we'll look at how to add and configure a Total Row to an Excel Table. All Excel Tables come with a built-in Total Row feature. The total row allows you to easily show summary calculations below a table. You can use this total row to calculate counts, sums, min and max, averages, and...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

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

*   [Sum across multiple worksheets with criteria](https://exceljet.net/formulas/sum-across-multiple-worksheets-with-criteria)
    
*   [Sum by group](https://exceljet.net/formulas/sum-by-group)
    
*   [Sum if date is greater than](https://exceljet.net/formulas/sum-if-date-is-greater-than)
    
*   [Sum if cells contain specific text](https://exceljet.net/formulas/sum-if-cells-contain-specific-text)
    
*   [Sum if cells contain an asterisk](https://exceljet.net/formulas/sum-if-cells-contain-an-asterisk)
    
*   [Count numbers with leading zeros](https://exceljet.net/formulas/count-numbers-with-leading-zeros)
    
*   [Sum if greater than](https://exceljet.net/formulas/sum-if-greater-than)
    
*   [Subtotal by invoice number](https://exceljet.net/formulas/subtotal-by-invoice-number)
    
*   [Sum time](https://exceljet.net/formulas/sum-time)
    
*   [Sum by fiscal year](https://exceljet.net/formulas/sum-by-fiscal-year)
    

### Videos

*   [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [How to add a totals row to a Table](https://exceljet.net/videos/how-to-add-a-totals-row-to-a-table)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
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

*   [Microsoft SUMIF function documentation](https://support.office.com/en-us/article/sumif-function-169b8c99-c05c-4483-a712-1697a653039b)
    

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