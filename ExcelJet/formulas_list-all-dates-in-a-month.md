# List all dates in a month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/list-all-dates-in-a-month

---

[Skip to main content](https://exceljet.net/formulas/list-all-dates-in-a-month#main-content)

[](https://exceljet.net/formulas/list-all-dates-in-a-month#)

*   [Previous](https://exceljet.net/formulas/biweekly-pay-schedule)
    
*   [Next](https://exceljet.net/formulas/list-nth-weekdays-of-the-month)
    

[Date series](https://exceljet.net/formulas#Date-series)

List all dates in a month
=========================

by Dave Bruns · Updated 23 Jun 2025

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

[DAY](https://exceljet.net/functions/day-function)

[LET](https://exceljet.net/functions/let-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9199/download?token=XjjShdM6)
 (25.05 KB)

![Excel formula: List all dates in a month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/list_all_dates_in_a_month.png "Excel formula: List all dates in a month")

Summary
-------

To generate a list of all dates in a given month, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. In the example shown, the formula in D5 is:

    =SEQUENCE(DAY(EOMONTH(B5,0)),,EOMONTH(B5,-1)+1)

With the date May 15, 2025, in cell B5, the result is a list of the 31 dates in May 2025. The output is fully dynamic. If the date in B5 is changed to another date, like 9-Jun-2025, the formula will list the 30 dates in June 2025.

> This formula returns all dates in a given month. To list only workdays, see [this formula](https://exceljet.net/formulas/sequence-of-workdays)
> . SEQUENCE is only available in Excel 2021 and later. [Later in the article](https://exceljet.net/formulas/list-all-dates-in-a-month#approach-for-older-versions-of-excel)
> , I cover a workaround formula to use in older versions of Excel.

Generic formula
---------------

    =SEQUENCE(DAY(EOMONTH(A1)),,EOMONTH(A1,-1)+1)

Explanation 
------------

In this example, we'll use SEQUENCE to generate all dates in a given month. Creating a complete list of dates for a specific month is a common Excel task with many practical applications, from building project timelines and work schedules to generating calendar views and tracking daily data. The input is any date within the target month (it doesn't matter which specific day), and the output is a dynamic list that automatically adjusts when you change the input date. The technique works because Excel [stores dates as serial numbers](https://exceljet.net/glossary/excel-date)
, allowing SEQUENCE to count through them just like any other numeric sequence. Although the core of the solution is SEQUENCE, it's also interesting how we use the DAY and EOMONTH functions to calculate the inputs to SEQUENCE. The EOMONTH function is particularly useful and comes up in all kinds of other formulas. The DAY function (together with EOMONTH) is a clever way to get the total days in a month.

### Table of Contents

*   [The SEQUENCE function](https://exceljet.net/formulas/list-all-dates-in-a-month#the-sequence-function)
    
*   [SEQUENCE with dates](https://exceljet.net/formulas/list-all-dates-in-a-month#sequence-with-dates)
    
*   [SEQUENCE to list all dates in a month](https://exceljet.net/formulas/list-all-dates-in-a-month#sequence-to-list-all-dates-in-a-month)
    
*   [LET version of the formula](https://exceljet.net/formulas/list-all-dates-in-a-month#let-version-of-the-formula)
    
*   [All dates between two dates](https://exceljet.net/formulas/list-all-dates-in-a-month#all-dates-between-two-dates)
    
*   [Current month dates with TODAY function](https://exceljet.net/formulas/list-all-dates-in-a-month#current-month-dates-with-today-function)
    
*   [Approach for older versions of Excel](https://exceljet.net/formulas/list-all-dates-in-a-month#approach-for-older-versions-of-excel)
    
*   [Useful links](https://exceljet.net/formulas/list-all-dates-in-a-month#useful-links)
    

### The SEQUENCE function

The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 can generate numeric sequences using a generic syntax like this:

    =SEQUENCE(rows,[columns],[start],[step])

_Rows_ is the number of rows to return, _columns_ is the number of columns to return, _start_ is the starting value, and _step_ is the increment to use between values. The arguments _columns_, _step_, and _start_ all default to 1. For example, we can ask for the numbers 1-10 like this:

    =SEQUENCE(10) // returns {1;2;3;4;5;6;7;8;9;10}

To get the numbers 51-60, we can set start to 50:

    =SEQUENCE(10,,50) // returns {50;51;52;53;54;55;56;57;58;59}

In both formulas above, SEQUENCE generates an array of numbers that will [spill](https://exceljet.net/glossary/spill)
 into 10 rows. 

### SEQUENCE with dates

Because dates are just numbers in Excel, we can easily configure SEQUENCE to output dates. For example, to output the first 5 days in May 2025, we could use a formula like this:

    =SEQUENCE(5,,"1-May-2025") // returns {45778;45779;45780;45781;45782}

The result will be an array of serial numbers, as shown above. In this array, the number 45778 corresponds to the date 1-May-2025 in [Excel's date system](https://exceljet.net/glossary/excel-date)
. To display these numbers as dates, apply [number formatting](https://exceljet.net/shortcuts#Number-Formatting)
.

### SEQUENCE to list all dates in a month

![Using SEQUENCE to generate a list of all dates in a given month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/list_all_dates_in_a_month_example.png "Using SEQUENCE to generate a list of all dates in a given month")

In the worksheet shown, we want to generate a list of all dates in a given month, where the month is input as a date in cell B5. To use SEQUENCE for this task, we need to calculate two input values based on the date in B5: (1) the number of days in the month and (2) the first day of the month. To get the number of days in the month, we can use the [DAY function](https://exceljet.net/functions/day-function)
 like this:

    =DAY(EOMONTH(B5,0))

In this snippet, we use EOMONTH to get the last day of the _current_ month (note the offset is zero), then we use the DAY function to get the number of days in the month. For example, with a date like 15-May-2025 in B5, EOMONTH returns the date 31-May-2025, and DAY returns 31, which is equal to the number of days in the month. To get the first day of the month, we can use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 like this:

    =EOMONTH(B5,-1)+1 // get first day in month

Here, we use EOMONTH to travel back to the last day of the "previous" month and then add 1 to move forward one day to land on the first day of the "current" month, relative to the date in B5. The final formula in cell D5 looks like this:

    =SEQUENCE(DAY(EOMONTH(B5,0)),,EOMONTH(B5,-1)+1)
    

The inputs provided to SEQUENCE are as follows:

*   _rows_ - DAY(EOMONTH(B5,0)) // days in month
*   _columns_ - omitted, defaults to 1
*   _start_ - EOMONTH(B5,-1)+1 // first of month
*   _step_ - omitted, defaults to 1

With the above configuration, SEQUENCE returns an array of 31 serial numbers that correspond to all dates in May 2025:

    {45778;45779;45780;45781;45782;45783;45784;45785;45786;45787;45788;45789;45790;45791;45792;45793;45794;45795;45796;45797;45798;45799;45800;45801;45802;45803;45804;45805;45806;45807;45808}

> You must apply a [number format](https://exceljet.net/articles/custom-number-formats)
>  for dates to display these serial numbers as dates.

The output is fully dynamic. If the date in B5 is changed to 9-Jun-2025, the formula will list the 30 dates in June 2025. Notice that the actual date given to SEQUENCE doesn't matter because the formula automatically calculates the first day of the month (with EOMONTH, as explained above) for the start value in SEQUENCE. 

### LET version of the formula

We can use the [LET function](https://exceljet.net/functions/let-function)
 to clean up the formula above somewhat like this:

    =LET(
      date,B5,
      first,EOMONTH(date,-1)+1,
      days,DAY(EOMONTH(date,0)),
      SEQUENCE(days,,first)
    )

This is an excellent example of how the LET function creates cleaner code and results in a formula that is easier to read and debug.

> Tip: To see the entire formula above in the formula bar, use the [shortcut](https://exceljet.net/shortcuts)
>  Control + U.

### All dates between two dates

The generic formula to create a list of all dates between two dates looks like this:

    =SEQUENCE(end-start+1,1,start)
    

This can be adapted to generate a list of all dates in a month like this:

    =LET(
      date,B5,
      first,EOMONTH(date,-1)+1,
      last,EOMONTH(date,0),
      SEQUENCE(last-first+1,,first)
    )
    

The results will be the same, but I think the first formula above is slightly easier to understand and configure.

### Current month dates with TODAY function

To generate a list of all dates in the current month (without needing to specify a date in a cell), you can replace the cell reference with the [TODAY function](https://exceljet.net/functions/today-function)
:

    =SEQUENCE(DAY(EOMONTH(TODAY(),0)),,EOMONTH(TODAY(),-1)+1)

This formula automatically lists all dates for the current month and updates continuously. For example, if today is June 15, 2025, the formula will generate all 30 dates in June 2025. Tomorrow, if it's still June, it will show the same list, but if the month changes to July, it will automatically update to show all 31 dates in July 2025.

The formula works exactly the same way as the previous version, but uses TODAY() instead of a cell reference to determine the target month. This approach is useful for things that need to stay up-to-date:

*   Dashboard reports that always show current month data
*   Daily logs or tracking sheets that auto-update
*   Templates that need to work regardless of when they're opened

### Approach for older versions of Excel

In older versions of Excel, we don't have the SEQUENCE function, so we need to take a different approach. There are many options for this kind of problem, but I think the approach shown below works pretty well:

![Alternative formula approach for older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/list_all_dates_in_a_month_legacy_formula.png "Alternative formula approach for older versions of Excel")

There are two different formulas in the worksheet. The first formula in cell D5 gets the first-of-month from the date in cell B5 like this:

    =EOMONTH(B5,-1)+1

The second formula, entered in cell D6 and copied down manually until it returns nothing, looks like this:

    =IFERROR(IF(D5+1>EOMONTH($D$5,0),"",D5+1),"")

Working from the inside out, the core formula increments dates with the [IF function](https://exceljet.net/functions/if-function)
 like this:

    IF(D5+1>EOMONTH($D$5,0),"",D5+1)

The formula first adds 1 to the value in D5, then checks if the resulting date is greater than the last day of the month, calculated with `EOMONTH($D$5,0)`. If so, IF returns an empty string (""), which looks like a blank cell. If not, the result is D5+1, which adds one day to the previous date. As the formula is copied down, it generates all dates in the given month and then begins to output "blank" cells. To handle the #VALUE! error that arises after the first blank cell, the core formula above is wrapped in the [IFERROR function](https://exceljet.net/functions/iferror-function)
:

    =IFERROR(formula,"")

IFERROR catches the value error and returns an empty string ("") when necessary. The result is that you can copy the formula well past the end of the month and not see any errors.

### Useful links

*   [How to use the SEQUENCE function](https://exceljet.net/functions/sequence-function)
     \- overview
*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
     - 3 min video
*   [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)
     - 3 min video
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
     - Video training

Related formulas
----------------

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

[![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")](https://exceljet.net/formulas/sequence-of-workdays)

### [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    
*   [DAY Function](https://exceljet.net/functions/day-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

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