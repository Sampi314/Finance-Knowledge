# Excel NETWORKDAYS.INTL function | Exceljet

**Source:** https://exceljet.net/functions/networkdays.intl-function

---

[Skip to main content](https://exceljet.net/functions/networkdays.intl-function#main-content)

[](https://exceljet.net/functions/networkdays.intl-function#)

*   [Previous](https://exceljet.net/functions/networkdays-function)
    
*   [Next](https://exceljet.net/functions/now-function)
    

Excel 2010

[Date and time](https://exceljet.net/functions#Date-and-time)

NETWORKDAYS.INTL Function
=========================

by Dave Bruns · Updated 14 Jul 2021

Related functions 
------------------

[WORKDAY](https://exceljet.net/functions/workday-function)

[NETWORKDAYS](https://exceljet.net/functions/networkdays-function)

![Excel NETWORKDAYS.INTL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20networkdays.intl%20function.png "Excel NETWORKDAYS.INTL function")

Summary
-------

The Excel NETWORKDAYS.INTL function calculates the number of working days between two dates. NETWORKDAYS.INTL can optionally exclude a list of holidays and provides a way to specify which days of the week are considered weekends.

Purpose 
--------

Get work days between two dates

Return value 
-------------

A number representing days.

Syntax
------

    =NETWORKDAYS.INTL(start_date,end_date,[weekend],[holidays])

*   _start\_date_ - The start date.
*   _end\_date_ - The end date.
*   _weekend_ - \[optional\] Setting for which days of the week should be considered weekends.
*   _holidays_ - \[optional\] A reference to dates that should be considered non-work days.

Using the NETWORKDAYS.INTL function 
------------------------------------

The NETWORKDAYS.INTL function returns the number of working days between two dates, taking into account holidays and weekends. This function is more robust than the [NETWORKDAYS function](https://exceljet.net/functions/networkdays-function)
 because it allows you to control which days of the week are considered weekends. 

NETWORKDAYS.INTL takes four [arguments](https://exceljet.net/glossary/function-argument)
: _start\_date_, _end\_date_, _weekend_, and _holidays_. The _start\_date_, _end\_date_ and _holidays_ arguments must be [valid Excel dates](https://exceljet.net/glossary/excel-date)
. The _weekend_ argument controls which days of the week are considered weekends, and therefore not included in the count. Holidays are also treated as non-working days and will not be included in the result.

Both the weekend and holidays arguments are optional. By default, NETWORKDAYS.INTL will exclude Saturdays and Sundays, but this can be customized as explained below. To exclude holidays, supply a range that contains non-working dates for the _holiday_ argument. 

NETWORKDAYS.INTL includes both the start date and end date when calculating workdays – if you give NETWORKDAYS.INTL the same date for _start\_date_ and _end\_date_, and the date is not a weekend or holiday, the result is 1.

### Examples

In the example shown, the following formulas are used:

    =NETWORKDAYS.INTL(B5,C5) // result 1, default
    =NETWORKDAYS.INTL(B5,C5,1,holidays) // result 2, exclude holidays
    =NETWORKDAYS.INTL(B5,C5,"1000000") // result 3, Monday is weekend
    

where "holidays" is the [named range](https://exceljet.net/glossary/named-range)
 I5:I13.

Result 1 in column E shows the default configuration, where Saturday and Sunday are treated as weekends and excluded from the count. Result 2 in column D shows the effect of excluding holidays from the working day count. Result 3 shows how the NETWORKDAYS.INTL function can be configured to define custom weekends. The text string "1000000" sets Mondays as a weekend, and all other days are considered working days. See below for more detail on configuring weekends.

### Configuring weekends

The NETWORKDAYS.INTL function provides two options to configure weekends. The first option is to supply a number as shown in the table below.

|     |     |
| --- | --- |
| **Weekend number** | **Weekend days** |
| 1 (default) | Saturday, Sunday |
| 2   | Sunday, Monday |
| 3   | Monday, Tuesday |
| 4   | Tuesday, Wednesday |
| 5   | Wednesday, Thursday |
| 6   | Thursday, Friday |
| 7   | Friday, Saturday |
| 11  | Sunday only |
| 12  | Monday only |
| 13  | Tuesday only |
| 14  | Wednesday only |
| 15  | Thursday only |
| 16  | Friday only |
| 17  | Saturday only |

The second way to configure weekends is to provide a [text string](https://exceljet.net/glossary/text-value)
 composed of 1s and 0s. This text is provided as a string of 7 characters which must be either 1 or 0. In this scheme, the number 1 means weekend and 0 means workday. Each character represents a different day of the week, starting with the first character as Monday. Below are some examples:

    NETWORKDAYS.INTL(start,end,"0101011") // workdays = M,W,F
    NETWORKDAYS.INTL(start,end,"1010111") // workdays = Tue, Thu
    NETWORKDAYS.INTL(start,end,"1111100") // workdays = Sat,Sun
    NETWORKDAYS.INTL(start,end,"0000000") // all workdays, no weekends
    

### Notes:

*   If _start\_date_ is greater than _end\_date_, the function returns a negative value.
*   NETWORKDAYS.INTL includes both the start date and end date when calculating workdays. This means if you give NETWORKDAYS.INTL the same date for start date and end date, it will return 1.
*   If start\_date or end\_date are out of range, NETWORKDAYS.INTL returns the #NUM! error.
*   If weekend is invalid, NETWORKDAYS.INTL returns the #VALUE! error.

NETWORKDAYS.INTL function examples
----------------------------------

[![Excel formula: Working days left in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/working%20days%20left%20in%20month.png "Excel formula: Working days left in month")](https://exceljet.net/formulas/working-days-left-in-month)

### [Working days left in month](https://exceljet.net/formulas/working-days-left-in-month)

NETWORKDAYS is a built in function accepts a start date, end date, and (optionally) a range that contains holiday dates. In this case, the start date is Jan 10, 2018, provided as cell B5. The end date is calculated using the EOMONTH function with an offset of zero, which returns the last day of the...

[![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")](https://exceljet.net/formulas/get-work-hours-between-dates)

### [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per...

[![Excel formula: Get workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workdays%20between%20dates.png "Excel formula: Get workdays between dates")](https://exceljet.net/formulas/get-workdays-between-dates)

### [Get workdays between dates](https://exceljet.net/formulas/get-workdays-between-dates)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can optionally exclude a list of holidays supplied as dates. For example, in the screenshot shown, the formula in D6 is: =NETWORKDAYS(B6,C6...

[![Excel formula: Workdays per month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/workdays%20per%20month.png "Excel formula: Workdays per month")](https://exceljet.net/formulas/workdays-per-month)

### [Workdays per month](https://exceljet.net/formulas/workdays-per-month)

First, it's important to understand that the values in the Month column (B) are actual dates, formatted with the custom number format "mmm". For example, B4 contains January 1, 2014, but displays only "Jan" per the custom number format. The formula itself is based on the NETWORKDAYS function, which...

[![Excel formula: Working days in year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/working%20days%20in%20year.png "Excel formula: Working days in year")](https://exceljet.net/formulas/working-days-in-year)

### [Working days in year](https://exceljet.net/formulas/working-days-in-year)

NETWORKDAYS is a built-in function accepts a start date, an end date, and (optionally) a range that contains holiday dates. In the example shown, we generate the start and end date using the DATE function like this: DATE(D5,1,1) // first day of year DATE(D5,12,31) // last day of year The DATE...

[![Excel formula: Get work hours between dates and times](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20work%20hours%20between%20dates%20and%20times.png "Excel formula: Get work hours between dates and times")](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)

### [Get work hours between dates and times](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)

This formula calculates total working hours between two dates and times, that occur between a "lower" and "upper" time. In the example shown, the lower time is 9:00 AM and the upper time is 5:00 PM. These appear in the formula as the named ranges "lower" and "upper". The logic of the formula is to...

NETWORKDAYS.INTL function videos
--------------------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20due%20dates%20with%20WORKDAY_Thumb.png)](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

### [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

In this video we'll look at how to calculate due dates with the WORKDAY and WORKDAY.INTL functions. The WORKDAY function returns a date in the future or past that takes into account weekends and, optionally, holidays. You can use the WORKDAY function to calculate things like ship dates, delivery...

Related functions
-----------------

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

[![Excel NETWORKDAYS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20networkdays%20function.png "Excel NETWORKDAYS function")](https://exceljet.net/functions/networkdays-function)

### [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)

The Excel NETWORKDAYS function calculates the number of working days between two dates. NETWORKDAYS automatically excludes weekends (Saturday and Sunday) and can _optionally_ exclude a list of holidays supplied as dates. ...

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
    
*   [Workdays per month](https://exceljet.net/formulas/workdays-per-month)
    
*   [Working days in year](https://exceljet.net/formulas/working-days-in-year)
    
*   [Get work hours between dates and times](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)
    
*   [Working days left in month](https://exceljet.net/formulas/working-days-left-in-month)
    
*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    

### Videos

*   [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
    

### Functions

*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    
*   [NETWORKDAYS Function](https://exceljet.net/functions/networkdays-function)
    

### Links

*   [Microsoft NETWORKDAYS.INTL function documentation](https://support.office.com/en-us/article/networkdays-intl-function-a9b26239-4f20-46a1-9ab8-4e925bfd5e28)
    

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