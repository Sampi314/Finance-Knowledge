# Sequence of days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sequence-of-days

---

[Skip to main content](https://exceljet.net/formulas/sequence-of-days#main-content)

[](https://exceljet.net/formulas/sequence-of-days#)

*   [Previous](https://exceljet.net/formulas/sequence-of-custom-days)
    
*   [Next](https://exceljet.net/formulas/sequence-of-leap-years)
    

[Date series](https://exceljet.net/formulas#Date-series)

Sequence of days
================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SEQUENCE](https://exceljet.net/functions/sequence-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7963/download?token=mRk85kta)
 (14.76 KB)

![Excel formula: Sequence of days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sequence_of_days.png "Excel formula: Sequence of days")

Summary
-------

To generate a series of sequential dates, you can use the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. In the example shown, the formula in D5 is:

    =SEQUENCE(B8,1,B5)

The result is a series of 12 dates, beginning on September 1, 2023, the date in cell B5.

_Note: To exclude weekends and/or holidays from the sequence, [see this formula instead](https://exceljet.net/formulas/sequence-of-workdays)
._

Generic formula
---------------

    =SEQUENCE(rows,1,start,step)

Explanation 
------------

The goal is to generate a series of sequential dates with a formula. In the current version of Excel, the easiest method is to use the SEQUENCE function. SEQUENCE can return all dates at the same time into a range on the worksheet. In older versions of Excel without the SEQUENCE function, you can enter a formula, then manually copy the formula down as needed. Both approaches are explained below.

### Background study

*   [How to use the SEQUENCE function](https://exceljet.net/functions/sequence-function)
     \- overview
*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
     - 3 min video
*   [SEQUENCE of dates](https://exceljet.net/videos/sequence-of-dates)
     - 3 min video
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
     - Video training

### SEQUENCE function

The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is a dynamic array function that can generate multiple results. When used by itself on the worksheet, SEQUENCE outputs an array of results that "[spill](https://exceljet.net/glossary/spill)
" onto the worksheet in a "[spill range](https://exceljet.net/glossary/spill-range)
". SEQUENCE can generate numeric sequences in rows, columns, or rows and columns. The generic syntax for the SEQUENCE function looks like this:

    =SEQUENCE(rows,[columns],[start],[step])

_Rows_ is the number of rows to return, _columns_ is the number of columns to return, _start_ is the starting value, and _step_ is the increment to use between values. In this example, the goal is to generate a sequence of 12 dates, starting with the date in cell B5. To generate the dates, the formula in cell D5 is:

    =SEQUENCE(B8,1,B5)
    

The inputs provided to SEQUENCE are as follows:

*   _rows_ - B8 (12)
*   _columns_ - 1
*   _start_ - B5 (1-Sep-2023)
*   _step_ - omitted, defaults to 1

Because [dates in Excel are just serial numbers](https://exceljet.net/glossary/excel-date)
, and the date in B5 is represented by the number 45170 in Excel's date system, SEQUENCE returns an [array](https://exceljet.net/glossary/array)
 that contains 12 large sequential numbers like this:

    {45170;45171;45172;45173;45174;45175;45176;45177;45178;45179;45180;45181}

Each number in this array represents a date, starting with September 1, 2023. The array lands in cell D5 and [spills](https://exceljet.net/glossary/spill)
 into the range D5:D16. When these numbers are [formatted as dates](https://exceljet.net/articles/custom-number-formats)
, they display 12 consecutive dates beginning on September 1, 2023, and ending on September 12, 2023. If the start date in cell B5 is changed, SEQUENCE will automatically return a new set of dates. 

For more details, see [How to use the SEQUENCE function](https://exceljet.net/functions/sequence-function)
.

### All dates between two dates

The formula above generates a set number of dates, provided as the rows argument. To adapt the formula to generate all the dates between two a start date and an end date you can adapt the formula like this:

    SEQUENCE(end-start+1,1,start)

Where the inputs to SEQUENCE are:

*   _rows_ - start date - end date + 1
*   _columns_ - 1
*   _start_ - start date

### Older versions of Excel

In older versions of Excel, there is no SEQUENCE function. However, if you want to generate a sequence of dates with a formula, you can use a generic formula like this:

    =A1+1

Where A1 contains a start date. This works because [dates in Excel are large serial numbers](https://exceljet.net/glossary/excel-date)
 so it is possible to create and manipulate dates with normal math operations. In this formula above, adding 1 to a date entered in cell A1 is the same as adding 1 day. To adapt the SEQUENCE example above to an older version of Excel, enter this formula in cell D5:

    =B5

This formula simply gets the start date in cell B5. Then in D6, enter this formula:

    =D5+1

And copy the formula down as needed. Each subsequent formula creates a new date incremented by one day. One key difference in this approach is that it is not possible to dynamically change the number of dates created as we can with the SEQUENCE function. Instead, the dates must be copied manually.

### Workdays only

The formula above will output will list _all days in the sequence_, including weekends and holidays. To generate a sequence of workdays only, you can use the SEQUENCE function with the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
, as [explained on this page](https://exceljet.net/formulas/sequence-of-workdays)
.

Related formulas
----------------

[![Excel formula: Sequence of months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_months.png "Excel formula: Sequence of months")](https://exceljet.net/formulas/sequence-of-months)

### [Sequence of months](https://exceljet.net/formulas/sequence-of-months)

The goal is to generate a series of dates by month based on a given start date. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE function inside the EDATE function like this: =EDATE(B5,SEQUENCE(12,1,0)) The result is a series of 12 dates, incremented by...

[![Excel formula: Sequence of years](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence%20of%20years.png "Excel formula: Sequence of years")](https://exceljet.net/formulas/sequence-of-years)

### [Sequence of years](https://exceljet.net/formulas/sequence-of-years)

The goal is to generate a series of dates one year apart. In the current version of Excel, the easiest way to do this is with the SEQUENCE function together with the DATE, YEAR, MONTH, and DAY functions. In older versions of Excel, you can use the same date functions and a more manual approach...

[![Excel formula: Sequence of workdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sequence_of_workdays.png "Excel formula: Sequence of workdays")](https://exceljet.net/formulas/sequence-of-workdays)

### [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)

The goal is to generate a dynamic list of sequential working days with a formula. The start date should be a variable input, and weekends and holidays should be automatically excluded from the output. In the current version of Excel, the easiest way to solve this problem is to use the SEQUENCE...

[![Excel formula: List workdays between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list_workdays_between_dates.png "Excel formula: List workdays between dates")](https://exceljet.net/formulas/list-workdays-between-dates)

### [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)

The goal is to list the working days between a start date and an end date. In the simplest form, this means we want to list dates that are Monday, Tuesday, Wednesday, Thursday, or Friday, but exclude dates that are Saturday or Sunday. In addition, we need an option to exclude a list of given...

Related functions
-----------------

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

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

*   [Sequence of months](https://exceljet.net/formulas/sequence-of-months)
    
*   [Sequence of years](https://exceljet.net/formulas/sequence-of-years)
    
*   [Sequence of workdays](https://exceljet.net/formulas/sequence-of-workdays)
    
*   [List workdays between dates](https://exceljet.net/formulas/list-workdays-between-dates)
    

### Functions

*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    

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