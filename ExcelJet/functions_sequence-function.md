# Excel SEQUENCE function | Exceljet

**Source:** https://exceljet.net/functions/sequence-function

---

[Skip to main content](https://exceljet.net/functions/sequence-function#main-content)

[](https://exceljet.net/functions/sequence-function#)

*   [Previous](https://exceljet.net/functions/scan-function)
    
*   [Next](https://exceljet.net/functions/sort-function)
    

Excel 2021

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

SEQUENCE Function
=================

by Dave Bruns · Updated 17 Mar 2025

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[FILTER](https://exceljet.net/functions/filter-function)

[SORT](https://exceljet.net/functions/sort-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")

Summary
-------

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. 

Purpose 
--------

Get array of list of sequential numbers

Return value 
-------------

Array of sequential values

Syntax
------

    =SEQUENCE(rows,[columns],[start],[step])

*   _rows_ - Number of rows to return.
*   _columns_ - \[optional\] Number of columns to return.
*   _start_ - \[optional\] Starting value (defaults to 1).
*   _step_ - \[optional\] Increment between each value (defaults to 1).

Using the SEQUENCE function 
----------------------------

The SEQUENCE function generates a list of sequential numbers in an array. The array can be one-dimensional, or two-dimensional, controlled by _rows_ and _columns_ arguments. SEQUENCE can be used on its own to create an array of sequential numbers that [spill](https://exceljet.net/glossary/spill)
 directly on the worksheet. It can also be used to generate a numeric array [inside another formula](https://exceljet.net/formulas/filter-on-first-or-last-n-values)
, a requirement that comes up frequently in more advanced formulas.

The SEQUENCE function takes four [arguments](https://exceljet.net/glossary/function-argument)
: _rows_, _columns_, _start_, and _step_. All values default to 1. The rows and columns arguments control the number of rows and columns that should be generated in the output. For example, the formulas below generate numbers between 1 and 5 in rows and columns:

    =SEQUENCE(5,1) // returns {1;2;3;4;5} in 5 rows
    =SEQUENCE(1,5) // returns {1,2,3,4,5} in 5 columns
    

Note that the output from SEQUENCE is an [array](https://exceljet.net/glossary/array)
 of values that will [spill](https://exceljet.net/glossary/spill)
 into adjacent cells. The formula below will create a 5 x 5 array that contains 25 cells with the values 1-25:

    =SEQUENCE(5,5) // numbers 1-25 in a 5 x 5 array

The syntax for SEQUENCE indicates that _rows_ is required and columns is optional. However, either can be omitted:

    =SEQUENCE(5) // returns {1;2;3;4;5} in 5 rows
    =SEQUENCE(,5) // returns {1,2,3,4,5} in 5 columns
    

The _start_ argument is the starting point in the numeric sequence, and _step_ controls the increment between each value. Both formulas below use a _start_ value of 10 and a _step_ value of 5:

    =SEQUENCE(3,1,10,5) // returns {10;15;20} in 3 rows
    =SEQUENCE(1,3,10,5) // returns {10,15,20} in 3 columns
    

> Video: [T](https://exceljet.net/videos/filter-function-basic-example)
> [he SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

### Examples

In the example in the screen above, the formula in B4 is:

    =SEQUENCE(10,5,0,3)
    

With this configuration, SEQUENCE returns an array of sequential numbers, 10 rows by 5 columns, starting at zero and incremented by 3. The result is 50 numbers starting at 0 and ending at 147, as shown in the screen.

### Positive and negative

SEQUENCE can work with both positive and negative values. To count from -10 to zero in increments of 2 in rows, set _rows_ to 6, _columns_ to 1, _start_ to -10, and _step_ to 2:

    =SEQUENCE(6,1,-10,2) // returns {-10;-8;-6;-4;-2;0}
    

To count down between 10 and zero:

    =SEQUENCE(11,1,10,-1) // returns {10;9;8;7;6;5;4;3;2;1;0}
    

### Sequence of dates

Because [Excel dates are serial numbers](https://exceljet.net/glossary/excel-date)
, you can easily use SEQUENCE to generate sequential dates. For example, to generate a list of 10 days starting today in columns, you can use SEQUENCE with the [TODAY function](https://exceljet.net/functions/today-function)
.

    =SEQUENCE(1,10,TODAY(),1)
    

[More details here](https://exceljet.net/formulas/sequence-of-days)
. To generate a list of 12 dates corresponding to the first day of the month for all months in a year (2022 in this case) you can use SEQUENCE with the [DATE](https://exceljet.net/functions/date-function)
 and [EDATE](https://exceljet.net/functions/edate-function)
 functions:

    =EDATE(DATE(2022,1,1),SEQUENCE(12,1,0))
    

To generate a list of twelve-month names (instead of dates) you can wrap the formulas above in the [TEXT function](https://exceljet.net/functions/text-function)
 like this:

    =TEXT(EDATE(DATE(2022,1,1),SEQUENCE(12,1,0)),"mmmm")
    

[More information about these formulas here](https://exceljet.net/formulas/sequence-of-months)
.

### SEQUENCE with text

SEQUENCE generates numeric arrays. However, it is possible to use SEQUENCE to create arrays that contain text. For example, the formula below will generate a 5 x 5 array filled with "x":

    =REPT("x",SEQUENCE(5,5,1,0)) // 5 x 5 array of x's

SEQUENCE is configured ot return a 5 x 5 array of 1's, which are fed into the [REPT function](https://exceljet.net/functions/rept-function)
 with "x" as the text to repeat. By replacing "x" with an empty string, we can generate an empty 5 x 5 array:

    =REPT("",SEQUENCE(5,5,1,0)) // empty 5 x 5 array

The formula below will generate an array that contains the 26 letters from A-Z:

    =CHAR(SEQUENCE(26,,65)) // generate A-Z

The SEQUENCE function returns 26 numbers starting with 65. The [CHAR function](https://exceljet.net/functions/char-function)
 returns a specific character based on its [ASCII number](https://exceljet.net/glossary/ascii)
. The letter "A" is 65, and "Z" is 90, so the result is all 26 uppercase letters.

> You can also use the [MAKEARRAY function](https://exceljet.net/functions/makearray-function)
>  to generate an array that contains the result of a custom calculation.

SEQUENCE function examples
--------------------------

[![Excel formula: Count day of week between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20day%20of%20week%20between%20dates.png "Excel formula: Count day of week between dates")](https://exceljet.net/formulas/count-day-of-week-between-dates)

### [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)

At the core, this formula uses the WEEKDAY function to test a number of dates to see if they land on a given day of week (dow) and the SUMPRODUCT function to tally up the total. When given a date, WEEKDAY simply returns a number between 1 and 7 that corresponds to a particular day of the week. With...

[![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")](https://exceljet.net/formulas/sequence-of-workdays)

### [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE...

[![Excel formula: Semimonthly pay schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/semimonthly_pay_schedule.png "Excel formula: Semimonthly pay schedule")](https://exceljet.net/formulas/semimonthly-pay-schedule)

### [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)

In this example, the goal is to create a list of pay dates that follow a semimonthly schedule. A semimonthly pay schedule means employees are paid twice a month, usually on fixed dates such as the 1st and 15th or the 15th and the last day of the month. This results in 24 pay periods over the course...

[![Excel formula: Max of every nth column](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/max_of_every_nth_column.png "Excel formula: Max of every nth column")](https://exceljet.net/formulas/max-of-every-nth-column)

### [Max of every nth column](https://exceljet.net/formulas/max-of-every-nth-column)

In this example, the goal is to calculate the maximum value of every "nth" column in a row of data, where n is a variable entered in the named range M2 . This problem can be solved in several ways, as explained below. The explanation below also includes a formula that will work in older versions of...

[![Excel formula: Automatic row numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/automatic_row_numbers.png "Excel formula: Automatic row numbers")](https://exceljet.net/formulas/automatic-row-numbers)

### [Automatic row numbers](https://exceljet.net/formulas/automatic-row-numbers)

In this example, the goal is to create automatic row numbers starting in cell B5 that match the data entered in column C. When new data is added to the list, the row numbers should increase as required. If items are deleted, the row numbers should respond accordingly. This has traditionally been a...

[![Excel formula: List all dates in a month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_all_dates_in_a_month.png "Excel formula: List all dates in a month")](https://exceljet.net/formulas/list-all-dates-in-a-month)

### [List all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month)

In this example, we'll use SEQUENCE to generate all dates in a given month. Creating a complete list of dates for a specific month is a common Excel task with many practical applications, from building project timelines and work schedules to generating calendar views and tracking daily data. The...

[![Excel formula: LAMBDA append range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lambda%20append%20range.png "Excel formula: LAMBDA append range")](https://exceljet.net/formulas/lambda-append-range)

### [LAMBDA append range](https://exceljet.net/formulas/lambda-append-range)

Note: this example was created before the VSTACK function and HSTACK function were introduced to Excel. VSTACK combines ranges vertically and HSTACK combines ranges horizontally. These functions are a much easier way to append ranges, but this example is still useful as a way to understand how to...

[![Excel formula: Sequence of custom days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_custom_days.png "Excel formula: Sequence of custom days")](https://exceljet.net/formulas/sequence-of-custom-days)

### [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)

The goal is to generate a series of "custom" days of the week based on a start date entered in cell B5. For example, you might want to list sequential dates for any of the following combinations of days: Mondays, Wednesdays, and Fridays (as shown) Tuesdays, Thursdays, and Saturdays Tuesdays and...

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

[![Excel formula: Hours that overlap specific time blocks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hours_that_overlap_specific_time_blocks.png "Excel formula: Hours that overlap specific time blocks")](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

### [Hours that overlap specific time blocks](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks)

In this example, the goal is to calculate exactly how much of a task, shift, or event falls inside one or more defined blocks of time. The formula accepts a start and end time for the overall task or shift, as well as a start and end time for the block of interest. In the worksheet shown, the Start...

[![Excel formula: Reverse a list or range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/reverse_a_list_or_range.png "Excel formula: Reverse a list or range")](https://exceljet.net/formulas/reverse-a-list-or-range)

### [Reverse a list or range](https://exceljet.net/formulas/reverse-a-list-or-range)

In this example, the goal is to "reverse" the items in the range B5:B14, so that the first item appears last, the second item appears second to last, and so on. When you first encounter a problem like this in Excel, your first instinct might be to sort the values in some way using the SORT function...

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Find and replace multiple values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/find-and-replace-multiple-values.png "Excel formula: Find and replace multiple values")](https://exceljet.net/formulas/find-and-replace-multiple-values)

### [Find and replace multiple values](https://exceljet.net/formulas/find-and-replace-multiple-values)

There is no built-in function to perform a series of find and replace operations in Excel, but you can create a formula that does the same thing. The goal in this example is to replace multiple ("find") values with corresponding ("replace") values in a single "replace all" operation. The text...

[![Excel formula: List nth weekdays of the month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_nth_weekdays_of_the_month.png "Excel formula: List nth weekdays of the month")](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

### [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

In this example, the goal is to generate a list of "nth weekdays of the month" with a formula. For example, the formula should be able to create a list of any of the following: 2nd Tuesdays of the month 1st Fridays of the month 3rd Mondays of the month This is a somewhat challenging problem in...

SEQUENCE function videos
------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/SEQUENCE%20of%20times-Play.png)](https://exceljet.net/videos/sequence-of-times)

### [SEQUENCE of times](https://exceljet.net/videos/sequence-of-times)

In this video, we'll look at how to generate a sequence of times with the SEQUENCE function . The SEQUENCE function can be used to generate numeric sequences of all kinds. Since Excel times are just numbers, SEQUENCE works well for generating times. In the first worksheet, let's generate 9 times,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/New%20dynamic%20array%20functions%20in%20Excel-Play.png)](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

### [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)

In this video, we'll quickly review new Dynamic Array functions in Excel. With the introduction of dynamic array formulas, Excel includes 6 brand new functions that directly leverage dynamic array behavior. Each of these functions is covered in more detail later in the course, so this is just a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/SEQUENCE%20of%20dates-Play.png)](https://exceljet.net/videos/sequence-of-dates)

### [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)

In this video, we'll look at how to generate a sequence of dates with the SEQUENCE function . The SEQUENCE function can be used to generate numeric sequences of all kinds. Since Excel dates are just numbers, SEQUENCE works well for generating dates. In this first worksheet, we have a couple cells...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cell contains number](https://exceljet.net/formulas/cell-contains-number)
    
*   [Generate quarter dates](https://exceljet.net/formulas/generate-quarter-dates)
    
*   [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)
    
*   [Repeat range of values](https://exceljet.net/formulas/repeat-range-of-values)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [Generate random text strings](https://exceljet.net/formulas/generate-random-text-strings)
    
*   [Sum bottom n values with criteria](https://exceljet.net/formulas/sum-bottom-n-values-with-criteria)
    
*   [Multiple matches into separate columns](https://exceljet.net/formulas/multiple-matches-into-separate-columns)
    
*   [Count day of week between dates](https://exceljet.net/formulas/count-day-of-week-between-dates)
    
*   [Split text string to character array](https://exceljet.net/formulas/split-text-string-to-character-array)
    

### Videos

*   [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
    
*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)
    
*   [SEQUENCE of times](https://exceljet.net/videos/sequence-of-times)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

### Links

*   [Microsoft SEQUENCE function documentation](https://support.office.com/en-us/article/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90)
    

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