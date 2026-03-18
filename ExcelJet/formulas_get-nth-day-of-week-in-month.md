# Get nth day of week in month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-nth-day-of-week-in-month

---

[Skip to main content](https://exceljet.net/formulas/get-nth-day-of-week-in-month#main-content)

[](https://exceljet.net/formulas/get-nth-day-of-week-in-month#)

*   [Previous](https://exceljet.net/formulas/get-next-scheduled-event)
    
*   [Next](https://exceljet.net/formulas/get-nth-day-of-year)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get nth day of week in month
============================

by Dave Bruns · Updated 11 Dec 2025

Related functions 
------------------

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[MOD](https://exceljet.net/functions/mod-function)

[LET](https://exceljet.net/functions/let-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[MONTH](https://exceljet.net/functions/month-function)

[NA](https://exceljet.net/functions/na-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9453/download?token=MUyIG9Se)
 (21.45 KB)

![Excel formula: Get nth day of week in month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get-nth-day-of-week-in-month_0.png "Excel formula: Get nth day of week in month")

Summary
-------

To get the nth day of week in a month (i.e., the first Tuesday, third Tuesday, fourth Thursday, etc.), you can use a formula based on the [WEEKDAY](https://exceljet.net/functions/weekday-function)
 and [MOD](https://exceljet.net/functions/mod-function)
 functions. In the example shown, the formula in E5 is:

    =B5+MOD(C5-WEEKDAY(B5),7)+(D5-1)*7
    

As the formula is copied down it returns the nth occurrence of the target day of the week (dow) in the month for each row, using the date in column B as the starting date, the target day of week in column C, and the nth occurrence in column D. The target day of week is given as a number between 1 and 7, where 1 represents Sunday and 7 represents Saturday.

> This is a tricky formula to understand. See below for [variations based on the LET function](https://exceljet.net/formulas/get-nth-day-of-week-in-month#using-let-for-clarity)
> , which make the formula easier to read and understand.

Generic formula
---------------

    =date+MOD(dow-WEEKDAY(date),7)+(n-1)*7

Explanation 
------------

This example demonstrates how to calculate the nth occurrence of a specific day of the week within a month. For instance, you might need to find the 2nd Tuesday, the 4th Wednesday, or the 1st Friday of any given month. The worksheet is structured with the starting date in column B, the target day of week (dow) as a number in column C, and the occurrence number (n) in column D. Note that the date is assumed to be the first day of the month. The article below explains in detail how the formula in the worksheet shown works. It also shows how to rewrite the formula with the LET function to improve transparency and to trap potential problems.

> This example shows how to get one specific day of the week in a month. If you instead want to list all nth weekdays in a given date range, see the [example on this page](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)
> .

### Table of contents

*   [The WEEKDAY function](https://exceljet.net/formulas/get-nth-day-of-week-in-month#the-weekday-function)
    
*   [How the core formula works](https://exceljet.net/formulas/get-nth-day-of-week-in-month#how-the-core-formula-works)
    
*   [Using LET for clarity](https://exceljet.net/formulas/get-nth-day-of-week-in-month#using-let-for-clarity)
    
*   [Normalizing to the first of the month](https://exceljet.net/formulas/get-nth-day-of-week-in-month#normalizing-to-the-first-of-the-month)
    
*   [Guarding against non-existent dates](https://exceljet.net/formulas/get-nth-day-of-week-in-month#guarding-against-non-existent-dates)
    

### The WEEKDAY function

The formulas on this page depend on the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
, so it is important to understand how it works. When given a date, WEEKDAY returns a number representing the day of the week for a given date. By default, WEEKDAY returns numbers 1 through 7, where 1 represents Sunday, and 7 represents Saturday:

| Day | Number |
| --- | --- |
| Sunday | 1   |
| Monday | 2   |
| Tuesday | 3   |
| Wednesday | 4   |
| Thursday | 5   |
| Friday | 6   |
| Saturday | 7   |

For example, `=WEEKDAY("6-Dec-2025")` returns 7, because December 6th, 2025, is a Saturday, and `=WEEKDAY("7-Dec-2025")` returns 1, because December 7th, 2025, is a Sunday. We use the WEEKDAY function in the formulas below to figure out what day of week a particular date falls on. We also use the same numeric codes above to specify the target day of week (dow) that we want to find. For example, if the target day of week is Tuesday, we would use the number 3, since Tuesday is the 3rd day of the week in WEEKDAY's default numbering scheme.

### How the core formula works

At a high level, the formula starts on the first day of the month, calculates an offset to reach the first target day, then adds the appropriate number of complete weeks to arrive at the nth occurrence of the target. The start date is in cell B5, the target day is in cell C5, and the value for n comes from cell D5. The formula in E5 looks like this:

    =B5+MOD(C5-WEEKDAY(B5),7)+(D5-1)*7
    

First, we calculate the offset to the target day of week using the [MOD function](https://exceljet.net/functions/mod-function)
 and the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
 like this:

    MOD(C5-WEEKDAY(B5),7)
    

This is the trickiest part of the formula to understand. The MOD function is used here to calculate a repeating pattern of numbers (0-6), similar to how a clock wraps around from 12 back to 1. By taking the difference between the target day of week (C5) and the current day of week (WEEKDAY(B5)), then wrapping that difference with MOD, we get the number of days needed to move forward to reach the target day. For example, if the starting date is a Monday (2) and we want Tuesday (3), the offset is 1 day. If the starting date is a Thursday (5) and we want Tuesday (3), MOD wraps the calculation to give us 4 days forward to the next Tuesday.

Once we have the offset, we add it to the starting date in B5 to get the first occurrence of the target day of the week:

    B5+MOD(C5-WEEKDAY(B5),7)
    

This moves us from the given starting date to the first occurrence of the target day of the week on or after that date. The final step is to add the appropriate number of complete weeks to reach the nth occurrence, which is done by multiplying the difference between the nth occurrence and 1 by 7:

    +(D5-1)*7
    

Since we've already landed on the first occurrence, we add (n-1) complete weeks to reach the desired occurrence. For the 1st occurrence, we add zero weeks. For the 2nd occurrence, we add 1 week (7 days), and so on.

### Using LET for clarity

The formula above can be rewritten using the [LET function](https://exceljet.net/functions/let-function)
 to make the logic more transparent with named variables like this:

    =LET(
        date, B5,
        dow, C5,
        n, D5,
        offset, MOD(dow-WEEKDAY(date),7),
        date + offset + (n-1)*7
    )
    

> Use the [keyboard shortcut](https://exceljet.net/shortcuts)
>  Control + Shift + U to expand the formula bar.

This version makes the formula self-documenting. Each step has a clear name: `date` is the starting date, `dow` is the target day of week, `n` is the occurrence we want, and `offset` is the calculated adjustment needed to reach the target day. The final line is the formula we saw earlier, but now it is clear what each part does:

    date + offset + (n-1)*7
    

### Normalizing to the first of the month

The formula above assumes that the date provided is always the first of a month, but it doesn't verify this requirement. If you provide a date that is not the first, the formula may return an incorrect result. To trap and prevent this potential problem, we can extend the LET version to normalize any incoming date to the first of the month, like this:

    =LET(
        date, B5,
        dow, C5,
        n, D5,
        first, EOMONTH(date,-1)+1,
        offset, MOD(dow-WEEKDAY(first),7),
        first + offset + (n-1)*7
    )
    

The variable `first` calculates the [first day of the month](https://exceljet.net/formulas/get-first-day-of-month)
 using EOMONTH, which returns the last day of the previous month, plus one day. This ensures the formula always starts from the beginning of the month, regardless of what date is provided.

### Guarding against non-existent dates

Another problem with the formula above is that it does not guard against cases where the nth occurrence doesn't exist in a given month. For example, asking for the 5th Tuesday in a month that only has 4 Tuesdays will cause the formula to return an incorrect date in the following month. To prevent this, you can add a check that returns an error when the result falls outside the target month:

    =LET(
        date, B5,
        dow, C5,
        n, D5,
        first, EOMONTH(date,-1)+1,
        offset, MOD(dow-WEEKDAY(first),7),
        result, first + offset + (n-1)*7,
        IF(MONTH(result)=MONTH(date), result, NA())
    )
    

The final [IF statement](https://exceljet.net/functions/if-function)
 compares the month of the calculated result with the month of the original date. If they match, the result is valid and is returned. If they don't match, it means we have landed on a date in the next month, and the formula returns a #N/A error with the [NA function](https://exceljet.net/functions/na-function)
 to make it clear that the requested occurrence doesn't exist in that month. If you prefer not to see an error, you could return a custom message or an empty string ("") instead.

> Note: The LET versions of the formula return the same result as the original formula; they just do so in a more transparent way. The last two formulas add functionality.

Related formulas
----------------

[![Excel formula: List nth weekdays of the month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_nth_weekdays_of_the_month.png "Excel formula: List nth weekdays of the month")](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

### [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)

In this example, the goal is to generate a list of "nth weekdays of the month" with a formula. For example, the formula should be able to create a list of any of the following: 2nd Tuesdays of the month 1st Fridays of the month 3rd Mondays of the month This is a somewhat challenging problem in...

[![Excel formula: Get first day of month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_day_of_month.png "Excel formula: Get first day of month")](https://exceljet.net/formulas/get-first-day-of-month)

### [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)

In this example, the goal is to get the first day of the month based on any valid date. This problem can be solved by combining the EOMONTH function with simple addition. The EOMONTH Function The EOMONTH function returns the last day of the month, a given number of months in the past or future. For...

[![Excel formula: Get last working day in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20working%20day%20in%20month.png "Excel formula: Get last working day in month")](https://exceljet.net/formulas/get-last-working-day-in-month)

### [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)

Working from the inside out, the EOMONTH function gets the last day of month of any date. To this result, we add 1, which results in the first day of the next month. This date goes into WORKDAY function as the "start date", along with -1 for "days". The WORKDAY function automatically steps back 1...

[![Excel formula: Get last weekday in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20last%20weekday%20in%20month.png "Excel formula: Get last weekday in month")](https://exceljet.net/formulas/get-last-weekday-in-month)

### [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)

First, this formula determines the first day of the next month \*after\* a given date. It does this my using EOMONTH to get the last day of the month, then adding one day: =EOMONTH(B5,0)+1 Next, the formula calculates the number of days required to "roll back" to the last requested weekday in the...

Related functions
-----------------

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel NA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20na%20function.png "Excel NA function")](https://exceljet.net/functions/na-function)

### [NA Function](https://exceljet.net/functions/na-function)

The Excel NA function returns the #N/A error. #N/A means "not available" or "no value available". You can use the NA function to display the #N/A error when information is missing.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [List nth weekdays of the month](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    
*   [Get last working day in month](https://exceljet.net/formulas/get-last-working-day-in-month)
    
*   [Get last weekday in month](https://exceljet.net/formulas/get-last-weekday-in-month)
    

### Functions

*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [NA Function](https://exceljet.net/functions/na-function)
    

### Links

*   [Chip Pearson's page on date and time functions](http://www.cpearson.com/Excel/DateTimeWS.htm)
    

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