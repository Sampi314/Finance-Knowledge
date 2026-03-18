# Working days in year - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/working-days-in-year

---

[Skip to main content](https://exceljet.net/formulas/working-days-in-year#main-content)

[](https://exceljet.net/formulas/working-days-in-year#)

*   [Previous](https://exceljet.net/formulas/workdays-per-month)
    
*   [Next](https://exceljet.net/formulas/working-days-left-in-month)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Working days in year
====================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

[DATE](https://exceljet.net/functions/date-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Working days in year](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/working%20days%20in%20year.png "Excel formula: Working days in year")

Summary
-------

To calculate the number of working days in a year, you can use the NETWORKDAYS function. NETWORKDAYS automatically excludes weekends and holidays if they are provided. In the example shown, the formula in E5 is:

    =NETWORKDAYS(DATE(D5,1,1),DATE(D5,12,31),holidays)
    

Where D5 contains a year, and **holidays** is the [named range](https://exceljet.net/glossary/named-range)
 E5:E14.

_Note: NETWORKDAYS includes both the start and end dates in the calculation if they are workdays._

Generic formula
---------------

    =NETWORKDAYS(DATE(year,1,1),DATE(year,12,31),holidays)

Explanation 
------------

NETWORKDAYS is a built-in function accepts a start date, an end date, and (optionally) a range that contains holiday dates. In the example shown, we generate the start and end date using the [DATE function](https://exceljet.net/functions/date-function)
 like this:

    DATE(D5,1,1) // first day of year
    DATE(D5,12,31) // last day of year
    

The DATE function returns these dates directly to the NETWORKDAYS function as start\_date and end\_date, respectively.

Holidays are supplied as a list of dates in E5:E14, the named range **holidays**.

NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and dates supplied as holidays and returns a total count of working days in the year 2019.

### No holidays provided

The formula in E6 returns a higher working day count because holidays are not supplied:

    =NETWORKDAYS(DATE(D6,1,1),DATE(D6,12,31))
    

### Working days remaining this year

To return the working days that remain in a given year, the TODAY function can be used to generate a start date like this:

    =NETWORKDAYS(TODAY(),DATE(D5,12,31),holidays)
    

### Custom workdays/weekends

To work with custom weekends (i.e. weekends are Sunday and Monday, etc.) switch to the more powerful [NETWORKDAYS.INTL function](https://exceljet.net/functions/networkdays.intl-function)
, which allows control over which days of the week are considered workdays.

Related formulas
----------------

[![Excel formula: Workdays per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/workdays%20per%20month.png "Excel formula: Workdays per month")](https://exceljet.net/formulas/workdays-per-month)

### [Workdays per month](https://exceljet.net/formulas/workdays-per-month)

First, it's important to understand that the values in the Month column (B) are actual dates, formatted with the custom number format "mmm". For example, B4 contains January 1, 2014, but displays only "Jan" per the custom number format. The formula itself is based on the NETWORKDAYS function, which...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")](https://exceljet.net/formulas/get-work-hours-between-dates)

### [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per...

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Get work hours between dates custom schedule](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20custom2.png "Excel formula: Get work hours between dates custom schedule")](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

### [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)

At the core, this formula uses the WEEKDAY function to figure out the day of week (i.e. Monday, Tuesday, etc.) for every day between the two given dates. WEEKDAY returns a number between 1 and 7. With default settings, Sunday=1 and Saturday = 7. The trick to this formula is assembling an array of...

[![Excel formula: List holidays between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20holidays%20between%20two%20dates.png "Excel formula: List holidays between two dates")](https://exceljet.net/formulas/list-holidays-between-two-dates)

### [List holidays between two dates](https://exceljet.net/formulas/list-holidays-between-two-dates)

At a high level, this formula uses a nested IF function to return an array of holidays between two dates. This array is then processed by the TEXTJOIN function, which converts the array to text using a comma as the delimiter. Working from the inside out, we generate the array of matching holidays...

Related functions
-----------------

[![Excel NETWORKDAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays%20function.png "Excel NETWORKDAYS function")](https://exceljet.net/functions/networkdays-function)

### [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can _optionally_ exclude a list of holidays supplied as dates. ...

[![Excel NETWORKDAYS.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays.intl%20function.png "Excel NETWORKDAYS.INTL function")](https://exceljet.net/functions/networkdays.intl-function)

### [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)

The Excel NETWORKDAYS.INTL function calculates the number of working days between two dates. NETWORKDAYS.INTL can optionally exclude a list of holidays and provides a way to specify which days of the week are considered weekends.

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Workdays per month](https://exceljet.net/formulas/workdays-per-month)
    
*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    
*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)
    
*   [List holidays between two dates](https://exceljet.net/formulas/list-holidays-between-two-dates)
    

### Functions

*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

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