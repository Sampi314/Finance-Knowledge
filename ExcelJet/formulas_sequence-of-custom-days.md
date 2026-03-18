# Sequence of custom days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sequence-of-custom-days

---

[Skip to main content](https://exceljet.net/formulas/sequence-of-custom-days#main-content)

[](https://exceljet.net/formulas/sequence-of-custom-days#)

*   [Previous](https://exceljet.net/formulas/semimonthly-pay-schedule)
    
*   [Next](https://exceljet.net/formulas/sequence-of-days)
    

[Date series](https://exceljet.net/formulas#Date-series)

Sequence of custom days
=======================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7999/download?token=G3oblghL)
 (18.83 KB)

![Excel formula: Sequence of custom days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sequence_of_custom_days.png "Excel formula: Sequence of custom days")

Summary
-------

To generate a dynamic list of dates that include only certain days of the week (i.e. only Mondays, Wednesdays, and Fridays) you can use the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
 with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. In the example shown, the date in B5 is a hardcoded start date. The formula in B6 is:

    =WORKDAY.INTL(B5-1,SEQUENCE(B8),"0101011")
    

The formula returns the next 12 Mondays, Wednesdays, and Fridays after the start date in B5. The number 12 comes from cell B8 and the start date comes from B5.  If either value is changed, all dates will recalculate.

Generic formula
---------------

    =WORKDAY.INTL(A1-1,SEQUENCE(n),"0101011")

Explanation 
------------

The goal is to generate a series of "custom" days of the week based on a start date entered in cell B5. For example, you might want to list sequential dates for any of the following combinations of days:

*   Mondays, Wednesdays, and Fridays (as shown)
*   Tuesdays, Thursdays, and Saturdays
*   Tuesdays and Thursdays
*   Mondays and Fridays

The number of dates to create (n) is entered in cell B8. If the start date or the number of dates to create is changed, the dates should be recalculated. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the WORKDAY.INTL function. In older versions of Excel, you can also use the WORKDAY.INTL function and a more manual approach, as explained below.

### WORKDAY.INTL function

The [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
 function takes a start date and returns the next workday based on a given offset value provided as the _days_ argument. WORKDAY.INTL will automatically exclude Saturday and Sunday, and can optionally exclude dates that are holidays. The generic syntax for WORKDAY.INTL looks like this:

    =WORKDAY.INTL(start_date,days,[weekend],[holidays])

*   _start\_date_ - the date to start from
*   _days_ - the number of days to move forward or back
*   _weekend_ - a code to specify which days are weekends
*   _holidays_ - a list of dates that are non-working days

One of WORKDAY.INTL's tricks is that it can be configured to treat any day of the week as a workday by providing the _weekend_ argument as a 7-digit code that covers all seven days of the week, Monday through Saturday. In this scheme, a 1 indicates a weekend (non-working) day, and a 0 indicates a workday. The table below shows sample codes in column B and the workdays they define in column J:

![Weekend code options for WORKDAY.INTL](https://exceljet.net/sites/default/files/images/functions/inline/workday.intl_function_weekend_options.png "Weekend code options for WORKDAY.INTL")

This method is more flexible since it can define _any day of the week_ as a weekend or workday. For example, to get the next workday that is a Monday, Wednesday, or Friday after a date in cell A1, you can use a formula like this:

    =WORKDAY.INTL(A1,1,"0101011") // Mon, Wed, Fri

To get the next Tuesday or Thursday, you can use a formula like this:

    =WORKDAY.INTL(A1,1,"1010111") // Tue, Thu

You can also use this feature to create a list of [weekends only](https://exceljet.net/formulas/sequence-of-weekends)
.

_Note: weekend must be entered as a text string surrounded by double quotes ("") when using this feature._

Current Excel version
---------------------

In the current version of Excel (Excel 2019+), the easiest way to solve this problem is to use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 inside the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
. In the workbook shown above, the formula in cell D5 is:

    =WORKDAY.INTL(B5-1,SEQUENCE(B8),"0101011")

The inputs provided to WORKDAY.INTL are as follows:

*   _start\_date_ - B5-1 (the day before the start date)
*   _days_ - array created by SEQUENCE (see below)
*   _weekend_ - "0101011" (code allowing Mon, Wed, and Fri only)
*   _holidays_ - omitted (could be supplied as a range of dates)

Working from the inside out, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is used to generate a sequential array of n numbers, where n comes from cell B8. With the number 12 in cell B8, SEQUENCE generates an array like this:

    =SEQUENCE(B8)
    =SEQUENCE(12)
    ={1;2;3;4;5;6;7;8;9;10;11;12}

Next, the _start\_date_ is calculated by subtracting 1 from the date in B5. We do this because we want to force WORKDAY.INTL to check the start date as well. If it is a Monday, Wednesday, or Friday, it should be included in the list:

    =B5-1
    =45170-1
    =45169 // 31-Aug-2023

[Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
, so the result is 45169, a number that represents 31-Aug-2023, the day before the start date in B5. Simplifying, we have:

    =WORKDAY.INTL(45169,{1;2;3;4;5;6;7;8;9;10;11;12},"0101011")

Because _days_ is given as an array with 12 numbers, WORKDAY.INTL returns 12 dates filtered by the code "0101011", which treats only Mondays, Wednesdays, or Fridays as workdays. With this configuration, WORKDAY.INTL, returns the next 12 Saturdays and Sundays after 31-Aug-2023, skipping all Saturdays, Sundays, Tuesdays, and Thursdays. For more details on WORKDAY.INTL, see [How to use the WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
.

### Tuesdays and Thursdays

To create a list of Tuesdays and Thursdays, just update the weekend code like so:

    =WORKDAY.INTL(B5-1,SEQUENCE(B8),"1010111") // Tue and Thu

### List custom days between dates

To adapt this formula to list all Mondays, Wednesdays, and Fridays _between_ two given dates (_start_ and _end_), you can use the same basic idea in a formula like this:

    =LET(dates,SEQUENCE(end-start+1,1,start),FILTER(dates,WORKDAY.INTL(dates-1,1,"0101011")=dates))

[See this page](https://exceljet.net/formulas/list-workdays-between-dates)
 for a detailed explanation of how this approach works.

Legacy Excel
------------

In older versions of Excel, there is no SEQUENCE function, so we don't have a simple way to request 12 dates at once. One simple solution is to set up the worksheet so that we can "drag copy" a formula that will return the next Saturday or Sunday after the "cell above". First, enter this formula in cell D5:

    =WORKDAY.INTL(B5-1,1,"0101011")

*   _start\_date_ - B5-1 (day before the start date)
*   _days_ - 1 (i.e. next date)
*   _weekend_ - "1111100" (code allowing Mon, Wed, and Fri only)

To get the _start\_date_, we subtract 1 day from the date in B5 to force WORKDAY.INTL to evaluate the start date in B5, like other dates. If the date in cell B5 is a Saturday or Sunday, it will be returned by the formula above. Otherwise, the next Saturday or Sunday will be returned. As explained above, the weekend argument is given as the code "1111100", which tells WORKDAY.INTL to treat only Mondays, Wednesdays, and Fridays as workdays. Next, in cell D6, enter the formula below and copy the formula down as needed:

    =WORKDAY.INTL(D5,1,"0101011")

![Sequence of custom days - solution for older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sequence_of_custom_days_legacy.png "Sequence of custom days - solution for older versions of Excel")

As the formula is copied down, it begins with the date in the "cell above" and returns the next Monday, Wednesday, or Friday. Because the formula in cell D6 refers to the start date in cell B5, cell B5 still drives all results. The downside of this approach is that the formula in D5 is different from the formulas in cell D6 and below, so you must take care to keep them separate.

Conclusion
----------

The WORKDAY.INTL function will calculate the next working day and can be customized with the "weekend" argument to treat _any day of the week_ as a weekend or workday. The SEQUENCE function can be used within WORKDAY.INTL to create a dynamic list of custom days based on a start date and the number of dates you want. You can also combine WORKDAY.INTL with SEQUENCE and the [FILTER function](https://exceljet.net/functions/filter-function)
 to list custom days _between two given dates_. In older versions of Excel without SEQUENCE, you can use a more manual approach to get the same results.

Related formulas
----------------

[![Excel formula: Sequence of weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_weekends.png "Excel formula: Sequence of weekends")](https://exceljet.net/formulas/sequence-of-weekends)

### [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)

The goal is to generate a series of sequential weekend days (Saturday and Sunday) with a formula. The start date is entered in cell B5. The number of dates to create (n) is entered in cell B8. If either of these two values are changed, a new list of weekend dates should be generated. In the current...

[![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")](https://exceljet.net/formulas/sequence-of-workdays)

### [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

Related functions
-----------------

[![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")](https://exceljet.net/functions/workday.intl-function)

### [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be...

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/SEQUENCE%20of%20dates-Play.png)](https://exceljet.net/videos/sequence-of-dates)

### [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)

In this video, we'll look at how to generate a sequence of dates with the SEQUENCE function . The SEQUENCE function can be used to generate numeric sequences of all kinds. Since Excel dates are just numbers, SEQUENCE works well for generating dates. In this first worksheet, we have a couple cells...

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

*   [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)
    
*   [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    

### Functions

*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

### Videos

*   [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)
    
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