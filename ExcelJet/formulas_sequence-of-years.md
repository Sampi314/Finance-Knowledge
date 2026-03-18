# Sequence of years - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sequence-of-years

---

[Skip to main content](https://exceljet.net/formulas/sequence-of-years#main-content)

[](https://exceljet.net/formulas/sequence-of-years#)

*   [Previous](https://exceljet.net/formulas/sequence-of-workdays)
    
*   [Next](https://exceljet.net/formulas/10-most-common-text-values)
    

[Date series](https://exceljet.net/formulas#Date-series)

Sequence of years
=================

by Dave Bruns · Updated 26 Aug 2023

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[DATE](https://exceljet.net/functions/date-function)

[YEAR](https://exceljet.net/functions/year-function)

[MONTH](https://exceljet.net/functions/month-function)

[DAY](https://exceljet.net/functions/day-function)

![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")

Summary
-------

To generate a series of dates by year, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 together with the [DATE](https://exceljet.net/functions/date-function)
, [YEAR](https://exceljet.net/functions/year-function)
, [MONTH](https://exceljet.net/functions/month-function)
, and [DAY](https://exceljet.net/functions/day-function)
 functions. In the example shown, the formula in D5 is:

    =DATE(SEQUENCE(12,1,YEAR(B5)),MONTH(B5),DAY(B5))
    

The result is a series of 12 dates, incremented by one year, beginning with May 1, 2019.

Generic formula
---------------

    =DATE(SEQUENCE(12,1,YEAR(A1)),MONTH(B5),DAY(A1))

Explanation 
------------

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach. Both methods are described below.

### SEQUENCE function

The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 generates numeric arrays. For example, to generate the numbers 1 through 10 you can use SEQUENCE like this:

    =SEQUENCE(10) // returns {1;2;3;4;5;6;7;8;9;10}

To solve this problem, we can use SEQUENCE to generate the years we need (2019-2030), then hand the years off to the DATE function along with the correct values for month and day. In the worksheet shown, the formula in D5 is:

    =DATE(SEQUENCE(12,1,YEAR(B5)),MONTH(B5),DAY(B5))

Working from the inside out, the year, month, and day values from the date in B5 are first extracted with the YEAR, MONTH, and DAY functions. With the date May 1, 2019, in cell B5 YEAR returns 2019, MONTH returns 5, and DAY returns 1. The formula now looks like this:

    =DATE(SEQUENCE(12,1,2019),5,1)

Next, the SEQUENCE function is evaluated with the following inputs:

*   _rows_ - 12
*   _columns_ - 1
*   _start_ - 2019

The result from SEQUENCE is an array with 12 years like this:

    {2019;2020;2021;2022;2023;2024;2025;2026;2027;2028;2029;2030}
    

This array is returned as the _year_ argument inside the DATE function:

    =DATE({2019;2020;2021;2022;2023;2024;2025;2026;2027;2028;2029;2030},5,1)

Because we are giving the DATE function 12 values for the year, we are essentially asking for 12 separate dates, through a process known as "[lifting](https://exceljet.net/glossary/lifting)
". The _month_ is provided as 5 and _day_ is provided as 1. The result is an array of 12 dates in serial number format like this:

    {43586;43952;44317;44682;45047;45413;45778;46143;46508;46874;47239;47604}

These results spill into the range D5:D16. When these numbers are [formatted as dates](https://exceljet.net/articles/custom-number-formats)
, the final result is a list of 12 dates, one year apart, beginning on May 1, 2019, and ending on May 1, 2030.

### Year only option

It is also possible to use the same approach to create a list of years only, as seen in column F. The formula in cell F5 is:

    =SEQUENCE(12,1,YEAR(B5))
    

SEQUENCE is configured to output 12 years as before. The value for _start_ is provided by the YEAR function:

    =YEAR(B5) // returns 2019
    

Since cell B5 contains the date May 1, 2019, the result is 2019. After YEAR is evaluated, we have:

    =SEQUENCE(12,1,2019)
    

SEQUENCE then returns a list of 12 sequential years beginning in 2019 and incremented by 1:

    {2019;2020;2021;2022;2023;2024;2025;2026;2027;2028;2029;2030}
    

The array lands in cell F5 and values spill into the range F5:F16.

### Legacy Excel

To create a series of dates by year in an older version of Excel, we need to take a different approach, because there is no SEQUENCE function. One option is to use a formula like this:

    =DATE(YEAR(date)+1,MONTH(date),DAY(date))

This formula first extracts the components of a date (year, month, day) with the DAY, MONTH, and YEAR functions. Then it adds 1 to the year value and returns the results to the [DATE function](https://exceljet.net/functions/date-function)
 which creates a new date. To adapt this formula to the worksheet shown, enter this formula in cell D5:

    =B5

_Note: This formula simply pulls in the start date from cell B5. The reason we do this is to maintain the workbook structure, with the start date in cell B5. Once we have the start date in cell D5, all formulas below can reference the "cell above". An alternative would be to simply hardcode the start date into cell D5, but that would leave the start date in B5_ _"orphaned" with no purpose. It's a good example of how the [dynamic array](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 created by SEQUENCE provides a more compact, elegant solution._

Next, in cell D6, enter the formula below:

    =DATE(YEAR(D5)+1,MONTH(D5),DAY(D5))

To solve this formula, Excel first extracts the year, month, and day values from the date in D5, then adds 1 to the year value. Next, a new date is reassembled by the DATE function, using the same day and month, and year + 1 for the year:

    =DATE(YEAR(D5)+1,MONTH(D5),DAY(D5))
    =DATE(2019+1,5,1)
    =DATE(2020,5,1)
    ="01-May-2020"
    

The result in D6 is the date May 1, 2020. As the formula is copied down, it returns a series of dates incremented by one year. The result should look like this:

![Formula for series of years in older versions of Excel](https://exceljet.net/sites/default/files/images/formulas/inline/sequence_of_years_legacy_excel.png "Formula for series of years in older versions of Excel")

 If you only want a list of incremented years, enter this formula in cell D5:

    =YEAR(B5)

Then in cell D6, enter and copy down this formula:

    =D5+1

The result should look like this:

![Formula for series of years only in older versions of Excel](https://exceljet.net/sites/default/files/images/formulas/inline/sequence_of_years_only_legacy_excel.png "Formula for series of years only in older versions of Excel")

You can easily customize this formula if needed. For example, if you need a series of dates where every date is the first day of a new year, you can use a formula like this:

    =DATE(YEAR(date)+1,1,1)
    

Related formulas
----------------

[![Excel formula: Sequence of days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_days.png "Excel formula: Sequence of days")](https://exceljet.net/formulas/sequence-of-days)

### [Sequence of days](https://exceljet.net/formulas/sequence-of-days)

The goal is to generate a series of sequential dates with a formula. In the current version of Excel, the easiest method is to use the SEQUENCE function. SEQUENCE can return all dates at the same time into a range on the worksheet. In older versions of Excel without the SEQUENCE function, you can...

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")](https://exceljet.net/formulas/sequence-of-workdays)

### [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel MONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20month%20function.png "Excel MONTH function")](https://exceljet.net/functions/month-function)

### [MONTH Function](https://exceljet.net/functions/month-function)

The Excel MONTH function extracts the month from a given date as a number between 1 and 12. Use MONTH to extract a month number from a date into a cell, or to feed a month number into another function like the [DATE function](https://exceljet.net/functions/date-function)
.  
 ...

[![Excel DAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_day_function.png "Excel DAY function")](https://exceljet.net/functions/day-function)

### [DAY Function](https://exceljet.net/functions/day-function)

The Excel DAY function returns the day of the month as a number between 1 and 31 from a given date. DAY is commonly combined with the [YEAR function](https://exceljet.net/functions/year-function)
 and [MONTH function](https://exceljet.net/functions/month-function)
 to take apart dates for manipulation, and...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20work%20with%20dates-thumb.png)](https://exceljet.net/videos/how-to-work-with-dates)

### [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)

Excel contains special functions that will let you extract the day, month, and year from a valid date. Let's take a look. Here we have a set of random dates in column B. First, I'll add a formula to column C to pick up the date values in B and format them with the General format, so we can see the...

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
    
*   [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
    
*   [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [MONTH Function](https://exceljet.net/functions/month-function)
    
*   [DAY Function](https://exceljet.net/functions/day-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [How to work with dates](https://exceljet.net/videos/how-to-work-with-dates)
    

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