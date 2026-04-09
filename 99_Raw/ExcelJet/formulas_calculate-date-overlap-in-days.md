# Calculate date overlap in days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-date-overlap-in-days

---

[Skip to main content](https://exceljet.net/formulas/calculate-date-overlap-in-days#main-content)

[](https://exceljet.net/formulas/calculate-date-overlap-in-days#)

*   [Previous](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)
    
*   [Next](https://exceljet.net/formulas/calculate-days-open)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Calculate date overlap in days
==============================

by Dave Bruns · Updated 5 Jul 2024

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Calculate date overlap in days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20date%20overlap%20in%20days.png "Excel formula: Calculate date overlap in days")

Summary
-------

To calculate the number of days between a start and end date that overlap a period of interest with a separate start and end date, you can use a formula based on the MIN and MAX functions and basic date arithmetic. In the example shown, the formula in D5 is:

    =MAX(MIN(date2,C5)-MAX(date1,B5)+1,0)
    

where "date1" (G5) and "date2" (G6) are [named ranges](https://exceljet.net/articles/named-ranges)
 as seen in the worksheet above. As the formula is copied down, it returns the number of days between the start date in column B and the end date in column C that overlap the period between _date1_ (1-Jun-2024) and _date2 (30_\-Jun-2024).

Generic formula
---------------

    =MAX(MIN(date2,end)-MAX(date1,start)+1,0)

Explanation 
------------

In this example, the goal is to create a formula that will calculate the number of days between a start date in column B and an end date in column C that overlap a period defined by date 1 and date 2, which are variables that can be easily changed. You can use a formula like this to do things like:

*   Check if one project overlaps another
*   Check if a project overlaps a planned holiday
*   Check if a task overlaps a period of travel
*   Check for overlapping vacation schedules for team planning

The solution explained below involves sorting out the two sets of start and end dates and then performing basic date arithmetic. For convenience only, the "period of interest" is based on two [named ranges](https://exceljet.net/articles/named-ranges)
: (1) date1 (G5) and date2 (G6). This makes the formula slightly easier to read and write.

### How Excel handles dates

In Excel's date system, [dates are serial numbers](https://exceljet.net/glossary/excel-date)
 beginning on January 1, 1900. January 1, 1900 is 1, January 2, 1900 is 2, and so on. More recent dates are much larger numbers. For example, January 1, 1999 is 36161, and January 1, 2010 is 40179. The table below shows a few examples of dates and their corresponding serial numbers:

| Date | Number |
| --- | --- |
| 1-Jan-1900 | 1   |
| 2-Jan-1900 | 2   |
| 3-Jan-1900 | 3   |
| 1-Jan-1999 | 36161 |
| 1-Jan-2010 | 40179 |
| 1-Jan-2020 | 43831 |

Because dates are just numbers, you can easily calculate durations by subtracting the earlier date from the later date:

    =end-start+1

For example, with a start date of 1-Jun-2004 in cell A1 and an end date of 15-Jun-2024 in cell A2, this formula returns 15:

    =A2-A1+1 // returns 15

Excel evaluates this formula using date serial numbers like this:

    =A2-A1+1
    =45458-45444+1
    =14+1
    =15

Note that we add 1 in a formula like this because we want to include both the start and end dates in the result. When we subtract the start date from the end date, we get the number of days between the dates, excluding the end date itself. By adding 1, we include the end date in the count.

### Calculating overlap in days

As explained above, Excel dates are just large serial numbers, so it is easy to calculate the number of days between two dates. The main challenge in this problem is sorting out the start and end dates so that we can calculate an overlap correctly. We do this with the MIN and MAX functions to avoid a more complex formula based on the IF function. In the example shown, the formula in cell D5, copied down, looks like this:

    =MAX(MIN(date2,C5)-MAX(date1,B5)+1,0)

At a high level, this is just a variant of the formula to calculate the duration in days mentioned above:

    =end-start+1

However, because we have two start dates and two end dates, we need to do a bit more work so that we are subtracting the latest start date from the earliest end date. Working from the inside out, we first calculate an end date:

    MIN(date2,C5)

Here, we use the [MIN function](https://exceljet.net/functions/min-function)
 to find the earlier date between date2 (30-Jun-2024) and the end date in C5 (1-Jul-2024). Effectively, we are calculating the last possible date of the overlapping period because the overlap cannot extend beyond the earlier of these two dates. The result is 30-Jun-2024, since June 30 is earlier than July 1. Next, we calculate a start date like this:

    MAX(date1,B5)

This code uses the [MAX function](https://exceljet.net/functions/max-function)
 to find the later date between date1 (1-Jun-2024) and B5 (1-May-2024). This is the first possible date overlapping period because the overlap cannot start before the later of these two start dates. The result is 1-Jun-2024, since June 1 is later than May 1. Swapping in the values calculated above, we now have:

    =MAX("30-Jun-2024"-"1-Jun-2024"+1,0)

Using Excel's native serial numbers for the dates, subtracting the start date from the end date yields 29. To include both the start and end dates in the count, we add 1, and the final result is 30:

    =MAX(45473-45444+1,0)
    =MAX(29+1,0)
    =MAX(30,0)
    =30

In cases where there is no overlap in dates, the result after subtraction can be negative, so we use MAX function to force any negative numbers to zero.  In other words, we use the MAX function to trap negative values and return zero instead. Using MAX like this is a clever way to avoid using the IF function.

Related formulas
----------------

[![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")](https://exceljet.net/formulas/get-days-between-dates)

### [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)

Dates in Excel are serial numbers that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this: =C6-B6 =...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

### Training

*   [Core Excel](https://exceljet.net/training/core-excel)
    
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