# Last n weeks - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/last-n-weeks

---

[Skip to main content](https://exceljet.net/formulas/last-n-weeks#main-content)

[](https://exceljet.net/formulas/last-n-weeks#)

*   [Previous](https://exceljet.net/formulas/last-n-months)
    
*   [Next](https://exceljet.net/formulas/last-updated-date-stamp)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Last n weeks
============

by Dave Bruns · Updated 25 Aug 2019

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

[TODAY](https://exceljet.net/functions/today-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

![Excel formula: Last n weeks](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/last%20n%20weeks_0.png "Excel formula: Last n weeks")

Summary
-------

To check if a date is within the last n weeks of today's date, you can use a formula based on the AND, TODAY, and WEEKDAY functions. In the example shown, we are testing for dates in the last 2 weeks. The formula in C5, copied down, is:

    =AND(B5>=TODAY()-WEEKDAY(TODAY(),3)-14,B5<TODAY()-WEEKDAY(TODAY(),3))
    

The result is TRUE for any date in the last complete 2 week period, where weeks begin on Monday. The TODAY function will return the current date on an ongoing basis, so this formula can be used create reports to show a rolling 4 weeks, rolling 6 weeks, etc.

Generic formula
---------------

    =AND(A1>=TODAY()-WEEKDAY(TODAY(),3)-(n*7),A1<TODAY()-WEEKDAY(TODAY(),3))

Explanation 
------------

In the image shown, the current date is August 24, 2019.

[Excel dates are serial numbers](https://exceljet.net/glossary/excel-date)
, so they can be manipulated with simple math operations. The [TODAY function](https://exceljet.net/functions/today-function)
 always returns the current date.

Inside the [AND function](https://exceljet.net/functions/and-function)
, the first logical test checks to see if the date in B5 is greater than or equal to the Monday two weeks previous.

    B5>=TODAY()-WEEKDAY(TODAY(),3)-14
    

This is based on a [formula described here](https://exceljet.net/formulas/get-monday-of-the-week)
 which gets the Monday of the current week. Once we have that date, we subtract 14 days to get the Monday two weeks prior.

The second logical test simply checks if the date is less than Monday in the current week.

    B5<TODAY()-WEEKDAY(TODAY(),3)
    

when both results are TRUE, the AND function will return TRUE. If either result is FALSE, the AND function will return FALSE.

### Last 6 weeks

The number of weeks is configurable by using an (n\*7) value, where n is number of weeks. To test for the last 6 weeks, you can adjust the formula like this:

    =AND(B5>=TODAY()-WEEKDAY(TODAY(),3)-42,B5<TODAY()-WEEKDAY(TODAY(),3))
    

### Include current week

To include the current week, you can use only the first logical test:

    B5>=TODAY()-WEEKDAY(TODAY(),3)-14
    

Note: this will include future dates (if any) that appear in source data.

Related formulas
----------------

[![Excel formula: Last n days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%207%20days.png "Excel formula: Last n days")](https://exceljet.net/formulas/last-n-days)

### [Last n days](https://exceljet.net/formulas/last-n-days)

In the image shown, the current date is August 19, 2019. Excel dates are serial numbers , so you can manipulate them with simple math operations. The TODAY function always returns the current date. Inside the AND function , the first logical test checks to see if the date in B5 is greater than or...

[![Excel formula: Last n months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20n%20months.png "Excel formula: Last n months")](https://exceljet.net/formulas/last-n-months)

### [Last n months](https://exceljet.net/formulas/last-n-months)

In this example, the goal is to create a formula that will return TRUE if a date is in the last complete 6 month period, starting in the previous month. This means the date must fall between a calculated start date and end date, which requires two logical tests. The formula uses the AND function to...

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Last n days](https://exceljet.net/formulas/last-n-days)
    
*   [Last n months](https://exceljet.net/formulas/last-n-months)
    

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    

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