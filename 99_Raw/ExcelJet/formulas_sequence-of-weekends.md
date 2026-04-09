# Sequence of weekends - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sequence-of-weekends

---

[Skip to main content](https://exceljet.net/formulas/sequence-of-weekends#main-content)

[](https://exceljet.net/formulas/sequence-of-weekends#)

*   [Previous](https://exceljet.net/formulas/sequence-of-times)
    
*   [Next](https://exceljet.net/formulas/sequence-of-workdays)
    

[Date series](https://exceljet.net/formulas#Date-series)

Sequence of weekends
====================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

![Excel formula: Sequence of weekends](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sequence_of_weekends.png "Excel formula: Sequence of weekends")

Summary
-------

To create a list of weekend days only (i.e. a list of Saturdays and Sundays), you can use a formula based on the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 inside the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
. In the example shown, the formula in D5 is:

    =WORKDAY.INTL(B5-1,SEQUENCE(B8),"1111100")
    

The result is a series of the next 12 Saturdays and Sundays after September 1, 2023. This list is dynamic. The number 12 comes from cell B8 and the start date comes from B5.  If either value is changed, a new list of weekend dates is generated.

_Notes: (1) In older versions of Excel without the SEQUENCE function, you can use a more manual approach as explained below. (2) If you need a list of weekends between two dates, you can use a variation of [this formula](https://exceljet.net/formulas/list-workdays-between-dates)
, as explained below._

Generic formula
---------------

    =WORKDAY.INTL(start-1,SEQUENCE(n),"1111100")

Explanation 
------------

The goal is to generate a series of sequential weekend days (Saturday and Sunday) with a formula. The start date is entered in cell B5. The number of dates to create (n) is entered in cell B8. If either of these two values are changed, a new list of weekend dates should be generated. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the WORKDAY.INTL function. In older versions of Excel, you can also use the WORKDAY.INTL function with a more manual approach, as explained below.

### WORKDAY.INTL function

The [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
 function takes a date and returns the next workday based on a given offset value provided as the _days_ argument. WORKDAY.INTL will automatically exclude weekends and can optionally exclude dates that are holidays. In this example, we don't need to exclude holidays so we are only using the first 3 arguments in WORKDAY.INTL:

    =WORKDAY.INTL(start_date,days,weekend)

*   _start\_date_ - the date to start from
*   _days_ - the number of days to move forward or back
*   _weekend_ - a code to specify which days are weekends

One of the arguments provided to WORKDAY.INTL is called "weekend", and controls which days are considered non-working days. The _weekend_ argument can be provided as a number linked to a [preconfigured list](https://exceljet.net/functions/workday.intl-function#weekend-codes)
, or as a 7-digit code that covers all seven days of the week, Monday through Saturday. In this code, a 1 indicates a weekend and a 0 indicates a workday. Each digit in the code represents a day of the week. The first digit represents Monday and the last digit represents Sunday. For example, to configure WORKDAY.INTL to get the next working day after a date in cell A1, where Saturday and Sunday are weekends, you can use a formula like this:

    =WORKDAY.INTL(A1,1,"0000011") // weekends = sat, sun

To get the next working day when Friday, Saturday, and Sunday are weekend days, you can use a formula like this:

    =WORKDAY.INTL(A1,1,"0000111") // weekends = fri, sat, sun

The screen below demonstrates how WORKDAY.INTL behaves with different codes. In all cases, the start date comes from column B and the weekend code comes from column C. The result in column F shows the next working day after the start date:

![Workday.intl weekend code configuration example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/workday.intl_weekend_code_configuration.png "Workday.intl weekend code configuration example")

Notice as we add more weekend days (i.e. non-working days) the next working day gets pushed out. We use this behavior to list Saturdays or Sundays only in the formulas explained below.

Current version
---------------

In the current version of Excel (Excel 2019+), the easiest way to solve this problem is to use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 inside the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
. In the workbook shown above, the formula in cell D5 is:

    =WORKDAY.INTL(B5-1,SEQUENCE(B8),"1111100")

The WORKDAY.INTL function takes a date and returns the next workday based on a given offset value. The inputs provided to WORKDAY.INTL are as follows:

*   _start\_date_ - B5-1 (the day before the start date)
*   _days_ - array created by SEQUENCE (see below)
*   _weekend_ - "1111100" (code allowing Saturdays and Sundays only)
*   _holidays_ - omitted (not needed)

Working from the inside out, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is used to generate a sequential array of n numbers, where n comes from cell B8. With the number 12 in cell B8, SEQUENCE generates an array like this:

    =SEQUENCE(B8)
    =SEQUENCE(12)
    ={1;2;3;4;5;6;7;8;9;10;11;12}

The _start\_date_ is calculated by subtracting 1 from the date in B5. We do this because we want to force WORKDAY.INTL to evaluate the start date as well. If it is a Saturday or Sunday, it should be included in the list. [Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
, so this operation evaluates like this:

    =B5-1
    =45170-1
    =45169 // 31-Aug-2023

The number 45169 represents 31-Aug-2023, the day before the start date in B5.  Simplifying, we now have:

    =WORKDAY.INTL(45169,{1;2;3;4;5;6;7;8;9;10;11;12},"1111100")

Since we are providing _days_ as an array containing 1-12, we are asking WORKDAY.INTL for the next 12 work days after 31-Aug-2023 when _weekend_ is given as "1111100". This is a special way of indicating which days of the week should be treated as weekend dates (i.e. non-working days), which are excluded by WORKDAY.INTL. There are 7 characters in the string, one for each day of the week starting on Monday. A "1" means the day is a non-working day (i.e. a "weekend") and should be excluded. A "0" means the day _is a working day_ and should be allowed. With this configuration, WORKDAY.INTL, returns the next 12 Saturdays and Sundays after 31-Aug-2023, skipping the days Monday through Friday. For more details on WORKDAY.INTL, see [How to use the WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
.

### List weekends between dates

To adapt this formula to list the weekends between two dates (_start_ and _end_), you can use a generic formula like this:

    =LET(dates,SEQUENCE(end-start+1,1,start),FILTER(dates,WORKDAY.INTL(dates-1,1,"1111100")=dates))

[See this page](https://exceljet.net/formulas/list-workdays-between-dates)
 for a detailed explanation of how this approach works.

Legacy Excel
------------

In older versions of Excel, there is no SEQUENCE function, so we don't have a simple way to request 12 dates at once. One simple solution is to set up the worksheet so that we can "drag copy" a formula that will return the next Saturday or Sunday after the "cell above". First, enter this formula in cell D5:

    =WORKDAY.INTL(B5-1,1,"1111100")

Here we use the WORKDAY.INTL function to determine the next Saturday or Sunday after the start date with these inputs:

*   _start\_date_ - B5-1 (the day before the start date)
*   _days_ - 1 (i.e. next date)
*   _weekend_ - "1111100" (code allowing Saturdays and Sundays only)

To get the start\_date, we subtract 1 day from the date in B5 to force WORKDAY.INTL to evaluate the start date in B5 like other dates. If the date in cell B5 is a Saturday or Sunday, it will be returned by the formula above. Otherwise, the next Saturday or Sunday will be returned. As explained above, the weekend argument is given as the code "1111100" This tells WORKDAY.INTL to treat the weekdays Monday through Friday as "weekends" and Saturday and Sunday as workdays. The result is that WORKDAY.INTL will only return dates that are a Saturday or Sunday.

Next, in cell D6, enter the formula below and copy the formula down as needed:

    =WORKDAY.INTL(D5,1,"1111100")

![Sequence of weekends  - legacy formula for older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sequence_of_weekends_legacy_formula.png "Sequence of weekends  - legacy formula for older versions of Excel")

The inputs to WORKDAY.INTL are as follows:

*   _start\_date_ - D5 (the "cell above")
*   _days_ - 1 (i.e. next date)
*   _weekend_ - "1111100" (code allowing Saturdays and Sundays only)

As the formula is copied down, it begins with the date in the "cell above" and returns the next Saturday or Sunday. Because the formula in cell D6 refers to the start date in cell B5, cell B5 is still operational and will drive all results. The downside of this approach is that the formula in D5 is different from the formulas in cell D6 and below, so you must take care to keep them separate.

Conclusion
----------

The key to this formula is the WORKDAY.INTL function which can calculate the next working day, and can be customized with the "weekend" argument to treat Saturdays and Sundays as working days. In Excel 2019+, the SEQUENCE function can be used within WORKDAY.INTL to generate a dynamic array of weekend dates based on a start date and the number of weekends you want to list. In addition, you can combine WORKDAY.INTL with SEQUENCE and the [FILTER function](https://exceljet.net/functions/filter-function)
 to list weekends _between_ two given dates. In an older version of Excel without SEQUENCE, you can use a manual "drag copy" approach to get the same results.

Related formulas
----------------

[![Excel formula: Sequence of custom days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_custom_days.png "Excel formula: Sequence of custom days")](https://exceljet.net/formulas/sequence-of-custom-days)

### [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)

The goal is to generate a series of "custom" days of the week based on a start date entered in cell B5. For example, you might want to list sequential dates for any of the following combinations of days: Mondays, Wednesdays, and Fridays (as shown) Tuesdays, Thursdays, and Saturdays Tuesdays and...

[![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")](https://exceljet.net/formulas/sequence-of-workdays)

### [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE...

[![Excel formula: Sequence of days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_days.png "Excel formula: Sequence of days")](https://exceljet.net/formulas/sequence-of-days)

### [Sequence of days](https://exceljet.net/formulas/sequence-of-days)

The goal is to generate a series of sequential dates with a formula. In the current version of Excel, the easiest method is to use the SEQUENCE function. SEQUENCE can return all dates at the same time into a range on the worksheet. In older versions of Excel without the SEQUENCE function, you can...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

Related functions
-----------------

[![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")](https://exceljet.net/functions/workday.intl-function)

### [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be...

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

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

*   [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)
    
*   [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)
    
*   [Sequence of days](https://exceljet.net/formulas/sequence-of-days)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    

### Functions

*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
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