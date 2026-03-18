# Sequence of months - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sequence-of-months

---

[Skip to main content](https://exceljet.net/formulas/sequence-of-months#main-content)

[](https://exceljet.net/formulas/sequence-of-months#)

*   [Previous](https://exceljet.net/formulas/sequence-of-leap-years)
    
*   [Next](https://exceljet.net/formulas/sequence-of-times)
    

[Date series](https://exceljet.net/formulas#Date-series)

Sequence of months
==================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[EDATE](https://exceljet.net/functions/edate-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")

Summary
-------

To generate a series of dates incremented by month, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 together with the [EDATE function](https://exceljet.net/functions/edate-function)
. In the example shown, the formula in D5 is:

    =EDATE(B5,SEQUENCE(12,1,0))

The result is a series of 12 dates, incremented by one month, beginning on June 1, 2023.

_Note: in the generic version of the formula above, 'n' is the number of dates you wish to generate. In this example, n is 12, since we want 12 dates._

Generic formula
---------------

    =EDATE(A1,SEQUENCE(n,1,0))

Explanation 
------------

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 inside the [EDATE function](https://exceljet.net/functions/edate-function)
 like this:

    =EDATE(B5,SEQUENCE(12,1,0))

The result is a series of 12 dates, incremented by one month, beginning on June 1, 2023, and ending on May 1, 2024. At a high level, this formula uses the EDATE function to return 12 dates one month apart, and it uses the SEQUENCE function to create the numeric array needed to perform this operation in one step.

### EDATE function

The EDATE function moves forward or backward in time in one-month increments from a given start date. The generic syntax for EDATE looks like this:

    =EDATE(start_date,months)

Inside EDATE, _start\_date_ is any valid Excel date, and _months_ is the number of months to add or subtract from _start\_date_. For example, with the date June 1, 2023, in cell B5, EDATE works like this:

    =EDATE(B5,-2) // returns April 1, 2023
    =EDATE(B5,-1) // returns May 1, 2023
    =EDATE(B5,0) // returns June 1, 2023
    =EDATE(B5,1) // returns July 1, 2023
    =EDATE(B5,2) // returns August 1, 2023
    =EDATE(B5,3) // returns September 1, 2023

The challenge in this problem is that we want to return 12 dates at the same time. One way to accomplish this is to use the SEQUENCE function to generate a numeric array we can plug into EDATE.

For more details on EDATE, see: [How to use the EDATE function](https://exceljet.net/functions/edate-function)
.

### SEQUENCE function

The SEQUENCE function is designed to generate numeric sequences in rows and/or columns. The generic syntax for SEQUENCE looks like this:

    =SEQUENCE(rows,[columns],[start],[step])

In the example shown, we use SEQUENCE to generate 12 sequential numbers like this:

    SEQUENCE(12,1,0)

Here, _rows_ is 12, _columns_ is 1, and _start_ is 0. The reason we want this array to begin with zero is that we want to include the start date in the final result. With this configuration, SEQUENCE will return an array like this:

    {0;1;2;3;4;5;6;7;8;9;10;11}

This array is then provided to the EDATE function as the _months_ argument, as described below.

For more details on SEQUENCE, see [How to use the SEQUENCE function](https://exceljet.net/functions/sequence-function)
.

### EDATE + SEQUENCE

The array created by SEQUENCE is returned as the _months_ argument inside the EDATE function:

    =EDATE(B5,{0;1;2;3;4;5;6;7;8;9;10;11})

EDATE then returns 12 dates, beginning with the date in B5. Because Excel dates are stored [as large serial numbers](https://exceljet.net/glossary/excel-date)
, the result is an array like this:

    {45078;45108;45139;45170;45200;45231;45261;45292;45323;45352;45383;45413}
    

This array lands in cell D5 and spills into the range D5:D16. When this range is formatted with date formatting, Excel will display 12 dates beginning on June 1, 2023, and ending on May 1, 2024.

### End of month

To generate a series of "end of month" dates, you can use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 instead of EDATE like this:

    =EOMONTH(B5,SEQUENCE(12,1,0))
    

EOMONTH works just like EDATE, except it always returns a date at the end of the month, regardless of the date provided.

### Month names only

To generate a list of month names (instead of actual dates), you can wrap the formula above in the [TEXT function](https://exceljet.net/functions/text-function)
:

    =TEXT(EDATE(B5,SEQUENCE(12,1,0)),"mmmm")
    

The TEXT function will use the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mmmm" to convert each date into a text string equal to the month name. The format "mmmm" tells the TEXT function to extract the full month name from a given date.

### Older versions of Excel

In older versions of Excel, there is no SEQUENCE function. This means we don't have an easy way to calculate and return 12 dates all at once. However, you can still generate a series of dates by month with a more manual approach like this:

![Dates by month in legacy Excel](https://exceljet.net/sites/default/files/images/formulas/inline/sequence_of_months_legacy.png "Dates by month in legacy Excel")

Here, the start date is hardcoded into cell B5. The formula in cell B6, copied down, is:

    =EDATE(B5,1)

This formula uses the EDATE function to add one month to the date in cell B5. As the formula is copied down, it returns a date one month after the date in the previous row.

Related formulas
----------------

[![Excel formula: Sequence of days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_days.png "Excel formula: Sequence of days")](https://exceljet.net/formulas/sequence-of-days)

### [Sequence of days](https://exceljet.net/formulas/sequence-of-days)

The goal is to generate a series of sequential dates with a formula. In the current version of Excel, the easiest method is to use the SEQUENCE function. SEQUENCE can return all dates at the same time into a range on the worksheet. In older versions of Excel without the SEQUENCE function, you can...

[![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")](https://exceljet.net/formulas/sequence-of-workdays)

### [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE...

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sequence of days](https://exceljet.net/formulas/sequence-of-days)
    
*   [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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