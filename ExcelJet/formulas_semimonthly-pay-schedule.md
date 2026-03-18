# Semimonthly pay schedule - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/semimonthly-pay-schedule

---

[Skip to main content](https://exceljet.net/formulas/semimonthly-pay-schedule#main-content)

[](https://exceljet.net/formulas/semimonthly-pay-schedule#)

*   [Previous](https://exceljet.net/formulas/list-workdays-between-dates)
    
*   [Next](https://exceljet.net/formulas/sequence-of-custom-days)
    

[Date series](https://exceljet.net/formulas#Date-series)

Semimonthly pay schedule
========================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[LET](https://exceljet.net/functions/let-function)

[DAY](https://exceljet.net/functions/day-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[WORKDAY](https://exceljet.net/functions/workday-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8011/download?token=PCVKhM9w)
 (32.57 KB)

![Excel formula: Semimonthly pay schedule](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/semimonthly_pay_schedule.png "Excel formula: Semimonthly pay schedule")

Summary
-------

To create a list of pay dates that occur twice a month on regular days, you can use a formula based on the [FILTER function](https://exceljet.net/functions/filter-function)
 and the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. In the example shown, the formula in cell D5 is:

    =LET(dates,SEQUENCE(B8-B5+1,1,B5),FILTER(dates,(DAY(dates)=1)+(DAY(dates)=15)))

The result is a list of the 12 pay dates on the 1st and 15th of each month between January 1, 2023, and June 30, 2023. See below for an explanation and for an alternative formula for the 15th and last day of the month.

_Note: if you just need a biweekly pay schedule, where employees are paid every other week on a given day,_ [_see this example_](https://exceljet.net/formulas/biweekly-pay-schedule)
_._

Generic formula
---------------

    =LET(dates,SEQUENCE(end-start+1,1,start),FILTER(dates,(DAY(dates)=1)+(DAY(dates)=15)))

Explanation 
------------

In this example, the goal is to create a list of pay dates that follow a semimonthly schedule. A semimonthly pay schedule means employees are paid twice a month, usually on fixed dates such as the 1st and 15th or the 15th and the last day of the month. This results in 24 pay periods over the course of a year. For example, in the worksheet shown above, payroll dates are the 1st and 15th of each month. In the worksheet shown above, the formula solves this problem in two steps. Step 1 is to generate a list of all dates between the start date and the end date. Step 2 is to filter those dates so that only those that land on the 1st and 15th remain. The formula in cell D5 looks like this:

    =LET(dates,SEQUENCE(B8-B5+1,1,B5),FILTER(dates,(DAY(dates)=1)+(DAY(dates)=15)))

### Background study

If you are not familiar with the SEQUENCE function, these links will help you get up to speed quickly:

*   [How to use the SEQUENCE function](https://exceljet.net/functions/sequence-function)
     \- overview
*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
     - 3 min video
*   [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)
     - 3 min video
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
     - video training

### Generating the dates

The first step is to generate all the dates, and this is done with the SEQUENCE function here:

    SEQUENCE(B8-B5+1,1,B5) // generate all dates

The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 generates numeric sequences. [Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
, so this part of the formula evaluates like this:

    =SEQUENCE(B8-B5+1,1,B5)
    =SEQUENCE(45107-44927+1,1,44927)
    =SEQUENCE(181,1,44927)

Essentially, we are asking SEQUENCE for 181 sequential dates that start on 44927, which is the serial number for January 1, 2023, in Excel's date system. The SEQUENCE generates an array that contains 181 dates, and these are defined as the variable "date" by the [LET function](https://exceljet.net/functions/let-function)
:

    =LET(dates,SEQUENCE(B8-B5+1,1,B5)

We use the LET function here to avoid redundancy. We need to use the full range of dates more than once in the formula, and creating this array once and assigning it to _dates_ means the operation does not need to be repeated. This makes the formula easier to read and understand, and also improves performance.

### Filtering the dates

At this point, we have a list of all dates within the target date range, and we have named the list _dates_. The next step is to filter the list to extract just the dates we are about: the paydays that occur on the 1st and 15th of each month. To do this, we use the [FILTER function](https://exceljet.net/functions/filter-function)
, which is configured like this:

    FILTER(dates,(DAY(dates)=1)+(DAY(dates)=15))

The _array_ in FILTER is given as _dates_, which contains all dates between January 1, 2023, and June 30, 2023. The _include_ argument is set up like this:

    (DAY(dates)=1)+(DAY(dates)=15) // 1st and 15th only

Here, we use the [DAY function](https://exceljet.net/functions/day-function)
 to extract just the day from the date, then use [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
 with addition to construct an OR condition. In other words, we are filtering on dates that land on the 1st or the 15th day of each month. The final result from FILTER is an array of the 12 dates that land on the 1st and 15th of each month in the target date range. For more information on using addition (+) to create "OR logic", see this short video: [Array formulas with AND and OR logic](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
.

### Alternative formula - 15th and last

The formula above can be easily adapted to return payroll dates that follow different rules. For example, to return a list of payroll dates that fall on the 15th and _last_ day of each month, you can use a formula like this:

    =LET(dates,SEQUENCE(B8-B5+1,1,B5),FILTER(dates,(DAY(dates)=15)+(dates=EOMONTH(dates,0))))

The only difference in this formula is that the _include_ logic inside FILTER has been adjusted like this:

    (DAY(dates)=15)+(dates=EOMONTH(dates,0)) // 15th and last

The test for the 15th is the same. To test each for an "end of month" date, we use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
. Inside, EOMONTH, we provide 0 for months to return the last day of the month. As before, the two expressions are joined with addition (+) to create [OR logic](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
. The screen below shows the result:

![Formula for semimonthly pay dates on the 15th and last day of month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/semimonthly_pay_schedule_alternative.png "Formula for semimonthly pay dates on the 15th and last day of month")

### WORKDAY adjustment

The formulas above work well, but they don't check what day of the week pay dates land on. In the real world, companies often adjust pay dates that land on a holiday or weekend to the _previous_ business day. So, for example, if the 15th of the month lands on a Saturday, the date is adjusted to Friday the 14th. To adjust dates that land on weekends or holidays back to the _previous_ working day, you can use the WORKDAY function with a special configuration like this:

    =WORKDAY(date+1,-1)

Essentially, we move forward one day, and then ask WORKDAY for the [previous workday](https://exceljet.net/formulas/previous-working-day)
 by providing -1 for _days_. In this configuration, WORKDAY returns the original date if it is a working day. Otherwise, WORKDAY steps back one day at a time and returns the first working day found. You can see the result in the worksheet below:

![Using the WORKDAY function to adjust final dates](https://exceljet.net/sites/default/files/images/formulas/inline/semimonthly_pay_schedule_with_workday_adustment.png "Using the WORKDAY function to adjust final dates")

The original results from the "1st and 15h" formula appear in column D. Column F shows the adjusted dates. Notice that four dates have been shifted back to the _previous_ working day.

### All in one formula

It is possible to combine the formulas above into a single formula by piping the results from FILTER directly into the WORKDAY function like this:

    =LET(dates,SEQUENCE(B8-B5+1,1,B5),WORKDAY(FILTER(dates,(DAY(dates)=1)+(DAY(dates)=15))+1,-1))

This formula will return the same results seen in column F, all in one step. In the same way, you can use the formula below to list adjusted dates for the 15th and last day of the month, like this:

    =LET(dates,SEQUENCE(B8-B5+1,1,B5),WORKDAY(FILTER(dates,(DAY(dates)=15)+(dates=EOMONTH(dates,0)))+1,-1))

In both formulas, we've nested the FILTER formula inside the [WORKDAY function](https://exceljet.net/functions/workday-function)
 as the _start\_date_ argument. This causes all the dates returned by FILTER to go through the WORKDAY, and only dates that land on non-working days are adjusted.

_Note: To simplify things, I have not provided holidays to WORKDAY, but you can easily add this optional argument to make WORKDAY skip official holidays. See_ [_Previous working day_](https://exceljet.net/formulas/previous-working-day)
 _for an example._

### Legacy Excel

In older versions of Excel, there is no SEQUENCE function or FILTER function, so we can't use the approach explained above. One option is to hardcode the first date into cell D5, then enter this formula in cell D6 and drag copy it down as needed:

    =IF(DAY(D5)=1,D5+14,EOMONTH(D5,0)+1)

![Formula for semimonthly pay dates in older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/semimonthly_pay_schedule_legacy_excel.png "Formula for semimonthly pay dates in older versions of Excel")

This formula uses the [IF function](https://exceljet.net/functions/if-function)
 and the [DAY function](https://exceljet.net/functions/day-function)
 to check the date in the "cell above" to see if it is the first of the month. If it is, IF returns the date + 14 days. If it is _not_ the first of the month, we use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 to move to the end of the month, then add one day to land on the first day of the next month.

### Alternative

To list pay dates that fall on the 15th and last day of the month in older versions of Excel, you can use the same basic process and a formula like this:

    =IF(DAY(D5)=15,EOMONTH(D5,0),D5+15)

![Alternative formula for semimonthly pay dates in older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/semimonthly_pay_schedule_alternative_legacy_excel.png "Alternative formula for semimonthly pay dates in older versions of Excel")

This formula assumes that the first date in D5 is either the 15th of a month or the last day of a month. As before, this formula uses the IF and DAY functions to check the date in the "cell above". If the day is the 15th, we use the EOMONTH function to move to the end of the month. If the day is not the 15th, we assume it is the last day of the month and add 15 days.

Related formulas
----------------

[![Excel formula: Biweekly pay schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/biweekly_pay_schedule.png "Excel formula: Biweekly pay schedule")](https://exceljet.net/formulas/biweekly-pay-schedule)

### [Biweekly pay schedule](https://exceljet.net/formulas/biweekly-pay-schedule)

In this example, the goal is to create a list of pay dates that follow a biweekly schedule. A biweekly pay schedule means employees are paid every two weeks on a given day of the week. Each pay period is 14 days, and there are usually 26 pay dates per year, though occasionally 27 depending on the...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

[![Excel formula: Sequence of weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_weekends.png "Excel formula: Sequence of weekends")](https://exceljet.net/formulas/sequence-of-weekends)

### [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)

The goal is to generate a series of sequential weekend days (Saturday and Sunday) with a formula. The start date is entered in cell B5. The number of dates to create (n) is entered in cell B8. If either of these two values are changed, a new list of weekend dates should be generated. In the current...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/FILTER%20function%20basic%20example-play.png)](https://exceljet.net/videos/filter-function-basic-example)

### [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)

In this video, we’ll set up the FILTER function with a basic example. Filtering to extract data based on matching criteria is a traditionally hard problem in Excel. However, the new FILTER function makes this task much easier. The FILTER function is designed to extract data from a list or table...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Array%20formulas%20with%20AND%20and%20OR%20logic-play.png)](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)

### [Array formulas with AND and OR logic](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)

In this video, we'll look at how to use Boolean algebra in array formulas for AND and OR logic. In an earlier video, I showed how AND logic corresponds to multiplication and OR logic corresponds to addition. Let's look at how to apply this in an array formula. In the first worksheet, we want to sum...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Biweekly pay schedule](https://exceljet.net/formulas/biweekly-pay-schedule)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    
*   [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [DAY Function](https://exceljet.net/functions/day-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [FILTER function basic example](https://exceljet.net/videos/filter-function-basic-example)
    
*   [Array formulas with AND and OR logic](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
    

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