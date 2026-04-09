# Add workdays to date custom workweek - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-workdays-to-date-custom-workweek

---

[Skip to main content](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek#main-content)

[](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek#)

*   [Previous](https://exceljet.net/formulas/add-months-to-date)
    
*   [Next](https://exceljet.net/formulas/add-years-to-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Add workdays to date custom workweek
====================================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

[WORKDAY](https://exceljet.net/functions/workday-function)

![Excel formula: Add workdays to date custom workweek](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add_workdays_to_date_custom_workweek.png "Excel formula: Add workdays to date custom workweek")

Summary
-------

To add or subtract workdays to a date using a custom workweek schedule, you can use a formula based on the [WORKDAY.INTL function](https://exceljet.net/functions/workday-intl-function)
. In the worksheet shown, we have configured WORKDAY.INTL to apply a four-day workweek, Monday through Thursday, where Friday, Saturday, and Sunday are days off. The formulas in G5 and G6 are:

    =WORKDAY.INTL(start,days,"0000111")
    =WORKDAY.INTL(start,days,"0000111",holidays)
    

Where _start_ (B5), _days_ (B8), and _holidays_ (B11:B13) are [named ranges](https://exceljet.net/glossary/named-range)
. Both formulas show the result of adding 4 workdays, starting from December 23, 2024. The first formula excludes weekends (Friday-Sunday) and returns December 30, 2024. The second formula excludes weekends _and_ holidays and returns January 2, 2025.

_Notes: (1) This example builds on the_ [_more basic solution here_](https://exceljet.net/formulas/add-business-days-to-date)
_, which uses the_ [_WORKDAY function_](https://exceljet.net/functions/workday-function)
 _and a standard 5-day workweek. (2) The dates in columns D and E are not required in this solution; they exist only to help visualize how the WORKDAY.INTL function evaluates working and non-working days and arrives at a final result. See below for details on how this is set up._

Generic formula
---------------

    =WORKDAY.INTL(start,days,"0000111",holidays)

Explanation 
------------

In this example, the goal is to calculate a workday _n_ days in the future based on a 4-day workweek and, optionally, holidays. For convenience, _start_ (B5), _days_ (B8), and _holidays_ (B11:B13) are [named ranges](https://exceljet.net/glossary/named-range)
. The dates in columns D and E are dynamically generated based on the start date in B5. Conditional formatting is used to shade excluded days in gray and to highlight the final calculated dates in yellow. All calculations are performed with the WORKDAY.INTL function.

### The WORKDAY.INTL function

Excel's [WORKDAY.INTL function](https://exceljet.net/functions/workday-intl-function)
 takes a date and returns the next working day _n_ days in the future or past. Unlike the simpler WORKDAY function, WORKDAY.INTL can be configured to make any day of the week a workday or a non-workday. You can use the WORKDAY.INTL function to calculate ship dates, delivery dates, and completion dates that must be calculated based on workdays. For example, with a start date in cell A1, you can calculate a date 4 workdays in the future based on a 4-day workweek (Mon-Thu) like this:

    =WORKDAY.INTL(A1,4,"0000111")

In this configuration, WORKDAY.INTL will exclude Friday, Saturday, and Sunday, and return the next workday, 4 days after the starting date. The 7-digit code "0000111" is supplied for the _weekend_ argument. This is what defines workdays and non-workdays. There is one digit for each day of the week, Monday through Saturday. In this scheme, a 1 indicates a weekend (non-working) day, and a 0 indicates a workday. The code "0000111" means Monday through Thursday are workdays, and Friday through Sunday are weekends (i.e., non-working days).

> You can also provide numeric codes to set preconfigured combinations of workdays and weekends. For example, the number 11 means weekends are "Sunday only". However, the numbers are arbitrary and personally, I think the text string option is better since it will handle any combination of workdays and weekdays, and is at least marginally intuitive :) See our [WORKDAY.INTL page](https://exceljet.net/functions/workday.intl-function)
>  for details.

WORKDAY.INTL can optionally exclude holidays as well. For example, with a list of holiday dates in the range C1:C3, you can calculate the next workday 4 days after the starting date in A1 while also excluding the dates in C1:C3:

    =WORKDAY.INTL(A1,4,"0000111",C1:C3)

### WORKDAY.INTL solution

Now that we have the basics out of the way, let's look at how the formulas in the example shown are configured. The worksheet in the example shown contains 3 named ranges: _start_ (B5), _days_ (B8), and _holidays_ (B11:B13). The names are for convenience only and make the formulas easier to read. The formula in cell G5 calculates the next working day 4 days after December 23, 2024, and _does not_ take into account holidays:

    =WORKDAY.INTL(start,days,"0000111") // returns 30-Dec-2024
    

The weekend code "0000111" defines a 4-day workweek, Monday through Thursday. The result is Monday, December 30, 2024. The formula in cell G6 performs the same calculation but also excludes the dates in _holidays_ (B11:B13).

    =WORKDAY.INTL(start,days,"0000111",holidays) // returns 02-Jan-2025
    

The result is Thursday, January 2, 2025. Notice the holidays in the range B11:B13 are valid dates. When providing holidays, only the date matters. The name of the holiday is not relevant.

### Data visualization

To help visualize what WORKDAY.INTL is actually doing, the worksheet also includes a range of dates in columns D and E. This part of the worksheet is not required in this solution; it exists only to help visualize how the WORKDAY.INTL function evaluates working and non-working days and arrives at a final result. The dates are dynamically generated based on the start date with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. The formulas in D5 and E5 are identical and look like this:

    =SEQUENCE(13,1,start)

*   _rows_ - 13 (this number is arbitrary and can be increased or decreased)
*   _columns_ - 1
*   _start_ - start (cell B5, which contains 23-Dec-2024)

With this configuration, SEQUENCE generates 13 dates, starting with the start date in cell B5. This works because [Excel dates](https://exceljet.net/glossary/excel-date)
 are stored as serial numbers. However, the dates must be formatted as dates. Otherwise, Excel might display the raw serial numbers. To make it easy to see what day of the week each date is, the dates in the range D5:E17 are formatted with the following [custom number format](https://exceljet.net/articles/custom-number-formats)
:

    ddd, dd-mmm-yy

This date format displays an abbreviated day name (e.g., "Mon") followed by the date.

### Shading non-working days with conditional formatting

Part of the visualization involves shading non-working days in gray, which is done with [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
 triggered by a formula. To keep this formatting in sync with the results in column G, we must use the WORKDAY.INTL function. In column D, the formula used to trigger the conditional formatting looks like this:

    =WORKDAY.INTL(D5-1,1,"0000111")<>D5

Essentially, we are testing for non-work days by comparing the output from WORKDAY.INTL to the original date. The formula is slightly convoluted because we can't test the date directly; we need to use [a workaround formula](https://exceljet.net/formulas/date-is-workday)
 that first subtracts 1 day from the start date and then asks for the next workday. If the result from WORKDAY.INTL _is not equal to the original date_, it means WORKDAY.INTL shifted the date because it is a non-working day. The formula returns TRUE, and the shading is applied.

To shade non-working days in column E, we use a similar formula that also includes our list of holidays in B11:B13:

    =WORKDAY.INTL(E5-1,1,"0000111",holidays)<>E5

The result is that more days are shaded since both weekends and holidays are non-working days.

### Highlighting final results with conditional formatting

Finally, we have the two formulas that highlight in yellow the calculated dates in column G:

    =D5=$G$5 // column D
    =E5=$G$6 // column E

In column D, the first formula checks for a date equal to the result in G5. In column E, the second formula checks for a date equal to the result in cell G6. Because G5 and G6 are not defined as named ranges, we must use the [absolute references](https://exceljet.net/glossary/absolute-reference)
 $G$5 and $G$6.

To create independent conditional formatting rules that do not require the dates in column G, you can use self-contained formulas that use WORKDAY.INTL directly like this:

    =D5=WORKDAY.INTL(start,days,"0000111")
    =E5=WORKDAY.INTL(start,days,"0000111",holidays)

The result is the same. The difference is that the conditional formatting is unlinked from column G results.

### Conditional formatting summary

There are four conditional formatting rules used in the workbook shown as seen below:

![The four conditional formatting rules used in the workbook shown](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/add_workdays_to_date_custom_workweek_conditional_formatting_rules_0.png "The four conditional formatting rules used in the workbook shown")

### Add workdays - Sunday only weekends

By default, the WORKDAY.INTL function will exclude "normal" weekends where Saturday and Sunday are non-working days. To specify a custom workweek where only Sunday is a weekend day, you can use the weekend code "0000001". With this adjustment, the formulas in cells G5 and G6 are:

    =WORKDAY.INTL(start,days,"0000001")
    =WORKDAY.INTL(start,days,"0000001",holidays)

The formulas that trigger the conditional formatting that shades non-working days columns D and E look like this:

    =WORKDAY.INTL(D5-1,1,"0000001")<>D5
    =WORKDAY.INTL(E5-1,1,"0000001",holidays)<>E5
    

![Example of a custom workweek with Sunday-only weekends](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/add_workdays_to_date_custom_workweek_sunday_only.png "Example of a custom workweek with Sunday-only weekends")

### Add workdays - no weekends

In the worksheet below, we have configured the WORKDAY.INTL formulas to define a custom workweek with no weekends. The formulas in cells G5 and G6 are:

    =WORKDAY.INTL(start,days,"0000000")
    =WORKDAY.INTL(start,days,"0000000",holidays)

The code "0000000" for the weekend argument means no days of the week are weekends (i.e., non-working days). The formulas that trigger the conditional formatting rules that shade non-working days columns D and E are:

    =WORKDAY.INTL(D5-1,1,"0000000")<>D5
    =WORKDAY.INTL(E5-1,1,"0000000",holidays)<>E5
    

![Example of a custom workweek with no weekends](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/add_workdays_to_date_custom_workweek_no_weekends.png "Example of a custom workweek with no weekends")

Related formulas
----------------

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Add days exclude certain days of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Add%20days%20exclude%20certain%20days%20of%20week.png "Excel formula: Add days exclude certain days of week")](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)

### [Add days exclude certain days of week](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)

The WORKDAY.INTL function is based on the WORKDAY function , which is designed to add work days to a date. WORKDAY automatically excludes Saturday and Sunday, and optionally can exclude a list of custom holidays. The WORKDAY.INTL does the same thing, but makes it possible to exclude any days of the...

[![Excel formula: Previous working day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/previous_working_day.png "Excel formula: Previous working day")](https://exceljet.net/formulas/previous-working-day)

### [Previous working day](https://exceljet.net/formulas/previous-working-day)

In the worksheet shown, column B contains 12 dates. The goal is to calculate the previous working day before each date, taking into account weekends (Saturday and Sunday) and the holidays listed in column F. The formula should automatically skip weekends and any dates considered non-working days...

[![Excel formula: Date is workday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_workday.png "Excel formula: Date is workday")](https://exceljet.net/formulas/date-is-workday)

### [Date is workday](https://exceljet.net/formulas/date-is-workday)

In this example, the goal is to test a date to determine whether it is a workday. In Excel, you can use either the WORKDAY function or its more flexible sibling WORKDAY.INTL to accomplish this task. WORKDAY function The WORKDAY function calculates a date in the future or past that is, by definition...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

[![Excel formula: Get project end date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20project%20end%20date.png "Excel formula: Get project end date")](https://exceljet.net/formulas/get-project-end-date)

### [Get project end date](https://exceljet.net/formulas/get-project-end-date)

This formula uses the WORKDAY function to calculate an end date. WORKDAY can calculate dates in the future or past, and automatically excludes weekends and holidays (if provided). In the example shown, we have the project start date in column C, and days in column D. Days represents the duration of...

[![Excel formula: Sequence of custom days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_custom_days.png "Excel formula: Sequence of custom days")](https://exceljet.net/formulas/sequence-of-custom-days)

### [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)

The goal is to generate a series of "custom" days of the week based on a start date entered in cell B5. For example, you might want to list sequential dates for any of the following combinations of days: Mondays, Wednesdays, and Fridays (as shown) Tuesdays, Thursdays, and Saturdays Tuesdays and...

Related functions
-----------------

[![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")](https://exceljet.net/functions/workday.intl-function)

### [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be...

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

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

*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Add days exclude certain days of week](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)
    
*   [Previous working day](https://exceljet.net/formulas/previous-working-day)
    
*   [Date is workday](https://exceljet.net/formulas/date-is-workday)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    
*   [Get project end date](https://exceljet.net/formulas/get-project-end-date)
    
*   [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)
    

### Functions

*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    
*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    

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