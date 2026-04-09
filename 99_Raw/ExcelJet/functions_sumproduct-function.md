# Excel SUMPRODUCT function | Exceljet

**Source:** https://exceljet.net/functions/sumproduct-function

---

[Skip to main content](https://exceljet.net/functions/sumproduct-function#main-content)

[](https://exceljet.net/functions/sumproduct-function#)

*   [Previous](https://exceljet.net/functions/sumifs-function)
    
*   [Next](https://exceljet.net/functions/sumsq-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

SUMPRODUCT Function
===================

by Dave Bruns · Updated 25 Jun 2025

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMIF](https://exceljet.net/functions/sumif-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")

Summary
-------

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS, but with more flexibility. Other functions can easily be used inside SUMPRODUCT to extend functionality even further.

Purpose 
--------

Multiply, then sum arrays

Return value 
-------------

The result of multiplied and summed arrays

Syntax
------

    =SUMPRODUCT(array1,[array2],...)

*   _array1_ - The first array or range to multiply, then add.
*   _array2_ - \[optional\] The second array or range to multiply, then add.

Using the SUMPRODUCT function 
------------------------------

The SUMPRODUCT function multiplies [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. If only one array is supplied, SUMPRODUCT will simply sum the items in the array. Up to 30 ranges or arrays can be supplied. When you first encounter SUMPRODUCT, it may seem boring, complex, and even pointless. But SUMPRODUCT is an amazingly versatile function with many uses. Because it will handle arrays gracefully, you can use it to process ranges of cells in clever, elegant ways.

### Key features

*   Works with arrays natively in older versions of Excel (no need for Ctrl+Shift+Enter)
*   Can apply complex AND/OR logic using Boolean algebra
*   Works for conditional sums, counts, and averages (can replace SUMIFS, COUNTIFS, AVERAGEIFS)
*   Automatically treats non-numeric values as zeros (like the SUM function)
*   Can use other functions like LEN, ISBLANK, ISTEXT, ISERROR, etc., directly
*   Works in all Excel versions

### Table of contents

*   [Classic SUMPRODUCT example](https://exceljet.net/functions/sumproduct-function#classic-sumproduct-example)
    
*   [SUMPRODUCT for conditional sums](https://exceljet.net/functions/sumproduct-function#sumproduct-for-conditional-sums)
    
*   [SUMPRODUCT for conditional sums and counts](https://exceljet.net/functions/sumproduct-function#sumproduct-for-conditional-sums-and-counts)
    
*   [SUMPRODUCT with double negative (--)](https://exceljet.net/functions/sumproduct-function#sumproduct-with-double-negative)
    
*   [SUMPRODUCT with OR logic](https://exceljet.net/functions/sumproduct-function#sumproduct-with-or-logic)
    
*   [SUMPRODUCT with abbreviated syntax](https://exceljet.net/functions/sumproduct-function#sumproduct-with-abbreviated-syntax)
    
*   [Ignoring empty cells](https://exceljet.net/functions/sumproduct-function#ignoring-empty-cells)
    
*   [SUMPRODUCT with other functions](https://exceljet.net/functions/sumproduct-function#sumproduct-with-other-functions)
    
*   [Arrays and Excel 365](https://exceljet.net/functions/sumproduct-function#arrays-and-excel-365)
    

### Classic SUMPRODUCT example

The "classic" SUMPRODUCT example illustrates how you can calculate a sum directly without a [helper column](https://exceljet.net/glossary/helper-column)
. For example, in the worksheet below, you can use SUMPRODUCT to get the total of all numbers in column F without using column F at all:

![Classic SUMPRODUCT example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/classic%20sumproduct%20example.png?itok=ukUVWI7c "Classic SUMPRODUCT example")

To perform this calculation, SUMPRODUCT uses values in columns D and E directly like this:

    =SUMPRODUCT(D5:D14,E5:E14) // returns 1612
    

The result is the same as summing all values in column F. The formula is evaluated like this:

    =SUMPRODUCT(D5:D14,E5:E14)
    =SUMPRODUCT({10;6;14;9;11;10;8;9;11;10},{15;18;15;16;18;18;15;16;18;16})
    =SUMPRODUCT({150;108;210;144;198;180;120;144;198;160})
    =1612
    

This use of SUMPRODUCT can be handy, especially when there is no room (or need) for a helper column with an intermediate calculation. However, the most common use of SUMPRODUCT in the real world is to apply conditional logic in situations that require more flexibility than functions like SUMIFS and COUNTIFS can offer.

### SUMPRODUCT for conditional sums

A typical use for the SUMPRODUCT function is to calculate conditional sums, much like you would use a function like SUMIFS. In the worksheet shown below, SUMPRODUCT is used to calculate conditional sums with four separate formulas:

    =SUMPRODUCT(--(C5:C14="red"),F5:F14) // red
    =SUMPRODUCT(--(B5:B14="tx"),--(C5:C14="red"),F5:F14) // tx and red
    =SUMPRODUCT(--(B5:B14="co"),--(C5:C14="blue"),F5:F14) // co and blue
    =SUMPRODUCT(--(C5:C14<>"red"),F5:F14) // not red
    

![SUMPRODUCT for conditional sums](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumproduct_function_conditional_sums_example.png "SUMPRODUCT for conditional sums")

The results are visible in cells I5, I6, I7, and I8. The article below explains how SUMPRODUCT can be used to calculate these kinds of conditional sums, and the purpose of the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) in the formulas.

### SUMPRODUCT for conditional sums and counts

The SUMPRODUCT function can be used for conditional sums or counts. To illustrate how this works, let's look at a very simple example. Assume we have some order data in A2:B6, with State in column A, and Sales in column B:

|     |     |     |
| --- | --- | --- |
|     | A   | B   |
| 1   | State | Sales |
| 2   | UT  | 75  |
| 3   | CO  | 100 |
| 4   | TX  | 125 |
| 5   | CO  | 125 |
| 6   | TX  | 150 |

Using SUMPRODUCT, you can _sum_ total sales for Texas ("TX") with this formula:

    =SUMPRODUCT(--(A2:A6="TX"),B2:B6)
    

You can also _count_ total sales for Texas ("TX") with this formula:

    =SUMPRODUCT(--(A2:A6="TX"))
    

Notice we have retained the conditional logic `--(A2:A6="TX")` from the formula above, and simply removed the second array (Sales). This is the basic idea of counting with SUMPRODUCT. The conditional logic remains, but the second array is removed. However, to make this work, we need a way to coerce the true and false values that the logic creates into ones and zeros. Let's look at that next.

### SUMPRODUCT with double negative (--)

The formulas above use a [double negative (--)](https://exceljet.net/glossary/double-unary)
 to make the conditional logic work properly. To understand why this is necessary, let's trace through exactly what happens when SUMPRODUCT processes our Texas example. When Excel evaluates the expression `A2:A6="TX"`, it creates an array of TRUE and FALSE values based on which cells match "TX". Here's what the two arrays look like initially:

|     |     |     |     |
| --- | --- | --- | --- |
| array1 | array2 | Product | Result |
| FALSE | 75  | FALSE \* 75 | 0   |
| FALSE | 100 | FALSE \* 100 | 0   |
| TRUE | 125 | TRUE \* 125 | 0   |
| FALSE | 125 | FALSE \* 125 | 0   |
| TRUE | 150 | TRUE \* 150 | 0   |
| **Sum** |     |     | **0** |

_Array1_ contains the TRUE/FALSE results from our condition, while _array2_ contains the corresponding sales values. The problem is that SUMPRODUCT needs to multiply these arrays together, but the raw TRUE and FALSE values can't be used directly because they are treated as zeros, making our entire calculation return zero.

This is where the [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 becomes important. The double negative is [one of several ways](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 to convert TRUE and FALSE values into their numeric equivalents: TRUE becomes 1, and FALSE becomes 0. This conversion enables [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 operations within our formula. After applying the double negative, here's how the table above works:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| array1 |     | array2 |     | Product |
| 0   | \*  | 75  | \=  | 0   |
| 0   | \*  | 100 | \=  | 0   |
| 1   | \*  | 125 | \=  | 125 |
| 0   | \*  | 125 | \=  | 0   |
| 1   | \*  | 150 | \=  | 150 |
| **Sum** |     |     |     | **275** |

Now SUMPRODUCT can perform the calculation successfully. In [array](https://exceljet.net/videos/what-is-an-array)
 terms, the formula evaluates like this:

    =SUMPRODUCT({0,0,1,0,1},{75,100,125,125,150})
    

SUMPRODUCT multiplies the corresponding elements of both arrays, then sums the result:

    =SUMPRODUCT({0,0,125,0,150}) // returns 275

The same double negative principle applies to our conditional count example. Recall that we can count Texas sales using `=SUMPRODUCT(--(A2:A6="TX"))`. After applying the double negative, we get the array `{0,0,1,0,1}`. Since we're only providing one array to SUMPRODUCT (no second array to multiply against), SUMPRODUCT simply sums the values in this single array: 0+0+1+0+1 = 2. This gives us a count of 2, representing the two rows where the state equals "TX". The double negative is essential here because without it, SUMPRODUCT would receive `{FALSE,FALSE,TRUE,FALSE,TRUE}` and treat these logical values as zeros, returning 0 instead of the correct count.

> [This example](https://exceljet.net/formulas/sumproduct-with-if)
>  expands on the ideas above with more detail.

### SUMPRODUCT with OR logic

It is also possible to use the SUMPRODUCT function with OR logic, i.e., sum if this or that. The trick is to use Boolean logic, where OR logic is represented with addition (+). You can see this approach in the worksheet below:

![SUMPRODUCT function with OR logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumproduct_function_with_or_logic.png "SUMPRODUCT function with OR logic")

The formulas in I5:I7 are as follows:

    =SUMPRODUCT(--((C5:C14="red")+(C5:C14="blue")>0),F5:F14) // red or blue
    =SUMPRODUCT(--((B5:B14="tx")+(C5:C14="red")>0),F5:F14) // tx or red
    =SUMPRODUCT(--((B5:B14="co")+(C5:C14="blue")>0),F5:F14) // co or blue
    

Notice that the two logical expressions are joined with addition (+), and the resulting array is checked against zero (>0) and then converted to 1s and 0s with the double negative (--):

    --((C5:C14="red")+(C5:C14="blue")>0)
    

For a more detailed explanation of how and why this works, watch this 3-minute video: [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
. Also, see [this example](https://exceljet.net/formulas/sum-if-cells-contain-either-x-or-y)
, which explains several ways to approach a problem like this.

### SUMPRODUCT with abbreviated syntax

You will often see the formula described above written in a different way, like this:

    =SUMPRODUCT((A2:A6="TX")*B2:B6) // returns 275
    

Notice that all calculations have been moved into _array1_. The result is the same, but this syntax provides several advantages. First, the formula is more compact, especially as the logic becomes more complex. This is because the double negative (--) is no longer needed to convert TRUE and FALSE values — the math operation of multiplication (_)_ automatically _converts the TRUE and FALSE values from (A2:A6="TX") to 1s and 0s. But the most important advantage is_ flexibility_. When using separate arguments, the operation is always multiplication, since SUMPRODUCT returns the sum of_ products\*. This limits the formula to AND logic since multiplication corresponds to addition in [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
. Moving calculations into one argument means you can use addition (+) for OR logic, in any combination. In other words, you can choose your own math operations, which ultimately dictate the logic of the formula. [See example here](https://exceljet.net/formulas/count-rows-with-or-logic)
.

> Even though the double negative is no longer needed, there is no harm in leaving it in the formula.

With the above advantages in mind, there is one disadvantage to the abbreviated syntax. SUMPRODUCT is programmed to ignore the errors that result from multiplying text values in arrays given as _separate arguments_. This can be [handy in certain situations](https://exceljet.net/formulas/sum-columns-based-on-adjacent-criteria)
. With the abbreviated syntax, this advantage goes away, since the multiplication happens inside a single array argument. In this case, the normal behavior applies: text values will create #VALUE! errors.

_Note: Technically, moving calculations into array1 creates an "_[_array operation_](https://exceljet.net/glossary/array-operation)
_", and SUMPRODUCT is one of only a few functions that can handle an array operation natively without Control + Shift + Enter in_ [_Legacy Excel_](https://exceljet.net/glossary/legacy-excel)
_. See_ [_Why SUMPRODUCT?_](https://exceljet.net/articles/why-sumproduct)
 _for more details._

### Ignoring empty cells

To ignore empty cells with SUMPRODUCT, you can use an expression like _range<>""_. In the example below, the formulas in F5 and F6 both ignore cells in column C that do not contain a value:

    =SUMPRODUCT(--(C5:C15<>"")) // count
    =SUMPRODUCT(--(C5:C15<>"")*D5:D15) // sum
    

![SUMPRODUCT example - ignore empty cells](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/sumproduct%20ignore%20empty%20cells.png?itok=ZLbac_XK "SUMPRODUCT example - ignore empty cells")

### SUMPRODUCT with other functions

SUMPRODUCT can use other functions directly. You might see SUMPRODUCT used with the LEN function to count total characters in a range, or with functions like ISBLANK, ISTEXT, etc., to count blanks in a range or text values in a range. These are not normally array functions, but when they are given a range, they create an array of results. Because SUMPRODUCT is built to work with arrays, it is able to perform calculations on the arrays directly. You can see an example of this in the worksheet below, where we have eight text strings in the range B5:B12, and we are using SUMPRODUCT with the LEN function to calculate the total characters in the range with this formula in cell D5:

    =SUMPRODUCT(LEN(B5:B12))

![Example of using SUMPRODUCT with other functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/classic_sumproduct_with_other_functions.png "Example of using SUMPRODUCT with other functions")

For example, assume you have 10 different text values in A1:A10 and you want to count the total characters for all 10 values. You could add a helper column in column B that uses this formula: LEN(A1) to calculate the characters in each cell. Then you could use SUM to add up all 10 numbers. However, using SUMPRODUCT, you can write a formula like this:

    =SUMPRODUCT(LEN(A1:A10))
    

Working from the inside out, the LEN function runs first and returns an array of 8 results. The SUMPRODUCT function then sums the array and returns the final result. The formula evaluates like this:

    =SUMPRODUCT(LEN(A1:A10))
    =SUMPRODUCT({38;40;33;32;29;40;32;42})
    =286

The final result is 286. To be clear, you can use the SUM function to do the same thing in a current version of Excel. However, in older versions of Excel (Excel 2019 and older), using SUMPRODUCT this way is a way to avoid having to enter the formula using Ctrl+Shift+Enter. 

### Arrays and Excel 365

This is a confusing topic, but it must be mentioned. In Excel 2019 and earlier, the SUMPRODUCT function can be used to create array formulas that don't require [Ctrl + Shift + Enter](https://exceljet.net/shortcuts/enter-array-formula)
. This is a key reason that SUMPRODUCT was so widely used to create more advanced formulas for the past 20 years or so, up to the introduction of dynamic array formulas. Using SUMPRODUCT was a way to get array formulas to work in _any version_ of Excel _without special handling_.

However, in [Excel 365](https://exceljet.net/glossary/excel-365)
, the formula engine [handles arrays natively](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. This means you can often use the SUM function in place of SUMPRODUCT in an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 with the same result, with no need to enter the formula in a special way. However, if the same formula is opened in an earlier version of Excel, it will still require Ctrl + Shift + Enter to work correctly.

> The bottom line is that SUMPRODUCT is a safer option if a worksheet will be used often in older versions of Excel. For more details and examples, see [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)

### Notes

*   SUMPRODUCT treats non-numeric items in arrays as zeros.
*   Array arguments must be the same size. Otherwise, SUMPRODUCT will generate a #VALUE! error value.
*   Logical tests inside arrays will create TRUE and FALSE values. In most cases, you'll want to coerce these to 1's and 0's.
*   SUMPRODUCT can often use the result of other functions directly.

SUMPRODUCT function examples
----------------------------

[![Excel formula: Count rows with OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20OR%20logic.png "Excel formula: Count rows with OR logic")](https://exceljet.net/formulas/count-rows-with-or-logic)

### [Count rows with OR logic](https://exceljet.net/formulas/count-rows-with-or-logic)

One of the trickier problems in Excel is to count rows in a set of data with "OR logic". There are two basic scenarios: (1) you want to count rows where a value in a column is "x" OR "y" (2) you want to count rows where a value, "x", exists in one column OR another. In this example, the goal is to...

[![Excel formula: Count cells that are blank](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20are%20blank_0.png "Excel formula: Count cells that are blank")](https://exceljet.net/formulas/count-cells-that-are-blank)

### [Count cells that are blank](https://exceljet.net/formulas/count-cells-that-are-blank)

In this example, the goal is to count cells in a range that are blank. Counting blank cells in Excel can be tricky because cells can look blank even when they are not actually empty. The article below explains three different approaches. COUNTBLANK function The simplest way to count empty cells in...

[![Excel formula: Conditional formatting dates overlap](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Conditional%20formatting%20dates%20overlap.png "Excel formula: Conditional formatting dates overlap")](https://exceljet.net/formulas/conditional-formatting-dates-overlap)

### [Conditional formatting dates overlap](https://exceljet.net/formulas/conditional-formatting-dates-overlap)

Consider for a moment how overlapping dates work. For a project to overlap the dates of other projects, two conditions must be true: The start date must be less than or equal (<=) to at least one other end date and the list. The end date for the project must be greater than or equal to (>=)...

[![Excel formula: Weighted average](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/weighted_average.png "Excel formula: Weighted average")](https://exceljet.net/formulas/weighted-average)

### [Weighted average](https://exceljet.net/formulas/weighted-average)

In this example, the goal is to calculate a weighted average of scores for each name in the table using the weights that appear in the named range weights (I5:K5) and the scores in columns C through E. A weighted average (also called a weighted mean ) is an average where some values are more...

[![Excel formula: Count day of week between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20day%20of%20week%20between%20dates.png "Excel formula: Count day of week between dates")](https://exceljet.net/formulas/count-day-of-week-between-dates)

### [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)

At the core, this formula uses the WEEKDAY function to test a number of dates to see if they land on a given day of week (dow) and the SUMPRODUCT function to tally up the total. When given a date, WEEKDAY simply returns a number between 1 and 7 that corresponds to a particular day of the week. With...

[![Excel formula: Count cells that contain numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20numbers.png "Excel formula: Count cells that contain numbers")](https://exceljet.net/formulas/count-cells-that-contain-numbers)

### [Count cells that contain numbers](https://exceljet.net/formulas/count-cells-that-contain-numbers)

In this example, the goal is to count the number of cells in a range that contain numbers. This problem can be solved with the COUNT function or the SUMPRODUCT function. Both methods are explained below. COUNT function The COUNT function counts the number of cells in a range that contain numeric...

[![Excel formula: Text is greater than number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/text%20is%20greater%20than%20number.png "Excel formula: Text is greater than number")](https://exceljet.net/formulas/text-is-greater-than-number)

### [Text is greater than number](https://exceljet.net/formulas/text-is-greater-than-number)

Excel's formula engine has some quirks that you should be aware of. One of these quirks is that Excel will treat a text value as larger than a number by default. For example: =90>100 // returns FALSE ="A">100 // returns TRUE The second formula above returns TRUE when you probably expect it to...

[![Excel formula: Count numbers by nth digit](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20numbers%20by%20nth%20digit.png "Excel formula: Count numbers by nth digit")](https://exceljet.net/formulas/count-numbers-by-nth-digit)

### [Count numbers by nth digit](https://exceljet.net/formulas/count-numbers-by-nth-digit)

In this example, the goal is to count numbers in the range B5:B15 ( named data ) where the third digit is a specific number, indicated in column D. You might think the COUNTIF function would be a good way to solve this problem. However, for reasons explained below, COUNTIF won't work. Instead, you...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Get work hours between dates custom schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20custom2.png "Excel formula: Get work hours between dates custom schedule")](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

### [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

At the core, this formula uses the WEEKDAY function to figure out the day of week (i.e. Monday, Tuesday, etc.) for every day between the two given dates. WEEKDAY returns a number between 1 and 7. With default settings, Sunday=1 and Saturday = 7. The trick to this formula is assembling an array of...

[![Excel formula: SUMPRODUCT case-sensitive lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT_case_sensitive_lookup.png "Excel formula: SUMPRODUCT case-sensitive lookup")](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

### [SUMPRODUCT case-sensitive lookup](https://exceljet.net/formulas/sumproduct-case-sensitive-lookup)

The SUMPRODUCT function multiplies arrays together and returns the sum of products. If only one array is supplied, SUMPRODUCT will simply sum the items in the array. For example, if we give SUMPRODUCT one array in the form of the data\[Qty\] column: =SUMPRODUCT(data\[Qty\]) // returns 54 SUMPRODUCT...

[![Excel formula: Count unique values in a range with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values%20with%20COUNTIF.png "Excel formula: Count unique values in a range with COUNTIF")](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)

### [Count unique values in a range with COUNTIF](https://exceljet.net/formulas/count-unique-values-in-a-range-with-countif)

Working from the inside out, COUNTIF is configured to values in the range B5:B14, using all of these same values as criteria: COUNTIF(B5:B14,B5:B14) Because we provide 10 values for criteria, we get back an array with 10 results like this: {3;3;3;2;2;3;3;3;2;2} Each number represents a count – "Jim...

[![Excel formula: Count matches between two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20matches%20between%20two%20columns.png "Excel formula: Count matches between two columns")](https://exceljet.net/formulas/count-matches-between-two-columns)

### [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)

In this example, the goal is to compare two columns and return the count of matches in corresponding rows. A good way to solve this problem is to use the SUMPRODUCT function or the SUM function, as explained below. SUMPRODUCT function The SUMPRODUCT function is a versatile function that handles...

[![Excel formula: Count cells that do not contain](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20do%20not%20contain.png "Excel formula: Count cells that do not contain")](https://exceljet.net/formulas/count-cells-that-do-not-contain)

### [Count cells that do not contain](https://exceljet.net/formulas/count-cells-that-do-not-contain)

In this example, the goal is to count cells that do not contain a specific substring. This problem can be solved with the COUNTIF function or the SUMPRODUCT function . Both approaches are explained below. Although COUNTIF is not case-sensitive, the SUMPRODUCT version of the formula can be adapted...

[![Excel formula: Count birthdays by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20birthdays%20by%20month.png "Excel formula: Count birthdays by month")](https://exceljet.net/formulas/count-birthdays-by-month)

### [Count birthdays by month](https://exceljet.net/formulas/count-birthdays-by-month)

You would think you could use the COUNTIF function to count birthdays, but the trouble is COUNTIF only works with ranges , and won't let you use something like MONTH to extract just the month number from dates. So, we use the SUMPRODUCT function with custom logic instead. Inside SUMPRODUCT, we have...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel SUMIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumif%20function.png "Excel SUMIF function")](https://exceljet.net/functions/sumif-function)

### [SUMIF Function](https://exceljet.net/functions/sumif-function)

The Excel SUMIF function returns the sum of cells that meet a single condition. Criteria can be applied to dates, numbers, and text. The SUMIF function supports logical operators (>,<,<>,=) and wildcards (\*,?) for partial matching....

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Text is greater than number](https://exceljet.net/formulas/text-is-greater-than-number)
    
*   [Conditional formatting dates overlap](https://exceljet.net/formulas/conditional-formatting-dates-overlap)
    
*   [Count total words in a range](https://exceljet.net/formulas/count-total-words-in-a-range)
    
*   [Sum every nth column](https://exceljet.net/formulas/sum-every-nth-column)
    
*   [Count cells over n characters](https://exceljet.net/formulas/count-cells-over-n-characters)
    
*   [Data validation must not contain](https://exceljet.net/formulas/data-validation-must-not-contain)
    
*   [Sum by month ignore year](https://exceljet.net/formulas/sum-by-month-ignore-year)
    
*   [Sum if cell contains text in another cell](https://exceljet.net/formulas/sum-if-cell-contains-text-in-another-cell)
    
*   [Sum last 30 days](https://exceljet.net/formulas/sum-last-30-days)
    
*   [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMIF Function](https://exceljet.net/functions/sumif-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    

### Links

*   [Microsoft SUMPRODUCT function documentation](https://support.office.com/en-us/article/sumproduct-function-16753e75-9f68-4874-94ac-4d2145a2fd2e)
    

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