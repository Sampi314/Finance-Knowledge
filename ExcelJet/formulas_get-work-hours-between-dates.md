# Get work hours between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-work-hours-between-dates

---

[Skip to main content](https://exceljet.net/formulas/get-work-hours-between-dates#main-content)

[](https://exceljet.net/formulas/get-work-hours-between-dates#)

*   [Previous](https://exceljet.net/formulas/get-week-number-from-date)
    
*   [Next](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get work hours between dates
============================

by Dave Bruns · Updated 2 Oct 2018

Related functions 
------------------

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")

Summary
-------

To calculate the total number of work hours between two dates, you can use a formula based on the NETWORKDAYS function, where "start" is the start date, "end" is the end date, "holidays" is a range that includes dates, and "hours" is the number of work hours in a workday. In the example shown, the formula in D7 is:

    =NETWORKDAYS(B7,C7,holidays)*8

where "holidays" is the [named range](https://exceljet.net/glossary/named-range)
 G6:G8.

Generic formula
---------------

    =NETWORKDAYS(start,end,holidays)*hours

Explanation 
------------

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per day, 8 in the example shown.

The NETWORKDAYS function includes both the start and end date in the calculation, and excludes both Saturday and Sunday by default. The function will also exclude holidays when then are provided as the "holidays" argument as a range of valid dates.

In these example shown, the first two formulas use the NETWORKDAYS function.

    D6=NETWORKDAYS(B6,C6)*8 // no holidays
    D7=NETWORKDAYS(B7,C7,holidays)*8 // holidays provided
    

If your workweek includes days other than Monday through Friday, you can switch to the [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)
 function, which provides a "weekend" argument that can be used to define which days of the week are workdays and weekend days. NETWORKDAYS.INTL can be configured just like NETWORKDAYS, but it provides an additional argument called "weekend" to control which days in a week are considered workdays.

The next 4 formulas use the NETWORKDAYS.INTL function:

    D8=NETWORKDAYS.INTL(B8,C8)*8 // Mon-Fri, no holidays
    D9=NETWORKDAYS.INTL(B9,C9,11)*8 // Mon-Sat, no holidays
    D10=NETWORKDAYS.INTL(B10,C10)*8 // M-F, no holidays
    D11=NETWORKDAYS.INTL(B11,C11,1,holidays)*8 // M-F, w/ holidays
    

Click the function names above to learn more about configuration options.

### Custom work schedule

This formula assumes all working days have the same number of work hours. If you need to calculate work hours with a custom schedule where work hours vary according to the day of week, you can try a formula like this:

    =SUMPRODUCT(MID(schedule,WEEKDAY(ROW(INDIRECT(start&":"&end))),1)*ISNA(MATCH(ROW(INDIRECT(start&":"&end)),holidays,0)))
    

You can find an [explanation here](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)
.

Related formulas
----------------

[![Excel formula: Get work hours between dates and times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20and%20times.png "Excel formula: Get work hours between dates and times")](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)

### [Get work hours between dates and times](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)

This formula calculates total working hours between two dates and times, that occur between a "lower" and "upper" time. In the example shown, the lower time is 9:00 AM and the upper time is 5:00 PM. These appear in the formula as the named ranges "lower" and "upper". The logic of the formula is to...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Get work hours between dates custom schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20custom2.png "Excel formula: Get work hours between dates custom schedule")](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

### [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

At the core, this formula uses the WEEKDAY function to figure out the day of week (i.e. Monday, Tuesday, etc.) for every day between the two given dates. WEEKDAY returns a number between 1 and 7. With default settings, Sunday=1 and Saturday = 7. The trick to this formula is assembling an array of...

Related functions
-----------------

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

*   [Get work hours between dates and times](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)
    
*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)
    

### Functions

*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)
    

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