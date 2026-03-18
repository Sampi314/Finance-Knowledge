# Add months to date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-months-to-date

---

[Skip to main content](https://exceljet.net/formulas/add-months-to-date#main-content)

[](https://exceljet.net/formulas/add-months-to-date#)

*   [Previous](https://exceljet.net/formulas/add-decimal-minutes-to-time)
    
*   [Next](https://exceljet.net/formulas/add-workdays-to-date-custom-workweek)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Add months to date
==================

by Dave Bruns · Updated 4 Jun 2024

Related functions 
------------------

[EDATE](https://exceljet.net/functions/edate-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: Add months to date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add_months_to_date.png "Excel formula: Add months to date")

Summary
-------

To add a given number of years to a date, you can use the [EDATE function](https://exceljet.net/functions/edate-function)
. In the workbook shown, the formula in F5 is:

    =EDATE(date,D5)

As the formula is copied down, it adds the months in column B to the date in cell B5. The result in each row is a new date as shown.

Generic formula
---------------

    =EDATE(date,months)

Explanation 
------------

In this example, the goal is to add a given number of months to a date. If the number of months is positive, the date should move forward. If the number of months is negative, the date should move backward. The standard solution for this problem in Excel is to use the EDATE function although in certain cases you may want to use the EOMONTH function instead. Both approaches are explained below.

### The EDATE function

The [EDATE function](https://exceljet.net/functions/edate-function)
 can add or subtract whole months from a date. You can use EDATE to calculate expiration dates, contract dates, due dates, anniversary dates, and other dates in the future or past. The generic syntax for EDATE looks like this:

    =EDATE(start_date,months)

EDATE takes two arguments as follows:

*   _start\_date_ - The starting date, which must be a valid Excel date.
*   months - The number of months before or after _start\_date_. A positive number will move the date forward and a negative number will move the date backward. 

The EDATE function is fully automatic. Simply supply a valid date and a number for _months_ and EDATE will return a new date. For example, if we give EDATE the date June 1, 2024, and the number 3 for months, the result is September 1, 2024:

    =EDATE("1-Jun-2024",3) // returns "1-Sep-2024"

In the worksheet shown, we have a start date in cell B5 and a various number of months in column D. The formula in cell F5 looks like this:

    =EDATE($B$5,D5)

Note that $B$5 is an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to lock this cell as the formula is copied down:

![Adding months to a date with the EDATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/add_months_to_date_example.png "Adding months to a date with the EDATE function")

As the formula is copied down, it adds the months in column B to the start date in cell B5. The result in each row is a new date as shown. Notice that the positive month numbers in D5:D10 move the date forward in time and the negative month numbers in D11:D16 move the date back in time.  If we change the start date in B5 to September 12, 2024, we get a new set of dates:

![The same worksheet after changing the start date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/add_months_to_date_new_date_example.png "The same worksheet after changing the start date")

Note the output from EDATE keeps the day (12) from the start date.

### The EOMONTH function

In specific situations, you may want to add months to a date and end up on the last day of the month, regardless of the starting day. In that case, you can switch from the EDATE function to the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
. EOMONTH works just like EDATE, so it is a drop-in replacement. In the worksheet below, the formula in cell B5 is:

    =EOMONTH($B$5,D5)

![Adding months to a date with the EOMONTH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/add_months_to_date_eomonth_example.png "Adding months to a date with the EOMONTH function")

The result from EOMONTH is the same as EDATE except that all dates are at the _end of the month_. The day in the start date is not used.

### Adding years

To add years to a date, you can multiply by 12 inside EDATE like this:

    =EDATE(A1,12*10) // 10 years
    =EDATE(A1,12*50) // 50 years
    
    

Excel will solve the multiplication first, then feed the result to EDATE as the _months_ argument. For a more detailed discussion of this topic, [see this page](https://exceljet.net/formulas/add-years-to-date)
.

Related formulas
----------------

[![Excel formula: Add years to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_years_to_date.png "Excel formula: Add years to date")](https://exceljet.net/formulas/add-years-to-date)

### [Add years to date](https://exceljet.net/formulas/add-years-to-date)

Ever needed to calculate someone's retirement date? Or figure out when a 30-year mortgage will end? Or maybe you're setting a contract expiration date? In each case, you need a way to add years to a date. Here's something that might surprise you: most Excel users tackle this problem with a formula...

[![Excel formula: Add days to date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_days_to_date.png "Excel formula: Add days to date")](https://exceljet.net/formulas/add-days-to-date)

### [Add days to date](https://exceljet.net/formulas/add-days-to-date)

In this example, the goal is to add days to a date. This is a frequent task in Excel when you need to calculate a new date by adding a specified number of days to an existing date. Here are some examples of situations where this might be useful: Calculate a due date by adding a given number of days...

Related functions
-----------------

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add years to date](https://exceljet.net/formulas/add-years-to-date)
    
*   [Add days to date](https://exceljet.net/formulas/add-days-to-date)
    

### Functions

*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

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