# Get project midpoint - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-project-midpoint

---

[Skip to main content](https://exceljet.net/formulas/get-project-midpoint#main-content)

[](https://exceljet.net/formulas/get-project-midpoint#)

*   [Previous](https://exceljet.net/formulas/get-project-end-date)
    
*   [Next](https://exceljet.net/formulas/get-project-start-date)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get project midpoint
====================

by Dave Bruns · Updated 26 Sep 2018

Related functions 
------------------

[WORKDAY](https://exceljet.net/functions/workday-function)

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

![Excel formula: Get project midpoint](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20project%20midpoint2.png "Excel formula: Get project midpoint")

Summary
-------

To calculate an approximate project midpoint date, you can use the WORKDAY function. In the example shown, the formula in E5 is:

    =WORKDAY(C5,E5/2,holidays)
    

where "holidays" is the [named range](https://exceljet.net/glossary/named-range)
 G5:G10.

Generic formula
---------------

    =WORKDAY(start,days/2,holidays)

Explanation 
------------

The WORKDAY function returns a date in the future or past, based on a start date, workdays, and optional holidays. WORKDAY automatically excludes weekends, and counts only Monday through Friday as workdays.

In the example shown, WORKDAY is configured to get a project midpoint date by adding half of the days value to the start date:

    =WORKDAY(C5,E5/2,holidays)
    

Project A is 5 workdays, so E5/2 = 2.5 days. The WORKDAY function ignores fractional values and uses only the integer portion of days, so it uses the value 2 to return a date of May 8.

Note the WORKDAY function does not count the start date as a workday.

### Custom schedule

The WORKDAY function always treats Saturday and Sunday as non-working days. To get a midpoint for a project where working days are not Monday-Friday, substitute the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
 for WORKDAY. For example, to calculate a midpoint in a project where workdays are Monday-Saturday you can use a formula like this:

    =WORKDAY.INTL(start,days/2,11,holidays)
    

There are many other ways to configure WORKDAY.INTL. [This page provides details](https://exceljet.net/functions/workday.intl-function)
.

Related formulas
----------------

[![Excel formula: Get project end date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20project%20end%20date.png "Excel formula: Get project end date")](https://exceljet.net/formulas/get-project-end-date)

### [Get project end date](https://exceljet.net/formulas/get-project-end-date)

This formula uses the WORKDAY function to calculate an end date. WORKDAY can calculate dates in the future or past, and automatically excludes weekends and holidays (if provided). In the example shown, we have the project start date in column C, and days in column D. Days represents the duration of...

[![Excel formula: Get project start date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20project%20start%20date.png "Excel formula: Get project start date")](https://exceljet.net/formulas/get-project-start-date)

### [Get project start date](https://exceljet.net/formulas/get-project-start-date)

This formula is uses the WORKDAY function, which returns a date in the future or past, based on start date and required work days. WORKDAY automatically excludes weekends, and can also exclude holidays if provided as a range of dates. In the example shown, the project end date is in column C, and...

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

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

*   [Get project end date](https://exceljet.net/formulas/get-project-end-date)
    
*   [Get project start date](https://exceljet.net/formulas/get-project-start-date)
    
*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    

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