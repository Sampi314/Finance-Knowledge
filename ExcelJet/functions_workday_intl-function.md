# Excel WORKDAY.INTL function | Exceljet

**Source:** https://exceljet.net/functions/workday.intl-function

---

[Skip to main content](https://exceljet.net/functions/workday.intl-function#main-content)

[](https://exceljet.net/functions/workday.intl-function#)

*   [Previous](https://exceljet.net/functions/workday-function)
    
*   [Next](https://exceljet.net/functions/year-function)
    

Excel 2010

[Date and time](https://exceljet.net/functions#Date-and-time)

WORKDAY.INTL Function
=====================

by Dave Bruns · Updated 7 Jun 2024

Related functions 
------------------

[WORKDAY](https://exceljet.net/functions/workday-function)

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")

Summary
-------

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be configured for a custom workweek, where any day of the week can be a workday or non-workday. You can use WORKDAY.INTL function to calculate project start dates, delivery dates, and completion dates that must factor in working and non-working days.

Purpose 
--------

Get a date n working days in the future or past

Return value 
-------------

A serial number representing a date in Excel.

Syntax
------

    =WORKDAY.INTL(start_date,days,[weekend],[holidays])

*   _start\_date_ - The start date.
*   _days_ - Working days before or after start date.
*   _weekend_ - \[optional\] Setting for non-working days.
*   _holidays_ - \[optional\] A list of dates that are non-working days.

Using the WORKDAY.INTL function 
--------------------------------

The WORKDAY.INTL function calculates a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can WORKDAY.INTL to calculate project start dates, delivery dates, and completion dates that must ignore non-working days. The WORKDAY.INTL function is more robust than the simpler WORKDAY function because weekend days can be customized so that _any day of the week_ can be a workday or non-workday. Note that WORKDAY.INTL will _automatically_ exclude Saturdays and Sundays but will only exclude holidays if they are provided.

The WORKDAY.INTL function takes four [arguments](https://exceljet.net/glossary/function-argument)
:

*   _start\_date -_ the date from which to start counting. Note that WORKDAY.INTL _does not_ include the start date as a work day.
*   _days_ - the number of days in the future or past to calculate a workday. Use a positive number for days to calculate dates in the future, and a negative number for past dates.
*   _weekend_ - an optional argument that controls which days of the week are working and non-working days. If _weekend_ is omitted, WORKDAY.INTL will treat Saturdays and Sundays as non-working days by default. The _weekend_ argument can be provided as a numeric code or a text string like "0000011". See below for details.
*   _holidays_ - an optional argument to provide non-working dates that should be skipped when computing a result. _Holidays_ must be provided as a range or array that contains valid Excel dates.

### The WORKDAY.INTL function explained

To illustrate how WORKDAY.INTL works, assume we are scheduling a task that takes 5 working days, starting on Monday, July 1, 2024. The goal is to calculate a date that is 5 working days after July 1, 2024. Beginning with the simplest case, let's just add 5 days to the start date:

    ="1-Jul-2024"+5 // returns "6-Jul-2024"

The result is Saturday, July 6, 2024. While this is a valid result, it doesn't take into account that Saturday is probably not a working day. If, on the other hand, we use WORKDAY.INTL to calculate a date 5 days after July 1:

    =WORKDAY.INTL("1-Jul-2024",5) // returns "8-Jul-2024"

The result is Monday, July 8, 2024. This is because WORKDAY.INTL automatically skips Saturdays and Sundays when it calculates a result. Taking things one step further, what if we need to schedule based on a 4-day workweek, where the workdays are Monday through Thursday? In that case, we can extend the formula with the optional _weekend_ argument like this:

    =WORKDAY.INTL("1-Jul-2024",5,"0000111") // returns "9-Jul-2024"

The result is now Tuesday, July 9. The text string "0000111" means Mondays, Tuesdays, Wednesdays, and Thursdays are workdays, and Fridays, Saturdays, and Sundays are "weekend days" (i.e. non-working days). Finally, let's extend the formula one more time and provide two holidays:

    =WORKDAY.INTL("1-Jul-2024",5,"0000111",{"4-Jul-2024";"2-Sep-2024"}) // returns "10-Jul-2024"

Since one of the holidays (July 4, 2024) overlaps schedule, WORKDAY.INTL now returns Tuesday, Wednesday, July 10, 2024, since Thursday, July 4, 2024 is also skipped in the calculation.

_Note: the holidays above are provided as an [array constant](https://exceljet.net/glossary/array-constant)
 but more typically holidays are provided as a range. Remember that holidays must be valid Excel dates. The name of the holiday is not used at all by_ WORKDAY.INTL.

Of course, in real life, you will not hardcode dates into formulas like this. You will instead use cell references. The screen below shows the four formulas above "ported" to a workbook with cell references. Notice the final calculated date moves farther into the future as we restrict the schedule:

![The WORKDAY.INTL function explained with a simple example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_workday.intl_function_explained.png "The WORKDAY.INTL function explained with a simple example")

The formula in D5 does not use WORKDAY.INTL and simply [adds 5 days](https://exceljet.net/formulas/add-days-to-date)
 to the start date:

    =B5+C5 // returns "6-Jul-2024"
    

The formula in D6 uses the WORKDAY.INTL function but does not provide any holidays:

    =WORKDAY.INTL(B6,C6)// returns "8-Jul-2024"
    

The formula in D7 implements a 4-day workweek by providing "0000111" for the _weekend_ argument:

    =WORKDAY.INTL(B7,C7,"0000111") // returns "9-Jul-2024"

Finally, the formula in D8 sets the same 4-day workweek and provides a small list of holidays in B13:B14:

    =WORKDAY.INTL(B7,C7,"0000111",B13:B14) // returns "10-Jul-2024"
    

In all cases, the _start\_date_ in column B and the _days_ in column D are the same.

### The weekend argument

What makes WORKDAY.INTL different from the original WORKDAY function is the _weekend_ argument. Whereas the WORKDAY function is hardcoded to treat Saturday and Sunday as weekend (i.e. non-working) days the _weekend_ argument in WORKDAY.INTL can be configured to specify any day of the week as a working or non-working day.

> The name "weekend" is somewhat confusing since it suggests "end of the week" been when non-working days may occur anywhere in a week, so I recommend you think of the _weekend_ argument in WORKDAY.INTL to mean "non-working days". This is a more accurate reflection of its purpose.

There are two ways to configure the weekend argument:

1.  Use a numeric code to select from a pre-configured list of working and non-working days
2.  Provide a 7-digit code string that provides a setting for every day of the week.

Let's look at both approaches.

### Numeric code for weekend

The first way to provide a value for weekend is to provide a numeric code from the [table below](https://exceljet.net/functions/workday.intl-function#weekend_codes)
, which contains 14 preconfigured options. For example, the generic formulas below show how WORKDAY.INTL can be configured to find the "next" working day with three different workweeks:

1.  A standard 5-day workweek with Saturday and Sunday as weekend days (1, the default)
2.  A 5-day workweek with Sunday and Monday as weekend days (2)
3.  A 6-day workweek with Sundays only as a weekend (11)

    =WORKDAY.INTL(A1,1,1) // Saturday and Sunday (default)
    =WORKDAY.INTL(A1,1,2) // Sunday and Monday
    =WORKDAY.INTL(A1,1,11) // Sunday only
    

In the last two examples above, we use the numeric code 11 to set weekends to Sundays only. See the [table below](https://exceljet.net/functions/workday.intl-function#weekend_codes)
 for the full list of available codes. Note that unlike the "code string" option explained below, these codes are numeric and should not be entered as text. For simplicity, none of the formulas above provided holidays, but they can be added as the fourth argument.

|     |     |
| --- | --- |
| **Code** | **Weekend days** |
| 1 (default) | Saturday, Sunday |
| 2   | Sunday, Monday |
| 3   | Monday, Tuesday |
| 4   | Tuesday, Wednesday |
| 5   | Wednesday, Thursday |
| 6   | Thursday, Friday |
| 7   | Friday, Saturday |
| 11  | Sunday only |
| 12  | Monday only |
| 13  | Tuesday only |
| 14  | Wednesday only |
| 15  | Thursday only |
| 16  | Friday only |
| 17  | Saturday only |

### Code string for weekends

The second way to provide a value for weekend is to provide 7-digit text string that covers all seven days of the week, Monday through Saturday. This text string can contain only 1s and 0s. In this scheme, a 1 indicates a weekend (non-working) day, and a 0 indicates a workday. The table below shows sample weekend codes in column B and the workdays they define in column J:

![Weekend code options for WORKDAY.INTL](https://exceljet.net/sites/default/files/images/functions/inline/workday.intl_function_weekend_options.png "Weekend code options for WORKDAY.INTL")

_In the image above, shaded cells indicate non-working days and unshaded cells are working days._

The most confusing thing about this method is that you need to "think backwards": you are not marking working days with a 1, you are marking non-working days with a 1. _The zeros are working days_. For example, to specify a 6-day workweek with Sunday only as a nonworking day, you would provide "0000001" (row 8 in the worksheet above):

    =WORKDAY.INTL(A1,1,"0000001")

To get the next workday that is a Monday, Wednesday, or Friday, you can use a formula like this:

    =WORKDAY.INTL(A1,1,"0101011")

To get the next workday that is a Tuesday or Thursday, you can use a formula like this:

    =WORKDAY.INTL(A1,1,"1010111")

You can use this same feature to create a list of [weekends only](https://exceljet.net/formulas/sequence-of-weekends)
, or a list of sequential [Mondays, Wednesdays, and Fridays](https://exceljet.net/formulas/sequence-of-custom-days)
, or any other combination of weekdays, so long as the pattern repeats each week.

_Note: weekend must be entered as a text string surrounded by double quotes (i.e."0000011") when using this feature. Personally, I prefer the this second approach because it can handle any combination of working/non-working days and you don't need to look up an arbitrary numeric code._

### Worksheet Example

In the worksheet below, Column B contains a variety of different start dates, column C contains the number of days to use, and "holidays" is the [named range](https://exceljet.net/glossary/named-range)
 F5:F13:

![WORKDAY.INTL function worksheet example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_workday.intl_function_worksheet_example.png "WORKDAY.INTL function worksheet example")

The formula in cell D5 is:

    =WORKDAY.INTL(B5,C5,11,holidays)

*   _start\_date_ - January 1, 2021 (B5)
*   _days_ - 1, (C5)
*   _weekend_ - 11 (numeric code for Sunday-only weekend)
*   _holidays_ - holidays (the named range F5:F13)

As the formula is copied down, WORKDAY.INTL calculates a date n working days from the start date using the value in column C for _days_. When calculating a result, WORKDAY.INTL excludes dates that are Sundays and dates that are holidays.

_Note: [named ranges](https://exceljet.net/articles/named-ranges)
 automatically behave like absolute references so there is no need to lock the reference to "holidays" before copying the formula. If you prefer not to use a named range, use an absolute reference like $F$5:$F$13 instead._

### Visualized Example

It can be hard to visualize how WORKDAY.INTL works when it calculates a result. The worksheet below contains a more detailed example that shows non-working days shaded in gray in columns D and E:

![WORKDAY.INTL function visualization](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_workday.intl_function_visualization.png "WORKDAY.INTL function visualization")

In the example above, WORKDAY.INTL is used to calculate a date that is 4 working days after 23-Dec-2024. The weekend argument is provided as "0000111, " specifying a 4-day workweek where Fridays, Saturdays, and Sundays are non-working days. The formulas in G5 and G6 show the result with and without the holidays in B11:B13:

    =WORKDAY.INTL(start,days,"0000111")
    =WORKDAY.INTL(start,days,"0000111",holidays)
    

The first formula (G5) excludes weekend days only and returns December 30, 2024. The second formula (G6) excludes weekend days _and_ holidays and returns January 2, 2025. The dates in columns D and E are not required in this solution, they exist only to help visualize how the WORKDAY.INTL function evaluates working and non-working days and arrives at a final result. The shading and highlighting are applied with [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
. For a full explanation with details, [see this page](https://exceljet.net/formulas/add-business-days-to-date)
.

### Example - is this date a workday?

One problem you might run into is how to test a date to determine whether it is a workday. You can use WORKDAY.INTL for this task, but the formula is not immediately obvious. Essentially, we need to "trick" WORKDAY.INTL into evaluating a given date by shifting the date back one day and then asking for the next workday. You can see this approach in the worksheet below. The formula in cell D5 is:

    =WORKDAY.INTL(B5-1,1,"0000111",holidays)=B5

![Testing - is this date a workday?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_workday.intl_function_date_is_workday.png "Testing - is this date a workday?")

For a more detailed explanation, see this example: [Date is Workday](https://exceljet.net/formulas/date-is-workday)
.

### Recommendations

*   Use cell references for the start date, days, and holidays to make it easy to adjust the output quickly.
*   Using the code string format for _weekend_ (e.g. "0000111") is more flexible than a numeric code because you can make any day of the week a workday or non-workday.
*   WORKDAY.INTL returns a date. If you need to calculate the number of working days between two dates, see the [NETWORKDAYS function](https://exceljet.net/functions/networkdays-function)
     or the more flexible [NETWORKDAYS.INTL function](https://exceljet.net/functions/networkdays.intl-function)
    .

### Notes

*   WORKDAY.INTL returns a _date_ that is a given number of working _days_ from a specified _start\_date_
*   WORKDAY.INTL _does not_ include the start date as a work day.
*   Use a positive number for _days_ to calculate dates in the future, and a negative number for past dates.
*   If _any argument is_ invalid, WORKDAY.INTL will return #NUM! or #VALUE!, depending on the input.
*   If days is zero, WORKDAY.INTL will return the _start\_date_ unchanged.
*   The _weekend_ argument can be provided as a numeric code or a text string like "0000011"
*   _Holidays_ must be provided as valid Excel dates in a range or array.

WORKDAY.INTL function examples
------------------------------

[![Excel formula: Get project end date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20project%20end%20date.png "Excel formula: Get project end date")](https://exceljet.net/formulas/get-project-end-date)

### [Get project end date](https://exceljet.net/formulas/get-project-end-date)

This formula uses the WORKDAY function to calculate an end date. WORKDAY can calculate dates in the future or past, and automatically excludes weekends and holidays (if provided). In the example shown, we have the project start date in column C, and days in column D. Days represents the duration of...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

[![Excel formula: Add days exclude certain days of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Add%20days%20exclude%20certain%20days%20of%20week.png "Excel formula: Add days exclude certain days of week")](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)

### [Add days exclude certain days of week](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)

The WORKDAY.INTL function is based on the WORKDAY function , which is designed to add work days to a date. WORKDAY automatically excludes Saturday and Sunday, and optionally can exclude a list of custom holidays. The WORKDAY.INTL does the same thing, but makes it possible to exclude any days of the...

[![Excel formula: Get project start date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20project%20start%20date.png "Excel formula: Get project start date")](https://exceljet.net/formulas/get-project-start-date)

### [Get project start date](https://exceljet.net/formulas/get-project-start-date)

This formula is uses the WORKDAY function, which returns a date in the future or past, based on start date and required work days. WORKDAY automatically excludes weekends, and can also exclude holidays if provided as a range of dates. In the example shown, the project end date is in column C, and...

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Sequence of weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_weekends.png "Excel formula: Sequence of weekends")](https://exceljet.net/formulas/sequence-of-weekends)

### [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)

The goal is to generate a series of sequential weekend days (Saturday and Sunday) with a formula. The start date is entered in cell B5. The number of dates to create (n) is entered in cell B8. If either of these two values are changed, a new list of weekend dates should be generated. In the current...

[![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")](https://exceljet.net/formulas/sequence-of-workdays)

### [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE...

[![Excel formula: Next business day 6 months in future](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20business%20day%206%20months%20in%20future.png "Excel formula: Next business day 6 months in future")](https://exceljet.net/formulas/next-business-day-6-months-in-future)

### [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)

Working from the inside out, EDATE first calculates a date 6 months in the future. In the example shown, that date is December 24, 2015. Next, the formula subtracts 1 day to get December 23, 2015, and the result goes into the WORKDAY function as the start date, with days = 1, and the range B9:B11...

[![Excel formula: Add workdays to date custom workweek](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_workdays_to_date_custom_workweek.png "Excel formula: Add workdays to date custom workweek")](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)

### [Add workdays to date custom workweek](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)

In this example, the goal is to calculate a workday n days in the future based on a 4-day workweek and, optionally, holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Get project midpoint](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20project%20midpoint2.png "Excel formula: Get project midpoint")](https://exceljet.net/formulas/get-project-midpoint)

### [Get project midpoint](https://exceljet.net/formulas/get-project-midpoint)

The WORKDAY function returns a date in the future or past, based on a start date, workdays, and optional holidays. WORKDAY automatically excludes weekends, and counts only Monday through Friday as workdays. In the example shown, WORKDAY is configured to get a project midpoint date by adding half of...

[![Excel formula: Previous working day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/previous_working_day.png "Excel formula: Previous working day")](https://exceljet.net/formulas/previous-working-day)

### [Previous working day](https://exceljet.net/formulas/previous-working-day)

In the worksheet shown, column B contains 12 dates. The goal is to calculate the previous working day before each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. The formula should automatically skip weekends and any dates considered non-working days...

[![Excel formula: Sequence of custom days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_custom_days.png "Excel formula: Sequence of custom days")](https://exceljet.net/formulas/sequence-of-custom-days)

### [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)

The goal is to generate a series of "custom" days of the week based on a start date entered in cell B5. For example, you might want to list sequential dates for any of the following combinations of days: Mondays, Wednesdays, and Fridays (as shown) Tuesdays, Thursdays, and Saturdays Tuesdays and...

[![Excel formula: Next working day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next_working_day.png "Excel formula: Next working day")](https://exceljet.net/formulas/next-working-day)

### [Next working day](https://exceljet.net/formulas/next-working-day)

In the worksheet shown, column B contains 12 dates. The goal is to calculate the next working day after each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. In other words, the formula should automatically skip weekends and any dates defined as non-...

[![Excel formula: Date is workday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_workday.png "Excel formula: Date is workday")](https://exceljet.net/formulas/date-is-workday)

### [Date is workday](https://exceljet.net/formulas/date-is-workday)

In this example, the goal is to test a date to determine whether it is a workday. In Excel, you can use either the WORKDAY function or its more flexible sibling WORKDAY.INTL to accomplish this task. WORKDAY function The WORKDAY function calculates a date in the future or past that is, by definition...

Related functions
-----------------

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

[![Excel NETWORKDAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays%20function.png "Excel NETWORKDAYS function")](https://exceljet.net/functions/networkdays-function)

### [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can _optionally_ exclude a list of holidays supplied as dates. ...

[![Excel NETWORKDAYS.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays.intl%20function.png "Excel NETWORKDAYS.INTL function")](https://exceljet.net/functions/networkdays.intl-function)

### [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)

The Excel NETWORKDAYS.INTL function calculates the number of working days between two dates. NETWORKDAYS.INTL can optionally exclude a list of holidays and provides a way to specify which days of the week are considered weekends.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)
    
*   [Get project midpoint](https://exceljet.net/formulas/get-project-midpoint)
    
*   [Get project end date](https://exceljet.net/formulas/get-project-end-date)
    
*   [Previous working day](https://exceljet.net/formulas/previous-working-day)
    
*   [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)
    
*   [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    
*   [Add days exclude certain days of week](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)
    
*   [Next working day](https://exceljet.net/formulas/next-working-day)
    
*   [Add workdays to date custom workweek](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    

### Functions

*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    
*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)
    

### Articles

*   [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
    

### Links

*   [Microsoft WORKDAY.INTL function documentation](https://support.office.com/en-us/article/workday-intl-function-a378391c-9ba7-4678-8a39-39611a9bf81d)
    

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