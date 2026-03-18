# Sequence of workdays - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sequence-of-workdays

---

[Skip to main content](https://exceljet.net/formulas/sequence-of-workdays#main-content)

[](https://exceljet.net/formulas/sequence-of-workdays#)

*   [Previous](https://exceljet.net/formulas/sequence-of-weekends)
    
*   [Next](https://exceljet.net/formulas/sequence-of-years)
    

[Date series](https://exceljet.net/formulas#Date-series)

Sequence of workdays
====================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)

[ROW](https://exceljet.net/functions/row-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7971/download?token=qLYXhF0s)
 (24.36 KB)

![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")

Summary
-------

To create a list of workdays that exclude weekends and holidays, you can use a formula based on the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 inside the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
. In the example shown, the formula in D5 is:

    =WORKDAY.INTL(B5-1,SEQUENCE(12),1,B8:B11)
    

The result is a series of 12 dates, beginning on September 1, 2023, and ending on September 19, 2023. Notice that weekends and holidays are _not included_ in the result.

_Notes: (1) If you don't need to exclude weekends or holidays,_ [_see this formula_](https://exceljet.net/formulas/sequence-of-days)
_. (2) In older versions of Excel without the SEQUENCE function, you can use a more manual approach as explained below. (3) To generate a list of working days between two dates,_ [_see this formula_](https://exceljet.net/formulas/list-workdays-between-dates)
_._

Generic formula
---------------

    =WORKDAY.INTL(A1-1,SEQUENCE(n),weekend,holidays)

Explanation 
------------

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 inside the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
 like this:

    =WORKDAY.INTL(B5-1,SEQUENCE(12),1,B8:B11)
    

The result is a list of 12 working days, starting on September 1, 2023, and ending on September 19, 2023. Weekends and holidays are omitted from the result. Note that the number of dates to return is hardcoded into the formula as 12. However, this value could easily be exposed on the worksheet as another variable.

In older versions of Excel without the SEQUENCE function, you can use a more manual approach, which is also explained below.

### SEQUENCE function

Working from the inside out, let's look first at the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. SEQUENCE is designed to generate numeric sequences in rows and/or columns. The generic syntax for SEQUENCE looks like this:

    =SEQUENCE(rows,[columns],[start],[step])

In this example, the goal is to generate a sequence of 12 workdays that exclude weekends and holidays. The hard part of this problem is done by the WORKDAY.INTL function (see below), which is designed for this purpose. However, we need a way to ask WORKDAY.INTL to return 12 workdays, and this is where SEQUENCE comes into the picture. We use SEQUENCE inside WORKDAY.INTL to create a value for the _days_ argument like this:

    =SEQUENCE(12)

With the number 12 given for the _rows_ argument, SEQUENCE returns an array that contains 12 numbers starting with 1 and ending with 12:

    {1;2;3;4;5;6;7;8;9;10;11;12}

The other arguments not provided to SEQUENCE (columns, start, and step) all default to 1.

For more details, see [How to use the SEQUENCE function](https://exceljet.net/functions/sequence-function)
.

### WORKDAY.INTL function

The [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
 function takes a date and returns the next workday based on a given offset value provided as the _days_ argument. WORKDAY.INTL will automatically exclude weekends and can optionally exclude dates that are holidays. The generic syntax for WORKDAY.INTL looks like this:

    =WORKDAY.INTL(start_date,days,[weekend],[holidays])

The arguments inside WORKDAY.INTL have the following purpose:

*   _start\_date_ - the date to start from
*   _days_ - the number of days to move forward or back
*   _weekend_ - the weekend scheme to use
*   _holidays_ - dates to be excluded as holidays

The screen below shows the basic operation of WORKDAY.INTL:

![Basic operation of WORKDAY.INTL function](https://exceljet.net/sites/default/files/images/formulas/inline/sequence_of_workdays_basic_workday.intl_operation.png "Basic operation of WORKDAY.INTL function")

In the worksheet shown at the top, we use WORKDAY.INTL with the SEQUENCE function like this:

    =WORKDAY.INTL(B5-1,SEQUENCE(12),1,B8:B11)
    

The inputs provided to WORKDAY.INTL are as follows:

*   _start\_date_ - B5-1 (the day before the start date)
*   _days_ - array created by SEQUENCE
*   _weekend_ - 1 (Saturdays and Sundays)
*   _holidays_ - B8:B11 (dates that are holidays)

With the configuration above, WORKDAY.INTL starts on the day before the start date and calculates 12 workdays using the numbers returned by SEQUENCE as the _days_ argument. After SEQUENCE runs, the formula looks like this:

    =WORKDAY.INTL(B5-1,{1;2;3;4;5;6;7;8;9;10;11;12},1,B8:B11)

You can see now that we are asking WORKDAY.INTL for twelve results: the workday 1 day after the start date, the workday 2 days after the start date, the workday 3 days after the start date, and so on. The reason we start one day before the start date is to force WORKDAY.INTL to evaluate the start date as a potential weekend or holiday so that it can be excluded if necessary.

_Notes: (1) weekend is optional and will default to 1 to exclude Saturdays and Sundays. (2) Holidays is an optional argument and can be omitted. (3) For more details on WORKDAY.INTL, see_ [_How to use the WORKDAY.INTL function_](https://exceljet.net/functions/workday.intl-function)
_._

Legacy Excel
------------

In older versions of Excel, there is no SEQUENCE function. This means we don't have a simple way to calculate 12 workdays all at once. However, one simple solution is to use the WORKDAY.INTL and "drag copy" the formula down as needed. You can see this approach in the screen below. The formula in D6 looks like this:

    =WORKDAY.INTL(D5,1,1,$B$8:$B$11)

![A simple option for older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sequence_of_workdays_legacy_simple.png "A simple option for older versions of Excel")

The inputs to WORKDAY.INTL are as follows:

*   _start\_date_ - D5 (the "cell above")
*   _days_ - 1 (i.e. next workday)
*   _weekend_ - 1 (Saturdays and Sundays)
*   _holidays_ - $B$8:$B$11 (holidays as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
    )

As the formula is copied down, it simply calculates the "next workday" after the date in the row above. If the date in D5 changes, all formulas will recalculate to return valid workdays.

_Notes: (1) The formula in D5 is simply =B5 so that the start date in cell B5 is still functional. (2) One limitation of this formula is that it does not evaluate the start date as a potential non-working day._

### More complete option

It is also possible to generate workdays with a more complex formula that uses the ROW function to determine the number of days to give WORKDAY.INTL. This allows the formula to evaluate the start date and makes it possible to copy the same formula into D5:D16. In the screen below, the formula in cell D5 is:

    =WORKDAY.INTL($B$5-1,ROW()-4,1,$B$8:$B$11)

![Workday formula in older versions of Excel](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sequence_of_workdays_legacy.png "Workday formula in older versions of Excel")

The inputs provided to WORKDAY.INTL are as follows:

*   _start\_date_ - $B$5-1 (the day before the start date)
*   _days_ - ROW()-4 (we subtract 4 to start with 1)
*   _weekend_ - 1 (Saturdays and Sundays)
*   _holidays_ - $B$8:$B$11 (dates that are holidays)

We don't have the SEQUENCE function to generate a value for days, but this approach mimics the same behavior. As before, we first subtract 1 day from the starting date in cell B5. We do this to force WORKDAY.INTL to evaluate the start date as a potential weekend or holiday. To create a value for days, we use the [ROW function](https://exceljet.net/functions/row-function)
 and subtract 4. We subtract 4 because the formula is entered in row 5, and we want to begin with 1. You will need to adjust this value if the formula is entered in a different row. As the formula is copied down, this value will increment.

For _weekend_, we provide 1, which is a code that configures WORKDAY.INTL to exclude Saturdays and Sundays. For holidays, we provide B8:B11, a range that contains dates that should be treated as non-working days. Notice that $B$5 and $B$8:$B$11 are entered as [absolute references](https://exceljet.net/glossary/absolute-reference)
 because we don't want these values to change as the formula is copied. As the formula is copied down, the value returned by ROW() will increase, and each subsequent formula will display the next workday starting from the date in the cell above.

Related formulas
----------------

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

[![Excel formula: Sequence of weekends](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_weekends.png "Excel formula: Sequence of weekends")](https://exceljet.net/formulas/sequence-of-weekends)

### [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)

The goal is to generate a series of sequential weekend days (Saturday and Sunday) with a formula. The start date is entered in cell B5. The number of dates to create (n) is entered in cell B8. If either of these two values are changed, a new list of weekend dates should be generated. In the current...

[![Excel formula: Sequence of custom days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_custom_days.png "Excel formula: Sequence of custom days")](https://exceljet.net/formulas/sequence-of-custom-days)

### [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)

The goal is to generate a series of "custom" days of the week based on a start date entered in cell B5. For example, you might want to list sequential dates for any of the following combinations of days: Mondays, Wednesdays, and Fridays (as shown) Tuesdays, Thursdays, and Saturdays Tuesdays and...

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

[![Excel formula: Sequence of days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_days.png "Excel formula: Sequence of days")](https://exceljet.net/formulas/sequence-of-days)

### [Sequence of days](https://exceljet.net/formulas/sequence-of-days)

The goal is to generate a series of sequential dates with a formula. In the current version of Excel, the easiest method is to use the SEQUENCE function. SEQUENCE can return all dates at the same time into a range on the worksheet. In older versions of Excel without the SEQUENCE function, you can...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel WORKDAY.INTL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20workday.intl%20function.png "Excel WORKDAY.INTL function")](https://exceljet.net/functions/workday.intl-function)

### [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)

The Excel WORKDAY.INTL function returns a date in the future or past that is a given number of working days from a specified start date, excluding weekends and (optionally) holidays. Unlike the simpler [WORKDAY function](https://exceljet.net/functions/workday.intl-function)
, WORKDAY.INTL can be...

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20due%20dates%20with%20WORKDAY_Thumb.png)](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

### [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

In this video we'll look at how to calculate due dates with the WORKDAY and WORKDAY.INTL functions. The WORKDAY function returns a date in the future or past that takes into account weekends and, optionally, holidays. You can use the WORKDAY function to calculate things like ship dates, delivery...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    
*   [Sequence of weekends](https://exceljet.net/formulas/sequence-of-weekends)
    
*   [Sequence of custom days](https://exceljet.net/formulas/sequence-of-custom-days)
    
*   [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [Sequence of days](https://exceljet.net/formulas/sequence-of-days)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [WORKDAY.INTL Function](https://exceljet.net/functions/workday.intl-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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