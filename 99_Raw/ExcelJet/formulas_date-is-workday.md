# Date is workday - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/date-is-workday

---

[Skip to main content](https://exceljet.net/formulas/date-is-workday#main-content)

[](https://exceljet.net/formulas/date-is-workday#)

*   [Previous](https://exceljet.net/formulas/date-is-same-month-and-year)
    
*   [Next](https://exceljet.net/formulas/days-in-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Date is workday
===============

by Dave Bruns · Updated 31 May 2024

Related functions 
------------------

[WORKDAY](https://exceljet.net/functions/workday-function)

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

![Excel formula: Date is workday](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/date_is_workday.png "Excel formula: Date is workday")

Summary
-------

To test a date to determine whether it is a workday, you can use a formula based on the [WORKDAY function](https://exceljet.net/functions/workday-function)
. In the example shown, the formula in C5 is:

    =WORKDAY(B5-1,1,holidays)=B5

where "holidays" is the [named range](https://exceljet.net/glossary/named-range)
 G5:G7. As the formula is copied down, it returns TRUE for dates that are workdays and FALSE for dates that are non-workdays. In column, B non-workdays are shaded in gray using conditional formatting triggered by a similar formula. See below for details.

Generic formula
---------------

    =WORKDAY(date-1,1,holidays)=date

Explanation 
------------

In this example, the goal is to test a date to determine whether it is a workday. In Excel, you can use either the WORKDAY function or its more flexible sibling WORKDAY.INTL to accomplish this task.

### WORKDAY function

The [WORKDAY function](https://exceljet.net/functions/workday-function)
 calculates a date in the future or past that is, by definition, a workday. WORKDAY automatically excludes weekends (Saturday and Sunday) and can optionally exclude holidays. WORKDAY accepts 3 arguments: _start\_date_, _days_, and (optionally) _holidays_. The generic syntax looks like this:

    =WORKDAY(start_date,days,[holidays])

For example, if we provide WORKDAY with the date May 31, 2024 (a Friday), and ask for a workday 1 day in the future, WORKDAY skips Saturday and Sunday and returns June 3, 2024:

    =WORKDAY("31-May-2024",1) // returns "3-June-2024"

In this example, we are not providing holidays. If we have a list of dates that are holidays we can provide them like this:

    =WORKDAY("31-May-2024",1,holidays) // returns "3-June-2024"

Where "holidays" is a previously defined [named range](https://exceljet.net/articles/named-ranges)
, or a simple range like G5:G7, usually entered as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 like $G$5:$G$7 to prevent changes when the formula is copied.

### Testing for a workday

Since in this problem we want to check a single date and get a TRUE or FALSE result, we would ideally use WORKDAY with _days_ set to zero in a simple formula like this:

    =WORKDAY(date,0,holidays)=B5
    

However, this _doesn't work,_ since WORKDAY will not evaluate a date when _days_ is zero. It always returns the original start date, even if it is a weekend or holiday. The solution is to supply the _start\_date_ as a simple calculation that subtracts 1 like this:

    =WORKDAY(B5-1,1,holidays)=B5
    

This causes WORKDAY to step back one day, then add 1 day to the result, taking into account weekends and holidays. Effectively, we are "tricking" WORKDAY into evaluating the original date as the _start\_date_. When the date falls on a weekend or holiday, WEEKDAY will automatically adjust the date forward to the next working day. If the date is a workday, it will remain unchanged. Then we compare the original start date in cell B5 to the result of the WORKDAY function. If the dates are the same (i.e. the result from WORKDAY is the same as the date in B5) we know we have a workday and the formula returns TRUE. If not, WORKDAY has shifted the date (which means it is a non-working day) and the formula returns FALSE. This is the formula used in cell D5 of the worksheet shown above.

### Shading non-workdays with conditional formatting

In the worksheet shown, we are also shading non-workdays in gray with [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
, triggered by this formula:

    =WORKDAY(B5-1,1,holidays)<>B5

This formula is almost the same, but notice that we are comparing the result from WORKDAY with the original date using the "not equal to" [operator](https://exceljet.net/glossary/logical-operators)
 ("<>") instead of the "equal to" ("=") operator. This reverses the operation of the formula so that it returns TRUE when a date is not a workday and FALSE when a date is a workday. We do this because we want to shade _non-workdays_.

### Ensure a calculated date falls on a workday

If you are returning a date with another formula and want to make sure the date is a workday, you can use a formula like this:

    =WORKDAY(calculated_date-1,1,holidays)
    

The idea is the same as above - we subtract one day from the date, then ask WORKDAY to give us the next working day.

_Note: if you need to evaluate workdays with a custom workweek schedule, where weekends are not Saturday and Sunday, use the more flexible [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
 function._

Related formulas
----------------

[![Excel formula: Next working day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/next_working_day.png "Excel formula: Next working day")](https://exceljet.net/formulas/next-working-day)

### [Next working day](https://exceljet.net/formulas/next-working-day)

In the worksheet shown, column B contains 12 dates. The goal is to calculate the next working day after each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. In other words, the formula should automatically skip weekends and any dates defined as non-...

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

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Next working day](https://exceljet.net/formulas/next-working-day)
    
*   [Next business day 6 months in future](https://exceljet.net/formulas/next-business-day-6-months-in-future)
    

### Functions

*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    
*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    

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