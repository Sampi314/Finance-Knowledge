# Excel TODAY function | Exceljet

**Source:** https://exceljet.net/functions/today-function

---

[Skip to main content](https://exceljet.net/functions/today-function#main-content)

[](https://exceljet.net/functions/today-function#)

*   [Previous](https://exceljet.net/functions/timevalue-function)
    
*   [Next](https://exceljet.net/functions/weekday-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

TODAY Function
==============

by Dave Bruns · Updated 15 Jul 2021

Related functions 
------------------

[NOW](https://exceljet.net/functions/now-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel TODAY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")

Summary
-------

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use the [NOW function](https://exceljet.net/functions/now-function)
.

Purpose 
--------

Get the current date

Return value 
-------------

Excel date as a serial number

Syntax
------

    =TODAY()

Using the TODAY function 
-------------------------

The TODAY function returns the current date, and will continually update each time the worksheet is updated. Use F9 to force the worksheet to recalculate and update the value.

The value returned by the TODAY function is a standard [Excel date](https://exceljet.net/glossary/excel-date)
. To display the result as a date, apply a date [number format](https://exceljet.net/glossary/number-format)
. Optionally [customize the number format](https://exceljet.net/articles/custom-number-formats)
 as you like. If you want the current date _with_ a time value, use the [NOW function](https://exceljet.net/functions/now-function)
.

### Examples

The TODAY function can be used on its own, or combined with other functions. The formulas below show how the TODAY function can be used in various ways:

    =TODAY()  // current date
    =TODAY()-7  // one week in past
    =TODAY()+7  // one week in future
    =TODAY()+90  // 90 days from today
    =EDATE(TODAY(),3)  // 3 months from today
    =EDATE(TODAY(),12)  // 1 year from today
    =EDATE(TODAY(),-12)  // 1 year in the past
    =EOMONTH(TODAY(),-1)+1  // first day of current month
    =TODAY()+TIME(18,0,0)  // today at 6:00 PM
    =TODAY()+1+TIME(12,0,0)  // tomorrow at noon
    

### Static date and time

If you need a static date and time that won't change,  you can use the following shortcuts:

*   [Insert current date](https://exceljet.net/shortcuts/insert-current-date)
     - Control + ;
*   [Insert current time](https://exceljet.net/shortcuts/insert-current-time)
     - Control + Shift + :

To enter both values in a single cell, enter the date, a space, then the time.

### Formatting results

The result of TODAY is a serial number representing a valid [Excel date](https://exceljet.net/glossary/excel-date)
. You can format the value returned by TODAY using any standard date [format](https://exceljet.net/glossary/number-format)
. You can use the [TEXT function](https://exceljet.net/functions/text-function)
 to build a text message that includes the current date:

    ="The current date is "&TEXT(TODAY(),"mmm d")
    

To return a message like "The current date is May 31".

TODAY function examples
-----------------------

[![Excel formula: Invoice age and status](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/invoice_age_and_status.png "Excel formula: Invoice age and status")](https://exceljet.net/formulas/invoice-age-and-status)

### [Invoice age and status](https://exceljet.net/formulas/invoice-age-and-status)

The goal is to calculate the correct invoice status ("OK", "Paid", or "Overdue") using the following rules: If there is an "x" in the "Paid" column, return "Paid". If there is not an "x" in the "Paid" column, and if the age is less than 31 days, return "OK" If there is not an "x" in the "Paid"...

[![Excel formula: Dynamic calendar grid](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula.png "Excel formula: Dynamic calendar grid")](https://exceljet.net/formulas/dynamic-calendar-grid)

### [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will dynamically return the first day of the current month. With the layout of the grid as shown, the main problem is to calculate the date in the first cell in the calendar (B6). This...

[![Excel formula: Last n days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%207%20days.png "Excel formula: Last n days")](https://exceljet.net/formulas/last-n-days)

### [Last n days](https://exceljet.net/formulas/last-n-days)

In the image shown, the current date is August 19, 2019. Excel dates are serial numbers , so you can manipulate them with simple math operations. The TODAY function always returns the current date. Inside the AND function , the first logical test checks to see if the date in B5 is greater than or...

[![Excel formula: Last n weeks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/last%20n%20weeks_0.png "Excel formula: Last n weeks")](https://exceljet.net/formulas/last-n-weeks)

### [Last n weeks](https://exceljet.net/formulas/last-n-weeks)

In the image shown, the current date is August 24, 2019. Excel dates are serial numbers , so they can be manipulated with simple math operations. The TODAY function always returns the current date. Inside the AND function , the first logical test checks to see if the date in B5 is greater than or...

[![Excel formula: Range contains specific date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/range%20contains%20specific%20date2.png "Excel formula: Range contains specific date")](https://exceljet.net/formulas/range-contains-specific-date)

### [Range contains specific date](https://exceljet.net/formulas/range-contains-specific-date)

First, it's important to note first that Excel dates are simply large serial numbers . When we check for a date with a formula, we are looking for a specific large number, not text . This formula is a basic example of using the COUNTIFS function with just one condition. The named range dates is...

[![Excel formula: Data validation date in specific year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20date%20in%20specific%20year.png "Excel formula: Data validation date in specific year")](https://exceljet.net/formulas/data-validation-date-in-specific-year)

### [Data validation date in specific year](https://exceljet.net/formulas/data-validation-date-in-specific-year)

Data validation rules are triggered when a user adds or changes a cell value. This custom validation formula simply checks the year of any date against a hard-coded year value using the YEAR function. When a user enters a value, the YEAR function extracts and compares the year to 2016: =YEAR(C5)=...

[![Excel formula: Calculate days remaining](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20days%20remaining.png "Excel formula: Calculate days remaining")](https://exceljet.net/formulas/calculate-days-remaining)

### [Calculate days remaining](https://exceljet.net/formulas/calculate-days-remaining)

Dates in Excel are just serial numbers that begin on January 1, 1900. If you enter 1/1/1900 in Excel, and format the result with the "General" number format , you'll see the number 1. This means that you can easily calculate the days between two dates by subtracting the earlier date from the later...

[![Excel formula: Get days before a date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_days_before_a_date.png "Excel formula: Get days before a date")](https://exceljet.net/formulas/get-days-before-a-date)

### [Get days before a date](https://exceljet.net/formulas/get-days-before-a-date)

In Excel, dates are simply serial numbers. In the standard date system for windows, based on the year 1900, where January 1, 1900 is the number 1. Dates are valid through 9999, which is serial number 2,958,465. This means that January 1, 2050 is the serial number 54,789. In the example, the date is...

[![Excel formula: Calculate days open](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/calculate%20days%20open.png "Excel formula: Calculate days open")](https://exceljet.net/formulas/calculate-days-open)

### [Calculate days open](https://exceljet.net/formulas/calculate-days-open)

In this example, the goal is to calculate the number of days a ticket/case/issue has been open. We start counting on the date a ticket was opened and stop counting on the date a ticket was closed. If there is no closed date, the ticket is still open. Because dates in Excel are just serial numbers...

[![Excel formula: Conditional formatting date past due](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/conditional%20formatting%20date%20past%20due.png "Excel formula: Conditional formatting date past due")](https://exceljet.net/formulas/conditional-formatting-date-past-due)

### [Conditional formatting date past due](https://exceljet.net/formulas/conditional-formatting-date-past-due)

In this example, we want to apply three different colors, depending on how much the original date varies from the current date: Green if the variance is less than 3 days Yellow if the variance is between 3 and 10 days Red if the variance is greater than 10 days For each rule, we calculate a...

[![Excel formula: Dynamic calendar formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Dynamic%20calendar%20formula_0.png "Excel formula: Dynamic calendar formula")](https://exceljet.net/formulas/dynamic-calendar-formula)

### [Dynamic calendar formula](https://exceljet.net/formulas/dynamic-calendar-formula)

Note: This example assumes the start date will be provided as the first of the month. See below for a formula that will automatically return the first day of the current month. In this example, the goal is to generate a dynamic calendar for any given month, based on a start date entered in cell J6...

[![Excel formula: Happy birthday message](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/happy%20birthday%20message.png "Excel formula: Happy birthday message")](https://exceljet.net/formulas/happy-birthday-message)

### [Happy birthday message](https://exceljet.net/formulas/happy-birthday-message)

In this example, the goal is to display a Happy Birthday message when a birthday in a given cell matches the current date. The core of the problem is to compare the given birthday to the current date while ignoring the year. There are two main ways to approach the problem. The first way is to use...

[![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")](https://exceljet.net/formulas/get-days-between-dates)

### [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)

Dates in Excel are serial numbers that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this: =C6-B6 =...

### [Display the current date](https://exceljet.net/formulas/display-the-current-date)

The TODAY function takes no arguments; it is entered with empty parentheses. When you enter the TODAY function in a cell, it will display the current date. Each time the worksheet is recalculated or opened, the date will be updated. The TODAY function only inserts the date, time is not included. If...

[![Excel formula: Working days left in month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/working%20days%20left%20in%20month.png "Excel formula: Working days left in month")](https://exceljet.net/formulas/working-days-left-in-month)

### [Working days left in month](https://exceljet.net/formulas/working-days-left-in-month)

NETWORKDAYS is a built in function accepts a start date, end date, and (optionally) a range that contains holiday dates. In this case, the start date is Jan 10, 2018, provided as cell B5. The end date is calculated using the EOMONTH function with an offset of zero, which returns the last day of the...

TODAY function videos
---------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20function%20arguments-thumb.png)](https://exceljet.net/videos/how-to-use-function-arguments)

### [How to use function arguments](https://exceljet.net/videos/how-to-use-function-arguments)

You've probably noticed that functions use parentheses, and inside those parentheses are certain inputs. These inputs have a special name: arguments. Let's look at some examples. Arguments can be required or optional. Some functions take three or more arguments, and some functions don't take any...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20step%20through%20complex%20formulas%20using%20evaluate-thumb.png)](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)

### [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)

Excel has a handy feature called Evaluate Formula, which solves a formula one step at a time. Each time you click the Evaluate button, Excel will solve the underlined part of the formula and show you the result. Here's the same worksheet we looked at in a previous video when we talked about...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20check%20and%20debug%20a%20formula%20with%20F9.png)](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

### [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

One thing you'll frequently do in Excel is check or debug formulas. In this video, we'll look at how to use the F9 key to quickly break a formula down into pieces that you can understand. Here we have a simple list of names. In addition to names, we have a column for birthdate, a column for age,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20display%20current%20date%20and%20time-thumb.png)](https://exceljet.net/videos/how-to-display-current-date-and-time)

### [How to display current date and time](https://exceljet.net/videos/how-to-display-current-date-and-time)

In this video we look at several ways to handle current dates and times. You may often want to enter a current date and time into a worksheet. A simple way to do this is to enter a time or date stamp. You can do this using keyboard shortcuts. Control semicolon enters the current date. Control-Shift...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20expiration%20dates.png)](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)

### [How to calculate and highlight expiration dates](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)

In this video we'll look at how to calculate and highlight expiration dates. Let's say your company has started a membership program of some kind and your boss just sent you a set of data. She's given you a list of 1,000 people that have renewed a membership in the last year or so, and she's...

Related functions
-----------------

[![Excel NOW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20now%20function.png "Excel NOW function")](https://exceljet.net/functions/now-function)

### [NOW Function](https://exceljet.net/functions/now-function)

The Excel NOW function returns the current date and time, updated continuously when a worksheet is changed or opened. The NOW function takes no arguments. You can format the value returned by NOW as a date, or as a date with time by applying a [number format](https://exceljet.net/glossary/number-format)
...

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

*   [Display the current date](https://exceljet.net/formulas/display-the-current-date)
    
*   [Range contains specific date](https://exceljet.net/formulas/range-contains-specific-date)
    
*   [Filter on dates expiring soon](https://exceljet.net/formulas/filter-on-dates-expiring-soon)
    
*   [Working days left in month](https://exceljet.net/formulas/working-days-left-in-month)
    
*   [Add days to date](https://exceljet.net/formulas/add-days-to-date)
    
*   [Invoice age and status](https://exceljet.net/formulas/invoice-age-and-status)
    
*   [Data validation allow weekday only](https://exceljet.net/formulas/data-validation-allow-weekday-only)
    
*   [Last n weeks](https://exceljet.net/formulas/last-n-weeks)
    
*   [Last updated date stamp](https://exceljet.net/formulas/last-updated-date-stamp)
    
*   [Dynamic calendar grid](https://exceljet.net/formulas/dynamic-calendar-grid)
    

### Videos

*   [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
    
*   [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)
    
*   [How to display current date and time](https://exceljet.net/videos/how-to-display-current-date-and-time)
    
*   [How to use function arguments](https://exceljet.net/videos/how-to-use-function-arguments)
    
*   [How to calculate and highlight expiration dates](https://exceljet.net/videos/how-to-calculate-and-highlight-expiration-dates)
    

### Functions

*   [NOW Function](https://exceljet.net/functions/now-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Links

*   [Microsoft TODAY function documentation](https://support.office.com/en-us/article/today-function-5eb3078d-a82c-4736-8930-2f51a028fdd9)
    

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