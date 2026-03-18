# Longest winning streak - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/longest-winning-streak

---

[Skip to main content](https://exceljet.net/formulas/longest-winning-streak#main-content)

[](https://exceljet.net/formulas/longest-winning-streak#)

*   [Previous](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)
    
*   [Next](https://exceljet.net/formulas/lookup-last-file-revision)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Longest winning streak
======================

by Dave Bruns · Updated 15 Apr 2025

Related functions 
------------------

[SCAN](https://exceljet.net/functions/scan-function)

[FREQUENCY](https://exceljet.net/functions/frequency-function)

[MAX](https://exceljet.net/functions/max-function)

[IF](https://exceljet.net/functions/if-function)

[LET](https://exceljet.net/functions/let-function)

[FILTER](https://exceljet.net/functions/filter-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

[DROP](https://exceljet.net/functions/drop-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8278/download?token=nWoUTRR1)
 (25.7 KB)

![Excel formula: Longest winning streak](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/longest_winning_streak.png "Excel formula: Longest winning streak")

Summary
-------

The easiest way to calculate a count of the longest winning streak is to use the [SCAN function](https://exceljet.net/functions/scan-function)
 with the [MAX function](https://exceljet.net/functions/max-function)
. In the example shown, the formula in cell E5 is:

    =MAX(SCAN(0,C5:C22,LAMBDA(a,v,IF(v="w",a+1,0))))
    

The result is 5 — the longest streak of consecutive wins, starting on April 15 and ending on April 25.

_Note: SCAN is only available in the latest version of Excel. See below for formulas that will work in older versions of Excel._

Generic formula
---------------

    =MAX(SCAN(0,array,LAMBDA(a,v,IF(v="w",a+1,0))))

Explanation 
------------

In this example, the goal is to calculate a count for the longest winning streak in a set of data. In the worksheet shown, wins ("W") and losses ("L") are recorded in column C, so this means we want to count the longest consecutive series of W's. Although we are specifically counting the longest winning streak in this example, the same approach can be used to count many other things, including:

*   Consecutive days of exercise.
*   Consecutive days without symptoms.
*   Consecutive days practicing a language or skill.
*   Consecutive days not drinking, or not smoking.
*   Consecutive days without an accident (at a factory for example).

To handle these use cases, you will need to adjust the formulas to work with the data as recorded.

### Options

The article below explains four formula solutions:

1.  A [simple solution](https://exceljet.net/formulas/longest-winning-streak#simple_scan_formula)
     based on the SCAN function.
2.  A more robust SCAN-based formula that [lists all winning steaks](https://exceljet.net/formulas/longest-winning-streak#formula_to_list_all_winning_streaks)
    .
3.  A simple solution [based on a helper column](https://exceljet.net/formulas/longest-winning-streak#formula_based_on_helper_column)
     for older versions of Excel.
4.  A l[egacy array formula](https://exceljet.net/formulas/longest-winning-streak#legacy_array_formula)
     based on the FREQUENCY function.

Options #1 and #2 above require a version of Excel with the SCAN function, which is currently Excel 365. Options #3 and #4 will work in older versions of Excel.

### Simple SCAN formula

In the current version of Excel with the SCAN function, the simplest way to solve this problem is like this:

    =MAX(SCAN(0,C5:C22,LAMBDA(a,v,IF(v="w",a+1,0))))

The SCAN formula may look scary, but it is actually pretty simple. Starting at zero, SCAN runs through the list of results. When it encounters a "w", it adds 1 to a running count. When it encounters any other value, it resets the running count to zero. SCAN returns the full set of running counts to MAX, which returns the maximum number. Let's look at the details.

The [SCAN function](https://exceljet.net/functions/scan-function)
 applies a custom calculation to each item in an array and returns a new array that contains the intermediate values created during the scan. Because SCAN has a mechanism to keep track of intermediate values (an accumulator), it works well for running totals and other calculations that display intermediate results. In this formula, SCAN is configured like this:

    SCAN(0,C5:C22,LAMBDA(a,v,IF(v="w",a+1,0)))

Here, the _initial\_value_ is provided as zero (0), and the _array_ is given as C5:C22, which contains 18 values like this:

    {"L";"W";"W";"L";"L";"L";"W";"W";"W";"W";"W";"L";"L";"L";"W";"L";"W";"W"}

The custom LAMBDA calculation looks like this:

    =LAMBDA(a,v,IF(v="w",a+1,0)

When the value (v) is equal to "w", the accumulator (a) is incremented by 1. Otherwise, the accumulator is reset to zero. The output from SCAN looks like this:

    {0;1;2;0;0;0;1;2;3;4;5;0;0;0;1;0;1;2}

This array contains 18 numbers which represent the running counts of consecutive wins. Notice the count starts over again at zero when there is a loss. When there are consecutive wins, it increases. The final step in the formula is to extra the maximum value with the [MAX function](https://exceljet.net/functions/max-function)
, which is wrapped around SCAN:

    =MAX({0;1;2;0;0;0;1;2;3;4;5;0;0;0;1;0;1;2})

The result is 5, which is the longest streak of consecutive wins.

### Formula to list all winning streaks

You can also solve this problem with a more advanced SCAN formula that reports _all winning streaks_ at the same time. You can see the result in the worksheet below, where the formula in E5 is:

![Using the SCAN function to return all winning streaks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/all_winning_streaks.png "Using the SCAN function to return all winning streaks")

    =LET(
    streaks,SCAN(0,C5:C22,LAMBDA(a,v,IF(v="w",a+1,0))),
    shifted,VSTACK(DROP(streaks,1),0),
    ends,(streaks>0)*(shifted=0),
    FILTER(streaks,ends)
    )

This formula uses the [LET function](https://exceljet.net/functions/let-function)
 to define three variables. First, the variable _streaks_ is defined with SCAN like this:

    SCAN(0,C5:C22,LAMBDA(a,v,IF(v="w",a+1,0)))

This is the SCAN formula from the first example above, and the result is the same numeric array of winning streaks:

    {0;1;2;0;0;0;1;2;3;4;5;0;0;0;1;0;1;2}

Next, the variable _shifted_ is defined like this:

    VSTACK(DROP(streaks,1),0)

Here, we "shift" the _streaks_ array up one row by dropping the first row with [DROP](https://exceljet.net/functions/drop-function)
, then adding a row that contains zero to the end with [VSTACK](https://exceljet.net/functions/vstack-function)
. The result looks like this:

    {1;2;0;0;0;1;2;3;4;5;0;0;0;1;0;1;2;0}

The idea here is to make it easy to make it easy to check any value in _streaks_ together with its "next" value. We use the shifted array to create the variable _ends_ like this:

    (streaks>0)*(shifted=0)

This expression uses [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
 to check (1) the current value in streaks is greater than zero and (2) the next value is zero. In other words, we are marking the end of winning streaks. The result from the expression above is an array of 1s and 0s like this:

    {0;0;1;0;0;0;0;0;0;0;1;0;0;0;1;0;0;1}

If you study the array closely, you can see that the 1s in this array mark the last row of a winning streak. For example, the third item is a 1, because the 2-game winning streak in rows 2 and 3 has ended. In the last step, we generate a list of winning streaks with the FILTER function like this:

    FILTER(streaks,ends)

In this step, the _ends_ array is used to filter the _streaks_ array. Because _ends_ marks the end of winning streaks, the result from FILTER are the counts for the four winning streaks in the data:

    {2;5;1;2}

Although this formula is more complicated than the first formula above, it is also more flexible. You can wrap the MAX function around FILTER to get the maximum winning streak, display all winning streaks, or sort or filter the list of winning streaks to suit your needs.

### Formula based on a helper column

If you are using an older version of Excel that does not offer the SCAN function, or if you just want a simpler and more transparent approach, you can use a [helper column](https://exceljet.net/glossary/helper-column)
. In the screen below, the helper column is column D and the formula in cell D5 is:

    =IF(C5="w",SUM(D4,1),0)

![Longest winning streak with helper column](https://exceljet.net/sites/default/files/images/formulas/inline/longest_winning_streak_with_helper.png "Longest winning streak with helper column")

As the formula is copied down, it creates a running total of consecutive wins. If the value in column C is "w", the SUM function is used to sum add 1 to the row above. Otherwise, the count is reset to zero.

_Note: using the_ [_SUM function_](https://exceljet.net/functions/sum-function)
 _like this is a clever way to avoid an error when a cell value contains text, since SUM treats text values as zero. With a normal formula like =IF(C5="w", D4+1,0) the result will be #VALUE! if cell C5 contains "W", because the header text in cell D4 will cause an error. Also, note that Excel is not case-sensitive by default, so we are using a lowercase "w" to test values._

Once the helper column is populated, the MAX function is used in cell F5 to return a final result:

    =MAX(D5:D22) // returns 5

The result is 5, the longest streak of consecutive wins in the data.

### Legacy array formula based on FREQUENCY

_This formula only makes sense in an older version of Excel when you don't want to use a helper column. FREQUENCY is one of those quirky functions that turned up in hard-to-solve problems in the past, before_ [_dynamic array formulas_](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 _were introduced. The formula explained below is an_ [_array formula_](https://exceljet.net/videos/what-is-an-array-formula)
 _that must be entered with Control + Shift + Enter in Excel 2019 and older._

Do you like tricky formulas? If so, you might like this formula based on the [FREQUENCY function](https://exceljet.net/functions/frequency-function)
:

    =MAX(FREQUENCY(IF(list,id),IF(list,,id)))

I ran this formula many years ago in a comment on a [Chandoo formula challenge page](https://chandoo.org/wp/longest-winning-streak-problem/)
. Since we don't have a list of numeric ids to work with, and since wins and losses are recorded as "W" and "L" instead of TRUE and FALSE, we need to adjust the formula as follows to make it work for the example on this page:

    =MAX(FREQUENCY(IF(C5:C22="w",ROW(C5:C22)),IF(C5:C22="w",0,ROW(C5:C22))))

This is a tricky formula to understand. The key idea is that FREQUENCY gathers numbers into "bins". Each bin has an upper limit and holds the count of all numbers in the data set that are less than or equal to the upper limit, and greater than the previous bin number. The formula creates a new bin at the end of each winning streak using the row number of the loss. All other bins are created as zero. The practical effect is a count of consecutive wins in each bin.

Inside FREQUENCY, the _data\_array_ is generated with this code:

    IF(C5:C22="w",ROW(C5:C22))

The result is an array with 18 items like this:

    {FALSE;6;7;FALSE;FALSE;FALSE;11;12;13;14;15;FALSE;FALSE;FALSE;19;FALSE;21;22}

Notice that only wins make it into this array, appearing as column numbers. The losses become FALSE. The _bins\_array_ is generated in a similar way like this:

    IF(C5:C22="w",0,ROW(C5:C22))
    

Here the logic is reversed and the result is an array like this:

    {5;0;0;8;9;10;0;0;0;0;0;16;17;18;0;20;0;0}

In this array, only the row numbers for the losses survive as non-zero values, and they become the bins that tally wins. The wins are forced to zero and don't collect any numbers from the data array, since zero or FALSE values are ignored. The final arrays delivered to FREQUENCY look like this:

    =FREQUENCY({FALSE;6;7;FALSE;FALSE;FALSE;11;12;13;14;15;FALSE;FALSE;FALSE;19;FALSE;21;22},{5;0;0;8;9;10;0;0;0;0;0;16;17;18;0;20;0;0})

With these inputs, FREQUENCY returns an array of counts per bin that looks like this:

    {0;0;0;2;0;0;0;0;0;0;0;5;0;0;0;1;0;0;2}

Finally, the MAX function returns 5, the longest streak of consecutive wins.

Related formulas
----------------

[![Excel formula: Calculate win loss tie totals](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20win%20loss%20tie%20totals.png "Excel formula: Calculate win loss tie totals")](https://exceljet.net/formulas/calculate-win-loss-tie-totals)

### [Calculate win loss tie totals](https://exceljet.net/formulas/calculate-win-loss-tie-totals)

The goal in this example is to calculate total wins, losses, and ties for each team listed in column G. The problem is complicated somewhat by the fact that a team can appear in either column B or C, so we need to take this into account when calculating wins and losses. For convenience and...

[![Excel formula: Count consecutive monthly orders](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20consecutive%20monthly%20orders.png "Excel formula: Count consecutive monthly orders")](https://exceljet.net/formulas/count-consecutive-monthly-orders)

### [Count consecutive monthly orders](https://exceljet.net/formulas/count-consecutive-monthly-orders)

In this example, the goal is to count the maximum number of consecutive monthly orders. That is, we want to count consecutive monthly orders greater than zero. This is a tricky formula to understand, so buckle up! They key to the formula is knowing that the FREQUENCY function gathers numbers into "...

Related functions
-----------------

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel FREQUENCY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20frequency%20function.png "Excel FREQUENCY function")](https://exceljet.net/functions/frequency-function)

### [FREQUENCY Function](https://exceljet.net/functions/frequency-function)

The Excel FREQUENCY function returns a frequency distribution, which is a list that shows the frequency of values at given intervals. FREQUENCY returns multiple values and must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control-shift-enter, except in...

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Calculate win loss tie totals](https://exceljet.net/formulas/calculate-win-loss-tie-totals)
    
*   [Count consecutive monthly orders](https://exceljet.net/formulas/count-consecutive-monthly-orders)
    

### Functions

*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [FREQUENCY Function](https://exceljet.net/functions/frequency-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    

### Links

*   [What is the length of longest winning streak (Chandoo)](http://chandoo.org/wp/2015/01/30/longest-winning-streak-problem/)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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