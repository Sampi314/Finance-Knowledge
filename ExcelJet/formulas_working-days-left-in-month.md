# Working days left in month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/working-days-left-in-month

---

[Skip to main content](https://exceljet.net/formulas/working-days-left-in-month#main-content)

[](https://exceljet.net/formulas/working-days-left-in-month#)

*   [Previous](https://exceljet.net/formulas/working-days-in-year)
    
*   [Next](https://exceljet.net/formulas/year-is-a-leap-year)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Working days left in month
==========================

by Dave Bruns · Updated 16 Oct 2019

Related functions 
------------------

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

[NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Working days left in month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/working%20days%20left%20in%20month.png "Excel formula: Working days left in month")

Summary
-------

To calculate the number of workdays remaining in a month, you can use the NETWORKDAYS function. NETWORKDAYS automatically excludes weekends, and it can optionally exclude a custom list of holidays as well. In the example shown, the formula in C5 is:

    =NETWORKDAYS(B5,EOMONTH(B5,0),E5:E14)
    

Were B5 contains a current date, and the range E5:E14 contains dates that are holidays.

_Note: NETWORKDAYS includes both the start and end dates in the calculation if they are workdays._

Generic formula
---------------

    =NETWORKDAYS(date,EOMONTH(date,0),holidays)

Explanation 
------------

NETWORKDAYS is a built in function accepts a start date, end date, and (optionally) a range that contains holiday dates.

In this case, the start date is Jan 10, 2018, provided as cell B5. The end date is calculated using the EOMONTH function with an offset of zero, which returns the last day of the month of the date given. A list of holidays is provided as the range E5:E14.

The EOMONTH function resolves to Jan 31, 2018, and the number of working days between Jan 10 and Jan 31 (inclusive) is 16. One of those working days (Jan 15) is listed as a holiday, so NETWORKDAYS returns a final result of 15.

### Working days remaining this month

To return the working days that remain in the current month, the formula can be adapted with the TODAY function as follows:

    =NETWORKDAYS(TODAY(),EOMONTH(TODAY(),0),holidays)
    

### Custom workdays / weekends

To work with custom weekends (i.e. weekends are Sunday and Monday, etc.) switch to the more robust NETWORKDAYS.INTL function, which allows control over which days of the week are considered workdays. See [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)
 for more information.

### Need a date?

If you need to calculate a date **n** workdays in the past or future, see the [WORKDAY](https://exceljet.net/functions/workday-function)
 function.

Related formulas
----------------

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

*   [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    
*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Get work hours between dates custom schedule](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule)
    
*   [List holidays between two dates](https://exceljet.net/formulas/list-holidays-between-two-dates)
    

### Functions

*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    
*   [NETWORKDAYS.INTL Function](https://exceljet.net/functions/networkdays.intl-function)
    
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