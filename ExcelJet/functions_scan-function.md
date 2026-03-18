# Excel SCAN function | Exceljet

**Source:** https://exceljet.net/functions/scan-function

---

[Skip to main content](https://exceljet.net/functions/scan-function#main-content)

[](https://exceljet.net/functions/scan-function#)

*   [Previous](https://exceljet.net/functions/regextest-function)
    
*   [Next](https://exceljet.net/functions/sequence-function)
    

Excel 2024

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

SCAN Function
=============

by Dave Bruns · Updated 1 Nov 2025

Related functions 
------------------

[LAMBDA](https://exceljet.net/functions/lambda-function)

[LET](https://exceljet.net/functions/let-function)

[MAP](https://exceljet.net/functions/map-function)

[SCAN](https://exceljet.net/functions/scan-function)

[REDUCE](https://exceljet.net/functions/reduce-function)

[MAKEARRAY](https://exceljet.net/functions/makearray-function)

[BYCOL](https://exceljet.net/functions/bycol-function)

[BYROW](https://exceljet.net/functions/byrow-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9349/download?token=pqa-o1Zo)
 (67.39 KB)

![Excel SCAN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")

Summary
-------

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other calculations that show intermediate results. 

Purpose 
--------

Scan array and return intermediate results

Return value 
-------------

An array of results

Syntax
------

    =SCAN([initial_value],array,function)

*   _initial\_value_ - \[optional\] The initial value of the accumulator. Default is zero.
*   _array_ - The array to be scanned.
*   _function_ - The function or custom LAMBDA to apply.

Using the SCAN function 
------------------------

The SCAN function applies a custom calculation to each element in a given array and returns an [array](https://exceljet.net/glossary/array)
 that contains each intermediate value created during the scan. SCAN can generate running totals, running counts, and other calculations that create intermediate or incremental results. The results returned by SCAN are the value of an "accumulator" at each step in the process.

Like the [REDUCE function](https://exceljet.net/functions/reduce-function)
, SCAN iterates over all elements in an array and performs a calculation on each element while updating the value of an accumulator. However, while REDUCE returns a _single_ value, SCAN returns an _array_ of values.

### Key features

*   Useful for running totals, running counts, and other "running" results.
*   Returns all intermediate values as an array, not just the final result.
*   Uses a custom LAMBDA function to apply the calculation.
*   Tracks the prior result of a calculation as an "accumulator".
*   Plays nicely with dynamic array formulas (expands with data).

> SCAN returns the value of the accumulator when each element in the array is processed. The result is an array of "intermediate" values. To scan an array and return a single aggregated result, see the [REDUCE function](https://exceljet.net/functions/reduce-function)
> . To process each element in an array individually and return an array of non-intermediate results, see the [MAP function](https://exceljet.net/functions/map-function)

### Table of contents

*   [LAMBDA structure](https://exceljet.net/functions/scan-function#lambda-structure)
    
*   [SCAN for a basic running total](https://exceljet.net/functions/scan-function#scan-for-a-basic-running-total)
    
*   [SCAN with abbreviated function syntax](https://exceljet.net/functions/scan-function#scan-with-abbreviated-function-syntax)
    
*   [SCAN with dynamic range](https://exceljet.net/functions/scan-function#scan-with-dynamic-range)
    
*   [SCAN for YTD calculations](https://exceljet.net/functions/scan-function#scan-for-ytd-calculations)
    
*   [SCAN for conditional running totals](https://exceljet.net/functions/scan-function#scan-for-conditional-running-totals)
    
*   [SCAN for running counts](https://exceljet.net/functions/scan-function#scan-for-running-counts)
    
*   [SCAN with a boolean array](https://exceljet.net/functions/scan-function#scan-with-a-boolean-array)
    
*   [SCAN for a running count by category](https://exceljet.net/functions/scan-function#scan-for-a-running-count-by-category)
    
*   [SCAN with text values](https://exceljet.net/functions/scan-function#scan-with-text-values)
    
*   [SCAN for a running MAX](https://exceljet.net/functions/scan-function#scan-for-a-running-max)
    
*   [SCAN to find the longest winning streak](https://exceljet.net/functions/scan-function#scan-to-find-the-longest-winning-streak)
    
*   [SCAN for compounded interest](https://exceljet.net/functions/scan-function#scan-for-compounded-interest)
    

### LAMBDA structure

The SCAN function takes three arguments: _initial\_value_, _array_, and _function_. _Initial\_value_ is the initial seed value to use for the first result. _Initial\_value_ is optional and defaults to zero (0). _Array_ is the array or range to scan, and _function_ is typically a [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to apply to each value in the _array_. The structure of the LAMBDA used inside SCAN looks like this:

    LAMBDA(a,v,calculation)
    

The first argument, _a_, is the accumulator used to store intermediate values. The accumulator begins as the _initial\_value_ provided to SCAN and changes as the SCAN function loops over the elements in the array and applies a calculation. The _v_ argument is the value of each element in the _array_ at a given iteration. The _calculation_ is a formula that operates on the accumulator (a) and value (v). The result of the calculation defines the value of the accumulator for the next iteration, and the final result is an array that contains all accumulator values created during the scan. For example, in the formula below, SCAN is used to create a running total of an array with three values:

    =SCAN(0,{1,2,3},LAMBDA(a,v,a+v)) // returns {1,3,6}
    

The _initial\_value_ is provided as zero, the _array_ is hard-coded as the array constant {1,2,3}, and the calculation, `LAMBDA(a,v,a+v)`, simply adds the accumulator and value. The table below shows how the accumulator value changes during each iteration when SCAN processes the array {1,2,3} with an initial value of 0. Notice that the accumulator is updated with the result of the calculation at each iteration.

| Iteration | Value (v) | Accumulator (a) | Calculation | Result |
| --- | --- | --- | --- | --- |
| Initial | \-  | 0   | \-  | \-  |
| 1   | 1   | 0   | 0 + 1 | 1   |
| 2   | 2   | 1   | 1 + 2 | 3   |
| 3   | 3   | 3   | 3 + 3 | 6   |

The final result returned by SCAN is the array {1,3,6}, which contains all intermediate values calculated during the scan.

> The SCAN function always assigns the first argument of LAMBDA to the accumulator (a) and the second argument to the current value (v) from the array. This behavior is built into the function's design and cannot be changed. The names _a_ and _v_ are arbitrary, used to represent _accumulator_ and _value_. You can use any names that make sense to you for a given use case.

### SCAN for a basic running total

A simple use of SCAN is to create a running total. In the worksheet shown below, we have a list of values in the range B5:B16, and we want to create a running total of the values in the range. The formula in D5 is:

    =SCAN(0,B5:B16,LAMBDA(a,v,a+v))
    

![SCAN function for basic running total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-basic-running-total.png "SCAN function for basic running total")

The result is a running sum of values in the range B5:B16. All values are returned at the same time in a single array.

### SCAN with abbreviated function syntax

Like other newer dynamic array functions, SCAN supports an abbreviated syntax for the function argument. Using the abbreviated syntax, the formula above can also be written like this:

    =SCAN(0,B5:B16,SUM)
    

![Basic running total with SCAN using abbreviated syntax](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-basic-running-total-abbreviated-syntax.png "Basic running total with SCAN using abbreviated syntax")

It is not obvious, but SCAN is delivering two values, the accumulator and the value to the SUM function at each loop. The result is a running total. While the abbreviated syntax is handy, note that SCAN's iterative behavior means that many of Excel's stock functions won't return useful results. For example, if we try to use SCAN with COUNT on the data above to create a _running count_, the result will always be 2:

    =SCAN(0,B5:B16,COUNT) // returns {2,2,2,2,2,2,2,2,2,2,2,2}
    

To illustrate why this is the case, the table below shows how SCAN processes the first 5 values when using COUNT. At each iteration, COUNT returns the number of numeric values it receives. Since it always receives 2 values (the accumulator and the current value), the result is always 2:

| Iteration | Value (v) | Accumulator (a) | Calculation | Result |
| --- | --- | --- | --- | --- |
| 1   | 8   | 0   | COUNT(0,8) | 2   |
| 2   | 4   | 2   | COUNT(2,4) | 2   |
| 3   | 11  | 2   | COUNT(2,11) | 2   |
| 4   | 8   | 2   | COUNT(2,8) | 2   |
| 5   | 1   | 2   | COUNT(2,1) | 2   |

In general, functions that work well with abbreviated syntax inside of SCAN are those that will operate naturally on two inputs and return useful results (i.e. SUM, MAX, MIN, etc.)

### SCAN with a dynamic range

One of SCAN's key strengths is its ability to work with dynamic arrays. When you give SCAN an _array_ that is dynamically generated, it will automatically adjust the output to match the size of the array as it expands or contracts. You can see an example of this in the screen below, where SCAN has been configured to return a dynamic running total of the values in column B. The formula in cell D5 looks like this:

    =SCAN(0,TRIMRANGE(B5:B1000,2),SUM)

![SCAN function with a dynamic range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-with-dynamic-range.png "SCAN function with a dynamic range")

Notice we are using the abbreviated syntax and calling the SUM function directly. The key feature of this formula, which makes the output dynamic, is the use of the [TRIMRANGE function](https://exceljet.net/functions/trimrange-function)
 to provide the _array_ to SCAN:

    TRIMRANGE(B5:B1000,2)

TRIMRANGE will adjust the starting range of B5:B1000 to match the data it contains by removing empty trailing rows. The resulting "trimmed" range is returned directly to SCAN, which returns running totals to match. As a more concise alternative, you can also use the dot operator instead of TRIMRANGE:

    =SCAN(0,B5:.B1000,SUM) // dot operator syntax

> SCAN also works well with other dynamic ranges in Excel, including values in an [Excel Table](https://exceljet.net/articles/excel-tables)
>  and [spill ranges](https://exceljet.net/glossary/spill-range)
> .

### SCAN for YTD calculations

One common use of SCAN is to create a YTD calculation. In the worksheet shown below, we have a list of months in the range B5:B16, and sales numbers in the range C5:C16. We want to create a YTD calculation of the sales numbers in the range. The formula in E5 is:

    =SCAN(0,C5:C16,LAMBDA(a,v,a+v))
    

![SCAN function for YTD (year to date) calculations](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-ytd-calculations.png "SCAN function for YTD (year to date) calculations")

The result is a list of running YTD totals of the values in C5:C16.

### SCAN for conditional running totals

Because the calculation applied by SCAN is fully customizable, it is possible to apply conditions. In the worksheet shown below, we have a list of numbers in the range B5:B16, and the goal is to create a running total of the odd numbers in the range. The formula in D5 looks like this:

    =SCAN(0,B5:B16,LAMBDA(a,v,IF(ISODD(v),a+v,a)))
    

![SCAN function for conditional running totals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-conditional-running-totals.png "SCAN function for conditional running totals")

Notice we use the [ISODD function](https://exceljet.net/excel-functions/excel-isodd-function)
 inside the [IF function](https://exceljet.net/excel-functions/excel-if-function)
 to check if the value is odd. If it is, the value is added to the accumulator. If it is not, the accumulator is returned unchanged. The result is a list of running totals of the odd numbers in B5:B16.

### SCAN for running counts

SCAN can also be used for running counts. In the worksheet shown below, we have a list of values in the range B5:B16 and the goal is to create a running count of the numbers in the range. The formula in D5 looks like this:

    =SCAN(0,B5:B16,LAMBDA(a,v,a+COUNT(v)))
    

![SCAN function for running counts](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-running-counts.png "SCAN function for running counts")

The COUNT function only counts numbers, so it will return 0 for text values, errors, and empty cells. There are 6 numbers in the range, and the final result is an array like this:

    {1;2;2;3;3;4;4;5;5;6;6;6}
    

Notice that the count is only incremented when SCAN encounters a numeric value. Otherwise, the accumulator is returned unchanged. The result is a running count of the numbers in B5:B16. As an alternative to COUNT, you could also use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 to create a running count of numbers:

    =SCAN(0,B5:B16,LAMBDA(a,v,a+ISNUMBER(v)))
    

In a similar way, you could use [ISBLANK](https://exceljet.net/functions/isblank-function)
 to count blanks, [ISTEXT](https://exceljet.net/functions/istext-function)
 to count text values, [ISERROR](https://exceljet.net/functions/iserror-function)
 to count errors, and so on.

### SCAN with a Boolean array

Sometimes it makes sense to perform a Boolean operation on an array and then use the SCAN function to iterate over the result instead of working with the source array. A good example of this is when you want to perform a conditional running count and suppress redundant counts. You can see an example of this in the worksheet below, we have a list of colors in B5:B16, and the goal is to return a running count for the appearance of the color "blue", but for other colors, we want the result to be blank. The formula in D5 looks like this:

    =LET(
        hits,B5:B16="Blue",
        counts,SCAN(0,hits,LAMBDA(a,v,a+v)),
        IF(hits,counts,"")
    )
    

![SCAN function for a conditional count using a boolean array](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-conditional-count-with-boolean-array.png "SCAN function for a conditional count using a boolean array")

To make the formula more readable and efficient, we use the LET function. First, we create a Boolean array representing the values in B5:B16 that are equal to "blue" using the expression `B5:B16="Blue"`. The result of this operation is an array like this:

    {FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;FALSE;TRUE;FALSE}
    

Notice that TRUE values correspond to the color "blue" in column B. All other values are FALSE. We assign this array to the variable _hits_. Next, we use the SCAN function to iterate over the _hits_ array and create a running count of TRUE values:

    =SCAN(0,hits,LAMBDA(a,v,a+v))
    

The math operation of `a+v` will automatically coerce the TRUE values to 1 and the FALSE values to 0, so that the accumulator is incremented by 1 for each TRUE value. The resulting array looks like this:

    {0;1;0;0;1;0;1;1;0;0;1;0}
    

The resulting array is assigned to the variable counts. Finally, we use the IF function to filter out unwanted counts:

    =IF(hits,counts,"")
    

When hits are TRUE, we return the count; otherwise, we return an empty string (""). The final result is a running count of "Blue" with redundant counts suppressed.

> Note: this same approach could be used in the previous example to create a running count of numbers without redundant counts.

### SCAN for a running count by category

The SCAN function can also be used to create a running count by category. In the worksheet below, we have a list of categories ("A", "B", "C") in the range B5:B16, and the goal is to create a running count for each category. The formula in D5 looks like this:

    =LET(
        groups,B5:B16,
        changes,IF(groups<>VSTACK("",DROP(groups, -1)),1,0),
        SCAN(0,changes,LAMBDA(a,v,IF(v=1,1,a+1)))
    )
    

![SCAN function for a running count by category](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-running-count-by-category.png "SCAN function for a running count by category")

This is a case where we need to create an intermediate array of changes before we can use the scan function. First, we define the variable `groups` to equal the range B5:B16. Then we set the variable `changes` to equal the result of this calculation:

    IF(groups<>VSTACK("", DROP(groups, -1)), 1, 0)
    

The formula above uses VSTACK to add an empty string ("") at the beginning of the array, and DROP to remove the last value from the original array. This creates an array that is offset by one position, which allows us to compare each value with the previous value. For example, if the original array is {A,A,A,B,B,C,C}, after using VSTACK and DROP, we get:

| Original | Offset | Different? |
| --- | --- | --- |
| A   | ""  | 1   |
| A   | A   | 0   |
| A   | A   | 0   |
| B   | A   | 1   |
| B   | B   | 0   |
| C   | B   | 1   |
| C   | C   | 0   |

The IF function then compares these arrays and returns 1 when values are different (indicating a category change) and 0 when they are the same (indicating we're still in the same category). The result is the array below, which is assigned to the variable `changes`:

    {1;0;0;0;1;0;0;0;1;0;0;0}
    

Finally, SCAN processes this array of changes. When it encounters a 1 (indicating a category change), it resets the counter to 1. When it encounters a 0 (indicating we're still in the same category), it increments the previous count by 1. The result is a running count within each category.

### SCAN with text values

SCAN can also be used to concatenate text values. To work with text values, set the _initial\_value_ to an empty string (""). The formula below creates a running concatenation of an array:

    =SCAN("",{"a","b","c"},LAMBDA(a,v,a&v)) // returns {"a","ab","abc"}
    

You can see an example of this approach in the worksheet below, where we have text in column B and the formula in column D is

    =SCAN("",B5:B16,LAMBDA(a,v,a&v))
    

![SCAN function with text values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-text-values.png "SCAN function with text values")

The result is a running concatenation of the text values in column B as seen in the worksheet above.

Note: let me know if you run into a good use case for SCAN with text values.

### SCAN for a running MAX

The SCAN function can also be used to create a running MAX. In the worksheet below, we have a list of values in the range B5:B16 and the goal is to create a running maximum. The formula in D5 looks like this:

    =SCAN(0,B5:B16,MAX)
    

The result is a list of running maximum values. Notice that the max value only changes when SCAN encounters a new maximum value.

![SCAN function for a running MAX](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-running-max.png "SCAN function for a running MAX")

Also, notice that this is a case where the abbreviated syntax for functions inside of SCAN works well, since `MAX(a,v)` works as needed. The equivalent "long form" formula would look like this:

    =SCAN(0,B5:B16,LAMBDA(a,v,MAX(a,v)))
    

To create a running minimum, just replace the MAX function with the MIN function.

> Note: In this example, we have set _initial\_value_ to zero because the values in column B will always be positive. If values could be negative, we need to supply an initial value that is less than or equal to the minimum value in the range. A general form for a running MAX that will work for any input values is: `=SCAN(MIN(range),range,MAX)` Excel power users will also sometimes use `=SCAN(-9.99E+307,range,MAX)`, since -9.99E+307 is the smallest number Excel can represent.

### SCAN to find the longest winning streak

One interesting use of SCAN is to find the longest winning streak. This is traditionally a tricky problem to solve in Excel, but with SCAN, it's fairly straightforward. In the worksheet below, we have a list of dates in column B, and column C contains a "W" or "L" to indicate a win or loss. The goal is to find the longest winning streak, which is 5 consecutive wins in this case. The formula in cell E5 looks like this:

    =MAX(SCAN(0,C5:C16,LAMBDA(a,v,IF(v="w",a+1,0))))
    

![SCAN function to find the longest winning streak](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-longest-winning-streak.png "SCAN function to find the longest winning streak")

Notice the SCAN function is wrapped in the MAX function. Inside SCAN, we use the IF function to increment the accumulator by 1 if the value is "W". Otherwise, we set the accumulator to 0. The result is a running count of consecutive wins. For the data shown above, the result from SCAN is an array like this:

    {0;1;2;0;0;0;1;2;3;4;5;0}
    

This array is then passed to the MAX function, which returns the largest value in the array:

    =MAX({0;1;2;0;0;0;1;2;3;4;5;0}) // returns 5
    

The final result is 5. Without the SCAN function, finding the longest winning streak is a lot more complicated. For a full explanation, see [this article](https://exceljet.net/formulas/longest-winning-streak)
.

### SCAN for compounded interest

The SCAN function can also be used to calculate compounded interest. In the worksheet below, we have variable inputs for starting balance, annual interest rate, and the number of years. The formula in E5 generates a sequence of years with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 like this:

    =SEQUENCE(C7) // returns {1;2;3;4;5;6;7;8;9;10}
    

The formula in F5 uses the SCAN function to calculate compound interest like this:

    =SCAN(C5,E5#,LAMBDA(a,v,a*(1+C6)))
    

![SCAN function for compounded interest](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/scan-function-compounded-interest.png "SCAN function for compounded interest")

The _initial\_value_ is the starting balance in cell C5, the _array_ is the sequence of years, and the _calculation_ is the formula for compound interest. The final result is a list of ending balances for each year. Notice we use the [spill range operator](https://exceljet.net/glossary/spill-range-operator)
 (E5#) to provide an array of years to the SCAN function. This allows the results to expand or contract based on the number of years provided. If we change the number of years in C7 to 15, SEQUENCE will output a list of all 15 years, and the SCAN function will generate a balance for the 5 additional years.

> You can find another more advanced example of the SCAN function here: [Modeling the 4% Retirement Rule in Excel](https://exceljet.net/articles/modeling-the-4-percent-retirement-rule-in-excel)
> .

SCAN function examples
----------------------

[![Excel formula: Mortgage payment schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/mortgage_schedule_with_extra_payment.png "Excel formula: Mortgage payment schedule")](https://exceljet.net/formulas/mortgage-payment-schedule)

### [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)

The goal of this example is to show how to create a mortgage payment schedule using Excel formulas. A mortgage payment schedule is a detailed breakdown of every payment over the life of a loan. Each payment represents one period , typically a month. For each period, the schedule shows how much of...

[![Excel formula: Cash denomination calculator](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cash_denomination_calculator.png "Excel formula: Cash denomination calculator")](https://exceljet.net/formulas/cash-denomination-calculator)

### [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)

In this example, the goal is to build a "cash denomination calculator." A cash denomination calculator is a tool for counting and verifying cash amounts. It can calculate the denominations needed to achieve a certain cash value. It can also perform the reverse calculation and determine the cash...

[![Excel formula: Calculate running total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate%20running%20total.png "Excel formula: Calculate running total")](https://exceljet.net/formulas/calculate-running-total)

### [Calculate running total](https://exceljet.net/formulas/calculate-running-total)

In this example, the goal is to calculate a running total in column D of the worksheet as shown. A running total, or cumulative sum, is a set of partial sums that changes as more data is collected. Each calculation represents the sum of values up to that point. In this example, each calculation...

[![Excel formula: Running count of occurrence in list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/running%20count%20of%20occurrence%20in%20list.png "Excel formula: Running count of occurrence in list")](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

### [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)

In this example, the goal is to create a running count for a specific value that appears in column B. The value to count is entered in cell E5, which is the named range value . The core of the solution explained below is the COUNTIF function , with help from the IF function to suppress a count for...

[![Excel formula: Longest winning streak](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/longest_winning_streak.png "Excel formula: Longest winning streak")](https://exceljet.net/formulas/longest-winning-streak)

### [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)

In this example, the goal is to calculate a count for the longest winning streak in a set of data. In the worksheet shown, wins ("W") and losses ("L") are recorded in column C, so this means we want to count the longest consecutive series of W's. Although we are specifically counting the longest...

[![Excel formula: Count unique dates ignore time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20dates%20ignore%20time.png "Excel formula: Count unique dates ignore time")](https://exceljet.net/formulas/count-unique-dates-ignore-time)

### [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)

In this example, the goal is to count the unique dates in a range of timestamps (i.e. dates that contain dates and times). In addition, we also want to create the table of results seen in E7:F9. For convenience, data is the named range B5:B16. Basic count To get a count of individual dates that...

[![Excel formula: Dynamic summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20summary%20count.png "Excel formula: Dynamic summary count")](https://exceljet.net/formulas/dynamic-summary-count)

### [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)

In this example, the goal is to build a simple summary count table with a formula. Once created, the summary table should automatically update to show new values and counts when data changes. The article below walks through several options, from simple to very advanced. The more advanced options...

Related functions
-----------------

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel MAKEARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20makearray%20function.png "Excel MAKEARRAY function")](https://exceljet.net/functions/makearray-function)

### [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)

The Excel MAKEARRAY function returns an array with specified rows and columns, based on a custom [LAMBDA calculation](https://exceljet.net/functions/lambda-function)
. MAKEARRAY can be used to create arrays with variable dimensions based on a calculation....

[![Excel BYCOL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20bycol%20function.png "Excel BYCOL function")](https://exceljet.net/functions/bycol-function)

### [BYCOL Function](https://exceljet.net/functions/bycol-function)

The Excel BYCOL function applies a function to each column in a given array and returns one result per column. BYCOL can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Running count of occurrence in list](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)
    
*   [Mortgage payment schedule](https://exceljet.net/formulas/mortgage-payment-schedule)
    
*   [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)
    
*   [Dynamic summary count](https://exceljet.net/formulas/dynamic-summary-count)
    
*   [Cash denomination calculator](https://exceljet.net/formulas/cash-denomination-calculator)
    
*   [Calculate running total](https://exceljet.net/formulas/calculate-running-total)
    

### Functions

*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [MAKEARRAY Function](https://exceljet.net/functions/makearray-function)
    
*   [BYCOL Function](https://exceljet.net/functions/bycol-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

### Links

*   [Microsoft SCAN function documentation](https://support.microsoft.com/en-us/office/scan-function-d58dfd11-9969-4439-b2dc-e7062724de29)
    

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