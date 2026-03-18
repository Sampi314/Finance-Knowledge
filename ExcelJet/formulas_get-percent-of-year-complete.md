# Get percent of year complete - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-percent-of-year-complete

---

[Skip to main content](https://exceljet.net/formulas/get-percent-of-year-complete#main-content)

[](https://exceljet.net/formulas/get-percent-of-year-complete#)

*   [Previous](https://exceljet.net/formulas/get-nth-day-of-year)
    
*   [Next](https://exceljet.net/formulas/get-previous-sunday)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get percent of year complete
============================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[YEARFRAC](https://exceljet.net/functions/yearfrac-function)

[YEAR](https://exceljet.net/functions/year-function)

[DATE](https://exceljet.net/functions/date-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6617/download?token=R_8_m2Ot)
 (13.59 KB)

![Excel formula: Get percent of year complete](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20percent%20of%20year%20complete_0.png "Excel formula: Get percent of year complete")

Summary
-------

To show the amount of time completed in a year as a percentage value, based on any given date, you can use the [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
 together with the [YEAR](https://exceljet.net/functions/year-function)
 and [DATE](https://exceljet.net/functions/date-function)
 functions. In the example shown, the formula in C5, copied down, is:

    =YEARFRAC(DATE(YEAR(B5),1,1),B5)
    

The results in column C are fractional values with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied. 

Generic formula
---------------

    =YEARFRAC(DATE(YEAR(date),1,1),date)

Explanation 
------------

The goal in this example is to return the amount of time completed in a year as a percentage value, based on any given date. In other words, when given the date July 1, 2021, the formula should return 50% since we are halfway\* through the year.

_\*By default, the YEARFRAC function uses a 30/360-day convention, assuming a year contains twelve 30-day months = 360 days. This is controlled by an [optional argument called "basis"](https://exceljet.net/functions/yearfrac-function#basis)
._

The core of the formula is the [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
, which returns the fractional years between two dates as a decimal value. The formula in C5, copied down, is:

    =YEARFRAC(DATE(YEAR(B5),1,1),B5)
    

YEARFRAC takes two dates: a start date and an end date:

    =YEARFRAC(start, end)
    

We calculate the start date with the [DATE function](https://exceljet.net/functions/date-function)
 and [YEAR function](https://exceljet.net/functions/year-function)
 like this:

    DATE(YEAR(B5),1,1) // returns first of year
    

The YEAR function extracts the year from the date in B5:

    YEAR(B5) // returns 2021
    

The number is returned directly to the DATE function with the number "1" hard-coded for both month and day [arguments](https://exceljet.net/glossary/function-argument)
:

    =DATE(2021,1,1) // returns 1-Jan-2021
    

The end date is the date given in column B. With January 15, 2021, in B5, the formula is evaluated like this:

    =YEARFRAC(DATE(YEAR(B5),1,1),B5)
    =YEARFRAC(DATE(2021,1,1),B5)
    =YEARFRAC(44197,44211)
    =0.0388888888888889
    =4%
    

_Note: the large serial numbers in Step 3 above are [Excel dates](https://exceljet.net/glossary/excel-date)
 in their raw format._

The [YEARFRAC function](https://exceljet.net/functions/yearfrac-function)
 returns the decimal value 0.0388888888888889. Then this value is formatted with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 which displays as a percentage.

### Current year and date

To return the percent of the year completed based on the current year and current date, you can adjust the formula to use the [TODAY function](https://exceljet.net/functions/today-function)
 like this:

    =YEARFRAC(DATE(YEAR(TODAY()),1,1),TODAY())
    

In this version, the TODAY function returns the current date which goes into YEARFRAC twice – once as the start date, and once as the end date. Note the start date uses the [DATE function](https://exceljet.net/functions/date-function)
 to create a date for the first of the year, by hard-coding the number 1 for month and day and extracting the current year with the [YEAR function](https://exceljet.net/functions/year-function)
. The result is the percentage of the year completed through as of today. This percentage will continually update over time.

### Percent of the year remaining

To calculate the percent of the year remaining instead of the percent complete, you can adjust the formula to subtract the fractional year from "1". In the example shown, D5 contains this formula copied down:

    =1-YEARFRAC(DATE(YEAR(B5),1,1),B5)
    

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 35% is read as "thirty-five percent" and is equivalent to 35/100 or 0.35. Accordingly, the values in columns C and D are _decimal values_ with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Related formulas
----------------

[![Excel formula: Get days between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20days%20between%20dates.png "Excel formula: Get days between dates")](https://exceljet.net/formulas/get-days-between-dates)

### [Get days between dates](https://exceljet.net/formulas/get-days-between-dates)

Dates in Excel are serial numbers that start on 1/1/1900, which is represented by the number 1. In the example shown, the formula in cell D6 simply subtracts the numeric value of 1/1/1999 (36161) from the numeric value of 1/1/2000 (36526) to get a result of 365. The steps look like this: =C6-B6 =...

[![Excel formula: Calculate years between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Calculate_years_between_dates.png "Excel formula: Calculate years between dates")](https://exceljet.net/formulas/calculate-years-between-dates)

### [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)

In this example, the goal is to calculate the number of years between a start date in column B and an end date in column C. An easy way to solve this problem is to use the YEARFRAC function, which returns the number of years between any two dates as a decimal number. YEARFRAC function The YEARFRAC...

[![Excel formula: Get amount with percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20amount%20with%20percent_0.png "Excel formula: Get amount with percentage")](https://exceljet.net/formulas/get-amount-with-percentage)

### [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)

In this example, the goal is to convert the percentages shown in column C to amounts, where the total of all amounts is given as $1945. In other words, if we know Rent is 36.0%, and the total of all expenses is $1945, we want to calculate that Rent is $700. With "x" as the number we want to find,...

[![Excel formula: Project complete percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/project%20complete%20percentage_0.png "Excel formula: Project complete percentage")](https://exceljet.net/formulas/project-complete-percentage)

### [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)

In this example if a task is marked "Done", then it is considered complete. The goal is to calculate the percent complete for the project by showing the ratio of complete tasks to total tasks, expressed as a percentage. The formula in F6 is: =COUNTA(C5:C11)/COUNTA(B5:B11) At the core, this formula...

[![Excel formula: Percent of goal](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20goal.png "Excel formula: Percent of goal")](https://exceljet.net/formulas/percent-of-goal)

### [Percent of goal](https://exceljet.net/formulas/percent-of-goal)

In this example, the objective is to calculate a percentage for each goal shown in column C of the table using the actual values in column D. In other words, given a goal of 100000, and an actual amount of 112000, we want to return 112% as the result. The general formula for this calculation, where...

[![Excel formula: Percent of students absent](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/percent%20of%20students%20absent.png "Excel formula: Percent of students absent")](https://exceljet.net/formulas/percent-of-students-absent)

### [Percent of students absent](https://exceljet.net/formulas/percent-of-students-absent)

In this example, the goal is to answer the question "What percentage of students were absent from each class". In other words, given a class with 30 students total, 27 of which were present, we want to return 10% absent. The general formula for this calculation, where "x" is the percent absent is:...

Related functions
-----------------

[![Excel YEARFRAC function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/excel_yearfrac_function.png "Excel YEARFRAC function")](https://exceljet.net/functions/yearfrac-function)

### [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)

The Excel YEARFRAC function returns a decimal value that represents fractional years between two dates. You can use YEARFRAC to do things like calculate age with a birthdate....

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

[![Excel DATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20date.png "Excel DATE function")](https://exceljet.net/functions/date-function)

### [DATE Function](https://exceljet.net/functions/date-function)

The Excel DATE function creates a valid date from individual year, month, and day components. The DATE function is useful for assembling dates that need to change dynamically based on other values in a worksheet.

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
    
*   [Calculate years between dates](https://exceljet.net/formulas/calculate-years-between-dates)
    
*   [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)
    
*   [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)
    
*   [Percent of goal](https://exceljet.net/formulas/percent-of-goal)
    
*   [Percent of students absent](https://exceljet.net/formulas/percent-of-students-absent)
    

### Functions

*   [YEARFRAC Function](https://exceljet.net/functions/yearfrac-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    
*   [DATE Function](https://exceljet.net/functions/date-function)
    

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