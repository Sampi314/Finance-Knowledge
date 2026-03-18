# Hours that overlap specific time blocks - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks

---

[Skip to main content](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#main-content)

[](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#)

*   [Previous](https://exceljet.net/formulas/happy-birthday-message)
    
*   [Next](https://exceljet.net/formulas/if-monday-roll-back-to-friday)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Hours that overlap specific time blocks
=======================================

by Dave Bruns · Updated 16 Jun 2025

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

[MAX](https://exceljet.net/functions/max-function)

[LET](https://exceljet.net/functions/let-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[INT](https://exceljet.net/functions/int-function)

[MAP](https://exceljet.net/functions/map-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9184/download?token=liRW3Yu4)
 (24.07 KB)

![Excel formula: Hours that overlap specific time blocks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/hours_that_overlap_specific_time_blocks.png "Excel formula: Hours that overlap specific time blocks")

Summary
-------

To calculate the total number of hours that fall into specific time blocks, you can use a formula that calculates the "overlap" between the time blocks and a given start and end time. In the example shown, the formula in F6 looks like this:

    =BlockHours($B6,$C6,F$2,F$3)

This formula is a custom [LAMBDA](https://exceljet.net/functions/lambda-function)
 named "BlockHours". The result in F6 is the number of hours (6:00) that fall into Block 1 (8:00 AM - 5:00 PM) based on a start time of 6:00 AM and an end time of 2:00 PM. The logic for this kind of calculation is quite complex because we need to take into account the possibility of the start and end times crossing midnight. See the article below for a detailed explanation.

> June 11, 2025 - The original version of the formula I published in 2015 (!) was buggy. I looked at the problem again many times since then, but never had the energy to straighten things out. The logic for this kind of formula is annoyingly complex because time overlap calculations are tricky, plus we need to handle cases where the start and end times cross midnight. Finally, in 2025, I decided to roll up my sleeves and crank out a working version. The nice thing about revisiting this formula so late in the game is that Excel now provides the LET and LAMBDA functions. LET allows us to reduce redundancy in the code significantly, and LAMBDA lets us hide the complexity completely inside a custom function. - Dave

> June 15, 2025 - I fixed a bug to handle cases where (1) the block crosses midnight and (2) the start time is before the block end. New worksheet posted. Thanks, Jean-Marie, for pointing this problem out! - Dave

Explanation 
------------

In this example, the goal is to calculate exactly how much of a task, shift, or event falls inside one or more defined blocks of time. The formula accepts a start and end time for the overall task or shift, as well as a start and end time for the block of interest. In the worksheet shown, the Start times are entered in column B, and the End times are in column C. Column E contains the total hours between Start and End times, and formulas in columns F, G, and H calculate the overlap in hours with the 3 custom time blocks shown. The number of time blocks can be adjusted to suit the use case.

### Use cases

Here are some ways a formula like this might be used:

1.  Calculating premium pay for hours logged in non-standard time periods.
2.  Monitoring power or resource usage across peak and off-peak hours.
3.  Tracking hours logged for workers on call 24 hours a day.
4.  Tracking downtime during business-critical periods of the day.

> Note that the Start and End times are actually "[datetimes](https://exceljet.net/glossary/excel-datetime)
> " (date + time). This is an important detail because it makes it easy to determine if the times cross midnight. You are free to adjust the number formatting as you like.

### Table of Contents

*   [Datetimes for Start and End](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#datetimes-for-start-and-end)
    
*   [LET version of the formula](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#let-version)
    
*   [Variable list and definition](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#variable-list)
    
*   [Windows of time](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#windows-of-time)
    
*   [LAMBDA version of the formula](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#lambda-version)
    
*   [Generic formula for intersection](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#generic-formula-for-intersection)
    
*   [How the formula works](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#how-the-formula-works)
    
*   [Converting to decimal hours](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#converting-to-decimal-hours)
    
*   [Multi-day version of the formula](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#multi-day-version)
    

### Datetimes for Start and End

All values in columns C and B are entered as [Excel datetimes](https://exceljet.net/glossary/excel-datetime)
 (date + time). In the formula bar, they look like this:

    5/12/2025  6:00:00 AM // start (B6)
    5/12/2025  2:00:00 PM // end (C6)

![Start and End times are datetimes (dates + times)](https://exceljet.net/sites/default/files/images/formulas/inline/hours_that_overlap_datetime_example.png "Start and End times are datetimes (dates + times)")

You are free to use any date formatting you like to display the datetimes. In the worksheet shown, all dates in the range B6:C17 are formatted with the following [custom number format](https://exceljet.net/articles/custom-number-formats)
:

    dd-mmm-yy h:mm

Using datetimes is an important simplification in the design of this worksheet because it minimizes calculations to determine if the start and end span midnight. As an added benefit, it also means we can calculate the total hours in the shift in column E with a simple formula like this:

    =C6-B6 // total hours between start and end

As long as the start and end are datetimes, and the end > start, this formula will work correctly.

> For details on how Excel stores dates and times, [see this page](https://exceljet.net/glossary/excel-date)
> . For a detailed walkthrough of different ways to calculate the hours between two times, [see this page](https://exceljet.net/formulas/calculate-hours-between-two-times)
> .

### LET version of the formula

Without the LAMBDA wrapper, the LET version of the formula looks like this:

    =LET(
      start,$B6,
      end,$C6,
      blockStart,F$2,
      blockEnd,F$3,
      startDay,INT(start),
      endDay,INT(end),
      shift,(blockEnd<blockStart)*(MOD(start,1)<blockEnd),
      windowStart,startDay-shift+blockStart,
      windowEnd,startDay-shift+blockEnd+(blockEnd<blockStart),
      startDayHours,MAX(0,MIN(end,windowEnd)-MAX(start,windowStart)),
      endDayHours,IF(endDay>startDay,
      MAX(0,MIN(end,endDay+blockEnd+(blockEnd<blockStart))-
      MAX(start,endDay+blockStart)),0),
      startDayHours+endDayHours
    )

> Tip: Use the [keyboard shortcut](https://exceljet.net/shortcuts)
>  Control + U to expand the formula bar to see more than one line at a time in longer formulas like this.

Notice the [mixed references](https://exceljet.net/glossary/mixed-reference)
: $B6 and $C6 are set up to lock the column, and F$2 and F$3 are set up to lock the row. This is done so that the formula can easily be copied from F6 down and across the full range of F6:H17. The screen below shows the formula in action:

![LET version of the formula](https://exceljet.net/sites/default/files/images/formulas/inline/hours_that_overlap_specific_time_blocks_LET_version.png "LET version of the formula")

### Variable list

Here is a list of all the variables used in the above formula:

*   `start` – the full Excel date‑time value at which the task, shift, or event begins (B6)
*   `end` – the full Excel date‑time value at which the task, shift, or event ends (C6)
*   `blockStart` – start time for the block of interest (F2)
*   `blockEnd` – end time for the block of interest (F3)
*   `startDay` – the calendar day (date) of `start`
*   `endDay` – the calendar day (date) of `end`
*   `shift` - 1-day shift if block crosses midnight and the start time < blockEnd
*   `windowStart` – the `blockStart` converted to a window start datetime
*   `windowEnd` – the `blockEnd` converted to a window end datetime
*   `startDayHours` – hours that overlap the block on the `start` day
*   `endDayHours` – hours that overlap the block on the `end` day

Note: the final result is hours as native [Excel time](https://exceljet.net/glossary/excel-time)
. Multiply by 24 to [convert to decimal hours](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#converting-to-decimal-hours)
.

### Windows of time

Naming the many variables used in this formula in a meaningful way is tricky. The most difficult naming decision was `windowStart` and `windowEnd`, which are meant to express a "window in time". We already have the `blockStart` and `blockEnd`, but these are just times, not anchored to any particular date. When we calculate the overlap in hours that span midnight, we need to tie the time values to a date. For example, a time block might start at 10 PM and end at 3 AM. For a time shift that crosses midnight, we need to calculate the 2-hour overlap on the start date and the 3-hour overlap on the end date. To make calculating the overlap in times easier, `windowStart` and `windowEnd` are true datetimes.

### LAMBDA version of the formula

The custom LAMBDA version of the formula uses the four main inputs as function arguments. The formula is named "BlockHours" and looks like this:

    =LAMBDA(start,end,blockStart,blockEnd,
      LET(
        startDay,INT(start),
        endDay,INT(end), 
        shift,(blockEnd<blockStart)*(MOD(start,1)<blockEnd),
        windowStart,startDay-shift+blockStart,
        windowEnd,startDay-shift+blockEnd+(blockEnd<blockStart),
        startDayHours,MAX(0,MIN(end,windowEnd)-MAX(start,windowStart)),
        endDayHours,IF(endDay>startDay,
        MAX(0,MIN(end,endDay+blockEnd+(blockEnd<blockStart))-
        MAX(start,endDay+blockStart)),0),
        startDayHours+endDayHours
      )
    )

Once named and defined with the Name Manager, you can call it like this:

    =BlockHours($B6,$C6,F$2,F$3)

![LAMBDA version of the formula](https://exceljet.net/sites/default/files/images/formulas/inline/hours_that_overlap_specific_time_blocks_LAMBDA_version.png "LAMBDA version of the formula")

> Converting a formula to a named lambda involves wrapping the formula in the LAMBDA function and refactoring the formula to move the variable inputs into the LAMBDA as arguments. Then you define and name the formula with the [Name Manager](https://exceljet.net/glossary/name-manager)
> . For details, see our [LAMBDA function page](https://exceljet.net/functions/lambda-function)
> .

### Generic formula for intersection

In the section below, we explain how the formula works, step by step. One of the things you'll notice in the code below is a pattern that repeats to calculate the overlap of two time intervals:

    MAX(0,MIN(end,windowEnd) - MAX(start, windowStart))

This is a pattern you'll see in more advanced Excel formulas and in other languages. It's a clever way to measure the intersection of two one-dimensional intervals using MAX and MIN, which avoids more complicated nested IF statements. In plain English, it says:

1.  Take the _latter_ of the two start points.
2.  Take the _earlier_ of the two end points.
3.  Subtract them to get the possible overlap.
4.  If the result is negative (no overlap), force to zero (0).

### How the formula works

The LET version of this formula handles time overlap calculations by breaking the problem into manageable pieces using named variables. Here's how it works:

**Step 0: Get the inputs**

To start off, the formula picks up four values directly from the worksheet:

      start,$B6,
      end,$C6,
      blockStart,F$2,
      blockEnd,F$3,

The `start` comes from cell B6, which contains the start time entered as a datetime. The `end` comes from cell C6, which contains the end time entered as a datetime. The `blockStart` variable is defined using the block start time in F2. The `blockEnd` variable is defined using the block start time in F3. 

> Note, in the LAMBDA version of the formula, these four values are supplied directly as function arguments. 

**Step 1: Extract the dates**

    startDay,INT(start),
    endDay,INT(end),
    

These variables extract just the date portion from the start and end datetimes. This is important for handling shifts that cross midnight.

_Note: The_ [_INT function_](https://exceljet.net/functions/int-function)
 _is used to_ [_separate the date from the time_](https://exceljet.net/formulas/remove-time-from-timestamp)
_._

**Step 2: Create time windows**

      shift,(blockEnd<blockStart)*(MOD(start,1)<blockEnd),
      windowStart,startDay-shift+blockStart,
      windowEnd,startDay-shift+blockEnd+(blockEnd<blockStart),
    

The formula converts the block times (like "8:00 AM" and "5:00 PM") into full datetimes by adding them to the start date. It also creates a `shift` variable that handles cases where (1) the block crosses midnight and (2) the start time is before the block end. If both conditions are TRUE, `shift` = 1, otherwise `shift` = 0. For overnight blocks where `blockEnd<blockStart` (like 11 PM to 6 AM), it adds 1 to push the end time into the next day. 

> A good example of why this problem is challenging - the edge cases are tricky!

**Step 3: Calculate overlap on the start day**

    startDayHours,MAX(0,MIN(end,windowEnd)-MAX(start,windowStart)),
    

This finds the overlap between the shift and the time block on the starting day. Note, we are working with the windows and not the block times, since the windows are anchored to dates. We use the intersection code [explained above](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#generic-formula-for-intersection)
 (MAX/MIN logic) to determine the actual overlap period, then subtract to get hours. The MAX(0,...) ensures that negative results are forced to zero (0).

**Step 4: Calculate overlap on the end day (if different)**

    endDayHours,IF(endDay>startDay,
        MAX(0,MIN(end,endDay+blockEnd+(blockEnd<blockStart))-
        MAX(start,endDay+blockStart)),0),
    

For shifts spanning midnight, this code calculates overlapping hours on the end day. Again, we use the [generic intersection](https://exceljet.net/formulas/hours-that-overlap-specific-time-blocks#generic-formula-for-intersection)
 formula explained above. The logic is similar to Step 3. Note that overlap is only calculated if `endDay > startDay`. Otherwise, IF returns zero (0).

**Step 5: Sum the results**

    startDayHours+endDayHours
    

The final result adds the overlap hours from both days. The logic is somewhat complex, but this is because the formula is designed to handle complex scenarios like overnight shifts and overnight time blocks by treating each day separately, then combining the results.

### Converting to decimal hours

The formulas above use Excel's native time units, in which time is expressed as [fractional values of one day](https://exceljet.net/glossary/excel-time)
. However, you can easily convert the formulas to output decimal hours if needed. One option is to multiply the final result by 24 in the formula itself:

    (startDayHours+endDayHours)*24 // convert to decimal hours

Another option with the LAMBDA version of the formula is to perform the same operation outside the formula:

    =BlockHours($B6,$C6,F$2,F$3)*24 // convert to decimal hours

With either option, you will need to adjust the number formatting to display decimal hours as you like.

### Multi-day version of the formula

One question that comes up when you're working on a formula like this is how to handle time shifts that span multiple days. One option is to use the [SEQUENCE](https://exceljet.net/functions/sequence-function)
 and [MAP](https://exceljet.net/functions/map-function)
 functions to call the custom LAMBDA once per day, like this:

    =LET(
      start,$B6,
      end,$C6,
      blockStart,F$2,
      blockEnd,F$3,
      days,SEQUENCE(INT(end)-INT(start)+1,1,INT(start)),
      SUM(
        MAP(days,
        LAMBDA(day,
        BlockHours(MAX(start,day),MIN(end,day+1),blockStart,blockEnd))
        )
      )
    )

Notice we are calling BlockHours inside the MAP function, which is looping over the `days` array created by SEQUENCE. The basic operation of this formula works in three steps as follows. First, SEQUENCE creates a date range as an array of calendar dates using the `start` and `end` datetimes like this:

    SEQUENCE(INT(end)-INT(start)+1,1,INT(start))

Next, the MAP function applies the custom BlockHours function to each day.

    MAP(days,
      LAMBDA(day,
      BlockHours(MAX(start,day),MIN(end,day+1),blockStart,blockEnd))

Note that for each day in the sequence, it calls BlockHours with a start time of `MAX(start,day)`. This is because we want to use the _actual start time_ on the first day, and _midnight_ (day) on subsequent days. In a similar way, we use an end time of `MIN(end,day+1)` so that BlockHours will use _midnight of the next day on intermediate days_, and the _actual end time on the final day_. You can see the result in the worksheet below, where the start and end times have been adjusted to define larger time spans:

![Multi-day version of the formula with MAP and SEQUENCE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/hours_that_overlap_specific_time_blocks_multiday_version.png "Multi-day version of the formula with MAP and SEQUENCE")

I think this is a cool example of how the new [dynamic array functions in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 can be used to extend the functionality of an existing formula in surprising and powerful ways. I haven't tested this thoroughly yet, but I think it works. Please let me know if you find otherwise! The multi-day formula is on the third sheet in the workbook.

Related formulas
----------------

[![Excel formula: Calculate hours between two times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate_hours_between_two_times.png "Excel formula: Calculate hours between two times")](https://exceljet.net/formulas/calculate-hours-between-two-times)

### [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)

In this example, the goal is to calculate the difference between two times in Excel in hours and minutes. This basic problem comes up frequently when tracking time and may be described in various ways: Calculate elapsed working time in hours. Calculate the duration of an activity in hours...

[![Excel formula: Timesheet overtime calculation formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20overtime%20calculation.png "Excel formula: Timesheet overtime calculation formula")](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

### [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)

Note: it's important to understand that Excel deals with time as fractions of a day . So, 12:00 PM is .5, 6:00 AM is .25, 6 PM is .75, and so on. This works fine for standard time and date calculations, but in many cases you'll want to convert times to decimal hours to make other calculations more...

[![Excel formula: Basic timesheet formula with breaks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20timesheet%20formula%20with%20breaks.png "Excel formula: Basic timesheet formula with breaks")](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)

### [Basic timesheet formula with breaks](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)

At the core, this formula subtracts start time from end time to get duration in hours. This is done to calculate both work time and break time. MOD(C6-B6,1) // get work time MOD(E6-D6,1) // get break time Next, break time is subtracted from work time to get "net" work hours. This formula uses the...

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel MAP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20map%20function.png "Excel MAP function")](https://exceljet.net/functions/map-function)

### [MAP Function](https://exceljet.net/functions/map-function)

The Excel MAP function "maps" a custom LAMBDA function to each value in a supplied [array](https://exceljet.net/glossary/array)
. The LAMBDA is applied to each value, and the result from MAP is an array of results with the same dimensions as the original array.

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

*   [Calculate hours between two times](https://exceljet.net/formulas/calculate-hours-between-two-times)
    
*   [Timesheet overtime calculation formula](https://exceljet.net/formulas/timesheet-overtime-calculation-formula)
    
*   [Basic timesheet formula with breaks](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)
    

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [MAP Function](https://exceljet.net/functions/map-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

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