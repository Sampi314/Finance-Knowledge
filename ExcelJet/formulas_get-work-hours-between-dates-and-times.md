# Get work hours between dates and times - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-work-hours-between-dates-and-times

---

[Skip to main content](https://exceljet.net/formulas/get-work-hours-between-dates-and-times#main-content)

[](https://exceljet.net/formulas/get-work-hours-between-dates-and-times#)

*   [Previous](https://exceljet.net/formulas/get-work-hours-between-dates)
    
*   [Next](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get work hours between dates and times
======================================

by Dave Bruns · Updated 9 Jul 2020

Related functions 
------------------

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

![Excel formula: Get work hours between dates and times](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20work%20hours%20between%20dates%20and%20times.png "Excel formula: Get work hours between dates and times")

Summary
-------

To calculate total work hours between two dates and times, you can use a formula based on the NETWORKDAYS function. In the example shown, E5 contains this formula:

    =(NETWORKDAYS(B5,C5)-1)*(upper-lower)
    +IF(NETWORKDAYS(C5,C5),MEDIAN(MOD(C5,1),upper,lower),upper)
    -MEDIAN(NETWORKDAYS(B5,B5)*MOD(B5,1),upper,lower)
    

where "lower" is the [named range](https://exceljet.net/glossary/named-range)
 H5 and "upper" is the named range H6.

_Note: this example was inspired by [a formula challenge on Chandoo](https://chandoo.org/wp/working-hours-formula/)
, and a more complete solution provided by [formula master Barry Houdini](https://www.mrexcel.com/forum/excel-questions/426101-calculate-only-working-hours-between-two-dates-excluding-weekends.html)
 on the MrExcel forum._

Generic formula
---------------

    =(NETWORKDAYS(start,end)-1)*(upper-lower)
    +IF(NETWORKDAYS(end,end),MEDIAN(MOD(end,1),upper,lower),upper)
    -MEDIAN(NETWORKDAYS(start,start)*MOD(start,1),upper,lower)
    

Explanation 
------------

This formula calculates total working hours between two dates and times, that occur between a "lower" and "upper" time. In the example shown, the lower time is 9:00 AM and the upper time is 5:00 PM. These appear in the formula as the [named ranges](https://exceljet.net/glossary/named-range)
 "lower" and "upper".

The logic of the formula is to calculate all possible working hours between the start and end dates, inclusive, then back out any hours on the start date that occur between the start time and lower time, and any hours on the end date that occur between the end time and the upper time.

The [NETWORKDAYS function](https://exceljet.net/functions/networkdays-function)
 handles the exclusion of weekends and holidays (when provided as a range of dates). You can switch to [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)
 if your schedule has non-standard working days.

### Formatting output

The result is a number which represents total hours. Like all [Excel times](https://exceljet.net/glossary/excel-time)
, you will need to format the output with a suitable [number format](https://exceljet.net/articles/custom-number-formats)
. In the example shown, we are using:

    [h]:mm
    

The square brackets stop Excel from rolling over when hours are greater than 24. In other words, they make it possible to display hours greater than 24. If you need a decimal value for hours, you can [multiply the result by 24](https://exceljet.net/formulas/convert-excel-time-to-decimal-hours)
 and format as a regular number.

### Simple version

If start and end times will _always_ occur between lower and upper times, you can use a simpler version of this formula:

    =(NETWORKDAYS(B5,C5)-1)*(upper-lower)+MOD(C5,1)-MOD(B5,1)
    

### No start time and end time

To calculate total work hours between two dates, assuming all days are full workdays, you can use an even simpler formula:

    =NETWORKDAYS(start,end,holidays)*hours
    

See [explanation here](https://exceljet.net/formulas/get-work-hours-between-dates)
 for details.

Related formulas
----------------

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Get work hours between dates custom schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20custom2.png "Excel formula: Get work hours between dates custom schedule")](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

### [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

At the core, this formula uses the WEEKDAY function to figure out the day of week (i.e. Monday, Tuesday, etc.) for every day between the two given dates. WEEKDAY returns a number between 1 and 7. With default settings, Sunday=1 and Saturday = 7. The trick to this formula is assembling an array of...

[![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")](https://exceljet.net/formulas/get-work-hours-between-dates)

### [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per...

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

*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)
    
*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    
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