# List nth weekdays of the month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/list-nth-weekdays-of-the-month

---

[Skip to main content](https://exceljet.net/formulas/list-nth-weekdays-of-the-month#main-content)

[](https://exceljet.net/formulas/list-nth-weekdays-of-the-month#)

*   [Previous](https://exceljet.net/formulas/list-all-dates-in-a-month)
    
*   [Next](https://exceljet.net/formulas/list-workdays-between-dates)
    

[Date series](https://exceljet.net/formulas#Date-series)

List nth weekdays of the month
==============================

by Dave Bruns · Updated 8 Dec 2025

Related functions 
------------------

[LET](https://exceljet.net/functions/let-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[FILTER](https://exceljet.net/functions/filter-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[TEXT](https://exceljet.net/functions/text-function)

[EDATE](https://exceljet.net/functions/edate-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8025/download?token=31QYKUkY)
 (29.15 KB)

![Excel formula: List nth weekdays of the month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/list_nth_weekdays_of_the_month.png "Excel formula: List nth weekdays of the month")

Summary
-------

To generate a list of nth weekdays (i.e. 2nd Tuesdays of the month, 1st Fridays of the month, etc.) you can use a formula based on the [LET](https://exceljet.net/functions/let-function)
, [SEQUENCE](https://exceljet.net/functions/sequence-function)
, [FILTER](https://exceljet.net/functions/filter-function)
, and [BYROW](https://exceljet.net/functions/byrow-function)
 functions. In the worksheet shown, the formula in cell D5 is:

    =LET(
    start,EOMONTH(TODAY(),-1)+1,
    months,B5,
    n,B11,
    dow,B8,
    end,EDATE(start,months)-1,
    dates,SEQUENCE(end-start+1,1,start,1),
    fdates,FILTER(dates,TEXT(dates,"dddd")=dow),
    instance,BYROW(fdates,LAMBDA(d,SUM((TEXT(d,"mmyy")=TEXT(fdates,"mmyy"))*(d>=fdates)))),
    FILTER(fdates,instance=n)
    )

The result is a list of "2nd Tuesdays of the month" for the next 12 months, starting in the current month. By changing values for the day of week (_dow_) and _n_, you can use the same formula to list other nth weekdays in a month.

Explanation 
------------

In this example, the goal is to generate a list of "nth weekdays of the month" with a formula. For example, the formula should be able to create a list of any of the following:

*   2nd Tuesdays of the month
*   1st Fridays of the month
*   3rd Mondays of the month

This is a somewhat challenging problem in Excel, because there is no built-in function to help you find, say, the 2nd Tuesday of a given month. However, Excel offers many other powerful functions that can be used to craft a custom solution. At a high level, the approach I've taken here to solve this problem looks like this:

1.  Define a start date and end date
2.  Generate a list of _all dates_ between these dates
3.  Filter the list of dates by the supplied "day of week"
4.  Calculate an instance number for each date
5.  Filter the dates again by the desired instance number

This is a "brute force" approach, in that we don't try to do anything clever when we create our initial list of dates. Instead, we simply generate _all the dates_ in the date range, then we come back and selectively remove dates we don't want until we are left with a final list of desired dates.

> Note: If you just need a _single_ nth day in a month (i.e., the 3rd Friday in a given month), use the formula [on this page](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
> .

### Key functions

This is a more advanced formula based on several newer functions in Excel. If you are unfamiliar with these functions, use the links below for reference:

*   [LET function](https://exceljet.net/functions/let-function)
    
*   [SEQUENCE function](https://exceljet.net/functions/sequence-function)
    
*   [FILTER function](https://exceljet.net/functions/filter-function)
    
*   [LAMBDA function](https://exceljet.net/functions/lambda-function)
    
*   [BYROW function](https://exceljet.net/functions/byrow-function)
    

> We also have video training on [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
> .

### Define a start and end date

The start and end date are defined in the first six lines of the formula here:

    =LET(
    start,EOMONTH(TODAY(),-1)+1,
    months,B5,
    n,B11,
    dow,B8,
    end,EDATE(start,months)-1,
    

We open with the [LET function](https://exceljet.net/functions/let-function)
, which allows us to declare and define a number of variables. The first variable is "start", which we define to be the [first day of the current month](https://exceljet.net/formulas/get-first-day-of-month)
 like this:

    EOMONTH(TODAY(),-1)+1 // start

Moving on, we then declare and assign values to "months" (12), "n" (2), and "dow" ("Tuesday"). The abbreviation "dow" stands for "day of week". Finally, we use the [EDATE function](https://exceljet.net/functions/edate-function)
 to define a value for "end":

    EDATE(start,months)-1 // end

Here, we use EDATE to move 12 months forward from the start date (defined above as the 1st day in the current month), then we subtract 1 day to end up on the last day of the previous month. This gives us a date range that spans the full number of months.

At this point, we are done with set-up and have everything we need to begin generating dates.

### Generate a list of all dates

Next, we use the [SEQUENCE](https://exceljet.net/functions/sequence-function)
 function to generate a list of all dates between _start_ and _end_ like this:

    SEQUENCE(end-start+1,1,start,1)

This works because [Excel dates](https://exceljet.net/glossary/excel-date)
 are stored as large serial numbers, and SEQUENCE is designed to generate numeric arrays. The resulting array of dates is assigned to the variable "dates". For more details, see [Sequence of days](https://exceljet.net/formulas/sequence-of-days)
.

### Filter the list of dates by day of week

Next, we need to filter the list of days by the "target" day of the week, previously defined as "dow" above, and given the value "Tuesday" from cell B8. To filter the list, we use the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    FILTER(dates,TEXT(dates,"dddd")=dow)

Essentially, FILTER removes all dates that are not Tuesdays, by using the [TEXT function](https://exceljet.net/functions/text-function)
 to get the weekday name of each date and testing the name against the value assigned to _dow_ ("Tuesday")_._ The resulting [array](https://exceljet.net/glossary/array)
 of dates is assigned to the variable "fdates" which stands for "filtered dates".

### Calculate an instance number for each date

Next, we perform the trickiest step in the formula, which is to calculate an "instance" number for each date in _fdates_. We do this with the [BYROW function](https://exceljet.net/functions/byrow-function)
 and like this:

    BYROW(fdates,LAMBDA(d,SUM((TEXT(d,"mmyy")=TEXT(fdates,"mmyy"))*(d>=fdates))))

The BYROW function applies a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each row of a given array and returns one result per row. In this case, we are using BYROW to process _fdates_, the array of Tuesdays defined in the previous step. Inside the LAMBDA function "d" is a variable that represents a single date in _fdates_. The calculation that is applied to each row looks like this:

    SUM((TEXT(d,"mmyy")=TEXT(fdates,"mmyy"))*(d>=fdates))

At a high level, BYROW works through each date (d) in _fdates_ and asks two questions:

1.  Is the date (d) in the same year and month as other filtered dates (fdates)?
2.  is the date (d) greater than or equal to the other dates in _fdates?_

The logic for the first question is based on the [TEXT function](https://exceljet.net/functions/text-function)
 here:

    TEXT(d,"mmyy")=TEXT(fdates,"mmyy"))

The logic to answer the second question is here:

    (d>=fdates)

Each expression results in an array of TRUE and FALSE values. The two expressions are joined by multiplication (\*) which creates [AND logic using Boolean algebra](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
. The math operation automatically converts the TRUE and FALSE values to 1s and 0s, and the  SUM function sums the results. It is important to understand that this operation is performed on _each date (d)_ in _fdates_. For the first Tuesday in a month, the SUM function returns 1, for the second Tuesday, SUM returns 2, and so on. The final array returned by the BYROW function looks like this:

    {1;2;3;4;1;2;3;4;5;1;2;3;4;1;2;3;4;1;2;3;4;5;1;2;3;4;1;2;3;4;1;2;3;4;5;1;2;3;4;1;2;3;4;1;2;3;4;5;1;2;3;4}

In this array, each number corresponds to the "nth occurrence" of a Tuesday in a month across the full date range. The numbers reset to 1 when the month changes, so the 2's in the array represent "Second Tuesdays". The array is then assigned to the variable "instance".

### Filter dates again by desired instance number

The last step in the formula is to filter the dates again by the "target" instance number like this:

    FILTER(fdates,instance=n)

Here the [FILTER function](https://exceljet.net/functions/filter-function)
 is configured to filter fdates. With _n_ previously defined as 2, we have:

    FILTER(fdates,instance=2)

The final result is a list of all second Tuesdays in the date range. This formula is dynamic. If the number of months (_month_), day of week (_dow_), or instance number (_n_) is changed, the formula will return a new set of results.

Legacy Excel
------------

In older versions of Excel, we don't have functions like LET, FILTER, BYCOL, LAMBDA, and SEQUENCE. However, it is possible to build a list of "nth weekdays of the month" with some [helper columns](https://exceljet.net/glossary/helper-column)
 and a more manual approach. You can see this approach in the workbook below:

![Solution for second Tuesdays of the month in older versions of Excel](https://exceljet.net/sites/default/files/images/formulas/inline/list_nth_weekdays_of_the_month_legacy_excel.png "Solution for second Tuesdays of the month in older versions of Excel")

The formula in cell B11 to calculate a first-of-month date in the current month is based on the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 and the [TODAY function](https://exceljet.net/functions/today-function)
:

    =EOMONTH(TODAY(),-1)+1

You can read more about this formula here: [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
. The formula to calculate the end date in B14 is:

    =EDATE(B11,B5)-1

The formula to get the first Tuesday of the month in cell D5 is interesting:

    =B11+MATCH(B8,TEXT(B11+{0,1,2,3,4,5,6},"dddd"),0)-1

Basically, we need a formula that will calculate the first Tuesday after (and including) the start date. You can find a full explanation of this tricky formula here: [Get next day of week](https://exceljet.net/formulas/get-next-day-of-week)
. The formula in cell E5 to get the day name from the date in column D is based on the [TEXT function](https://exceljet.net/functions/text-function)
 with the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "dddd".

    =TEXT(D5,"dddd")

The formula in F6 to calculate "instance" is:

    =IF(MONTH(D6)=MONTH(D5),F5+1,1)

Here, we use the [IF function](https://exceljet.net/videos/the-if-function)
 with the [MONTH function](https://exceljet.net/functions/month-function)
 to compare the month in the current row. If the month is the same, we increment by 1. If not, we reset the number to 1. As these formulas are copied down, they create a list of all the Tuesdays after the start date along with an instance number. To get a list of just the 2nd Tuesdays, use the filter to filter on rows where the instance is 2.

Related formulas
----------------

[![Excel formula: Sequence of days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_days.png "Excel formula: Sequence of days")](https://exceljet.net/formulas/sequence-of-days)

### [Sequence of days](https://exceljet.net/formulas/sequence-of-days)

The goal is to generate a series of sequential dates with a formula. In the current version of Excel, the easiest method is to use the SEQUENCE function. SEQUENCE can return all dates at the same time into a range on the worksheet. In older versions of Excel without the SEQUENCE function, you can...

[![Excel formula: Semimonthly pay schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/semimonthly_pay_schedule.png "Excel formula: Semimonthly pay schedule")](https://exceljet.net/formulas/semimonthly-pay-schedule)

### [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)

In this example, the goal is to create a list of pay dates that follow a semimonthly schedule. A semimonthly pay schedule means employees are paid twice a month, usually on fixed dates such as the 1st and 15th or the 15th and the last day of the month. This results in 24 pay periods over the course...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

[![Excel formula: Sequence of weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_weekends.png "Excel formula: Sequence of weekends")](https://exceljet.net/formulas/sequence-of-weekends)

### [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)

The goal is to generate a series of sequential weekend days (Saturday and Sunday) with a formula. The start date is entered in cell B5. The number of dates to create (n) is entered in cell B8. If either of these two values are changed, a new list of weekend dates should be generated. In the current...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Get nth day of week in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get-nth-day-of-week-in-month_0.png "Excel formula: Get nth day of week in month")](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

### [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)

This example demonstrates how to calculate the nth occurrence of a specific day of the week within a month. For instance, you might need to find the 2nd Tuesday, the 4th Wednesday, or the 1st Friday of any given month. The worksheet is structured with the starting date in column B, the target day...

Related functions
-----------------

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20due%20dates%20with%20WORKDAY_Thumb.png)](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

### [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

In this video we'll look at how to calculate due dates with the WORKDAY and WORKDAY.INTL functions. The WORKDAY function returns a date in the future or past that takes into account weekends and, optionally, holidays. You can use the WORKDAY function to calculate things like ship dates, delivery...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sequence of days](https://exceljet.net/formulas/sequence-of-days)
    
*   [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    
*   [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [Get nth day of week in month](https://exceljet.net/formulas/get-nth-day-of-week-in-month)
    

### Functions

*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
    

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