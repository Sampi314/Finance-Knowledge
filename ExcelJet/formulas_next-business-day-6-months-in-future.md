# Next business day 6 months in future - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/next-business-day-6-months-in-future

---

[Skip to main content](https://exceljet.net/formulas/next-business-day-6-months-in-future#main-content)

[](https://exceljet.net/formulas/next-business-day-6-months-in-future#)

*   [Previous](https://exceljet.net/formulas/next-biweekly-payday-from-date)
    
*   [Next](https://exceljet.net/formulas/next-working-day)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Next business day 6 months in future
====================================

by Dave Bruns · Updated 25 Aug 2016

Related functions 
------------------

[WORKDAY](https://exceljet.net/functions/workday-function)

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

![Excel formula: Next business day 6 months in future](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/next%20business%20day%206%20months%20in%20future.png "Excel formula: Next business day 6 months in future")

Summary
-------

To get a date 6 months in the future, on the next work day, you can use a formula based on the WORKDAY function, with help from EDATE.

In the example shown, the formula in C6 is

    =WORKDAY(EDATE(B6,6)-1,1,B9:B11)
    

Generic formula
---------------

    =WORKDAY(EDATE(date,6)-1,1,holidays)

Explanation 
------------

Working from the inside out, EDATE first calculates a date 6 months in the future. In the example shown, that date is December 24, 2015.

Next, the formula subtracts 1 day to get December 23, 2015, and the result goes into the WORKDAY function as the start date, with days = 1, and the range B9:B11 provided for holidays.

WORKDAY then calculates the next business day one day in the future, taking into account holidays and weekends.

If you need more flexibility with weekends, you can use WORKDAY.INTL.

Related formulas
----------------

[![Excel formula: Date is workday](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/date_is_workday.png "Excel formula: Date is workday")](https://exceljet.net/formulas/date-is-workday)

### [Date is workday](https://exceljet.net/formulas/date-is-workday)

In this example, the goal is to test a date to determine whether it is a workday. In Excel, you can use either the WORKDAY function or its more flexible sibling WORKDAY.INTL to accomplish this task. WORKDAY function The WORKDAY function calculates a date in the future or past that is, by definition...

[![Excel formula: Calculate retirement date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20retirement%20date.png "Excel formula: Calculate retirement date")](https://exceljet.net/formulas/calculate-retirement-date)

### [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)

In this example, the goal is to calculate a retirement date at age 60, based on a given birthdate. The simplest way to do this is with the EDATE function. The EDATE function will return a date n months in the future or past when given a date and the number of months to traverse. In this case, we...

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

*   [Date is workday](https://exceljet.net/formulas/date-is-workday)
    
*   [Calculate retirement date](https://exceljet.net/formulas/calculate-retirement-date)
    

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