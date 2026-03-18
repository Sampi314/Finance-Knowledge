# Add business days to date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-business-days-to-date

---

[Skip to main content](https://exceljet.net/formulas/add-business-days-to-date#main-content)

[](https://exceljet.net/formulas/add-business-days-to-date#)

*   [Previous](https://exceljet.net/formulas/round-to-nearest-5)
    
*   [Next](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Add business days to date
=========================

by Dave Bruns · Updated 14 Apr 2025

Related functions 
------------------

[WORKDAY](https://exceljet.net/functions/workday-function)

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8340/download?token=FndhGtT_)
 (20.3 KB)

![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")

Summary
-------

To add or subtract business days (workdays) to a date, you can use a formula based on the [WORKDAY function](https://exceljet.net/functions/workday-function)
. In the example, the formulas in G5 and G6 are:

    =WORKDAY(start,days)
    =WORKDAY(start,days,holidays)
    

Where _start_ (B5), _days_ (B8), and _holidays_ (B11:B13) are [named ranges](https://exceljet.net/glossary/named-range)
. Both formulas show the result of adding 5 workdays, starting from December 23, 2024. The first formula excludes weekends only returns December 30, 2024. The second formula excludes weekends _and_ holidays and returns January 2, 2025.

_Notes: This is a basic example based on a standard 5-day workweek. If you need to customize which days are workdays and non-work days,_ [_see this page_](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)
_. (2) The dates in columns D and E are not required in this solution, they exist only to help visualize how the WORKDAY function evaluates working and non-working days and arrives at a final result. See below for details on how this is set up._

Generic formula
---------------

    =WORKDAY(start,days,holidays)

Explanation 
------------

In this example, the goal is to calculate a workday _n_ days in the future while excluding weekends and optionally holidays. For convenience, _start_ (B5), _days_ (B8), and _holidays_ (B11:B13) are [named ranges](https://exceljet.net/glossary/named-range)
. The dates in columns D and E are dynamically generated based on the start date in B5. Conditional formatting is used to shade excluded days in gray and to highlight the final calculated dates in yellow. All calculations are performed with the WORKDAY function.

### The WORKDAY function

Excel's [WORKDAY function](https://exceljet.net/functions/workday-function)
 takes a date and returns the next working day _n_ days in the future or past. You can use the WORKDAY function to calculate ship dates, delivery dates, and completion dates that need to take into account working and non-working days. For example, with a start date in cell A1, you can calculate a date 5 workdays in the future with a formula like this:

    =WORKDAY(A1,5)

In this basic configuration, WORKDAY will automatically exclude Saturdays and Sundays, and return the next workday 5 days after the starting date. WORKDAY can optionally exclude holidays as well as weekends. For example, with a list of holiday dates in the range C1:C3 you can calculate the next workday 5 days after the starting date in A1 while also excluding holidays:

    =WORKDAY(A1,5,C1:C3)

### WORKDAY solution

The worksheet in the example shown contains 3 named ranges: _start_ (B5), _days_ (B8), and _holidays_ (B11:B13). The names are for convenience only and make the formulas easier to read. The formula in cell G5 calculates the next working day 5 days after December 23, 2024, and _does not_ take into account holidays:

    =WORKDAY(start,days) // returns 30-Dec-2024
    

The result is Monday, December 30, 2024. The formula in cell G6 performs the same calculation but also excludes the dates in _holidays_ (B11:B13).

    =WORKDAY(start,days,holidays) // returns 02-Jan-2025
    

The result is Thursday, January 2, 2025. Notice the holidays in the range B11:B13 are valid dates.

### Data visualization

The dates in columns D and E are not required in this solution, they exist only to help visualize how the WORKDAY function evaluates working and non-working days and arrives at a final result. The dates are dynamically generated based on the start date with [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. The formula in D5 and E5 is the same and looks like this:

    =SEQUENCE(13,1,start)

*   _rows_ - 13 (arbitrary, can be increased or decreased)
*   _columns_ - 1
*   _start_ - start (cell B5, which contains 23-Dec-2024)

With this configuration, SEQUENCE generates 13 dates, starting with the start date in cell B5. This works because [Excel dates](https://exceljet.net/glossary/excel-date)
 are stored as serial numbers. To make it easy to see what day of the week each date is, the dates in the range D5:E17 are formatted with the following [custom number format](https://exceljet.net/articles/custom-number-formats)
:

    ddd, dd-mmm-yy

This date format displays an abbreviated day name (e.g. "Mon") followed by the date.

### Shading non-working days with conditional formatting

The gray shading indicates which days are not workdays and this formatting is applied with [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
. The key is to use the WORKDAY function to trigger the formatting to accurately illustrate how WORKDAY evaluates working and non-working days in this date range. In column D the conditional formatting is triggered by this formula:

    =WORKDAY(D5-1,1)<>D5

Essentially, we are asking WORKDAY if each date is not a workday by running the date through the workday function and then checking if the date is not equal to itself. Because WORKDAY will not evaluate a date if zero is provided for days, we use [a workaround formula](https://exceljet.net/formulas/date-is-workday)
 that first subtracts 1 day from the start date and then asks for the next workday. If the result from WORKDAY is not equal to the original date, it means WORKDAY shifted the date because it is a non-working day. The formula returns TRUE and the shading is applied.

To shade non-working days in column E, we use this formula:

    =WORKDAY(E5-1,1,holidays)<>E5

The two formulas are very similar, but this formula also provides the named range _holidays_ (B11:B13). The result is that more days are shaded since both weekends and holidays are non-working days.

### Highlighting final results with conditional formatting

The formulas that highlight the final calculated dates in yellow look like this:

    =D5=$G$5 // column D
    =E5=$G$6 // column E

In column D, the first formula checks for a date equal to the result in G5. In column E, the second formula checks for a date equal to the result in cell G6. Because G5 and G6 are not defined as named ranges, we must use the absolute references $G$5 and $G$6. To create independent conditional formatting rules that do not require the dates in column G, you can use the WORKDAY function directly in formulas like this:

    =D5=WORKDAY(start,days)
    =E5=WORKDAY(start,days,holidays)

The result is the same. The difference is that the conditional formatting is unlinked from column G results and therefore self-contained.

### Conditional formatting summary

In total, there are four conditional formatting rules used in the workbook shown as seen below:

![The worksheet uses four conditional formatting rules](https://exceljet.net/sites/default/files/images/formulas/inline/add_business_days_to_date_conditional_formatting_rules.png "The worksheet uses four conditional formatting rules")

> If you need to implement a custom work schedule (i.e. a 4-day workweek, a 6-day workweek, etc.) you will want to switch to the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
>  which provides more flexibility. See [this example](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)
>  for details.

Related formulas
----------------

[![Excel formula: Add workdays to date custom workweek](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_workdays_to_date_custom_workweek.png "Excel formula: Add workdays to date custom workweek")](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)

### [Add workdays to date custom workweek](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)

In this example, the goal is to calculate a workday n days in the future based on a 4-day workweek and, optionally, holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Add days exclude certain days of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Add%20days%20exclude%20certain%20days%20of%20week.png "Excel formula: Add days exclude certain days of week")](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)

### [Add days exclude certain days of week](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)

The WORKDAY.INTL function is based on the WORKDAY function , which is designed to add work days to a date. WORKDAY automatically excludes Saturday and Sunday, and optionally can exclude a list of custom holidays. The WORKDAY.INTL does the same thing, but makes it possible to exclude any days of the...

[![Excel formula: Date is workday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_workday.png "Excel formula: Date is workday")](https://exceljet.net/formulas/date-is-workday)

### [Date is workday](https://exceljet.net/formulas/date-is-workday)

In this example, the goal is to test a date to determine whether it is a workday. In Excel, you can use either the WORKDAY function or its more flexible sibling WORKDAY.INTL to accomplish this task. WORKDAY function The WORKDAY function calculates a date in the future or past that is, by definition...

[![Excel formula: Get project end date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20project%20end%20date.png "Excel formula: Get project end date")](https://exceljet.net/formulas/get-project-end-date)

### [Get project end date](https://exceljet.net/formulas/get-project-end-date)

This formula uses the WORKDAY function to calculate an end date. WORKDAY can calculate dates in the future or past, and automatically excludes weekends and holidays (if provided). In the example shown, we have the project start date in column C, and days in column D. Days represents the duration of...

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

*   [Add workdays to date custom workweek](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)
    
*   [Add days exclude certain days of week](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)
    
*   [Date is workday](https://exceljet.net/formulas/date-is-workday)
    
*   [Get project end date](https://exceljet.net/formulas/get-project-end-date)
    

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