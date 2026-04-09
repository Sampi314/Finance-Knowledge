# Add days to date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-days-to-date

---

[Skip to main content](https://exceljet.net/formulas/add-days-to-date#main-content)

[](https://exceljet.net/formulas/add-days-to-date#)

*   [Previous](https://exceljet.net/formulas/add-days-exclude-certain-days-of-week)
    
*   [Next](https://exceljet.net/formulas/add-decimal-hours-to-time)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Add days to date
================

by Dave Bruns · Updated 29 May 2024

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

[EDATE](https://exceljet.net/functions/edate-function)

[WORKDAY](https://exceljet.net/functions/workday-function)

![Excel formula: Add days to date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add_days_to_date.png "Excel formula: Add days to date")

Summary
-------

To add days to a date in Excel you can use simple addition. In the example shown, the formula in cell E5 is:

    =B5+C5

As the formula is copied down, the days in column C are added to the date in column B. The dates in column E show the result of this operation.

Generic formula
---------------

    =date+days

Explanation 
------------

In this example, the goal is to add days to a date. This is a frequent task in Excel when you need to calculate a new date by adding a specified number of days to an existing date.  Here are some examples of situations where this might be useful:

*   Calculate a due date by adding a given number of days to a start date.
*   Determine an expiration date by adding days to the manufacturing date.
*   Schedule a follow-up appointment by adding days to the initial appointment date.
*   Calculate the end date for a contract or legal agreement.

The article below provides several examples of how to set up a formula like this in Excel and notes some potential issues you may encounter.

### About Excel dates

In Excel, [dates are stored as serial numbers](https://exceljet.net/glossary/excel-date)
 that begin with 1. For example, January 1, 1900, is the number 1, January 2, 1900, is 2, and so on. As I write this, the current date is May 28, 2024, which is stored as the serial number 45440. Because Excel dates are just numbers, you can perform arithmetic operations on dates, such as adding or subtracting days to get a new date.

### Simple example

In the simplest case, you can hardcode the number of days directly into a formula. For example, with the date January 1, 2024, in cell A1, you can use a formula like this to add 14 days to the date:

    =A1+14 // returns 15-Jan-2024

The result is January 15, 2024, which is the date 14 days after January 1, 2024. The formulas below the result of adding a different number of days to the date January 1, 2024, in cell A1:

    =A1+1 // returns 02-Jan-2024
    =A1+2 // returns 03-Jan-2024
    =A1+3 // returns 04-Jan-2024
    =A1+7 // returns 08-Jan-2024
    =A1+14 // returns 15-Jan-2024
    =A1+21 // returns 22-Jan-2024

Remember that "under the hood" Excel performs this arithmetic with large serial numbers. Because January 1, 2024, is stored as the number 45292, the actual math operation looks like this:

    =45292+1 // returns 45293
    =45292+2 // returns 45294
    =45292+3 // returns 45295
    =45292+7 // returns 45299
    =45292+14 // returns 45306
    =45292+21 // returns 45313

Excel then displays the large numbers as dates using a date [number format](https://exceljet.net/glossary/number-format)
.

### Example with a cell reference

Of course, you can easily set up a formula to use a cell reference that contains the days to add. In the worksheet shown, we are not hardcoding days into the formula. Instead, we are picking up the days entered in column C with a cell reference. The formula in cell E5 looks like this:

    =B5+C5

![Example - add days to date with a cell reference](https://exceljet.net/sites/default/files/images/formulas/inline/add_days_to_date_with_a_cell_reference.png "Example - add days to date with a cell reference")

As the formula is copied down, the days in column C are added to the dates in column B. The resulting dates can be seen in column E.

_Note: the dates in columns B and E are formatted with the [custom date format](https://exceljet.net/articles/custom-number-formats)
 "ddd, d-mmm-yyyy" to show the day of the week (e.g. Mon, Tue, etc.) along with the date._

### Subtracting days from a date

As you might guess, you can subtract days from a date as well. To subtract 7 days from the date 1-Jan-2024 in cell A1, you can use a formula like this:

    =A1-7

The result is Mon, 25-Dec-2023. If you use cell references for days, you will find it easier to keep the original formula based on addition (+) and enter the days as a negative number. You can see the result in the worksheet below, where the formula in cell E5 is:

    =B5+C5

![Example - subtract days from date with a cell reference](https://exceljet.net/sites/default/files/images/formulas/inline/subtract_days_from_date_with_a_cell_reference.png "Example - subtract days from date with a cell reference")

The original formula is the same, but the negative day numbers "subtract" days from the date in column B. This approach is more flexible since you can enter negative or positive days.

### Days from today

If you want to add days to the current date, you can use the [TODAY function](https://exceljet.net/functions/today-function)
. For example, to add 10 days, you can use this formula:

    =TODAY()+10

This formula will return a date 10 days from today. Note that this formula will continue to calculate on an ongoing basis because the TODAY function will always return the current date.

### Add workdays to date

There are many situations in business where you need to add a specific number of business days to a date, automatically skipping non-working days like weekends and holidays. In these scenarios, you can add days with the [WORKDAY function](https://exceljet.net/functions/workday-function)
 or its more flexible sibling [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
. For example, to add 5 business days to a date while excluding Saturdays and Sundays, you can use a formula like this:

    =WORKDAY(A1,5) // add 5 working days

For a detailed explanation of using the WORKDAY function like this, including the option to skip holidays, see [Add business days to a date](https://exceljet.net/formulas/add-business-days-to-date)
.

### Same date next month

If you want to add days to date and end up on the same day next month (or in 6 months) you will have trouble calculating how many days you need to add. Instead, you should use a different approach based on the [EDATE function](https://exceljet.net/functions/edate-function)
. With a valid date in cell A1, you can use EDATE to return a date 1 month, 3 months, and 6 months from the date like this:

    =EDATE(A1,1) // same day in 1 month
    =EDATE(A1,3) // same day in 3 months
    =EDATE(A1,6) // same day in 6 months

The EDATE function can travel forward or backward in time based on the number of months provided. The [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 works in a similar way to EDATE but will always return a date at the _end of a month_.

### Potential issues

Although adding dates in Excel is simple, there are several potential issues you may encounter.

*   Date Formatting: Make sure cells that contain dates are formatted as dates. If not, Excel might display the result as a serial number. To format a cell as a date:
    *   Use the keyboard shortcut Control + 1 to open "Format Cells".
    *   Select "Date" from the list of formats.
    *   Choose the desired date format and click "OK".
*   #VALUE error: if your formula results in a #VALUE! error, it may be that Excel does not correctly understand the date you are adding days to. If Excel sees a date in cell A1 as text, a formula like =A1+1 will return #VALUE! To fix this problem, [take steps to make Excel read the dates correctly](https://exceljet.net/formulas/convert-text-to-date)
    .
*   Negative result: If you end up with a negative date value (i.e. a negative serial number) Excel will not display the number as a date. Instead, you will see a string of hash characters like #######. To fix this problem, adjust the formula or the dates to return a positive result.
*   Excel Date Limitations: Excel handles dates from January 1, 1900, to December 31, 9999. Adding days to a date that results in a date outside this range will cause Excel to display a string of hash characters like #######.

Related formulas
----------------

[![Excel formula: Add business days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_business_days_to_date.png "Excel formula: Add business days to date")](https://exceljet.net/formulas/add-business-days-to-date)

### [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)

In this example, the goal is to calculate a workday n days in the future while excluding weekends and optionally holidays. For convenience, start (B5), days (B8), and holidays (B11:B13) are named ranges . The dates in columns D and E are dynamically generated based on the start date in B5...

[![Excel formula: Add years to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_years_to_date.png "Excel formula: Add years to date")](https://exceljet.net/formulas/add-years-to-date)

### [Add years to date](https://exceljet.net/formulas/add-years-to-date)

Ever needed to calculate someone's retirement date? Or figure out when a 30-year mortgage will end? Or maybe you're setting a contract expiration date? In each case, you need a way to add years to a date. Here's something that might surprise you: most Excel users tackle this problem with a formula...

[![Excel formula: Add months to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_months_to_date.png "Excel formula: Add months to date")](https://exceljet.net/formulas/add-months-to-date)

### [Add months to date](https://exceljet.net/formulas/add-months-to-date)

In this example, the goal is to add a given number of months to a date. If the number of months is positive, the date should move forward. If the number of months is negative, the date should move backward. The standard solution for this problem in Excel is to use the EDATE function although in...

Related functions
-----------------

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel WORKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday%20function.png "Excel WORKDAY function")](https://exceljet.net/functions/workday-function)

### [WORKDAY Function](https://exceljet.net/functions/workday-function)

The Excel WORKDAY function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. You can use the WORKDAY function to calculate things like start dates, delivery dates, and completion dates...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_date_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)

### [How to use date formatting in Excel](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)

In this lesson we'll take a look at the Date format. The Date format is flexible and can display the same date in many different ways. Let's take a look. Here we have a set of dates in column B of our table. Let's start off by copying these dates to all columns. Let's look first at the Short Date...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add business days to date](https://exceljet.net/formulas/add-business-days-to-date)
    
*   [Add years to date](https://exceljet.net/formulas/add-years-to-date)
    
*   [Add months to date](https://exceljet.net/formulas/add-months-to-date)
    

### Functions

*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [WORKDAY Function](https://exceljet.net/functions/workday-function)
    

### Videos

*   [How to use date formatting in Excel](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)
    

### Training

*   [Core Excel](https://exceljet.net/training/core-excel)
    

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