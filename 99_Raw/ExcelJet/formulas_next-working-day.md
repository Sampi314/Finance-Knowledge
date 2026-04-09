# Next working day - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/next-working-day

---

[Skip to main content](https://exceljet.net/formulas/next-working-day#main-content)

[](https://exceljet.net/formulas/next-working-day#)

*   [Previous](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    
*   [Next](https://exceljet.net/formulas/pad-week-numbers-with-zeros)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Next working day
================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[WORKDAY](https://exceljet.net/functions/workday-function)

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

![Excel formula: Next working day](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/next_working_day.png "Excel formula: Next working day")

Summary
-------

To get the next working day, or next business day, you can use the [WORKDAY function](https://exceljet.net/functions/workday-function)
 or the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
. In the example shown, the formula in D5 is:

    =WORKDAY(B5,1,holidays)

Where _holidays_ is the [named range](https://exceljet.net/glossary/named-range)
 F5:F15. As the formula is copied down, it begins with the date in column B and returns the next working day _after_ that date.

Generic formula
---------------

    =WORKDAY(date,1,holidays)

Explanation 
------------

In the worksheet shown, column B contains 12 dates. The goal is to calculate the _next working day_ after each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. In other words, the formula should automatically skip weekends and any dates defined as non-working days.

### WORKDAY function

The [WORKDAY function](https://exceljet.net/functions/workday-function)
 takes a date and returns the next working day n days in the future or past. You can use WORKDAY to calculate things like ship dates, delivery dates, and completion dates that need to take into account working and non-working days. The generic syntax for WORKDAY looks like this:

    =WORKDAY(start_date,days,[holidays])

Where _days_ is a number (n) and holidays is an optional range that contains non-working dates. For this problem, we want the next working day, so we provide 1 for _days_. The formula in D5, copied down, looks like this:

    =WORKDAY(B5,1,holidays)

Where _holidays_ is the [named range](https://exceljet.net/glossary/named-range)
 F5:F15, which contains days that should be excluded. The WORKDAY function is fully automatic. Given a valid date, it will add days to the date, skipping weekends and holidays. Named ranges behave like [absolute references](https://exceljet.net/glossary/absolute-reference)
 by default, so the range will not change as the formula is copied down. Without a named range, you will need to lock the reference like this:

    =WORKDAY(B5,1,$F$5:$F$15)

As the formula is copied down, it returns the next business day after the starting date in column B. Saturdays and Sundays are automatically skipped, as well as any dates that appear in the range F5:F15.

### Current date or next workday

There may be situations where you want to return the _current date_ when it's a working day or the _next working date_ if not. To do this, you can adjust the formula like so:

    =WORKDAY(B5-1,1,holidays)

![Formula for current date or the next working day](https://exceljet.net/sites/default/files/images/formulas/inline/current_date_or_next_working_day.png "Formula for current date or the next working day")

Here, we first subtract 1 day from the date inside the WORKDAY function, then feed that date to WORKDAY as the _start\_date_. WORKDAY then moves forward one day to the original date and checks the result. If the original date is a working day, WORKDAY returns the date unchanged. Otherwise, WORKDAY will continue to move forward one day at a time, skipping weekends and holidays along the way, until it finds a valid workday. You can see the result in the worksheet above.

### Custom weekends

The WORKDAY function defines a weekend as Saturday and Sunday only. If you need more flexibility on which days of the week are considered weekends or working days, use the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
 instead. For example, to calculate the next working day for this example with a standard work week of Monday-Thursday, where weekend days are Friday, Saturday, and Sunday, you can use WORKDAY.INTL like this:

    =WORKDAY.INTL(B5,1,"0000111",holidays)

WORKDAY.INTL includes an extra argument called weekend that can be provided as a string of 1s and 0s like "0000111". In this scheme, a 1 indicates a weekend and a 0 indicates a workday. For more details, see How to use the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
.

Related formulas
----------------

[![Excel formula: Previous working day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/previous_working_day.png "Excel formula: Previous working day")](https://exceljet.net/formulas/previous-working-day)

### [Previous working day](https://exceljet.net/formulas/previous-working-day)

In the worksheet shown, column B contains 12 dates. The goal is to calculate the previous working day before each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. The formula should automatically skip weekends and any dates considered non-working days...

[![Excel formula: Date is workday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_workday.png "Excel formula: Date is workday")](https://exceljet.net/formulas/date-is-workday)

### [Date is workday](https://exceljet.net/formulas/date-is-workday)

In this example, the goal is to test a date to determine whether it is a workday. In Excel, you can use either the WORKDAY function or its more flexible sibling WORKDAY.INTL to accomplish this task. WORKDAY function The WORKDAY function calculates a date in the future or past that is, by definition...

[![Excel formula: Next business day 6 months in future](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next%20business%20day%206%20months%20in%20future.png "Excel formula: Next business day 6 months in future")](https://exceljet.net/formulas/next-business-day-6-months-in-future)

### [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)

Working from the inside out, EDATE first calculates a date 6 months in the future. In the example shown, that date is December 24, 2015. Next, the formula subtracts 1 day to get December 23, 2015, and the result goes into the WORKDAY function as the start date, with days = 1, and the range B9:B11...

Related functions
-----------------

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

[![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")](https://exceljet.net/functions/workday.intl-function)

### [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be...

Related videos
--------------

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

*   [Previous working day](https://exceljet.net/formulas/previous-working-day)
    
*   [Date is workday](https://exceljet.net/formulas/date-is-workday)
    
*   [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    

### Functions

*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    
*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    

### Videos

*   [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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