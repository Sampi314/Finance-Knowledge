# Biweekly pay schedule - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/biweekly-pay-schedule

---

[Skip to main content](https://exceljet.net/formulas/biweekly-pay-schedule#main-content)

[](https://exceljet.net/formulas/biweekly-pay-schedule#)

*   [Previous](https://exceljet.net/formulas/year-is-a-leap-year)
    
*   [Next](https://exceljet.net/formulas/list-all-dates-in-a-month)
    

[Date series](https://exceljet.net/formulas#Date-series)

Biweekly pay schedule
=====================

by Dave Bruns · Updated 14 Sep 2023

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[WORKDAY](https://exceljet.net/functions/workday-function)

![Excel formula: Biweekly pay schedule](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/biweekly_pay_schedule.png "Excel formula: Biweekly pay schedule")

Summary
-------

To create a list of pay dates that occur biweekly (every two weeks) on a given day of the week, you can use a formula based on the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. In the example shown, the formula in cell D5 is:

    =SEQUENCE(B8,1,B5,14)

Where the date in cell B5 is a valid pay date to start from. With 26 in cell B8, the result is a list of 26 pay dates beginning on Friday, January 6, 2023. See below for an explanation and for an alternative formula that takes into account holidays.

_Note: To list semimonthly pay dates that occur twice monthly, usually on fixed dates like the 1st and 15th, [see this example](https://exceljet.net/formulas/semimonthly-pay-schedule)
._

Generic formula
---------------

    =SEQUENCE(n,1,start,14)

Explanation 
------------

In this example, the goal is to create a list of pay dates that follow a biweekly schedule. A biweekly pay schedule means employees are paid every two weeks on a given day of the week. Each pay period is 14 days, and there are usually 26 pay dates per year, though occasionally 27 depending on the calendar. In the worksheet shown above, pay dates are every other Friday, beginning on the first Friday of the year. We can solve this problem with the SEQUENCE function, as explained below.

### Background study

If you are unfamiliar with the SEQUENCE function, or dynamic array formulas in general, these links will help you get up to speed quickly:

*   [How to use the SEQUENCE function](https://exceljet.net/functions/sequence-function)
     \- overview
*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
     - 3 min video
*   [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)
     - 3 min video
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
     - video training

### SEQUENCE function

The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is used to generate numeric sequences with the following syntax:

    =SEQUENCE(rows,[columns],[start],[step])

*   _rows_ - the number of rows to return
*   _columns_ - the number of columns to return
*   _start_ - the starting value
*   _step_ - the increment to use between values

In this example, the goal is to generate a sequence of 26 pay dates, each 14 days apart. To generate the dates, the formula in cell D5 is:

    =SEQUENCE(B8,1,B5,14)

Inside SEQUENCE, we provide the following values:

*   _rows_ - B8 (26)
*   _columns_ - 1
*   _start_ - B5 (January 6, 2023 = 44932)
*   _step_ - 14 (days between dates)

We can use SEQUENCE to generate dates in Excel because [Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
. The serial number for January 1, 2023, is 44927, so the serial number for January 6, 2023, is 44932. The formula is evaluated by Excel's formula engine like this:

    =SEQUENCE(B8,1,B5,14)
    =SEQUENCE(26,1,44932,14)

Essentially, we are asking SEQUENCE for 26 numbers that start on 44927 and are incremented by 14. With the above configuration, SEQUENCE returns an [array](https://exceljet.net/glossary/array)
 that contains 26 dates in serial number format:

    {44932;44946;44960;44974;44988;45002;45016;45030;45044;45058;45072;45086;45100;45114;45128;45142;45156;45170;45184;45198;45212;45226;45240;45254;45268;45282}

These values spill into the range D5:D30. When properly formatted, they display as dates. In this particular example, we are using the [custom number format](https://exceljet.net/articles/custom-number-formats)
 below:

    ddd d-mmm-yyyy

This causes Excel to display an abbreviated day name (i.e. "Fri") before the date to make it easy to verify correct results.

### Holidays

The formula above does not take into account pay dates that land on holidays, which are typically moved to the previous business day. One way to do this is to add in the [WORKDAY function](https://exceljet.net/functions/workday-function)
, which can calculate the next or previous workday from a given start date, taking into account weekends and holidays. The generic formula looks like this:

    =WORKDAY(SEQUENCE(n,1,start,14)+1,-1,holidays)

Where _n_ is the number of dates to generate, and _holidays_ is a range or array that contains dates that are holidays. The worksheet below shows how this formula can be adapted to the worksheet discussed above:

![Formula for biweekly pay schedule excluding holidays](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/biweekly_pay_schedule_with_holidays.png "Formula for biweekly pay schedule excluding holidays")

Here, we basically feed the results from SEQUENCE directly into the WORKDAY function, with the range B11:B12 given for the _holidays_ argument. We have to use a bit of trickery here to get WORKDAY to check the date returned by SEQUENCE. We do this by asking WORKDAY for the workday _previous_ to the date + 1. In other words, we add 1 to the date, then ask WORKDAY for the previous workday by providing -1 for days. This causes WORKDAY to check the original date from SEQUENCE, and step back to the previous workday if the pay date is in fact a holiday. With the (arbitrary) dates of Feb 17, 2023, and April 28, 2023, provided as holidays in the range B11:B12, notice how the formula rolls back to Thursday in cells D8 and D13.

Related formulas
----------------

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

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

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

*   [Semimonthly pay schedule](https://exceljet.net/formulas/semimonthly-pay-schedule)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    
*   [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)
    
*   [Get first day of month](https://exceljet.net/formulas/get-first-day-of-month)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    

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