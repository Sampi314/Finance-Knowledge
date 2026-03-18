# Get days, hours, and minutes between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates

---

[Skip to main content](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates#main-content)

[](https://exceljet.net/formulas/get-days-hours-and-minutes-between-dates#)

*   [Previous](https://exceljet.net/formulas/get-days-between-dates-ignoring-years)
    
*   [Next](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get days, hours, and minutes between dates
==========================================

by Dave Bruns · Updated 8 Nov 2019

Related functions 
------------------

[INT](https://exceljet.net/functions/int-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Get days, hours, and minutes between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20days%20hours%20and%20minutes%20between%20dates2.png "Excel formula: Get days, hours, and minutes between dates")

Summary
-------

To calculate and display the days, hours, and minutes between two dates, you can use the [TEXT function](https://exceljet.net/functions/text-function)
 with a little help from the [INT function](https://exceljet.net/functions/int-function)
. In the example shown, the formula in D5 is:

    =INT(C5-B5)&" days "&TEXT(C5-B5,"h"" hrs ""m"" mins """)
    

Generic formula
---------------

    =INT(end-start)&" days "&TEXT(end-start,"h"" hrs ""m"" mins """)
    

Explanation 
------------

Most of the work in this formula is done by the TEXT function, which applies a [custom number format](https://exceljet.net/articles/custom-number-formats)
 for hours and minutes to a value created by subtracting the start date from the end date.

    TEXT(C5-B5,"h"" hrs ""m"" mins """)
    

This is an example of embedding text into a custom number format, and this text must be surrounded by an extra pair of double quotes. Without the extra double quotes, the custom text format looks like this:

    h "hrs" m "min"
    

The value for days is calculated with the INT function, which simply returns the integer portion of the end date minus the start date:

    INT(C5-B5) // get day value
    

_Note: Although you can use "d" in a custom number format for days, the value will reset to zero when days is greater than 31._

### Include seconds

To include seconds, you can extend the custom number format like this:

    =INT(C5-B5)&" days "&TEXT(C5-B5,"h"" hrs ""m"" mins ""s"" secs""")
    

### Total days, hours, and minutes between dates

To get the total days, hours, and minutes between a set of start and end dates, you can adapt the formula using SUMPRODUCT like this:

    =INT(SUMPRODUCT(ends-starts))&" days "&TEXT(SUMPRODUCT(ends-starts),"h"" hrs ""m"" mins """)
    

where "ends" represents the range of end dates, and "starts" represents the range of start dates. In the example shown, D11 contains this formula:

    =INT(SUMPRODUCT(C5:C9-B5:B9))&" days "&TEXT(SUMPRODUCT(C5:C9-B5:B9),"h"" hrs ""m"" mins """)
    

Related formulas
----------------

[![Excel formula: Get days, months, and years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20months%20and%20years%20between%20dates.png "Excel formula: Get days, months, and years between dates")](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

### [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)

In this example, the goal is to output the time between a start date and an end date as a text string that lists years, months, and days separately. For example, given a start date of 1-Jan-2018 and an end date of 1-Jul-2018, the result should be a string like this: "1 years, 6 months, 0 days"...

[![Excel formula: Calculate years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate_years_between_dates.png "Excel formula: Calculate years between dates")](https://exceljet.net/formulas/calculate-years-between-dates)

### [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)

In this example, the goal is to calculate the number of years between a start date in column B and an end date in column C. An easy way to solve this problem is to use the YEARFRAC function, which returns the number of years between any two dates as a decimal number. YEARFRAC function The YEARFRAC...

[![Excel formula: Get months between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_months_between_dates.png "Excel formula: Get months between dates")](https://exceljet.net/formulas/get-months-between-dates)

### [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)

In this example, the goal is to calculate the number of months between two valid Excel dates . This is a curiously tricky problem in Excel because the number of days in a month varies, and the rules about how a whole month might be calculated are not obvious. In addition, there is not a modern...

Related functions
-----------------

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get days, months, and years between dates](https://exceljet.net/formulas/get-days-months-and-years-between-dates)
    
*   [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)
    
*   [Get months between dates](https://exceljet.net/formulas/get-months-between-dates)
    

### Functions

*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

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